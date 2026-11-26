# Project: Svartúlfr Verse Thematic Character Scenarios

## Architecture
- Target Scenario JSON files located in `FINAL/scenarios/`:
  1. `Svartulfr_Scenario_Camp_Mystic.json` (8 slots, Lake Erie shuttle arrival, Lua startup script)
  2. `Svartulfr_Scenario_SUCC_Route_Alyssa.json` (8 slots, Theta Iota Theta, Pre-Med, 6 greetings)
  3. `Svartulfr_Scenario_SUCC_Route_Jasper.json` (8 slots, Wyrm Hall 304, Cocketeers pool, 5 greetings)
  4. `Svartulfr_Scenario_Villa_Douglas.json` (7 slots, 7 canonical male Douglas/Bloodmoon, 5 greetings)
  5. `Svartulfr_Scenario_DMHA_Dungeons.json` (9 slots, Kakihara card excerpts, 4 greetings)
  6. `Svartulfr_Scenario_Underworld_Sindacato.json` (6 slots, Jean-Luc Virtuoso Human Telepath, 4 greetings)
- Standalone Lorebook IDs attached to every scenario:
  - `_gwwCxCfQ6PQaLEjAQVpJL` (Lorebook I)
  - `_HfG7TeV6MJyj6bxMwxkpt` (Lorebook II)
  - `_9zWTGqYJNJ4BCDMj8gfcD` (Lorebook III)
  - `_EjXxkmPVhpCXg8xABpFkK` (Location)
  - `_zwEqgEEzh12X6gHVmMKKC` (NPC Primary)
  - `_Uht3Ckz44JBDrPnUHq7LV` (NPC Secondary)
- API Endpoints:
  - `POST https://app.wyvern.chat/api/character-scenarios` (deploy scenario with `visibility: "private"`)
  - `GET https://app.wyvern.chat/api/character-scenarios/{id}` (verify live status, slots, greetings, lorebooks)
- Auth: `scratch/wyvern_token.txt` (via `python scratch/refresh_token.py` if needed)
- Output Artifacts: `FINAL/scenarios/*.json`, `CHANGELOG.md`

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Camp Mystic Scenario | 8 slots, Lake Erie shuttle arrival, Lua startup script, 4 greetings | M2 | ORIGINAL_REQUEST §R1.1 |
| 2 | SUCC Route Alyssa Scenario | 8 slots, Finnegan Novak Arctic Wolf demi-human, 6 greetings | M2 | ORIGINAL_REQUEST §R1.2 |
| 3 | SUCC Route Jasper Scenario | 8 slots, Russ Sinclair, Scarlett Rose, Echo, Cocketeers, 5 greetings | M2 | ORIGINAL_REQUEST §R1.3 |
| 4 | Villa Douglas Scenario | 7 slots (7 canonical male Douglas/Bloodmoon), 5 greetings | M2 | ORIGINAL_REQUEST §R1.4 |
| 5 | DMHA Dungeons Scenario | 9 slots, Kakihara card excerpts, 4 greetings | M2 | ORIGINAL_REQUEST §R1.5 |
| 6 | Underworld Sindacato Scenario | 6 slots, Jean-Luc Virtuoso Human Telepath, 4 greetings | M2 | ORIGINAL_REQUEST §R1.6 |
| 7 | Lorebook Attachments | Attach all 6 standalone lorebook IDs to every scenario | M2 | ORIGINAL_REQUEST §R1 |
| 8 | Formatting Discipline | Zero em-dashes, standard dialogue quotes, plain text actions | M3 | ORIGINAL_REQUEST §R2 |
| 9 | Schema Invariants | Slot schema (`key`, `label`, `pool`, `unavailable_count: 0`), greetings format | M3 | ORIGINAL_REQUEST §R2 |
| 10 | Live Deployment | POST to Wyvern API with Bearer token, capture scenario IDs | M4 | ORIGINAL_REQUEST §R3 |
| 11 | Live Verification | GET from Wyvern API, verify HTTP 200 and schema integrity | M4 | ORIGINAL_REQUEST §R3 |
| 12 | Changelog Documentation | Update CHANGELOG.md with scenario IDs and metadata | M5 | ORIGINAL_REQUEST §R3 |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Survey & Discovery | Inspect schema requirements, existing scenario examples, card IDs, tokens | none | DONE |
| 2 | Payload Assembly | Construct 6 complete scenario JSON files in FINAL/scenarios/ | M1 | IN_PROGRESS |
| 3 | Verification & Forensic Audit | Audit schema invariants, em-dashes, dialogue format, canon constraints | M2 | PLANNED |
| 4 | Live Wyvern Deployment | Deploy scenarios via POST /api/character-scenarios and verify via GET | M3 | PLANNED |
| 5 | Changelog & Final Wrap-up | Document all scenario IDs and metadata in CHANGELOG.md | M4 | PLANNED |

## Code Layout & File Boundaries
- Output scenario directory: `FINAL/scenarios/`
- Reference character cards / lore: `ARCHIVIO/`, `FINAL/`, `scratch/`
- Authentication / Token scripts: `scratch/wyvern_token.txt`, `scratch/refresh_token.py`
- Deployment scripts / logs: `scratch/`
- Changelog: `CHANGELOG.md`
- Working metadata: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_2\`
