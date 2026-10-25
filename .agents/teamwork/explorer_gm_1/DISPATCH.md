# DISPATCH — Explorer GM 1 (Assistant Architecture & Wyvern API)
Role: teamwork_preview_explorer
Target: Investigate Standalone Assistant schema, Wyvern API endpoints, lorebook bindings, and existing scripts/references.

## 2026-10-20T17:23:34Z
[Message] timestamp=2026-10-20T17:23:34Z sender=6c88066a-eba8-41aa-adf7-8e00569a9154 priority=MESSAGE_PRIORITY_HIGH content=You are Explorer GM 1 (Assistant Architecture Explorer).
Working Directory: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_1
Authoritative Request: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (section "## Follow-up — 2026-10-20T17:19:55Z").
Project Scope: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_3\PROJECT.md.
Core rules: GEMINI.md, AGENTS.md.

OBJECTIVE:
Investigate how standalone Assistants in Wyvern Chat (/mine > ASSISTANT) are defined, structured, and deployed via Wyvern Web API or client-side storage:
1. Inspect the Wyvern API endpoint for assistants. Is it /api/assistants, /api/characters?type=assistant, /api/mine/assistants, or similar? Check scratch/, scripts/, or perform safe read-only API inspection with scratch/wyvern_token.txt (or curl/python script if needed, or inspect browser network logs/endpoints).
2. Determine the exact JSON payload schema required to create an Assistant named "Svartúlfr — Game Master & World Engine":
   - System prompt schema / field names
   - Final instructions / post_history_instructions field names
   - Lorebook attachments schema (how the 6 lorebook IDs: _gwwCxCfQ6PQaLEjAQVpJL, _HfG7TeV6MJyj6bxMwxkpt, _9zWTGqYJNJ4BCDMj8gfcD, _EjXxkmPVhpCXg8xABpFkK, _zwEqgEEzh12X6gHVmMKKC, _Uht3Ckz44JBDrPnUHq7LV are linked: e.g. lorebook_ids, linked_lorebooks, etc.)
   - D20 + S.P.E.C.I.A.L. (STR, PER, END, CHA, INT, AGI, LCK) skill check resolution engine specification and isolated diegetic formatting > [TEST: ...].
   - Canon rules (Italian Sandwich language enforcement, third-person present tense, anti-puppeting of {{user}}, thought privacy, multi-NPC dialogue format Nome: "...").
3. Check if any existing Assistant payloads or scripts exist in FINAL/, ARCHIVIO/, scratch/, or scripts/.

BOUNDARIES:
- Read-only investigation. Do NOT deploy or modify project files.
- Write your comprehensive findings to e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_1\analysis.md and a structured handoff.md.
- Signal completion back to parent via send_message with handoff path.
