# Scope: Wyvern Local Failover Proxy Cascade & API Key Audit

## Architecture
- `proxy/config_free_proxy.json`: Failover cascade configuration, provider definitions, model endpoints, cooldowns, timeout settings, and payload optimization rules.
- `proxy/free_tier_proxy.py`: FastAPI local micro-proxy handling OpenAI-compatible `/v1/chat/completions`, streaming SSE, fallback rotation, circuit breaker, and payload sanitization/compaction.
- Local configuration & secrets (`.env.example`, `proxy/config_free_proxy.json`): Provider API keys and environment variables.
- Documentation report (`proxy/API_KEY_ACQUISITION_GUIDE.md`): Comprehensive audit of missing/unconfigured API keys with direct console/signup URLs for zero or minimal cost acquisition.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Fiat Pillar Cascade Configuration | Configure GLM 5.2, Gemini Argon, Gemini 3.8, Gemma 4 as top fiat pillars | M1 | R1 |
| 2 | RPG Roleplay Quality Ranking | Rank and order all remaining cascade models by RPG roleplay quality | M1 | R1 |
| 3 | Proxy Implementation & Validation | Ensure `proxy/free_tier_proxy.py` properly loads and routes all configured models/providers | M1 | R1 |
| 4 | Static API Key Audit | Audit `.env` and `proxy/config_free_proxy.json` for missing or blank API keys | M1 | R2 |
| 5 | Acquisition Guide & URLs | Document direct console URLs and zero/minimal cost signup instructions | M1 | R2 |
| 6 | Test Suite Verification | Validate all existing and new proxy tests pass and configuration parses cleanly | M1 | Verification |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Failover Cascade Update & Key Audit | Update `config_free_proxy.json`, adjust `free_tier_proxy.py`, key audit & acquisition guide | none | DONE |

## Interface Contracts
- OpenAI-compatible REST API on local host (127.0.0.1:5005)
- Endpoints: `POST /v1/chat/completions`, `GET /v1/models`, `GET /health`
- Config schema: JSON defining `providers`, `models` cascade list, circuit breaker settings, and optimization parameters.
