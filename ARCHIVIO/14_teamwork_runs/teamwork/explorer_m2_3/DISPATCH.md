## 2026-10-24T11:14:30Z
You are an Explorer agent for Milestone 2 (explorer_m2_3).
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m2_3
You MUST read e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md before doing anything else.

Context:
- e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (MANDATORY)
- e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_8\PROJECT.md
- e:\repository\SvartulfrVerse\GEMINI.md
- Skill: e:\repository\SvartulfrVerse\.agents\skills\wyvern-card-lorebook-sync\SKILL.md
- Verifier: scripts/verify_npc_schema_contract.py

Task:
Design the automated mass remediation and live deployment pipeline for Milestone 2:
1. Specify the architecture of `scripts/remediate_lorebook_npcs.py`:
   - How it reads `FINAL/Svartulfr_NPC_Primary.json` and `FINAL/Svartulfr_NPC_Secondary.json`.
   - How it extracts clean name components from JED+ blocks (parsing `[NAME: First (Middle) Last; ...]` or explicit dossiers).
   - How it populates `npc_info` (`first_name`, `middle_names: list`, `last_name`, `nicknames: list`, `titles: list`, `npc_prefix: ""`).
   - How it fixes duplicate surname regexes and strips umbrella keys.
   - How it ensures root `gallery: []` and `gallery_count: 0`.
   - How it propagates 100% byte-for-byte identical data to `entries` and `lexicon` in `FINAL/` and `lorebooks/optimized/`.
2. Specify the live deployment PUT sequence:
   - How it authenticates via Wyvern JWT token (from `scratch/refresh_token.py` or existing token).
   - How it sends `PUT /api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` and `PUT /api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV` sending the clean `lexicon` payload without hitting HTTP 413.
3. Write your complete handoff report to e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m2_3\handoff.md.
Do NOT modify source files. You are read-only exploration. Send completion message using send_message.
