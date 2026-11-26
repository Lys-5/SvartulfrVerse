# Dispatch — Challenger R6-1

**Role**: teamwork_preview_challenger (Challenger 1: Scenarios & Wyvern API Rigor)
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\challenger_r6_1`
**Authoritative Request**: `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (see `## Follow-up — 2026-10-21T14:38:04Z`)
**Orchestrator Scope**: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6\SCOPE.md`
**Worker Handoff**: `e:\repository\SvartulfrVerse\.agents\teamwork\worker_r6_1\handoff.md`

## Assignment
1. Write an empirical stress test script to verify:
   - Query live Wyvern API for both scenarios (`char_scenario_CKgwq246DyCj1NNTBV9rt`, `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`).
   - Parse every greeting message text in both live scenarios: assert 0 occurrences of `{{scenarioChar`, 0 orphan macro tokens, 0 em-dashes (`—`).
   - Check all slots in both live scenarios: verify `unavailable_count == 0` for all slots.
   - Verify speaker_slot invariant across all 13 greetings (`greeting.speaker_slot == messages[0].speaker_slot` and `greeting.content == messages[0].content`).
   - Query live Wyvern API for Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`): assert HTTP 404.
   - Query `/characters/mine`: assert exactly 8 approved cards.
2. Deliver `handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`.

## 2026-10-21T15:10:34Z
[Message] timestamp=2026-10-21T15:10:34Z sender=4e0bd8eb-f1f2-49dd-afae-a447f27e63f2 priority=MESSAGE_PRIORITY_HIGH content=You are Challenger R6-1.
Your working directory is e:\repository\SvartulfrVerse\.agents\teamwork\challenger_r6_1.
You MUST read your dispatch instructions at e:\repository\SvartulfrVerse\.agents\teamwork\challenger_r6_1\DISPATCH.md, the authoritative request at e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (latest entry: ## Follow-up — 2026-10-21T14:38:04Z), e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6\SCOPE.md, and the worker handoff at e:\repository\SvartulfrVerse\.agents\teamwork\worker_r6_1\handoff.md.

Task:
Empirically challenge scenario integrity and Wyvern API calls:
- Query live Wyvern API for both scenarios (char_scenario_CKgwq246DyCj1NNTBV9rt and char_scenario_Kq4mJEBH83j7Q7DdVfFnF).
- Inspect all greeting message texts: assert 0 occurrences of {{scenarioChar, 0 em-dashes.
- Inspect all slots: assert unavailable_count == 0 for all slots.
- Verify speaker_slot invariant across all 13 greetings.
- Query live Wyvern API for Jared Thompson (_xJVPtBLL3dxy69RLKL9X9): assert HTTP 404.
- Query /characters/mine: assert exactly 8 approved cards.
Deliver handoff.md with explicit verdict: APPROVE or REQUEST_CHANGES.
Send a message to your parent when done.
