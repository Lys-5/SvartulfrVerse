## 2026-10-25T12:22:48Z
You are survey_explorer_2, an exploration agent for the Svartúlfr Verse project.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\survey_explorer_2
Your parent is orchestrator_12 (conversation ID: beb67cac-6ac6-4f74-a9f5-135370772105).

Read your instructions, constraints, and scope:
1. Read e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (especially under header ## 2026-10-25T12:18:07Z).
2. Read e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_12\PROJECT.md.
3. Survey all canonical sources for character data in the repository:
   - `lorebooks/optimized/*.json` (JED+ NPC entries across the 6 lorebooks)
   - `FINAL/` cards and personas
   - `scratch/rpg_full_snapshots/` and `scratch/rpg_snapshots/`
   - other scratch/ files (e.g., dossiers, character lists)
4. Map out data availability for all characters that exist in World `_YpX47fNraQFw2dD7TdycJ`:
   - Full JED+ description and summary
   - Established age and birthdate (and conversion to integer world-hours from epoch 827-12-21 UTC <= 10486470)
   - 6 RPG stats (might, resilience, agility, wit, presence, scouting summing to 31, level <= 99)
   - 9 contextual outfits per GEMINI.md §4
   - Pronouns and non-umbrella activation keys
5. Identify any characters that lack sufficient canonical data and must be cataloged in scratch/missing_data.md per R3.
6. Write a comprehensive survey report and handoff in e:\repository\SvartulfrVerse\.agents\teamwork\survey_explorer_2\handoff.md.
When finished, notify parent with send_message including a concise summary and the file path.
