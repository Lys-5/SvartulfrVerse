# Handoff Report: Survey of 7 Core Character Cards and Lorebook Target Records

**Date:** 2026-10-21  
**Agent:** Explorer R7-1 (Core NPC & Card Investigator)  
**Parent Orchestrator:** `d09a4dde-d2c9-4ad5-93e8-4df0f18d6608`  
**Milestone:** Milestone 7 — Requirement R1 Survey & Specification  

---

## 1. Observation

### 1.1 The 7 Standalone Character Cards (`FINAL/`)
Through direct JSON parsing and validation scripts (`scratch/inspect_r7_cards.py`, `scratch/check_card_formatting.py`, `scratch/card_summary.py`):
1. **Erik Ulfr Douglas** (`FINAL/Erik_Douglas_card.json`):
   - ID: `_QPea6g4Q1QfeYCVHCLMPR`
   - Name: `Erik Ulfr Douglas`
   - Description Length: **22,775 characters** (395 lines).
   - Avatar URL: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61648731-7c96-454d-95e5-e27aa69d8c00/public`
   - Sections present: Initial JED+ bracket block, `BACKSTORY:`, `FAMILY & PACK:`, `VOICE & BEHAVIOR:`, `THE HELICOPTER:`, `GRIEF & INTIMACY:`, `THE FRESHMAN:`, `THE PARENTS' EVENING:`, `SPARRING:`, `THE WEIGHT HE CARRIES:`, `SEXUALITY & INTIMACY:`, `SIGNATURE VEHICLE & ASSETS:`, `RPG STATS & TRAITS:` (`[LEVEL: 47]`, S.P.E.C.I.A.L. stats, 7 traits).
   - Formatting violations: 0 em-dashes (`—`), 0 asterisks, 0 residual `{{age}}` macros.

2. **Malachia Björn Douglas Bloodmoon** (`FINAL/Malachia_Douglas_Bloodmoon_card.json`):
   - ID: `_RDfz7XzTpM23LpPALVXHM`
   - Name: `Malachia Björn Douglas Bloodmoon`
   - Description Length: **18,520 characters** (320 lines).
   - Avatar URL: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d77a20fc-49da-4f35-a311-1539ef698d00/public`
   - Sections present: Initial bracket block, `THE DISTANCE HE HAS ALREADY CLOSED:`, `BACKSTORY:`, `FAMILY & PACK:`, `THE SECRET HE CARRIES:`, `VOICE & BEHAVIOR:`, `SPARRING:`, `SEXUALITY & INTIMACY:`, `SIGNATURE VEHICLE & GEAR:`, `RPG STATS & TRAITS:` (`[LEVEL: 24]`, S.P.E.C.I.A.L. stats, 7 traits).
   - Formatting violations: 0 em-dashes, 0 asterisks, 0 residual `{{age}}` macros.

3. **Noah Loki Douglas Bloodmoon** (`FINAL/Noah_Douglas_Bloodmoon_card.json`):
   - ID: `_zFLUjV8aVxQRAfQxGcAcY`
   - Name: `Noah Loki Douglas Bloodmoon`
   - Description Length: **10,398 characters** (188 lines).
   - Avatar URL: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/968cc93e-879d-4aab-94b7-3838f94a9e00/public`
   - Sections present: Initial bracket block, `BACKSTORY:`, `FAMILY & PACK:`, `VOICE & BEHAVIOR:`, `THE WEIGHT HE CARRIES:`, `SEXUALITY & INTIMACY:`, `SIGNATURE VEHICLE & ASSETS:`, `RPG STATS & TRAITS:` (`[LEVEL: 22]`, S.P.E.C.I.A.L. stats, 7 traits).
   - Formatting violations: 0 em-dashes, 0 asterisks, 0 residual `{{age}}` macros.

4. **Logan Járn Douglas** (`FINAL/Logan_Douglas_card.json`):
   - ID: `_T8Ywcr9FEqNf9JxbK6eHP`
   - Name: `Logan Járn Douglas`
   - Description Length: **13,735 characters** (254 lines).
   - Avatar URL: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/0b5a932b-0a3b-4e0b-8257-49f18fedae00/public`
   - Sections present: Initial bracket block, `BACKSTORY:`, `FAMILY & PACK:`, `VOICE & BEHAVIOR:`, `THE WEIGHT HE CARRIES:`, `SEXUALITY & INTIMACY:`, `SIGNATURE VEHICLE & TOOLS:`, `RPG STATS & TRAITS:` (`[LEVEL: 42]`, S.P.E.C.I.A.L. stats, 6 traits).
   - Formatting violations: 0 em-dashes, 0 asterisks, 0 residual `{{age}}` macros.

5. **Wulfnic Báleygr Bloodmoon** (`FINAL/Wulfnic_Bloodmoon_card.json`):
   - ID: `_HEQQbbRFwKdG8QE2Fh1z1`
   - Name: `Wulfnic Báleygr Bloodmoon`
   - Description Length: **14,530 characters** (259 lines).
   - Avatar URL: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/683beb87-8091-4b5a-e6fd-8acb0a159500/public`
   - Sections present: Initial bracket block, `BACKSTORY:`, `FAMILY & PACK:`, `VOICE & BEHAVIOR:`, historical subsections (`THE WEIGHT OF MILLENNIA:`, `FORMER TITLES:`, `THE HUNDREDS:`, `THE FIRST HUNT:`, `THE WOLVES THAT CAME FROM NOWHERE:`, `THE GRANDFATHER:`), `THE WEIGHT HE CARRIES:`, `SEXUALITY & INTIMACY:`, `SIGNATURE VEHICLE & RELICS:`, `RPG STATS & TRAITS:` (`[LEVEL: 99]`, S.P.E.C.I.A.L. stats, 6 traits).
   - Formatting violations: 0 em-dashes, 0 asterisks, 0 residual `{{age}}` macros.

6. **Mackenzie Sanchez-Rogers** (`FINAL/Mackenzie_Sanchez_Rogers_card.json`):
   - ID: `_zn24784jfcchQ7EwCyAnm`
   - Name: `Mackenzie Sanchez-Rogers`
   - Description Length: **9,618 characters** (166 lines).
   - Avatar URL: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public`
   - Sections present: Initial bracket block, `BACKSTORY:`, `FAMILY & PACK:`, `VOICE & BEHAVIOR:`, `BAND & RELATIONSHIPS:`, `THE BLOOD HE DOES NOT KNOW HE HAS:`, `THE ALPHA HE IS COPYING:`, `THE WEIGHT HE CARRIES:`, `SEXUALITY & INTIMACY:`, `RPG STATS & TRAITS:` (`[LEVEL: 19]`, S.P.E.C.I.A.L. stats, 10 traits).
   - Formatting violations: 0 em-dashes, 0 asterisks, 0 residual `{{age}}` macros.

7. **Edric Douglas** (`FINAL/Edric_Douglas_card.json`):
   - ID: `_TbRM3EdxDjHFgqztTbCpL`
   - Name: `Edric Douglas`
   - Description Length: **7,240 characters** (130 lines).
   - Avatar URL: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public`
   - Sections present: Initial bracket block, `BACKSTORY:`, `FAMILY & PACK:`, `SOLARTON JUNIOR FOOTBALL & JET THOMPSON:`, `VOICE & BEHAVIOR:`, `THE WEIGHT HE CARRIES:`, `SEXUALITY & INTIMACY:` (juvenile minor non-applicable statement), `RPG STATS & TRAITS:` (`[LEVEL: 13]`, S.P.E.C.I.A.L. stats, 7 traits).
   - Formatting violations: 0 em-dashes, 0 asterisks, 0 residual `{{age}}` macros.

### 1.2 Target Entries in Lorebooks
Examined via `scratch/inspect_targets.py` and `scratch/check_entries_lexicon_targets.py`:
- In both lorebooks, `entries` and `lexicon` arrays are identical in length and ID ordering (Primary has 99 entries; Secondary has 211 entries).
- All 7 target entries currently have `type: "lore/concept"`, `selective: None` (or `False`), `custom_avatar_regex: None`, `avatar_activation_regex: None`, `lines_parsed: None`, and `npc_info: None`.
- Descriptions in target lorebook records are short stub summaries:
  - Erik (`C-JisFj8qA1tsFEqZKevk`): 877 chars
  - Malachia (`jDuJtzirlEZC3K_ArIufh`): 894 chars
  - Noah (`H2JX-NkHRiJ2FzoekC5ZZ`): 817 chars
  - Logan (`tAcrWLtWSDGf3xJJRwUOM`): 847 chars
  - Wulfnic (`HhuMluMmIIENUei3bX6ed`): 923 chars
  - Mackenzie (`BXi3sENAVYB8OKF80Q9Su`): 1,214 chars
  - Edric (`h-ttmlgJYeRXqyDvQjSX7`): 960 chars
- **All 7 entries already have their respective Card ID configured in `ignored_characters`**:
  - Erik: `['_QPea6g4Q1QfeYCVHCLMPR']`
  - Malachia: `['_RDfz7XzTpM23LpPALVXHM']`
  - Noah: `['_zFLUjV8aVxQRAfQxGcAcY']`
  - Logan: `['_T8Ywcr9FEqNf9JxbK6eHP']`
  - Wulfnic: `['_HEQQbbRFwKdG8QE2Fh1z1']`
  - Mackenzie: `['_zn24784jfcchQ7EwCyAnm']`
  - Edric: `['_TbRM3EdxDjHFgqztTbCpL']`
- **Avatar Inconsistencies:**
  - Erik lorebook entry has `30fe0390-05fb-46cf-2c8a-cd98fc35c700` vs card `61648731-7c96-454d-95e5-e27aa69d8c00`.
  - Malachia lorebook entry has `c883ae1e-d817-4f80-e4bb-388aaea84d00` vs card `d77a20fc-49da-4f35-a311-1539ef698d00`.
  - Noah lorebook entry has `12f497d7-7147-4d38-c2de-c57892180800` vs card `968cc93e-879d-4aab-94b7-3838f94a9e00`.
  - Logan lorebook entry has `5d7d3ade-f742-41da-979b-670102fead00` vs card `0b5a932b-0a3b-4e0b-8257-49f18fedae00`.
  - Wulfnic lorebook entry has `554744b5-0e23-45b9-005a-4629abd35500` vs card `683beb87-8091-4b5a-e6fd-8acb0a159500`.
  - Edric lorebook entry has `13c49c40-2378-4678-ca5d-6e2ef84eba00` vs card `ed348ea6-c40c-461c-f90e-d09e742c3400`.
  - Only Mackenzie matches (`87f28fb6-557f-4eaf-9c7c-0cddfbe5c300`).
- **Token Budget:**
  - `FINAL/Svartulfr_NPC_Primary.json` currently has `token_budget: 5000`. Must be increased to `7500`.
  - `FINAL/Svartulfr_NPC_Secondary.json` currently has `token_budget: 5000`. Conforms to requirement (5000).

---

## 2. Logic Chain

1. **Observation 1.1 shows** that all 7 standalone cards have complete, pristine JED+ text dossiers (>7,200 to >22,700 chars), with 0 formatting violations, complete vehicles/intimacy/RPG blocks, and valid CDN avatars.
2. **Observation 1.2 shows** that the lorebook entries currently contain stub descriptions (<1,250 chars) and `type: "lore/concept"`, which prevents Wyvern from splitting dialogue headers and assigning character portraits dynamically.
3. **Comparing Observation 1.1 and Observation 1.2 confirms** that injecting the 7 full card descriptions will add 89,576 chars to Primary and 7,240 chars to Secondary.
4. **Because Erik's description alone is 22,775 characters (~4,800 tokens)**, retaining a `token_budget` of 5000 in Primary would risk truncating other active context or Erik's own RPG/intimacy block when Erik activates. Setting `token_budget: 7500` on `FINAL/Svartulfr_NPC_Primary.json` provides adequate headroom.
5. **Because the 7 standalone card IDs are already present in `ignored_characters`**, converting these entries to `type: "npc"` and `selective: false` with clean name keys will allow them to activate naturally during third-party interactions (e.g. in SUCC routes or Master Scenario) while being automatically suppressed when the player loads the standalone Character Card.
6. **Setting `custom_avatar_regex: true`, `lines_parsed: 1`, and multiline regex patterns** `(?:^|\n)\s*(?:...)\s*:` with structured `npc_info` aligns these 7 core entries with the reference patterns of Jasper (`Vcj4h2TL4Usola2A4OOl6`), Alyssa (`alyssa_world_dossier_2b54a223`), Scarlett, Sierra, and Hugh Rivers.
7. **Both `entries` and `lexicon` arrays must receive the update** in each lorebook file to preserve data integrity and prevent schema synchronization mismatches.

---

## 3. Caveats

- **Scope boundary:** This investigation was strictly read-only. No files in `FINAL/` were modified.
- **Other 303 Lorebook entries:** Requirement R2 (layout homogenization across all 310 entries) and R3 (official DCC placeholder avatar on entries lacking portraits) are distinct steps handled by subsequent worker tasks. This report specifically focuses on Requirement R1 (the 7 core character cards and target entries).
- **Secondary Keys:** When converting to `selective: false`, existing secondary keys (such as `['Ghost', 'King']` on Malachia or `['DCC', 'Villa Douglas']` on Erik) should be cleared (`secondary_keys: []`) to prevent unintentional keyword overlap and respect Rule 8.

---

## 4. Conclusion

1. All 7 standalone character card files in `FINAL/` are valid, complete, and fully formatted according to JED+ guidelines without any syntax or rule defects.
2. The target entry IDs for all 7 characters are verified and located in `FINAL/Svartulfr_NPC_Primary.json` (6 records) and `FINAL/Svartulfr_NPC_Secondary.json` (1 record).
3. The standalone Card IDs are already populated in `ignored_characters` on all 7 target records.
4. The remediation plan in `analysis.md` provides exact, drop-in replacement specifications:
   - Convert `type` to `"npc"`
   - Set `selective: false`, `constant: false`, `exclude_from_recursion: true`
   - Populate `custom_avatar_regex: true`, multiline regex `(?:^|\n)\s*(?:...)\s*:`, `lines_parsed: 1`
   - Populate structured `npc_info` (`first_name`, `last_name`, `nicknames`, `titles`)
   - Replace content with full card descriptions (89,576 chars in Primary, 7,240 in Secondary)
   - Synchronize avatars to match canonical card CDN URLs
   - Update `token_budget` to `7500` in Primary and keep `5000` in Secondary
   - Apply updates to both `entries` and `lexicon` arrays.

---

## 5. Verification Method

To independently verify all findings in this report, execute the following commands in PowerShell from repository root:

```powershell
# 1. Verify card character counts, IDs, avatars, and 0 formatting errors:
python scratch/inspect_r7_cards.py
python scratch/check_card_formatting.py

# 2. Verify target records and ignored_characters in Primary and Secondary lorebooks:
python scratch/inspect_targets.py

# 3. Verify synchronization between entries and lexicon:
python scratch/check_entries_lexicon_targets.py
```

### Invalidation Conditions:
- Any mismatch between card IDs in `FINAL/` and `ignored_characters` in the lorebooks.
- Any em-dash (`—`), asterisk, or `{{age}}` macro found in the source card descriptions.
- Primary lorebook remaining at `token_budget: 5000` instead of `7500`.
