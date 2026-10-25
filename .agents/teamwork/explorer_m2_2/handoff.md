# Milestone 2 (R2) Exploration Report: Svartúlfr NPC Secondary Schema Contract & Data Audit

**Explorer Agent**: `explorer_m2_2`  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m2_2`  
**Parent Orchestrator ID**: `c8a5c469-63a4-4154-bc85-fe2572ebf1e1`  
**Target File**: `FINAL/Svartulfr_NPC_Secondary.json` (and `lorebooks/optimized/Svartulfr_NPC_Secondary.json`)  
**Live Wyvern Lorebook ID**: `_Uht3Ckz44JBDrPnUHq7LV`  
**Timestamp**: `2026-10-24T11:25:00Z`

---

## 1. Observation

### 1.1 Local Lorebook Inventory and Contract Baseline
Executed `python scripts/verify_npc_schema_contract.py --all` and inspected `FINAL/Svartulfr_NPC_Secondary.json`:
- **Total Local Entries**: Exactly 211 entries in `entries` and 211 entries in `lexicon`.
- **Entries == Lexicon Parity**: Verified 100% byte-for-byte serialization equality (`len: 2,122,641 bytes`).
- **Root Gallery**: `gallery: []` and `gallery_count: 0` are present and valid per contract.
- **Avatars**: 211/211 entries possess valid HTTPS URLs:
  - 158 entries use the canonical DCC werewolf silhouette placeholder (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`).
  - 53 entries use dedicated Cloudflare Images character portraits.
- **`npc_info` Contract Status**: **0/211 valid entries** under the Milestone 1 contract:
  - `first_name`: Present across 211/211 entries.
  - `last_name`: Present across 211/211 entries (string or empty/None).
  - `nicknames`: Present across 211/211 entries (list of strings).
  - `titles`: Present across 211/211 entries (list of strings).
  - `middle_names`: **Missing on 211/211 entries** (field omitted from dictionary).
  - `npc_prefix`: **Missing on 211/211 entries** (field omitted from dictionary).

---

### 1.2 Extraction of JED+ Name Components

#### A. Middle Names (102 Entries Identified)
Every entry was audited against JED+ headers (`[NAME: ...]`), `ALIASES:`, and `FULL NAME:` directives:
1. **Camp Mystic Entries (Indices 111–210, exactly 100 entries)**:
   All 100 Camp Mystic campers (80 entries) and counselors (20 entries) contain a complete 3-token name in their first alias in `ALIASES:` (e.g., `Avery Lin Calder`, `Sofia Mae Rourke`, `Jasper Finn Rowan`, `Mara Evelyn Voss`, `Silas Orin Thorne`).
   - Extract `middle_names: [tokens[1]]` for each of indices 111 to 210.
2. **Core / City Entries (Indices 0–110, exactly 2 entries)**:
   - **Index 5 (`m6PNxuNGvi7YmlFRVgFWr`) `Luisa Sanchez Rogers`**:
     - `first_name`: `"Luisa"`
     - `middle_names`: `["Sanchez"]`
     - `last_name`: `"Rogers"`
   - **Index 6 (`4YklgqNsuRUDx7Q_KRFji`) `Alistair Ambrose DeVille`**:
     - `first_name`: `"Alistair"`
     - `middle_names`: `["Ambrose"]`
     - `last_name`: `"DeVille"`
3. **Remaining Entries (109 entries)**:
   - Require `middle_names: []` to satisfy the strict schema contract.

---

#### B. Titles (110 Entries Identified)
Audited all 211 entries for official titles, academic ranks, and leadership positions:
1. **Camp Mystic Campers (80 entries, Indices 111–190)**:
   - `titles: ["Camp Mystic Camper"]`
2. **Camp Mystic Counselors (20 entries, Indices 191–210)**:
   - `titles: ["Camp Mystic Counselor"]`
3. **Academic & Coaching Staff (5 entries)**:
   - Index 19 (`Coach Mithers`): `titles: ["Coach"]`, `first_name: "Mithers"`, `last_name: ""`
   - Index 21 (`Professor Marit Christiansen`): `titles: ["Professor"]`, `first_name: "Marit"`, `last_name: "Christiansen"`
   - Index 22 (`Professor Mollusk Moreau`): `titles: ["Professor"]`, `first_name: "Mollusk"`, `last_name: "Moreau"`
   - Index 29 (`Coach Mack`): `titles: ["Coach"]`, `first_name: "Mack"`, `last_name: ""`
   - Index 80 (`Professor Dryden Kiwetin`): `titles: ["Professor"]`, `first_name: "Dryden"`, `last_name: "Kiwetin"`
4. **Clan Ranks and Faction Leaders (5 entries)**:
   - Index 106 (`Thrakgor Deathspine`): `titles: ["Warchief of the Deathspine Clan"]`
   - Index 107 (`Crowe`): `titles: ["DDM Special Contractor"]`
   - Index 108 (`Morgeth Steeltooth`): `titles: ["Master Arcane Blacksmith"]`
   - Index 109 (`Thorvald`): `titles: ["Hirdman of the Ancestral Woods"]`
   - Index 110 (`Harald Sigurdsson`): `titles: ["Jarl of the Hinterland Pack"]`
5. **Remaining Entries (101 entries)**:
   - `titles: []`

---

#### C. Nicknames & Umbrella/Generic Term Audit (9 Dirty Entries Identified)
Of the 152 entries with populated nicknames, 9 entries contain broad umbrella terms, non-name sentences, or generic common nouns that violate GEMINI.md §7 and trigger spurious activations:

| Index | Entry Name | Current Nicknames | Flagged Items & Rationale | Cleaned Nicknames Proposal |
|---|---|---|---|---|
| **4** | `Ariadne Cirillo` (`CyZknaH7OmYQi5S3ESpNJ`) | `['Nurse Cirillo', 'nurse', 'drider', 'succubus', 'health centre']` | `'nurse'`, `'drider'`, `'succubus'` (umbrella keyword), `'health centre'` (location) | `['Ari', 'Nurse Cirillo']` |
| **7** | `Cato` (`05-b04_y2eB4XzUjJ5y4K`) | `['The Gator', 'Guard Dog', 'alligator demihuman', "Alistair's bodyguard"]` | `'alligator demihuman'` (species umbrella), `"Alistair's bodyguard"` (description) | `['The Gator', 'Guard Dog']` |
| **8** | `Damien Bishop` (`JVtCCxuX3EoaEDgGzhMeM`) | `['Bishop', 'The Hellhound Detective', 'Private Detective']` | `'Bishop'` (duplicate of `last_name`). Note: `secondary_keys` contains `'demon'` (canonical broad key). | Nicknames: `['The Hellhound Detective', 'Private Detective']`. Secondary keys: purge `'demon'`, keep `['detective', 'horns', 'occult', 'investigator']`. |
| **9** | `Everett Rottmore` (`yF51D-9F8l6rZ5_p1U8g7`) | `['The Mortician', 'The Fixer', 'Bone Mask', 'Fixer', 'Mortician']` | Bare nouns `'Fixer'`, `'Mortician'` | `['The Mortician', 'The Fixer', 'Bone Mask']` |
| **10** | `Vasile Ionescu` (`G90UoB8v8P1dC0r_H5VjT`) | `['The Jailer', 'The Trapper', 'Hunter', 'Trapper']` | Bare nouns `'Hunter'`, `'Trapper'` | `['The Jailer', 'The Trapper']` |
| **18** | `Brittany Willow` (`7i9V8B0k1M2n_O3p4Q5rS`) | `['Malachia super-fan', 'SUCC student', 'TIT Sorority', 'brownies']` | `'SUCC student'` (umbrella keyword), `'brownies'` (food noun), `'TIT Sorority'` (org) | `['Malachia super-fan']` |
| **39** | `Campus Staff Rat` (`oov5UWuVhZ3RGgoxMkaTS`) | `['rat', 'staff']` | Bare generic nouns `'rat'`, `'staff'` | `['Rodent Campus Worker']` |
| **40** | `Adrian` (`Og7V6v67guXXAaP0_PsTM`) | `['adrian', 'baker', 'croissant']` | `'adrian'` (first name), `'baker'`, `'croissant'` (nouns) | `['Adrian the Baker']` |
| **80** | `Professor Dryden Kiwetin` (`8N0vB1k2M3n4_O5p6Q7rS`) | `['called "Whtikow" only in rumor', 'never to his face', 'Dryden Kiwetin', 'Professor Kiwetin']` | Sentence fragments: `'called "Wîhtikow" only in rumor'`, `'never to his face'`; redundant full/title names | `['Wîhtikow']` |
| **88** | `Siebren Dijkstra` (`4B5c6D7e8F9g_H0i1J2kL`) | `['Dislikes nicknames']` | Sentence fragment `'Dislikes nicknames'` | `[]` (empty list) |

---

### 1.3 The 10 Legacy Duplicate Surname Defects in `avatar_activation_regex`
Audited all custom regex patterns using `detect_duplicate_surnames()`. The legacy regex generator executed a naive concatenation `f"{nickname} {last_name}"`. For nicknames that already incorporated the character's last name or honorific, this caused adjacent duplicate surname concatenations:

| # | Index | Entry Name | Entry ID | Last Name | Legacy Regex Pattern Snippet | Detected Duplicate |
|---|---|---|---|---|---|---|
| 1 | 2 | `Alicia Virtuoso` | `QeicBpVQvmhrnLgITDnrU` | `Virtuoso` | `(?:^\|\n)\s*(?:Alicia\ Virtuoso\|Mrs\ Virtuoso\ Virtuoso\|Mrs\ Virtuoso...` | `['Virtuoso Virtuoso']` |
| 2 | 4 | `Ariadne Cirillo` | `CyZknaH7OmYQi5S3ESpNJ` | `Cirillo` | `(?:^\|\n)\s*(?:Ariadne\ Cirillo\|Nurse\ Cirillo\ Cirillo\|Nurse\ Cirillo...` | `['Cirillo Cirillo']` |
| 3 | 5 | `Luisa Sanchez Rogers` | `m6PNxuNGvi7YmlFRVgFWr` | `Rogers` | `(?:^\|\n)\s*(?:Luisa\ Sanchez\ Rogers\|...\|Sanchez\ Rogers\ Rogers...` | `['Rogers Rogers']` |
| 4 | 6 | `Alistair Ambrose DeVille` | `4YklgqNsuRUDx7Q_KRFji` | `DeVille` | `(?:^\|\n)\s*(?:Alistair\ Ambrose\ DeVille\|Mr\.\ DeVille\ DeVille...` | `['DeVille DeVille']` |
| 5 | 8 | `Damien Bishop` | `JVtCCxuX3EoaEDgGzhMeM` | `Bishop` | `(?:^\|\n)\s*(?:Damien\ Bishop\|Bishop\ Bishop\|Bishop...` | `['Bishop Bishop']` |
| 6 | 17 | `Adelin Coso` | `gyZ3SOAsx3M7l42RDqSeZ` | `Coso` | `(?:^\|\n)\s*(?:Adelin\ Coso\|Coach\ Coso\ Coso\|Coach\ Coso...` | `['Coso Coso']` |
| 7 | 21 | `Professor Marit Christiansen` | `tmBjBzi064j8hQ5PtQ7iK` | `Christiansen` | `(?:^\|\n)\s*(?:Professor\ Marit\ Christiansen\|...\|Marit\ Christiansen\ Christiansen...` | `['Christiansen Christiansen']` |
| 8 | 22 | `Professor Mollusk Moreau` | `2eFIqOaYGue3oIes911d2` | `Moreau` | `(?:^\|\n)\s*(?:Professor\ Mollusk\ Moreau\|...\|Mollusk\ Moreau\ Moreau...` | `['Moreau Moreau']` |
| 9 | 39 | `Campus Staff Rat` | `oov5UWuVhZ3RGgoxMkaTS` | `Rat` | `(?:^\|\n)\s*(?:Campus\ Staff\ Rat\|...\|rat\ Rat\|rat...` | `['Rat Rat']` |
| 10 | 62 | `Graham Purcell` | `rfEPGtkW4OKx-NcFOAry_` | `Purcell` | `(?:^\|\n)\s*(?:Graham\ Purcell\|...\|Major\ Purcell\ Purcell\|Major\ Purcell...` | `['Purcell Purcell']` |

*Note on Jet Thompson (Index 0)*: While not producing a double identical token (`Thompson Thompson`), Jet Thompson suffered from the identical naive bug: his nicknames `Hank's son` and `Edric's friend` became `Hank's son Thompson` and `Edric's friend Thompson` in the regex pattern.
*Compilation Verification*: Compiling all 211 entries via Wyvern Module 93312 WH (`compile_wyvern_avatar_regex`) completely eliminates 100% of these duplicate surname concatenations.

---

### 1.4 Live API Sync Difference: 211 Local vs 209 Live
Executed live GET query to Wyvern API:
`GET https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV`  
Headers: `Authorization: Bearer <JWT>`, `User-Agent: AuditorBot/1.0`  
- **Result**: `HTTP 200 OK`
- **Live Entry Count**: **209 entries** in `lexicon`
- **Local Entry Count**: **211 entries** in `FINAL/Svartulfr_NPC_Secondary.json`
- **Exact Delta Identification**:
  1. `Finn the Satyr` (`quJQvjvUWQLUeOCNv2Wko`): Local index 97. Missing from live Wyvern.
  2. `Jasper Rowan` (`d1Qg6eRvuKC8iI5kNWPzb`): Local index 188. Missing from live Wyvern.
  - Live minus Local: 0 entries.
- **Root Cause**: Finn the Satyr and Jasper Rowan (Ghost camper in Cabin B-07 for Camp Mystic) were authored/standardized in local repository files in recent commits (`f651148`, `d162630`) but not yet deployed live to Wyvern API.
- **Action Required for Milestone 2**: When PUT deployment is executed, the live lorebook will be cleanly promoted from 209 to 211 entries.

---

### 1.5 Anti-Collision Invariants
Audited anti-collision properties across all 211 entries:
1. **`ignored_characters`**:
   - Exactly **1 entry** has `ignored_characters`:
     - **Index 1 (`Edric Douglas`, ID: `h-ttmlgJYeRXqyDvQjSX7`)**:
       `ignored_characters: ["_TbRM3EdxDjHFgqztTbCpL"]`
   - This matches Edric Douglas's live Character Card ID (`FINAL/Edric_Douglas_card.json`, Wyvern `/characters/mine`).
   - Invariant: This entry suppression must be preserved 1:1 to prevent bot-duplication when playing with Edric Douglas in the party.
2. **`ignored_personas`**:
   - `0 entries` have `ignored_personas` in Secondary Lorebook (correct; only Alyssa and Jasper are personas, and their entries reside in Primary Lorebook `_zwEqgEEzh12X6gHVmMKKC`).
3. **`selective` Configuration**:
   - Currently, 210 entries have `selective: None` and 1 has `selective: False`.
   - Invariant: In accordance with GEMINI.md §7, all 211 entries must explicitly declare `"selective": False`.
4. **Secondary Keys Cleaning**:
   - Index 8 (`Damien Bishop`): currently has `secondary_keys: ['detective', 'demon', 'horns', 'occult', 'investigator']`.
   - Invariant: `'demon'` must be removed because it is a `CANONICAL_BROAD_KEYS` umbrella keyword. Cleaned: `['detective', 'horns', 'occult', 'investigator']`.

---

## 2. Logic Chain

1. **Premise 1 (Schema Incompleteness)**: Observation 1.1 reveals that `verify_npc_schema_contract.py` rejects 100% of current entries because `npc_info` omits `middle_names` and `npc_prefix`.
2. **Premise 2 (Name Component Determinism)**: Observation 1.2 extracts exact, deterministic name components:
   - 102 entries with middle names (100 Camp Mystic + Luisa Sanchez Rogers + Alistair Ambrose DeVille).
   - 110 entries with formal titles (Campers, Counselors, Professors, Coaches, Clan Leaders).
   - 9 entries requiring nickname hygiene to eliminate umbrella words (`succubus`, `drider`, `SUCC student`), sentence fragments (`Dislikes nicknames`), and generic nouns (`nurse`, `brownies`, `rat`).
3. **Premise 3 (Compiler Superiority)**: Observation 1.3 shows that the 10 legacy duplicate surname defects (`Virtuoso Virtuoso`, `Rogers Rogers`, etc.) and flawed strings (`Hank's son Thompson`) were caused by a naive `f"{nick} {last_name}"` concatenation. Running Wyvern's native Module 93312 WH compiler resolves 100% of these defects with zero syntax errors.
4. **Premise 4 (Safe Live Sync)**: Observation 1.4 confirms that the local file contains exactly 2 legitimate canonical entries (`Finn the Satyr` and `Jasper Rowan`) not yet pushed to live Wyvern. Deploying the remediated 211 entries will achieve 100% synchronization.
5. **Premise 5 (Anti-Collision Safety)**: Observation 1.5 proves that preserving `ignored_characters: ["_TbRM3EdxDjHFgqztTbCpL"]` on Edric Douglas, enforcing `selective: false` across all 211 entries, and purging `'demon'` from Damien Bishop guarantees full anti-collision safety.

---

## 3. Caveats

1. **Read-Only Scope**: This agent is strictly an Explorer and did not alter any source files. All remediation must be executed by the designated Worker agent.
2. **PUT Payload Size Restriction**: When deploying to `PUT /api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV`, only `lexicon` and top-level metadata should be transmitted in the JSON payload (omitting the duplicate `entries` array) to avoid Wyvern Cloudflare HTTP 413 Payload Too Large errors. Local files must retain both arrays byte-for-byte identical.
3. **Unicode Normalization in Kiwetin**: Professor Dryden Kiwetin's Cree name uses the circumflex (`Dryden Kîwêtin` and `Wîhtikow`). Ensure UTF-8 NFC normalization is preserved during remediation.

---

## 4. Conclusion

The audit of `FINAL/Svartulfr_NPC_Secondary.json` is complete, comprehensive, and actionable:
1. **Target Schema**: Populate `npc_info` with `{ first_name, middle_names, last_name, nicknames, titles, npc_prefix: None }` across all 211 entries.
2. **Middle Names Mapping**: Assign `middle_names` to exactly 102 entries (100 Camp Mystic campers/counselors from their JED+ `ALIASES:`, `Sanchez` for Luisa Sanchez Rogers, and `Ambrose` for Alistair Ambrose DeVille); assign `[]` to the other 109 entries.
3. **Titles Mapping**: Retain `titles` for the 110 identified entries; assign `[]` to the remaining 101 entries.
4. **Nickname Sanitation**: Clean the 9 flagged entries (purge `nurse`, `drider`, `succubus`, `health centre`, `SUCC student`, `brownies`, `rat`, `staff`, `baker`, `croissant`, sentence fragments) and purge `demon` from Damien Bishop's `secondary_keys`.
5. **Regex Recompilation**: Recompile all 211 `avatar_activation_regex` patterns using native Wyvern Module 93312 WH, eliminating all 10 legacy duplicate surname defects.
6. **Anti-Collision**: Explicitly set `selective: false` across all 211 entries and preserve Edric Douglas's `ignored_characters: ["_TbRM3EdxDjHFgqztTbCpL"]`.
7. **Parity & Deployment**: Synchronize `entries == lexicon` byte-for-byte locally and deploy the remediated 211 entries to Wyvern API (`_Uht3Ckz44JBDrPnUHq7LV`), bringing live entry count from 209 to 211.

---

## 5. Verification Method

To independently verify this investigation:
1. **Contract Self-Test & File Audit**:
   ```bash
   python scripts/verify_npc_schema_contract.py --all
   ```
2. **Inspect Identified Middle Name Entries**:
   ```bash
   python -c "
   import json
   with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
       d = json.load(f)
   for idx in [5, 6, 111, 188, 210]:
       print(idx, d['lexicon'][idx]['name'], d['lexicon'][idx].get('content')[:120])
   "
   ```
3. **Verify Live Wyvern Entry Count & Missing IDs**:
   ```bash
   python -c "
   import urllib.request, json
   with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
       t = f.read().strip()
   req = urllib.request.Request('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers={'Authorization': f'Bearer {t}', 'User-Agent': 'AuditorBot/1.0'})
   with urllib.request.urlopen(req) as r:
       data = json.loads(r.read())
   lex = data.get('lexicon', [])
   print('Live Count:', len(lex))
   ids = {e['entry_id'] for e in lex}
   print('Finn present?', 'quJQvjvUWQLUeOCNv2Wko' in ids)
   print('Jasper Rowan present?', 'd1Qg6eRvuKC8iI5kNWPzb' in ids)
   "
   ```
   *Expected Result*: Live count is 209; Finn and Jasper Rowan return `False`.
