# Dispatch — Explorer R6-1

**Role**: teamwork_preview_explorer (Investigation of R1 & R2: Scenarios & Greeting Macros)
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1`
**Authoritative Request**: `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (see `## Follow-up — 2026-10-21T14:38:04Z`)
**Orchestrator Scope**: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6\SCOPE.md`

## Assignment
1. Investigate Wyvern API live state for the 2 SUCC scenarios:
   - `char_scenario_CKgwq246DyCj1NNTBV9rt` (Alyssa rev 10)
   - `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` (Jasper rev 4)
   - Check Bearer token in `scratch/wyvern_token.txt` (test if valid or if `python scratch/refresh_token.py` is needed).
   - Fetch the current live payloads using GET requests.
2. Inspect local scenario files in `FINAL/scenarios/`:
   - Identify the 4 files of scenarios deleted from Wyvern: Camp Mystic, DMHA, Underworld, Villa Douglas.
   - Inspect the current versions of Alyssa Route and Jasper Route scenarios.
3. Analyze all greetings and messages in both SUCC scenarios:
   - Find all occurrences of `{{scenarioChar "..."}}` macros.
   - Specifically locate those referring to characters turned into NPCs: Scarlett (`4NzXF4_0hYxmN7Idltzpw` / `best_friend` / `crush`), Russ (`YCxAqNoShpefVvk0_Pc7i` / `male_roommate`), Jared (`RM6rcwv8MlY1XWaCTQp0M` / `quarterback`), Stan (`ekdQjq63xP7HtNuaPQJQE` / `friend`), Sierra (`ijy8vrlphNv19-p-gbYuY` / `roommate`).
   - Identify the exact literal text replacements required.
4. Inspect slot and pool configurations:
   - Find any slots/pools with `unavailable_count: 1` or inaccessible card pools.
   - Check `speaker_slot` for all greetings and messages to ensure no resolution errors.
5. Produce a comprehensive report in `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\analysis.md` and complete handoff in `handoff.md`.


## 2026-10-21T14:43:05Z
From: 4e0bd8eb-f1f2-49dd-afae-a447f27e63f2
You are Explorer R6-1.
Your working directory is e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1.
You MUST read your dispatch instructions at e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\DISPATCH.md, the authoritative request at e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (latest entry: ## Follow-up — 2026-10-21T14:38:04Z), and e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6\SCOPE.md.

Task:
1. Check Wyvern Bearer token in scratch/wyvern_token.txt. Test live GET against char_scenario_CKgwq246DyCj1NNTBV9rt and char_scenario_Kq4mJEBH83j7Q7DdVfFnF.
2. Inspect local scenario files in FINAL/scenarios/. Map the 4 files to move to ARCHIVIO/scenarios/ and current state of Alyssa & Jasper SUCC routes.
3. Inspect all occurrences of {{scenarioChar "..."}} in greetings for both scenarios. Identify the macro keys pointing to NPC characters (Scarlett, Russ, Jared, Stan, Sierra) and map their exact literal text replacements.
4. Inspect slot and pool configurations: find slots/pools with unavailable_count: 1, inspect speaker_slot validity across all messages.
5. Write your detailed analysis to e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r6_1\analysis.md and your handoff to handoff.md.
Send a message to your parent when done.
