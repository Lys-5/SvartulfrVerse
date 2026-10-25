# Handoff Report: Lorebook Primary Restoration & 6 NPC Profiles

**Agent**: Explorer R6-3  
**Role**: teamwork_preview_explorer (Survey & Discovery for R4)  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_3`  
**Recipient**: Parent Orchestrator (`4e0bd8eb-f1f2-49dd-afae-a447f27e63f2`)  
**Timestamp**: 2026-10-21T15:00:00Z  

---

## 1. Observation

1. **`FINAL/Svartulfr_NPC_Primary.json` Entry Identity & Schema**:
   - Total entries: 99 in `entries`, 99 in `lexicon`. `entries == lexicon` evaluates to `True`.
   - Each entry uses `"entry_id"` as its primary key identifier, e.g. line 3161:
     ```json
     "entry_id": "Vcj4h2TL4Usola2A4OOl6"
     ```
   - Target entries found in `FINAL/Svartulfr_NPC_Primary.json`:
     - Scarlett Rose: index 17, `entry_id: "4NzXF4_0hYxmN7Idltzpw"`, `content` len 761 chars, `type: "lore/concept"`, `npc_info: null`, `avatar_activation_regex: null`.
     - Sierra Cruz: index 18, `entry_id: "ijy8vrlphNv19-p-gbYuY"`, `content` len 813 chars, `type: "lore/concept"`, `npc_info: null`, `avatar_activation_regex: null`.
     - Russell 'Russ' Sinclair: index 24, `entry_id: "YCxAqNoShpefVvk0_Pc7i"`, `content` len 1,385 chars, `type: "lore/concept"`, `avatar: null`, `npc_info: null`.
     - Stanley Davies Jr.: index 41, `entry_id: "ekdQjq63xP7HtNuaPQJQE"`, `content` len 779 chars, `type: "lore/concept"`, `npc_info: null`.
     - Jared Thompson: index 62, `entry_id: "RM6rcwv8MlY1XWaCTQp0M"`, `content` len 793 chars, `type: "lore/concept"`, `npc_info: null`.
     - Alyssa Hvit Douglas Bloodmoon: index 98, `entry_id: "alyssa_world_dossier_2b54a223"`, `content` len 902 chars, `type: "lore/concept"`, `selective: true`, `secondary_keys: ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]`, `avatar: ""` (empty string).

2. **Wyvern Web API Status**:
   - `GET https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` with Bearer token from `scratch/wyvern_token.txt` and `User-Agent: AuditorBot/1.0`:
     - Status: `HTTP 200 OK`.
     - Payload keys: `['id', '_id', 'created_at', 'updated_at', 'photoURL', 'name', 'description', 'scan_depth', 'token_budget', 'recursive_scanning', 'extensions', 'lexicon', ...]`
     - `len(data['lexicon']) == 99`.

3. **Jasper Persona Protection Record**:
   - Index 60, `entry_id: "Vcj4h2TL4Usola2A4OOl6"`:
     ```json
     {
       "entry_id": "Vcj4h2TL4Usola2A4OOl6",
       "keys": ["Jasper Douglas", "Jasper Svartr", "Jasper Douglas-Bloodmoon"],
       "secondary_keys": ["Dossier", "Scheda", "Archivio", "Database", "Profilo"],
       "key_logic": "AND_ANY",
       "selective": true,
       "type": "lore/concept",
       "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public"
     }
     ```

4. **Source Card Files in `FINAL/`**:
   Direct inspection of card files verified:
   - `FINAL/Scarlett_Rose_card.json`: description length 4,777 chars, avatar `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c8bdfad3-bb90-4e38-9642-f28a6f3b0600/public`.
   - `FINAL/Sierra_Cruz_card.json`: description length 5,117 chars, avatar `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c8bdfad3-bb90-4e38-9642-f28a6f3b0600/public`.
   - `FINAL/Russ_card.json`: description length 5,505 chars, avatar `https://ella.janitorai.com/bot-avatars/9yrobVTbiGDRLHlS6GtIz.webp`.
   - `FINAL/Stan_Davies_Jr_card.json`: description length 8,008 chars, avatar `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7c9c7d1-51e6-4441-82e3-c6ab5f537500/public`.
   - `FINAL/Jared_Thompson_card.json`: description length 8,696 chars, avatar `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7476db0-8dae-4450-8c84-3408b375c000/public`.
   - `FINAL/Alyssa_Douglas_Bloodmoon_card.json`: description length 16,957 chars, avatar `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public`.
   - Compliance check: 0 em-dashes, 0 action asterisks, 0 illegal macros (`{{user}}`, `{{age}}`), 0 `\ufffd` corruption across all 6 files.

---

## 2. Logic Chain

1. From Observation 1, the 6 target entries in `FINAL/Svartulfr_NPC_Primary.json` are currently short stubs under 1,400 characters, missing avatars, or missing NPC metadata.
2. From Observation 4, complete and compliant JED+ source descriptions exceeding 2,000 characters exist for all 6 characters in `FINAL/*_card.json`.
3. From Observation 3, Jasper's record demonstrates the canonical protection mechanism against Persona duplicate hallucination: setting `selective: true` with `secondary_keys: ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]`, `key_logic: "AND_ANY"`, and `type: "lore/concept"` prevents context injection during normal conversation while allowing explicit dossier lookups.
4. From Observation 1, Alyssa (`alyssa_world_dossier_2b54a223`) already has `selective: true` and the dossier `secondary_keys`, but is missing a valid avatar (`avatar: ""`) and full content (only 902 chars). Updating her record with the card's valid Cloudflare avatar (`ba5a7fed...`) and full description (16,957 chars) achieves exact parity with Jasper.
5. For Scarlett, Sierra, Russ, Stan, and Jared, because they are no longer standalone player cards or personas in `/characters/mine` (R3 dismission), they function purely as NPCs in character scenarios. Therefore, they must have `type: "npc"`, `selective: false`, `secondary_keys: []`, `custom_avatar_regex: true`, `lines_parsed: 1`, multiline `avatar_activation_regex`, and structured `npc_info` for proper UI avatar splitting.
6. From Observation 2, live Wyvern API lorebook `_zwEqgEEzh12X6gHVmMKKC` expects payload with property `lexicon`. Therefore, the worker must update both `entries` and `lexicon` in `FINAL/Svartulfr_NPC_Primary.json` and transmit the updated `lexicon` via `PUT`.

---

## 3. Caveats

- **Network User-Agent**: Any HTTP request sent to `https://app.wyvern.chat` must include a custom User-Agent (such as `AuditorBot/1.0`); default `Python-urllib` triggers Cloudflare 403 error 1010.
- **Card Dismission**: The 6 source card files in `FINAL/` are scheduled to be moved to `ARCHIVIO/cards_legacy/` under R3 during implementation. The Worker should extract their descriptions before moving the files or read them from `FINAL/` before relocation.
- No other caveats.

---

## 4. Conclusion

1. The target entries in `FINAL/Svartulfr_NPC_Primary.json` are identified at indices 17, 18, 24, 41, 62, and 98.
2. Full JED+ descriptions (>2,000 chars) are verified and ready for extraction from `FINAL/*_card.json`.
3. Alyssa's record must be updated with avatar `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public` and 16,957 characters of JED+ description, preserving `selective: true` and the 5 dossier secondary keys.
4. Scarlett, Sierra, Russ, Stan, and Jared must be upgraded to `type: "npc"`, `selective: false`, valid avatars, multiline avatar activation regexes, and `npc_info`.
5. A simulation script (`scratch/test_simulation.py`) confirmed that applying these updates modifies exactly 6 entries, maintains the 99 total entry count, and produces schema-compliant JSON.

---

## 5. Verification Method

To independently verify these findings:
1. Run `python scratch/inspect_targets_final.py` (or inspect `FINAL/Svartulfr_NPC_Primary.json`) to confirm indices 17, 18, 24, 41, 62, and 98 and their current state.
2. Run `python scratch/audit_card_descriptions.py` to confirm description lengths (>2,000 chars) and zero formatting violations.
3. Run `python scratch/check_wyvern_lorebook.py` to verify HTTP 200 on `_zwEqgEEzh12X6gHVmMKKC` and 99 live entries.
4. Run `python scratch/test_simulation.py` to verify update mechanics.

*Invalidation conditions*:
- If Wyvern API rejects `PUT /api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` with status != 200.
- If total entry count in `FINAL/Svartulfr_NPC_Primary.json` departs from 99.
- If Alyssa triggers during normal persona gameplay without the secondary keys.
