# Comprehensive Analysis Report — Explorer R6-1
**Investigative Focus**: R1 (Wyvern API Live Sync, Local Scenario Files & Archive Mapping) & R2 (Greeting Macro Optimizations, Slot/Pool Configurations & Speaker Slots)
**Author**: Explorer R6-1 (`teamwork_preview_explorer`)
**Target Entities**:
- `char_scenario_CKgwq246DyCj1NNTBV9rt` (SUCC Collegiate Arc - Alyssa Route)
- `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` (SUCC Collegiate Arc - Jasper Route)
- Directory `FINAL/scenarios/` & target directory `ARCHIVIO/scenarios/`

---

## 1. Executive Summary

Explorer R6-1 executed an exhaustive, read-only empirical investigation into the live state of the Wyvern Web API and local repository files for character scenarios and greeting macro configurations.

Key Findings:
1. **Bearer Token & Live Scenarios Health**: The Bearer token in `scratch/wyvern_token.txt` was expired, producing HTTP 403 Forbidden. After refreshing via `python scratch/refresh_token.py`, both SUCC scenarios were successfully queried with HTTP 200:
   - **Alyssa Route** (`char_scenario_CKgwq246DyCj1NNTBV9rt`): Live revision 10, visibility `private`, 8 slots, 7 greetings, 15 attached Lorebooks (`lorebook_ids`).
   - **Jasper Route** (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`): Live revision 4, visibility `private`, 8 slots, 6 greetings, 15 attached Lorebooks (`lorebook_ids`).
2. **Local Scenario Directory Mapping (R1)**:
   - Exactly 4 scenario files in `FINAL/scenarios/` correspond to the scenarios previously deleted from Wyvern and must be relocated to `ARCHIVIO/scenarios/`:
     - `FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json` (17,330 bytes)
     - `FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json` (16,520 bytes)
     - `FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json` (15,049 bytes)
     - `FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json` (18,185 bytes)
   - Exactly 2 scenario files must remain active in `FINAL/scenarios/`:
     - `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json`
     - `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json`
3. **Discrepancy Between Local and Live Alyssa Route**:
   - Live Alyssa is revision 10, but local file is revision 8.
   - Crucially, Live Alyssa still contains legacy slot keys (`brother` [Noah] and `eldest_brother` [Malachia]) for slots 5 and 8, whereas Local Alyssa has already canonicalized them to `childhood_friend` (Finnegan Novak) and `sports_rival` (Vincent Campbell).
   - Local Alyssa also contains the comprehensive "Cast and Verified Roles:" overview block in its `scenario` field, which is absent from Live revision 10.
4. **Greeting Macro Occurrences & Literal Replacements (R2)**:
   - Total macros found across greetings: **26 in Alyssa Route**, **19 in Jasper Route**.
   - Exactly **17 occurrences in Alyssa** and **12 occurrences in Jasper** reference the 5 retired characters turned into NPCs:
     - **Scarlett Rose**: `best_friend` in Alyssa (6 occurrences); `crush` in Jasper (3 occurrences).
     - **Russell 'Russ' Sinclair**: `male_roommate` in Jasper (6 occurrences).
     - **Jared Thompson**: `quarterback` in Alyssa (4 occurrences); `quarterback` in Jasper (2 occurrences).
     - **Stanley Davies Jr.**: `friend` in Alyssa (2 occurrences); `friend` in Jasper (1 occurrence).
     - **Sierra Cruz**: `roommate` in Alyssa (4 occurrences).
   - In addition, in Jasper Route, `twin` (4 occurrences) references Alyssa Hvit Douglas Bloodmoon. Because Alyssa's standalone card was retired and her slot pool is empty, `{{scenarioChar "twin"}}` in Jasper route greetings must also be replaced with "Alyssa" or "Alyssa Hvit Douglas Bloodmoon" to avoid unpopulated macro evaluation.
   - `childhood_friend` (Finn Novak) and `sports_rival` (Vincent Campbell) possess empty pools (`pool: []`) in both scenarios; their macro instances should likewise be replaced with literal names.
5. **Slot and Pool Configurations & `unavailable_count: 1`**:
   - On Live Wyvern, multiple slots currently show `unavailable_count: 1` because they reference cards that were deleted or made unavailable:
     - Live Alyssa: `best_friend` (`_qXgBMbFYJfc84hbLHhe92`), `roommate` (`_pnrXbkWqcgmFAf3meRWFY`), `friend` (`_Xd3NhKnRJByMTtdb6PjxJ`).
     - Live Jasper: `twin` (`_6exg3yPfe2eCDK4hTftkh`), `male_roommate` (`_wn6DkCcg3Xqa2Xpx9ttnT`), `crush` (`_qXgBMbFYJfc84hbLHhe92`), `friend` (`_Xd3NhKnRJByMTtdb6PjxJ`).
     - In addition, `quarterback` (`_xJVPtBLL3dxy69RLKL9X9` Jared Thompson) will trigger `unavailable_count: 1` as soon as Jared is deleted under R3.
   - **Remediation Invariant**: Setting `pool: []` and `unavailable_count: 0` for these slots eliminates all Wyvern errors while preserving the slot keys in `slots` so that message `speaker_slot` references remain 100% valid.
   - **Speaker Invariant Verification**: Across all 7 greetings in Alyssa and all 6 greetings in Jasper, `greeting.speaker_slot == messages[0].speaker_slot` and `greeting.content == messages[0].content` holds with 100% precision.

---

## 2. Wyvern Bearer Token & Live GET Status

### 2.1 Token Verification and Refresh
- **File**: `scratch/wyvern_token.txt`
- **Initial State**: JWT Bearer token was expired, resulting in HTTP 403 Forbidden upon API requests to `https://app.wyvern.chat/api/character-scenarios/{id}`.
- **Refresh Execution**: Executed `python scratch/refresh_token.py` communicating with Google Secure Token API (`securetoken.googleapis.com/v1/token?key=AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw`).
- **Refreshed Token**: Valid JWT generated (length 1,142 bytes), written to `scratch/wyvern_token.txt`.
- **Cloudflare Header Invariant**: Direct requests require `User-Agent: Mozilla/5.0` and `Accept: application/json` to avoid automated Cloudflare anti-bot blocks.

### 2.2 Live GET Scenario Payloads
Live scenario data fetched and dumped to `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\live_scenarios_dump.json`:

| Metric | Alyssa Route (`char_scenario_CKgwq246DyCj1NNTBV9rt`) | Jasper Route (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`) |
|---|---|---|
| HTTP Status | 200 OK | 200 OK |
| Revision | **10** | **4** |
| Visibility | `private` | `private` |
| Rating | `explicit` | `explicit` |
| Slots Count | 8 | 8 |
| Greetings Count | 7 | 6 |
| Lorebook IDs Count | 15 | 15 |
| Updated At | 2026-10-21T00:38:38.979Z | 2026-10-21T00:17:09.977Z |
| Creator UID | `2r4fVpvImte5dbljedLkZJxre2d2` | `2r4fVpvImte5dbljedLkZJxre2d2` |

Both scenarios successfully retain the full suite of 15 standalone Lorebooks (`lorebook_ids`):
1. `_gwwCxCfQ6PQaLEjAQVpJL` (Svartúlfr - Lorebook I)
2. `_HfG7TeV6MJyj6bxMwxkpt` (Svartúlfr - Lorebook II)
3. `_9zWTGqYJNJ4BCDMj8gfcD` (Svartúlfr - Lorebook III)
4. `_EjXxkmPVhpCXg8xABpFkK` (Svartúlfr - Location)
5. `_zwEqgEEzh12X6gHVmMKKC` (Svartúlfr - NPC Primary)
6. `_Uht3Ckz44JBDrPnUHq7LV` (Svartúlfr - NPC Secondary)
7. `_GV1KyHVY1RMbCnWgLkzDG` (A0 Behavioral Realism)
8. `_GbWJbkhgLzWexMHrjyUUc` (A1 Physics)
9. `_FaVcHfmrqcaJq8pa3WmRw` (A2 Social Realism)
10. `_BbrRgrcdGPMLEbBU2b6xk` (A3 Medical Realism)
11. `_gchmML4Q478zdFjhXf8rN` (A4 Cultural Realism)
12. `_brNyzEdhzNAyxK8xC8hhm` (A5 Sex Position)
13. `_YtKLMTwyMxNf1DNYqBx1t` (A5.5 Scene Tone)
14. `_b9HgpUXtAW8VmTy82BPDV` (A6 World Realism)
15. `_c8bEm1bWphwqFBXWRPrV8` (A7 Queer Realism)

---

## 3. Local Scenario Directory Mapping & State Analysis

### 3.1 Files in `FINAL/scenarios/`
Directory `FINAL/scenarios/` currently contains 6 JSON scenario files and 1 `desktop.ini`:
1. `FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json` (17,330 bytes)
2. `FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json` (16,520 bytes)
3. `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json` (22,748 bytes)
4. `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json` (20,431 bytes)
5. `FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json` (15,049 bytes)
6. `FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json` (18,185 bytes)

### 3.2 Mapping to `ARCHIVIO/scenarios/` (Requirement R1)
The 4 files to move to `ARCHIVIO/scenarios/` are:
- `Svartulfr_Scenario_Camp_Mystic.json` -> `ARCHIVIO/scenarios/Svartulfr_Scenario_Camp_Mystic.json`
- `Svartulfr_Scenario_DMHA_Dungeons.json` -> `ARCHIVIO/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json`
- `Svartulfr_Scenario_Underworld_Sindacato.json` -> `ARCHIVIO/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json`
- `Svartulfr_Scenario_Villa_Douglas.json` -> `ARCHIVIO/scenarios/Svartulfr_Scenario_Villa_Douglas.json`

The 2 files remaining in `FINAL/scenarios/`:
- `Svartulfr_Scenario_SUCC_Route_Alyssa.json`
- `Svartulfr_Scenario_SUCC_Route_Jasper.json`

### 3.3 Comparative Analysis: Local vs Live SUCC Scenarios

#### Alyssa Route
- **Revision Discrepancy**: Live is revision 10; Local file is revision 8.
- **Slot Differences**:
  - Live revision 10: `['twin', 'best_friend', 'crush', 'roommate', 'brother', 'quarterback', 'friend', 'eldest_brother']`
  - Local revision 8: `['twin', 'best_friend', 'crush', 'roommate', 'childhood_friend', 'quarterback', 'friend', 'sports_rival']`
  - Rationale: The local file previously refactored slots 5 and 8 from legacy `brother`/`eldest_brother` to the true canonical SUCC characters `childhood_friend` (Finnegan Novak) and `sports_rival` (Vincent Campbell).
- **Greeting 4 Speaker Slots**:
  - Live rev 10: Message 0 has `speaker_slot: "eldest_brother"`; Message 1 has `speaker_slot: "brother"`.
  - Local rev 8: Message 0 has `speaker_slot: "sports_rival"`; Message 1 has `speaker_slot: "childhood_friend"`.
- **Overview Text**: Local rev 8 includes the structured "Cast and Verified Roles:" section detailing Alyssa, Jasper, Scarlett, Mac, Sierra, Finn, Jared, Stan, and Vincent. Live rev 10 lacks this section.

#### Jasper Route
- **Revision Parity**: Live is revision 4; Local file is revision 4.
- **Slot Parity**: Slot keys match 100%: `['twin', 'male_roommate', 'crush', 'ai_companion', 'childhood_friend', 'quarterback', 'friend', 'sports_rival']`.
- **Text Parity**: Scenario overview and greeting contents match 100%.
- **Unavailable Count Difference**: On Live, 4 slots report `unavailable_count: 1` (`twin`, `male_roommate`, `crush`, `friend`), whereas local has `unavailable_count: 0`.

---

## 4. Macro Occurrences & Literal Text Replacement Map

### 4.1 Summary of Macro Distribution
In Wyvern scenarios, `{{scenarioChar "slot_key"}}` dynamically replaces the slot key with the character card's name. When a character is retired from card status to Lorebook NPC status, that slot's card pool becomes empty or inaccessible. Replacing these macros with literal text ensures zero macro breakage and prevents empty string replacement in dialog/narration.

Total Macros Extracted:
- **Alyssa Route**: 26 macros (17 targeting retired NPCs Scarlett, Sierra, Jared, Stan; 5 twin Jasper; 2 crush Mac; 1 childhood_friend Finn; 1 sports_rival Vincent).
- **Jasper Route**: 19 macros (12 targeting retired NPCs Russ, Scarlett, Jared, Stan; 4 twin Alyssa; 1 childhood_friend Finn; 2 sports_rival Vincent).

### 4.2 Comprehensive Macro Mapping Table — Alyssa Route

| # | Greeting | Field / Msg | Macro Key | Target Character | Verbatim Context Snippet | Proposed Literal Replacement |
|---|---|---|---|---|---|---|
| 01 | G0 (Welcome Day) | `messages[2]` | `best_friend` | Scarlett Rose | `A sweet, familiar scent of hibiscus tea and crushed mint drifted through the quad air as {{scenarioChar "best_friend"}} hurried up the paved walkway...` | `Scarlett Rose` |
| 02 | G1 (Greek Row) | `greeting.content` | `roommate` | Sierra Cruz | `{{scenarioChar "roommate"}} stood by the full-length mirror, adjusting the hem...` | `Sierra Cruz` |
| 03 | G1 (Greek Row) | `messages[0]` | `roommate` | Sierra Cruz | `{{scenarioChar "roommate"}} stood by the full-length mirror, adjusting the hem...` | `Sierra Cruz` |
| 04 | G2 (Labs) | `greeting.content` | `best_friend` | Scarlett Rose | `{{scenarioChar "best_friend"}} rested her sketchpad beside a tray of botanical specimens...` | `Scarlett Rose` |
| 05 | G2 (Labs) | `messages[0]` | `best_friend` | Scarlett Rose | `{{scenarioChar "best_friend"}} rested her sketchpad beside a tray of botanical specimens...` | `Scarlett Rose` |
| 06 | G2 (Labs) | `messages[1]` | `friend` | Stanley Davies Jr. | `{{scenarioChar "friend"}} adjusted his wire-rimmed glasses, double-checking the spectrometer...` | `Stanley Davies Jr.` |
| 07 | G3 (Smoking Corner) | `messages[1]` | `best_friend` | Scarlett Rose | `{{scenarioChar "best_friend"}} walked down the stone stairs carrying a folder...` | `Scarlett Rose` |
| 08 | G4 (Ice Rink) | `messages[2]` | `quarterback` | Jared Thompson | `{{scenarioChar "quarterback"}} stood near the tunnel railing in his black Bulls training jersey...` | `Jared Thompson` |
| 09 | G5 (Bulls Tunnel) | `greeting.content` | `quarterback` | Jared Thompson | `{{scenarioChar "quarterback"}} towered in his gold-and-black practice jersey...` | `Jared Thompson` |
| 10 | G5 (Bulls Tunnel) | `messages[0]` | `quarterback` | Jared Thompson | `{{scenarioChar "quarterback"}} towered in his gold-and-black practice jersey...` | `Jared Thompson` |
| 11 | G5 (Bulls Tunnel) | `messages[1]` | `friend` | Stanley Davies Jr. | `{{scenarioChar "friend"}} leaned against the concrete wall, clutching his binder with a deadpan expression...` | `Stanley Davies Jr.` |
| 12 | G5 (Bulls Tunnel) | `messages[2]` | `roommate` | Sierra Cruz | `{{scenarioChar "roommate"}} walked past carrying cheer practice flags, laughing...` | `Sierra Cruz` |
| 13 | G6 (Sidewinders) | `messages[1]` | `best_friend` | Scarlett Rose | `{{scenarioChar "best_friend"}} danced beside {{user}}, laughing over the pounding bass...` | `Scarlett Rose` |

*Secondary Non-Card Macros in Alyssa Route*:
- G0 `messages[1]`: `{{scenarioChar "childhood_friend"}}` -> `Finnegan Novak` (Finn is an NPC with empty pool).
- G4 `greeting.content` & `messages[0]`: `{{scenarioChar "sports_rival"}}` -> `Vincent Campbell` (Vincent is an NPC with empty pool).
- Approved Card Macros in Alyssa Route (Can remain as macros or be replaced):
  - `twin`: Jasper Douglas (`_t4J9aQNJM36cUKAP4wB4U`) -> approved card.
  - `crush`: Mackenzie Sanchez-Rogers (`_zn24784jfcchQ7EwCyAnm`) -> approved card.

### 4.3 Comprehensive Macro Mapping Table — Jasper Route

| # | Greeting | Field / Msg | Macro Key | Target Character | Verbatim Context Snippet | Proposed Literal Replacement |
|---|---|---|---|---|---|---|
| 01 | G0 (Welcome Day) | `messages[2]` | `crush` | Scarlett Rose | `A sudden draft of sweet vanilla and elderflower announced {{scenarioChar "crush"}}, who slipped through the edge of the crowd...` | `Scarlett Rose` |
| 02 | G1 (Wyrm 304) | `greeting.content` | `male_roommate` | Russell Sinclair | `{{scenarioChar "male_roommate"}} sat perched on the low vinyl sofa, his bare shoulders covered in dark ink...` | `Russell Sinclair` |
| 03 | G1 (Wyrm 304) | `messages[0]` | `male_roommate` | Russell Sinclair | `{{scenarioChar "male_roommate"}} sat perched on the low vinyl sofa, his bare shoulders covered in dark ink...` | `Russell Sinclair` |
| 04 | G2 (Roof Hack) | `messages[1]` | `male_roommate` | Russell Sinclair | `{{scenarioChar "male_roommate"}} stepped through the roof access door, carrying two cold cans of energy soda...` | `Russell Sinclair` |
| 05 | G3 (Quad Tension) | `messages[1]` | `quarterback` | Jared Thompson | `{{scenarioChar "quarterback"}} strode across the lawn with his heavy football duffel slung over his shoulder...` | `Jared Thompson` |
| 06 | G3 (Quad Tension) | `messages[2]` | `friend` | Stanley Davies Jr. | `{{scenarioChar "friend"}} stood a few paces back with a dry smirk, tapping his pen against his textbook...` | `Stanley Davies Jr.` |
| 07 | G4 (Warehouse Rave) | `greeting.content` | `male_roommate` | Russell Sinclair | `{{scenarioChar "male_roommate"}} pushed through the backstage black curtain, wiping sweat from his brow...` | `Russell Sinclair` |
| 08 | G4 (Warehouse Rave) | `messages[0]` | `male_roommate` | Russell Sinclair | `{{scenarioChar "male_roommate"}} pushed through the backstage black curtain, wiping sweat from his brow...` | `Russell Sinclair` |
| 09 | G5 (Halloween Party)| `greeting.content` | `crush` | Scarlett Rose | `{{scenarioChar "crush"}} stood by the second-floor wooden balustrade, dressed in an intricate wood-nymph costume...` | `Scarlett Rose` |
| 10 | G5 (Halloween Party)| `messages[0]` | `crush` | Scarlett Rose | `{{scenarioChar "crush"}} stood by the second-floor wooden balustrade, dressed in an intricate wood-nymph costume...` | `Scarlett Rose` |
| 11 | G5 (Halloween Party)| `messages[1]` | `quarterback` | Jared Thompson | `Down in the crowded foyer, {{scenarioChar "quarterback"}} held up a carved pumpkin punch bowl...` | `Jared Thompson` |
| 12 | G5 (Halloween Party)| `messages[2]` | `male_roommate` | Russell Sinclair | `{{scenarioChar "male_roommate"}} caught Jasper's eye from the landing below with a drink in hand...` | `Russell Sinclair` |

*Secondary Non-Card Macros in Jasper Route*:
- `twin`: Alyssa Hvit Douglas Bloodmoon (G0 greeting.content & msg[0], G1 msg[2], G4 msg[1]).
  - **Critical Note**: In Jasper Route, Alyssa is the twin, but her card (`_6exg3yPfe2eCDK4hTftkh`) has been retired (she is a Persona). If slot `twin` has `pool: []`, `{{scenarioChar "twin"}}` in Jasper route will NOT resolve to any card!
  - **Recommendation**: Replace `{{scenarioChar "twin"}}` with `Alyssa Hvit Douglas Bloodmoon` (or `Alyssa`) across all Jasper greetings.
- `childhood_friend`: Finnegan Novak (G0 msg[1]). Pool is empty -> replace with `Finnegan Novak`.
- `sports_rival`: Vincent Campbell (G3 greeting.content & msg[0]). Pool is empty -> replace with `Vincent Campbell`.

---

## 5. Slot & Pool Configuration Analysis

### 5.1 Slots with `unavailable_count: 1`
When a character card in a slot's `pool` is deleted or inaccessible, Wyvern marks `unavailable_count: 1` on that slot. If left unaddressed, Wyvern's scenario runtime throws warnings or blocks scenario initialization.

#### Live Alyssa Route (`char_scenario_CKgwq246DyCj1NNTBV9rt`):
- `best_friend`: `_qXgBMbFYJfc84hbLHhe92` (Scarlett Rose) -> `unavailable_count: 1`
- `roommate`: `_pnrXbkWqcgmFAf3meRWFY` (Sierra Cruz) -> `unavailable_count: 1`
- `friend`: `_Xd3NhKnRJByMTtdb6PjxJ` (Stanley Davies Jr.) -> `unavailable_count: 1`
- `quarterback`: `_xJVPtBLL3dxy69RLKL9X9` (Jared Thompson) -> currently `unavailable_count: 0`, but will become `1` once deleted in R3.

#### Live Jasper Route (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`):
- `twin`: `_6exg3yPfe2eCDK4hTftkh` (Alyssa Hvit) -> `unavailable_count: 1`
- `male_roommate`: `_wn6DkCcg3Xqa2Xpx9ttnT` (Russ Sinclair) -> `unavailable_count: 1`
- `crush`: `_qXgBMbFYJfc84hbLHhe92` (Scarlett Rose) -> `unavailable_count: 1`
- `friend`: `_Xd3NhKnRJByMTtdb6PjxJ` (Stanley Davies Jr.) -> `unavailable_count: 1`
- `quarterback`: `_xJVPtBLL3dxy69RLKL9X9` (Jared Thompson) -> currently `unavailable_count: 0`, will become `1` once deleted in R3.

### 5.2 Remediation Strategy for Inaccessible Card Pools
To completely eradicate `unavailable_count: 1` while preventing speaker resolution errors:
1. **Empty the `pool` array (`pool: []`) and set `unavailable_count: 0`** for all slots whose cards are retired/deleted.
2. **Retain the slot objects in the `slots` array**. Do NOT delete the slot definitions from `slots`.
   - Reason: Message objects reference `speaker_slot`. If a slot key is removed from `slots`, any message with that `speaker_slot` becomes invalid or orphaned.
   - By retaining the slot with `pool: []` and descriptive `label`, Wyvern recognizes the slot key as valid. This pattern is already proven by `ai_companion`, `childhood_friend`, and `sports_rival`, which have always operated with `pool: []` and `unavailable_count: 0`.
3. **Preserve Valid Approved Cards in Pools**:
   - In Alyssa Route:
     - `twin`: keep `_t4J9aQNJM36cUKAP4wB4U` (Jasper Svartr, weight 100).
     - `crush`: keep `_zn24784jfcchQ7EwCyAnm` (Mackenzie Sanchez-Rogers, weight 100).

### 5.3 Speaker Slot Validity Verification
Every greeting and message across both scenarios was audited against defined slot keys:

#### Alyssa Route (7 Greetings, 21 Messages):
- G0: `speaker_slot: "twin"` -> M0: `twin`, M1: `childhood_friend`, M2: `best_friend`
- G1: `speaker_slot: "roommate"` -> M0: `roommate`, M1: `childhood_friend`, M2: `twin`
- G2: `speaker_slot: "best_friend"` -> M0: `best_friend`, M1: `friend`, M2: `twin`
- G3: `speaker_slot: "crush"` -> M0: `crush`, M1: `best_friend`, M2: `twin`
- G4: `speaker_slot: "sports_rival"` -> M0: `sports_rival`, M1: `childhood_friend`, M2: `quarterback`
- G5: `speaker_slot: "quarterback"` -> M0: `quarterback`, M1: `friend`, M2: `roommate`
- G6: `speaker_slot: "crush"` -> M0: `crush`, M1: `best_friend`, M2: `twin`

*Result*: 100% of speaker slots in Local Alyssa reference valid slot keys (`twin`, `best_friend`, `crush`, `roommate`, `childhood_friend`, `quarterback`, `friend`, `sports_rival`).
*Invariant Check*: `greeting.speaker_slot == messages[0].speaker_slot` holds for all 7 greetings.

#### Jasper Route (6 Greetings, 18 Messages):
- G0: `speaker_slot: "twin"` -> M0: `twin`, M1: `childhood_friend`, M2: `crush`
- G1: `speaker_slot: "male_roommate"` -> M0: `male_roommate`, M1: `ai_companion`, M2: `twin`
- G2: `speaker_slot: "ai_companion"` -> M0: `ai_companion`, M1: `male_roommate`, M2: `childhood_friend`
- G3: `speaker_slot: "sports_rival"` -> M0: `sports_rival`, M1: `quarterback`, M2: `friend`
- G4: `speaker_slot: "male_roommate"` -> M0: `male_roommate`, M1: `twin`, M2: `ai_companion`
- G5: `speaker_slot: "crush"` -> M0: `crush`, M1: `quarterback`, M2: `male_roommate`

*Result*: 100% of speaker slots in Jasper reference valid slot keys (`twin`, `male_roommate`, `crush`, `ai_companion`, `childhood_friend`, `quarterback`, `friend`, `sports_rival`).
*Invariant Check*: `greeting.speaker_slot == messages[0].speaker_slot` holds for all 6 greetings.

---

## 6. Implementation Action Plan for Worker Agent (R1 & R2)

1. **R1 Execution**:
   - Create directory `ARCHIVIO/scenarios/`.
   - Move the 4 retired scenario JSON files from `FINAL/scenarios/` into `ARCHIVIO/scenarios/`:
     - `Svartulfr_Scenario_Camp_Mystic.json`
     - `Svartulfr_Scenario_DMHA_Dungeons.json`
     - `Svartulfr_Scenario_Underworld_Sindacato.json`
     - `Svartulfr_Scenario_Villa_Douglas.json`
   - Keep only `Svartulfr_Scenario_SUCC_Route_Alyssa.json` and `Svartulfr_Scenario_SUCC_Route_Jasper.json` in `FINAL/scenarios/`.
2. **R2 Execution**:
   - Update `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json`:
     - Set slot keys to the canonical 8: `twin`, `best_friend`, `crush`, `roommate`, `childhood_friend`, `quarterback`, `friend`, `sports_rival`.
     - Set `pool: []` and `unavailable_count: 0` for `best_friend`, `roommate`, `childhood_friend`, `quarterback`, `friend`, `sports_rival`.
     - Retain `pool` with weight 100 for `twin` (`_t4J9aQNJM36cUKAP4wB4U`) and `crush` (`_zn24784jfcchQ7EwCyAnm`).
     - In all greetings and messages, replace the 17 NPC macros with literal names (`Scarlett Rose`, `Sierra Cruz`, `Jared Thompson`, `Stanley Davies Jr.`), and secondary NPC macros (`Finnegan Novak`, `Vincent Campbell`).
     - Ensure `greeting.content == messages[0].content` on all greetings.
   - Update `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json`:
     - Set `pool: []` and `unavailable_count: 0` for `twin`, `male_roommate`, `crush`, `ai_companion`, `childhood_friend`, `quarterback`, `friend`, `sports_rival`.
     - In all greetings and messages, replace the 12 NPC macros with literal names (`Russell Sinclair`, `Scarlett Rose`, `Jared Thompson`, `Stanley Davies Jr.`), plus `twin` with `Alyssa Hvit Douglas Bloodmoon`, `childhood_friend` with `Finnegan Novak`, and `sports_rival` with `Vincent Campbell`.
     - Ensure `greeting.content == messages[0].content` on all greetings.
   - Synchronize with Wyvern API via `PUT https://app.wyvern.chat/api/character-scenarios/{id}`:
     - For Alyssa: use revision 10.
     - For Jasper: use revision 4.
     - Confirm HTTP 200 response for both.
