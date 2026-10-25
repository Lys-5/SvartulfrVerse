# Dispatch — Explorer R6-3

**Role**: teamwork_preview_explorer (Investigation of R4: Lorebook Primary & 6 NPC Profiles Restoration)
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_3`
**Authoritative Request**: `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (see `## Follow-up — 2026-10-21T14:38:04Z`)
**Orchestrator Scope**: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6\SCOPE.md`

## 2026-10-21T14:43:05Z
[Message] timestamp=2026-10-21T14:43:05Z sender=4e0bd8eb-f1f2-49dd-afae-a447f27e63f2 priority=MESSAGE_PRIORITY_HIGH content=You are Explorer R6-3.
Your working directory is e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_3.
You MUST read your dispatch instructions at e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_3\DISPATCH.md, the authoritative request at e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (latest entry: ## Follow-up — 2026-10-21T14:38:04Z), and e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6\SCOPE.md.

Task:
1. Investigate FINAL/Svartulfr_NPC_Primary.json and Wyvern API for Lorebook _zwEqgEEzh12X6gHVmMKKC.
2. Locate the 6 target entries (Scarlett Rose, Sierra Cruz, Russell 'Russ' Sinclair, Stanley Davies Jr., Jared Thompson, Alyssa Hvit Douglas Bloodmoon).
3. Find source JED+ descriptions for these 6 characters (confirming >2000 chars), avatar URLs, and npc_info.
4. Inspect Jasper's record (Vcj4h2TL4Usola2A4OOl6) in Svartulfr_NPC_Primary.json for exact Persona anti-duplicate settings (selective: true, secondary_keys Dossier, key_logic: AND_ANY).
5. Document how Alyssa's record must be configured to mirror Jasper's protection while containing full JED+ description and valid avatar.
6. Verify Scarlett, Sierra, Russ, Stan, Jared configuration (type: "npc", selective: false, avatar, multiline regex, npc_info).
7. Write your detailed analysis to e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_3\analysis.md and your handoff to handoff.md.
Send a message to your parent when done.

## Assignment
1. Investigate `FINAL/Svartulfr_NPC_Primary.json` and Lorebook Primary `_zwEqgEEzh12X6gHVmMKKC`:
   - Inspect the current state of both `entries` and `lexicon` in `FINAL/Svartulfr_NPC_Primary.json`.
   - Locate the 6 target entries by ID or name:
     - Scarlett Rose (`4NzXF4_0hYxmN7Idltzpw`)
     - Sierra Cruz (`ijy8vrlphNv19-p-gbYuY`)
     - Russell 'Russ' Sinclair (`YCxAqNoShpefVvk0_Pc7i`)
     - Stanley Davies Jr. (`ekdQjq63xP7HtNuaPQJQE`)
     - Jared Thompson (`RM6rcwv8MlY1XWaCTQp0M`)
     - Alyssa Hvit Douglas Bloodmoon (`alyssa_world_dossier_2b54a223`)
2. Investigate source JED+ descriptions for these 6 characters:
   - Check where the full JED+ source card files are located (e.g. in `FINAL/`, `ARCHIVIO/`, or elsewhere in the repo).
   - Verify if their full descriptions exceed 2,000 characters.
   - Extract their full descriptions, avatars, and character details.
3. Investigate Persona anti-duplicate protection on Jasper:
   - Inspect Jasper's record (`Vcj4h2TL4Usola2A4OOl6`) in `Svartulfr_NPC_Primary.json`.
   - Document its exact fields: `selective: true`, `secondary_keys: ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`, `key_logic: 'AND_ANY'`, etc.
   - Determine how Alyssa (`alyssa_world_dossier_2b54a223`) must be structured identically to mirror Jasper.
4. Investigate the 5 other NPCs:
   - For Scarlett, Sierra, Russ, Stan, Jared: verify `type: "npc"`, `selective: false`, avatar URL, multiline regex (`avatar_activation_regex`), `lines_parsed: 1`, `npc_info`.
5. Check Wyvern API GET for lorebook `_zwEqgEEzh12X6gHVmMKKC`:
   - Current revision, entry count, schema compatibility.
6. Produce a comprehensive report in `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_3\analysis.md` and complete handoff in `handoff.md`.
