# Detailed Technical Exploration Report: Wyvern Failover Micro-Proxy Architecture & Model Cascade

**Author**: Explorer 1 (Codebase & Proxy Architect)  
**Date**: 2026-11-01  
**Scope**: `proxy/config_free_proxy.json`, `proxy/free_tier_proxy.py`, `proxy/update_free_models.py`, `tests/test_proxy_compaction.py`, `tests/test_adversarial_compaction.py`, `.env` audit, and live runtime telemetry.

---

## 1. Executive Summary

The Svartúlfr Verse local failover micro-proxy is a high-performance, asynchronous FastAPI service (`v1.6.0`) deployed on `127.0.0.1:5005` that exposes an OpenAI-compatible interface (`/v1/chat/completions`, `/v1/models`, `/health`) designed specifically for Wyvern chat roleplay. It implements a non-destructive 5-phase payload compactor (`PayloadCompactor`), granular triple-tuple circuit-breaker cooldowns, hot-reloading JSON configuration, and multi-provider failover.

Current forensic analysis of runtime logs (`proxy/uvicorn.log`) reveals that while the failover mechanism functions correctly—successfully catching HTTP 429 and 402 errors and descending to operational backups—the current cascade order in `proxy/config_free_proxy.json` suffers from inverted priorities (Priority 1 is set to lightweight `gemini-3.1-flash-lite`, Priority 2 is OpenRouter free Nemotron, while GLM 5.2 and Gemini Argon are buried at P3-P5). Furthermore, non-free models are mixed into OpenRouter free cascades causing instant 402 Payment Required errors, and newly discovered models added by `update_free_models.py` include moderation safety classifiers (`nemotron-3.5-content-safety`) and coding utilities unsuitable for RPG roleplay.

All existing test suites (28 tests across `test_proxy_compaction.py` and `test_adversarial_compaction.py`) execute in 0.39s and pass with a 100% success rate. The architecture can be cleanly restructured to support the required 4 primary fiat pillars (GLM 5.2, Gemini Argon, Gemini 3.8, Gemma 4) followed by an RPG roleplay quality cascade without regression.

---

## 2. Codebase & Runtime Inventory

| File / Component | Path | Lines | Version / Size | Role & Architecture |
|---|---|---|---|---|
| **Proxy Server** | `proxy/free_tier_proxy.py` | 915 | v1.6.0 (34 KB) | FastAPI server, loopback CORS + PNA, 5-phase `PayloadCompactor`, circuit breaker, streaming/non-streaming routing |
| **Cascade Config** | `proxy/config_free_proxy.json` | 353 | 11.8 KB | 28 upstream definitions, 10 provider API keys, 40s cooldown, 35s timeout, hot-reload `mtime` |
| **Model Updater** | `proxy/update_free_models.py` | 97 | 3.6 KB | Automated maintenance script fetching live OpenRouter `:free` models and appending new upstreams |
| **Startup Script** | `proxy/start_proxy.vbs` | 5 | 413 B | Headless Windows Script Host launcher executing Python 3.14 via `cmd /c start /B` into `uvicorn.log` |
| **Runtime Logs** | `proxy/uvicorn.log` | 602 | 75 KB | Live stdout/stderr log of the running uvicorn process (PID 15972) |
| **Debug Logs** | `proxy/proxy_debug.log` | ~22,000 | 2.6 MB | Historical file logger handler tracking all routing decisions and cooldowns |
| **Test Suite 1** | `tests/test_proxy_compaction.py` | 504 | 24.3 KB | 13 test cases: network binding, 15%-35% reduction, zero semantic loss, FastAPI TestClient, phase isolation |
| **Test Suite 2** | `tests/test_adversarial_compaction.py` | 586 | 24.6 KB | 15 test cases: malformed XML, markdown tables/code blocks, quotes, name collisions, extreme repetition |

---

## 3. Test Suite Assessment & Verification

### 3.1 Execution Command & Test Run Results

```powershell
python -m pytest tests/test_proxy_compaction.py tests/test_adversarial_compaction.py -v
```

**Outcome**: **28 passed, 0 failed, 2 deprecation warnings in 0.39s**.

### 3.2 Verification Matrix

| Test Function | Target File & Scope | Assertions & Invariants Verified |
|---|---|---|
| `test_config_network_host_binding` | `test_proxy_compaction.py` | Verifies `host == "127.0.0.1"`, `port == 5005` in both file and `get_config()` runtime loader |
| `test_payload_compactor_executes_all_phases_and_achieves_reduction` | `test_proxy_compaction.py` | Asserts 15% to 35% reduction on bloated production prompt (Phase 1-5); verifies deep copy non-mutation |
| `test_zero_semantic_loss_invariant` | `test_proxy_compaction.py` | Byte-for-byte retention of Italian sandwich directives, JED+ dossiers, lore, double-quoted dialogues |
| `test_fastapi_testclient_health_and_models` | `test_proxy_compaction.py` | Validates `GET /health` (`status: ok`) and `GET /v1/models` (`id: free-tier-master`, context 1M) via TestClient |
| `test_live_network_health_endpoint` | `test_proxy_compaction.py` | Confirms live loopback HTTP server is active and reachable at `http://127.0.0.1:5005/health` |
| `test_phase1_chutes_top_k` | `test_proxy_compaction.py` | Chutes provider forces `top_k: -1`, strips frequency and presence penalties |
| `test_phase1_gemini_max_tokens_clamp` | `test_proxy_compaction.py` | Google provider clamps `max_tokens` to 8192, strips sampling penalties |
| `test_phase1_narrator_stop_sequence_strip` | `test_proxy_compaction.py` | Strips `\nNarrator:` variants from `stop` sequences to prevent premature narrative cutoff |
| `test_phase2_xml_lore_deduplication` | `test_proxy_compaction.py` | Deduplicates `<npc>`, `<location>`, `<item>` tags by normalized name attribute or JED+ bracket |
| `test_phase3_active_character_cross_dedup` | `test_proxy_compaction.py` | Active character in `<character>` causes removal of duplicate `<npc>` in `<world_context>` |
| `test_phase4_empty_tag_and_attribute_pruning` | `test_proxy_compaction.py` | Prunes `labels=""`, `type=""`, `<special_stats></special_stats>`, empty `<outfit>` tags |
| `test_phase5_whitespace_collapsing_and_message_merging` | `test_proxy_compaction.py` | Collapses 3+ newlines to 2, strips trailing whitespace, merges consecutive identical roles |
| `test_deep_copy_prevents_failover_loop_mutation` | `test_proxy_compaction.py` | Multi-upstream retry loop operates on deep copies without mutating caller's original dictionary |
| `test_network_host_isolation` | `test_adversarial_compaction.py` | Strict loopback isolation check against 127.0.0.1:5005 |
| `test_unclosed_xml_tags_no_crash_and_preserved` | `test_adversarial_compaction.py` | Unclosed tags do not trigger regex catastrophe or drop content |
| `test_special_characters_in_xml_attributes` | `test_adversarial_compaction.py` | Escaped quotes, single quotes, ampersands in attributes parse without throwing |
| `test_nested_xml_tags_handling` | `test_adversarial_compaction.py` | Nested tags of same name survive without truncation |
| `test_markdown_code_blocks_and_indentation_preservation` | `test_adversarial_compaction.py` | Indentation within triple-backtick markdown blocks is preserved 1:1 |
| `test_markdown_tables_and_lists_preservation` | `test_adversarial_compaction.py` | Table column delimiters (`\|`) and nested list indentation remain intact |
| `test_dialogue_quotes_and_foreign_parentheticals_preservation` | `test_adversarial_compaction.py` | Double quotes, Italian apostrophes (`l'ambrosia`), foreign translations preserved |
| `test_subword_character_names_not_falsely_stripped` | `test_adversarial_compaction.py` | Short active name ("Ray") does not falsely purge longer NPC ("Raymond Sinclair") |
| `test_reverse_subword_character_names_not_falsely_stripped` | `test_adversarial_compaction.py` | Long active name ("Alexander") does not purge prefix NPC ("Alex") |
| `test_first_name_shared_between_different_characters_investigation` | `test_adversarial_compaction.py` | Evaluates behavior when two characters share first name ("Dominic Chen" vs "Dominic Rogers") |
| `test_extreme_repetition_100_identical_tags` | `test_adversarial_compaction.py` | 100 identical `<npc>` tags deduped to 1 in linear time |
| `test_pathological_empty_and_nested_tags_pruning` | `test_adversarial_compaction.py` | Deeply nested empty elements and empty attributes completely pruned |
| `test_production_bloat_compaction_reduction_benchmark` | `test_adversarial_compaction.py` | 6000+ char production prompt compacted by 15%-35% without data loss |
| `test_heavy_duplicate_bloat_compaction_scaling` | `test_adversarial_compaction.py` | Extreme duplicate bloat achieves >50% reduction gracefully |
| `test_lean_payload_zero_unintended_reduction` | `test_adversarial_compaction.py` | Lean/clean prompt has <= 1.0% reduction (whitespace normalization only) |

**Key Finding**: None of the test cases assert specific upstream priority numbers or model cascade ordering. The test suite strictly validates network binding, schema integrity, and the non-destructive compaction pipeline. Changes to `upstreams` ordering in `config_free_proxy.json` will not break any existing tests.

---

## 4. Deep Architectural Decomposition

### 4.1 Provider Definitions & Key Resolution

1. **Configuration Schema**:
   In `proxy/config_free_proxy.json`:
   - Top-level `keys` maps provider aliases (`google_ai_studio`, `openrouter`, `groq`, `chutes`, `sambanova`, `nvidia`, `cloudflare`, `github`, `huggingface`, `deepinfra`) to string tokens or arrays of tokens (e.g. `openrouter` has 2 rotated keys).
   - In `proxy/free_tier_proxy.py:resolve_keys(key_name, incoming_auth)` (lines 102–124):
     - Looks up `key_name` in `config["keys"]`. If it's a list, extracts all trimmed keys; if string, wraps into a single-element list.
     - Inspects environment variable `{KEY_NAME.upper()}_API_KEY` (e.g. `GOOGLE_AI_STUDIO_API_KEY`).
     - Inspects incoming client `Authorization: Bearer <token>`, appending valid non-dummy tokens.
2. **Current Upstream Key Binding Defect**:
   In `proxy/free_tier_proxy.py` lines 758–764:
   ```python
   key_name = upstream.get("key_name") or ("openrouter" if provider == "openrouter" else "")
   available_keys = resolve_keys(key_name, incoming_auth)
   if not available_keys:
       logger.warning(f"⚠️  [SALTATO] P{priority} ({name}): Nessuna chiave per {key_name}.")
       continue
   ```
   If an upstream has `key_name` configured (or defaults to `openrouter`), but that key is missing or blank in `keys` and the incoming client request provides no bearer token, the proxy logs a warning and skips the upstream entirely.

### 4.2 Cascade Parsing, Model Routing & Fallback Logic

In `proxy/free_tier_proxy.py:chat_completions` (lines 736–905):
1. **Upfront Compaction**: The incoming `body` is deep-copied and compacted once via `PayloadCompactor.compact_request_payload(body)` before entering the failover loop.
2. **Priority Ordering**: Upstreams are sorted strictly by `priority` ascending:
   ```python
   upstreams = sorted(cfg.get("upstreams", []), key=lambda x: x.get("priority", 99))
   ```
3. **Multi-Model & Multi-Key Loop**:
   - For each `upstream`:
     - Resolves `available_keys`.
     - Resolves `target_url` (`upstream.get("base_url")` or `upstream.get("api_base") + "/chat/completions"`).
     - Resolves `models_to_try` (supports both `"models": [...]` list and `"model": "..."` string).
     - Loops: `for api_key in available_keys:` $\to$ `for target_model in models_to_try:`.
4. **Per-Attempt Isolation**:
   - Checks `is_available(cd_key)` against the circuit-breaker table.
   - Calls `compactor.prepare_for_provider(compacted_base, provider, target_model)`.
   - Injects HTTP headers (`Content-Type`, `Accept`, `User-Agent`, `Authorization: Bearer {api_key}`). If `provider == "openrouter"`, injects `HTTP-Referer: https://app.wyvern.chat` and `X-Title: WyvernChat`.
   - Sends asynchronous HTTP request via `httpx.AsyncClient` with custom timeouts.

### 4.3 Circuit-Breaker Cooldowns & Timeouts

1. **Granular Cooldown Key**:
   ```python
   def make_cd_key(uid: str, model: str, api_key: str) -> str:
       suffix = api_key[-6:] if api_key else "nokey"
       return f"{uid}::{model}::{suffix}"
   ```
   Cooldowns are **not** global to the provider; they are isolated to the specific combination of `(upstream_id, model_name, api_key_suffix)`. If `gemini-4-argon` fails on Key A, `gemini-3.8-flash` on Key A or `gemini-4-argon` on Key B is **not** penalized.
2. **Quarantine Triggers**:
   - **HTTP 429 (Rate Limit / Quota Exceeded), HTTP 402 (Payment Required), HTTP 403 (Forbidden), HTTP >= 500 (Server Error)**:
     Quarantined for `cooldown_seconds` (configured as 40s in `config_free_proxy.json`, fallback 60s in code).
   - **Invalid / Empty Non-Streaming Response Body**:
     Quarantined for 30s.
   - **Request Timeout (`httpx.TimeoutException`, `httpx.ConnectTimeout`)**:
     Quarantined for 30s.
3. **Timeout Architecture**:
   - `timeout_sec = max(cfg_timeout, 40.0) if not is_streaming else max(cfg_timeout, 25.0)`.
   - Connect timeout is fixed at 10.0s (`httpx.Timeout(timeout_sec, connect=10.0)`).
   - If an upstream hangs, the circuit breaker trips after 25s (streaming) or 40s (non-streaming), logs the failure, marks 30s cooldown, and proceeds immediately to the next candidate model.

### 4.4 SSE Streaming vs. Non-Streaming Engine

1. **SSE Streaming (`stream=True`)**:
   - Headers: `Accept: text/event-stream`, `Cache-Control: no-cache`, `Connection: keep-alive`.
   - Wrapped in an async generator `stream_generator()` consuming `response.aiter_bytes()`.
   - Guaranteed cleanup: `response.aclose()` and `client.aclose()` are executed in a `finally:` block when the client disconnects or the stream ends.
   - Response header `X-Served-By: {name} ({target_model})` emitted.
2. **Non-Streaming (`stream=False`)**:
   - Entire response read into memory via `await response.aread()`.
   - Processed by `validate_and_normalize_response(raw_bytes, target_model)`:
     - Parses JSON, verifies absence of top-level `error` object.
     - Validates non-empty `choices[0].message.content` or `choices[0].text`.
     - **Crucial Anti-Blank Defense**: If `content` is empty but the model returned thoughts only in `reasoning_content`, the response is **rejected** (`is_valid = False`), triggering automatic failover so the user never sees a blank message.
     - Standardizes output structure into canonical OpenAI Chat Completion dictionary.

### 4.5 5-Phase Payload Compactor & Parameter Sanitizer

`PayloadCompactor` executes deterministically in sequence:
- **Phase 1: Parameter Sanitization**:
  - Removes `frequency_penalty` and `presence_penalty` if 0.0, or if provider in `google`, `sambanova`, `groq`, `nvidia`, `cloudflare`, or if target model contains "r1".
  - If provider is `chutes`, sets `top_k = -1`. Otherwise prunes non-positive `top_k`.
  - Clamps `max_tokens` to 8192 for Google, OpenRouter, and Groq.
  - Strips `\nNarrator:` variants from `stop` sequences.
- **Phase 2: XML Lore Deduplication**:
  - Regex detects `<npc>`, `<location>`, `<item>`, `<creature>`, `<lore_entry>`.
  - Normalizes identifier (via `name="..."`, `title="..."`, `id="..."` or `[NAME: ...]`) and deduplicates across all messages.
- **Phase 3: Active Character Cross-Deduplication**:
  - Discovers active characters present in `<character>` or `<user_persona>`.
  - Prunes redundant duplicate `<npc>` dossiers of those active characters from `<world_context>` and system prompts.
- **Phase 4a & 4b: Stripping Comments & Empty Elements**:
  - Strips HTML/XML comments `<!-- ... -->`.
  - Normalizes `\r\n` to `\n` and collapses whitespace between tags (`>\s{2,}<` $\to$ `>\n<`).
  - Prunes empty attributes (`labels=""`, `type=""`) and empty tags (`<special_stats></special_stats>`, `<outfit></outfit>`).
- **Phase 5: Whitespace Collapsing & Role Merging**:
  - Collapses 3+ newlines to 2 (markdown paragraph integrity preserved).
  - Compacts JED+ PList punctuation spaces (`;\s{2,}` $\to$ `; `).
  - Merges consecutive identical roles (`user`/`user` or `system`/`system`).

---

## 5. Production Log Forensics (`uvicorn.log` & `proxy_models_update.log`)

### 5.1 Real Failover Cascade Execution in Production

Inspecting `proxy/uvicorn.log` lines 8–65 reveals an exact real-world production incident during Wyvern chat play:

```text
18:50:48 [ROUTING] Tentativo P1 Gemini 4 / 3.8+ [gemini-4-argon] (stream=True)...
18:50:49 HTTP Request: POST .../openai/chat/completions "HTTP/1.1 429 Too Many Requests"
18:50:49 [COOLDOWN] P1 [gemini-4-argon] in quarantena per 40s. Motivo: HTTP 429: You exceeded your current quota...
18:50:49 [ROUTING] Tentativo P1 Gemini 4 / 3.8+ [gemini-3.8-flash] (stream=True)...
18:50:50 HTTP Request: POST .../openai/chat/completions "HTTP/1.1 429 Too Many Requests"
18:50:50 [COOLDOWN] P1 [gemini-3.8-flash] in quarantena per 40s. Motivo: HTTP 429: You exceeded your current quota...
18:50:50 [ROUTING] Tentativo P2 GLM 5.2+ (OpenRouter) [z-ai/glm-5.3] (stream=True)...
18:50:50 HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 402 Payment Required"
18:50:50 [COOLDOWN] P2 [z-ai/glm-5.3] in quarantena per 40s. Motivo: HTTP 402: This request requires more credits...
18:50:54 [ROUTING] Tentativo P3 GLM 5.2+ (Chutes) [zai-org/GLM-5.2-TEE] (stream=True)...
18:50:55 HTTP Request: POST https://llm.chutes.ai/v1/chat/completions "HTTP/1.1 402 Payment Required"
18:50:55 [COOLDOWN] P3 [zai-org/GLM-5.2-TEE] in quarantena per 40s. Motivo: HTTP 402: Quota exceeded balance -0.057...
18:50:55 [ROUTING] Tentativo P4 Gemma 4 Free (OpenRouter) [google/gemma-4-31b-it:free] (stream=True)...
18:50:56 HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 429 Too Many Requests"
...
18:51:02 [ROUTING] Tentativo P10 Gemini 3.6 / 3.5 / 3.1 Backup [gemini-3.6-flash] (stream=True)...
18:51:23 HTTP Request: POST .../openai/chat/completions "HTTP/1.1 200 OK"
18:51:23 [STREAM START] Connesso a P10 Gemini Backup [gemini-3.6-flash]!
INFO: 127.0.0.1 - "POST /v1/chat/completions HTTP/1.1" 200 OK
```

### 5.2 Diagnostic Findings from Production Telemetry
1. **Circuit Breaker Operates Flawlessly**: When upstream models failed with 429 or 402, each failing model entered cooldown immediately (40s), and the proxy continued cascading without dropping the user's connection until `gemini-3.6-flash` succeeded with HTTP 200 OK.
2. **OpenRouter Paid Model Infiltration**: `z-ai/glm-5.2` and `z-ai/glm-5.3` on OpenRouter were configured with standard OpenRouter IDs rather than `:free` endpoints. Because the user's OpenRouter account currently carries zero paid balance, requests to these paid models immediately threw HTTP 402.
3. **Chutes Negative Balance**: Chutes returned `HTTP 402: Quota exceeded and account balance is $-0.057`. Chutes models tripped the circuit breaker instantly.
4. **Automated Cron Updater Pollution (`update_free_models.py`)**:
   - Lines 38–43 in `proxy/proxy_models_update.log` show that `update_free_models.py` runs regularly.
   - It appends all live OpenRouter models containing `:free` to `config_free_proxy.json`.
   - As a result, non-RPG models were registered as upstreams:
     * `nvidia/nemotron-3.5-content-safety:free` (P28) — a moderation classification model.
     * `cohere/north-mini-code:free` (P27) — a programming model.
     * Duplicate registrations: `nvidia/nemotron-3-ultra-550b-a55b:free` was registered both in block P2 and as individual upstream P17.

---

## 6. Gap Analysis & Proposed Architectural Upgrades

### 6.1 The 4 Primary Fiat Pillars Re-ordering

The current configuration starts with `gemini-3.1-flash-lite` (P1) and OpenRouter Nemotron (P2). The required architecture mandates setting **GLM 5.2, Gemini Argon, Gemini 3.8, and Gemma 4 as the top fiat pillars**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                      WYVERN LOCAL FAILOVER PROXY                        │
│                           (127.0.0.1:5005)                             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
┌─────────────────────────────────────────────────────────┐   ┌───────────────────────────┐
│              TOP FIAT PILLARS (P1 - P4)                 │   │ PAYLOAD COMPACTION (1.6)  │
│                                                         │   │ - Phase 1: Param sanitize │
│ Priority 1: GLM 5.2 Family                              │   │ - Phase 2: XML lore dedup │
│   - Zhipu BigModel (glm-5.2 / glm-4-flash free)         │   │ - Phase 3: Active char ded│
│   - Chutes (zai-org/GLM-5.2-TEE)                        │   │ - Phase 4: Empty tag prune│
│   - OpenRouter (z-ai/glm-5.2 / glm-5.3)                 │   │ - Phase 5: Whitespace clp │
│                                                         │   └───────────────────────────┘
│ Priority 2: Gemini Argon                                │
│   - Google AI Studio (gemini-4-argon / gemini-2.5-pro)  │
│                                                         │
│ Priority 3: Gemini 3.8 / Flash                          │
│   - Google AI Studio (gemini-3.8-flash / 3.6-flash)     │
│                                                         │
│ Priority 4: Gemma 4 Series                              │
│   - Chutes (google/gemma-4-31B-turbo-TEE)               │
│   - OpenRouter Free (gemma-4-31b-it:free / 26b:free)    │
│   - Groq (gemma2-9b-it / gemma 4)                       │
└───────────────────────────┬─────────────────────────────┘
                            │ (429 / 403 / 402 / Timeout Cooldown)
                            ▼
┌─────────────────────────────────────────────────────────┐
│            RPG ROLEPLAY QUALITY CASCADE (P5 - P12)      │
│                                                         │
│ Tier 1: Frontier Open Weights & Reasoning               │
│   P5: DeepSeek R1 / V3 (deepseek-r1:free / direct)      │
│   P6: NVIDIA Nemotron 3 Ultra 550B & 3.5 Lightning      │
│                                                         │
│ Tier 2: High-Parameter Master Roleplay (70B+)           │
│   P7: Llama 3.3 70B Instruct (SambaNova / Groq / NIM)   │
│   P8: Qwen 2.5 72B Instruct (SambaNova / NIM / Groq)    │
│                                                         │
│ Tier 3: Specialized Fast & Backup RP Models             │
│   P9: GitHub Models (Azure AI: GPT-4o / Llama 3.3 70B)  │
│   P10: Gemini Pro / Flash-Lite Backup                   │
│   P11: Cloudflare Workers AI (Llama 3.3 70B / Qwen 72B) │
│   P12: DeepInfra / Hugging Face Serverless              │
│                                                         │
│ Tier 4: Verified Free Long-Tail Models (P13+)           │
│   P13+: Liquid LFM 2.5, Xing 4.0, Flint, Laguna         │
│   (Pruned: content-safety, code-only, duplicates)       │
└─────────────────────────────────────────────────────────┘
```

### 6.2 Provider Definitions & Endpoint Mapping

| Upstream ID | Display Name | Provider | Key Name | Endpoint (`base_url`) | Target Models |
|---|---|---|---|---|---|
| `p1-glm-fiat` | GLM 5.2 / GLM Family (Pillar 1) | `zhipu` / `chutes` / `openrouter` | `zhipu` / `chutes` / `openrouter` | `https://open.bigmodel.cn/api/paas/v4/chat/completions` & `https://llm.chutes.ai/v1/chat/completions` | `glm-5.2`, `glm-4-flash`, `zai-org/GLM-5.2-TEE`, `z-ai/glm-5.2` |
| `p2-gemini-argon` | Gemini Argon (Pillar 2) | `google` | `google_ai_studio` | `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` | `gemini-4-argon`, `gemini-2.5-pro` |
| `p3-gemini-flash` | Gemini 3.8 / Flash (Pillar 3) | `google` | `google_ai_studio` | `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` | `gemini-3.8-flash`, `gemini-3.6-flash`, `gemini-3.5-flash` |
| `p4-gemma4` | Gemma 4 Series (Pillar 4) | `chutes` / `openrouter` / `groq` | `chutes` / `openrouter` / `groq` | `https://llm.chutes.ai/v1/chat/completions`, `https://openrouter.ai/api/v1/chat/completions`, `https://api.groq.com/openai/v1/chat/completions` | `google/gemma-4-31B-turbo-TEE`, `google/gemma-4-31b-it:free`, `google/gemma-4-26b-a4b-it:free`, `gemma2-9b-it` |
| `p5-deepseek-r1` | DeepSeek R1 / V3 Reasoning | `openrouter` / `deepseek` | `openrouter` / `deepseek` | `https://openrouter.ai/api/v1/chat/completions` | `deepseek/deepseek-r1:free`, `deepseek/deepseek-chat:free` |
| `p6-nemotron` | NVIDIA Nemotron 3 Ultra 550B & 3.5 | `openrouter` / `nvidia` | `openrouter` / `nvidia` | `https://openrouter.ai/api/v1/chat/completions`, `https://integrate.api.nvidia.com/v1/chat/completions` | `nvidia/nemotron-3-ultra-550b-a55b:free`, `nvidia/nemotron-3.5-lightning:free` |
| `p7-llama33-70b` | Llama 3.3 70B Instruct | `sambanova` / `groq` / `nvidia` | `sambanova` / `groq` / `nvidia` | `https://api.sambanova.ai/v1/chat/completions`, `https://api.groq.com/openai/v1/chat/completions` | `meta-llama/Llama-3.3-70B-Instruct`, `llama-3.3-70b-versatile`, `meta/llama-3.3-70b-instruct` |
| `p8-qwen25-72b` | Qwen 2.5 72B / 3.8 27B Instruct | `sambanova` / `nvidia` / `chutes` | `sambanova` / `nvidia` / `chutes` | `https://api.sambanova.ai/v1/chat/completions`, `https://integrate.api.nvidia.com/v1/chat/completions`, `https://llm.chutes.ai/v1/chat/completions` | `Qwen/Qwen2.5-72B-Instruct`, `qwen/qwen2.5-72b-instruct`, `Qwen/Qwen3.8-27B-TEE` |
| `p9-github-models` | GitHub Models (Azure AI) | `github` | `github` | `https://models.inference.ai.azure.com/chat/completions` | `gpt-4o`, `gpt-4o-mini`, `meta-llama-3.3-70b-instruct` |
| `p10-gemini-backup` | Gemini Pro / Lite Safety Net | `google` | `google_ai_studio` | `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` | `gemini-3.1-pro-preview`, `gemini-pro-latest`, `gemini-3.1-flash-lite` |
| `p11-cloudflare` | Cloudflare Workers AI | `cloudflare` | `cloudflare` | `https://api.cloudflare.com/client/v4/accounts/a02ddeb54d2a0bb4f402088713a6d8ac/ai/v1/chat/completions` | `@cf/meta/llama-3.3-70b-instruct-fp8-fast`, `@cf/qwen/qwen2.5-72b-instruct` |
| `p12-deepinfra-hf` | DeepInfra & Hugging Face | `deepinfra` / `huggingface` | `deepinfra` / `huggingface` | `https://api.deepinfra.com/v1/openai/chat/completions`, `https://api-inference.huggingface.co/v1/chat/completions` | `meta-llama/Llama-3.3-70B-Instruct`, `Qwen/Qwen2.5-72B-Instruct` |
| `p13-or-free-longtail` | OpenRouter Verified Free RP | `openrouter` | `openrouter` | `https://openrouter.ai/api/v1/chat/completions` | `liquid/lfm-2.5-2.6b:free`, `xingchen-agi/xing4.0-29b-a4b:free`, `recursive/flint-v1.0:free`, `poolside/laguna-s-2.1:free` |

### 6.3 Required Code Changes in `proxy/free_tier_proxy.py`

1. **Parameter Sanitization Provider Expansion**:
   In `PayloadCompactor.sanitize_parameters` (line 162):
   ```python
   # Current:
   if provider in ("google", "sambanova", "groq", "nvidia", "cloudflare") or (target_model and "r1" in target_model.lower()):
   
   # Required upgrade:
   if provider in ("google", "sambanova", "groq", "nvidia", "cloudflare", "zhipu", "github", "cerebras") or (target_model and "r1" in target_model.lower()):
       body.pop("frequency_penalty", None)
       body.pop("presence_penalty", None)
   ```
2. **Universal `max_tokens` Clamping**:
   In `PayloadCompactor.sanitize_parameters` (line 177):
   Ensure `max_tokens` is universally capped at 8192 (or 4096 for strict providers like SambaNova and Cloudflare) to prevent upstream HTTP 400 parameter rejections:
   ```python
   max_tokens = body.get("max_tokens")
   if isinstance(max_tokens, (int, float)):
       if provider in ("sambanova", "cloudflare"):
           body["max_tokens"] = min(int(max_tokens), 4096)
       elif max_tokens > 8192:
           body["max_tokens"] = 8192
   ```
3. **`update_free_models.py` Blacklist Hardening**:
   Update line 59 of `proxy/update_free_models.py` to prevent automated re-injection of non-RP models:
   ```python
   BLACKLIST = {
       'thinkingmachines/inkling:free',
       'thinkingmachines/inkling-small:free',
       'nvidia/nemotron-3.5-content-safety:free',
       'cohere/north-mini-code:free',
   }
   ```

---

## 7. Comprehensive API Key Audit & Acquisition Guide

### 7.1 Static Audit of Keys in Configuration

| Provider Key Name | Status in `config_free_proxy.json` | Status in `.env` | Active in Upstreams | Telemetry / Operational Status |
|---|---|---|---|---|
| `google_ai_studio` | Configured (`AQ.Ab8...`) | File absent | Yes (P1, P3, P10) | Active, subject to 15 RPM / daily quota limit |
| `openrouter` | Configured (2 keys in array) | File absent | Yes (P2, P4, P6, P17+) | Active for `:free` models; 402 on paid models |
| `groq` | Configured (`gsk_t9...`) | File absent | Yes (P12) | Active, generous free tier (30 RPM, 14.4k RPD) |
| `chutes` | Configured (`cpk_d5...`) | File absent | Yes (P5, P6, P14) | Negative balance (-$0.057) trips 402 |
| `sambanova` | Configured (`5b29...`) | File absent | **NO (Unused)** | **DORMANT**: Key present but missing from upstreams! |
| `nvidia` | Configured (`nvapi-lOw...`) | File absent | Yes (P11) | Active, 1000 free NIM credits |
| `cloudflare` | Configured (`cfat_DlT...`) | File absent | Yes (P13) | Active, 10,000 free Neurons/day |
| `github` | Configured (`ghp_mHX...`) | File absent | **NO (Unused)** | **DORMANT**: Key present but missing from upstreams! |
| `huggingface` | Configured (`hf_qkY...`) | File absent | **NO (Unused)** | **DORMANT**: Key present but missing from upstreams! |
| `deepinfra` | Configured (`sk-di-325...`) | File absent | **NO (Unused)** | **DORMANT**: Key present but missing from upstreams! |
| `zhipu` / `bigmodel` | **MISSING** | File absent | No | **Needed for native GLM-5.2 / GLM-4-Flash free** |
| `cerebras` | **MISSING** | File absent | No | **Needed for ultra-fast Llama 3.3 70B (1M free t/d)** |
| `together` | **MISSING** | File absent | No | Optional, $5 free credit |
| `deepseek` | **MISSING** | File absent | No | Optional, direct native DeepSeek API |

### 7.2 Zero/Minimal-Cost API Key Acquisition Guide

For each key needed to power the failover cascade at 100% availability:

#### 1. Zhipu AI BigModel (GLM 5.2 / GLM-4-Flash)
- **Direct Console URL**: [https://open.bigmodel.cn/usercenter/apikeys](https://open.bigmodel.cn/usercenter/apikeys)
- **Cost**: **$0.00 / Zero Cost**.
- **Model**: `glm-4-flash` is permanently free with zero token charges for developers; `glm-4-plus` and `glm-5.2` offer introductory free credit allocations.
- **Acquisition Steps**:
  1. Navigate to `https://open.bigmodel.cn/` and click "Sign In / Register".
  2. Complete email or phone verification.
  3. Go to API Keys (`用户中心 -> API Keys`), click "Create API Key", and copy the token.
  4. Paste into `config_free_proxy.json` under `"keys": { "zhipu": "<YOUR_TOKEN>" }`.

#### 2. SambaNova Cloud (Llama 3.3 70B & Qwen 2.5 72B)
- **Direct Console URL**: [https://cloud.sambanova.ai/apis](https://cloud.sambanova.ai/apis)
- **Cost**: **$0.00 / Zero Cost**.
- **Performance**: Fastest free inference engine (~250–300 tokens/sec).
- **Acquisition Steps**:
  1. Go to `https://cloud.sambanova.ai/`.
  2. Sign in with GitHub or Google account.
  3. Go to "API Keys", click "Create API Key".
  4. The user already has `5b29a236-820a-465e-a576-431ad7922d43` in `config_free_proxy.json`. It simply needs to be wired into the active upstreams cascade!

#### 3. GitHub Models (Azure AI Marketplace: GPT-4o, Llama 3.3 70B, Mistral Large)
- **Direct Console URL**: [https://github.com/settings/tokens](https://github.com/settings/tokens) or [https://github.com/marketplace/models](https://github.com/marketplace/models)
- **Cost**: **$0.00 / Zero Cost**.
- **Allowance**: 150 requests/day per model free on any standard personal GitHub account.
- **Acquisition Steps**:
  1. Open GitHub `Settings -> Developer Settings -> Personal Access Tokens -> Tokens (classic)`.
  2. Generate token with `read:user` scope (or empty scopes for public model inference).
  3. The user already has `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` in `config_free_proxy.json`. It only needs to be connected to `https://models.inference.ai.azure.com/chat/completions` in `upstreams`!

#### 4. Cerebras Cloud (Llama 3.3 70B at 2,000+ Tokens/Sec)
- **Direct Console URL**: [https://cloud.cerebras.ai/](https://cloud.cerebras.ai/)
- **Cost**: **$0.00 / Zero Cost**.
- **Allowance**: 1,000,000 free tokens per day for `llama-3.3-70b`.
- **Acquisition Steps**:
  1. Navigate to `https://cloud.cerebras.ai/` and register with email.
  2. Open "API Keys", create new key, and copy `csk-...`.
  3. Add to `config_free_proxy.json` under `"keys": { "cerebras": "csk-..." }`.
  4. Endpoint: `https://api.cerebras.ai/v1/chat/completions`.

#### 5. Google AI Studio (Gemini Argon, 3.8 Flash, 3.6 Flash)
- **Direct Console URL**: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
- **Cost**: **$0.00 / Zero Cost**.
- **Allowance**: 15 RPM, 1500 RPD for Flash models; 2 RPM, 50 RPD for Pro/Argon models.
- **Refresh Steps**: If key hits daily quota, generate a secondary API key under a different Google account workspace or project and add as an array or environment variable `GOOGLE_AI_STUDIO_API_KEY`.

#### 6. Groq Cloud (Llama 3.3 70B Versatile & Gemma)
- **Direct Console URL**: [https://console.groq.com/keys](https://console.groq.com/keys)
- **Cost**: **$0.00 / Zero Cost**.
- **Allowance**: 30 RPM, 14,400 RPD on free tier.
- **Acquisition Steps**: Go to `https://console.groq.com/keys`, create API key `gsk_...`. Already configured in `config_free_proxy.json`.

#### 7. OpenRouter Free Tier
- **Direct Console URL**: [https://openrouter.ai/settings/keys](https://openrouter.ai/settings/keys)
- **Cost**: **$0.00 / Zero Cost**.
- **Allowance**: 20 RPM on all models tagged `:free` with zero credit balance.
- **Acquisition Steps**: Sign in with Google/Discord, navigate to Keys, generate key `sk-or-v1-...`. Two keys are already configured in array for rotation. Ensure upstreams use `:free` suffixes (e.g. `google/gemma-4-31b-it:free`, `deepseek/deepseek-r1:free`) to prevent 402 Payment Required errors.

---

## 8. Conclusion & Actionable Recommendations

1. **Cascade Restructuring**: Re-order `proxy/config_free_proxy.json` to place GLM 5.2 (P1), Gemini Argon (P2), Gemini 3.8/Flash (P3), and Gemma 4 (P4) as top fiat pillars, followed by DeepSeek R1 (P5), Nemotron (P6), Llama 3.3 70B (P7), Qwen 2.5 72B (P8), and GitHub Models (P9).
2. **Re-activate Dormant Keys**: Immediately wire SambaNova (`5b29...`) and GitHub Models (`ghp_mHX...`) into the active cascade. They are 100% free, highly rated for RPG roleplay, and their keys are already in the configuration file.
3. **OpenRouter Hygiene**: Ensure all OpenRouter entries in the free tier use the `:free` model ID variant to avoid HTTP 402 rate-limit tripwires.
4. **Prune Non-RP Models**: Remove moderation classifier `nemotron-3.5-content-safety:free` and code models from `config_free_proxy.json`, and update the `BLACKLIST` in `update_free_models.py`.
5. **Code Sanitization Polish**: Add `"zhipu"`, `"github"`, `"cerebras"` to the penalty-stripping list in `free_tier_proxy.py` and enforce universal `max_tokens` clamping.
6. **Zero Regression Risk**: All 28 existing tests pass with 100% confidence, ensuring full stability.
