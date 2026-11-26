## 2026-10-24T10:41:32Z

You are an Explorer agent (explorer_m1_it2_2).
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_it2_2
You MUST read e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md before doing anything else.

Context & Failure Output:
- e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (MANDATORY)
- e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_8\PROJECT.md
- e:\repository\SvartulfrVerse\GEMINI.md (see §7 Triage Import Lorebook ed Architettura Lexicon World - Zero Keyword Ombrello BROAD_KEYS)
- Challenger 2 Handoff: e:\repository\SvartulfrVerse\.agents\teamwork\challenger_m1_2\handoff.md
- Target file: scripts/verify_npc_schema_contract.py and tests/test_npc_schema_contract.py

Failure Details:
`validate_anti_collision_contract` completely omitted checking for generic umbrella keywords (`BROAD_KEYS`) on NPC entries, violating GEMINI.md §7:
"Divieto assoluto di tag generici (`solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega`, ecc.) sulle schede NPC per evitare l'attivazione massiva simultanea di oltre 100 voci."

Task:
Analyze and formulate the exact fix strategy for `validate_anti_collision_contract`:
- Define the canonical set of `BROAD_KEYS` per GEMINI.md §7.
- Specify how `validate_anti_collision_contract` should inspect `entry.get("keys", [])` and `entry.get("secondary_keys", [])` (and `entry.get("nicknames", [])` if applicable) for case-insensitive exact matches against `BROAD_KEYS`.
- Detail the exact error messages and unit tests to add in `tests/test_npc_schema_contract.py`.
Write your report to e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_it2_2\handoff.md.
Do NOT modify source files. You are read-only exploration. Send completion message using send_message.
