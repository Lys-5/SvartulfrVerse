## 2026-10-24T10:49:26Z

You are Worker agent for Milestone 1 Iteration 2 (worker_m1_it2).
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\worker_m1_it2
You MUST read e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md before doing anything else.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Context & Explorer Handoff Reports to read:
- e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (MANDATORY)
- e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_8\PROJECT.md
- e:\repository\SvartulfrVerse\GEMINI.md
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_it2_1\handoff.md (Whitespace regex normalization & middle_names fix)
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_it2_2\handoff.md (CANONICAL_BROAD_KEYS anti-collision fix)
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_it2_3\handoff.md (Type guards, boolean check, and URL netloc fix)

Exclusive Write Ownership:
- scripts/verify_npc_schema_contract.py
- tests/test_npc_schema_contract.py
- e:\repository\SvartulfrVerse\.agents\teamwork\worker_m1_it2\handoff.md
Do NOT modify FINAL/*.json in this turn.

Task:
Implement the verified remediation strategies in `scripts/verify_npc_schema_contract.py` and `tests/test_npc_schema_contract.py`:
1. `detect_duplicate_surnames`: Add pre-normalization of backslash-escaped whitespace (`\ `), regex whitespace tokens (`\s+`), and quote/hyphen classes per explorer_m1_it2_1. Ensure it cleanly catches all 20 legacy duplicate surname entries in FINAL/ while giving 0 false positives on valid entries.
2. `validate_npc_info_schema`: Enforce that `"middle_names"` MUST be present in `npc_info`, must not be None, and must be an `isinstance(..., list)`.
3. `validate_anti_collision_contract`: Add `CANONICAL_BROAD_KEYS` (17 terms: solarton, succ, blackwood, losangeles, underworld, vampire, werewolf, human, demihuman, demi-human, demon, college, student, alpha, beta, omega, pack) per explorer_m1_it2_2 and verify exact case-insensitive matches on keys, secondary_keys, and nicknames.
4. `validate_avatar_gallery_contract`:
   - Add type guards on non-dict `entry` and `lorebook_root`.
   - Reject boolean `gallery_count`: `isinstance(gc, bool) or not isinstance(gc, int) or gc < 0`.
   - Add `is_valid_https_url` ensuring non-empty netloc and real domain labels (rejecting bare `https://`).
5. `validate_entries_lexicon_parity`:
   - Add type guard for non-dict `lorebook_data`.
6. Add unit test cases in `tests/test_npc_schema_contract.py` covering all hardened contracts and new tests.
7. Run tests with `python tests/test_npc_schema_contract.py` and `uv run --with pytest --with regex pytest tests/test_npc_schema_contract.py -v`.
8. Run CLI verifier: `python scripts/verify_npc_schema_contract.py --all`.
9. Document commands, exact outputs, and verification in `e:\repository\SvartulfrVerse\.agents\teamwork\worker_m1_it2\handoff.md`.
10. Send completion message using send_message.
