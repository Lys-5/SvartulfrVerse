# Handoff Report — BROAD_KEYS Anti-Collision Contract Fix Strategy

- **Agent**: `explorer_m1_it2_2`
- **Role**: Explorer / Problem Analysis & Strategy Formulation
- **Target Files**:
  - `scripts/verify_npc_schema_contract.py`
  - `tests/test_npc_schema_contract.py`
  - `tests/test_adversarial_npc_schema.py`
- **Status**: Complete Investigation & Actionable Fix Strategy

---

## 1. Observation

### 1.1 Direct Inspection of `validate_anti_collision_contract`
In `scripts/verify_npc_schema_contract.py:355-399`:
```python
355: def validate_anti_collision_contract(entry: Dict[str, Any]) -> Tuple[bool, List[str]]:
356:     """
357:     Validates anti-collision preservation:
358:     - ignored_characters: list of str (Character Card IDs)
359:     - ignored_personas: list of str (Persona IDs)
360:     - selective: bool
361:     - secondary_keys: list of str
362:     Rules:
363:       * ignored_characters and ignored_personas must be lists of strings.
364:       * selective must be False unless secondary_keys is populated.
365:     """
366:     errors = []
367:     if not isinstance(entry, dict):
368:         return False, ["Entry must be a dictionary"]
369: 
370:     # ignored_characters
371:     ic = entry.get("ignored_characters")
372:     if ic is not None:
373:         if not isinstance(ic, list):
374:             errors.append(f"'ignored_characters' must be a list, got {type(ic).__name__}")
375:         else:
376:             for i, item in enumerate(ic):
377:                 if not isinstance(item, str):
378:                     errors.append(f"'ignored_characters[{i}]' must be a string card ID, got {type(item).__name__}")
379: 
380:     # ignored_personas
381:     ip = entry.get("ignored_personas")
382:     if ip is not None:
383:         if not isinstance(ip, list):
384:             errors.append(f"'ignored_personas' must be a list, got {type(ip).__name__}")
385:         else:
386:             for i, item in enumerate(ip):
387:                 if not isinstance(item, str):
388:                     errors.append(f"'ignored_personas[{i}]' must be a string persona ID, got {type(item).__name__}")
389: 
390:     # selective vs secondary_keys
391:     selective = entry.get("selective", False)
392:     sec_keys = entry.get("secondary_keys", [])
393:     if not isinstance(sec_keys, list):
394:         errors.append(f"'secondary_keys' must be a list, got {type(sec_keys).__name__}")
395:     elif selective and len(sec_keys) == 0:
396:         errors.append("Entry has 'selective: true' but 'secondary_keys' is empty (prohibited by GEMINI.md §7)")
397: 
398:     return len(errors) == 0, errors
```
**Observation**: Lines 355-399 only validate `ignored_characters`, `ignored_personas`, and `selective` vs `secondary_keys`. There is **zero inspection** of `keys`, `secondary_keys`, or `nicknames` for umbrella keywords (`BROAD_KEYS`), completely omitting enforcement of `GEMINI.md §7`.

### 1.2 Verification of Rule Canon in Project Documentation
1. **`GEMINI.md §7` (Line 166)**:
   > "Divieto assoluto di tag generici (`solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega`, ecc.) sulle schede NPC per evitare l'attivazione massiva simultanea di oltre 100 voci."
2. **`Rule 08` (`.agents/rules/08_triage_lorebook_e_lexicon.md:80-81`)**:
   > "1. Zero Keyword Ombrello (`BROAD_KEYS`) sugli NPC:
   > È vietato assegnare tag geografici o tassonomici generici (`solarton`, `succ`, `blackwood`, `losangeles`, `underworld`, `vampire`, `werewolf`, `human`, `demihuman`, `demon`, `college`, `student`, `alpha`, `beta`, `omega`, `pack`) alle schede NPC del Lorebook. Tali keyword causerebbero l'attivazione simultanea di oltre 100 schede, prosciugando l'intero token budget. Le keyword degli NPC devono essere unicamente il nome, cognome, soprannomi e alias univoci del personaggio."
3. **`scripts/optimize_lorebooks.py:32-36`**:
   ```python
   BROAD_KEYS = {
       "solarton", "succ", "blackwood", "losangeles", "underworld",
       "vampire", "werewolf", "human", "demihuman", "demon",
       "college", "student", "alpha", "beta", "omega", "pack"
   }
   ```
4. **`tests/test_adversarial_npc_schema.py:31-35`**:
   ```python
   BROAD_KEYS = {
       "solarton", "succ", "blackwood", "losangeles", "underworld",
       "vampire", "werewolf", "human", "demihuman", "demon",
       "college", "student", "alpha", "beta", "omega", "pack"
   }
   ```

### 1.3 Empirical Execution of Adversarial Negative Test
Running `python -m unittest tests/test_adversarial_npc_schema.py`:
```
  [ADVERSARIAL VULNERABILITY FOUND] validate_anti_collision_contract allowed BROAD_KEYS ['alpha', 'werewolf', 'solarton'] without error!
  [ADVERSARIAL VULNERABILITY FOUND] avatar='https://' (bare scheme without domain/path) passed validation!
  [ADVERSARIAL VULNERABILITY FOUND] gallery_count=True passed validation because bool is subclass of int in Python!
  [ADVERSARIAL CRASH FOUND] validate_avatar_gallery_contract(entry='str') crashed with AttributeError: 'str' object has no attribute 'get'
  [ADVERSARIAL CRASH FOUND] validate_avatar_gallery_contract(lorebook_root=123) crashed with TypeError: argument of type 'int' is not a container or iterable
  [ADVERSARIAL CRASH FOUND] validate_entries_lexicon_parity(456) crashed with TypeError: argument of type 'int' is not a container or iterable
```
This confirms that passing `keys: ["alpha", "werewolf", "solarton"]` returned `(True, [])`.

### 1.4 Scan of Real Repository Files (`FINAL/`)
A diagnostic scan of `FINAL/Svartulfr_NPC_Primary.json` (99 entries) and `FINAL/Svartulfr_NPC_Secondary.json` (211 entries) for exact matches against `BROAD_KEYS`:
- `FINAL/Svartulfr_NPC_Primary.json`: **0** broad keys found across all `keys`, `secondary_keys`, and `nicknames`.
- `FINAL/Svartulfr_NPC_Secondary.json`: **1** entry matched:
  - `name`: `"Damien Bishop"`
  - `keys`: `["Damien", "Bishop", "Damien Bishop"]` (Clean)
  - `secondary_keys`: `["detective", "demon", "horns", "occult", "investigator"]` (Contains `"demon"`)
  This demonstrates that once `validate_anti_collision_contract` is hardened, the audit CLI tool (`scripts/verify_npc_schema_contract.py --all`) will accurately catalog Damien Bishop's `secondary_keys: demon` for Milestone 2 remediation, exactly as it already catalogs the missing root gallery in `Svartulfr_NPC_Primary.json`.

---

## 2. Logic Chain

1. **Premise 1**: `GEMINI.md §7` and `Rule 08 §4.1` state that generic umbrella keywords (`BROAD_KEYS`) are strictly prohibited on NPC lorebook entries to prevent context bloat and mass simultaneous activation of 100+ character cards.
2. **Premise 2**: As observed in §1.1, `validate_anti_collision_contract` completely omitted inspecting trigger keys or secondary keys.
3. **Premise 3**: As confirmed in §1.3, an entry with `keys: ["alpha", "werewolf", "solarton"]` passed validation with `(True, [])`, representing an empirical False Negative.
4. **Premise 4**: NPC lorebook entries define activation triggers in `keys` and contextual filters in `secondary_keys`. Top-level `nicknames` (and `npc_info.nicknames`) are also used by the Wyvern avatar parser. Any presence of an exact umbrella keyword in these fields causes unintended activation or speaker turn confusion.
5. **Premise 5**: Proper names frequently contain umbrella words as sub-components (e.g., `Roman Blackwood`, `Katarina Blackwood`, `Alpha Rivers`, `Douglas Pack`). A substring match (e.g., `bk in k`) would cause catastrophic False Positives, rejecting legitimate canonical NPCs. Therefore, **case-insensitive exact matching** on stripped strings (`k.strip().lower() in CANONICAL_BROAD_KEYS`) is required.
6. **Inference**: Hardening `validate_anti_collision_contract` requires:
   - Defining `CANONICAL_BROAD_KEYS` as a frozen set of the 17 authoritative umbrella terms.
   - Performing list-of-strings type checks on `entry.get("keys", [])`, `entry.get("secondary_keys", [])`, and `entry.get("nicknames", [])` / `npc_info.get("nicknames", [])`.
   - Iterating each token and asserting `k.strip().lower() not in CANONICAL_BROAD_KEYS`.
   - Adding explicit unit tests in `tests/test_npc_schema_contract.py` covering positive (compound names passing) and negative (exact broad keys failing) assertions.

---

## 3. Caveats

- **Scope Boundary**: As an Explorer agent, no modifications have been made to source code (`scripts/verify_npc_schema_contract.py` or `tests/test_npc_schema_contract.py`). All proposed changes are documented here for implementation by the SWE/contractor agent.
- **Milestone 2 Lorebook Data Remediation**: `FINAL/Svartulfr_NPC_Secondary.json` contains `Damien Bishop` with `secondary_keys: ["demon", ...]`. When the contract check is enabled, `scripts/verify_npc_schema_contract.py --check-files` will report this violation. This is expected behavior for Milestone 1 (R1 verification tooling), and the actual JSON file fix will occur in Milestone 2 (R2).

---

## 4. Conclusion & Actionable Fix Strategy

### 4.1 Canonical Set of `BROAD_KEYS`
Define in `scripts/verify_npc_schema_contract.py` at module level:

```python
CANONICAL_BROAD_KEYS = frozenset({
    "solarton",
    "succ",
    "blackwood",
    "losangeles",
    "underworld",
    "vampire",
    "werewolf",
    "human",
    "demihuman",
    "demi-human",
    "demon",
    "college",
    "student",
    "alpha",
    "beta",
    "omega",
    "pack",
})
```
*Rationale*:
- Exactly covers the 16 taxonomy and location keywords codified in `Rule 08 §4.1` and `GEMINI.md §7`, plus the standard hyphenated variant `demi-human`.
- Immutable `frozenset` guarantees $O(1)$ lookups and prevents accidental mutation.

### 4.2 Exact Implementation for `validate_anti_collision_contract`
Replace lines 355-399 in `scripts/verify_npc_schema_contract.py` with the following hardened logic:

```python
def validate_anti_collision_contract(entry: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Validates anti-collision preservation:
    - ignored_characters: list of str (Character Card IDs)
    - ignored_personas: list of str (Persona IDs)
    - selective: bool
    - secondary_keys: list of str
    - keys: list of str (no CANONICAL_BROAD_KEYS)
    - nicknames / npc_info.nicknames: list of str (no CANONICAL_BROAD_KEYS)
    Rules:
      * ignored_characters and ignored_personas must be lists of strings.
      * selective must be False unless secondary_keys is populated.
      * keys, secondary_keys, and nicknames must not contain generic umbrella keywords (GEMINI.md §7).
    """
    errors = []
    if not isinstance(entry, dict):
        return False, ["Entry must be a dictionary"]

    # 1. ignored_characters
    ic = entry.get("ignored_characters")
    if ic is not None:
        if not isinstance(ic, list):
            errors.append(f"'ignored_characters' must be a list, got {type(ic).__name__}")
        else:
            for i, item in enumerate(ic):
                if not isinstance(item, str):
                    errors.append(f"'ignored_characters[{i}]' must be a string card ID, got {type(item).__name__}")

    # 2. ignored_personas
    ip = entry.get("ignored_personas")
    if ip is not None:
        if not isinstance(ip, list):
            errors.append(f"'ignored_personas' must be a list, got {type(ip).__name__}")
        else:
            for i, item in enumerate(ip):
                if not isinstance(item, str):
                    errors.append(f"'ignored_personas[{i}]' must be a string persona ID, got {type(item).__name__}")

    # 3. selective vs secondary_keys
    selective = entry.get("selective", False)
    sec_keys = entry.get("secondary_keys", [])
    if not isinstance(sec_keys, list):
        errors.append(f"'secondary_keys' must be a list, got {type(sec_keys).__name__}")
    else:
        if selective and len(sec_keys) == 0:
            errors.append("Entry has 'selective: true' but 'secondary_keys' is empty (prohibited by GEMINI.md §7)")
        for i, k in enumerate(sec_keys):
            if not isinstance(k, str):
                errors.append(f"'secondary_keys[{i}]' must be a string, got {type(k).__name__}")
            elif k.strip().lower() in CANONICAL_BROAD_KEYS:
                errors.append(f"Prohibited broad umbrella keyword '{k.strip()}' found in 'secondary_keys' (GEMINI.md §7 violation)")

    # 4. keys inspection
    keys = entry.get("keys")
    if keys is not None:
        if not isinstance(keys, list):
            errors.append(f"'keys' must be a list, got {type(keys).__name__}")
        else:
            for i, k in enumerate(keys):
                if not isinstance(k, str):
                    errors.append(f"'keys[{i}]' must be a string, got {type(k).__name__}")
                elif k.strip().lower() in CANONICAL_BROAD_KEYS:
                    errors.append(f"Prohibited broad umbrella keyword '{k.strip()}' found in 'keys' (GEMINI.md §7 violation)")

    # 5. nicknames inspection (top-level and inside npc_info)
    nicknames = entry.get("nicknames")
    if nicknames is not None:
        if not isinstance(nicknames, list):
            errors.append(f"'nicknames' must be a list, got {type(nicknames).__name__}")
        else:
            for i, n in enumerate(nicknames):
                if not isinstance(n, str):
                    errors.append(f"'nicknames[{i}]' must be a string, got {type(n).__name__}")
                elif n.strip().lower() in CANONICAL_BROAD_KEYS:
                    errors.append(f"Prohibited broad umbrella keyword '{n.strip()}' found in 'nicknames' (GEMINI.md §7 violation)")

    npc_info = entry.get("npc_info")
    if isinstance(npc_info, dict):
        info_nicks = npc_info.get("nicknames")
        if isinstance(info_nicks, list):
            for i, n in enumerate(info_nicks):
                if isinstance(n, str) and n.strip().lower() in CANONICAL_BROAD_KEYS:
                    errors.append(f"Prohibited broad umbrella keyword '{n.strip()}' found in 'npc_info.nicknames' (GEMINI.md §7 violation)")

    return len(errors) == 0, errors
```

### 4.3 Co-Fixes Identified by Challenger 2
To eliminate all empirical crashes and vulnerabilities identified in `challenger_m1_2/handoff.md`, the implementer should also apply:

1. **In `validate_avatar_gallery_contract` (lines 313-335)**:
   ```python
   # Guard against non-dict root
   if lorebook_root is not None:
       if not isinstance(lorebook_root, dict):
           return False, ["Lorebook root must be a dictionary"]
       ...
       # Guard against boolean gallery_count (issubclass(bool, int) is True)
       if "gallery_count" not in lorebook_root:
           errors.append("Lorebook root missing 'gallery_count' property")
       elif isinstance(lorebook_root["gallery_count"], bool) or not isinstance(lorebook_root["gallery_count"], int) or lorebook_root["gallery_count"] < 0:
           errors.append(f"Lorebook root 'gallery_count' must be a non-negative integer, got {lorebook_root.get('gallery_count')}")

   # Guard against non-dict entry and bare https scheme
   if entry is not None:
       if not isinstance(entry, dict):
           return False, ["Entry must be a dictionary"]
       avatar = entry.get("avatar")
       if not avatar:
           errors.append("Entry missing 'avatar' field or avatar is empty")
       elif not isinstance(avatar, str):
           errors.append(f"Entry 'avatar' must be a string URL, got {type(avatar).__name__}")
       elif not avatar.startswith("https://") or len(avatar.strip()) <= 8:
           errors.append(f"Entry 'avatar' must be an HTTPS URL with domain, got: {avatar}")
   ```

2. **In `validate_entries_lexicon_parity` (lines 405-408)**:
   ```python
   if not isinstance(lorebook_data, dict):
       return False, ["Lorebook data must be a dictionary"]
   ```

### 4.4 Unit Tests to Add in `tests/test_npc_schema_contract.py`
Add the following test methods to class `TestAntiCollisionContract`:

```python
    def test_broad_umbrella_keys_in_keys_fails(self):
        """Rejects broad umbrella keywords in primary keys (GEMINI.md §7)."""
        entry = {
            "name": "Hugh Rivers",
            "keys": ["Hugh Rivers", "Alpha", "werewolf", "solarton"],
            "selective": False,
            "secondary_keys": []
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("Prohibited broad umbrella keyword 'Alpha' found in 'keys'" in e for e in errors))
        self.assertTrue(any("Prohibited broad umbrella keyword 'werewolf' found in 'keys'" in e for e in errors))
        self.assertTrue(any("Prohibited broad umbrella keyword 'solarton' found in 'keys'" in e for e in errors))

    def test_broad_umbrella_keys_in_secondary_keys_fails(self):
        """Rejects broad umbrella keywords in secondary_keys (GEMINI.md §7)."""
        entry = {
            "name": "Damien Bishop",
            "keys": ["Damien", "Bishop"],
            "selective": False,
            "secondary_keys": ["detective", "demon", "horns"]
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("Prohibited broad umbrella keyword 'demon' found in 'secondary_keys'" in e for e in errors))

    def test_broad_umbrella_keys_in_nicknames_fails(self):
        """Rejects broad umbrella keywords in top-level nicknames and npc_info.nicknames."""
        entry = {
            "name": "Student NPC",
            "keys": ["Student NPC"],
            "nicknames": ["student", "Freshman"],
            "npc_info": {
                "first_name": "Test",
                "nicknames": ["college"]
            }
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertFalse(valid)
        self.assertTrue(any("Prohibited broad umbrella keyword 'student' found in 'nicknames'" in e for e in errors))
        self.assertTrue(any("Prohibited broad umbrella keyword 'college' found in 'npc_info.nicknames'" in e for e in errors))

    def test_compound_names_containing_broad_substrings_pass(self):
        """Ensures exact matching prevents false positives on legitimate compound proper names."""
        entry = {
            "name": "Roman Blackwood",
            "keys": ["Roman Blackwood", "Roman", "Alpha Rivers", "Douglas Pack"],
            "secondary_keys": ["Blackwood Heir", "Alpha of the Douglas Pack"],
            "selective": False
        }
        valid, errors = validate_anti_collision_contract(entry)
        self.assertTrue(valid, f"False positive rejection of valid compound names: {errors}")
        self.assertEqual(len(errors), 0)

    def test_case_insensitive_and_whitespace_broad_keys_matching(self):
        """Verifies case-insensitive and stripped matching for broad keys."""
        for raw_key in ["  ALPHA  ", "sUcC", "WEREWOLF", "Demihuman", "demi-human"]:
            entry = {"keys": [raw_key]}
            valid, errors = validate_anti_collision_contract(entry)
            self.assertFalse(valid, f"Expected {repr(raw_key)} to be caught")
            self.assertTrue(any("Prohibited broad umbrella keyword" in e for e in errors))

    def test_malformed_keys_and_nicknames_types_fail(self):
        """Verifies type safety for keys and nicknames."""
        entry_str_keys = {"keys": "NotAList"}
        valid, errors = validate_anti_collision_contract(entry_str_keys)
        self.assertFalse(valid)
        self.assertTrue(any("'keys' must be a list" in e for e in errors))

        entry_bad_elem = {"keys": ["Valid", 123]}
        valid, errors = validate_anti_collision_contract(entry_bad_elem)
        self.assertFalse(valid)
        self.assertTrue(any("'keys[1]' must be a string" in e for e in errors))
```

### 4.5 Self-Test Suite Update in `scripts/verify_npc_schema_contract.py`
In `run_self_tests()`, update `invalid_ac_cases` to include:
```python
    invalid_ac_cases = [
        ({"ignored_characters": "not_a_list"}, "ignored_characters string"),
        ({"ignored_personas": [123]}, "ignored_personas non-string"),
        ({"selective": True, "secondary_keys": []}, "selective without secondary_keys"),
        ({"keys": ["alpha"]}, "broad umbrella key in keys"),
        ({"secondary_keys": ["werewolf"]}, "broad umbrella key in secondary_keys"),
        ({"nicknames": ["student"]}, "broad umbrella key in nicknames"),
        ({"keys": "not_a_list"}, "keys string"),
        ({"keys": [123]}, "keys non-string element"),
    ]
```
And add an assertion that a compound proper name entry passes:
```python
    valid_compound_entry = {
        "keys": ["Roman Blackwood", "Alpha Rivers"],
        "secondary_keys": ["Blackwood Heir"],
        "selective": False
    }
    ok, errs = validate_anti_collision_contract(valid_compound_entry)
    assert ok, f"Expected valid compound entry to pass, got: {errs}"
    print("  [PASS] Legitimate compound names with broad substrings passed without false positives.")
```

---

## 5. Verification Method

To independently verify the implementation:

1. **Run Unit Tests**:
   ```powershell
   python -m unittest tests/test_npc_schema_contract.py
   ```
   *Expected Result*: All existing tests plus the 6 new unit tests pass (54+ passed tests).

2. **Run Adversarial Stress Test Suite**:
   ```powershell
   python -m unittest tests/test_adversarial_npc_schema.py
   ```
   *Expected Result*: 34 passed tests, with ZERO `[ADVERSARIAL VULNERABILITY FOUND]` or `[ADVERSARIAL CRASH FOUND]` diagnostic messages.

3. **Run Verification Tool CLI Self-Tests**:
   ```powershell
   python scripts/verify_npc_schema_contract.py --self-test
   ```
   *Expected Result*: Exits 0, reporting all contract self-tests passed including Contract 4 broad keys enforcement and zero compound false positives.

4. **Run Verification Tool File Audit**:
   ```powershell
   python scripts/verify_npc_schema_contract.py --check-files
   ```
   *Expected Result*: Successfully runs without unhandled exceptions; identifies expected Milestone 2 catalog items (`Primary`: missing gallery root; `Secondary`: Damien Bishop `secondary_keys: demon`).
