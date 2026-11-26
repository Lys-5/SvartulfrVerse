## 2026-10-20T23:02:44Z
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

You are the Scenario Implementation Worker.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_15lb_1

MANDATORY READING:
You MUST read:
- e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
- e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_5\SCOPE.md
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_1\analysis.md
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_2\analysis.md
- e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\analysis.md

YOUR OBJECTIVE:
Update all 7 Character Scenarios (6 thematic + 1 Master) both on the live Wyvern Web API and in local repository files:
1. Suite of 15 Lorebooks assigned to lorebook_ids in canonical order:
   ["_gwwCxCfQ6PQaLEjAQVpJL", "_HfG7TeV6MJyj6bxMwxkpt", "_9zWTGqYJNJ4BCDMj8gfcD", "_EjXxkmPVhpCXg8xABpFkK", "_Uht3Ckz44JBDrPnUHq7LV", "_zwEqgEEzh12X6gHVmMKKC", "_GV1KyHVY1RMbCnWgLkzDG", "_GbWJbkhgLzWexMHrjyUUc", "_FaVcHfmrqcaJq8pa3WmRw", "_BbrRgrcdGPMLEbBU2b6xk", "_gchmML4Q478zdFjhXf8rN", "_brNyzEdhzNAyxK8xC8hhm", "_YtKLMTwyMxNf1DNYqBx1t", "_b9HgpUXtAW8VmTy82BPDV", "_c8bEm1bWphwqFBXWRPrV8"]
2. Configure "Offer a persona to play as" via linked_persona_ids on all greetings:
   - Alyssa Persona ID: "persona_1786335754946"
   - Jasper Persona ID: "1792155173728"
   - Dual scenarios (Villa Douglas, Camp Mystic, DMHA Dungeons, Underworld Sindacato): assign ["persona_1786335754946", "1792155173728"] to ALL greetings.
   - SUCC Route Alyssa: assign ["persona_1786335754946"] to ALL greetings.
   - SUCC Route Jasper: assign ["1792155173728"] to ALL greetings.
   - Master Scenario: assign ["persona_1786335754946", "1792155173728"] to 16 shared/neutral greetings, while preserving 7 [FemPOV] greetings with ["persona_1786335754946"] and 6 [MalePOV] greetings with ["1792155173728"].
3. Live API execution:
   - Scenarios IDs on Wyvern:
     * Master Scenario: char_scenario_1DC43ggb6mB8YLJDJKrU4
     * Villa Douglas: char_scenario_88N1eQXqkbydKX9q9XQzp
     * Camp Mystic: char_scenario_nLC84wrHdrbB6P3DEhwKb
     * DMHA Dungeons: char_scenario_eqtRNnDpKbxDp7dmJmq6E
     * Underworld Sindacato: char_scenario_rrUCdBPH6WTNyBnQkMAKR
     * SUCC Route Alyssa: char_scenario_CKgwq246DyCj1NNTBV9rt
     * SUCC Route Jasper: char_scenario_Kq4mJEBH83j7Q7DdVfFnF
   - Bearer token from scratch/wyvern_token.txt. Use Cloudflare headers (User-Agent: Mozilla/5.0..., Accept: application/json).
   - Perform fresh GET before PUT on each scenario to obtain latest revision (prevent HTTP 409).
   - PUT to https://app.wyvern.chat/api/character-scenarios/:id and verify HTTP 200.
4. Local persistence:
   - Update local files:
     * FINAL/scenarios/Svartulfr_Scenario_Camp_Mystic.json
     * FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json
     * FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json
     * FINAL/scenarios/Svartulfr_Scenario_Villa_Douglas.json
     * FINAL/scenarios/Svartulfr_Scenario_DMHA_Dungeons.json
     * FINAL/scenarios/Svartulfr_Scenario_Underworld_Sindacato.json
     * FINAL/Svartulfr_Master_Scenario.json
5. Update CHANGELOG.md documenting this milestone.
6. Verification:
   - Perform post-update GET on all 7 scenarios and verify that lorebook_ids has 15 items and linked_persona_ids are accurately set.
   - Verify local JSON files match the remote updates.

FILE OWNERSHIP:
You exclusively own:
- FINAL/scenarios/*.json
- FINAL/Svartulfr_Master_Scenario.json
- CHANGELOG.md
- helper scripts created in scratch/ (e.g. scratch/update_scenarios_15lb.py)

DELIVERABLES:
- Write progress to e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_15lb_1\progress.md.
- Write your final report to e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_15lb_1\analysis.md and handoff.md.
- When done, send a completion message with full verification evidence back to the caller.
