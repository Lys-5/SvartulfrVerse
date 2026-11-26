# SCOPE — Character Scenarios Assembly, Validation & Deployment

## Target Milestone
Assemble, validate, and deploy the 6 thematic character scenarios for Svartúlfr Verse to Wyvern Web API with strict invariants.

## Scenarios Inventory
1. `Svartulfr_Scenario_Camp_Mystic.json` (8 slots, Lake Erie shuttle arrival, Lua script for supervisor/cabins, Edric 13yo, 4 greetings)
2. `Svartulfr_Scenario_SUCC_Route_Alyssa.json` (8 slots, Theta Iota Theta, Pre-Med labs, library smoking corner, rink, Bulls locker, 6 greetings)
3. `Svartulfr_Scenario_SUCC_Route_Jasper.json` (8 slots, Wyrm Hall 304, roof hacking, hallway, rave, BRO party, Cocketeers pool, 5 greetings)
4. `Svartulfr_Scenario_Villa_Douglas.json` (7 slots: 7 canonical male Douglas/Bloodmoon cards, 5 greetings)
5. `Svartulfr_Scenario_DMHA_Dungeons.json` (9 slots: Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, 4 greetings)
6. `Svartulfr_Scenario_Underworld_Sindacato.json` (6 slots: Ballantine vs Sinners, Jean-Luc Virtuoso [Human Telepath], Alicia, Dr. Arthur Sinclair, Sully, Ilya/Vasile, 4 greetings)

## Invariants & Guardrails
- **Visibility**: Tassativamente `"private"` (CRITICAL: NOT `"unlisted"`).
- **Format Discipline**:
  - Zero em-dashes (`—` or `–`) anywhere in titles, descriptions, greetings, or messages.
  - Spoken dialogue strictly in standard double quotes (`"..."`).
  - Actions and narration in plain text (no asterisks).
  - Asterisks reserved strictly for unvoiced internal thoughts (`*...*`).
  - Foreign phrases formatted as `"Original phrase"` followed by `([Italian translation])`.
- **Lorebooks**: All 6 standalone lorebook IDs attached to each scenario:
  `["_gwwCxCfQ6PQaLEjAQVpJL", "_HfG7TeV6MJyj6bxMwxkpt", "_9zWTGqYJNJ4BCDMj8gfcD", "_EjXxkmPVhpCXg8xABpFkK", "_zwEqgEEzh12X6gHVmMKKC", "_Uht3Ckz44JBDrPnUHq7LV"]`
- **Slots**:
  - `key`, `label`, `pool` array, and `unavailable_count: 0`.
  - For active standalone cards: pool with valid card ID and weight 100.
  - For Lorebook NPCs / open slots: pool `[]` (empty array, weight not applicable, unavailable_count: 0).
- **Greetings**:
  - Multi-message greeting parity: `greeting.content == messages[0].content` and `greeting.speaker_slot == messages[0].speaker_slot`.
  - Every `speaker_slot` in `messages` must be present in `slots[].key`.
  - No redundant hardcoded speaker prefixes inside message contents.
- **Character Invariants**:
  - Russell Sinclair and Scarlett Rose surnames verified.
  - Finnegan Novak explicitly specified as Arctic Wolf demi-human (one pair of animal ears, non-shifter).
  - Jean-Luc Virtuoso explicitly specified as Human Telepath.
  - Villa Douglas contains exactly the 7 canonical male cards.
- **Wyvern API Deployment**:
  - POST /api/character-scenarios for each scenario with `visibility: "private"`.
  - Verify HTTP 200 and valid IDs via GET.
  - Update `CHANGELOG.md`.

## Milestones & Status
| # | Step | Description | Status |
|---|------|-------------|--------|
| 1 | Survey & Discovery | Review explorer handoffs (1, 2, 3) | DONE |
| 2 | Implementation (Worker) | Generate 6 scenario JSON files, validate, deploy to Wyvern API, update CHANGELOG.md | IN_PROGRESS |
| 3 | Review (Reviewers) | Dual review of schema, files, and live Wyvern API state | PLANNED |
| 4 | Challenge (Challengers) | Adversarial checks on em-dashes, quotes, slot parity, unavailable_count, private visibility | PLANNED |
| 5 | Audit (Auditor) | Forensic integrity verification against cheat/facade | PLANNED |
| 6 | Gate & Handoff | Gate decision and final report to Sentinel | PLANNED |
