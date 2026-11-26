# Handoff Report: Milestone R1 — Pillar 3 & Pillar 4 Investigation

- **Author**: Explorer 3 (Pillar 3 & 4 Investigator)
- **Recipient**: Parent Orchestrator (`5c61ad50-aa94-4b67-ad53-492fd2f90e52`) / Worker
- **Date**: 2026-10-16T22:00:00Z
- **Target Files**: All 6 standalone lorebooks in `FINAL/`:
  1. `FINAL/Svartulfr_Lorebook_I.json` (`_gwwCxCfQ6PQaLEjAQVpJL`, 219 entries)
  2. `FINAL/Svartulfr_Lorebook_II.json` (`_HfG7TeV6MJyj6bxMwxkpt`, 143 entries)
  3. `FINAL/Svartulfr_Lorebook_III.json` (`_9zWTGqYJNJ4BCDMj8gfcD`, 35 entries)
  4. `FINAL/Svartulfr_Location.json` (`_EjXxkmPVhpCXg8xABpFkK`, 196 entries)
  5. `FINAL/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`, 106 entries)
  6. `FINAL/Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`, 310 entries)
  *Total entries analyzed*: 1,009 entries.

---

## 1. Observation

### 1.1 Scope & Inventory
Scanning all 6 standalone lorebooks in `FINAL/` produced the following entry counts:
- `FINAL/Svartulfr_Lorebook_I.json`: `entries`: 219, `lexicon`: 219 (identical)
- `FINAL/Svartulfr_Lorebook_II.json`: `entries`: 143, `lexicon`: 143 (identical)
- `FINAL/Svartulfr_Lorebook_III.json`: `entries`: 35, `lexicon`: 35 (discrepancy: `entries` has SillyTavern schema, `lexicon` has Wyvern schema)
- `FINAL/Svartulfr_Location.json`: `entries`: 196, `lexicon`: 196 (identical)
- `FINAL/Svartulfr_NPC_Primary.json`: `entries`: 106, `lexicon`: 106 (identical)
- `FINAL/Svartulfr_NPC_Secondary.json`: `entries`: 310, `lexicon`: 310 (identical)
- **Total entries**: **1,009** entries across both `entries` and `lexicon` arrays.

### 1.2 Pillar 3 Observations: Residual `{{age}}` Macros
- **Search command**: Script `scratch/inspect_p3_p4.py` scanning for regex pattern `r'\{\{\s*age\s*\}\}'` case-insensitively across all strings in `FINAL/*.json`.
- **Result**: Exactly **0 occurrences of `{{age}}`** across all 1,009 entries in all 6 files in `FINAL/`.
- **Unique macros found across `FINAL/`**:
  `['{{pronounObjectiveCap}}', '{{pronounObjective}}', '{{pronounPosDetCap}}', '{{pronounPosDet}}', '{{pronounPosPro}}', '{{pronounReflexive}}', '{{pronounSubjectiveCap}}', '{{pronounSubjective}}', '{{user}}']`.
  Zero age macros exist in `FINAL/`.
- **Historical Comparison**:
  - Scanning `lorebooks/source/` revealed **178 historical occurrences** of `{{age}}`:
    - `lorebooks/source/Svartulfr_NPC_Primary.json`: 86 occurrences.
    - `lorebooks/source/Svartulfr_Lorebook_III.json`: 59 occurrences.
    - `lorebooks/source/Svartulfr_Lorebook_I.json`: 26 occurrences.
    - `lorebooks/source/Svartulfr_Lorebook_II.json`: 7 occurrences.
  - Scanning `lorebooks/optimized/` revealed **85 unmirrored occurrences** of `{{age}}`:
    - `lorebooks/optimized/Svartulfr_Lorebook_I.json`: 26 occurrences.
    - `lorebooks/optimized/Svartulfr_Lorebook_III.json`: 59 occurrences.
  - In `FINAL/`, all these entries were migrated and statically evaluated at World-Age 2024:
    - Example: Dominic Rogers: Source had `AGE: {{age}}; BIRTHDAY: Nov...`, `FINAL/` has `AGE: 20; BIRTHDAY: November 14`.
    - Example: Roman Blackwood: Source had `AGE: {{age}}`, `FINAL/` has `AGE: 20`.
    - Example: Alicia Virtuoso (moved from LB I to Secondary NPC): Source had `AGE: {{age}}`, `FINAL/` has `AGE: 28`.
    - Example: Marek: Source had `AGE: {{age}}`, `FINAL/` has `AGE: 38 (Born 18 March 1986)`.

### 1.3 Pillar 4 Observations: NPC Avatars & Regex Splitting
- **Total NPC Entries**: Exactly **416 entries** across all 6 lorebooks have `type: "npc"`:
  - `FINAL/Svartulfr_NPC_Primary.json`: 106 entries.
  - `FINAL/Svartulfr_NPC_Secondary.json`: 310 entries.
  - The other 4 files (`Lorebook I`, `Lorebook II`, `Lorebook III`, `Location`) have 0 entries with `type: "npc"`.
- **Avatar Status on NPCs (416 total)**:
  - **Valid Avatar URLs**: **114 entries** (27.4%)
    - In Primary: 62 entries
    - In Secondary: 52 entries
    - Host domains breakdown:
      - `imagedelivery.net` (Cloudflare): 59 entries
      - `io-modernfantasy.uwu.ai`: 33 entries
      - `ella.janitorai.com`: 21 entries
      - `io-succ.uwu.ai`: 1 entry
  - **Missing / Empty Avatars (`avatar: ""`)**: **302 entries** (72.6%)
    - In `Svartulfr_NPC_Primary.json`: **44 entries** (e.g., Hugh Rivers, Liam O'Connor, Bessie May, Neve, Jaelyn, Kian, Goran, Radek, Roman Blackwood, Eric, Javier Reyes, Raymond, Dean, Scarlett Rose, Sierra, Varg Darkfire, Karshin Darkfire, Boros Darkfire, Aras Darkfire, Kolya Varenkov, Marlowe Voss, Zefir Hvitskog, Vito Marino, Viola Carter, Ut Berg, Naomi Black, Marcus Thornfield, Marcus O'Connor, Magnus Douglas III, Lord Cornelius Douglas, Isobel Blackwater, Helena Weiss, GLUTTONY - Kevin, Federico Savini, Elizabeth Duskwood, Eclipse Noir, ENVY - Siobhan, Dominic Chen, Darius Vale, Cass Harrow, Bianca Rossi, Aurora Night, Archer Wolfwood, Angelo Moreno).
    - In `Svartulfr_NPC_Secondary.json`: **258 entries** (e.g., Jet Thompson, Allegra Lumsden, Luisa Sanchez Rogers, Eira Elloway, Vespera Thorne, Evan, Bramble Mossmere, Silas, Ailsa Hourie, Adelin Coso, Brittany Willow, Coach Mithers, Hideo Reid, Professor Marit Christiansen, Professor Mollusk Moreau, and 243 others).
    - Every missing avatar entry has `avatar: ""` (string of length 0). None are `null` or missing the key.
- **Avatar Regex Splitting Compliance (416 total)**:
  - `custom_avatar_regex`: **416 / 416 are `true`** (100% compliant). Zero missing or false.
  - `lines_parsed`: **416 / 416 are `1`** (100% compliant). Zero missing or non-1.
  - `avatar_activation_regex`: **416 / 416 match multiline format** `r'^\(\?:\^\|\\n\)\\s\*\(\?:.+\)\\s\*:$'` (100% compliant).
    - Examples:
      - `Hugh Rivers`: `(?:^|\n)\s*(?:Hugh\ Rivers|Alpha\ Rivers\ Rivers|Alpha\ Rivers|The\ Mountain\ Sovereign\ Rivers|The\ Mountain\ Sovereign|Hugh)\s*:`
      - `Mei`: `(?:^|\n)\s*(?:Mei)\s*:`
      - `Jet Thompson`: `(?:^|\n)\s*(?:Jet\ Thompson|Hank's\ son\ Thompson|Hank's\ son|Edric's\ friend\ Thompson|Edric's\ friend|Jet)\s*:`
  - `npc_info` object: **416 / 416 valid dicts** containing `['first_name', 'last_name', 'nicknames', 'titles']` (100% compliant).
- **Canonical Svartúlfr Crest Avatar URL**:
  - `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public`
  - Verified present in the repository and confirmed as the official Cloudflare asset for Svartúlfr.

---

## 2. Logic Chain

1. **Pillar 3 (`{{age}}` Macro Evaluation)**:
   - Premise: Requirement R1 calls for identifying any residual `{{age}}` macros, and R2 calls for replacing them with static ages at World-Age 2024 per `GEMINI.md §6`.
   - Observation: Exhaustive regex scan across all 1,009 entries in all 6 files in `FINAL/` yielded 0 matches for `{{age}}`.
   - Tracing: In earlier data pipelines (reflected in `CHANGELOG.md`), 178 `{{age}}` macros from `lorebooks/source/` were already evaluated and converted into static ages in `FINAL/`.
   - Evaluation Logic at World-Age 2024:
     - World Clock epoch is 21 December 827 AD; World-Age 10,486,470 hours corresponds to April 5, 2024 (`GEMINI.md §6`).
     - Undergraduate students at SUCC campus default to age 20 (born 2003–2004).
     - Characters with explicit birthdates were calculated to their 2024 anniversary (e.g. 1980 -> 44, 1986 -> 38, 1996 -> 28, 1998 -> 26).
     - Firstborns / Divine Blood remain visually frozen at ascension (~18-40) with chronological age >1000, capped at RPG level 99.
   - Inference: `FINAL/` is already 100% compliant regarding Pillar 3. However, `lorebooks/optimized/` still contains 85 stale `{{age}}` macros from legacy files; the Worker must mirror the remediated `FINAL/` files into `lorebooks/optimized/` during Milestone R2 to eliminate this discrepancy.

2. **Pillar 4 (NPC Avatars & Regex Splitting)**:
   - Premise: Requirement R1/R2 mandates that 100% of NPC entries must have valid avatars, `custom_avatar_regex: true`, `lines_parsed: 1`, and multiline regex splitting format, and that any NPC lacking an avatar must receive the canonical Svartúlfr Crest fallback avatar with all affected entries recorded in `scratch/missing_npc_avatars.json`.
   - Observation:
     - All 416 NPC entries already possess valid `custom_avatar_regex: true`, `lines_parsed: 1`, and multiline regex splitting `(?:^|\n)\s*(?:...)\s*:`.
     - Exactly 302 NPC entries (44 in Primary, 258 in Secondary) have `avatar: ""`.
   - Inference:
     - The Worker only needs to update `avatar` from `""` to `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public` on these 302 entries.
     - The Worker must update both `entries` and `lexicon` arrays identically.
     - The Worker must output `scratch/missing_npc_avatars.json` logging all 302 affected entries.

---

## 3. Caveats

1. **Non-NPC Spurious Avatar Metadata**:
   - `FINAL/Svartulfr_Lorebook_I.json`, `Svartulfr_Lorebook_II.json`, and `Svartulfr_Location.json` contain spurious NPC metadata (`avatar`, `custom_avatar_regex`, `lines_parsed`, `avatar_activation_regex`, `npc_info`) on non-NPC entries (locations, concepts, factions). This is Pillar 1's domain, investigated by Explorer 1.
2. **Lorebook III Schema Discrepancy**:
   - In `FINAL/Svartulfr_Lorebook_III.json`, `entries` uses SillyTavern schema (`uid`, `key`, `comment`, etc.) while `lexicon` uses Wyvern native schema (`entry_id`, `keys`, `name`, etc.). The Worker must synchronize them to Wyvern schema to satisfy Acceptance Criteria "entries and lexicon arrays in all 6 files are completely identical in length and content".
3. **External Card Files**:
   - Single-character card files in `FINAL/` (e.g. `Erik_Douglas_card.json`, etc.) were also verified: none contain residual `{{age}}` macros.

---

## 4. Conclusion & Remediation Rules for Worker

### 4.1 Summary of Findings
| Pillar | Scope | Total Checked | Compliant | Requiring Action | Action Required |
|---|---|---|---|---|---|
| **Pillar 3** | All 6 Lorebooks in `FINAL/` | 1,009 entries | 1,009 | **0** | Verification only in `FINAL/`; mirror to `lorebooks/optimized/` |
| **Pillar 4 (Avatars)** | NPC entries (Primary & Secondary) | 416 NPCs | 114 | **302** | Apply canonical crest fallback avatar (`https://imagedelivery.net/...`) |
| **Pillar 4 (Regex)** | `custom_avatar_regex: true` | 416 NPCs | 416 | **0** | Already 100% compliant |
| **Pillar 4 (Lines)** | `lines_parsed: 1` | 416 NPCs | 416 | **0** | Already 100% compliant |
| **Pillar 4 (Pattern)** | Multiline `(?:^\|\n)\s*(?:...)\s*:` | 416 NPCs | 416 | **0** | Already 100% compliant |
| **Pillar 4 (Log)** | `scratch/missing_npc_avatars.json` | 302 entries | 0 (file pending) | **1 file** | Generate JSON log with all 302 entries |

### 4.2 Exact Remediation Instructions for Worker

#### Step 1: Avatar Remediation (Pillar 4)
In both `FINAL/Svartulfr_NPC_Primary.json` and `FINAL/Svartulfr_NPC_Secondary.json`:
For every item in `entries` and `lexicon` where `type == "npc"`:
- If `avatar` is empty string `""`, `null`, or does not start with `http`:
  1. Set `avatar = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"`.
  2. Maintain `custom_avatar_regex: true` and `lines_parsed: 1`.
  3. Keep the existing `avatar_activation_regex` untouched (it is already valid multiline format).
  4. Ensure identical mutation on both `entries[i]` and `lexicon[i]`.

#### Step 2: Generate `scratch/missing_npc_avatars.json`
Write a JSON file with the following exact schema:
```json
{
  "audit_timestamp": "2026-10-16T22:00:00Z",
  "canonical_fallback_url": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public",
  "total_remediated": 302,
  "summary": {
    "Svartulfr_NPC_Primary": 44,
    "Svartulfr_NPC_Secondary": 258
  },
  "entries": [
    {
      "lorebook": "Svartulfr_NPC_Primary.json",
      "lorebook_id": "_zwEqgEEzh12X6gHVmMKKC",
      "entry_id": "G5nWnHEcP0MM3zqgiFkNq",
      "index": 7,
      "name": "Hugh Rivers",
      "previous_avatar": "",
      "applied_avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public",
      "keys": ["Hugh Rivers"]
    }
  ]
}
```

#### Step 3: Age Assertions & Mirroring (Pillar 3)
- Run an automated assertion verifying:
  `re.search(r'\{\{\s*age\s*\}\}', json.dumps(item), re.I) is None`
  for all items in all 6 lorebooks.
- During R2 mirroring from `FINAL/` to `lorebooks/optimized/`, overwrite the stale files in `lorebooks/optimized/` so they reflect the 0-macro status.

---

## 5. Verification Method

To independently verify all findings in this report, execute the following commands in powershell:

### 5.1 Verify Pillar 3 (Zero `{{age}}` in `FINAL/`)
```powershell
python -c "
import json, re, glob
files = glob.glob('FINAL/*.json')
matches = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        txt = fp.read()
    found = re.findall(r'\{\{\s*age\s*\}\}', txt, re.I)
    if found:
        print(f'{f}: {len(found)} occurrences')
        matches += len(found)
print(f'Total {{age}} occurrences across FINAL/: {matches}')
assert matches == 0, 'Pillar 3 verification failed: residual {{age}} found!'
print('Pillar 3 PASS: Exactly 0 residual {{age}} macros in FINAL/')
"
```

### 5.2 Verify Pillar 4 (NPC Avatars & Regex Splitting)
```powershell
python -c "
import json, re
prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))['entries']
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))['entries']
all_npcs = prim + sec
assert len(all_npcs) == 416, f'Expected 416 NPCs, got {len(all_npcs)}'

missing_av = [e for e in all_npcs if not (e.get('avatar') and e['avatar'].startswith('http'))]
assert len(missing_av) == 302, f'Expected 302 missing avatars, got {len(missing_av)}'

prim_missing = [e for e in prim if not (e.get('avatar') and e['avatar'].startswith('http'))]
sec_missing = [e for e in sec if not (e.get('avatar') and e['avatar'].startswith('http'))]
assert len(prim_missing) == 44, f'Expected 44 Primary missing, got {len(prim_missing)}'
assert len(sec_missing) == 258, f'Expected 258 Secondary missing, got {len(sec_missing)}'

non_cust_regex = [e for e in all_npcs if e.get('custom_avatar_regex') is not True]
assert len(non_cust_regex) == 0, f'Found {len(non_cust_regex)} non-true custom_avatar_regex'

non_line_1 = [e for e in all_npcs if e.get('lines_parsed') != 1]
assert len(non_line_1) == 0, f'Found {len(non_line_1)} lines_parsed != 1'

reg_pat = re.compile(r'^\(\?:\^\|\\n\)\\s\*\(\?:.+\)\\s\*:$')
bad_reg = [e for e in all_npcs if not reg_pat.match(e.get('avatar_activation_regex', ''))]
assert len(bad_reg) == 0, f'Found {len(bad_reg)} bad avatar_activation_regex'

print('Pillar 4 PASS: 416 NPCs verified. 302 missing avatars (44 Prim, 258 Sec). 100% regex compliance.')
"
```

### Invalidation Conditions
- If any lorebook file in `FINAL/` is modified to introduce `{{age}}`, Pillar 3 findings are invalidated.
- If any NPC entry in `Svartulfr_NPC_Primary.json` or `Svartulfr_NPC_Secondary.json` is modified such that `avatar_activation_regex` deviates from `(?:^|\n)\s*(?:...)\s*:`, Pillar 4 regex compliance is invalidated.
