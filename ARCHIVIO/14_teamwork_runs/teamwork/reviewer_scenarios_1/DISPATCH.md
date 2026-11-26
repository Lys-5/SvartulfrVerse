# DISPATCH — Reviewer Scenarios 1

## Mission
Conduct an objective and rigorous review of the 6 character scenario JSON files in `FINAL/scenarios/` and `scratch/build_and_deploy_6_scenarios.py`.

## Working Directory
`e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_1`

## Mandatory Documents to Read
- `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (Authoritative requirements)
- `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_4\SCOPE.md`
- `e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_1\handoff.md`

## Review Focus
1. **Schema & JSON Structure**:
   - Verify all 6 files in `FINAL/scenarios/` parse as valid JSON.
   - Check all required fields: `name`, `display_description`, `avatar`, `tags`, `visibility`, `rating`, `scenario`, `startup_script`, `slots`, `greetings`, `lorebook_ids`.
2. **Invariants**:
   - `visibility: "private"` (NOT "unlisted").
   - Zero em-dashes (`\u2014`) or en-dashes (`\u2013`) in all strings.
   - Dialogue strictly in `"..."`, actions/narration in plain text (no asterisks), asterisks only for internal thoughts (`*...*`).
   - All 6 standalone lorebook IDs attached:
     `["_gwwCxCfQ6PQaLEjAQVpJL", "_HfG7TeV6MJyj6bxMwxkpt", "_9zWTGqYJNJ4BCDMj8gfcD", "_EjXxkmPVhpCXg8xABpFkK", "_zwEqgEEzh12X6gHVmMKKC", "_Uht3Ckz44JBDrPnUHq7LV"]`
   - Every slot: `key`, `label`, `pool` array, and `unavailable_count: 0`.
   - Multi-message greeting parity: root content and speaker_slot match messages[0]. No redundant speaker name prefixes in message contents.
3. **Character Specifics**:
   - Russell Sinclair and Scarlett Rose surnames verified.
   - Finnegan Novak explicitly specified as Arctic Wolf demi-human.
   - Jean-Luc Virtuoso explicitly specified as Human, Telepath.
   - Villa Douglas contains exactly the 7 canonical male cards.
   - DMHA scenario contains 9 slots: Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, DMHA strike team / Nomads.
   - Camp Mystic contains Lake Erie shuttle arrival, Marcus Vale / Celeste Nadir, Mara Voss, Edric 13yo, Lua startup script.

## Deliverables
- Execute tests (e.g. `python scratch/test_6_scenarios_adversarial.py`).
- Write report to `e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_1\handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`.
- Send message back to orchestrator.

## 2026-10-20T17:49:45Z
From: be560f41-366c-4523-9cb0-8842aafd8c44
Content:
You are reviewer_scenarios_1, the Schema & JSON Invariants Reviewer.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_1
Project directory: e:\repository\SvartulfrVerse

READ MANDATORY DOCUMENTS FIRST:
- e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
- e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_4\SCOPE.md
- e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_1\DISPATCH.md
- e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_1\handoff.md

TASK:
1. Review all 6 JSON files in FINAL/scenarios/:
   - Svartulfr_Scenario_Camp_Mystic.json
   - Svartulfr_Scenario_SUCC_Route_Alyssa.json
   - Svartulfr_Scenario_SUCC_Route_Jasper.json
   - Svartulfr_Scenario_Villa_Douglas.json
   - Svartulfr_Scenario_DMHA_Dungeons.json
   - Svartulfr_Scenario_Underworld_Sindacato.json
2. Check schema structure and all invariants:
   - "visibility": "private" (CRITICAL: MUST BE "private")
   - Zero em-dashes ('\u2014' or '\u2013') in any text
   - Dialogue enclosed strictly in standard double quotes ("..."), actions and narration in plain text (no asterisks), asterisks only for internal thoughts (*...*)
   - All 6 standalone lorebook IDs attached
   - Every slot: key, label, pool array, unavailable_count: 0
   - Multi-message greeting parity with messages[0]
   - No redundant speaker prefixes in message contents
3. Execute validation suite (e.g. python scratch/test_6_scenarios_adversarial.py).
4. Write your handoff report to e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_1\handoff.md with explicit verdict: APPROVE or REQUEST_CHANGES.
5. Send a completion message back to orchestrator via send_message.

