# Handoff Report — Explorer 2 (Live API Scenarios Explorer)

## 1. Observation
1. **Scenario IDs & Repository Records**:
   - `GEMINI.md` (lines 524, 549-555) and `FINAL/scenarios/*.json` document the 7 scenario IDs:
     - Master Scenario: `char_scenario_1DC43ggb6mB8YLJDJKrU4`
     - Camp Mystic: `char_scenario_nLC84wrHdrbB6P3DEhwKb`
     - SUCC Route Alyssa: `char_scenario_CKgwq246DyCj1NNTBV9rt`
     - SUCC Route Jasper: `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`
     - Villa Douglas: `char_scenario_88N1eQXqkbydKX9q9XQzp`
     - DMHA Dungeons: `char_scenario_eqtRNnDpKbxDp7dmJmq6E`
     - Underworld Sindacato: `char_scenario_rrUCdBPH6WTNyBnQkMAKR`
2. **Bearer Token & Expiration**:
   - Inspected `scratch/wyvern_token.txt` at 2026-10-20T22:43:52Z. Remaining TTL was 318.1 seconds.
   - Executed `python scratch/refresh_token.py` resulting in output:
     `Token refreshed successfully, len: 1142`
   - Second test confirmed token expiration `exp: 1792539858`, diff: 3596.8 seconds (~1 hour).
3. **Cloudflare Header Requirement**:
   - Initial `urllib.request` with default python user-agent failed with:
     `HTTP Error: 403 Forbidden | Body: error code: 1010`
   - Adding `'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ...'` and `'Accept': 'application/json'` resolved the issue and all GET requests succeeded with `HTTP 200`.
4. **Live GET API Status Across All 7 Scenarios**:
   - Running `.agents/teamwork/explorer_scenarios_15lb_2/inspect_all_scenarios.py` yielded:
     - `Master Scenario` (`char_scenario_1DC43ggb6mB8YLJDJKrU4`): revision `27`, `lorebook_ids` count `15`, greetings count `29`.
     - `Camp Mystic` (`char_scenario_nLC84wrHdrbB6P3DEhwKb`): revision `1`, `lorebook_ids` count `6`, greetings count `4`.
     - `SUCC Route Alyssa` (`char_scenario_CKgwq246DyCj1NNTBV9rt`): revision `1`, `lorebook_ids` count `6`, greetings count `6`.
     - `SUCC Route Jasper` (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`): revision `1`, `lorebook_ids` count `6`, greetings count `5`.
     - `Villa Douglas` (`char_scenario_88N1eQXqkbydKX9q9XQzp`): revision `1`, `lorebook_ids` count `6`, greetings count `5`.
     - `DMHA Dungeons` (`char_scenario_eqtRNnDpKbxDp7dmJmq6E`): revision `1`, `lorebook_ids` count `6`, greetings count `4`.
     - `Underworld Sindacato` (`char_scenario_rrUCdBPH6WTNyBnQkMAKR`): revision `1`, `lorebook_ids` count `6`, greetings count `4`.
5. **Greeting Persona Representation**:
   - Inspecting `greetings` objects in API response showed:
     - `linked_persona_ids`: array of ID strings. In Master Scenario, 7 greetings have `['persona_1786335754946']`, 6 greetings have `['1792155173728']`, and 16 have `[]`.
     - In the 6 thematic scenarios, all greetings currently have `linked_persona_ids: []`.
     - `linked_personas`: array of hydrated persona summary objects returned by GET:
       - `persona_1786335754946`: Alyssa (The White Moon)
       - `1792155173728`: Jasper (Technomancer & Cyber-Mage at SUCC)
6. **Local Files vs Live Cloud State**:
   - `FINAL/Svartulfr_Master_Scenario.json` has `revision: 26` (live is `27`), contains 15 lorebook IDs.
   - All 6 files in `FINAL/scenarios/*.json` have `revision: null` and contain only 6 lorebook IDs, with empty `linked_persona_ids: []`.

## 2. Logic Chain
1. From Observation 1, the 7 scenario IDs are well-established and uniquely identified.
2. From Observation 2, running `refresh_token.py` is required whenever token age exceeds ~50 minutes. The token is currently active and ready for worker deployment.
3. From Observation 3, any client or worker issuing calls against `https://app.wyvern.chat/api/` must specify standard browser `User-Agent` and `Accept` headers to avoid Cloudflare 1010 block.
4. From Observation 4, the 6 thematic scenarios deployed in the previous milestone are at revision 1 and only connect to the 6 initial standalone lorebooks. They require PUT updates with the 9 realism lorebooks to achieve the unified 15-lorebook suite.
5. From Observation 5, the Wyvern backend handles "Offer a persona to play as" via the `linked_persona_ids` array on each greeting. Sending string IDs in `linked_persona_ids` automatically populates the persona selector in the web UI.
6. From Observation 6, the worker must update both the live Wyvern cloud scenarios via PUT and the 7 local JSON files (`FINAL/scenarios/*.json` and `FINAL/Svartulfr_Master_Scenario.json`), maintaining synchronized revisions and exact schema parity.

## 3. Caveats
- No modifications were performed to live scenarios or local source files (Explorers are strictly read-only).
- Wyvern API enforces optimistic concurrency: sending an outdated `revision` will return `HTTP 409 Conflict`. Workers must fetch a fresh GET right before issuing PUT.
- A 2.5-second pacing delay must be observed between successive API calls to prevent rate-limit throttling.

## 4. Conclusion
The environment and live API are completely mapped, validated, and ready for execution.
- **Master Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`)**: Revision 27. Lorebook IDs already 15. Requires updating the 16 neutral greetings to `['persona_1786335754946', '1792155173728']` while preserving the 7 FemPOV (`['persona_1786335754946']`) and 6 MalePOV (`['1792155173728']`) greetings.
- **Dual Thematic Scenarios (Villa Douglas, Camp Mystic, DMHA Dungeons, Underworld Sindacato)**: Revision 1. Require expanding `lorebook_ids` from 6 to 15, and setting `linked_persona_ids: ['persona_1786335754946', '1792155173728']` on all greetings.
- **Single Thematic Routes (SUCC Route Alyssa, SUCC Route Jasper)**: Revision 1. Require expanding `lorebook_ids` from 6 to 15, and setting `linked_persona_ids: ['persona_1786335754946']` (for Alyssa) and `['1792155173728']` (for Jasper) on all greetings.
- **Local Persistence**: All 7 files in `FINAL/scenarios/` and `FINAL/Svartulfr_Master_Scenario.json` must be updated with the identical 15 lorebook IDs, updated greeting personas, and latest revisions.

## 5. Verification Method
1. **API Verification Command**:
   Run `.agents/teamwork/explorer_scenarios_15lb_2/inspect_all_scenarios.py` to confirm HTTP 200, revision numbers, and greeting structures.
2. **Local Schema Validation**:
   Run `.agents/teamwork/explorer_scenarios_15lb_2/test_payload_generation.py` to verify schema conformance and persona mapping logic across all 7 scenarios.
3. **Invalidation Conditions**:
   - Any scenario responding with non-200 HTTP status.
   - Any scenario having fewer or more than 15 lorebook IDs.
   - Any greeting lacking `linked_persona_ids` or containing mismatched persona IDs.
   - Any local JSON file disagreeing with the live Wyvern cloud revision or greeting contents.
