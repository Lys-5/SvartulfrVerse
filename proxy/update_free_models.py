import json
import pathlib
import sys
import datetime
import copy
from urllib import request as urllib_request

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

    config["upstreams"] = upstreams
    
    # Save updated config
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
        
    log(f"Total active upstreams configured: {len(config.get('upstreams', []))}")
    log("Daily Proxy Models Check completed successfully.")

if __name__ == "__main__":
    update_proxy_config()
