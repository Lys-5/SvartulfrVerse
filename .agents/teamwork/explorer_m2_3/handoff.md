# Handoff Report — Milestone 2: Automated Mass Remediation and Live Deployment Pipeline

## 1. Observation

Direct empirical observations from codebase inspection, schema contracts, audit tools, and live API queries:

1. **Local Files Audited**:
   - `FINAL/Svartulfr_NPC_Primary.json` (`PRIMARY_LOREBOOK_ID = '_zwEqgEEzh12X6gHVmMKKC'`)
   - `FINAL/Svartulfr_NPC_Secondary.json` (`SECONDARY_LOREBOOK_ID = '_Uht3Ckz44JBDrPnUHq7LV'`)
   - Mirror files: `lorebooks/optimized/Svartulfr_NPC_Primary.json` and `lorebooks/optimized/Svartulfr_NPC_Secondary.json`.

2. **Schema Contract Audit Execution (`scripts/verify_npc_schema_contract.py --all`)**:
   - Output from running `python scripts/verify_npc_schema_contract.py --all`:
     ```text
     Audit Report for: FINAL\Svartulfr_NPC_Primary.json
       Total Entries in Lexicon: 99
       Root Gallery Valid: False (Lorebook root missing 'gallery' array property; Lorebook root missing 'gallery_count' property)
       Entries == Lexicon Parity: True (OK)
       NPC Entries Checked: 99
       Valid Avatars: 99/99
       Valid npc_info: 0/99
       Legacy Duplicate Surname Defects in regex: 10

     Audit Report for: FINAL\Svartulfr_NPC_Secondary.json
       Total Entries in Lexicon: 211
       Root Gallery Valid: True (OK)
       Entries == Lexicon Parity: True (OK)
       NPC Entries Checked: 211
       Valid Avatars: 211/211
       Valid npc_info: 0/211
       Legacy Duplicate Surname Defects in regex: 10
     ```

3. **Root Cause of `Valid npc_info: 0/99` and `0/211`**:
   - Inspection via `.agents/teamwork/explorer_m2_3/check_npc_info_failures.py` revealed:
     - In `FINAL/Svartulfr_NPC_Primary.json`: `[99x] middle_names is required in npc_info (must be a list of strings)`
     - In `FINAL/Svartulfr_NPC_Secondary.json`: `[211x] middle_names is required in npc_info (must be a list of strings)`
   - Every single entry across both lorebooks (310 total) currently contains `first_name`, `last_name`, `nicknames`, `titles`, but is missing `"middle_names": []` and `"npc_prefix": ""`, violating `scripts/verify_npc_schema_contract.py:338-348`.

4. **Defect Catalog: Duplicate Surnames (20 Entries Total)**:
   - Evaluated using `scripts/verify_npc_schema_contract.py:detect_duplicate_surnames()`:
     - Primary Lorebook (10 defects):
       1. `#0 Hugh Rivers` (`G5nWnHEcP0MM3zqgiFkNq`): `Alpha\ Rivers\ Rivers` in regex `(?:^|\n)\s*(?:Hugh\ Rivers|Alpha\ Rivers\ Rivers|Alpha\ Rivers|The\ Mountain\ Sovereign\ Rivers|The\ Mountain\ Sovereign|Hugh)\s*:`
       2. `#10 Dominic Rogers` (`TG-Nl8HyTHt4QWaUW4nhm`): `Rogers Rogers` in regex `(?:^|\n)\s*(?:Dominic\ Rogers|Dom\ Rogers|Dom|Mr\.\ Rogers\ Rogers|Mr\.\ Rogers|Dominic)\s*:`
       3. `#25 Daniel "Danny" Boone` (`98DR0Xp_0gCt65iaWdEHC`): `Boone Boone`
       4. `#28 Harrison Black` (`hNcZTLV1G36Sxlg-bqCQG`): `Black Black`
       5. `#52 Marcus O'Connor` (`csHVm9GEgjr7JPntoIpbB`): `O'Connor O'Connor`
       6. `#66 Helena Weiss` (`MtpFa4Gsqvy40WSACfcNK`): `Weiss Weiss`
       7. `#68 Harlan Beaumont` (`O6RBF9yG-Tkm4cuL58-0k`): `Beaumont Beaumont`
       8. `#73 Federico "Riki" Savini` (`x1_kqtXMD324refVmHKWJ`): `Savini Savini`
       9. `#75 Eris Davies` (`ATOgrfjnoKGxRatwpYgZB`): `davies davies`
       10. `#77 Elizabeth Duskwood` (`7ScS-V6d8tiRnTOPlLD77`): `Duskwood Duskwood`
     - Secondary Lorebook (10 defects):
       1. `#2 Alicia Virtuoso` (`QeicBpVQvmhrnLgITDnrU`): `Virtuoso Virtuoso`
       2. `#4 Ariadne Cirillo` (`CyZknaH7OmYQi5S3ESpNJ`): `Cirillo Cirillo`
       3. `#5 Luisa Sanchez Rogers` (`m6PNxuNGvi7YmlFRVgFWr`): `Rogers Rogers`
       4. `#6 Alistair Ambrose DeVille` (`4YklgqNsuRUDx7Q_KRFji`): `DeVille DeVille`
       5. `#8 Damien Bishop` (`JVtCCxuX3EoaEDgGzhMeM`): `Bishop Bishop`
       6. `#17 Adelin Coso` (`gyZ3SOAsx3M7l42RDqSeZ`): `Coso Coso`
       7. `#21 Professor Marit Christiansen` (`tmBjBzi064j8hQ5PtQ7iK`): `Christiansen Christiansen`
       8. `#22 Professor Mollusk Moreau` (`2eFIqOaYGue3oIes911d2`): `Moreau Moreau`
       9. `#39 Campus Staff Rat` (`oov5UWuVhZ3RGgoxMkaTS`): `rat rat`
       10. `#62 Graham Purcell` (`rfEPGtkW4OKx-NcFOAry_`): `Purcell Purcell`

5. **Defect Catalog: Umbrella Keywords**:
   - Evaluated using `scripts/verify_npc_schema_contract.py:CANONICAL_BROAD_KEYS`:
     - Found in `secondary_keys`: `#8 Damien Bishop` in `FINAL/Svartulfr_NPC_Secondary.json` contains `'demon'`.
     - Zero umbrella keywords found in `keys` or `nicknames` across all 310 entries.

6. **Live Wyvern API Inspection**:
   - Wyvern Web API authentication verified via `scratch/refresh_token.py` (Firebase OAuth ID Token refresh).
   - Live query confirmed active:
     - `GET https://app.wyvern.chat/api/characters/mine` returns HTTP 200 with exactly the 8 canonical cards.
     - `GET https://app.wyvern.chat/api/user-personas` returns HTTP 200 with 3 personas (Alyssa, Echo, Jasper).
     - `GET https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` returns HTTP 200 with 99 entries.
     - `GET https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV` returns HTTP 200 with 209 entries (to be aligned to 211).

7. **Payload Size & HTTP 413 Analysis**:
   - `FINAL/Svartulfr_NPC_Primary.json` full file size: 1,535,172 bytes (1.46 MB).
   - `FINAL/Svartulfr_NPC_Secondary.json` full file size: 2,333,999 bytes (2.23 MB).
   - Compact PUT payload (omitting redundant `entries` array and stripping JSON formatting indentation):
     - Primary: 721,029 bytes (0.69 MB, 53.0% reduction).
     - Secondary: 1,039,755 bytes (0.99 MB, 55.5% reduction).

---

## 2. Logic Chain

1. **Contract Invariant Requirements**:
   - `verify_npc_schema_contract.py` mandates that for every NPC entry:
     - `npc_info` must contain: `first_name` (non-empty str), `middle_names` (list of str), `last_name` (str or None), `nicknames` (list of str), `titles` (list of str), `npc_prefix` (str or None).
     - Because `middle_names` was completely absent from all 310 entries, adding `"middle_names": [...]` (and `"npc_prefix": ""`) immediately brings schema compliance from 0/310 to 310/310.
   - For entries where names contain explicit middle names or titles in JED+ dossiers (e.g., `Dominic Wayne Rogers`, `Erik Ulfr Douglas`, `Alistair Ambrose DeVille`, `Professor Marit Christiansen`), these must be populated accurately into `middle_names` and `titles` rather than collapsed or dropped.

2. **Root Cause and Fix of Duplicate Surnames**:
   - The legacy regex compilation concatenated `f"{nick} {last_name}"` for every nickname. Whenever a nickname already ended with the surname (e.g., `Alpha Rivers`, `Mr. Rogers`, `Bishop`, `Lady Duskwood`), this appended a redundant second surname (`Alpha Rivers Rivers`, `Bishop Bishop`).
   - The fix requires a boundary check: when compiling candidate variants from nicknames, only append `last_name` if `last_name` is non-empty, `nick` does not end with `last_name` (`re.search(rf"\b{re.escape(last_name)}$", nick, re.I)` is None), and `nick.lower() != last_name.lower()`.
   - Verified via `.agents/teamwork/explorer_m2_3/test_clean_regex_builder.py`: 100% of the 20 defective entries compile to clean, valid regex patterns with zero duplicate surnames.

3. **Purging Umbrella Keys**:
   - GEMINI.md §7 and `verify_npc_schema_contract.py` forbid broad keywords (`solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `demon`, etc.) on NPC entries.
   - Damien Bishop's `secondary_keys` contains `'demon'`. Purging `'demon'` and ensuring `selective: false` with `secondary_keys: []` eliminates this violation.

4. **Preserving Anti-Collision Contracts**:
   - Core card characters in Primary (`Erik`, `Malachia`, `Noah`, `Logan`, `Wulfnic`, `Mackenzie`) and Secondary (`Edric`) must preserve their `ignored_characters` arrays (`["_QPea6g4Q1QfeYCVHCLMPR"]`, etc.).
   - Playable personas (`Alyssa`, `Jasper`) must preserve their `ignored_personas` arrays (`["persona_1786335754946"]`, etc.).

5. **Parity and Gallery Preservation**:
   - Primary lorebook is missing root `gallery: []` and `gallery_count: 0`. Injecting them resolves the gallery validation failure.
   - To maintain the 100% byte-for-byte parity contract between `entries` and `lexicon`, `data['entries']` must be assigned via `copy.deepcopy(data['lexicon'])` prior to saving.

6. **Payload Sizing and HTTP 413 Prevention**:
   - Cloudflare enforces request body limits on POST/PUT requests. Sending both `entries` and `lexicon` with 2-space indentation exceeds 2.3 MB.
   - Wyvern's backend only reads `lexicon` (or entries) to update the lorebook. Constructing a compact payload containing top-level fields plus `lexicon` (omitting `entries`) and serializing with `separators=(',', ':')` produces payloads of 721 KB and 1.04 MB. This eliminates any risk of HTTP 413 errors.

---

## 3. Caveats

- **Network Session & Token Lifetime**: Wyvern Firebase ID tokens expire after 3600 seconds (1 hour). The live deployment script must invoke `scratch/refresh_token.py:refresh()` automatically if a call receives HTTP 401 or if the token is stale.
- **Entry Count on Live Wyvern Server**: Live `Svartulfr - NPC Secondary` currently reports 209 entries on Wyvern server, whereas the local canonical file has 211 entries (the 2 added canonical NPCs are `Bruce` and `Adrian` or updated entries from previous migrations). Live deployment of the 211 entries will synchronize the server count to the local canonical truth.
- **No Source Code Changes Made**: In accordance with the Explorer archetype rules, no source files were modified during this investigation. All tests and inspection tools were executed strictly in the `.agents/teamwork/explorer_m2_3/` directory or run in-memory.

---

## 4. Conclusion & Complete Pipeline Specification

The design of the automated mass remediation script `scripts/remediate_lorebook_npcs.py` and the live deployment pipeline is specified below.

### 4.1 Specification of `scripts/remediate_lorebook_npcs.py`

#### Module Architecture and Constants
- **Script Location**: `scripts/remediate_lorebook_npcs.py`
- **Imports**: `argparse`, `copy`, `json`, `os`, `pathlib`, `re`, `sys`, `time`, `urllib.request`, `urllib.error`.
- **Import Contract Validators**:
  ```python
  from scripts.verify_npc_schema_contract import (
      validate_npc_info_schema,
      validate_avatar_gallery_contract,
      validate_anti_collision_contract,
      validate_entries_lexicon_parity,
      detect_duplicate_surnames,
      CANONICAL_BROAD_KEYS,
  )
  ```
- **Constants**:
  ```python
  PRIMARY_ID = '_zwEqgEEzh12X6gHVmMKKC'
  SECONDARY_ID = '_Uht3Ckz44JBDrPnUHq7LV'
  PRIMARY_BUDGET = 7500
  SECONDARY_BUDGET = 5000
  OFFICIAL_COVER = 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public'
  ```

#### Canonical Name & Middle Name Catalog
```python
KNOWN_SPECIAL_NAMES = {
    # Primary Core & Complex Names
    "Dominic Rogers": {"first_name": "Dominic", "middle_names": ["Wayne"], "last_name": "Rogers", "titles": []},
    "Roland Vickers": {"first_name": "Roland", "middle_names": ["Mark"], "last_name": "Vickers", "titles": []},
    "Marcus Thornfield": {"first_name": "Marcus", "middle_names": ["Iron"], "last_name": "Thornfield", "titles": []},
    "Kaladin Nargathon": {"first_name": "Kaladin", "middle_names": ["Blackwolf"], "last_name": "Nargathon", "titles": []},
    "Iordan R. Vess": {"first_name": "Iordan", "middle_names": ["R."], "last_name": "Vess", "titles": ["Alpha"]},
    "Noah Loki Douglas Bloodmoon": {"first_name": "Noah", "middle_names": ["Loki"], "last_name": "Douglas Bloodmoon", "titles": []},
    "Jasper Svartr Douglas Bloodmoon": {"first_name": "Jasper", "middle_names": ["Svartr"], "last_name": "Douglas Bloodmoon", "titles": []},
    "Alyssa Hvit Douglas Bloodmoon": {"first_name": "Alyssa", "middle_names": ["Hvit"], "last_name": "Douglas Bloodmoon", "titles": []},
    "Malachia Björn Douglas Bloodmoon": {"first_name": "Malachia", "middle_names": ["Björn"], "last_name": "Douglas Bloodmoon", "titles": []},
    "Nixara Hvit Bloodmoon": {"first_name": "Nixara", "middle_names": ["Hvit"], "last_name": "Bloodmoon", "titles": []},
    "Wulfnic Báleygr Bloodmoon": {"first_name": "Wulfnic", "middle_names": ["Báleygr"], "last_name": "Bloodmoon", "titles": []},
    "Logan Járn Douglas": {"first_name": "Logan", "middle_names": ["Járn"], "last_name": "Douglas", "titles": []},
    "Erik Ulfr Douglas": {"first_name": "Erik", "middle_names": ["Ulfr"], "last_name": "Douglas", "titles": []},
    "Lord Cornelius Douglas": {"first_name": "Cornelius", "middle_names": [], "last_name": "Douglas", "titles": ["Lord"]},
    "Magnus Douglas III": {"first_name": "Magnus", "middle_names": [], "last_name": "Douglas", "titles": ["III"]},
    "Dr. Arthur Sinclair": {"first_name": "Arthur", "middle_names": [], "last_name": "Sinclair", "titles": ["Dr."]},
    "Stanley Davies Sr.": {"first_name": "Stanley", "middle_names": [], "last_name": "Davies", "titles": ["Sr."]},
    "Stanley Davies Jr.": {"first_name": "Stanley", "middle_names": [], "last_name": "Davies", "titles": ["Jr."]},
    "Sullivan \"Sully\" Jones": {"first_name": "Sullivan", "middle_names": [], "last_name": "Jones", "titles": []},
    "Federico \"Riki\" Savini": {"first_name": "Federico", "middle_names": [], "last_name": "Savini", "titles": []},
    "Fade Greymoor": {"first_name": "Mihaela", "middle_names": [], "last_name": "Greymoor", "titles": []},
    "Echo": {"first_name": "Echo", "middle_names": [], "last_name": "", "titles": []},
    # Secondary Core & Complex Names
    "Alistair Ambrose DeVille": {"first_name": "Alistair", "middle_names": ["Ambrose"], "last_name": "DeVille", "titles": []},
    "Campus Staff Rat": {"first_name": "Campus", "middle_names": ["Staff"], "last_name": "Rat", "titles": []},
    "Luisa Sanchez Rogers": {"first_name": "Luisa", "middle_names": [], "last_name": "Sanchez-Rogers", "titles": []},
    "Amerian de Vian": {"first_name": "Amerian", "middle_names": ["de"], "last_name": "Vian", "titles": []},
    "Professor Marit Christiansen": {"first_name": "Marit", "middle_names": [], "last_name": "Christiansen", "titles": ["Professor"]},
    "Professor Mollusk Moreau": {"first_name": "Mollusk", "middle_names": [], "last_name": "Moreau", "titles": ["Professor"]},
    "Coach Mithers": {"first_name": "Mithers", "middle_names": [], "last_name": "", "titles": ["Coach"]},
    "Finn the Satyr": {"first_name": "Finn", "middle_names": [], "last_name": "the Satyr", "titles": []},
    "Charles \"Charlie\" DeVille": {"first_name": "Charles", "middle_names": [], "last_name": "DeVille", "titles": []},
    "Roger \"Rocky\" Mackenzie": {"first_name": "Roger", "middle_names": [], "last_name": "Mackenzie", "titles": []},
    "Romeo \"Gray\" Dean": {"first_name": "Romeo", "middle_names": [], "last_name": "Dean", "titles": []},
}
```

#### Remediation Pipeline Logic (Per Lorebook)
1. **Load Data**:
   Read `FINAL/Svartulfr_NPC_Primary.json` and `FINAL/Svartulfr_NPC_Secondary.json`.
2. **Root Sanitization**:
   - Ensure `data["gallery"] = data.get("gallery", [])`
   - Ensure `data["gallery_count"] = len(data["gallery"])`
   - Ensure `photoURL = OFFICIAL_COVER`
   - Ensure `token_budget` is set to `7500` (Primary) or `5000` (Secondary).
3. **Entry Remediation Loop (over `data['lexicon']`)**:
   For each entry `e`:
   - **Step 3A: Name Decomposition**:
     - Check `e.get('name')` in `KNOWN_SPECIAL_NAMES`. If matched, extract `first_name`, `middle_names`, `last_name`, and `titles`.
     - Otherwise, check `e.get('npc_info')`:
       - `first_name = info.get('first_name') or e.get('name').split()[0]`
       - `last_name = info.get('last_name') or (e.get('name').split()[-1] if len(e.get('name').split()) > 1 else "")`
       - `middle_names = info.get('middle_names') or []`
       - `titles = info.get('titles') or []`
     - Clean `nicknames`: start with `info.get('nicknames') or []`.
       - Strip any token matching `CANONICAL_BROAD_KEYS` (e.g., `'demon'`, `'student'`, `'werewolf'`, etc.).
   - **Step 3B: Format `npc_info`**:
     ```python
     e["npc_info"] = {
         "first_name": str(first_name).strip(),
         "middle_names": [str(m).strip() for m in middle_names if str(m).strip()],
         "last_name": str(last_name).strip() if last_name else "",
         "nicknames": [str(n).strip() for n in nicknames if str(n).strip() and str(n).strip().lower() not in CANONICAL_BROAD_KEYS],
         "titles": [str(t).strip() for t in titles if str(t).strip()],
         "npc_prefix": ""
     }
     ```
   - **Step 3C: Compile Clean Avatar Activation Regex**:
     Generate candidate variants:
     - Titles + Full Name: `f"{title} {first_name} {' '.join(middle_names)} {last_name}".strip()`
     - Full Name with Middle: `f"{first_name} {' '.join(middle_names)} {last_name}".strip()`
     - First + Last: `f"{first_name} {last_name}".strip()` if last_name else None
     - Nickname variants:
       - For `n` in `npc_info["nicknames"]`:
         - Only append `last_name` if `last_name` is present, `n` does NOT end with `last_name` (`re.search(rf"\b{re.escape(last_name)}$", n, re.I)` is None), and `n.lower() != last_name.lower()`.
         - Add `n`.
     - First name: `first_name`.
     - Deduplicate variants case-insensitively while preserving order.
     - Escape regex characters, replacing spaces with `\ `.
     - Set `e["avatar_activation_regex"] = rf"(?:^|\n)\s*(?:{'|'.join(escaped_variants)})\s*:"`
     - Set `e["custom_avatar_regex"] = True`
     - Set `e["lines_parsed"] = 1`
   - **Step 3D: Umbrella Key & Anti-Collision Sanitization**:
     - Filter `e["keys"]`: remove any key in `CANONICAL_BROAD_KEYS`.
     - Filter `e["secondary_keys"]`: remove any key in `CANONICAL_BROAD_KEYS`.
     - If `e.get("selective")` is not True:
       - Set `e["selective"] = False`
       - Set `e["secondary_keys"] = []`
     - Preserve `e["ignored_characters"]` and `e["ignored_personas"]`.
4. **Parity Synchronization**:
   - `data["entries"] = copy.deepcopy(data["lexicon"])`
5. **Contract Pre-Save Validation**:
   - Run `validate_avatar_gallery_contract(lorebook_root=data)`
   - Run `validate_entries_lexicon_parity(data)`
   - For every entry, assert `validate_npc_info_schema(e["npc_info"])[0]` is True.
   - For every entry, assert len(`detect_duplicate_surnames(e["avatar_activation_regex"], e["npc_info"]["last_name"])`) == 0.
   - For every entry, assert `validate_anti_collision_contract(e)[0]` is True.
6. **Disk Persistence**:
   - Write updated `data` with `indent=2, ensure_ascii=False` to:
     - `FINAL/Svartulfr_NPC_Primary.json`
     - `FINAL/Svartulfr_NPC_Secondary.json`
     - `lorebooks/optimized/Svartulfr_NPC_Primary.json`
     - `lorebooks/optimized/Svartulfr_NPC_Secondary.json`

---

### 4.2 Specification of Live Deployment PUT Sequence

#### Authentication and Headers
1. **Token Refresh**:
   - Read token from `scratch/wyvern_token.txt`.
   - Call `scratch/refresh_token.py:refresh()` if token is expired or upon encountering HTTP 401.
2. **HTTP Headers**:
   ```python
   headers = {
       "Authorization": f"Bearer {token}",
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
       "Accept": "application/json"
   }
   ```

#### Anti-HTTP 413 Payload Architecture
1. **Omit Redundant `entries` Array**:
   - The Wyvern backend expects the canonical list in `lexicon`. Sending both `entries` and `lexicon` inflates the payload to 2.4 MB.
2. **Compact Serializer**:
   - Construct dictionary:
     ```python
     compact_payload = {
         "name": data.get("name"),
         "description": data.get("description", ""),
         "photoURL": data.get("photoURL"),
         "token_budget": data.get("token_budget"),
         "visibility": data.get("visibility", "private"),
         "rating": data.get("rating", "explicit"),
         "scan_depth": data.get("scan_depth", 5),
         "recursive_scanning": data.get("recursive_scanning", True),
         "gallery": data.get("gallery", []),
         "gallery_count": len(data.get("gallery", [])),
         "lexicon": data.get("lexicon", [])
     }
     ```
   - Serialize with zero indentation:
     ```python
     payload_bytes = json.dumps(compact_payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
     ```
   - Resulting sizes:
     - Primary (`_zwEqgEEzh12X6gHVmMKKC`): ~721 KB.
     - Secondary (`_Uht3Ckz44JBDrPnUHq7LV`): ~1.04 MB.
     - Both well within Cloudflare's strict body limits.

#### Sequential Network Execution & Pacing
```python
# 1. Primary Lorebook PUT
req_prim = urllib.request.Request(
    f"https://app.wyvern.chat/api/lorebooks/{PRIMARY_ID}",
    data=primary_payload_bytes,
    headers=headers,
    method="PUT"
)
with urllib.request.urlopen(req_prim, timeout=90) as resp:
    assert resp.status == 200, f"Primary PUT failed with HTTP {resp.status}"

# Pacing delay to prevent rate limits
time.sleep(3.0)

# 2. Secondary Lorebook PUT
req_sec = urllib.request.Request(
    f"https://app.wyvern.chat/api/lorebooks/{SECONDARY_ID}",
    data=secondary_payload_bytes,
    headers=headers,
    method="PUT"
)
with urllib.request.urlopen(req_sec, timeout=90) as resp:
    assert resp.status == 200, f"Secondary PUT failed with HTTP {resp.status}"

# Pacing delay before verification
time.sleep(2.5)
```

#### Post-Deployment Cloud Verification
1. `GET https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC`:
   - Assert HTTP 200.
   - Assert `len(data["lexicon"]) == 99`.
   - Assert `data["token_budget"] == 7500`.
   - Assert `data["photoURL"] == OFFICIAL_COVER`.
2. `GET https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV`:
   - Assert HTTP 200.
   - Assert `len(data["lexicon"]) == 211`.
   - Assert `data["token_budget"] == 5000`.
   - Assert `data["photoURL"] == OFFICIAL_COVER`.

---

## 5. Verification Method

To independently verify the implementation once executed by the implementer agent:

1. **Local Contract Verification Command**:
   ```powershell
   python scripts/verify_npc_schema_contract.py --all
   ```
   **Pass Criteria**:
   - `ALL CONTRACT SELF-TESTS PASSED SUCCESSFULLY (100% SUCCESS RATE)`.
   - For all 4 files (`FINAL/Primary`, `FINAL/Secondary`, `lorebooks/optimized/Primary`, `lorebooks/optimized/Secondary`):
     - `Root Gallery Valid: True (OK)`
     - `Entries == Lexicon Parity: True (OK)`
     - `Valid Avatars: 99/99` and `211/211`
     - `Valid npc_info: 99/99` and `211/211` (100% compliance)
     - `Legacy Duplicate Surname Defects in regex: 0` (0 defects)
     - Zero umbrella keyword violations.

2. **Cloud API Verification Command**:
   ```powershell
   python scratch/inspect_current_state.py
   ```
   **Pass Criteria**:
   - `Success GET https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC -> name: Svartúlfr - NPC Primary, entries: 99`
   - `Success GET https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV -> name: Svartúlfr - NPC Secondary, entries: 211`

3. **Invalidation Conditions**:
   - If any entry produces `detect_duplicate_surnames() != []`.
   - If `middle_names` is omitted or not a list.
   - If `entries` serialization differs by even 1 byte from `lexicon`.
   - If PUT request fails with HTTP 413 (indicates `entries` was accidentally included in the PUT payload).
