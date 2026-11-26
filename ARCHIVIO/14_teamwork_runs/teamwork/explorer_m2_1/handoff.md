# Handoff Report: Milestone 2 Explorer — Svartúlfr NPC Primary Lorebook Analysis

**Agent ID**: `explorer_m2_1`  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m2_1`  
**Parent Agent**: `c8a5c469-63a4-4154-bc85-fe2572ebf1e1` (Orchestrator M2)  
**Target File**: `FINAL/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`, 99 entries)  
**Verifier Script**: `scripts/verify_npc_schema_contract.py`  
**Status**: Exploration & Synthesis Complete (Read-Only)

---

## 1. Observation

### 1.1 Root Structure & Gallery Contract
Inspecting `FINAL/Svartulfr_NPC_Primary.json` vs `FINAL/Svartulfr_NPC_Secondary.json`:
- `FINAL/Svartulfr_NPC_Primary.json` top-level keys:
  `['name', 'description', 'scan_depth', 'token_budget', 'recursive_scanning', 'entries', 'lexicon', 'visibility', 'rating', 'photoURL', 'id']`
  *Direct Observation*: `gallery` and `gallery_count` are completely absent at the root level of `FINAL/Svartulfr_NPC_Primary.json` (and mirror `lorebooks/optimized/Svartulfr_NPC_Primary.json`).
- `FINAL/Svartulfr_NPC_Secondary.json` top-level keys:
  Includes `"gallery": []` and `"gallery_count": 0`.
- Verifier execution (`python scripts/verify_npc_schema_contract.py --check-files`):
  ```text
  Audit Report for: FINAL\Svartulfr_NPC_Primary.json
    Total Entries in Lexicon: 99
    Root Gallery Valid: False (Lorebook root missing 'gallery' array property; Lorebook root missing 'gallery_count' property)
    Entries == Lexicon Parity: True (OK)
    NPC Entries Checked: 99
    Valid Avatars: 99/99
    Valid npc_info: 0/99
    Legacy Duplicate Surname Defects in regex: 10
  ```

### 1.2 Legacy Duplicate Surname Concatenations in `avatar_activation_regex`
Programmatic regex audit using `detect_duplicate_surnames()` identified exactly **10 entries** exhibiting duplicate surname concatenations resulting from legacy string formatting heuristics (e.g., appending `<Surname>` to an alias or title that already included the surname):

1. **[Index 00] `Hugh Rivers`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Hugh\ Rivers|Alpha\ Rivers\ Rivers|Alpha\ Rivers|The\ Mountain\ Sovereign\ Rivers|The\ Mountain\ Sovereign|Hugh)\s*:`
   - *Defects*: `Alpha Rivers Rivers`, `The Mountain Sovereign Rivers`
   - *Root Cause*: Appending `Rivers` to `Alpha Rivers` and `The Mountain Sovereign`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Hugh\ Rivers|Alpha\ Rivers|The\ Mountain\ Sovereign|Hugh)\s*:`

2. **[Index 10] `Dominic Rogers`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Dominic\ Rogers|Dom\ Rogers|Dom|Mr\.\ Rogers\ Rogers|Mr\.\ Rogers|Dominic)\s*:`
   - *Defects*: `Mr. Rogers Rogers`
   - *Root Cause*: Appending `Rogers` to `Mr. Rogers`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Dominic\ Rogers|Dom\ Rogers|Dom|Mr\.\ Rogers|Dominic)\s*:`

3. **[Index 25] `Daniel "Danny" Boone`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Daniel\ "Danny"\ Boone|Daniel\ Boone|Danny\ Boone|Danny|Boone\ Boone|Boone|Daniel)\s*:`
   - *Defects*: `Boone Boone`
   - *Root Cause*: Doubling bare token `Boone`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Daniel\ "Danny"\ Boone|Daniel\ Boone|Danny\ Boone|Danny|Boone|Daniel)\s*:`

4. **[Index 28] `Harrison Black`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Harrison\ Black|Harry\ Black|Harry|Councilman\ Black\ Black|Councilman\ Black|Harrison)\s*:`
   - *Defects*: `Councilman Black Black`
   - *Root Cause*: Appending `Black` to `Councilman Black`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Harrison\ Black|Harry\ Black|Harry|Councilman\ Black|Harrison)\s*:`

5. **[Index 52] `Marcus O'Connor`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Marcus\ O'Connor|Mark\ O'Connor\ O'Connor|Mark\ O'Connor|Oldtown\ O'Connor|Oldtown|Marcus)\s*:`
   - *Defects*: `Mark O'Connor O'Connor`
   - *Root Cause*: Appending `O'Connor` to `Mark O'Connor`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Marcus\ O'Connor|Mark\ O'Connor|Oldtown|Marcus)\s*:`

6. **[Index 66] `Helena Weiss`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Helena\ Weiss|Professor\ Weiss\ Weiss|Professor\ Weiss|Arcadia\ Weiss|Arcadia|Helena)\s*:`
   - *Defects*: `Professor Weiss Weiss`
   - *Root Cause*: Appending `Weiss` to `Professor Weiss`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Helena\ Weiss|Professor\ Weiss|Arcadia|Helena)\s*:`

7. **[Index 68] `Harlan Beaumont`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Harlan\ Beaumont|Huck\ Beaumont\ Beaumont|Huck\ Beaumont|Huck|Harlan)\s*:`
   - *Defects*: `Huck Beaumont Beaumont`
   - *Root Cause*: Appending `Beaumont` to `Huck Beaumont`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Harlan\ Beaumont|Huck\ Beaumont|Huck|Harlan)\s*:`

8. **[Index 73] `Federico "Riki" Savini`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Federico\ "Riki"\ Savini|Federico\ Savini|Riki\ Savini|Riki|Federico\ Savini\ Savini|Federico)\s*:`
   - *Defects*: `Federico Savini Savini`
   - *Root Cause*: Appending `Savini` to `Federico Savini`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Federico\ "Riki"\ Savini|Federico\ Savini|Riki\ Savini|Riki|Federico)\s*:`

9. **[Index 75] `Eris Davies`**:
   - *Verbatim Regex*: `(?:^|\n)\s*(?:Eris\ Davies|Stan's\ Mom\ Davies|Stan's\ Mom|ms\ davies\ Davies|ms\ davies|Eris)\s*:`
   - *Defects*: `ms davies Davies`, `Stan's Mom Davies`
   - *Root Cause*: Appending `Davies` to `ms davies` and `Stan's Mom`.
   - *Remediated Pattern*: `(?:^|\n)\s*(?:Eris\ Davies|Stan's\ Mom|ms\ davies|Mrs\.\ Davies|Eris)\s*:`

10. **[Index 77] `Elizabeth Duskwood`**:
    - *Verbatim Regex*: `(?:^|\n)\s*(?:Elizabeth\ Duskwood|Lady\ Duskwood\ Duskwood|Lady\ Duskwood|nonna\ Duskwood|nonna|Elizabeth)\s*:`
    - *Defects*: `Lady Duskwood Duskwood`, `nonna Duskwood`
    - *Root Cause*: Appending `Duskwood` to `Lady Duskwood` and `nonna`.
    - *Remediated Pattern*: `(?:^|\n)\s*(?:Elizabeth\ Duskwood|Lady\ Duskwood|nonna|Elizabeth)\s*:`

### 1.3 Anti-Collision & Persona Suppression State
Auditing the existing 99 entries in `FINAL/Svartulfr_NPC_Primary.json`:
- **`ignored_characters`**: Populated on exactly **13 entries**:
  1. `[17] Scarlett Rose`: `["_qXgBMbFYJfc84hbLHhe92"]` (Retired Card ID)
  2. `[18] Sierra Cruz`: `["_pnrXbkWqcgmFAf3meRWFY"]` (Retired Card ID)
  3. `[24] Russell 'Russ' Sinclair`: `["_wn6DkCcg3Xqa2Xpx9ttnT"]` (Retired Card ID)
  4. `[32] Wulfnic Báleygr Bloodmoon`: `["_HEQQbbRFwKdG8QE2Fh1z1"]` (Active Card ID)
  5. `[41] Stanley Davies Jr.`: `["_Xd3NhKnRJByMTtdb6PjxJ"]` (Retired Card ID)
  6. `[47] Noah Loki Douglas Bloodmoon`: `["_zFLUjV8aVxQRAfQxGcAcY"]` (Active Card ID)
  7. `[53] Malachia Björn Douglas Bloodmoon`: `["_RDfz7XzTpM23LpPALVXHM"]` (Active Card ID)
  8. `[55] Mackenzie Sanchez-Rogers`: `["_zn24784jfcchQ7EwCyAnm"]` (Active Card ID)
  9. `[57] Logan Járn Douglas`: `["_T8Ywcr9FEqNf9JxbK6eHP"]` (Active Card ID)
  10. `[60] Jasper Svartr Douglas Bloodmoon`: `["_t4J9aQNJM36cUKAP4wB4U"]` (Active Card ID)
  11. `[62] Jared Thompson`: `["_xJVPtBLL3dxy69RLKL9X9"]` (Retired Card ID)
  12. `[76] Erik Ulfr Douglas`: `["_QPea6g4Q1QfeYCVHCLMPR"]` (Active Card ID)
  13. `[98] Alyssa Hvit Douglas Bloodmoon`: `["_6exg3yPfe2eCDK4hTftkh"]` (Legacy Card ID)
- **`ignored_personas`**: Populated on exactly **2 entries**:
  - `[60] Jasper Svartr Douglas Bloodmoon`: `["1792155173728"]`
  - `[98] Alyssa Hvit Douglas Bloodmoon`: `["persona_1786335754946"]`
- **`selective` and `secondary_keys`**:
  - Current state in file: `selective: False`, `secondary_keys: []` on all 99 entries.
  - Required Milestone 2 target state per project directives:
    - `[60] Jasper Svartr Douglas Bloodmoon`: `selective: true`, `secondary_keys: ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]`, `key_logic: "AND_ANY"`.
    - `[98] Alyssa Hvit Douglas Bloodmoon`: `selective: true`, `secondary_keys: ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]`, `key_logic: "AND_ANY"`.
    - Remaining 97 entries: `selective: false`, `secondary_keys: []`.

### 1.4 Baseline `npc_info` Defect State
Across all 99 entries in `FINAL/Svartulfr_NPC_Primary.json`:
- `first_name`: present on 99/99 entries (though 4 entries had parse defects, e.g. entry [45] `Professor Loewe` had `first_name: "Loewe"`, entry [56] `Lord Cornelius Douglas` had `first_name: "Lord"`, entries [70]/[71]/[79] had `first_name: "GREED"`, `"GLUTTONY"`, `"ENVY"`).
- `middle_names`: **0/99 entries** currently contain `middle_names`. It is completely missing, causing `validate_npc_info_schema()` to fail on 100% of entries.
- `npc_prefix`: **0/99 entries** contain `npc_prefix` (defaults to `""`).
- `titles`: Only 2/99 entries had titles in `npc_info` (`Professor Loewe`, `Dr. Arthur Sinclair`).

---

## 2. Logic Chain

1. **From Schema Contract to Field Requirements**:
   - `scripts/verify_npc_schema_contract.py` defines the canonical Wyvern frontend contract:
     ```python
     "npc_info": {
         "first_name": str,             # non-empty
         "middle_names": List[str],     # mandatory key, list of strings (can be empty)
         "last_name": Optional[str],    # string or None
         "nicknames": List[str],        # list of strings
         "titles": List[str],           # list of strings
         "npc_prefix": Optional[str]    # string or None ("")
     }
     ```
   - Because `middle_names` is required by the validator on every entry, omitting it fails validation for all entries. Therefore, every single entry in `FINAL/Svartulfr_NPC_Primary.json` must be updated with `middle_names: []` (or populated with extracted middle names) and `npc_prefix: ""`.

2. **From JED+ Headers to Extracted Middle Names (13 Entries)**:
   - Deep inspection of JED+ bracket headers `[NAME: ...; MIDDLE_NAME: ...]` and Character Card headers revealed 13 characters possessing verified middle names:
     * `[10] Dominic Rogers`: `Dominic Wayne Rogers` -> `middle_names: ["Wayne"]`
     * `[32] Wulfnic Báleygr Bloodmoon`: `Wulfnic Báleygr Bloodmoon` -> `middle_names: ["Báleygr"]`
     * `[44] Roland Vickers`: `Roland Mark Vickers` -> `middle_names: ["Mark"]`
     * `[47] Noah Loki Douglas Bloodmoon`: `Noah Loki Douglas Bloodmoon` -> `middle_names: ["Loki"]`
     * `[48] Nixara Hvit Bloodmoon`: `Nixara Hvit Bloodmoon` -> `middle_names: ["Hvit"]`
     * `[51] Marcus Thornfield`: `Marcus Iron Thornfield` -> `middle_names: ["Iron"]`
     * `[53] Malachia Björn Douglas Bloodmoon`: `Malachia Björn Douglas Bloodmoon` -> `middle_names: ["Björn"]`
     * `[57] Logan Járn Douglas`: `Logan Dominic Járn Douglas` -> `middle_names: ["Dominic", "Járn"]` (Civil + Wolf Name)
     * `[58] Kaladin Nargathon`: `Kaladin Blackwolf Nargathon` -> `middle_names: ["Blackwolf"]`
     * `[60] Jasper Svartr Douglas Bloodmoon`: `Jasper Svartr Douglas Bloodmoon` -> `middle_names: ["Svartr"]`
     * `[65] Iordan R. Vess`: `Iordan R. Vess` -> `middle_names: ["R."]`
     * `[76] Erik Ulfr Douglas`: `Erik Ulfr Douglas` -> `middle_names: ["Cornelius", "Ulfr"]` (Civil + Wolf Name)
     * `[98] Alyssa Hvit Douglas Bloodmoon`: `Alyssa Hvit Douglas Bloodmoon` -> `middle_names: ["Hvit"]`

3. **From JED+ Headers and Lore to Canonical Titles (22 Entries)**:
   - Analysis of titles across the 99 entries identified:
     * `[00] Hugh Rivers`: `titles: ["Alpha"]`
     * `[10] Dominic Rogers`: `titles: ["Mr."]`
     * `[16] Bryson`: `titles: ["Chief"]`
     * `[20] Karshin Darkfire`: `titles: ["Chief"]`
     * `[28] Harrison Black`: `titles: ["Councilman"]`
     * `[32] Wulfnic Báleygr Bloodmoon`: `titles: ["Jarl", "Alpha"]`
     * `[40] Stanley Davies Sr.`: `titles: ["Mr."]`
     * `[45] Professor Loewe` (`Richard Loewe`): `titles: ["Professor"]`
     * `[53] Malachia Björn Douglas Bloodmoon`: `titles: ["Alpha"]`
     * `[54] Magnus Douglas III`: `titles: ["III", "Sir"]`
     * `[56] Lord Cornelius Douglas` (`Cornelius Douglas`): `titles: ["Lord"]`
     * `[58] Kaladin Nargathon`: `titles: ["Commander"]`
     * `[65] Iordan R. Vess`: `titles: ["Alpha"]`
     * `[66] Helena Weiss`: `titles: ["Professor"]`
     * `[69] Hank Thompson`: `titles: ["Coach"]`
     * `[75] Eris Davies`: `titles: ["Mrs.", "Ms."]`
     * `[76] Erik Ulfr Douglas`: `titles: ["Alpha", "Lord"]`
     * `[77] Elizabeth Duskwood`: `titles: ["Lady"]`
     * `[80] Dullahan`: `titles: ["Coach"]`
     * `[81] Dr. Arthur Sinclair` (`Arthur Sinclair`): `titles: ["Dr."]`
     * `[91] Barkley Rover`: `titles: ["Coach"]`
     * `[94] Archer Wolfwood`: `titles: ["Chancellor"]`

4. **From Heuristic Flaws to Clean Name Components**:
   - Several entries previously had titles or sins hardcoded into `first_name`:
     * Entry [45]: was `first_name: "Loewe"`, `last_name: ""`. Fixed: `first_name: "Richard"`, `last_name: "Loewe"`, `titles: ["Professor"]`.
     * Entry [56]: was `first_name: "Lord"`, `last_name: "Douglas"`. Fixed: `first_name: "Cornelius"`, `last_name: "Douglas"`, `titles: ["Lord"]`.
     * Entry [70]: was `first_name: "GREED"`, `last_name: "Roxie"`. Fixed: `first_name: "Roxie"`, `last_name: None`, `nicknames: ["Greed", "Rox"]`.
     * Entry [71]: was `first_name: "GLUTTONY"`, `last_name: "Kevin"`. Fixed: `first_name: "Kevin"`, `last_name: None`, `nicknames: ["Gluttony"]`.
     * Entry [74]: was `first_name: "Fade"`, `last_name: "Greymoor"`. Fixed: `first_name: "Mihaela"`, `last_name: "Greymoor"`, `nicknames: ["Fade"]`.
     * Entry [79]: was `first_name: "ENVY"`, `last_name: "Siobhan"`. Fixed: `first_name: "Siobhan"`, `last_name: None`, `nicknames: ["Envy"]`.
     * Entry [81]: was `first_name: "Arthur"`, `last_name: "Sinclair"`, `titles: ["Dr."]`. (Maintained correctly).

5. **From Legacy Regex Defects to Native Compilation**:
   - The 10 entries with duplicate surnames had hardcoded regex strings with doubled words.
   - When compiled cleanly using Module 93312 (`compile_wyvern_avatar_regex`), or cleaned in the manual regex string, 0 duplicate surname defects occur (tested via `scratch/test_compiled_primary_regex.py` -> 0/99 defects).

---

## 3. Comprehensive Master Catalog of All 99 Primary Entries

Below is the authoritative, verified specification for all 99 entries in `FINAL/Svartulfr_NPC_Primary.json`:

| Index | Entry Name | `first_name` | `middle_names` | `last_name` | `titles` | `nicknames` (Cleaned) | Notes / Special Protections |
|---|---|---|---|---|---|---|---|
| **00** | Hugh Rivers | Hugh | `[]` | Rivers | `["Alpha"]` | `["The Mountain Sovereign"]` | Legacy regex fixed (`Rivers Rivers` removed) |
| **01** | Liam O’Connor | Liam | `[]` | O'Connor | `[]` | `["Liam"]` | |
| **02** | Bessie May | Bessie | `[]` | May | `[]` | `["Bessie"]` | |
| **03** | Neve | Neve | `[]` | `null` | `[]` | `["The Archivist"]` | |
| **04** | Jaelyn | Jaelyn | `[]` | `null` | `[]` | `["Jae"]` | |
| **05** | Marek | Marek | `[]` | `null` | `[]` | `["The Iron Hammer", "Blue Devil", "Blue Oni"]` | |
| **06** | Kian | Kian | `[]` | `null` | `[]` | `["The Ghost Feather", "Shadow Scout"]` | |
| **07** | Goran | Goran | `[]` | `null` | `[]` | `["The Iron Ram", "Team Ukiyo Tank"]` | |
| **08** | Radek | Radek | `[]` | `null` | `[]` | `["The Tactician", "Squad Leader"]` | |
| **09** | Echo | Echo | `[]` | `null` | `[]` | `["E.C.H.O.", "familiar", "Jasper AI", "cyber familiar"]` | |
| **10** | Dominic Rogers | Dominic | `["Wayne"]` | Rogers | `["Mr."]` | `["Dom", "Bailey's Dad"]` | Legacy regex fixed (`Rogers Rogers` removed) |
| **11** | Roman Blackwood | Roman | `[]` | Blackwood | `[]` | `[]` | Single pair of wolf ears (demi-human) |
| **12** | Eric | Eric | `[]` | `null` | `[]` | `[]` | |
| **13** | Javier Reyes | Javier | `[]` | Reyes | `[]` | `["Javi"]` | |
| **14** | Raymond | Raymond | `[]` | `null` | `[]` | `["Ray"]` | |
| **15** | Dean | Dean | `[]` | `null` | `[]` | `[]` | |
| **16** | Bryson | Bryson | `[]` | `null` | `["Chief"]` | `["Chief Researcher", "MF Inc."]` | |
| **17** | Scarlett Rose | Scarlett | `[]` | Rose | `[]` | `["Red"]` | `ignored_characters: ["_qXgBMbFYJfc84hbLHhe92"]` |
| **18** | Sierra Cruz | Sierra | `[]` | Cruz | `[]` | `[]` | `ignored_characters: ["_pnrXbkWqcgmFAf3meRWFY"]` |
| **19** | Varg Darkfire | Varg | `[]` | Darkfire | `[]` | `["The Patriarch", "The Old King", "Il Patriarca", "Vecchio Re"]` | |
| **20** | Karshin Darkfire | Karshin | `[]` | Darkfire | `["Chief"]` | `["The Mastiff", "Chief of Security for HSK Consulting", "Il Mastino"]` | |
| **21** | Boros Darkfire | Boros | `[]` | Darkfire | `[]` | `["The Bastion", "Logistics Director of HSK Consulting", "Il Bastione"]` | |
| **22** | Aras Darkfire | Aras | `[]` | Darkfire | `[]` | `["The Whisper", "HR Director of HSK Consulting", "Il Sussurro"]` | |
| **23** | Kolya Varenkov | Kolya | `[]` | Varenkov | `[]` | `[]` | |
| **24** | Russell 'Russ' Sinclair | Russell | `[]` | Sinclair | `[]` | `["Russ"]` | `ignored_characters: ["_wn6DkCcg3Xqa2Xpx9ttnT"]` |
| **25** | Daniel "Danny" Boone | Daniel | `[]` | Boone | `[]` | `["Danny"]` | Legacy regex fixed (`Boone Boone` removed) |
| **26** | Marlowe Voss | Marlowe | `[]` | Voss | `[]` | `[]` | |
| **27** | Cassian Aralas | Cassian | `[]` | Aralas | `[]` | `[]` | |
| **28** | Harrison Black | Harrison | `[]` | Black | `["Councilman"]` | `["Harry"]` | Legacy regex fixed (`Black Black` removed) |
| **29** | Zero | Zero | `[]` | `null` | `[]` | `["Wrath"]` | Cleaned derogatory broad terms |
| **30** | Zefir Hvitskog | Zefir | `[]` | Hvitskog | `[]` | `["White Ghost", "Firstborn"]` | Age 1176 (turned at 16 in 864 AD) |
| **31** | Zeera Darkfire | Zeera | `[]` | Darkfire | `[]` | `["CEO of HSK Consulting", "Demonic Representative", "Horned Skull Clan Leader"]` | |
| **32** | Wulfnic Báleygr Bloodmoon | Wulfnic | `["Báleygr"]` | Bloodmoon | `["Jarl", "Alpha"]` | `["The First Tusk", "Primo Zanna", "The Ancient", "Alpha of Alphas"]` | `ignored_characters: ["_HEQQbbRFwKdG8QE2Fh1z1"]` |
| **33** | Vito Marino | Vito | `[]` | Marino | `[]` | `["Scar", "Ironworks Syndicate"]` | |
| **34** | Viola Carter | Viola | `[]` | Carter | `[]` | `["Via"]` | |
| **35** | Vincent Campbell | Vincent | `[]` | Campbell | `[]` | `["Vince", "Vi", "Ace"]` | |
| **36** | Ut Berg | Ut | `[]` | Berg | `[]` | `["The Mountain", "Út Fjallit", "Firstborn"]` | Age 1205 (turned at 45 in 864 AD) |
| **37** | Tomas Matthews | Tomas | `[]` | Matthews | `[]` | `[]` | |
| **38** | Tate | Tate | `[]` | `null` | `[]` | `["Subject 36"]` | Mononym |
| **39** | Sullivan "Sully" Jones | Sullivan | `[]` | Jones | `[]` | `["Sully"]` | |
| **40** | Stanley Davies Sr. | Stanley | `[]` | Davies | `["Mr."]` | `["Stanley Davies Sr."]`, Suffix: Sr. | |
| **41** | Stanley Davies Jr. | Stanley | `[]` | Davies | `[]` | `["Stan", "Stanley Davies Jr."]`, Suffix: Jr. | `ignored_characters: ["_Xd3NhKnRJByMTtdb6PjxJ"]` |
| **42** | Santiago Herrera | Santiago | `[]` | Herrera | `[]` | `["Santi", "Tank"]` | |
| **43** | Ruaraidh "Rory" Ballantine | Ruaraidh | `[]` | Ballantine | `[]` | `["Rory"]` | |
| **44** | Roland Vickers | Roland | `["Mark"]` | Vickers | `[]` | `[]` | Middle name Mark from JED+ |
| **45** | Professor Loewe | Richard | `[]` | Loewe | `["Professor"]` | `["Loewe"]` | Corrected first/last from JED+ |
| **46** | Oskar | Oskar | `[]` | `null` | `[]` | `["Ozzie", "Squidface"]` | Mononym |
| **47** | Noah Loki Douglas Bloodmoon | Noah | `["Loki"]` | Douglas Bloodmoon | `[]` | `["The Grey Eminence", "Golden Boy"]` | `ignored_characters: ["_zFLUjV8aVxQRAfQxGcAcY"]` |
| **48** | Nixara Hvit Bloodmoon | Nixara | `["Hvit"]` | Bloodmoon | `[]` | `["White Moon", "Pack Mom", "Whitemoon"]` | Middle name Hvit from JED+ |
| **49** | Nikolaj Jökull | Nikolaj | `[]` | Jökull | `[]` | `["Jokull", "eel", "marksman"]` | |
| **50** | Naomi Black | Naomi | `[]` | Black | `[]` | `["Uptown North"]` | |
| **51** | Marcus Thornfield | Marcus | `["Iron"]` | Thornfield | `[]` | `["Field Lead Marcus"]` | Middle name Iron from JED+ |
| **52** | Marcus O'Connor | Marcus | `[]` | O'Connor | `[]` | `["Mark", "Oldtown"]` | Legacy regex fixed (`O'Connor O'Connor` removed) |
| **53** | Malachia Björn Douglas Bloodmoon | Malachia | `["Björn"]` | Douglas Bloodmoon | `["Alpha"]` | `["The Berserker", "Ghost", "The King"]` | `ignored_characters: ["_RDfz7XzTpM23LpPALVXHM"]` |
| **54** | Magnus Douglas III | Magnus | `[]` | Douglas | `["III", "Sir"]` | `["Patriarch Magnus"]` | Suffix III |
| **55** | Mackenzie Sanchez-Rogers | Mackenzie | `[]` | Sanchez-Rogers | `[]` | `["Mac"]` | `ignored_characters: ["_zn24784jfcchQ7EwCyAnm"]` |
| **56** | Lord Cornelius Douglas | Cornelius | `[]` | Douglas | `["Lord"]` | `[]` | Corrected first name from JED+ |
| **57** | Logan Járn Douglas | Logan | `["Dominic", "Járn"]` | Douglas | `[]` | `["Uncle Logan", "The Peacemaker"]` | `ignored_characters: ["_T8Ywcr9FEqNf9JxbK6eHP"]` |
| **58** | Kaladin Nargathon | Kaladin | `["Blackwolf"]` | Nargathon | `["Commander"]` | `["Kal", "Subject Zero"]` | Middle name Blackwolf from JED+ |
| **59** | Jean-Luc Virtuoso | Jean-Luc | `[]` | Virtuoso | `[]` | `["Jean", "The Maestro"]` | Human Telepath |
| **60** | Jasper Svartr Douglas Bloodmoon | Jasper | `["Svartr"]` | Douglas Bloodmoon | `[]` | `["DJ Frequency", "Shadow Wolf", "Jasp"]` | `ignored_characters: ["_t4J9aQNJM36cUKAP4wB4U"]`, `ignored_personas: ["1792155173728"]`, `selective: true` |
| **61** | Jasmin Thompson | Jasmin | `[]` | Thompson | `[]` | `["Jas"]` | |
| **62** | Jared Thompson | Jared | `[]` | Thompson | `[]` | `["J-Man", "The Golden Bull"]` | `ignored_characters: ["_xJVPtBLL3dxy69RLKL9X9"]` |
| **63** | Janice Thompson | Janice | `[]` | Thompson | `[]` | `[]` | |
| **64** | Isobel Blackwater | Isobel | `[]` | Blackwater | `[]` | `["Dockside"]` | |
| **65** | Iordan R. Vess | Iordan | `["R."]` | Vess | `["Alpha"]` | `["Io"]` | Middle initial R. from JED+ |
| **66** | Helena Weiss | Helena | `[]` | Weiss | `["Professor"]` | `["Arcadia"]` | Legacy regex fixed (`Weiss Weiss` removed) |
| **67** | Harper Aries | Harper | `[]` | Aries | `[]` | `["Harp"]` | |
| **68** | Harlan Beaumont | Harlan | `[]` | Beaumont | `[]` | `["Huck"]` | Legacy regex fixed (`Beaumont Beaumont` removed) |
| **69** | Hank Thompson | Hank | `[]` | Thompson | `["Coach"]` | `[]` | Universally Coach Thompson |
| **70** | GREED - Roxie | Roxie | `[]` | `null` | `[]` | `["Greed", "Rox"]` | Mononym, Sinners code name |
| **71** | GLUTTONY - Kevin | Kevin | `[]` | `null` | `[]` | `["Gluttony"]` | Mononym, Sinners code name |
| **72** | Finnegan Novak | Finnegan | `[]` | Novak | `[]` | `["Finn"]` | Arctic Wolf demi-human |
| **73** | Federico "Riki" Savini | Federico | `[]` | Savini | `[]` | `["Riki"]` | Legacy regex fixed (`Savini Savini` removed) |
| **74** | Fade Greymoor | Mihaela | `[]` | Greymoor | `[]` | `["Fade"]` | True name Mihaela from JED+ |
| **75** | Eris Davies | Eris | `[]` | Davies | `["Mrs.", "Ms."]` | `["Stan's Mom"]` | Legacy regex fixed (`davies davies` removed) |
| **76** | Erik Ulfr Douglas | Erik | `["Cornelius", "Ulfr"]` | Douglas | `["Alpha", "Lord"]` | `["The Prime Alpha", "The Patriarch"]` | `ignored_characters: ["_QPea6g4Q1QfeYCVHCLMPR"]` |
| **77** | Elizabeth Duskwood | Elizabeth | `[]` | Duskwood | `["Lady"]` | `["Nonna"]` | Legacy regex fixed (`Duskwood Duskwood` removed) |
| **78** | Eclipse Noir | Eclipse | `[]` | Noir | `[]` | `[]` | |
| **79** | ENVY - Siobhan | Siobhan | `[]` | `null` | `[]` | `["Envy"]` | Mononym, Sinners code name |
| **80** | Dullahan | Dullahan | `[]` | `null` | `["Coach"]` | `["Coach D", "Dully"]` | Mononym |
| **81** | Dr. Arthur Sinclair | Arthur | `[]` | Sinclair | `["Dr."]` | `["Sloth", "The Alchemist"]` | Corrected from JED+ |
| **82** | Dominic Chen | Dominic | `[]` | Chen | `[]` | `[]` | |
| **83** | Darius Vale | Darius | `[]` | Vale | `[]` | `[]` | |
| **84** | Dante | Dante | `[]` | `null` | `[]` | `["Lust"]` | Mononym |
| **85** | Chase Anderson | Chase | `[]` | Anderson | `[]` | `["Goldie"]` | |
| **86** | Cass Harrow | Cass | `[]` | Harrow | `[]` | `[]` | |
| **87** | Casey Williams | Casey | `[]` | Williams | `[]` | `["Case"]` | |
| **88** | Brak Ironfist | Brak | `[]` | Ironfist | `[]` | `["Orc Representative"]` | |
| **89** | Bianca Rossi | Bianca | `[]` | Rossi | `[]` | `["Bia"]` | |
| **90** | Barrow | Barrow | `[]` | `null` | `[]` | `["The Horns"]` | Demi-human representative |
| **91** | Barkley Rover | Barkley | `[]` | Rover | `["Coach"]` | `["Barks", "Coach B"]` | Assistant Coach |
| **92** | Bailey Rogers | Bailey | `[]` | Rogers | `[]` | `["Red"]` | |
| **93** | Aurora Night | Aurora | `[]` | Night | `[]` | `[]` | |
| **94** | Archer Wolfwood | Archer | `[]` | Wolfwood | `["Chancellor"]` | `["Rettore"]` | Chancellor of SUCC |
| **95** | Angelo Moreno | Angelo | `[]` | Moreno | `[]` | `[]` | |
| **96** | Andrew Campbell | Andrew | `[]` | Campbell | `[]` | `["Andy"]` | |
| **97** | Abel Vilas | Abel | `[]` | Vilas | `[]` | `[]` | Cleaned trailing whitespace in name |
| **98** | Alyssa Hvit Douglas Bloodmoon | Alyssa | `["Hvit"]` | Douglas Bloodmoon | `[]` | `["White Moon", "Lyssa", "The Anchor"]` | `ignored_characters: ["_6exg3yPfe2eCDK4hTftkh"]`, `ignored_personas: ["persona_1786335754946"]`, `selective: true` |

---

## 4. Caveats

1. **Read-Only Constraint**: This investigation did not alter any files in `FINAL/`, `lorebooks/optimized/`, or on the live Wyvern API. All findings and proposed schemas were verified against `scripts/verify_npc_schema_contract.py` via simulation scripts in `scratch/`.
2. **Double Surnames for Douglas-Bloodmoon**: For Malachia, Noah, Jasper, and Alyssa, their legal and dynastic surname is `Douglas Bloodmoon`. Setting `last_name: "Douglas Bloodmoon"` correctly compiles in Wyvern's Module 93312 while preserving their wolf names (`Björn`, `Loki`, `Svartr`, `Hvit`) in `middle_names`.
3. **Double Middle Names for Erik and Logan**: Both Erik and Logan have two canonical middle names recorded in their Character Card headers: Erik has `["Cornelius", "Ulfr"]` (Civil + Wolf Name) and Logan has `["Dominic", "Járn"]` (Civil Nobility + Wolf Name). In `npc_info.middle_names`, both can either be represented as `["Cornelius", "Ulfr"]` and `["Dominic", "Járn"]`, or as single wolf names `["Ulfr"]` and `["Járn"]`. Both variants pass `validate_npc_info_schema()` with 100% compliance.
4. **Wyvern PUT Payload Discipline**: When Milestone 2 deploys `FINAL/Svartulfr_NPC_Primary.json` to `PUT /api/lorebooks/_zwEqgEEzh12X6gHVmMKKC`, only `lexicon` and top-level metadata must be transmitted in the HTTP request body (omitting the redundant `entries` array) to avoid HTTP 413 Payload Too Large errors, while maintaining exact byte-for-byte parity between `entries` and `lexicon` in local storage.

---

## 5. Conclusion

1. **Root Gallery Remediation**: `FINAL/Svartulfr_NPC_Primary.json` and `lorebooks/optimized/Svartulfr_NPC_Primary.json` must have `"gallery": []` and `"gallery_count": 0` added at root level.
2. **`npc_info` Sanitation**: All 99 entries in `FINAL/Svartulfr_NPC_Primary.json` must be updated with the canonical schema `{ first_name, middle_names, last_name, nicknames, titles, npc_prefix }`. This immediately brings `valid npc_info` from 0/99 to 99/99.
3. **Regex Duplicate Surname Remediation**: The 10 entries with concatenated duplicate surnames must be replaced with clean regex patterns, eliminating 100% of the defects identified by `detect_duplicate_surnames()`.
4. **Anti-Collision Configuration**:
   - Preserve `ignored_characters` on the 13 entries.
   - Preserve `ignored_personas` on Jasper (`1792155173728`) and Alyssa (`persona_1786335754946`).
   - Set `selective: true` with `secondary_keys: ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]` and `key_logic: "AND_ANY"` strictly on Jasper and Alyssa; maintain `selective: false` and `secondary_keys: []` on all remaining 97 entries.
5. **Parity**: Sychronize updated `lexicon` into `entries` byte-for-byte before saving to `FINAL/` and mirroring to `lorebooks/optimized/`.

---

## 6. Verification Method

To independently verify all findings and test proposals:

1. **Run Contract Verifier**:
   ```powershell
   python scripts/verify_npc_schema_contract.py --all
   ```
2. **Verify Proposed NPC Catalog**:
   ```powershell
   python scratch/build_canonical_primary_npc_table.py
   python scratch/test_compiled_primary_regex.py
   ```
   *Expected Output*:
   - `Total cataloged: 99. Valid count: 99/99`
   - `Total compiled duplicate defects: 0/99`
3. **Inspect Proposed JSON Output**:
   Inspect `scratch/proposed_primary_npc_info.json` to verify that all 99 entries have valid structures, non-null `middle_names: [...]`, clean titles, and zero broad umbrella terms.
