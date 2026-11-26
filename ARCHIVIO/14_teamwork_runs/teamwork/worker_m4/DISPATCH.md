# Task Assignment: Milestone 4 — Comprehensive Verification, Parity & CHANGELOG.md

## Objective
Finalize the end-to-end integration of emergent lore across the entire repository:
1. Run the entire suite of verification, regression, and test scripts.
2. Fix the minor pre-existing entry ID collision in `FINAL/Svartulfr_Lorebook_III.json` and its mirror `lorebooks/optimized/Svartulfr_Lorebook_III.json`:
   - Rename entry #40 (`Partita di Campionato Ice Hockey: SUCC Bears`) from `event_partita_di_campionato_` to `event_partita_di_campionato_hockey`.
   - Maintain 100% byte-for-byte parity `entries == lexicon` in both files.
3. Update `CHANGELOG.md` with an exhaustive, beautifully structured entry documenting the complete integration across all tiers.
4. Execute full repository health checks (`scripts/vault_health_check.py`, `tests/`, etc.).

## Inputs & Context
- `PROJECT.md`
- `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md`
- Milestone 1, 2, and 3 handoffs and verification scripts.

## Scope & File Ownership
You have exclusive write ownership of:
- `FINAL/Svartulfr_Lorebook_III.json` (entry #40 ID rename + parity)
- `lorebooks/optimized/Svartulfr_Lorebook_III.json` (entry #40 ID rename + parity)
- `CHANGELOG.md`
- `scripts/verify_milestone4_full_regression.py` (comprehensive regression runner)

## Required Test Execution
Run and report verbatim output for:
1. `python scripts/verify_milestone_1.py`
2. `python scripts/test_milestone_1_adversarial.py`
3. `python scripts/verify_milestone2_lorebooks.py`
4. `python scripts/verify_milestone3_cards_personas.py`
5. `python scripts/verify_npc_schema_contract.py --all`
6. `python scripts/verify_marks_and_images.py`
7. `python scripts/vault_health_check.py`
8. `python -m unittest discover tests`

## Formatting & Integrity Disciplines
- **Zero Em-Dashes (`—`)**: In all additions to `CHANGELOG.md` and modified lorebook entries. Use commas or periods.
- **Parity Invariant**: `FINAL/Svartulfr_Lorebook_III.json` and its mirror must maintain `entries == lexicon` byte-for-byte.
- **Positive Framing**: No negative framing tokens.
- **CHANGELOG Entry**: Must be placed at the top of `CHANGELOG.md` under a clear version/date header (e.g. `## [Unreleased] - 2026-11-02` or `## [1.2.0] - 2026-11-02: Emergent Lore & St. Brugge Integration`).

## MANDATORY INTEGRITY WARNING
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Completion Criteria
- All tests pass with 100% success rate.
- `CHANGELOG.md` fully updated.
- Duplicate entry ID resolved with exact parity preserved.
- Deliver full report to `.agents/teamwork/worker_m4/handoff.md`.

## 2026-11-02T07:47:33Z
[Message] timestamp=2026-11-02T07:47:33Z sender=a6280f2d-32ae-4a10-82fa-5604ad40f230 priority=MESSAGE_PRIORITY_HIGH
You are worker_m4, assigned to Milestone 4: Comprehensive Verification, Schema Parity & CHANGELOG.md for Svartúlfr Verse.

Your working directory is: `e:\repository\SvartulfrVerse\.agents\teamwork\worker_m4\`

You MUST first read:
1. `e:\repository\SvartulfrVerse\.agents\teamwork\worker_m4\DISPATCH.md`
2. `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md`
3. `e:\repository\SvartulfrVerse\PROJECT.md`

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

SCOPE & EXCLUSIVE WRITE OWNERSHIP:
- `FINAL/Svartulfr_Lorebook_III.json`
- `lorebooks/optimized/Svartulfr_Lorebook_III.json`
- `CHANGELOG.md`
- `scripts/verify_milestone4_full_regression.py`

TASKS:
1. Fix the minor pre-existing duplicate ID in `FINAL/Svartulfr_Lorebook_III.json` and `lorebooks/optimized/Svartulfr_Lorebook_III.json`:
   - Rename entry #40 (`Partita di Campionato Ice Hockey: SUCC Bears`) from `event_partita_di_campionato_` to `event_partita_di_campionato_hockey`.
   - Ensure `entries == lexicon` byte-for-byte in both files.
2. Update `CHANGELOG.md` with an exhaustive entry documenting the full integration of emergent lore across Vault, Lorebooks, Cards, and Personas (St. Brugge Private Academy, Father Revazhael, Applied Crystallography, Resonant Cylinders, Abyssal Magic, Alyssa & Jasper credentials/reputation, Suite 3 dynamics, DCC security).
   - Strict 0 em-dashes (`—`) in your additions! Use commas or periods.
3. Author and execute `scripts/verify_milestone4_full_regression.py` running the complete regression battery:
   - `python scripts/verify_milestone_1.py`
   - `python scripts/test_milestone_1_adversarial.py`
   - `python scripts/verify_milestone2_lorebooks.py`
   - `python scripts/verify_milestone3_cards_personas.py`
   - `python scripts/verify_npc_schema_contract.py --all`
   - `python scripts/verify_marks_and_images.py`
   - `python scripts/vault_health_check.py`
   - `python -m unittest discover tests`
4. Deliver your handoff report to `e:\repository\SvartulfrVerse\.agents\teamwork\worker_m4\handoff.md` and send a message when complete.
