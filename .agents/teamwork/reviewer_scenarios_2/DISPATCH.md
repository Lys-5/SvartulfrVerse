# DISPATCH — Reviewer Scenarios 2

## Mission
Conduct an objective and rigorous review of the live Wyvern Web API deployment, post-deployment GET responses, and CHANGELOG.md documentation.

## Working Directory
`e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_2`

## Mandatory Documents to Read
- `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (Authoritative requirements)
- `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_4\SCOPE.md`
- `e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_1\handoff.md`

## Review Focus
1. **Live Wyvern API Verification**:
   - Verify live GET calls to `https://app.wyvern.chat/api/character-scenarios/{id}` for all 6 scenario IDs:
     * `char_scenario_8GtdBd6dU7tPF481ekrKe` (Camp Mystic)
     * `char_scenario_664yrxUXYwNUUJfyf7da7` (SUCC Alyssa Route)
     * `char_scenario_Mfxz4Ym8QaECU6MjfmWG3` (SUCC Jasper Route)
     * `char_scenario_kw42g8J3NjBfKf7QW8zAG` (Villa Douglas)
     * `char_scenario_WdajqL3eJtT3GydxhDRT4` (DMHA Dungeons)
     * `char_scenario_MdbWc4gXbDqXHKrXY7YFx` (Underworld Sindacato)
   - Ensure all return HTTP 200 OK.
   - Confirm each deployed scenario on Wyvern cloud has `visibility: "private"`.
   - Confirm slot counts, greeting counts, and lorebook IDs match.
2. **CHANGELOG.md Verification**:
   - Check `CHANGELOG.md` to ensure the release entry documents all 6 scenarios, their IDs, slot structures, and deployment metadata accurately.

## Deliverables
- Execute verification commands (e.g. `python scratch/build_and_deploy_6_scenarios.py --verify-only`).
- Write report to `e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_2\handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`.
- Send message back to orchestrator.

## 2026-10-20T17:49:45Z
Sender: be560f41-366c-4523-9cb0-8842aafd8c44
Content:
You are reviewer_scenarios_2, the Wyvern Live API & Docs Reviewer.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_2
Project directory: e:\repository\SvartulfrVerse

READ MANDATORY DOCUMENTS FIRST:
- e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
- e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_4\SCOPE.md
- e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_2\DISPATCH.md
- e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_1\handoff.md

TASK:
1. Review the live Wyvern Web API deployment of all 6 scenarios:
   - char_scenario_8GtdBd6dU7tPF481ekrKe (Camp Mystic)
   - char_scenario_664yrxUXYwNUUJfyf7da7 (SUCC Alyssa Route)
   - char_scenario_Mfxz4Ym8QaECU6MjfmWG3 (SUCC Jasper Route)
   - char_scenario_kw42g8J3NjBfKf7QW8zAG (Villa Douglas)
   - char_scenario_WdajqL3eJtT3GydxhDRT4 (DMHA Dungeons)
   - char_scenario_MdbWc4gXbDqXHKrXY7YFx (Underworld Sindacato)
2. Run live GET queries (e.g. python scratch/build_and_deploy_6_scenarios.py --verify-only) to confirm HTTP 200, "visibility": "private", slot counts, greeting counts, and lorebook IDs.
3. Review CHANGELOG.md for accuracy of the scenario release documentation.
4. Write your handoff report to e:\repository\SvartulfrVerse\.agents\teamwork\reviewer_scenarios_2\handoff.md with explicit verdict: APPROVE or REQUEST_CHANGES.
5. Send a completion message back to orchestrator via send_message.

