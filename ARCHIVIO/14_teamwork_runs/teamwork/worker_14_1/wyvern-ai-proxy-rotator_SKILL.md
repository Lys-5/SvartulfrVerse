# Local copy of wyvern-ai-proxy-rotator skill
Source: e:\repository\SvartulfrVerse\.agents\skills\wyvern-ai-proxy-rotator\SKILL.md

---
name: wyvern-ai-proxy-rotator
description: >-
  Micro-proxy locale FastAPI OpenAI-compatible per Wyvern con rotazione automatica e failover
  circuit-breaker (cooldown 60s) su modelli Free Tier prioritari (GLM 5.2+, Gemini Argon,
  Gemini 3.1 Pro, Gemma 4+), supporto streaming SSE e CORS.
---

## 1. Architettura di Routing e Cascata di Priorità
Micro-proxy FastAPI (127.0.0.1:5005) con Circuit-Breaker & Cooldown Manager (60s).
- P1: GLM 5.2 / GLM Family (OpenRouter Free / Zhipu / NavyAI / Chutes)
- P2: Gemini Argon / Flash (Google AI Studio - 15 RPM Free)
- P3: Gemini 3.1 PRO / 2.5 Pro (Google AI Studio - Free Tier Solo Pro)
- P4: Gemma 4 / Gemma 2 27B (Groq / OpenRouter Free / SambaNova)

## 2. Componenti Software
- Proxy Server (`proxy/free_tier_proxy.py`): FastAPI / Uvicorn, CORS, `/v1/chat/completions`, `/v1/models`, `/health`.
- Configurazione Hot-Reload (`proxy/config_free_proxy.json`): mtime check.
- Middleware PayloadCompactor (Phase 1-5).
