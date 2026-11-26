# Investigation Report — Milestone R1: Standalone Lorebooks Audit & Repository Pre-Flight

**Agent**: Explorer 1 (`explorer_r1_1`)  
**Mission**: Milestone R1 — Safety Snapshot Pre-flight & 4-Pillar Structural Inspection of Standalone Lorebooks  
**Target Repository**: `e:\repository\SvartulfrVerse`  
**Timestamp**: 2026-10-16T21:55:00Z  

---

## 1. Observation

### 1.1 Lorebook File Names, IDs, and Entry Counts

Inspection of the `FINAL/` directory, `scratch/synced_wyvern_ids.json`, and live Wyvern Web API queries (`GET https://app.wyvern.chat/api/lorebooks/{id}`) confirmed the exact mapping and entry counts across all 6 standalone lorebooks:

| # | Lorebook Title | Filename in `FINAL/` | Lorebook ID | `entries` Count | `lexicon` Count | Equal? | Live Wyvern Lexicon |
|---|----------------|----------------------|-------------|-----------------|-----------------|--------|---------------------|
| 1 | Svartúlfr - Lorebook I | `Svartulfr_Lorebook_I.json` | `_gwwCxCfQ6PQaLEjAQVpJL` | 219 | 219 | Yes | 219 |
| 2 | Svartúlfr - Lorebook II | `Svartulfr_Lorebook_II.json` | `_HfG7TeV6MJyj6bxMwxkpt` | 143 | 143 | Yes | 143 |
| 3 | Svartúlfr - Lorebook III (SUCC & Underworld) | `Svartulfr_Lorebook_III.json` | `_9zWTGqYJNJ4BCDMj8gfcD` | 35 | 35 | Yes (counts) | 35 |
| 4 | Svartúlfr - Location | `Svartulfr_Location.json` | `_EjXxkmPVhpCXg8xABpFkK` | 196 | 196 | Yes | 196 |
| 5 | Svartúlfr - NPC Primary | `Svartulfr_NPC_Primary.json` | `_zwEqgEEzh12X6gHVmMKKC` | 106 | 106 | Yes | 106 |
| 6 | Svartúlfr - NPC Secondary | `Svartulfr_NPC_Secondary.json` | `_Uht3Ckz44JBDrPnUHq7LV` | 310 | 310 | Yes | 310 |
| **Total** | | | | **1,009** | **1,009** | | **1,009** |

- Total entries verified: **1,009 entries** in `entries` and **1,009 entries** in `lexicon`.
- Cumulative sum: 219 + 143 + 35 + 196 + 106 + 310 = 1,009.

### 1.2 Structural Schema Discrepancy in Lorebook III
- In `FINAL/Svartulfr_Lorebook_I.json`, `Svartulfr_Lorebook_II.json`, `Svartulfr_Location.json`, `Svartulfr_NPC_Primary.json`, and `Svartulfr_NPC_Secondary.json`, the `entries` array and `lexicon` array are identical in structure and keys (`entry_id`, `keys`, `secondary_keys`, `content`, `type`, etc.).
- In `FINAL/Svartulfr_Lorebook_III.json`:
  - `entries` array (35 items) is in SillyTavern / CharacterBook schema:
    ```json
    ["uid", "key", "keysecondary", "comment", "content", "constant", "selective", "selectiveLogic", "order", "position", "disable", "excludeRecursion", "probability", "useProbability", "depth", "matchWholeWords", "preventRecursion", "enabled", "priority"]
    ```
  - `lexicon` array (35 items) is in Wyvern Lexicon schema:
    ```json
    ["entry_id", "name", "type", "keys", "secondary_keys", "key_logic", "content", "enabled", "priority", "position"]
    ```
  - Deep equality test `entries == lexicon` returns `False` for `Svartulfr_Lorebook_III.json`.

### 1.3 Four-Pillar Inspection Findings in `FINAL/`

1. **Pillar 1: Spurious NPC metadata on non-NPC entries (`npc_info`, `custom_avatar_regex`, `lines_parsed`)**:
   - `Svartulfr_Lorebook_I.json` (219 entries): 0 occurrences.
   - `Svartulfr_Lorebook_II.json` (143 entries): 0 occurrences.
   - `Svartulfr_Lorebook_III.json` (35 entries): 0 occurrences.
   - `Svartulfr_Location.json` (196 entries): 0 occurrences.
   - All 416 NPC entries in Primary (106) and Secondary (310) are legitimate NPCs.
   - **Total Spurious Fields on Non-NPC Entries: 0**.

2. **Pillar 2: Umbrella keywords (`BROAD_KEYS`) on NPC trigger keys**:
   - `BROAD_KEYS` checked: `['solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega']`.
   - Lorebook I, II, III, Location: 0 NPC entries.
   - `Svartulfr_NPC_Primary.json`:
     - Entry index 60 (`entry_id: "jDuJtzirlEZC3K_ArIufh"`, name: `"Malachia Björn Douglas Bloodmoon"`):
       - Primary `keys`: `['Malachia', 'Björn', 'Malachia Björn', 'Mal', 'The King']`
       - `secondary_keys`: `['Ghost', 'King', 'Alpha', 'bodyguard', 'underground fighting']` -> contains verbatim `"Alpha"`.
   - `Svartulfr_NPC_Secondary.json`:
     - 0 entries contain standalone umbrella keys. (Phrases with partial substring matches, like `"succ student"` for Brittany Willow or `"succubus"` for Ariadne Cirillo, were inspected).
   - `selective: true` flag: 0 entries across all 6 files have `selective: true` set without secondary keys. In fact, `selective` is `false` or absent on 100% of entries.
   - **Total Standalone Umbrella Keys on NPCs: 1** (in Malachia's `secondary_keys`).

3. **Pillar 3: Residual `{{age}}` macros**:
   - Full regex scan `\{\{age[^\}]*\}\}` across all text of all 6 JSON files in `FINAL/`:
     - `Svartulfr_Lorebook_I.json`: 0
     - `Svartulfr_Lorebook_II.json`: 0
     - `Svartulfr_Lorebook_III.json`: 0
     - `Svartulfr_Location.json`: 0
     - `Svartulfr_NPC_Primary.json`: 0
     - `Svartulfr_NPC_Secondary.json`: 0
   - **Total Residual `{{age}}` Macros: 0**.

4. **Pillar 4: NPC Avatar portraits and regex splitting**:
   - Regex Splitting & Activation:
     - `custom_avatar_regex: true`: 106/106 in Primary (100%), 310/310 in Secondary (100%).
     - `lines_parsed: 1`: 106/106 in Primary (100%), 310/310 in Secondary (100%).
     - `avatar_activation_regex` contains `(?:^|\n)`: 106/106 in Primary (100%), 310/310 in Secondary (100%).
   - Avatar Portraits:
     - `Svartulfr_NPC_Primary.json` (106 entries):
       - Populated: 62 entries (53 Cloudflare imagedelivery.net, 6 JanitorAI, 3 uwu.ai).
       - Empty (`avatar: ""`): **44 entries**.
     - `Svartulfr_NPC_Secondary.json` (310 entries):
       - Populated: 52 entries (6 Cloudflare, 30 uwu.ai, 15 JanitorAI, 1 succ.uwu.ai).
       - Empty (`avatar: ""`): **258 entries**.
   - **Total NPCs Lacking Avatar Portraits: 302 entries** (44 + 258).

### 1.4 Backup Directory Status
- Path: `e:\repository\SvartulfrVerse\scratch\backup_pre_audit_lorebooks\`
- Status: **Does not exist yet**. `os.path.exists('scratch/backup_pre_audit_lorebooks')` returned `False`.
- Action needed: Must be created as the initial step of Milestone R2.

### 1.5 Wyvern API Token Status
- Path: `e:\repository\SvartulfrVerse\scratch\wyvern_token.txt`
- Size: 1,142 bytes.
- Verification: A live test request `GET https://app.wyvern.chat/api/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL` with `Authorization: Bearer <token>` returned **HTTP 200 OK** in 2.1s with full lorebook JSON payload.
- Status: **Fully active, authenticated, and valid**.

### 1.6 `lorebooks/optimized/` Status
- Path: `e:\repository\SvartulfrVerse\lorebooks\optimized\`
- Inspection of files vs `FINAL/`:
  - `Svartulfr_Lorebook_I.json`: MD5 mismatch (stale, 252 entries, 0 lexicon).
  - `Svartulfr_Lorebook_II.json`: MD5 match (identical).
  - `Svartulfr_Lorebook_III.json`: MD5 mismatch (stale, 202 entries, 0 lexicon).
  - `Svartulfr_Location.json`: MD5 mismatch (stale, 196 entries, 0 lexicon).
  - `Svartulfr_NPC_Primary.json`: MD5 match (identical).
  - `Svartulfr_NPC_Secondary.json`: MD5 mismatch (stale, 313 entries, 0 lexicon).
- Status: **Stale**. 4 out of 6 files in `lorebooks/optimized/` do not reflect current `FINAL/` state and lack `lexicon` entries. Milestone R2 must overwrite all 6 files.

---

## 2. Logic Chain

1. **Premise**: Milestone R1 requires verifying total entry counts, locating files and IDs, auditing 4 structural pillars, and checking backups and tokens before changes are made.
2. **Step 1 (File & ID Resolution)**: Direct inspection of `FINAL/` and `scratch/synced_wyvern_ids.json` confirmed that the 6 standalone lorebooks correspond exactly to the 6 IDs specified in `ORIGINAL_REQUEST.md`:
   - `_gwwCxCfQ6PQaLEjAQVpJL` -> `Svartulfr_Lorebook_I.json`
   - `_HfG7TeV6MJyj6bxMwxkpt` -> `Svartulfr_Lorebook_II.json`
   - `_9zWTGqYJNJ4BCDMj8gfcD` -> `Svartulfr_Lorebook_III.json`
   - `_EjXxkmPVhpCXg8xABpFkK` -> `Svartulfr_Location.json`
   - `_zwEqgEEzh12X6gHVmMKKC` -> `Svartulfr_NPC_Primary.json`
   - `_Uht3Ckz44JBDrPnUHq7LV` -> `Svartulfr_NPC_Secondary.json`
3. **Step 2 (Entry Count Verification)**: Summing `len(entries)` and `len(lexicon)` across all 6 files yields exactly 1,009 items in each array:
   $$219 + 143 + 35 + 196 + 106 + 310 = 1,009$$
   This satisfies the 1,009 total requirement.
4. **Step 3 (Dual Array Equivalence)**: Deep equality checks between `entries` and `lexicon` passed for 5 files, but failed on `Svartulfr_Lorebook_III.json` because `entries` contains legacy SillyTavern properties while `lexicon` contains Wyvern Lexicon properties. For acceptance criterion 5 ("entries and lexicon arrays in all 6 files are completely identical in length and content"), `Svartulfr_Lorebook_III.json` must have its `entries` replaced with its `lexicon` content.
5. **Step 4 (4-Pillar Remediation Scope Determination)**:
   - Pillar 1: Non-NPC entries have already been purged of spurious metadata (0 remaining).
   - Pillar 2: Malachia's `secondary_keys` contains `"Alpha"`, which triggers on general chat. It must be pruned.
   - Pillar 3: All `{{age}}` macros have already been resolved (0 remaining).
   - Pillar 4: Exactly 302 NPC entries (44 Primary, 258 Secondary) have `avatar: ""`. These must receive the canonical Svartúlfr Crest fallback avatar (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public`) and be recorded in `scratch/missing_npc_avatars.json`.
6. **Step 5 (Backup & Mirroring Plan)**:
   - `scratch/backup_pre_audit_lorebooks/` must be populated by copying the 6 files from `FINAL/` before remediation script runs.
   - After remediation, all 6 remediated files must be copied to `lorebooks/optimized/`.
7. **Step 6 (API Deployment Plan)**:
   - The token in `scratch/wyvern_token.txt` is verified live (HTTP 200).
   - Wyvern PUT requests must include both top-level metadata (`name`, `description`, `visibility: "private"`, `rating: "explicit"`, `scan_depth: 5`, `token_budget: 5000`, `recursive_scanning: true`) and both `entries` and `lexicon` payloads with 2.5s pacing to prevent metadata erasure or rate limiting.

---

## 3. Caveats

1. **Live Wyvern Current State**: Live Wyvern lorebooks currently have `entries: 0` for 5 out of 6 lorebooks (only `lexicon` was populated on previous deploy), while LB3 has 35/35. Deploying both `entries` and `lexicon` in R3 will bring Wyvern live into full dual-array synchronization.
2. **Compound Keywords**: Compound phrases such as `"succ student"` on Brittany Willow or `"blackwood council"` on council members were not flagged as isolated `BROAD_KEYS` because they are multi-word specific phrases. However, the implementer can choose whether to prune `"succ student"` to avoid partial token match if the engine uses sub-tokenization.

---

## 4. Conclusion

The repository is in an optimal state to proceed with Milestone R2 (Automated Remediation) and Milestone R3 (Live Wyvern API Deployment).
- Total entries: **1,009** (verified).
- Dual arrays: 5 of 6 lorebooks already synchronized; Lorebook III needs `entries = lexicon` alignment.
- Remediation targets:
  - 1 broad key to prune (`"Alpha"` from Malachia's `secondary_keys`).
  - 302 missing NPC avatars to populate with the canonical Crest fallback URL.
  - Snapshot copy to `scratch/backup_pre_audit_lorebooks/`.
  - Mirror copy to `lorebooks/optimized/`.
  - Live deployment of all 6 lorebooks via `PUT /api/lorebooks/{id}` using the verified token.

---

## 5. Verification Method

To independently verify all observations and data points, run the following commands in PowerShell from the repository root:

```powershell
# 1. Verify Entry and Lexicon Counts across all 6 files
python -c "import json, os; print([(f, len(json.load(open('FINAL/'+f, encoding='utf-8'))['entries']), len(json.load(open('FINAL/'+f, encoding='utf-8'))['lexicon'])) for f in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']]); print('Total Entries:', sum(len(json.load(open('FINAL/'+f, encoding='utf-8'))['entries']) for f in ['Svartulfr_Lorebook_I.json', 'Svartulfr_Lorebook_II.json', 'Svartulfr_Lorebook_III.json', 'Svartulfr_Location.json', 'Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']))"

# 2. Verify Wyvern API Token Validity
python -c "import urllib.request, json, pathlib; t = pathlib.Path('scratch/wyvern_token.txt').read_text(encoding='utf-8').strip(); req = urllib.request.Request('https://app.wyvern.chat/api/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL', headers={'Authorization': 'Bearer ' + t, 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}); res = urllib.request.urlopen(req); print('HTTP Status:', res.status)"

# 3. Verify Missing Avatars Count (302 total)
python -c "import json; p = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))['lexicon']; s = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))['lexicon']; print('Primary missing:', sum(1 for e in p if not (e.get('avatar') or '').strip())); print('Secondary missing:', sum(1 for e in s if not (e.get('avatar') or '').strip())); print('Total missing:', sum(1 for e in p if not (e.get('avatar') or '').strip()) + sum(1 for e in s if not (e.get('avatar') or '').strip()))"
```
