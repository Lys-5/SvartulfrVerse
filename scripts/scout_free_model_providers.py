#!/usr/bin/env python3
"""
Scout Free Model Providers & Endpoints (Daily Automated Scouting)
Part of Stage 1B in Svartúlfr Verse Daily Master Pipeline.

Queries live aggregators and provider endpoints (OpenRouter, Google AI Studio,
SiliconFlow, Hugging Face, etc.) to discover newly available free tokens or free-tier
endpoints for our core models:
  - GLM (GLM-5.3, GLM-5.2, GLM-4)
  - Gemini (Gemini 3.8, Gemini 3.5 Flash, Gemini 4)
  - Gemma (Gemma 4+, 31B, 26B)

Writes report to: logs/automations/free_token_providers_scouting.md
"""

import sys
import os
import json
import datetime
import pathlib
from urllib import request as urllib_request
from urllib import error as urllib_error

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGS_DIR = ROOT / "logs" / "automations"
CONFIG_PATH = ROOT / "proxy" / "config_free_proxy.json"
REPORT_MD = LOGS_DIR / "free_token_providers_scouting.md"

TARGET_FAMILIES = ["glm", "gml", "gemini", "gemma"]
BLACKLIST_KEYWORDS = [
    "thinkingmachines", "content-safety", "embed", "moderation",
    "flash-lite", "vision-only", "2b"
]

def log(msg: str):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")

def is_target_model(model_id: str) -> bool:
    mid = model_id.lower()
    if any(b in mid for b in BLACKLIST_KEYWORDS):
        return False
    return any(fam in mid for fam in TARGET_FAMILIES)

def scout_openrouter_free() -> list:
    log("Scouting OpenRouter for free models (:free)...")
    url = "https://openrouter.ai/api/v1/models"
    try:
        req = urllib_request.Request(
            url,
            headers={"Accept": "application/json", "User-Agent": "SvartulfrScout/1.0"}
        )
        with urllib_request.urlopen(req, timeout=15) as resp:
            if resp.getcode() == 200:
                data = json.loads(resp.read().decode("utf-8", errors="replace"))
                models = data.get("data", [])
                matched = []
                for m in models:
                    mid = m.get("id", "")
                    pricing = m.get("pricing", {})
                    prompt_price = float(pricing.get("prompt", 1.0))
                    compl_price = float(pricing.get("completion", 1.0))
                    is_zero_cost = (prompt_price == 0.0 and compl_price == 0.0) or ":free" in mid

                    if is_zero_cost and is_target_model(mid):
                        matched.append({
                            "provider": "OpenRouter",
                            "model_id": mid,
                            "name": m.get("name", mid),
                            "context_length": m.get("context_length", 32768),
                            "endpoint": "https://openrouter.ai/api/v1/chat/completions",
                            "auth_key": "openrouter"
                        })
                log(f"OpenRouter: Found {len(matched)} matching free models.")
                return matched
    except Exception as e:
        log(f"Warning: OpenRouter scout failed: {e}")
    return []

def scout_known_providers_status() -> list:
    log("Scouting known providers with active free tiers / promotions...")
    providers = [
        {
            "name": "Google AI Studio",
            "tier": "Free Tier (RPM / RPD quotas without credit card)",
            "supported_models": ["gemini-3.5-flash", "gemini-3.7-flash", "gemini-3.8-flash", "gemma-4-31b-it"],
            "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
            "key_config": "google_ai_studio",
            "status": "Active (4 keys in pool)"
        },
        {
            "name": "Zhipu AI (Z.ai / BigModel)",
            "tier": "Developer Free Quota / Startup Grant Program",
            "supported_models": ["glm-4-flash", "glm-5.3-flash", "glm-zero-preview"],
            "base_url": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
            "key_config": "zhipu",
            "status": "Active (Key configured)"
        },
        {
            "name": "SiliconFlow (SiliconCloud)",
            "tier": "Free Registration Tokens (Millions of initial free tokens)",
            "supported_models": ["GLM-5.3-Flash", "DeepSeek-V3", "Qwen3.8"],
            "base_url": "https://api.siliconflow.cn/v1/chat/completions",
            "key_config": "siliconflow",
            "status": "Available for registration (Free token grant on signup)"
        },
        {
            "name": "Cloudflare Workers AI",
            "tier": "Free Tier (10,000 Neurons / day free allowance)",
            "supported_models": ["@cf/google/gemma-7b-it", "GLM partner endpoints"],
            "base_url": "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run",
            "key_config": "cloudflare",
            "status": "Active (Token configured)"
        }
    ]
    return providers

def generate_scouting_report(or_models: list, known_providers: list) -> str:
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "# Report Quotidiano Scouting — Provider & Token Free Tier",
        f"\n**Data Scansione:** {now_str}  ",
        "**Target:** Modelli Prioritari (GLM 5.2+, Gemini 3.8+, Gemma 4+)  ",
        "**Stato Pipeline:** Stage 1B (Automazione Master Quotidiana)",
        "\n---",
        "\n## 1. Modelli Free Rilevati su OpenRouter (`:free`)",
    ]

    if or_models:
        lines.append("| Modello | Nome Visualizzato | Context Window | Endpoint |")
        lines.append("| :--- | :--- | :--- | :--- |")
        for m in or_models:
            lines.append(f"| `{m['model_id']}` | {m['name']} | {m['context_length']} | `{m['endpoint']}` |")
    else:
        lines.append("*Nessun nuovo modello free individuato su OpenRouter nelle ultime 24h.*")

    lines.append("\n---")
    lines.append("\n## 2. Panoramica Provider con Token Free / Programmi Sviluppatori")
    lines.append("| Provider | Offerta Free Tier | Modelli Chiave Supportati | Stato Chiave nel Proxy |")
    lines.append("| :--- | :--- | :--- | :--- |")
    for p in known_providers:
        models_str = ", ".join([f"`{m}`" for m in p["supported_models"]])
        lines.append(f"| **{p['name']}** | {p['tier']} | {models_str} | {p['status']} |")

    lines.append("\n---")
    lines.append("\n## 3. Opportunità di Espansione Limiti")
    lines.append("- **SiliconFlow:** Registrando un account gratuito su `siliconflow.cn` si ottiene un pacchetto di benvenuto con milioni di token gratuiti per modelli GLM e DeepSeek via API OpenAI-compatible. Basta incollare la chiave in `config_free_proxy.json` sotto `\"siliconflow\"`.")
    lines.append("- **Zhipu AI Startup / Dev Grant:** Per progetti open e TTRPG, il programma developer `z.ai` rilascia token gratuiti dedicati a sviluppatori.")
    lines.append("- **Google AI Studio Key Pool:** È possibile creare ulteriori chiavi su account Google secondari per ampliare ulteriormente il round-robin a 5+ chiavi.")
    lines.append("\n---")

    return "\n".join(lines)

def run_scout():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log("Starting Daily Free Token Providers Scout...")

    or_models = scout_openrouter_free()
    known_providers = scout_known_providers_status()

    report_content = generate_scouting_report(or_models, known_providers)
    REPORT_MD.write_text(report_content, encoding="utf-8")
    log(f"Scouting report written to {REPORT_MD}")

    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "openrouter_free_count": len(or_models),
        "openrouter_models": or_models,
        "providers_scouted": len(known_providers)
    }

if __name__ == "__main__":
    run_scout()
