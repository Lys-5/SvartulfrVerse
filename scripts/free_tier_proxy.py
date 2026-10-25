"""
Free Tier Auto-Rotator & Circuit Breaker Proxy for Wyvern
Version: 1.5.0 (Anti-Empty Response, Smart Cooldown, Param Sanitizer & File Logger)
"""

import os
import re
import sys
import time
import json
import logging
from typing import Dict, Any, List, Optional, Tuple
import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse

LOG_FILE = os.path.join(os.path.dirname(__file__), "proxy_debug.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8")
    ]
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
                logger.info("🔄 [CONFIG] Configurazione ricaricata con successo (Hot-Reload).")
    except Exception as e:
        logger.error(f"Errore lettura configurazione: {e}")
    return _cached_config

app = FastAPI(title="Wyvern Free Tier Failover Proxy v1.5.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cooldown granulare per combinazione (upstream_id + model + key_suffix)
cooldowns: Dict[str, float] = {}

def make_cd_key(uid: str, model: str, api_key: str) -> str:
    suffix = api_key[-6:] if api_key else "nokey"
    return f"{uid}::{model}::{suffix}"

def is_available(cd_key: str) -> bool:
    return time.time() > cooldowns.get(cd_key, 0.0)

def mark_cooldown(cd_key: str, label: str, reason: str, duration: Optional[float] = None):
    cfg = get_config()
    cooldown_sec = duration or cfg.get("cooldown_seconds", 60)
    cooldowns[cd_key] = time.time() + cooldown_sec
    logger.warning(f"❌ [COOLDOWN] {label} in quarantena per {cooldown_sec}s. Motivo: {reason}")

def resolve_keys(key_name: str, incoming_auth: Optional[str]) -> List[str]:
    cfg = get_config()
    val = cfg.get("keys", {}).get(key_name)
    keys: List[str] = []
    if isinstance(val, list):
        keys = [k.strip() for k in val if k and k.strip()]
    elif isinstance(val, str) and val.strip():
        keys = [val.strip()]

    env_key = os.environ.get(f"{key_name.upper()}_API_KEY", "").strip()
    if env_key and env_key not in keys:
        keys.append(env_key)

    if incoming_auth and incoming_auth.startswith("Bearer "):
        token = incoming_auth[7:].strip()
        if token and not token.startswith("sk-dummy") and token != "local" and token not in keys:
            keys.append(token)
    return keys

def deduplicate_wyvern_prompt(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Rimuove le biografie NPC duplicate dentro <PrimaryPool> se sono già presenti nel messaggio system,
    preservando integralmente <Outfit>, <Appearance>, <Users>, <PartyState> e Scenario Premise.
    """
    if not messages or len(messages) < 2:
        return messages

    sys_content = messages[0].get("content", "") if messages[0].get("role") == "system" else ""
    if "## NPC Database" not in sys_content:
        return messages

    new_messages = []
    for msg in messages:
        content = msg.get("content", "")
        if isinstance(content, str) and "<PrimaryPool>" in content and "</PrimaryPool>" in content:
            # Comprime i blocchi NPC massivi già presenti in system mantenendo header [NAME:...] e <Outfit>
            def shrink_npc_block(match):
                tag_name = match.group(1)
                inner = match.group(2)
                if tag_name in ("Users", "Alyssa", "PartyState", "PartyCharacters", "Outfit", "Appearance"):
                    return match.group(0)
                if f"<{tag_name}>" in sys_content:
                    header_match = re.search(r"(\[NAME:.*?\])", inner, re.DOTALL)
                    outfit_match = re.search(r"(<Outfit>.*?</Outfit>)", inner, re.DOTALL)
                    kept = []
                    if header_match:
                        kept.append(header_match.group(1))
                    if outfit_match:
                        kept.append(outfit_match.group(1))
                    if kept:
                        return f"<{tag_name}>\n" + "\n".join(kept) + f"\n</{tag_name}>"
                return match.group(0)

            compressed = re.sub(r"<([A-Za-zÀ-ÿ0-9_ -]+)>\n(\[NAME:.*?)</\1>", shrink_npc_block, content, flags=re.DOTALL)
            if len(compressed) < len(content):
                saved = len(content) - len(compressed)
                logger.info(f"✂️ [DEDUP] Rimossi {saved} caratteri di schede NPC duplicate da <PrimaryPool>.")
            new_messages.append({**msg, "content": compressed})
        else:
            new_messages.append(msg)
    return new_messages

def sanitize_request_body(body: Dict[str, Any], provider: str, target_model: str) -> Dict[str, Any]:
    req_body = dict(body)
    req_body["model"] = target_model

    # Deduplica le schede ripetute tra system e PrimaryPool
    if "messages" in req_body and isinstance(req_body["messages"], list):
        req_body["messages"] = deduplicate_wyvern_prompt(req_body["messages"])

    # Rimuove parametri non-standard OpenAI che causano 400 Bad Request su Groq/Google/SambaNova
    if provider in ("google", "groq", "sambanova"):
        req_body.pop("top_k", None)
        if req_body.get("stop") == []:
            req_body.pop("stop", None)

    if provider == "google":
        req_body.pop("frequency_penalty", None)
        req_body.pop("presence_penalty", None)
        if "max_tokens" in req_body and req_body["max_tokens"] > 8192:
            req_body["max_tokens"] = 8192

    return req_body

def validate_and_normalize_response(raw_bytes: bytes, target_model: str) -> Tuple[bool, Dict[str, Any], str]:
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
        err_msg = data["error"].get("message") if isinstance(data["error"], dict) else str(data["error"])
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

    finish_reason = choice0.get("finish_reason") or choice0.get("native_finish_reason") or "stop"

    # Se content_text è vuoto ma il modello ha scritto solo in reasoning_content (senza tag di risposta),
    # rifiuta per far scattare il failover verso un modello che risponda davvero alla scena.
    if not content_text or not str(content_text).strip():
        return False, data, f"Risposta con testo vuoto (finish_reason={finish_reason}, reasoning_len={len(str(reasoning_text))})"

    # Costruisce una risposta OpenAI Chat Completion standardizzata al 100%
    normalized = {
        "id": data.get("id") or f"chatcmpl-{int(time.time())}",
        "object": "chat.completion",
        "created": data.get("created") or int(time.time()),
        "model": data.get("model") or target_model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": str(content_text)
                },
                "finish_reason": finish_reason
            }
        ],
        "usage": data.get("usage") or {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0
        }
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
                "context_length": 1000000
            }
        ]
    }

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    cfg = get_config()
    body = await request.json()
    is_streaming = body.get("stream", False)
    incoming_auth = request.headers.get("authorization")

    upstreams = sorted(cfg.get("upstreams", []), key=lambda x: x.get("priority", 99))
    # Minimo 60s di timeout per richieste non-streaming con prompt grandi, anche se il json ha 8.0
    cfg_timeout = float(cfg.get("timeout_seconds", 60.0))
    timeout_sec = max(cfg_timeout, 65.0) if not is_streaming else max(cfg_timeout, 30.0)

    last_error = "Nessun modello disponibile"

    for upstream in upstreams:
        uid = upstream["id"]
        name = upstream["display_name"]
        priority = upstream["priority"]
        provider = upstream.get("provider", "generic")

        available_keys = resolve_keys(upstream.get("key_name", ""), incoming_auth)
        if not available_keys:
            logger.warning(f"⚠️  [SALTATO] P{priority} ({name}): Nessuna chiave per {upstream.get('key_name')}.")
            continue

        target_url = upstream["base_url"]
        models_to_try = upstream.get("models") or [upstream.get("model")]

        for api_key in available_keys:
            for target_model in models_to_try:
                cd_key = make_cd_key(uid, target_model, api_key)
                label = f"P{priority} {name} [{target_model}]"

                if not is_available(cd_key):
                    rem = round(cooldowns[cd_key] - time.time())
                    logger.info(f"⏭️  [SALTATO] {label} in cooldown ({rem}s rimanenti)...")
                    continue

                req_body = sanitize_request_body(body, provider, target_model)

                headers = {
                    "Content-Type": "application/json",
                    "Accept": "text/event-stream" if is_streaming else "application/json",
                    "User-Agent": "Wyvern-FreeTierProxy/1.5"
                }
                if api_key:
                    headers["Authorization"] = f"Bearer {api_key}"
                if provider == "openrouter":
                    headers["HTTP-Referer"] = "https://app.wyvern.chat"
                    headers["X-Title"] = "WyvernChat"

                logger.info(f"🚀 [ROUTING] Tentativo {label} (stream={is_streaming}, timeout={timeout_sec}s)...")

                client_timeout = httpx.Timeout(timeout_sec, connect=10.0)
                client = httpx.AsyncClient(timeout=client_timeout)

                try:
                    req = client.build_request("POST", target_url, headers=headers, json=req_body)
                    response = await client.send(req, stream=is_streaming)

                    if response.status_code != 200:
                        err_bytes = await response.aread()
                        err_str = err_bytes.decode("utf-8", errors="ignore")[:250]
                        last_error = f"{label} -> HTTP {response.status_code}: {err_str}"
                        
                        if response.status_code in (429, 402, 403) or response.status_code >= 500:
                            mark_cooldown(cd_key, label, f"HTTP {response.status_code}: {err_str[:80]}")
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
                                "X-Served-By": f"{name} ({target_model})"
                            }
                        )

                    # Gestione NON-STREAMING (Valida che non sia {"text": ""} prima di accettarla!)
                    raw_bytes = await response.aread()
                    await response.aclose()
                    await client.aclose()

                    is_valid, normalized_json, reason = validate_and_normalize_response(raw_bytes, target_model)
                    if not is_valid:
                        last_error = f"{label} -> {reason}"
                        mark_cooldown(cd_key, label, reason, duration=30)
                        continue

                    logger.info(f"✅ [SUCCESS] Risposta valida ({len(normalized_json['choices'][0]['message']['content'])} chars) da {label}!")
                    return JSONResponse(
                        content=normalized_json,
                        status_code=200,
                        headers={"X-Served-By": f"{name} ({target_model})"}
                    )

                except (httpx.TimeoutException, httpx.ConnectTimeout) as te:
                    last_error = f"Timeout ({timeout_sec}s) su {label}"
                    mark_cooldown(cd_key, label, f"Timeout dopo {timeout_sec}s", duration=30)
                    await client.aclose()
                    continue
                except Exception as e:
                    last_error = f"Eccezione su {label}: {e}"
                    logger.error(f"⚠️  {last_error}")
                    await client.aclose()
                    continue

    logger.error(f"🚨 [FALLIMENTO TOTALE] Nessun upstream riuscito. Ultimo errore: {last_error}")
    raise HTTPException(
        status_code=503,
        detail=f"Tutti i modelli Free Tier hanno fallito. Ultimo errore: {last_error}"
    )

if __name__ == "__main__":
    import uvicorn
    cfg = get_config()
    host = cfg.get("host", "127.0.0.1")
    port = int(cfg.get("port", 5005))
    logger.info(f"✨ Avvio Micro-Proxy Wyvern v1.5.0 su http://{host}:{port}...")
    uvicorn.run(app, host=host, port=port)