# DISPATCH — Worker Scenarios 1

## Mission
Implement, assemble, validate, and deploy the 6 thematic character scenarios for Svartúlfr Verse to the Wyvern Web API with strict invariants.

## Working Directory
`e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_1`

## Mandatory Documents to Read
- `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (Read in full!)
- `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_4\SCOPE.md`
- `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_1\handoff.md`
- `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_2\handoff.md`
- `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_3\handoff.md`

## Invariants & Critical Requirements
1. **CRITICAL USER DIRECTIVE**:
   Impostare tassativamente la visibilità di tutti e 6 i Character Scenario come `"private"` (`visibility: "private"`), non "unlisted".
   Assicurarsi che nei payload JSON generati in `FINAL/scenarios/` e nelle chiamate POST/PUT all'API Wyvern il campo visibility sia tassativamente `"private"`.
2. **Zero Em-Dashes**:
   Zero em-dashes (`—` or `–`) anywhere in titles, descriptions, scenario prompt, greetings, or message contents. Use commas or periods instead.
3. **Dialogue & Narration Formatting**:
   Spoken dialogue strictly in standard double quotes (`"..."`). Actions and narration in plain text (no asterisks). Asterisks reserved strictly for unvoiced internal thoughts (`*...*`).
4. **Standalone Lorebooks**:
   Attach all 6 standalone lorebook IDs to every scenario:
   `["_gwwCxCfQ6PQaLEjAQVpJL", "_HfG7TeV6MJyj6bxMwxkpt", "_9zWTGqYJNJ4BCDMj8gfcD", "_EjXxkmPVhpCXg8xABpFkK", "_zwEqgEEzh12X6gHVmMKKC", "_Uht3Ckz44JBDrPnUHq7LV"]`
5. **Slots & Availability**:
   - Every slot: `key`, `label`, `pool` array, and `unavailable_count: 0`.
   - Standalone cards in pool: weight 100.
   - Lorebook NPC / open slots: `pool: []` (empty array, unavailable_count: 0).
6. **Multi-Message Greetings**:
   - `greeting.content` must exactly match `greeting.messages[0].content`.
   - `greeting.speaker_slot` must exactly match `greeting.messages[0].speaker_slot`.
   - Every message in `messages` must have a `speaker_slot` present in `slots[].key`.
   - No redundant manual speaker prefixes (e.g. `Rory Ballantine: ...`) inside message content.
7. **Character Invariants**:
   - Surnames verified: Russell Sinclair (`_wn6DkCcg3Xqa2Xpx9ttnT`), Scarlett Rose (`_qXgBMbFYJfc84hbLHhe92`).
   - Finnegan Novak explicitly specified as Arctic Wolf demi-human (one pair of animal ears, non-shifter).
   - Jean-Luc Virtuoso explicitly specified as Human Telepath.
   - Villa Douglas contains exactly the 7 canonical male cards (`father`, `eldest_brother`, `tech_brother`, `politician_brother`, `maternal_grandfather`, `uncle`, `cousin`).
   - DMHA scenario 9 slots: Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, DMHA strike team / Nomads.
   - Camp Mystic: Lake Erie shuttle arrival, Marcus Vale / Celeste Nadir, Mara Voss, Edric 13yo, Lua startup script.
8. **Wyvern API Deployment**:
   - Use token from `scratch/wyvern_token.txt` (or run `python scratch/refresh_token.py` if needed).
   - POST to `https://app.wyvern.chat/api/character-scenarios` with standard browser User-Agent header, `visibility: "private"`, and 2.5s pacing delay.
   - Verify HTTP 200 for all 6 scenarios and query GET `/api/character-scenarios/{id}` to verify fields.
   - Update `CHANGELOG.md` with scenario IDs, slot counts, and deployment details.

## File Ownership
You own:
- `FINAL/scenarios/*.json`
- `scratch/build_and_deploy_6_scenarios.py` (and any helper/validation scripts you create)
- `CHANGELOG.md`

## MANDATORY INTEGRITY WARNING
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
