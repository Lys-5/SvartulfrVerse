# Handoff Report — Explorer 1 (Schema & Wyvern API Explorer)

**Target Milestone**: Svartúlfr Verse Character Scenarios Deployment  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_1`  
**Date**: 2026-10-20T17:23:00Z  

---

## 1. Observation

### 1.1 Direct Repository Evidence
- **Authoritative Requirements**: `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (lines 55–116) dictates the creation and deployment of 6 thematic scenario files in `FINAL/scenarios/` with 6 standalone lorebook IDs, `visibility: "unlisted"`, zero em-dashes, dialogue in quotes, plain text narration, and `unavailable_count: 0`.
- **Existing Master Scenario**: `FINAL/Svartulfr_Master_Scenario.json` (ID: `char_scenario_1DC43ggb6mB8YLJDJKrU4`) contains 13 slots, 29 greetings, root fields:
  ```json
  ['slot_count', 'greeting_count', 'id', 'name', 'display_description', 'avatar', 'tags', 'visibility', 'rating', 'status', 'revision', 'creator_uid', 'updated_at', 'linked_world_id', 'scenario', 'startup_script', 'slots', 'greetings', 'lorebook_ids', 'lorebooks', 'gallery', 'moderation_reason']
  ```
- **Validation Constants (`scratch/test_build_master_scenario_payload.py`, lines 9–17)**:
  - `name`: 1 to 200 characters, trimmed.
  - `display_description`: 0 to 20,000 characters.
  - `scenario`: 0 to 100,000 characters (the shared scenario prompt / Scenario Override).
  - `slots`: 1 to 20 slots. Slot key must match regex `^[a-zA-Z][a-zA-Z0-9_-]{0,63}$`, unique keys, label 1 to 120 characters, pool weights 0 to 1,000,000.
  - `greetings`: 1 to 100 greetings. Greeting name 1 to 200 characters, description 0 to 10,000 characters, content 0 to 100,000 characters.
  - `messages`: 1 to 20 messages per greeting, content 0 to 100,000 characters, `speaker_slot` must exist in `slots[].key`.
  - Root parity rule: `greeting.content == messages[0].content` and `greeting.speaker_slot == messages[0].speaker_slot`.

### 1.2 Live Wyvern API Observations
- **Endpoint GET**: `GET https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4`  
  - Tested with Bearer token in `scratch/wyvern_token.txt`: returned `HTTP 200 OK`, `Revision: 27`.
  - Confirmed fields `system_prompt` and `final_instructions` are not persisted on scenario entities by Wyvern (all context directives must be placed inside the root `scenario` field).
  - Confirmed `entry_restrictions` does not exist on Wyvern Character Scenarios entities.
- **Card Availability Check**:
  - Live query of the 14 canonical character cards in `FINAL/`:
    1. `_HEQQbbRFwKdG8QE2Fh1z1`: Wulfnic Báleygr Bloodmoon (`HTTP 200`)
    2. `_QPea6g4Q1QfeYCVHCLMPR`: Erik Ulfr Douglas (`HTTP 200`)
    3. `_RDfz7XzTpM23LpPALVXHM`: Malachia Björn Douglas Bloodmoon (`HTTP 200`)
    4. `_zFLUjV8aVxQRAfQxGcAcY`: Noah Loki Douglas Bloodmoon (`HTTP 200`)
    5. `_t4J9aQNJM36cUKAP4wB4U`: Jasper Svartr Douglas Bloodmoon (`HTTP 200`)
    6. `_6exg3yPfe2eCDK4hTftkh`: Alyssa Hvit Douglas Bloodmoon (`HTTP 200`)
    7. `_T8Ywcr9FEqNf9JxbK6eHP`: Logan Járn Douglas (`HTTP 200`)
    8. `_TbRM3EdxDjHFgqztTbCpL`: Edric Douglas (`HTTP 200`)
    9. `_xJVPtBLL3dxy69RLKL9X9`: Jared Thompson (`HTTP 200`)
    10. `_Xd3NhKnRJByMTtdb6PjxJ`: Stanley Davies Jr. (`HTTP 200`)
    11. `_zn24784jfcchQ7EwCyAnm`: Mackenzie Sanchez-Rogers (`HTTP 200`)
    12. `_pnrXbkWqcgmFAf3meRWFY`: Sierra Cruz (`HTTP 200`)
    13. `_qXgBMbFYJfc84hbLHhe92`: Scarlett Rose (`HTTP 200`)
    14. `_wn6DkCcg3Xqa2Xpx9ttnT`: Russell 'Russ' (`HTTP 200`)
  - Secondary/NPC IDs (`_K3C7KVy9eddtTF8aWX9gk`, `_EnRGd1jfbjTTGmz4EFJdd`, `_zBD6rWUkJBAjLfXnja4xh`, `_dJ7nRMQEbcUgdWG96MqLz`, `_3tMk6cRAFewRnKMkdJ4XU`, `_2EezhhEVdL677DULVdE9h`): returned `HTTP 404 Not Found`. They are managed exclusively through Lorebook NPC entries in `Svartulfr_NPC_Primary.json` and `Svartulfr_NPC_Secondary.json`.
- **Unavailable Count Root Cause**:
  In `scratch/live_scenario_current.json`, slots that had non-existent or deleted `character_id`s in their `pool` had `unavailable_count: 1`. Slots with an empty pool (`pool: []`) or containing valid active cards had `unavailable_count: 0`.

---

## 2. Logic Chain

1. **API Persistence & Schema Constraints**:
   - Because `GET /api/character-scenarios/{id}` returns the canonical state from Wyvern, any field not defined in the Wyvern schema is dropped.
   - Specifically, `scenario` is the authoritative field that Wyvern copies into the chat log as the `Scenario Override`. Therefore, all setting lore, character relationship summaries, format instructions, anti-ventriloquism rules, and perspective suppression invariants must reside inside `scenario`.
   - `display_description` is reader-facing only (shown on explore cards/overview in Markdown) and is not injected into the model's context.

2. **Slot Architecture and `unavailable_count` Invariant**:
   - Wyvern calculates `unavailable_count` by scanning each candidate in `slot.pool`. If any `character_id` is missing, unapproved, private to another user, or deleted, `unavailable_count` increments.
   - For slots representing canonical characters with active cards (the 14 cards verified above), `pool` must contain `[{"character_id": "<card_id>", "weight": 100}]`.
   - For slots representing NPCs (e.g. `supervisor`, `director`, `biker_enforcer`, `raid_leader`, `syndicate_boss`, etc.) or open student/camper roles (`cabin_mate_1`, `camper_peer_1`), `pool` must be `[]` (empty array).
   - An empty pool `[]` produces `unavailable_count: 0`, satisfies Wyvern's schema validation, and allows players to assign any card dynamically or rely on Lorebook NPC dialogue parsing.

3. **Multi-Message Greeting Invariants**:
   - Wyvern requires top-level alignment:
     `greeting.content === greeting.messages[0].content`  
     `greeting.speaker_slot === greeting.messages[0].speaker_slot`
   - Every message within `messages[]` must specify a `speaker_slot` that exists in `slots[].key`.
   - The UI automatically prepends the sender's display name to each message. As a result, message content must never include hardcoded speaker name prefixes (e.g. `Santiago Herrera: ...` inside greeting messages).
   - In-scene macros must use `{{scenarioChar "slot_key"}}` to refer to other slots, `{{char}}` for the current message sender, and `{{user}}` for the player.

4. **Formatting Invariants**:
   - Rule 03 / GEMINI.md mandate:
     - Zero em-dashes (`—`); replaced strictly with commas (`,`) or periods (`.`).
     - Spoken dialogue strictly in standard double quotes (`"..."`).
     - Actions, body language, and environmental narration in plain text (no asterisks).
     - Asterisks (`*...*`) reserved strictly for unvoiced internal thoughts.
     - Foreign phrases formatted as: `"Original phrase"` followed by `([Italian translation])`.

5. **Deployment Protocol**:
   - `POST https://app.wyvern.chat/api/character-scenarios` requires:
     * Headers: `Authorization: Bearer <token>`, `Content-Type: application/json`, `Accept: application/json`, `User-Agent: Mozilla/5.0...`.
     * `visibility: "unlisted"`.
     * `rating: "explicit"`.
     * Array of 6 standalone Lorebook IDs in `lorebook_ids`.
     * Pacing delay of 2.5 seconds between API requests.
   - Post-deployment verification requires `GET https://app.wyvern.chat/api/character-scenarios/{new_id}` returning `HTTP 200`, confirming `slot_count`, `greeting_count`, and `lorebook_ids`.

---

## 3. Caveats

1. **Persona Linking in Greetings**:
   - Greetings with `linked_persona_ids` (e.g. `persona_1786335754946` for Alyssa, `1792155173728` for Jasper) will only succeed if the creator owns those personas and they have `can_fork: true`. If a persona is not forkable, Wyvern returns `HTTP 400: Only your own forkable personas can be offered`.
   - For generic or dual-perspective greetings, `linked_persona_ids` should be `[]`.
2. **Character Scenarios vs World Mode**:
   - In Character Scenarios, World Engine features (dynamic clocks, location grids, item inventories) are replaced by standalone Lorebooks and the Handlebars/Lua runtime. Macro `{{age}}` is non-functional and must never be used.
3. **API Endpoints**:
   - The official endpoint host is `https://app.wyvern.chat/api/` (never use `api.wyvern.chat`, which lacks scenario routing).

---

## 4. Conclusion

### 4.1 Definitive Character Scenario JSON Schema Specification

```json
{
  "name": "Scenario Title (string, 1-200 chars, trimmed)",
  "display_description": "Reader-facing Markdown description (string, 0-20000 chars)",
  "avatar": "https://imagedelivery.net/.../public (string, valid image URL or \"\")",
  "tags": ["Werewolf", "College", "Urban Fantasy", "Demihuman"],
  "visibility": "unlisted",
  "rating": "explicit",
  "scenario": "Setting, cast definitions, rules, format discipline, and anti-ventriloquism directives (string, 0-100000 chars)",
  "startup_script": "-- Optional Lua startup script for slot resolution\n",
  "slots": [
    {
      "key": "slot_key (regex: ^[a-zA-Z][a-zA-Z0-9_-]{0,63}$)",
      "label": "Human Readable Slot Label (string, 1-120 chars)",
      "pool": [
        {
          "character_id": "_validCardId",
          "weight": 100
        }
      ],
      "unavailable_count": 0
    }
  ],
  "greetings": [
    {
      "id": "opening (string unique ID)",
      "name": "01. Greeting Title (string, 1-200 chars)",
      "description": "Reader-facing greeting summary (string, 0-10000 chars)",
      "content": "Must exactly match messages[0].content",
      "speaker_slot": "Must exactly match messages[0].speaker_slot",
      "linked_persona_ids": [],
      "messages": [
        {
          "id": "msg-1 (string unique ID)",
          "speaker_slot": "slot_key",
          "content": "Dialogue in quotes, narration in plain text, thoughts in *asterisks*, zero em-dashes."
        }
      ]
    }
  ],
  "lorebook_ids": [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV"
  ],
  "gallery": [],
  "linked_world_id": ""
}
```

### 4.2 Slot Pool Strategy for the 6 Thematic Scenarios

| Scenario | Slots & Pool Specification |
|---|---|
| **1. Camp Mystic** (8 slots) | - `twin`: pool with Jasper (`_t4J9aQNJM36cUKAP4wB4U`) + Alyssa (`_6exg3yPfe2eCDK4hTftkh`), weight 100.<br>- `cousin`: pool with Edric (`_TbRM3EdxDjHFgqztTbCpL`), weight 100.<br>- `supervisor`: pool `[]` (resolved via Lua: Marcus Vale vs Celeste Nadir).<br>- `director`: pool `[]` (Mara Voss, Lorebook NPC).<br>- `cabin_mate_1`, `cabin_mate_2`, `camper_peer_1`, `camper_peer_2`: pool `[]`. |
| **2. SUCC Route Alyssa** (8 slots) | - `twin`: pool with Jasper (`_t4J9aQNJM36cUKAP4wB4U`), weight 100.<br>- `best_friend`: pool with Scarlett Rose (`_qXgBMbFYJfc84hbLHhe92`), weight 100.<br>- `crush`: pool with Mackenzie Sanchez-Rogers (`_zn24784jfcchQ7EwCyAnm`), weight 100.<br>- `roommate`: pool with Sierra Cruz (`_pnrXbkWqcgmFAf3meRWFY`), weight 100.<br>- `childhood_friend`: pool `[]` (Finnegan Novak, Arctic Wolf demi-human Lorebook NPC).<br>- `quarterback`: pool with Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`), weight 100.<br>- `friend`: pool with Stanley Davies Jr. (`_Xd3NhKnRJByMTtdb6PjxJ`), weight 100.<br>- `sports_rival`: pool `[]` (Vincent Campbell, Bears captain Lorebook NPC). |
| **3. SUCC Route Jasper** (8 slots) | - `twin`: pool with Alyssa (`_6exg3yPfe2eCDK4hTftkh`), weight 100.<br>- `male_roommate`: pool with Russell 'Russ' Sinclair (`_wn6DkCcg3Xqa2Xpx9ttnT`), weight 100.<br>- `crush`: pool with Scarlett Rose (`_qXgBMbFYJfc84hbLHhe92`), weight 100.<br>- `ai_companion`: pool `[]` (Echo, digital persona/Lorebook NPC).<br>- `childhood_friend`: pool `[]` (Finnegan Novak).<br>- `quarterback`: pool with Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`), weight 100.<br>- `friend`: pool with Stanley Davies Jr. (`_Xd3NhKnRJByMTtdb6PjxJ`), weight 100.<br>- `sports_rival`: pool `[]` (Vincent Campbell). |
| **4. Villa Douglas** (7 slots) | Exactly the 7 canonical male cards with weight 100:<br>- `father`: Erik Ulfr Douglas (`_QPea6g4Q1QfeYCVHCLMPR`)<br>- `eldest_brother`: Malachia Björn Douglas Bloodmoon (`_RDfz7XzTpM23LpPALVXHM`)<br>- `tech_brother`: Jasper Svartr Douglas Bloodmoon (`_t4J9aQNJM36cUKAP4wB4U`)<br>- `politician_brother`: Noah Loki Douglas Bloodmoon (`_zFLUjV8aVxQRAfQxGcAcY`)<br>- `maternal_grandfather`: Wulfnic Báleygr Bloodmoon (`_HEQQbbRFwKdG8QE2Fh1z1`)<br>- `uncle`: Logan Járn Douglas (`_T8Ywcr9FEqNf9JxbK6eHP`)<br>- `cousin`: Edric Douglas (`_TbRM3EdxDjHFgqztTbCpL`) |
| **5. DMHA Dungeons** (9 slots) | - `twin_healer`: pool with Alyssa (`_6exg3yPfe2eCDK4hTftkh`), weight 100.<br>- `twin_tech`: pool with Jasper (`_t4J9aQNJM36cUKAP4wB4U`), weight 100.<br>- `eldest_brother`: pool with Malachia (`_RDfz7XzTpM23LpPALVXHM`), weight 100.<br>- `demihuman_representative`: pool `[]` (Barrow, Lorebook NPC).<br>- `biker_enforcer`: pool `[]` (Marek, Lorebook NPC).<br>- `raid_leader`: pool `[]` (Radek, Lorebook NPC).<br>- `tank_frontline`: pool `[]` (Goran, Lorebook NPC).<br>- `scout_infiltrator`: pool `[]` (Kian, Lorebook NPC).<br>- `faction_support`: pool `[]` (DMHA strike team / Nomads). |
| **6. Underworld Sindacato** (6 slots) | - `syndicate_boss`: pool `[]` (Ruaraidh "Rory" Ballantine, Lorebook NPC).<br>- `syndicate_fixer`: pool `[]` (Sullivan "Sully" Jones, Lorebook NPC).<br>- `sinners_leader`: pool `[]` (Jean-Luc Virtuoso [Human Telepath], Lorebook NPC).<br>- `sinners_matriarch`: pool `[]` (Alicia Virtuoso, Lorebook NPC).<br>- `sinners_alchemist`: pool `[]` (Dr. Arthur Sinclair, Lorebook NPC).<br>- `mercenary_tracker`: pool `[]` (Ilya Volkov / Vasile Ionescu, Lorebook NPCs). |

### 4.3 Standard Lua Startup Script Template for Camp Mystic

```lua
-- Camp Mystic Dynamic Supervisor & Cabin Mate Resolution
if memory and memory._scenario and memory._scenario.assignments then
    local p_id = (user and user.persona_id) or (memory._scenario.persona_id) or ''
    local u_name = string.lower((user and user.name) or '')
    local sub = string.lower((user and (user.pronoun_subjective or (user.pronouns and user.pronouns.subjective))) or '')
    local obj = string.lower((user and (user.pronoun_objective or (user.pronouns and user.pronouns.objective))) or '')

    local is_female = (sub == 'she' or obj == 'her' or string.find(u_name, 'alyssa') or string.find(u_name, 'female') or string.find(u_name, 'femmina'))
    local is_male = (sub == 'he' or obj == 'him' or string.find(u_name, 'jasper') or string.find(u_name, 'male') or string.find(u_name, 'maschio'))

    local alyssa_id = '_6exg3yPfe2eCDK4hTftkh'
    local jasper_id = '_t4J9aQNJM36cUKAP4wB4U'

    if is_female then
        memory._scenario.assignments['twin'] = jasper_id
        -- Female Camper assigns Celeste Nadir and Girls Zone
        memory._scenario.supervisor_role = 'Celeste Nadir (Moonflower Cabin)'
    elseif is_male then
        memory._scenario.assignments['twin'] = alyssa_id
        -- Male Camper assigns Marcus Vale and Boys Zone
        memory._scenario.supervisor_role = 'Marcus Vale (Lake Wolf Cabin)'
    else
        -- Neutral fallback
        math.randomseed(os.time())
        if math.random(1, 2) == 1 then
            memory._scenario.assignments['twin'] = alyssa_id
            memory._scenario.supervisor_role = 'Marcus Vale (Lake Wolf Cabin)'
        else
            memory._scenario.assignments['twin'] = jasper_id
            memory._scenario.supervisor_role = 'Celeste Nadir (Moonflower Cabin)'
        end
    end
end
```

---

## 5. Verification Method

To independently verify all findings and validate future scenario payloads:

1. **Verify Token & API Connectivity**:
   ```bash
   python -c "import urllib.request, json; token = open('scratch/wyvern_token.txt').read().strip(); req = urllib.request.Request('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}); resp = urllib.request.urlopen(req); print('HTTP', resp.status, 'Revision:', json.loads(resp.read().decode()).get('revision'))"
   ```
   *Expected result*: `HTTP 200 Revision: 27`

2. **Verify JSON Payload against Client Constraints**:
   Run schema check on any generated scenario JSON before POST:
   ```python
   def validate_scenario(sc):
       assert 1 <= len(sc['name']) <= 200, "Invalid name length"
       assert len(sc.get('display_description', '')) <= 20000, "display_description > 20000"
       assert len(sc['scenario']) <= 100000, "scenario > 100000"
       assert 1 <= len(sc['slots']) <= 20, "Slots count must be 1-20"
       keys = {s['key'] for s in sc['slots']}
       assert len(keys) == len(sc['slots']), "Duplicate slot keys"
       for s in sc['slots']:
           assert re.match(r'^[a-zA-Z][a-zA-Z0-9_-]{0,63}$', s['key']), f"Invalid key: {s['key']}"
           assert s.get('unavailable_count', 0) == 0, f"unavailable_count != 0 on slot {s['key']}"
       assert 1 <= len(sc['greetings']) <= 100, "Greetings count must be 1-100"
       for g in sc['greetings']:
           assert 1 <= len(g.get('messages', [])) <= 20, "Messages count must be 1-20"
           assert g['content'] == g['messages'][0]['content'], "Root content != messages[0]"
           assert g['speaker_slot'] == g['messages'][0]['speaker_slot'], "Root speaker_slot != messages[0]"
           assert '—' not in g['content'], "Em-dash found in greeting"
   ```

3. **Verify Deployment API Call Structure**:
   ```python
   # POST new scenario
   url = "https://app.wyvern.chat/api/character-scenarios"
   req = urllib.request.Request(
       url,
       data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
       headers={
           'Authorization': f'Bearer {token}',
           'Content-Type': 'application/json',
           'Accept': 'application/json',
           'User-Agent': 'Mozilla/5.0'
       },
       method='POST'
   )
   # Response returns HTTP 200/201 with new scenario object containing assigned id ('char_scenario_...')
   ```
