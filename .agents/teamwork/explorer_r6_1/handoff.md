# Handoff Report — Explorer R6-1

**Task**: Investigation of R1 (Wyvern API Live Sync, Local Scenario Files & Archive Mapping) and R2 (Greeting Macro Optimizations, Slot/Pool Configurations & Speaker Slots)
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1`
**Author**: Explorer R6-1 (`teamwork_preview_explorer`)
**Target Entities**:
- `char_scenario_CKgwq246DyCj1NNTBV9rt` (SUCC Route Alyssa)
- `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` (SUCC Route Jasper)
- `FINAL/scenarios/` and `ARCHIVIO/scenarios/`

---

## 1. Observation

1. **Wyvern Token & Live API Authentication**:
   - Inspection of `scratch/wyvern_token.txt` initially resulted in `HTTP 403: Forbidden` from `https://app.wyvern.chat/api/character-scenarios/char_scenario_CKgwq246DyCj1NNTBV9rt` due to token expiry and missing User-Agent header.
   - Executed `python scratch/refresh_token.py` (line 11: `FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'`), generating a fresh 1,142-byte JWT token.
   - Performing a live GET with `Authorization: Bearer <token>`, `User-Agent: Mozilla/5.0`, and `Accept: application/json` yielded:
     - `char_scenario_CKgwq246DyCj1NNTBV9rt`: `HTTP 200 OK`, `revision: 10`, `name: "Svartulfr: SUCC Collegiate Arc (Alyssa Route)"`, `slots`: 8, `greetings`: 7, `lorebook_ids`: 15, `visibility: "private"`.
     - `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`: `HTTP 200 OK`, `revision: 4`, `name: "Svartulfr: SUCC Collegiate Arc (Jasper Route)"`, `slots`: 8, `greetings`: 6, `lorebook_ids`: 15, `visibility: "private"`.
   - Complete live payloads were captured and saved in `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\live_scenarios_dump.json`.

2. **Local Scenario Files in `FINAL/scenarios/`**:
   - Listing `FINAL/scenarios/` revealed 6 scenario files:
     - `Svartulfr_Scenario_Camp_Mystic.json` (17,330 bytes)
     - `Svartulfr_Scenario_DMHA_Dungeons.json` (16,520 bytes)
     - `Svartulfr_Scenario_SUCC_Route_Alyssa.json` (22,748 bytes)
     - `Svartulfr_Scenario_SUCC_Route_Jasper.json` (20,431 bytes)
     - `Svartulfr_Scenario_Underworld_Sindacato.json` (15,049 bytes)
     - `Svartulfr_Scenario_Villa_Douglas.json` (18,185 bytes)
   - Directory `ARCHIVIO/scenarios/` does not yet exist.

3. **Differences Between Local and Live Scenarios**:
   - **Alyssa Route**:
     - Live is at `revision: 10`; local `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json` is at `revision: 8`.
     - Live slot keys: `['twin', 'best_friend', 'crush', 'roommate', 'brother', 'quarterback', 'friend', 'eldest_brother']`.
     - Local slot keys: `['twin', 'best_friend', 'crush', 'roommate', 'childhood_friend', 'quarterback', 'friend', 'sports_rival']`.
     - In Live Alyssa, Greeting 4 (Ice Rink) message 0 uses `speaker_slot: "eldest_brother"` and message 1 uses `speaker_slot: "brother"`. In Local Alyssa, they use `speaker_slot: "sports_rival"` and `speaker_slot: "childhood_friend"`.
     - Local Alyssa contains the "Cast and Verified Roles:" section in `scenario`, which is missing from Live.
   - **Jasper Route**:
     - Both Live and Local are at `revision: 4`.
     - Slot keys match 100%: `['twin', 'male_roommate', 'crush', 'ai_companion', 'childhood_friend', 'quarterback', 'friend', 'sports_rival']`.
     - All 6 greetings, message counts, and texts match between Live and Local.

4. **Greeting Macro Occurrences (`{{scenarioChar "..."}}`)**:
   - Audited every greeting and message across both scenarios:
     - **Alyssa Route**: Exactly 26 macro occurrences (17 referencing retired NPCs Scarlett, Sierra, Jared, Stan; 5 referencing `twin` Jasper; 2 referencing `crush` Mackenzie; 1 referencing `childhood_friend` Finn; 1 referencing `sports_rival` Vincent).
     - **Jasper Route**: Exactly 19 macro occurrences (12 referencing retired NPCs Russ, Scarlett, Jared, Stan; 4 referencing `twin` Alyssa; 1 referencing `childhood_friend` Finn; 2 referencing `sports_rival` Vincent).
   - Verbatim occurrences for target NPCs:
     - **Scarlett Rose**:
       - Alyssa G0 msg[2]: `{{scenarioChar "best_friend"}} hurried up the paved walkway...`
       - Alyssa G2 greeting.content & msg[0]: `{{scenarioChar "best_friend"}} rested her sketchpad...`
       - Alyssa G3 msg[1]: `{{scenarioChar "best_friend"}} walked down the stone stairs...`
       - Alyssa G6 msg[1]: `{{scenarioChar "best_friend"}} danced beside {{user}}...`
       - Jasper G0 msg[2]: `announced {{scenarioChar "crush"}}, who slipped through the edge of the crowd...`
       - Jasper G5 greeting.content & msg[0]: `{{scenarioChar "crush"}} stood by the second-floor wooden balustrade...`
     - **Russell 'Russ' Sinclair**:
       - Jasper G1 greeting.content & msg[0]: `{{scenarioChar "male_roommate"}} sat perched on the low vinyl sofa...`
       - Jasper G2 msg[1]: `{{scenarioChar "male_roommate"}} stepped through the roof access door...`
       - Jasper G4 greeting.content & msg[0]: `{{scenarioChar "male_roommate"}} pushed through the backstage black curtain...`
       - Jasper G5 msg[2]: `{{scenarioChar "male_roommate"}} caught Jasper's eye from the landing below...`
     - **Jared Thompson**:
       - Alyssa G4 msg[2]: `{{scenarioChar "quarterback"}} stood near the tunnel railing...`
       - Alyssa G5 greeting.content & msg[0]: `{{scenarioChar "quarterback"}} towered in his gold-and-black practice jersey...`
       - Jasper G3 msg[1]: `{{scenarioChar "quarterback"}} strode across the lawn with his heavy football duffel...`
       - Jasper G5 msg[1]: `Down in the crowded foyer, {{scenarioChar "quarterback"}} held up a carved pumpkin punch bowl...`
     - **Stanley Davies Jr.**:
       - Alyssa G2 msg[1]: `{{scenarioChar "friend"}} adjusted his wire-rimmed glasses...`
       - Alyssa G5 msg[1]: `{{scenarioChar "friend"}} leaned against the concrete wall, clutching his binder...`
       - Jasper G3 msg[2]: `{{scenarioChar "friend"}} stood a few paces back with a dry smirk...`
     - **Sierra Cruz**:
       - Alyssa G1 greeting.content & msg[0]: `{{scenarioChar "roommate"}} stood by the full-length mirror, adjusting the hem...`
       - Alyssa G5 msg[2]: `{{scenarioChar "roommate"}} walked past carrying cheer practice flags...`

5. **Slot/Pool Configurations & `unavailable_count: 1`**:
   - On Live Wyvern:
     - Alyssa has 3 slots reporting `unavailable_count: 1`: `best_friend` (`_qXgBMbFYJfc84hbLHhe92`), `roommate` (`_pnrXbkWqcgmFAf3meRWFY`), `friend` (`_Xd3NhKnRJByMTtdb6PjxJ`).
     - Jasper has 4 slots reporting `unavailable_count: 1`: `twin` (`_6exg3yPfe2eCDK4hTftkh`), `male_roommate` (`_wn6DkCcg3Xqa2Xpx9ttnT`), `crush` (`_qXgBMbFYJfc84hbLHhe92`), `friend` (`_Xd3NhKnRJByMTtdb6PjxJ`).
     - In both scenarios, `quarterback` (`_xJVPtBLL3dxy69RLKL9X9` Jared Thompson) currently has `unavailable_count: 0`, but will transition to `1` as soon as Jared's card is deleted from `/characters/mine` under R3.
   - Speaker Slot Invariant: In all 13 greetings across both scenarios, `greeting.speaker_slot == messages[0].speaker_slot` and `greeting.content == messages[0].content` holds true.

---

## 2. Logic Chain

1. **From Observation 1**: The live GET calls succeeded with HTTP 200, confirming that the scenarios are active on Wyvern under `char_scenario_CKgwq246DyCj1NNTBV9rt` (revision 10) and `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` (revision 4). Any update via `PUT` must submit the latest revision to avoid HTTP 409 conflict errors.
2. **From Observation 2**: Exactly 4 scenarios (Camp Mystic, DMHA Dungeons, Underworld Sindacato, Villa Douglas) were removed from Wyvern and only remain locally in `FINAL/scenarios/`. Moving these 4 files to a new directory `ARCHIVIO/scenarios/` satisfies R1 and leaves only the 2 official active SUCC scenarios in `FINAL/scenarios/`.
3. **From Observation 3**: Live Alyssa still contains legacy slots `brother` and `eldest_brother` (repurposed from Noah and Malachia), whereas Local Alyssa correctly defines `childhood_friend` and `sports_rival`. The local slot structure is canonical and aligns with the actual characters speaking in the messages (Finn and Vincent). Therefore, the deployment payload for Alyssa must adopt the 8 canonical slot keys from Local Alyssa while applying revision 10.
4. **From Observation 4**: In greetings, `{{scenarioChar "..."}}` evaluates dynamically against the character occupying the corresponding slot. Because Scarlett, Russ, Jared, Stan, and Sierra are now Lorebook NPCs rather than standalone character cards, their slots will no longer have card IDs. If the macros remain in the greeting text, they will fail to resolve or produce empty strings. Replacing them with their verbatim character names preserves fluent, immersive storytelling and satisfies R2.
5. **From Observation 4 (Jasper Route `twin`)**: In Jasper Route, `twin` represents Alyssa. However, Alyssa's card was retired to `ARCHIVIO/cards_legacy/` because she is a Persona and Lorebook NPC. Her slot in Jasper Route has `unavailable_count: 1`. When her pool is emptied, `{{scenarioChar "twin"}}` in Jasper Route greetings would also fail to resolve. Thus, replacing `{{scenarioChar "twin"}}` with `Alyssa Hvit Douglas Bloodmoon` or `Alyssa` in Jasper Route greetings is essential.
6. **From Observation 5**: To resolve `unavailable_count: 1`, the `pool` array for each retired card slot must be set to `[]` with `unavailable_count: 0`. Crucially, the slot itself must NOT be deleted from the `slots` array; keeping the slot object preserves the validity of `speaker_slot` on all messages.

---

## 3. Caveats

1. **Card Deletion Sequencing**: Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`) is currently in slot `quarterback` with `unavailable_count: 0`. Worker agent must coordinate R2 and R3 so that slot pools in scenarios are cleared of `_xJVPtBLL3dxy69RLKL9X9` before or alongside the `DELETE` API call for Jared.
2. **Approved Cards in Pools**: In Alyssa Route, slot `twin` (Jasper `_t4J9aQNJM36cUKAP4wB4U`) and slot `crush` (Mackenzie `_zn24784jfcchQ7EwCyAnm`) refer to cards that remain active in the 8 approved cards. Their pools should be retained. In Jasper Route, however, none of the 8 approved cards occupy room slots, so all 8 slots will operate with `pool: []`.
3. **Master Scenario**: `FINAL/Svartulfr_Master_Scenario.json` (170,117 bytes) is also present in `FINAL/`. The dispatch instructions for R1 specifically target moving the 4 thematic scenarios (Camp Mystic, DMHA, Underworld, Villa Douglas) to `ARCHIVIO/scenarios/`. Worker should ensure `Svartulfr_Master_Scenario.json` is handled according to user instructions.

---

## 4. Conclusion

The investigation of R1 and R2 is complete with 100% empirical evidence. The exact path forward for the Worker agent is clearly defined:
1. Move the 4 files (`Svartulfr_Scenario_Camp_Mystic.json`, `Svartulfr_Scenario_DMHA_Dungeons.json`, `Svartulfr_Scenario_Underworld_Sindacato.json`, `Svartulfr_Scenario_Villa_Douglas.json`) from `FINAL/scenarios/` to `ARCHIVIO/scenarios/`.
2. Update `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json`:
   - Canonicalize slots to: `twin`, `best_friend`, `crush`, `roommate`, `childhood_friend`, `quarterback`, `friend`, `sports_rival`.
   - Clear pools for `best_friend`, `roommate`, `childhood_friend`, `quarterback`, `friend`, `sports_rival` (`pool: []`, `unavailable_count: 0`).
   - Retain pools for `twin` (Jasper `_t4J9aQNJM36cUKAP4wB4U`) and `crush` (Mackenzie `_zn24784jfcchQ7EwCyAnm`).
   - In all greetings and messages, replace the 17 NPC macros with literal names (`Scarlett Rose`, `Sierra Cruz`, `Jared Thompson`, `Stanley Davies Jr.`), and secondary NPC macros (`Finnegan Novak`, `Vincent Campbell`).
3. Update `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json`:
   - Set `pool: []` and `unavailable_count: 0` for all 8 slots.
   - In all greetings and messages, replace the 12 NPC macros with literal names (`Russell Sinclair`, `Scarlett Rose`, `Jared Thompson`, `Stanley Davies Jr.`), plus `twin` with `Alyssa Hvit Douglas Bloodmoon`, `childhood_friend` with `Finnegan Novak`, and `sports_rival` with `Vincent Campbell`.
4. Deploy both updated scenarios via `PUT /api/character-scenarios/{id}` using Bearer token from `scratch/wyvern_token.txt` and revisions 10 (Alyssa) and 4 (Jasper), verifying HTTP 200.

---

## 5. Verification Method

To independently verify the findings in this report, execute the following commands in powershell:

1. **Verify Token & Live Scenario Retrieval**:
   ```bash
   python -c "
   import urllib.request, json
   token = open('scratch/wyvern_token.txt').read().strip()
   headers = {'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
   for sid in ['char_scenario_CKgwq246DyCj1NNTBV9rt', 'char_scenario_Kq4mJEBH83j7Q7DdVfFnF']:
       req = urllib.request.Request(f'https://app.wyvern.chat/api/character-scenarios/{sid}', headers=headers)
       with urllib.request.urlopen(req) as resp:
           d = json.loads(resp.read().decode())
           print(f'{sid}: status {resp.status}, rev {d.get(\"revision\")}, slots {len(d.get(\"slots\", []))}, greetings {len(d.get(\"greetings\", []))}')
   "
   ```
2. **Inspect Detailed Extraction Outputs**:
   - View `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\live_scenarios_dump.json`
   - View `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\all_macros_extracted.json`
   - View `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\analysis.md`
3. **Invalidation Conditions**:
   - The findings would be invalidated if Wyvern API returns non-200 responses, if scenario revisions increment prior to worker deployment, or if any `speaker_slot` does not match an existing key in `slots`.
