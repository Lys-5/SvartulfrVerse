# Dispatch Log — orchestrator_12

## 2026-10-25T12:18:07Z

You are orchestrator_12, Project Orchestrator for the Svartúlfr Verse project.

Your dedicated working directory is:
e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_12

Project root directory:
e:\repository\SvartulfrVerse

The authoritative user request is recorded in:
e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
under the timestamp header `## 2026-10-25T12:18:07Z`:

"Correct and complete all 125 World Characters in Wyvern World `_YpX47fNraQFw2dD7TdycJ`, then remove leftover NPC entries from that World's Lexicon.

Working directory: e:\repository\SvartulfrVerse
Integrity mode: development

Context: project rules in GEMINI.md and .agents/rules/ are binding. Auth token via `scripts/sync_from_wyvern_web.py:get_auth_token()`. API routes: GET /api/worlds/characters/world/<world_id>, GET/PUT/DELETE /api/worlds/characters/<id>, same pattern for /api/worlds/lexicon. Known traps (ARCHIVIO/03_Claude_Docs_and_Memories/claude_project_docs/Wyvern_API_Metodo_Scrittura.md and Atlas_Teague_Bug_Character_Bloccato_2026-09-14.md): a PUT with the full object returns 200 and writes nothing, so use PARTIAL PUT bodies with only changed fields and verify with GET; birthdate/start_timeline_position must be INTEGER world-hours (epoch 21 Dec 827 UTC), never ISO strings (ISO strings corrupted a whole world before); RPG level >= 100 silently blocks saving, cap at 99; passing species/occupation objects on POST caused HTTP 500. The 6 standalone Lorebooks (_gwwCxCfQ6PQaLEjAQVpJL, _HfG7TeV6MJyj6bxMwxkpt, _9zWTGqYJNJ4BCDMj8gfcD, _EjXxkmPVhpCXg8xABpFkK, _zwEqgEEzh12X6gHVmMKKC, _Uht3Ckz44JBDrPnUHq7LV) must NOT be modified. Canonical sources: lorebooks/optimized/*.json (JED+ NPC entries), FINAL/ cards, scratch/rpg_full_snapshots/, scratch/rpg_snapshots/.

## Requirements

### R1. Backup first
Before any write, save a complete JSON snapshot of all World Characters and the full World Lexicon of `_YpX47fNraQFw2dD7TdycJ` under scratch/.

### R2. Remove duplicates
Keep the complete record and delete the empty one (known case: Finnegan Novak, keep `_Yk9aK6X9WHzrWPCT7mzEK`, delete `_7Lkgnm4GyaPTrYfNGn1YT`). Same rule for any other duplicate found.

### R3. Missing-data gate (no invention)
Use only data present in canonical sources. For every character lacking data needed for a field (age/birthdate, enough dossier for RPG stats, enough appearance info for outfits), do NOT invent: collect them into a single file scratch/missing_data.md (one row per character, listing the missing fields) and report back to the parent agent so the user can fill it. Continue with all characters that have complete data.

### R4. Complete every character with sufficient data
Each must have: rpg_stats with 6 stats (might, resilience, agility, wit, presence, scouting; base 1 each, 25 points distributed, sum 31) and level = age capped at 99; birthdate == start_timeline_position as integer <= 10486470; pronouns; activation keys (name/surname/aliases, no umbrella keys like solarton, succ, blackwood, vampire, werewolf, student, alpha, omega); summary and long_summary derived from JED+; at least 9 contextual outfits per GEMINI.md §4 (casual, business/campus, gala/formal, party/club, beach/terme, sleep, nude, hybrid shift/mutation, full shift/other). Text rules: no em-dash, no markdown/asterisk bold, no {{age}} macro. Respect anatomy rules (single pair of animal ears for demi-humans; Sierra Cruz has no legs; Scarlett Rose candy-pink hair/eyes, scarlet horns).

### R5. Clean the World Lexicon
Delete NPC entries in the World Lexicon of `_YpX47fNraQFw2dD7TdycJ` only if a matching World Character verifiably exists. NPC entries without a matching character stay; list them in the final report.

### R6. Live verification
Validate with Chrome DevTools via CDP (port and ws path in %LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort) on https://app.wyvern.chat/sim/chat_log_PJx1W1rg3WUzRM7MnQrkN: Stats tab shows character sheets, no console errors, no failed network calls.

## Acceptance Criteria
- [ ] Snapshot exists and predates the first write
- [ ] 0 duplicate display_names among World Characters
- [ ] An independent verification script re-reads the API and confirms, for every non-blocked character: 6 stats summing to 31, level <= 99, birthdate == start_timeline_position integer <= 10486470, pronouns set, keys set with no umbrella keys, non-empty summary, >= 9 outfits
- [ ] 0 em-dashes, 0 `**`, 0 `{{age}}` in written text fields
- [ ] 0 NPC entries in the World Lexicon that match an existing World Character
- [ ] scratch/missing_data.md lists every blocked character; final report lists remaining unmatched NPC lexicon entries
- [ ] Standalone Lorebooks unchanged (verify updated_at before/after)
- [ ] /sim Stats tab populated, 0 console errors"

Follow the project rules in GEMINI.md and AGENTS.md. Maintain your persistent BRIEFING.md and progress.md in your working directory.
Decompose the mission into milestones, dispatch tasks to specialist subagents, verify deliverables, and communicate completion back to Sentinel.


## 2026-10-25T12:20:36Z

[Message from Parent 253c8c2b-c32d-4468-9518-9f9c0b020a7b]:
You are orchestrator_12, Project Orchestrator for the Svartúlfr Verse project.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_12
The full request and instructions are detailed in your working directory at e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_12\DISPATCH.md and in e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md under header ## 2026-10-25T12:18:07Z.

Mission:
Correct and complete all 125 World Characters in Wyvern World `_YpX47fNraQFw2dD7TdycJ`, then remove leftover NPC entries from that World's Lexicon.
Requirements:
R1. Backup first: Save full JSON snapshot of characters and lexicon of `_YpX47fNraQFw2dD7TdycJ` under scratch/ before any write.
R2. Remove duplicates: Keep complete record, delete empty one (e.g. Finnegan Novak, keep `_Yk9aK6X9WHzrWPCT7mzEK`, delete `_7Lkgnm4GyaPTrYfNGn1YT`).
R3. Missing-data gate (no invention): Use only canonical sources (lorebooks/optimized/*.json, FINAL/, scratch/rpg_full_snapshots/, scratch/rpg_snapshots/). If data is missing for age/birthdate, dossier for RPG, or outfits, record in scratch/missing_data.md and report to parent/user; continue for all characters with sufficient data.
R4. Complete every character with sufficient data: RPG stats (6 stats summing to 31, level = age capped at 99), birthdate == start_timeline_position as integer world-hours <= 10486470, pronouns, clean keys (no umbrella keys), summary/long_summary from JED+, at least 9 contextual outfits per GEMINI.md §4. Text rules: no em-dashes, no markdown/asterisk bold, no {{age}} macro. Single animal ear pair for demi-humans, Sierra Cruz no legs, Scarlett Rose candy-pink hair/eyes + scarlet horns. Note known API traps: partial PUT bodies with only changed fields and verify with GET; never ISO strings for dates; level capped at 99. Standalone Lorebooks MUST NOT be touched!
R5. Clean World Lexicon: Delete NPC entries in World Lexicon of `_YpX47fNraQFw2dD7TdycJ` only if a matching World Character verifiably exists. Keep unmatched ones and list in final report.
R6. Live verification: Validate with Chrome DevTools via CDP on https://app.wyvern.chat/sim/chat_log_PJx1W1rg3WUzRM7MnQrkN (Stats tab character sheets, 0 console errors, 0 failed network calls).

Decompose into milestones, dispatch workers, enforce gates, verify each milestone, maintain BRIEFING.md and progress.md, and report final victory back to Sentinel when complete.
