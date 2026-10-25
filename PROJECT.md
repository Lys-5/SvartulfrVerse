# Project: Svartúlfr Verse — World Simulation & VN Engine Optimization

## Architecture
- **World Core & Engine**: World `_YpX47fNraQFw2dD7TdycJ` ("Svartúlfr — Blackwood & Solarton") with World Clock epoch `827-12-21 00:00:00 UTC`, current age `10489902` (26 Aug 2024 06:00 UTC), full simulation engine (`rpg_stats`, `combat`, `inventory`, `currency`, `relationships`), and `world_features.vn_mode: true`.
- **Character Layer**: 13 Primary World Characters (`WorldCharacter` schema in MongoDB) embedded directly in the world with integer BigInt timeline parameters, Cloudflare CDN gallery avatars, full JED+ markdown descriptions, and balanced 25-point 6-stat RPG blocks (sum = 31, level = min(age, 99)).
- **Visual Novel & Scenario Layer**: Scenario `_2MTWKjxrQPdQVaz9y4Q7H` ("Welcome Day al Lunar Quad") with beat splitting syntax `=>Speaker:` parsed by frontend module 93312/nC to render character sprites and nameplates; active chat `chat_log_PJx1W1rg3WUzRM7MnQrkN` with message swipe patching.
- **Client & Display Configuration**: Chat overrides schema (`$`) with `vnMode: true`, `vnTextSpeed: "normal"`, `vnDirections: true`, `vnTextboxOpacity: 0.85`, right sidebar flags (`party_tied: true`, `auto_approve: false`, Stats tab character sheet loading).
- **Verification Layer**: Chrome DevTools Protocol (CDP) and headless Playwright browser inspection monitoring DOM rendering, network responses (HTTP 200), and console errors.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | 13 World Characters Deployment | Deploy Erik, Logan, Edric, Noah, Malachia, Jasper, Alyssa, Wulfnic, Zefir, Mackenzie, Finn, Sierra, Scarlett into World `_YpX47fNraQFw2dD7TdycJ` via `POST /api/worlds/characters` with BigInt birthdate, CDN avatars, JED+ profiles, and 25-pt RPG blocks. | M1 | Survey (Explorer 1) |
| 2 | Scenario Syntax Standardization | Standardize syntax to `=>Speaker:` across Scene 0, Scene 1, and Scene 2 in `FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json` and deploy via `PUT /api/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H`. | M2 | Survey (Explorer 2) |
| 3 | Active Chat Message #0 Patch | Patch message #0 swipe in `chat_log_PJx1W1rg3WUzRM7MnQrkN` via `PUT /api/new/chat-logs/swipe/message_swipe_99mmMgEEQjk2pkJN3hXkQ` with standardized `=>Speaker:` text. | M2 | Survey (Explorer 2) |
| 4 | VN Mode Display Settings | Configure Display Settings for Visual Novel Mode in `chat_overrides` on `chat_log_PJx1W1rg3WUzRM7MnQrkN` (`vnMode: true`, `vnDirections: true`, etc.). | M3 | Survey (Explorer 3) |
| 5 | Right Sidebar Flags Configuration | Enforce `party_tied: true` (scene/party auto-apply ON), `memory.memory_scan.auto_approve: false` (AI content creation OFF), and verify Stats tab character sheet loading. | M3 | Survey (Explorer 3) |
| 6 | Chrome DevTools Live Validation | Perform live browser inspection via CDP / Playwright on `https://app.wyvern.chat` verifying console logs, network requests, and DOM elements; fix errors autonomously. | M4 | Survey (Explorer 3) |
| 7 | Dual-Track E2E Test Suite & Audit | Execute comprehensive 4-tier E2E testing and forensic integrity audit. | M5 | Survey (Orchestrator) |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | World Characters Deployment | Deploy 13 Primary World Characters into World `_YpX47fNraQFw2dD7TdycJ` with BigInt timeline, CDN avatars, JED+ text, and balanced 25-pt RPG blocks. | none | DONE |
| 2 | Scenario & Chat Standardization | Standardize `=>Speaker:` in Scenario `_2MTWKjxrQPdQVaz9y4Q7H`, update local JSON, and patch Message #0 in `chat_log_PJx1W1rg3WUzRM7MnQrkN`. | none | DONE |
| 3 | Display Settings & Sidebar Flags | Configure `chat_overrides` for VN mode and enforce sidebar flags (`party_tied`, `auto_approve: false`). | M1, M2 | DONE |
| 4 | Chrome DevTools Live Validation | Execute live browser validation (DOM, console, network) on `app.wyvern.chat` and remediate any anomalies. | M1, M2, M3 | PLANNED |
| 5 | E2E Testing & Forensic Audit | Run full 4-tier test suite and forensic integrity audit for acceptance. | M1, M2, M3, M4 | PLANNED |

## Interface Contracts
### M1 ↔ World API (`POST /api/worlds/characters`)
- `world_id`: `_YpX47fNraQFw2dD7TdycJ`
- `name` / `display_name`: string
- `avatar`: HTTPS Cloudflare CDN URL
- `birthdate`: BigInt integer hours from 827-12-21
- `start_timeline_position`: BigInt integer hours
- `rpg_stats`: `{ enabled: true, level: min(age, 99), base_stats: { stat_1..6, might, resilience, agility, wit, presence, scouting } }` with sum = 31.

### M2 ↔ Wyvern Scenario & Chat Swipe API
- `PUT /api/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H`: full scenario JSON with `premade_scenes[i].scene_text` using `=>Speaker:` tags.
- `PUT /api/new/chat-logs/swipe/message_swipe_99mmMgEEQjk2pkJN3hXkQ`: `{ content: string }` with `=>Speaker:` tags, 0 em-dashes, 0 asterisks.

### M3 ↔ Chat Overrides API (`PUT /api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN`)
- `chat_overrides`: `{ version: 1, values: { vnMode: true, vnTextSpeed: "normal", vnDirections: true, vnAutoAdvance: false, vnAutoDelayMs: 2500, vnSkipRead: false, vnTextboxOpacity: 0.85, vnSpriteLimit: 3, vnItalicAsThought: false }, notes: {} }`

## Code Layout
- `FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json` (Scenario source of truth)
- `scripts/` (Operational scripts for deployment and verification)
- `scratch/` (Temporary diagnostics, inspection dumps, and test traces)
- `.agents/teamwork/` (Agent metadata, plans, and handoff reports)
