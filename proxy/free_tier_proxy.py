"""
Free Tier Auto-Rotator & Circuit Breaker Proxy for Wyvern
Version: 1.6.0 (Non-Destructive PayloadCompactor, Loopback 127.0.0.1, Multi-Provider Auto-Rotator)
"""

import os
import re
import sys
import time
import json
import copy
import logging
from typing import Dict, Any, List, Optional, Tuple, Set
import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse

try:
    from dotenv import load_dotenv

    _proxy_dir = os.path.dirname(os.path.abspath(__file__))
    _repo_root = os.path.dirname(_proxy_dir)
    for _env_path in (
        os.path.join(_proxy_dir, ".env"),
        os.path.join(_repo_root, ".env"),
    ):
        if os.path.exists(_env_path):
            load_dotenv(_env_path)
except ImportError:
    pass

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

LOG_FILE = os.path.join(os.path.dirname(__file__), "proxy_debug.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)
logger = logging.getLogger("FreeTierProxy")

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config_free_proxy.json")
_cached_config: Dict[str, Any] = {}
_last_mtime: float = 0.0


def get_config() -> Dict[str, Any]:
    global _cached_config, _last_mtime
    try:
        if os.path.exists(CONFIG_PATH):
            mtime = os.path.getmtime(CONFIG_PATH)
            if mtime != _last_mtime:
                with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                    _cached_config = json.load(f)
                _last_mtime = mtime
                logger.info(
                    "🔄 [CONFIG] Configurazione ricaricata con successo (Hot-Reload)."
                )
    except Exception as e:
        logger.error(f"Errore lettura configurazione: {e}")
    return _cached_config


app = FastAPI(title="Wyvern Free Tier Failover Proxy v1.6.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_private_network=True,
)


@app.middleware("http")
async def add_pna_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response

# Cooldown granulare per combinazione (upstream_id + model + key_suffix)
cooldowns: Dict[str, float] = {}


def make_cd_key(uid: str, model: str, api_key: str) -> str:
    suffix = api_key[-6:] if api_key else "nokey"
    return f"{uid}::{model}::{suffix}"


def is_available(cd_key: str) -> bool:
    return time.time() > cooldowns.get(cd_key, 0.0)


def mark_cooldown(
    cd_key: str, label: str, reason: str, duration: Optional[float] = None
):
    cfg = get_config()
    cooldown_sec = duration or cfg.get("cooldown_seconds", 60)
    cooldowns[cd_key] = time.time() + cooldown_sec
    logger.warning(
        f"❌ [COOLDOWN] {label} in quarantena per {cooldown_sec}s. Motivo: {reason}"
    )


def resolve_keys(key_name: str, incoming_auth: Optional[str]) -> List[str]:
    cfg = get_config()
    val = cfg.get("keys", {}).get(key_name)
    keys: List[str] = []
    if isinstance(val, list):
        keys = [k.strip() for k in val if k and k.strip()]
    elif isinstance(val, str) and val.strip():
        keys = [val.strip()]

    env_candidates = [f"{key_name.upper()}_API_KEY"]
    if key_name == "google_ai_studio":
        env_candidates.extend(["GEMINI_API_KEY", "GOOGLE_API_KEY"])
    elif key_name == "zhipu":
        env_candidates.extend(["BIGMODEL_API_KEY", "GLM_API_KEY"])
    elif key_name == "siliconflow":
        env_candidates.extend(["SILICON_API_KEY"])
    elif key_name == "github":
        env_candidates.extend(["GITHUB_TOKEN", "AZURE_INFERENCE_CREDENTIAL"])
    elif key_name == "cloudflare":
        env_candidates.extend(["CLOUDFLARE_API_TOKEN"])

    for env_var in env_candidates:
        env_key = os.environ.get(env_var, "").strip()
        if env_key and env_key not in keys:
            keys.append(env_key)

    if incoming_auth and incoming_auth.startswith("Bearer "):
        token = incoming_auth[7:].strip()
        if (
            token
            and not token.startswith("sk-dummy")
            and token != "local"
            and token not in keys
        ):
            keys.append(token)
    return keys


class PayloadCompactor:
    """
    Generalized, Non-Destructive Payload Compactor for Wyvern Chat Completions.
    Executes a 5-phase optimization pipeline:
      Phase 1: Parameter Sanitization (penalties, top_k, max_tokens, stop sequences)
      Phase 2: XML Lore Deduplication (<npc>, <location>, <item>, <creature>, <lore_entry>)
      Phase 3: Active Character Cross-Deduplication (remove duplicate NPC dossiers in world_context)
      Phase 4: Empty Tag & Attribute Pruning (<special_stats></special_stats>, labels="")
      Phase 5: Whitespace & Newline Collapsing (collapse 3+ newlines, strip trailing whitespace, merge consecutive roles)
    Guarantees Zero Semantic Loss.
    """

    LORE_TAGS = ("npc", "location", "item", "creature", "lore_entry")

    def deep_copy_payload(self, body: Dict[str, Any]) -> Dict[str, Any]:
        """Deep-copies the request body upfront to prevent in-place mutation during failover retries."""
        return copy.deepcopy(body)

    def sanitize_parameters(
        self,
        body: Dict[str, Any],
        provider: Optional[str] = None,
        target_model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Phase 1: Parameter Sanitization.
        Strips unsupported sampling penalties, fixes top_k, clamps max_tokens, cleans stop sequences.
        """
        # Frequency and presence penalties
        if body.get("frequency_penalty") == 0 or body.get("frequency_penalty") == 0.0:
            body.pop("frequency_penalty", None)
        if body.get("presence_penalty") == 0 or body.get("presence_penalty") == 0.0:
            body.pop("presence_penalty", None)

        if (
            provider
            in (
                "google",
                "sambanova",
                "groq",
                "nvidia",
                "cloudflare",
                "zhipu",
                "github",
                "cerebras",
                "mistral",
                "siliconflow",
            )
            or (target_model and "r1" in target_model.lower())
        ):
            body.pop("frequency_penalty", None)
            body.pop("presence_penalty", None)

        # top_k handling
        if provider == "chutes":
            body["top_k"] = -1
        else:
            top_k = body.get("top_k")
            if top_k is None or (isinstance(top_k, (int, float)) and top_k <= 0):
                body.pop("top_k", None)

        # max_tokens clamping
        max_tokens = body.get("max_tokens")
        if isinstance(max_tokens, (int, float)):
            if provider == "google" and max_tokens > 8192:
                body["max_tokens"] = 8192
            elif (
                provider
                in (
                    "openrouter",
                    "groq",
                    "cerebras",
                    "sambanova",
                    "mistral",
                    "zhipu",
                    "github",
                    "siliconflow",
                    "nvidia",
                    "cloudflare",
                )
                and max_tokens > 8192
            ):
                body["max_tokens"] = 8192

        # stop sequences cleanup (remove \nNarrator: and variants to avoid truncations)
        if "stop" in body:
            stop_val = body["stop"]
            if isinstance(stop_val, list):
                cleaned_stop = [
                    s
                    for s in stop_val
                    if isinstance(s, str) and "narrator" not in s.lower()
                ]
                if cleaned_stop:
                    body["stop"] = cleaned_stop
                else:
                    body.pop("stop", None)
            elif isinstance(stop_val, str):
                if "narrator" in stop_val.lower():
                    body.pop("stop", None)

        if target_model:
            body["model"] = target_model

        return body

    def deduplicate_xml_lore(
        self, messages: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], int]:
        """
        Phase 2: Generic XML Lore Deduplication.
        Deduplicates <npc>, <location>, <item>, <creature>, <lore_entry> by tag and normalized name.
        """
        seen_lore: Set[Tuple[str, str]] = set()
        chars_saved = 0
        new_messages = []

        lore_tag_re = re.compile(
            r'<(?P<tag>npc|location|item|creature|lore_entry)\b(?P<attrs>[^>]*)>(?P<content>.*?)</(?P=tag)>\s*',
            flags=re.DOTALL | re.IGNORECASE,
        )

        for msg in messages:
            content = msg.get("content")
            if not isinstance(content, str):
                new_messages.append(msg)
                continue

            def _dedup_replacer(m: re.Match) -> str:
                nonlocal chars_saved
                tag = m.group("tag").lower()
                attrs = m.group("attrs")
                inner = m.group("content")

                # Extract normalized name
                name_m = re.search(
                    r'\b(?:name|title|id)\s*=\s*["\']([^"\']+)["\']',
                    attrs,
                    re.IGNORECASE,
                )
                if name_m:
                    norm_name = name_m.group(1).strip().lower()
                else:
                    jed_m = re.search(r'\[NAME:\s*([^;\]]+)', inner, re.IGNORECASE)
                    if jed_m:
                        norm_name = jed_m.group(1).strip().lower()
                    else:
                        norm_name = inner.strip()[:80].lower()

                key = (tag, norm_name)
                if key in seen_lore:
                    chars_saved += len(m.group(0))
                    return ""
                seen_lore.add(key)
                return m.group(0)

            compressed = lore_tag_re.sub(_dedup_replacer, content)
            new_messages.append({**msg, "content": compressed})

        return new_messages, chars_saved

    def cross_deduplicate_active_characters(
        self, messages: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], int]:
        """
        Phase 3: Active Character Cross-Deduplication.
        Extracts active character names loaded in <character name="..."> or <user_persona name="...">,
        and removes redundant duplicate NPC dossiers in <world_context> or system prompt.
        """
        active_names: Set[str] = set()
        chars_saved = 0

        # Step 3.1: Discover active characters across all messages
        char_tag_re = re.compile(
            r'<(?:character|user_persona|persona)\b(?P<attrs>[^>]*)>(?P<content>.*?)</(?:character|user_persona|persona)>',
            flags=re.DOTALL | re.IGNORECASE,
        )
        for msg in messages:
            content = msg.get("content")
            if not isinstance(content, str):
                continue
            for m in char_tag_re.finditer(content):
                attrs = m.group("attrs")
                inner = m.group("content")
                name_m = re.search(
                    r'\bname\s*=\s*["\']([^"\']+)["\']', attrs, re.IGNORECASE
                )
                if name_m:
                    raw_n = name_m.group(1).strip().lower()
                    active_names.add(raw_n)
                    parts = raw_n.split()
                    if parts and len(parts[0]) >= 3:
                        active_names.add(parts[0])
                jed_m = re.search(r'\[NAME:\s*([^;\]]+)', inner, re.IGNORECASE)
                if jed_m:
                    raw_n = jed_m.group(1).strip().lower()
                    active_names.add(raw_n)
                    parts = raw_n.split()
                    if parts and len(parts[0]) >= 3:
                        active_names.add(parts[0])

        standalone_name_re = re.compile(
            r'<(?:character|user_persona|persona)\b[^>]*\bname\s*=\s*["\']([^"\']+)["\']',
            re.IGNORECASE,
        )
        for msg in messages:
            content = msg.get("content")
            if isinstance(content, str):
                for m in standalone_name_re.finditer(content):
                    raw_n = m.group(1).strip().lower()
                    active_names.add(raw_n)
                    parts = raw_n.split()
                    if parts and len(parts[0]) >= 3:
                        active_names.add(parts[0])

        if not active_names:
            return messages, 0

        def is_active_character_name(name_str: str) -> bool:
            clean = name_str.strip().lower()
            if not clean:
                return False
            if clean in active_names:
                return True
            tokens = clean.split()
            if tokens and len(tokens[0]) >= 3 and tokens[0] in active_names:
                return True
            for act in active_names:
                if clean.startswith(act + " ") or act.startswith(clean + " "):
                    return True
            return False

        # Step 3.2: Filter out duplicate <npc ...> blocks when character is already active
        npc_tag_re = re.compile(
            r'<npc\b(?P<attrs>[^>]*)>(?P<content>.*?)</npc>\s*',
            flags=re.DOTALL | re.IGNORECASE,
        )

        new_messages = []
        for msg in messages:
            content = msg.get("content")
            if not isinstance(content, str):
                new_messages.append(msg)
                continue

            def _npc_filter(m: re.Match) -> str:
                nonlocal chars_saved
                attrs = m.group("attrs")
                inner = m.group("content")

                name_m = re.search(
                    r'\bname\s*=\s*["\']([^"\']+)["\']', attrs, re.IGNORECASE
                )
                if name_m:
                    npc_name = name_m.group(1).strip()
                else:
                    jed_m = re.search(r'\[NAME:\s*([^;\]]+)', inner, re.IGNORECASE)
                    npc_name = jed_m.group(1).strip() if jed_m else ""

                if npc_name and is_active_character_name(npc_name):
                    chars_saved += len(m.group(0))
                    return ""
                return m.group(0)

            compressed = npc_tag_re.sub(_npc_filter, content)

            # Step 3.3: Handle legacy <PrimaryPool> blocks if present
            if "<PrimaryPool>" in compressed and "</PrimaryPool>" in compressed:

                def _pool_filter(m: re.Match) -> str:
                    nonlocal chars_saved
                    tag_name = m.group(1)
                    if tag_name.lower() in (
                        "users",
                        "partystate",
                        "partycharacters",
                        "outfit",
                        "appearance",
                    ):
                        return m.group(0)
                    if is_active_character_name(tag_name):
                        chars_saved += len(m.group(0))
                        return ""
                    return m.group(0)

                compressed = re.sub(
                    r"<([A-Za-zÀ-ÿ0-9_ -]+)>\n\[NAME:.*?</\1>\s*",
                    _pool_filter,
                    compressed,
                    flags=re.DOTALL,
                )

            new_messages.append({**msg, "content": compressed})

        return new_messages, chars_saved

    def strip_redundant_comments_and_format(
        self, messages: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], int]:
        """
        Phase 4a: Stripping of HTML/XML comments, Windows CRLF normalization,
        and redundant XML formatting injected by Wyvern or templating engines.
        Preserves strictly all JED+ attribute blocks and quoted dialogue.
        """
        new_messages = []
        chars_saved = 0
        comment_re = re.compile(r"<!--.*?-->", flags=re.DOTALL)
        crlf_re = re.compile(r"\r\n")

        for msg in messages:
            content = msg.get("content")
            if not isinstance(content, str):
                new_messages.append(msg)
                continue

            init_len = len(content)
            # 1. Normalize line endings to avoid double byte CRLF
            text = crlf_re.sub("\n", content)
            # 2. Strip non-functional HTML/XML comments
            text = comment_re.sub("", text)
            # 3. Collapse multiple spaces between XML tags: >   < -> >\n<
            text = re.sub(r">\s{2,}<", ">\n<", text)

            chars_saved += init_len - len(text)
            new_messages.append({**msg, "content": text})

        return new_messages, chars_saved

    def prune_empty_tags_and_attributes(
        self, messages: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], int]:
        """
        Phase 4b: Empty Tag & Attribute Pruning.
        Removes <special_stats></special_stats>, empty elements, and empty attributes like labels="".
        """
        new_messages = []
        chars_saved = 0
        empty_attr_re = re.compile(
            r'\s+(?:labels|type|description|category|role|class)=["\']\s*["\']'
        )
        empty_tag_re = re.compile(r'<([a-zA-Z0-9_-]+)(?:\s+[^>]*)?>\s*</\1>\s*')

        for msg in messages:
            content = msg.get("content")
            if not isinstance(content, str):
                new_messages.append(msg)
                continue

            init_len = len(content)
            text = empty_attr_re.sub("", content)

            # Up to 3 passes for nested empty tags
            for _ in range(3):
                new_text = empty_tag_re.sub("", text)
                if new_text == text:
                    break
                text = new_text

            chars_saved += init_len - len(text)
            new_messages.append({**msg, "content": text})

        return new_messages, chars_saved

    def collapse_whitespace(
        self, messages: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], int]:
        """
        Phase 5: Whitespace and Newline Collapsing.
        Collapses 3+ newlines to 2, strips trailing line whitespace, normalizes XML boundaries,
        compacts JED+ PList punctuation spaces, and merges consecutive identical roles.
        """
        new_messages = []
        chars_saved = 0

        for msg in messages:
            content = msg.get("content")
            if not isinstance(content, str):
                new_messages.append(msg)
                continue

            init_len = len(content)
            text = content

            # Tag boundary whitespace normalization (> \n\n < -> >\n<)
            text = re.sub(
                r'(</?[a-zA-Z0-9_-]+[^>]*>)[ \t]*\n[ \t]*\n+(?=[ \t]*</?[a-zA-Z0-9_-]+[^>]*>)',
                r"\1\n",
                text,
            )
            text = re.sub(
                r'(</?[a-zA-Z0-9_-]+[^>]*>)[ \t]*\n[ \t]*(</?[a-zA-Z0-9_-]+[^>]*>)',
                r"\1\n\2",
                text,
            )

            # Normalize JED+ PList spacing (e.g. ';   ' -> '; ', '[   ' -> '[')
            text = re.sub(r";[ \t]{2,}", "; ", text)
            text = re.sub(r"\[[ \t]+", "[", text)
            text = re.sub(r"[ \t]+\]", "]", text)

            # Collapse 3+ newlines to 2 (preserves markdown paragraphs)
            text = re.sub(r"\n{3,}", "\n\n", text)

            # Strip trailing whitespace on each line
            text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)

            # Strip leading/trailing whitespaces of message
            text = text.strip()

            chars_saved += init_len - len(text)
            new_messages.append({**msg, "content": text})

        # Merge consecutive messages with identical roles (user/user or system/system)
        merged: List[Dict[str, Any]] = []
        for m in new_messages:
            role = m.get("role", "user")
            content = m.get("content", "")
            if (
                merged
                and merged[-1].get("role") == role
                and role in ("user", "system")
                and isinstance(content, str)
                and isinstance(merged[-1].get("content"), str)
            ):
                prev = merged[-1]["content"]
                merged[-1]["content"] = f"{prev}\n\n{content}"
            else:
                merged.append(dict(m))

        # Filter out empty messages if more than one message exists
        filtered = [
            m
            for m in merged
            if (isinstance(m.get("content"), str) and m["content"]) or len(merged) == 1
        ]

        return filtered, chars_saved

    def compact_request_payload(
        self,
        body: Dict[str, Any],
        provider: Optional[str] = None,
        target_model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Executes the full 5-phase compaction pipeline on a deep copy of the request payload.
        Safe for failover retries; original input is NEVER modified in-place.
        """
        payload = self.deep_copy_payload(body)

        # Phase 1: Parameter Sanitization
        payload = self.sanitize_parameters(
            payload, provider=provider, target_model=target_model
        )

        # Prompt Compaction (Phases 2-5)
        if "messages" in payload and isinstance(payload["messages"], list):
            msgs = payload["messages"]
            before_chars = sum(
                len(m.get("content", ""))
                for m in msgs
                if isinstance(m.get("content"), str)
            )

            # Phase 2: XML Lore Deduplication
            msgs, saved_p2 = self.deduplicate_xml_lore(msgs)

            # Phase 3: Active Character Cross-Deduplication
            msgs, saved_p3 = self.cross_deduplicate_active_characters(msgs)

            # Phase 4a: Comments & CRLF Stripping
            msgs, saved_p4a = self.strip_redundant_comments_and_format(msgs)

            # Phase 4b: Empty Tag & Attribute Pruning
            msgs, saved_p4 = self.prune_empty_tags_and_attributes(msgs)

            # Phase 5: Whitespace & Newline Collapsing
            msgs, saved_p5 = self.collapse_whitespace(msgs)

            payload["messages"] = msgs

            after_chars = sum(
                len(m.get("content", ""))
                for m in msgs
                if isinstance(m.get("content"), str)
            )
            total_saved = before_chars - after_chars
            if total_saved > 0:
                pct = (total_saved / before_chars) * 100 if before_chars > 0 else 0
                logger.info(
                    f"✨ [COMPACT] Payload compattato: -{total_saved} chars (-{pct:.1f}%). "
                    f"[P2 lore dedup: {saved_p2}, P3 active char dedup: {saved_p3}, P4a comments: {saved_p4a}, P4b empty prune: {saved_p4}, P5 whitespace: {saved_p5}]"
                )

        return payload

    def prepare_for_provider(
        self,
        compacted_base: Dict[str, Any],
        provider: str,
        target_model: str,
    ) -> Dict[str, Any]:
        """
        Applies provider-specific parameter adjustments to an already-compacted base payload.
        Fast and non-destructive.
        """
        req_body = self.deep_copy_payload(compacted_base)
        return self.sanitize_parameters(
            req_body, provider=provider, target_model=target_model
        )

    def compact(
        self,
        body: Dict[str, Any],
        provider: Optional[str] = None,
        target_model: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Direct entry point for full compaction."""
        return self.compact_request_payload(
            body, provider=provider, target_model=target_model
        )


def deduplicate_wyvern_prompt(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Backwards-compatible helper delegating to PayloadCompactor."""
    compactor = PayloadCompactor()
    msgs, _ = compactor.deduplicate_xml_lore(messages)
    msgs, _ = compactor.cross_deduplicate_active_characters(msgs)
    return msgs


def sanitize_request_body(
    body: Dict[str, Any], provider: str, target_model: str
) -> Dict[str, Any]:
    """Backwards-compatible helper delegating to PayloadCompactor."""
    compactor = PayloadCompactor()
    return compactor.compact(body, provider=provider, target_model=target_model)


def validate_and_normalize_response(
    raw_bytes: bytes, target_model: str
) -> Tuple[bool, Dict[str, Any], str]:
    """
    Controlla che il JSON restituito dall'upstream contenga testo valido e lo normalizza
    nello schema rigoroso choices[0].message.content richiesto da WyvernChat.
    """
    if not raw_bytes:
        return False, {}, "Corpo risposta HTTP vuoto (0 byte)"

    try:
        data = json.loads(raw_bytes)
    except Exception as e:
        return False, {}, f"JSON non valido: {e}"

    if "error" in data and not data.get("choices"):
        err_msg = (
            data["error"].get("message")
            if isinstance(data["error"], dict)
            else str(data["error"])
        )
        return False, data, f"Errore upstream nel payload 200: {err_msg}"

    choices = data.get("choices", [])
    if not choices or not isinstance(choices, list):
        return False, data, "Lista 'choices' assente o vuota"

    choice0 = choices[0] if isinstance(choices[0], dict) else {}
    msg_obj = choice0.get("message") if isinstance(choice0.get("message"), dict) else {}

    # Estrae il testo da message.content o fallback su choice0.text
    content_text = msg_obj.get("content")
    if content_text is None:
        content_text = choice0.get("text")

    reasoning_text = (
        msg_obj.get("reasoning_content")
        or msg_obj.get("reasoning")
        or choice0.get("reasoning")
        or ""
    )

    finish_reason = (
        choice0.get("finish_reason") or choice0.get("native_finish_reason") or "stop"
    )

    # Se content_text è vuoto ma il modello ha scritto solo in reasoning_content (senza tag di risposta),
    # rifiuta per far scattare il failover verso un modello che risponda davvero alla scena.
    if not content_text or not str(content_text).strip():
        return (
            False,
            data,
            f"Risposta con testo vuoto (finish_reason={finish_reason}, reasoning_len={len(str(reasoning_text))})",
        )

    # Costruisce una risposta OpenAI Chat Completion standardizzata al 100%
    normalized = {
        "id": data.get("id") or f"chatcmpl-{int(time.time())}",
        "object": "chat.completion",
        "created": data.get("created") or int(time.time()),
        "model": data.get("model") or target_model,
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": str(content_text)},
                "finish_reason": finish_reason,
            }
        ],
        "usage": data.get("usage")
        or {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
    }
    return True, normalized, "OK"


@app.get("/health")
async def health_check():
    cfg = get_config()
    return {"status": "ok", "active_cooldowns": len(cooldowns), "log_file": LOG_FILE}


@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "free-tier-master",
                "object": "model",
                "created": 1749000000,
                "owned_by": "wyvern-proxy",
                "context_length": 1000000,
            }
        ],
    }


@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    cfg = get_config()
    body = await request.json()
    is_streaming = body.get("stream", False)
    incoming_auth = request.headers.get("authorization")

    # Upfront non-destructive compaction executed once before retry loop
    compactor = PayloadCompactor()
    compacted_base = compactor.compact_request_payload(body)

    upstreams = sorted(cfg.get("upstreams", []), key=lambda x: x.get("priority", 99))
    cfg_timeout = float(cfg.get("timeout_seconds", 35.0))
    timeout_sec = max(cfg_timeout, 40.0) if not is_streaming else max(cfg_timeout, 25.0)

    last_error = "Nessun modello disponibile"

    for upstream in upstreams:
        uid = upstream.get("id", "unknown-upstream")
        name = upstream.get("display_name", uid)
        priority = upstream.get("priority", 99)
        provider = upstream.get("provider", "generic")

        key_name = upstream.get("key_name") or ("openrouter" if provider == "openrouter" else "")
        available_keys = resolve_keys(key_name, incoming_auth)
        if not available_keys:
            logger.warning(
                f"⚠️  [SALTATO] P{priority} ({name}): Nessuna chiave per {key_name}."
            )
            continue

        target_url = upstream.get("base_url")
        if not target_url and upstream.get("api_base"):
            target_url = upstream["api_base"].rstrip("/") + "/chat/completions"
        if not target_url:
            logger.warning(f"⚠️  [SALTATO] P{priority} ({name}): Nessun URL base configurato.")
            continue

        models_to_try = upstream.get("models") or ([upstream.get("model")] if upstream.get("model") else [])

        for api_key in available_keys:
            for target_model in models_to_try:
                cd_key = make_cd_key(uid, target_model, api_key)
                label = f"P{priority} {name} [{target_model}]"

                if not is_available(cd_key):
                    rem = round(cooldowns[cd_key] - time.time())
                    logger.info(
                        f"⏭️  [SALTATO] {label} in cooldown ({rem}s rimanenti)..."
                    )
                    continue

                req_body = compactor.prepare_for_provider(
                    compacted_base, provider, target_model
                )

                headers = {
                    "Content-Type": "application/json",
                    "Accept": (
                        "text/event-stream" if is_streaming else "application/json"
                    ),
                    "User-Agent": "Wyvern-FreeTierProxy/1.6",
                }
                if api_key:
                    headers["Authorization"] = f"Bearer {api_key}"
                if provider == "openrouter":
                    headers["HTTP-Referer"] = "https://app.wyvern.chat"
                    headers["X-Title"] = "WyvernChat"
                if upstream.get("headers") and isinstance(upstream["headers"], dict):
                    headers.update(upstream["headers"])

                logger.info(
                    f"🚀 [ROUTING] Tentativo {label} (stream={is_streaming}, timeout={timeout_sec}s)..."
                )

                client_timeout = httpx.Timeout(timeout_sec, connect=10.0)
                client = httpx.AsyncClient(timeout=client_timeout)

                try:
                    req = client.build_request(
                        "POST", target_url, headers=headers, json=req_body
                    )
                    response = await client.send(req, stream=is_streaming)

                    if response.status_code != 200:
                        err_bytes = await response.aread()
                        err_str = err_bytes.decode("utf-8", errors="ignore")[:250]
                        last_error = (
                            f"{label} -> HTTP {response.status_code}: {err_str}"
                        )

                        if (
                            response.status_code in (429, 402, 403)
                            or response.status_code >= 500
                        ):
                            mark_cooldown(
                                cd_key,
                                label,
                                f"HTTP {response.status_code}: {err_str[:80]}",
                            )
                        else:
                            logger.warning(f"⚠️  [RIFIUTATO] {last_error}")

                        await response.aclose()
                        await client.aclose()
                        continue

                    # Gestione STREAMING
                    if is_streaming:
                        logger.info(f"✅ [STREAM START] Connesso a {label}!")

                        async def stream_generator():
                            try:
                                async for chunk in response.aiter_bytes():
                                    yield chunk
                            finally:
                                await response.aclose()
                                await client.aclose()

                        return StreamingResponse(
                            stream_generator(),
                            status_code=200,
                            media_type="text/event-stream",
                            headers={
                                "Cache-Control": "no-cache",
                                "Connection": "keep-alive",
                                "X-Served-By": f"{name} ({target_model})",
                            },
                        )

                    # Gestione NON-STREAMING (Valida che non sia {"text": ""} prima di accettarla!)
                    raw_bytes = await response.aread()
                    await response.aclose()
                    await client.aclose()

                    is_valid, normalized_json, reason = validate_and_normalize_response(
                        raw_bytes, target_model
                    )
                    if not is_valid:
                        last_error = f"{label} -> {reason}"
                        mark_cooldown(cd_key, label, reason, duration=30)
                        continue

                    logger.info(
                        f"✅ [SUCCESS] Risposta valida ({len(normalized_json['choices'][0]['message']['content'])} chars) da {label}!"
                    )
                    return JSONResponse(
                        content=normalized_json,
                        status_code=200,
                        headers={"X-Served-By": f"{name} ({target_model})"},
                    )

                except (httpx.TimeoutException, httpx.ConnectTimeout) as te:
                    last_error = f"Timeout ({timeout_sec}s) su {label}"
                    mark_cooldown(
                        cd_key, label, f"Timeout dopo {timeout_sec}s", duration=30
                    )
                    await client.aclose()
                    continue
                except Exception as e:
                    last_error = f"Eccezione su {label}: {e}"
                    logger.error(f"⚠️  {last_error}")
                    await client.aclose()
                    continue

    logger.error(
        f"🚨 [FALLIMENTO TOTALE] Nessun upstream riuscito. Ultimo errore: {last_error}"
    )
    raise HTTPException(
        status_code=503,
        detail=f"Tutti i modelli Free Tier hanno fallito. Ultimo errore: {last_error}",
    )


if __name__ == "__main__":
    import uvicorn

    cfg = get_config()
    host = cfg.get("host", "127.0.0.1")
    port = int(cfg.get("port", 5005))
    logger.info(f"✨ Avvio Micro-Proxy Wyvern v1.6.0 su http://{host}:{port}...")
    uvicorn.run(app, host=host, port=port)
