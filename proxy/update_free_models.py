import json
import pathlib
import sys
import datetime
import copy
from urllib import request as urllib_request
from urllib import error as urllib_error

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROXY_DIR = ROOT / "proxy"
CONFIG_PATH = PROXY_DIR / "config_free_proxy.json"
LOG_FILE = PROXY_DIR / "proxy_models_update.log"

# Blacklist tassativa per modelli non idonei al Roleplay/TTRPG
BLACKLIST_PATTERNS = [
    "thinkingmachines/inkling",
    "content-safety",
    "mini-code",
    "embed",
    "moderation",
    "flash-lite",
    "lite",
    "vision-only",
]

def log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted + "\n")

def is_rpg_suitable(model_id: str) -> bool:
    mid = model_id.lower()
    for pattern in BLACKLIST_PATTERNS:
        if pattern in mid:
            return False
    return True

def fetch_openrouter_free_models():
    log("Fetching live OpenRouter free models...")
    try:
        req = urllib_request.Request(
            "https://openrouter.ai/api/v1/models",
            headers={"Accept": "application/json", "User-Agent": "SvartulfrProxyUpdater/1.0"},
        )
        with urllib_request.urlopen(req, timeout=15) as resp:
            if resp.getcode() == 200:
                payload = json.loads(resp.read().decode("utf-8", errors="replace"))
                models = payload.get("data", [])
                free_list = [m["id"] for m in models if ":free" in m.get("id", "")]
                log(f"Found {len(free_list)} active OpenRouter :free models.")
                return free_list
    except Exception as e:
        log(f"Error fetching OpenRouter models: {e}")
    return []

def update_proxy_config():
    log("--- Starting Daily Proxy Models Check & Update (RPG Aligned) ---")
    if not CONFIG_PATH.exists():
        log(f"Config file not found at {CONFIG_PATH}")
        return

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    # 1. Fetch live OpenRouter free models
    live_or_free = fetch_openrouter_free_models()
    
    # Check current upstreams in config
    upstreams = config.get("upstreams", [])
    
    # Filtra ed espelle eventuali modelli non idonei (es. flash-lite o non-RPG)
    clean_upstreams = []
    purged_count = 0
    for u in upstreams:
        uid = u.get("id", "").lower()
        models = [str(m).lower() for m in (u.get("models") or [u.get("model")]) if m]
        if any(p in uid for p in BLACKLIST_PATTERNS) or any(any(p in m for p in BLACKLIST_PATTERNS) for m in models):
            purged_count += 1
            log(f"Purged non-RPG upstream: {u.get('display_name')} ({u.get('id')})")
            continue
        clean_upstreams.append(u)
    
    upstreams = clean_upstreams
    
    # Trova i modelli già censiti
    existing_models = set()
    for u in upstreams:
        if u.get("model"):
            existing_models.add(u.get("model"))
        if u.get("models"):
            existing_models.update(u.get("models"))

    # Individua nuovi modelli che siano idonei per RPG
    new_found = [
        m for m in live_or_free 
        if m not in existing_models and is_rpg_suitable(m)
    ]
    
    if new_found:
        log(f"Discovered {len(new_found)} new RPG-suitable OpenRouter free models: {new_found[:5]}...")
        # Assegna priorità in coda ai modelli curati (minimo 30) per non intaccare i pilastri fiat (1-8) né i tier RPG primari (9-22)
        current_max_prio = max([u.get("priority", 25) for u in upstreams] or [25])
        current_max_prio = max(current_max_prio, 29)
        
        for model_id in new_found:
            current_max_prio += 1
            slug = model_id.split("/")[-1].replace(":free", "")
            upstreams.append({
                "priority": current_max_prio,
                "id": f"or-{slug}",
                "display_name": f"OpenRouter Free - {slug.title()}",
                "provider": "openrouter",
                "model": model_id,
                "base_url": "https://openrouter.ai/api/v1/chat/completions",
                "key_name": "openrouter",
                "context_window": 32768,
                "max_tokens": 4096,
                "supports_system": True,
                "supports_streaming": True
            })
        log(f"Appended {len(new_found)} new upstreams at fallback priorities >= 30.")
    else:
        log("No new RPG-suitable OpenRouter free models to add. Curated hierarchy preserved.")

    # 2. Google AI Studio live discovery & quota ordering
    verify_and_update_google_models(config)

    # 3. OpenRouter key health audit
    audit_openrouter_keys(config)

    config["upstreams"] = upstreams
    
    # Save updated config
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        
    log(f"Total active upstreams configured: {len(config.get('upstreams', []))}")

    # 4. Daily Free Token Provider Scouting (Stage 1B sub-routine)
    try:
        sys.path.insert(0, str(ROOT))
        from scripts.scout_free_model_providers import run_scout
        scout_res = run_scout()
        log(f"Daily Free Model Scouting completed: {scout_res.get('openrouter_free_count')} target models detected.")
    except Exception as e:
        log(f"Warning: Scouting step failed: {e}")

    # 5. Live Proxy :5005 End-to-End Liveness Check
    verify_proxy_liveness()

    log("Daily Proxy Models Check & Scouting completed successfully.")


def _is_candidate_gemini_chat_model(model_id: str) -> bool:
    """Return True if a Google AI Studio model ID is a valid Gemini chat model (3.5+ / 4+)."""
    m = model_id.lower()
    if not m.startswith("gemini-"):
        return False
    excluded = (
        "tts", "image", "embed", "lite", "transcribe", "robotics",
        "computer-use", "customtools", "omni", "2.0", "2.5", "1.5",
    )
    if any(x in m for x in excluded):
        return False
    return any(v in m for v in ("gemini-4", "gemini-3.8", "gemini-3.7", "gemini-3.6", "gemini-3.5", "gemini-3.1-pro", "gemini-flash-latest"))


def _probe_google_model(api_key: str, model_id: str) -> str:
    """Probe a Google AI Studio model with a minimal request. Returns 'ok', 'quota_0', 'rate', 'not_found', or 'error'."""
    body = json.dumps({
        "model": model_id,
        "messages": [{"role": "user", "content": "Hi"}],
        "max_tokens": 5,
    }).encode("utf-8")
    req = urllib_request.Request(
        "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
        data=body,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    )
    try:
        with urllib_request.urlopen(req, timeout=12) as resp:
            return "ok" if resp.getcode() == 200 else "error"
    except urllib_error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="ignore")
        if e.code == 404:
            return "not_found"
        if e.code == 429:
            return "quota_0" if "limit: 0" in msg else "rate"
        return "error"
    except Exception:
        return "error"


def verify_and_update_google_models(config: dict) -> None:
    """Discover new Google AI Studio models, prune 404s, and order working models before limit:0 ones."""
    keys = config.get("keys", {}).get("google_ai_studio", [])
    if not keys:
        log("Google AI Studio: no keys configured, skipping live model check.")
        return

    discovered_gemini: list[str] = []
    discovered_gemma4: list[str] = []
    try:
        req = urllib_request.Request(
            f"https://generativelanguage.googleapis.com/v1beta/models?key={keys[0]}",
            headers={"Accept": "application/json"},
        )
        with urllib_request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
            for m in data.get("models", []):
                mid = m.get("name", "").replace("models/", "")
                if _is_candidate_gemini_chat_model(mid):
                    discovered_gemini.append(mid)
                elif mid.startswith("gemma-4-"):
                    discovered_gemma4.append(mid)
        log(f"Google AI Studio: discovered {len(discovered_gemini)} Gemini and {len(discovered_gemma4)} Gemma-4 chat models.")
    except Exception as e:
        log(f"Warning: Google AI Studio model discovery failed: {e}")

    probe_key = keys[-1]
    for upstream in config.get("upstreams", []):
        uid = upstream.get("id")
        if uid == "p2-gemini-cloud":
            candidates = list(dict.fromkeys((upstream.get("models") or []) + discovered_gemini))
            working, rate_limited, quota_zero = [], [], []
            for m in candidates:
                status = _probe_google_model(probe_key, m)
                if status == "not_found":
                    log(f"Google AI Studio: pruned deprecated model {m} (404).")
                    continue
                if status == "ok":
                    working.append(m)
                elif status == "quota_0":
                    quota_zero.append(m)
                else:
                    rate_limited.append(m)
            upstream["models"] = working + rate_limited + quota_zero
            log(f"p2-gemini-cloud updated: working={working}, rate_limited={rate_limited}, quota_0={quota_zero}")
        elif uid == "p3-gemma4-google" and discovered_gemma4:
            existing = upstream.get("models") or []
            upstream["models"] = list(dict.fromkeys(existing + discovered_gemma4))


def audit_openrouter_keys(config: dict) -> None:
    """Verify configured OpenRouter keys via /api/v1/auth/key and log invalid/exhausted keys."""
    keys = config.get("keys", {}).get("openrouter", [])
    for idx, k in enumerate(keys):
        suf = f"...{k[-6:]}" if len(k) >= 6 else "short"
        req = urllib_request.Request(
            "https://openrouter.ai/api/v1/auth/key",
            headers={"Authorization": f"Bearer {k}"},
        )
        try:
            with urllib_request.urlopen(req, timeout=10) as r:
                info = json.loads(r.read().decode("utf-8", errors="replace")).get("data", {})
                rem = info.get("free_model_daily_requests", {}).get("remaining")
                log(f"OpenRouter key #{idx+1} ({suf}): OK (free_daily_remaining={rem})")
        except urllib_error.HTTPError as e:
            log(f"WARNING: OpenRouter key #{idx+1} ({suf}) failed auth check: HTTP {e.code}")
        except Exception as e:
            log(f"WARNING: OpenRouter key #{idx+1} ({suf}) check error: {e}")


def verify_proxy_liveness() -> None:
    """Verify local proxy :5005 health and end-to-end completion responsiveness."""
    port = 5005
    try:
        with urllib_request.urlopen(f"http://127.0.0.1:{port}/health", timeout=5) as r:
            log(f"Proxy :{port} /health -> {r.read().decode('utf-8', errors='ignore')}")
    except Exception as e:
        log(f"WARNING: Proxy :{port} /health unreachable: {e}")
        return

    try:
        req = urllib_request.Request(
            f"http://127.0.0.1:{port}/v1/chat/completions",
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "model": "free-tier-master",
                "messages": [{"role": "user", "content": "Ping"}],
                "max_tokens": 5,
            }).encode("utf-8"),
        )
        with urllib_request.urlopen(req, timeout=45) as r:
            served_by = r.headers.get("X-Served-By", "unknown")
            log(f"Proxy :{port} /v1/chat/completions -> HTTP {r.status} (X-Served-By: {served_by})")
    except Exception as e:
        log(f"WARNING: Proxy :{port} /v1/chat/completions failed/hung: {e}")

if __name__ == "__main__":
    update_proxy_config()
