---
name: multi-model-unified-pipeline
description: >-
  Orchestrates the unified 5-stage Daily Master Pipeline (daily-master-pipeline)
  across a 3-Tier Multi-Model Team, Open-Provider Plug & Play Registry, Local
  Proxy (:5005), and the 5 PC OMEN Desktop AI Clients (Antigravity.exe,
  Gemini.exe, Grok Bot.exe, Claude.exe, copilotapp.exe) with an interactive
  HTML Telemetry Dashboard.
---

# Multi-Model Unified Pipeline & PC OMEN AI Fleet Orchestrator

## Overview

Unifies the 4 daily maintenance and lore enrichment automations (`daily-character-enrichment`, `daily-wyvern-monitor`, `daily-proxy-free-models`, `daily-omnisync-archive-mining`) into a single atomic **5-Stage Master Pipeline** (`daily-master-pipeline`, scheduled at `09:00 Europe/Rome`).

Every stage is routed through a **3-Tier Multi-Model Matrix** plus **2 Dedicated Desktop Specialist Policies** defined in [`references/models_registry.json`](references/models_registry.json):
- **Tier 1 (`scout-fast`)**: Primary IDE `gemini-3.8-flash` (effort `low`/`medium`, subagent `flash`/`flash_lite`), Twin Proxy `:5005` `gemma-4-31B-it` & `qwen-3.8-27b`, Desktop Client `copilotapp.exe`. Runs **Stage 0** (`vault_health_check.py` + PC OMEN AI Clients scan), **Stage 1A** (`daily_wyvern_platform_monitor.py`), and **Stage 1B** (`proxy/update_free_models.py`).
- **Tier 2 (`architect-sync`)**: Primary IDE `gemini-4-argon` & `claude-sonnet-5.5` (effort `medium`, subagent `inherit`), Twin Proxy `:5005` `z-ai/glm-5.3` & `deepseek-chat`, Desktop Clients `copilotapp.exe` & `Claude.exe`. Runs **Stage 2** (`daily_omnisync_archive_mining.py --skip-mining` for byte-for-byte `entries == lexicon` parity and Wyvern scenario slot checks).
- **Tier 3 (`lore-judge`)**: Primary IDE `claude-opus-5.5` & `gemini-4-argon` (effort `high`, subagent `pro`), Twin Proxy `:5005` `nvidia/nemotron-3-ultra-550b-a55b:free` / `z-ai/glm-5.3` / `deepseek-chat`, Desktop Client `Claude.exe`. Runs **Stage 3A** (`daily_character_enrichment.py` for active chat monitor + NPC enrichment) and **Stage 3B** (`archive_mining_engine.py` for historical lore recovery).
- **Dedicated Specialist — `Grok Bot.exe` / Groky Ecosystem (`groky_agenda_work_slots`)**: Hosts **Groky** (main coordinator for Gmail, Google Calendar Agenda with Italian/Ásatrú holidays and Davide's color legend, Google Home 10:00 wake-up, Meals) and sub-bots (`Hubby Groky`, `Purrky` for cats Rocky & Tatina at 19:30, `Game Groky`, `Code Groky` for dev/design projects, `Hire Me Groky`). Reserved **exclusively** in this workspace for proposing worldbuilding work-slot blocks in the user's Agenda via **Groky / Code Groky** (`agenda_work_slot`, `work_slot_blocking`, `worldbuilding_schedule`), strictly honoring Groky's golden rule: **nothing is sent or deleted without explicit user approval**.
- **Dedicated Specialist — `Gemini.exe` (`visual_studio_argon_images`)**: Reserved **exclusively** for Image & Visual Asset Generation via **Gemini 4 Argon** (`image_generation`, `visual_asset_creation`, `character_portrait`, `location_background`).
- **Stage 4 (`telemetry-archival`)**: Generates the interactive self-contained HTML Telemetry Dashboard (`scratch/unified_pipeline_dashboard.html`), writes the unified Markdown report (`scratch/daily_maintenance_report.md` and `logs/automations/`), and archives the session transcript via `scripts/archive_automation_chat.py --automation daily-master-pipeline`.

## Dependencies

This skill coordinates and references the following installed skills:
- **`automation`**: Manages the single scheduled sidecar `~/.gemini/config/sidecars/daily-master-pipeline/sidecar.json` (`CRON_TZ=Europe/Rome 0 9 * * *`).
- **`auto-loop`**: Master self-learning and multi-perspective execution workflow (`FASE 1..4`).
- **`wyvern-ai-proxy-rotator`**: Local FastAPI OpenAI-compatible proxy (`http://127.0.0.1:5005/v1/chat/completions`) with 40s-60s circuit-breaker failover across curated RPG models.
- **`wyvern-chat-audit-world-sync`**: Forensic audit of active Wyvern simulation chats (`chat_log_ftrtAD79eddk9Ue9Jr2WJ`) and World/Lorebook parity.
- **`chrome-devtools`**: Live DOM, Console, and Network inspection of the generated HTML Telemetry Dashboard (`scratch/unified_pipeline_dashboard.html`).

## Quick Start

Run the full 5-stage pipeline and generate the interactive HTML dashboard:

```powershell
uv run python .agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py run-all --limit 5 --output scratch/unified_pipeline_run.json
```

Scan active PC OMEN Desktop AI Clients (`Antigravity.exe`, `Gemini.exe`, `Grok Bot.exe`, `Claude.exe`, `copilotapp.exe`) and Local Proxy `:5005`:

```powershell
uv run python .agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py detect-clients --limit 20 --output scratch/omen_ai_clients_status.json
```

## Utility Scripts

All commands are exposed via `.agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py` and write structured output to `--output`.

### 1. `detect-clients`
Scans Windows processes on PC OMEN for registered Desktop AI clients, verifies Local Proxy `:5005` health and upstream count, and lists IDE models and external Plug & Play providers.

```powershell
uv run python .agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py detect-clients --limit 20 --output scratch/omen_ai_clients_status.json
```

### 2. `route-model`
Resolves the optimal Tier, primary IDE model, subagent type, normalized reasoning effort payload (`low`, `medium`, `high`), twin fallback model on `:5005`, and desktop client status.

```powershell
uv run python .agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py route-model --task-type lore_synthesis --effort high --output scratch/route_decision.json
```

### 3. `run-tier`
Executes only the stages assigned to Tier `1`, `2`, or `3` with automatic horizontal fallback.

```powershell
uv run python .agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py run-tier --tier 1 --limit 5 --output scratch/tier1_run.json
```

### 4. `run-all`
Executes the complete 5-stage unified pipeline (Stage 0, Stage 1A, Stage 1B, Stage 2, Stage 3A, Stage 3B, and Stage 4 Telemetry/Dashboard).

```powershell
uv run python .agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py run-all --limit 5 --output scratch/unified_pipeline_run.json
```

### 5. `dashboard`
Generates the self-contained interactive HTML Telemetry Dashboard (`scratch/unified_pipeline_dashboard.html`).

```powershell
uv run python .agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py dashboard --output scratch/unified_pipeline_dashboard.html
```

## Workflow

1. **Detect Fleet & Proxy Readiness**: Run `detect-clients --limit 20 --output scratch/omen_ai_clients_status.json` to inspect running PIDs for `Antigravity.exe`, `Gemini.exe`, `Grok Bot.exe`, `Claude.exe`, `copilotapp.exe`, and `:5005` upstreams.
2. **Execute Unified Master Pipeline**: Run `run-all --limit 5 --output scratch/unified_pipeline_run.json` (or invoke `python scripts/daily_maintenance_runner.py`).
3. **Inspect Telemetry Dashboard**: Generate or refresh `scratch/unified_pipeline_dashboard.html` via `dashboard --output scratch/unified_pipeline_dashboard.html` and verify via `chrome-devtools`.
4. **Archive Automation Transcript**: Run `python scripts/archive_automation_chat.py --automation daily-master-pipeline` to store the raw `.jsonl` transcript and formatted Markdown log in `logs/automations/`.

## Rate Limiting

- **Cross-Process File Lock & Monotonic Clock**: `CrossProcessRateLimiter` uses `time.monotonic()` (never `time.time()`) and coordinates across concurrent subagents via `scratch/.multi_model_rate_limit.lock` (`2.0 req/s`, minimum `0.5s` spacing).
- **HTTP 429 (`RateLimitError`) & 5xx Exponential Backoff**: Transient 5xx errors retry with exponential backoff (`1s`, `2s`, `4s`). Receiving HTTP 429 after retries raises `RateLimitError` and triggers horizontal failover to the Tier's twin model on Local Proxy `:5005`.

## Common Mistakes

1. **Omitting `--limit` or `--output` on CLI invocations**: Both `--limit` (on batch/list commands) and `--output` are mandatory to prevent silent truncation or context window bloat.
2. **Re-creating separate cron sidecars**: Never split the daily tasks back into 4 separate sidecars (`09:00`, `09:15`, `09:30`, `10:00`). Keep all daily stages unified inside `daily-master-pipeline` to eliminate redundant cold-start overhead.
3. **Using `schedule` tool instead of `sidecar.json`**: Always configure persistent schedules in `~/.gemini/config/sidecars/daily-master-pipeline/sidecar.json` with `"builtin": "schedule"` and `"restart_policy": "always"`.
