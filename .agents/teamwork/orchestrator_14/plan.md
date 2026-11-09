# Execution Plan — Milestone 1: Proxy Model Cascade & API Key Audit

## Objective
Update the Wyvern local failover micro-proxy model cascade in `proxy/config_free_proxy.json` and `proxy/free_tier_proxy.py` prioritizing GLM 5.2, Gemini Argon, Gemini 3.8, and Gemma 4 as top fiat pillars, rank remaining models by RPG roleplay quality, and audit missing API keys with acquisition URLs.

## Steps
1. **Survey & Technical Exploration**
   - Dispatch 3 parallel Explorers:
     - Explorer 1: Inspect `proxy/config_free_proxy.json`, `proxy/free_tier_proxy.py`, tests in repository (e.g. `tests/test_proxy*` or `pytest`), model naming/provider mappings, and existing cascade order.
     - Explorer 2: Review roleplay quality rankings of candidate models for Wyvern RP (GLM 5.2, Gemini Argon, Gemini 3.8, Gemma 4, DeepSeek, Claude, Mistral, Llama, Qwen, etc.), verifying current API IDs, provider specifications, context window, and system prompt handling.
     - Explorer 3: Audit `.env`, `.env.example`, `proxy/config_free_proxy.json` for all referenced provider environment variables / keys; document missing keys, signup URLs, and console acquisition links.
2. **Implementation**
   - Dispatch Worker with domain skill `wyvern-ai-proxy-rotator`:
     - Update `proxy/config_free_proxy.json` with the new cascade (GLM 5.2 -> Gemini Argon -> Gemini 3.8 -> Gemma 4 -> subsequent models ordered by RPG roleplay quality).
     - Update `proxy/free_tier_proxy.py` if needed to support providers/endpoints/format differences.
     - Generate/update the API key audit and acquisition guide document (e.g. `proxy/API_KEY_ACQUISITION_GUIDE.md`).
     - Run existing tests and verification commands to verify clean startup and config loading.
3. **Review & Empirical Verification**
   - Dispatch 2 independent Reviewers to review code quality, JSON validity, cascade order, and documentation completeness.
   - Dispatch 2 Challengers to empirically test config loading, route handling, model fallback logic, and key auditing.
4. **Forensic Integrity Audit**
   - Dispatch 1 Forensic Auditor (`teamwork_auditor`) for static analysis, integrity check, and zero-cheat verification.
5. **Gate & Synthesis**
   - Check all gate criteria in `GATE_STATUS.md`. If all pass, update progress and report final synthesis back to parent.
