# Dispatch — Worker R6-1

**Role**: teamwork_preview_worker (Implementation and Live Deployment)
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\worker_r6_1`
**Authoritative Request**: `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (see `## Follow-up — 2026-10-21T14:38:04Z`)
**Orchestrator Scope**: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6\SCOPE.md`

## MANDATORY INTEGRITY WARNING
> DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Input Evidence Files
- Explorer R6-1 Handoff: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\handoff.md` & `analysis.md`
- Explorer R6-2 Handoff: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_2\handoff.md` & `analysis.md`
- Explorer R6-3 Handoff: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_3\handoff.md` & `analysis.md`

## Assigned Implementation Tasks

### 1. R4 Implementation First (Safeguard Card Data Before Move)
- Read full JED+ descriptions, avatars, and character info from the 6 source card files in `FINAL/`:
  - `FINAL/Scarlett_Rose_card.json` (4,777 chars)
  - `FINAL/Sierra_Cruz_card.json` (5,117 chars)
  - `FINAL/Russ_card.json` (5,505 chars)
  - `FINAL/Stan_Davies_Jr_card.json` (8,008 chars)
  - `FINAL/Jared_Thompson_card.json` (8,696 chars)
  - `FINAL/Alyssa_Douglas_Bloodmoon_card.json` (16,957 chars)
- Update `FINAL/Svartulfr_NPC_Primary.json` (both `entries` and `lexicon` arrays):
  - Scarlett Rose (`4NzXF4_0hYxmN7Idltzpw`): `type: "npc"`, `selective: false`, `secondary_keys: []`, full description, avatar, `custom_avatar_regex: true`, `lines_parsed: 1`, multiline regex, `npc_info`.
  - Sierra Cruz (`ijy8vrlphNv19-p-gbYuY`): `type: "npc"`, `selective: false`, `secondary_keys: []`, full description, avatar, `custom_avatar_regex: true`, `lines_parsed: 1`, multiline regex, `npc_info`.
  - Russell 'Russ' Sinclair (`YCxAqNoShpefVvk0_Pc7i`): `type: "npc"`, `selective: false`, `secondary_keys: []`, full description, Janitor avatar (`9yrobVTbiGDRLHlS6GtIz.webp`), `custom_avatar_regex: true`, `lines_parsed: 1`, multiline regex, `npc_info`.
  - Stanley Davies Jr. (`ekdQjq63xP7HtNuaPQJQE`): `type: "npc"`, `selective: false`, `secondary_keys: []`, full description, avatar, `custom_avatar_regex: true`, `lines_parsed: 1`, multiline regex, `npc_info`.
  - Jared Thompson (`RM6rcwv8MlY1XWaCTQp0M`): `type: "npc"`, `selective: false`, `secondary_keys: []`, full description, avatar, `custom_avatar_regex: true`, `lines_parsed: 1`, multiline regex, `npc_info`.
  - Alyssa Hvit Douglas Bloodmoon (`alyssa_world_dossier_2b54a223`): `type: "lore/concept"`, `selective: true`, `secondary_keys: ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`, `key_logic: 'AND_ANY'`, Cloudflare avatar `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public`, full description (16,957 chars). (Exact parity with Jasper `Vcj4h2TL4Usola2A4OOl6`).
- Sync `FINAL/Svartulfr_NPC_Primary.json` to `lorebooks/optimized/Svartulfr_NPC_Primary.json`.
- Deploy Lorebook Primary (`_zwEqgEEzh12X6gHVmMKKC`) via `PUT /api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` using `scratch/wyvern_token.txt` and custom User-Agent. Verify HTTP 200.

### 2. R1 & R2 Implementation (Scenarios Sync, Macro Optimization, Slot/Pool Cleaning & PUT)
- Create `ARCHIVIO/scenarios/` directory.
- Move the 4 deleted scenarios from `FINAL/scenarios/` to `ARCHIVIO/scenarios/`:
  - `Svartulfr_Scenario_Camp_Mystic.json`
  - `Svartulfr_Scenario_DMHA_Dungeons.json`
  - `Svartulfr_Scenario_Underworld_Sindacato.json`
  - `Svartulfr_Scenario_Villa_Douglas.json`
- In `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json` and `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json`:
  - Replace all `{{scenarioChar "..."}}` macros targeting retired NPCs (Scarlett, Russ, Jared, Stan, Sierra) and in Jasper Route `twin` (Alyssa) with literal character names, per Explorer R6-1 mapping.
  - In slots: set `pool: []` and `unavailable_count: 0` for all retired card slots. (In Alyssa Route, retain pools for `twin` Jasper and `crush` Mackenzie).
  - Ensure all 8 slot objects remain in `slots` array so `speaker_slot` references on all messages remain valid.
  - Verify `greeting.speaker_slot == messages[0].speaker_slot` and `greeting.content == messages[0].content` on all greetings.
  - Deploy Alyssa Route (`char_scenario_CKgwq246DyCj1NNTBV9rt`) via `PUT` with latest revision. Verify HTTP 200.
  - Deploy Jasper Route (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`) via `PUT` with latest revision. Verify HTTP 200.

### 3. R3 Implementation (Character Cards Reduction to Exactly 8)
- Save pre-delete snapshot of Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`).
- Execute `DELETE https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9` with Bearer token and custom User-Agent. Verify HTTP 204.
- Verify via `GET https://app.wyvern.chat/api/characters/mine` that exactly the 8 approved cards remain (Erik, Malachia, Jasper, Noah, Edric, Logan, Wulfnic, Mackenzie).
- Create `ARCHIVIO/cards_legacy/` directory.
- Move the 6 disused cards from `FINAL/` to `ARCHIVIO/cards_legacy/`:
  - `Alyssa_Douglas_Bloodmoon_card.json`
  - `Jared_Thompson_card.json`
  - `Russ_card.json`
  - `Scarlett_Rose_card.json`
  - `Sierra_Cruz_card.json`
  - `Stan_Davies_Jr_card.json`
- Verify that `FINAL/` contains only the 8 approved card JSON files.

### 4. R5 Implementation & Documentation
- Execute full regression verification GET calls across all endpoints (`/characters/mine`, `/character-scenarios/{id}`, `/lorebooks/{id}`).
- Verify formatting discipline: zero em-dashes (`—`), dialog in double quotes, actions in plain text (no asterisks), no umbrella keywords on NPCs.
- Update `CHANGELOG.md` with detailed records of all changes, revisions, and verifications.
- Produce comprehensive execution report in `e:\repository\SvartulfrVerse\.agents\teamwork\worker_r6_1\handoff.md`.

## 2026-10-21T14:58:26Z

[Message] timestamp=2026-10-21T14:58:26Z sender=65f55b4b-ff49-4608-b683-6827a39956cd priority=MESSAGE_PRIORITY_HIGH content=PRIORITY USER DIRECTIVE & NATIVE WYVERN SCHEMA:

The user has instructed to apply Wyvern's native "DON'T ACTIVATE WHEN ACTIVE" feature to suppress lorebook entries when a character or persona is already active in chat, eliminating the need for the dummy `selective: true` / Dossier keyword workaround.

Wyvern native schema fields on lorebook entries:
- `ignored_characters`: list of character card IDs (strings)
- `ignored_personas`: list of persona IDs (strings)

When one of these is active in chat, Wyvern skips the lorebook entry entirely.

Apply the following to `FINAL/Svartulfr_NPC_Primary.json` (updating both `entries` and `lexicon`):

1. **Alyssa Hvit Douglas Bloodmoon** (`alyssa_world_dossier_2b54a223`):
   - `name`: "Alyssa Hvit Douglas Bloodmoon"
   - `type`: "npc"
   - `selective`: false
   - `secondary_keys`: []
   - `keys`: ["Alyssa Douglas", "Alyssa Hvit", "Alyssa Douglas-Bloodmoon", "Alyssa", "White Moon Alyssa"]
   - `key_logic`: "AND_ANY"
   - `avatar`: "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public"
   - `custom_avatar_regex`: true
   - `lines_parsed`: 1
   - `avatar_activation_regex`: r"(?:^|\n)\s*(?:Alyssa\ Douglas|Alyssa\ Hvit|White\ Moon|Alyssa)\s*:"
   - `npc_info`: {"first_name": "Alyssa", "last_name": "Douglas Bloodmoon", "nicknames": ["White Moon", "Lyssa"], "titles": []}
   - `content`: full 16,957-character JED+ description from `FINAL/Alyssa_Douglas_Bloodmoon_card.json`
   - `ignored_personas`: ["persona_1786335754946"]
   - `ignored_characters`: ["_6exg3yPfe2eCDK4hTftkh"]

2. **Jasper Svartr Douglas Bloodmoon** (`Vcj4h2TL4Usola2A4OOl6`):
   - `name`: "Jasper Svartr Douglas Bloodmoon"
   - `type`: "npc"
   - `selective`: false
   - `secondary_keys`: []
   - `keys`: ["Jasper Douglas", "Jasper Svartr", "Jasper Douglas-Bloodmoon", "Jasper", "Shadow Wolf Jasper"]
   - `key_logic`: "AND_ANY"
   - `avatar`: "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public"
   - `custom_avatar_regex`: true
   - `lines_parsed`: 1
   - `avatar_activation_regex`: r"(?:^|\n)\s*(?:Jasper\ Douglas|Jasper\ Svartr|Shadow\ Wolf|Jasper)\s*:"
   - `npc_info`: {"first_name": "Jasper", "last_name": "Douglas Bloodmoon", "nicknames": ["Shadow Wolf", "Jasp"], "titles": []}
   - `content`: full JED+ description from `FINAL/Jasper_Douglas_Bloodmoon_card.json`
   - `ignored_personas`: ["1792155173728"]
   - `ignored_characters`: ["_t4J9aQNJM36cUKAP4wB4U"]

3. **The 5 Converted NPC Cards**:
   - `Scarlett Rose` (`4NzXF4_0hYxmN7Idltzpw`): `ignored_characters`: ["_qXgBMbFYJfc84hbLHhe92"], `ignored_personas`: []
   - `Sierra Cruz` (`ijy8vrlphNv19-p-gbYuY`): `ignored_characters`: ["_pnrXbkWqcgmFAf3meRWFY"], `ignored_personas`: []
   - `Russell 'Russ' Sinclair` (`YCxAqNoShpefVvk0_Pc7i`): `ignored_characters`: ["_wn6DkCcg3Xqa2Xpx9ttnT"], `ignored_personas`: []
   - `Stanley Davies Jr.` (`ekdQjq63xP7HtNuaPQJQE`): `ignored_characters`: ["_Xd3NhKnRJByMTtdb6PjxJ"], `ignored_personas`: []
   - `Jared Thompson` (`RM6rcwv8MlY1XWaCTQp0M`): `ignored_characters`: ["_xJVPtBLL3dxy69RLKL9X9"], `ignored_personas`: []
   All 5 with full JED+ from source card JSONs, `type`: "npc", `selective`: false, multiline regex, valid avatars, `lines_parsed`: 1, `npc_info`.

4. **The Active Approved Cards in `Svartulfr_NPC_Primary.json`**:
   Add their card IDs to `ignored_characters`:
   - Erik Ulfr Douglas (`C-JisFj8qA1tsFEqZKevk`): `ignored_characters`: ["_QPea6g4Q1QfeYCVHCLMPR"]
   - Malachia Björn Douglas Bloodmoon (`jDuJtzirlEZC3K_ArIufh`): `ignored_characters`: ["_RDfz7XzTpM23LpPALVXHM"]
   - Noah Loki Douglas Bloodmoon (`H2JX-NkHRiJ2FzoekC5ZZ`): `ignored_characters`: ["_zFLUjV8aVxQRAfQxGcAcY"]
   - Logan Dominic Járn Douglas (`tAcrWLtWSDGf3xJJRwUOM`): `ignored_characters`: ["_T8Ywcr9FEqNf9JxbK6eHP"]
   - Wulfnic Báleygr Bloodmoon (`HhuMluMmIIENUei3bX6ed`): `ignored_characters`: ["_HEQQbbRFwKdG8QE2Fh1z1"]
   - Mackenzie Sanchez-Rogers (`BXi3sENAVYB8OKF80Q9Su`): `ignored_characters`: ["_zn24784jfcchQ7EwCyAnm"]

5. In `FINAL/Svartulfr_NPC_Secondary.json`:
   - Edric Douglas (`h-ttmlgJYeRXqyDvQjSX7`): `ignored_characters`: ["_TbRM3EdxDjHFgqztTbCpL"]

Proceed with this native implementation!

## 2026-10-21T15:04:47Z

[Message] timestamp=2026-10-21T15:04:47Z sender=65f55b4b-ff49-4608-b683-6827a39956cd priority=MESSAGE_PRIORITY_HIGH content=Continue with Task 3: R3 Implementation (Snapshot Jared Thompson, execute DELETE via Wyvern API, verify exactly 8 approved cards remain in /characters/mine, create ARCHIVIO/cards_legacy/ and move the 6 legacy cards) and Task 4 (R5 regression verification and documentation).
