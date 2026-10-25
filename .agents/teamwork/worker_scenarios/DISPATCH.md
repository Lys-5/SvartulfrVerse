# Dispatch Record — Worker Scenarios

Working directory: `e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios`

## 2026-10-20T17:27:06Z
Sender: 6f2f7fce-1035-4880-af5b-6087c18617c4 (orchestrator_2)
Content:
You are the Assembly Worker for the Svartúlfr Verse Character Scenarios milestone.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios

MANDATORY FIRST STEP: Read the authoritative requirements in:
e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (specifically the latest Follow-up — 2026-10-20T17:04:21Z and 2026-10-20T17:24:49Z).
Read the comprehensive Explorer handoff reports:
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_1\handoff.md (Schema & API)
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_2\handoff.md (Scenarios 1-4 Rosters & Greetings)
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_3\handoff.md (Scenarios 5-6 Rosters & Excerpts)

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

CRITICAL INVARIANTS:
1. All 6 scenarios must set "visibility": "private" (CRITICAL USER DIRECTIVE! Do NOT use "unlisted").
2. Zero em-dashes ('—' or '–') anywhere in the JSON files (titles, descriptions, greetings, messages). Use commas or periods.
3. Spoken dialogue strictly in standard double quotes ("..."). Actions and narration in plain text (no asterisks). Asterisks reserved strictly for unvoiced internal thoughts (*...*).
4. All 6 standalone lorebook IDs attached to every scenario:
   ["_gwwCxCfQ6PQaLEjAQVpJL", "_HfG7TeV6MJyj6bxMwxkpt", "_9zWTGqYJNJ4BCDMj8gfcD", "_EjXxkmPVhpCXg8xABpFkK", "_zwEqgEEzh12X6gHVmMKKC", "_Uht3Ckz44JBDrPnUHq7LV"]
5. Every slot must have: `key`, `label`, `pool` array, and `unavailable_count: 0`.
   - Verified active cards (14 canonical characters) use: `pool: [{"character_id": "<card_id>", "weight": 100}]`.
   - NPCs/open roles use: `pool: []` (empty array) so that `unavailable_count` is 0.
6. Greetings structure:
   - Root `greeting.content` must exactly match `greeting.messages[0].content`.
   - Root `greeting.speaker_slot` must exactly match `greeting.messages[0].speaker_slot`.
   - Every message in `messages` must have a `speaker_slot` present in `slots[].key`.
   - No hardcoded speaker prefixes (e.g. "Santiago Herrera: ...") inside message contents.
7. Character Constraints:
   - Russ Sinclair and Scarlett Rose surnames verified.
   - Finnegan Novak explicitly specified as Arctic Wolf demi-human (one pair of animal ears, non-shifter).
   - Jean-Luc Virtuoso explicitly specified as Human Telepath.
   - Villa Douglas contains exactly the 7 canonical male Douglas/Bloodmoon card holders:
     * father: Erik Ulfr Douglas (_QPea6g4Q1QfeYCVHCLMPR)
     * eldest_brother: Malachia Björn Douglas Bloodmoon (_RDfz7XzTpM23LpPALVXHM)
     * tech_brother: Jasper Svartr Douglas Bloodmoon (_t4J9aQNJM36cUKAP4wB4U)
     * politician_brother: Noah Loki Douglas Bloodmoon (_zFLUjV8aVxQRAfQxGcAcY)
     * maternal_grandfather: Wulfnic Báleygr Bloodmoon (_HEQQbbRFwKdG8QE2Fh1z1)
     * uncle: Logan Járn Douglas (_T8Ywcr9FEqNf9JxbK6eHP)
     * cousin: Edric Douglas (_TbRM3EdxDjHFgqztTbCpL)
   - DMHA scenario 9 slots: Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, DMHA strike team / Nomads.
   - Camp Mystic: Lake Erie shuttle arrival, Marcus Vale / Celeste Nadir, Mara Voss, Edric (13yo), Lua startup script.

FILES TO CREATE:
Directory: `FINAL/scenarios/`
1. `FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json`
2. `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json`
3. `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json`
4. `FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json`
5. `FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json`
6. `FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json`

VALIDATION:
Write and execute a validation test script (e.g. in `scratch/test_validate_scenarios.py`) that checks:
- All 6 files exist and are valid JSON.
- All 6 files have `visibility == "private"`.
- Zero em-dashes across all 6 files.
- All slot keys, labels, pools, and `unavailable_count: 0`.
- All greetings and messages have matching content/speaker_slot and valid slots.
- All 6 lorebook IDs present in every file.
- Verify character invariant requirements (surnames, species, 7 males, etc.).

Report the exact validation commands and results in your handoff report:
`e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios\handoff.md`.
When finished, send a message to orchestrator_2 via send_message.
