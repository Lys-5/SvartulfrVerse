# Review & Adversarial Handoff Report — Milestone 1 Iteration 2: NPC Schema Contract Hardening

**Agent**: `reviewer_m1_it2_1`  
**Roles**: Reviewer, Critic  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_m1_it2_1`  
**Parent Agent**: `c8a5c469-63a4-4154-bc85-fe2572ebf1e1`  
**Date**: `2026-10-24T11:18:00Z`  
**Status**: COMPLETE (Hard Handoff)  
**Verdict**: **APPROVE**  
**Overall Risk Assessment**: LOW  

---

## 1. Observation

### 1.1 Scope and Target Files
1. `tests/test_npc_schema_contract.py` (762 lines, 69 unit tests across 5 test classes).
2. `scripts/verify_npc_schema_contract.py` (957 lines, complete replicated Wyvern Module 93312 compiler, contract validators, and CLI audit runner).
3. Baseline worker handoff report: `.agents/teamwork/worker_m1_it2/handoff.md`.

### 1.2 Independent Test Suite Execution Results
- **Command 1 (Standalone Python Unit Tests)**:
  `python tests/test_npc_schema_contract.py`
  Result:
  ```text
  .....................................................................
  ----------------------------------------------------------------------
  Ran 69 tests in 0.036s

  OK
  ```
- **Command 2 (Pytest via UV with regex plugin)**:
  `uv run --with pytest --with regex pytest tests/test_npc_schema_contract.py -v`
  Result:
  ```text
  ============================= 69 passed in 0.11s ==============================
  ```
- **Command 3 (CLI Contract Self-Tests & Repository File Audit)**:
  `python scripts/verify_npc_schema_contract.py --all`
  Result:
  - 100% of contract self-tests passed (npc_info, Avatar Gallery, Module 93312 compilation, Anti-Collision, Parity).
  - File audit accurately cataloged:
    * `FINAL/Svartulfr_NPC_Primary.json`: Root Gallery Valid = False (missing gallery array/count), Parity = True, 10 legacy duplicate surname defects, Valid npc_info = 0/99 (missing mandatory `middle_names`).
    * `FINAL/Svartulfr_NPC_Secondary.json`: Root Gallery Valid = True, Parity = True, 10 legacy duplicate surname defects, Valid npc_info = 0/211 (missing mandatory `middle_names`).
    * Mirrors in `lorebooks/optimized/`: Identical audit metrics confirmed.

### 1.3 Direct Code Observations
1. **Contract 1 (`validate_npc_info_schema`)**:
   Lines 338–349 explicitly mandate the `"middle_names"` key:
   ```python
   if "middle_names" not in npc_info:
       errors.append("middle_names is required in npc_info (must be a list of strings)")
   else:
       mn = npc_info["middle_names"]
       if mn is None or not isinstance(mn, list):
           errors.append(f"middle_names must be a list of strings, got {type(mn).__name__ if mn is not None else 'null'}")
       else:
           for i, item in enumerate(mn):
               if not isinstance(item, str):
                   errors.append(f"middle_names[{i}] must be a string, got {type(item).__name__}")
   ```
2. **Contract 2 (`validate_avatar_gallery_contract` & `is_valid_https_url`)**:
   - Line 406 rejects boolean counts: `if isinstance(gc, bool) or not isinstance(gc, int) or gc < 0:`.
   - Lines 271–293 (`is_valid_https_url`) validates `s.startswith("https://")`, length > 8, non-empty `netloc`, and required domain dot labels, rejecting bare `https://`, `https://   `, and malformed fragments.
3. **Contract 3 (`normalize_wyvern_regex_pattern` & `detect_duplicate_surnames`)**:
   - Lines 190–201 normalize escaped whitespace (`r'\\+\s+' -> ' '`), whitespace tokens (`r'\\+s[+*]?' -> ' '`), character classes for quotes/hyphens (`['‘’ʼ‛′]` -> `'`, `[-‐‑‒–—−]` -> `-`), unescapes escaped punctuation, and collapses spaces.
   - Lines 218–242 detect duplicate surnames via a three-tier pipeline: known legacy catalog, doubled `last_name` matching, and generic adjacent boundary regex `\b([A-Za-z]+(?:['\-][A-Za-z]+)*)\s+\1\b`.
4. **Contract 4 (`validate_anti_collision_contract`)**:
   - `CANONICAL_BROAD_KEYS` (line 250) frozen set contains all 17 canonical broad umbrella keywords (`solarton`, `succ`, `blackwood`, `losangeles`, `underworld`, `vampire`, `werewolf`, `human`, `demihuman`, `demi-human`, `demon`, `college`, `student`, `alpha`, `beta`, `omega`, `pack`).
   - Case-insensitive exact token matching (`k.strip().lower() in CANONICAL_BROAD_KEYS`) applied across `keys`, `secondary_keys`, `nicknames`, and `npc_info.nicknames`.
5. **Contract 5 (`validate_entries_lexicon_parity`)**:
   - Lines 528–529 check `isinstance(lorebook_data, dict)`.
   - JSON serialization comparison `json.dumps(..., sort_keys=True)` detects differences and pinpoints the first diverging entry index.

---

## 2. Logic Chain

1. **Integrity Assessment**:
   - The implementations in `scripts/verify_npc_schema_contract.py` were scrutinized for hardcoded bypasses, facades, or shortcuts.
   - Observation: We tested arbitrary non-cataloged names (e.g. `Alpha\ Skywalker\ Skywalker`, `Alpha\ Kenobi\ Kenobi`, `Alpha\ Wu\ Wu`, `Jean-Luc\ Jean-Luc`, `D\'Artagnan\ D\'Artagnan`). `detect_duplicate_surnames` correctly caught every doubled name dynamically via tier 2 and tier 3 checks.
   - Observation: The 0/99 and 0/211 scores for `npc_info` in `FINAL/` reflect real absence of `"middle_names"` in the pre-remediation files, confirming that schema gating is fully functional and not self-certifying.
   - Conclusion: **Zero integrity violations detected.**

2. **Correctness & Robustness Verification**:
   - Escaped whitespace (`\ `) in legacy regexes (e.g. Hugh Rivers `Alpha\ Rivers\ Rivers`) is correctly stripped to `Alpha Rivers Rivers` before duplicate checking, successfully detecting all 20 legacy defects across Primary and Secondary lorebooks.
   - Negative tests confirmed that clean patterns with escaped whitespace (`Alpha\ Rivers`, `Dominic\ Rogers`, `Mrs\ Virtuoso`) produce 0 false positives.
   - Broad umbrella key checks strictly reject standalone prohibited terms (`"Alpha"`, `"werewolf"`, `"student"`) while correctly permitting legitimate compound proper names (`"Roman Blackwood"`, `"Alpha Rivers"`, `"Douglas Pack"`).
   - Boolean `gallery_count` values (`True`/`False`) and bare URLs (`"https://"`, `"https://bad"`) are strictly rejected.

3. **Adversarial Edge-Case Discovery (Minor Finding)**:
   - When stress-testing `detect_duplicate_surnames` with an invalid non-string integer `last_name: 123`, the script threw `AttributeError: 'int' object has no attribute 'strip'` on line 228.
   - In `audit_file` (line 651), if an entry contained `npc_info: {"last_name": 123}` along with an `avatar_activation_regex`, `audit_file` crashed on `detect_duplicate_surnames(custom_regex, last_name)`.
   - While real repository files do not contain integer surnames and `validate_npc_info_schema` checks `isinstance(last_name, str)`, adding defensive type checking (`if last_name and isinstance(last_name, str) and last_name.strip():`) is a recommended enhancement for Milestone 2.

---

## 3. Review Report

### Review Summary
- **Verdict**: **APPROVE**
- **Test Results**: 69/69 passed (100%)
- **Codebase Integrity**: Confirmed (No shortcuts, facades, or hardcoded cheating)

### Findings

#### [Minor] Finding 1: Type Guard Robustness in `detect_duplicate_surnames`
- **What**: `detect_duplicate_surnames` calls `last_name.strip()` without verifying `isinstance(last_name, str)`.
- **Where**: `scripts/verify_npc_schema_contract.py:228` (`if last_name and last_name.strip():`) and line 188 (`normalize_wyvern_regex_pattern`).
- **Why**: If a malformed entry has `last_name: 123` and `avatar_activation_regex: "some regex"`, `audit_file` crashes with `AttributeError` instead of completing the report.
- **Suggestion**: In Milestone 2 or next utility update, change line 228 to:
  ```python
  if last_name and isinstance(last_name, str) and last_name.strip():
  ```
  and line 188 to:
  ```python
  if not pattern_str or not isinstance(pattern_str, str):
      return ""
  ```

### Verified Claims
- Claim: Legacy duplicate surname defects cataloged = 20 (10 in Primary, 10 in Secondary) $\to$ Verified via `python scripts/verify_npc_schema_contract.py --all` $\to$ **PASS**
- Claim: `normalize_wyvern_regex_pattern` unescapes backslash whitespace and character classes $\to$ Verified via unit tests and interactive testing $\to$ **PASS**
- Claim: `middle_names: list` strictly enforced, returning 0/99 and 0/211 on un-remediated files $\to$ Verified via pytest and file audit $\to$ **PASS**
- Claim: `CANONICAL_BROAD_KEYS` rejects broad keys while preserving compound proper names $\to$ Verified via test suite and manual verification $\to$ **PASS**
- Claim: Boolean `gallery_count` and bare HTTPS URLs rejected $\to$ Verified via negative unit tests $\to$ **PASS**
- Claim: `entries == lexicon` byte-for-byte parity contract verified on repository files $\to$ Verified via `test_real_repository_primary_and_secondary_parity` $\to$ **PASS**

### Coverage Gaps
- None. All 5 contract requirements defined in `orchestrator_8/PROJECT.md` are covered by tests and audit commands.

---

## 4. Adversarial Challenge Report

### Challenge Summary
- **Overall Risk Assessment**: **LOW**

### Challenges

#### [Low] Challenge 1: Non-string primitive passed as `last_name` or `pattern_str`
- **Assumption challenged**: `detect_duplicate_surnames` assumes `last_name` is always `str` or `None`.
- **Attack scenario**: An unvalidated JSON payload contains `"npc_info": {"first_name": "Test", "last_name": 123}` and `"avatar_activation_regex": "Sample"`.
- **Blast radius**: `audit_file` encounters an unhandled `AttributeError` on line 228 during batch auditing.
- **Mitigation**: Add `isinstance(last_name, str)` guard to `detect_duplicate_surnames`. (Non-blocking for Milestone 1 because real repository files contain valid string names).

### Stress Test Results
- Scenario 1: Arbitrary doubled surname (`Alpha Skywalker Skywalker`) $\to$ Expected: detected $\to$ Actual: `['Skywalker Skywalker']` $\to$ **PASS**
- Scenario 2: Double surname without `last_name` argument (`Alpha Kenobi Kenobi`) $\to$ Expected: detected via generic word boundary $\to$ Actual: `['Kenobi Kenobi']` $\to$ **PASS**
- Scenario 3: Clean pattern with backslash whitespace (`Alpha\ Rivers`) $\to$ Expected: 0 defects $\to$ Actual: 0 defects $\to$ **PASS**
- Scenario 4: Compound name with broad substring (`Roman Blackwood`, `Douglas Pack`) $\to$ Expected: permitted $\to$ Actual: permitted (0 false positives) $\to$ **PASS**
- Scenario 5: Boolean `gallery_count: True` $\to$ Expected: rejected $\to$ Actual: rejected $\to$ **PASS**
- Scenario 6: Malformed URL (`https://` or `https://bad`) $\to$ Expected: rejected $\to$ Actual: rejected $\to$ **PASS**
- Scenario 7: Non-dict entry or lorebook root $\to$ Expected: graceful error tuple without crash $\to$ Actual: graceful error tuple $\to$ **PASS**

---

## 5. Caveats
- No caveats. All 5 contract areas were thoroughly investigated and verified independently.

---

## 6. Conclusion
The implementation of Milestone 1 Iteration 2 in `tests/test_npc_schema_contract.py` and `scripts/verify_npc_schema_contract.py` meets all technical, architectural, and quality standards. The contracts are authentic, robust, and correctly serve as the authoritative gate for Milestone 2 (Data Remediation).

**Verdict**: **APPROVE**.

---

## 7. Verification Method

To reproduce and verify this review independently:
1. `python tests/test_npc_schema_contract.py` (Must report 69 tests passed).
2. `uv run --with pytest --with regex pytest tests/test_npc_schema_contract.py -v` (Must report 69 passed).
3. `python scripts/verify_npc_schema_contract.py --all` (Must report 100% self-test pass rate and catalog the 20 legacy defects across `FINAL/` lorebooks).
