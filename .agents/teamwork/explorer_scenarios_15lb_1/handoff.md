# Handoff Report: Local Scenarios Investigation (15 Lorebooks & Persona IDs)

**Agent**: Explorer 1 (Local Scenarios Explorer)  
**Recipient**: Orchestrator (`ad7893ee-522b-4d55-8280-5903a5dd60f6`)  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_1`  
**Date**: 2026-10-20  
**Handoff Type**: Hard (Task Complete)  

---

## 1. Observation

Direct programmatic and inspection observations across the target scenario files in `e:\repository\SvartulfrVerse`:

### Observation 1.1: File Locations and Current Lorebook Counts
Tool Command:
`python .agents/teamwork/explorer_scenarios_15lb_1/inspect_summary.py`
Results:
- `FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json` (ID: `char_scenario_nLC84wrHdrbB6P3DEhwKb`):
  `lorebook_ids` count: 6 (`['_gwwCxCfQ6PQaLEjAQVpJL', '_HfG7TeV6MJyj6bxMwxkpt', '_9zWTGqYJNJ4BCDMj8gfcD', '_EjXxkmPVhpCXg8xABpFkK', '_zwEqgEEzh12X6gHVmMKKC', '_Uht3Ckz44JBDrPnUHq7LV']`). Missing: 9 realism IDs (`_GV1KyHVY1RMbCnWgLkzDG`, `_GbWJbkhgLzWexMHrjyUUc`, `_FaVcHfmrqcaJq8pa3WmRw`, `_BbrRgrcdGPMLEbBU2b6xk`, `_gchmML4Q478zdFjhXf8rN`, `_brNyzEdhzNAyxK8xC8hhm`, `_YtKLMTwyMxNf1DNYqBx1t`, `_b9HgpUXtAW8VmTy82BPDV`, `_c8bEm1bWphwqFBXWRPrV8`).
- `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json` (ID: `char_scenario_CKgwq246DyCj1NNTBV9rt`):
  `lorebook_ids` count: 6. Missing the same 9 realism IDs.
- `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json` (ID: `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`):
  `lorebook_ids` count: 6. Missing the same 9 realism IDs.
- `FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json` (ID: `char_scenario_88N1eQXqkbydKX9q9XQzp`):
  `lorebook_ids` count: 6. Missing the same 9 realism IDs.
- `FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json` (ID: `char_scenario_eqtRNnDpKbxDp7dmJmq6E`):
  `lorebook_ids` count: 6. Missing the same 9 realism IDs.
- `FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json` (ID: `char_scenario_rrUCdBPH6WTNyBnQkMAKR`):
  `lorebook_ids` count: 6. Missing the same 9 realism IDs.
- `FINAL/Svartulfr_Master_Scenario.json` (ID: `char_scenario_1DC43ggb6mB8YLJDJKrU4`):
  `lorebook_ids` count: 15. Set difference against target 15 canonical IDs is `set()`. Order is non-canonical (`_GbWJ...` starts first).

### Observation 1.2: Greetings Schema and Persona Placement
Tool Command:
`python .agents/teamwork/explorer_scenarios_15lb_1/inspect_greeting_schema.py`
Results:
- In all 6 files in `FINAL/scenarios/`:
  Greeting object keys: `['id', 'name', 'description', 'messages', 'speaker_slot', 'content', 'linked_persona_ids']`.
  `linked_persona_ids` is at greeting root level as `<class 'list'>`. In every greeting of the 6 files, it is initialized to `[]`.
  `linked_personas` does not exist in the 6 thematic scenario files (`linked_personas in greeting: False`).
- In `FINAL/Svartulfr_Master_Scenario.json`:
  Greeting object keys: `['messages', 'id', 'name', 'description', 'content', 'linked_persona_ids', 'speaker_slot', 'linked_personas']`.
  Both `linked_persona_ids` and `linked_personas` exist.

### Observation 1.3: Master Scenario Greetings Breakdown
Tool Command:
`python .agents/teamwork/explorer_scenarios_15lb_1/catalog_master_greetings.py`
Results:
Total greetings: 29.
- `[FemPOV]` greetings: 7 (indices: 2, 7, 8, 12, 16, 20, 28). Currently have `linked_persona_ids: ['persona_1786335754946']`.
- `[MalePOV]` greetings: 6 (indices: 3, 6, 9, 17, 18, 21). Currently have `linked_persona_ids: ['1792155173728']`.
- Shared / Neutral greetings: 16 (indices: 0, 1, 4, 5, 10, 11, 13, 14, 15, 19, 22, 23, 24, 25, 26, 27). Currently have `linked_persona_ids: []`.

### Observation 1.4: Persona Identifier Format
Verified across existing entries in `FINAL/Svartulfr_Master_Scenario.json`:
- Alyssa Persona ID: `"persona_1786335754946"`
- Jasper Persona ID: `"1792155173728"`

---

## 2. Logic Chain

1. **Premise 1 (R1 Scope)**: Requirement R1 mandates assigning the unified suite of 15 Lorebook IDs to all 7 scenarios (Observation 1.1).
2. **Inference 1**: The 6 thematic scenario files (`Camp_Mystic`, `SUCC_Route_Alyssa`, `SUCC_Route_Jasper`, `Villa_Douglas`, `DMHA_Dungeons`, `Underworld_Sindacato`) must have their `lorebook_ids` expanded from 6 to the 15 canonical IDs in order. `Svartulfr_Master_Scenario.json` must have its 15 IDs reordered to match the canonical sequence.
3. **Premise 2 (R2 Scope)**: Requirement R2 mandates configuring `linked_persona_ids` for "Offer a persona to play as" at the greeting level across all scenarios (Observation 1.2).
4. **Inference 2 (Dual Scenarios)**: For `Camp_Mystic`, `Villa_Douglas`, `DMHA_Dungeons`, and `Underworld_Sindacato`, all greetings must be configured with `linked_persona_ids: ["persona_1786335754946", "1792155173728"]`.
5. **Inference 3 (Single Routes)**: For `SUCC_Route_Alyssa`, all 6 greetings must have `linked_persona_ids: ["persona_1786335754946"]`. For `SUCC_Route_Jasper`, all 5 greetings must have `linked_persona_ids: ["1792155173728"]`.
6. **Inference 4 (Master Scenario)**: For `Svartulfr_Master_Scenario.json`, the 16 shared/neutral greetings must be updated from `[]` to `["persona_1786335754946", "1792155173728"]` (and their `linked_personas` array populated with both persona objects), while the 7 `[FemPOV]` and 6 `[MalePOV]` greetings remain untouched as single-persona greetings (Observation 1.3).

---

## 3. Caveats

1. **Remote Cloud API State**: This investigation focused on the local JSON files in `FINAL/scenarios/` and `FINAL/`. The live API state on Wyvern must be queried with `GET /api/character-scenarios/:id` prior to `PUT` execution by the worker to capture the latest cloud `revision` counter and avoid HTTP 409 Conflict.
2. **`linked_personas` Object Cache**: In `FINAL/Svartulfr_Master_Scenario.json`, `linked_personas` contains persona display metadata (avatar URL, name, title). While the Wyvern API primarily evaluates `linked_persona_ids`, maintaining matching `linked_personas` objects locally ensures full consistency between local files and live API responses.
3. **Formatting Integrity**: Zero em-dashes (`—`) were found in greeting content across all 6 thematic scenario files (8 em-dashes exist only in top-level title, comment, and prompt metadata of Master Scenario). No narrative edits are required; updates are strictly structural to `lorebook_ids`, `linked_persona_ids`, and `linked_personas`.

---

## 4. Conclusion

All 7 scenario files have been fully mapped, analyzed, and structurally verified. The required modifications are unambiguous and completely deterministic:
1. **Lorebooks**: Update `lorebook_ids` to the exact 15 canonical IDs in all 7 files.
2. **Dual Scenarios (4 files, 17 greetings total)**: Set `linked_persona_ids = ["persona_1786335754946", "1792155173728"]` on all greetings in `Camp_Mystic` (4), `Villa_Douglas` (5), `DMHA_Dungeons` (4), and `Underworld_Sindacato` (4).
3. **Single Route Alyssa (1 file, 6 greetings)**: Set `linked_persona_ids = ["persona_1786335754946"]` on all 6 greetings in `SUCC_Route_Alyssa`.
4. **Single Route Jasper (1 file, 5 greetings)**: Set `linked_persona_ids = ["1792155173728"]` on all 5 greetings in `SUCC_Route_Jasper`.
5. **Master Scenario (1 file, 29 greetings)**: Update the 16 shared greetings to `linked_persona_ids = ["persona_1786335754946", "1792155173728"]` (and matching `linked_personas`), while preserving the 7 `[FemPOV]` (`["persona_1786335754946"]`) and 6 `[MalePOV]` (`["1792155173728"]`) greetings.

---

## 5. Verification Method

To independently verify the local scenario files before and after modifications:

```bash
# 1. Verify Lorebook IDs length and content across all 7 scenarios
python -c "
import json
canonical = ['_gwwCxCfQ6PQaLEjAQVpJL', '_HfG7TeV6MJyj6bxMwxkpt', '_9zWTGqYJNJ4BCDMj8gfcD', '_EjXxkmPVhpCXg8xABpFkK', '_Uht3Ckz44JBDrPnUHq7LV', '_zwEqgEEzh12X6gHVmMKKC', '_GV1KyHVY1RMbCnWgLkzDG', '_GbWJbkhgLzWexMHrjyUUc', '_FaVcHfmrqcaJq8pa3WmRw', '_BbrRgrcdGPMLEbBU2b6xk', '_gchmML4Q478zdFjhXf8rN', '_brNyzEdhzNAyxK8xC8hhm', '_YtKLMTwyMxNf1DNYqBx1t', '_b9HgpUXtAW8VmTy82BPDV', '_c8bEm1bWphwqFBXWRPrV8']
files = [
    'FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json',
    'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json',
    'FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json',
    'FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json',
    'FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json',
    'FINAL/Svartulfr_Master_Scenario.json'
]
for f in files:
    d = json.load(open(f, encoding='utf-8'))
    assert d.get('lorebook_ids') == canonical, f'Lorebook mismatch in {f}'
print('All 7 scenarios match 15 canonical lorebook IDs perfectly!')
"

# 2. Verify Persona IDs assignments across greetings
python -c "
import json
alyssa = 'persona_1786335754946'
jasper = '1792155173728'

# Test dual scenarios
for f in ['Camp_Mystic', 'Villa_Douglas', 'DMHA_Dungeons', 'Underworld_Sindacato']:
    d = json.load(open(f'FINAL/scenarios/Svartulfr_Scenario_{f}.json', encoding='utf-8'))
    for g in d['greetings']:
        assert set(g['linked_persona_ids']) == {alyssa, jasper}, f'Dual error in {f} {g[\"id\"]}'

# Test single Alyssa route
d = json.load(open('FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json', encoding='utf-8'))
for g in d['greetings']:
    assert g['linked_persona_ids'] == [alyssa], f'Alyssa error in {g[\"id\"]}'

# Test single Jasper route
d = json.load(open('FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json', encoding='utf-8'))
for g in d['greetings']:
    assert g['linked_persona_ids'] == [jasper], f'Jasper error in {g[\"id\"]}'

# Test Master scenario
d = json.load(open('FINAL/Svartulfr_Master_Scenario.json', encoding='utf-8'))
for g in d['greetings']:
    if '[FemPOV]' in g['name']:
        assert g['linked_persona_ids'] == [alyssa]
    elif '[MalePOV]' in g['name']:
        assert g['linked_persona_ids'] == [jasper]
    else:
        assert set(g['linked_persona_ids']) == {alyssa, jasper}
print('All greetings across all 7 scenarios verified successfully!')
"
```

Invalidation Condition:
If any scenario has fewer than 15 lorebook IDs, if any dual greeting does not offer both personas, or if any single route greeting contains the wrong persona ID, verification fails.
