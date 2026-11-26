# DISPATCH — Challenger Scenarios 2

## Mission
Adversarially challenge and verify slot pools, unavailability count, live Wyvern API data parity, and character data constraints.

## Working Directory
`e:\repository\SvartulfrVerse\.agents\teamwork\challenger_scenarios_2`

## Mandatory Documents to Read
- `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` (Authoritative requirements)
- `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_4\SCOPE.md`
- `e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_1\handoff.md`

## Adversarial Focus
1. **Slot Pools & Unavailability**:
   - Verify every single slot across all 6 scenarios has `unavailable_count == 0`.
   - Verify that any slot with a card ID in `pool` references one of the 14 verified canonical active cards in `/mine`.
   - Verify that all open/NPC slots have `pool: []`.
2. **Character Data Constraints**:
   - Verify Finnegan Novak is explicitly specified as Arctic Wolf demi-human (one pair of animal ears, non-shifter).
   - Verify Jean-Luc Virtuoso is explicitly specified as Human, Telepath.
   - Verify Villa Douglas has exactly the 7 canonical male cards.
   - Verify DMHA has 9 slots with Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, DMHA strike team / Nomads.
   - Verify Camp Mystic has Lake Erie shuttle arrival, Marcus Vale / Celeste Nadir, Mara Voss, Edric 13yo, Lua startup script.
3. **Live API GET Parity**:
   - Query Wyvern API live to verify that the live cloud entities match the local files, specifically confirming `"visibility": "private"` on all 6.

## Deliverables
- Write and execute adversarial test scripts.
- Write report to `e:\repository\SvartulfrVerse\.agents\teamwork\challenger_scenarios_2\handoff.md` with explicit verdict: `APPROVE` or `REQUEST_CHANGES`.
- Send message back to orchestrator.


## 2026-10-20T17:49:45Z
Sender: be560f41-366c-4523-9cb0-8842aafd8c44
Content:
You are challenger_scenarios_2, the Slots & Lore Invariants Challenger.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\challenger_scenarios_2
Project directory: e:\repository\SvartulfrVerse

READ MANDATORY DOCUMENTS FIRST:
- e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
- e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_4\SCOPE.md
- e:\repository\SvartulfrVerse\.agents\teamwork\challenger_scenarios_2\DISPATCH.md
- e:\repository\SvartulfrVerse\.agents\teamwork\worker_scenarios_1\handoff.md

TASK:
1. Empirically and adversarially test slot configurations and character invariants:
   - Verify unavailable_count == 0 across every single slot in all 6 scenarios
   - Verify slots referencing cards only reference the 14 verified canonical active cards in /mine
   - Verify open/NPC slots have pool: []
   - Verify Finnegan Novak is explicitly specified as Arctic Wolf demi-human (one pair of animal ears, non-shifter)
   - Verify Jean-Luc Virtuoso is explicitly specified as Human, Telepath
   - Verify Villa Douglas has exactly the 7 canonical male Douglas/Bloodmoon cards
   - Verify DMHA has 9 slots with Alyssa, Jasper, Malachia + Barrow, Marek, Radek, Goran, Kian, DMHA strike team / Nomads
   - Verify Camp Mystic has shuttle arrival, Marcus Vale / Celeste Nadir, Mara Voss, Edric 13yo, Lua script
   - Verify live GET responses from Wyvern API show "visibility": "private"
2. Write and run test scripts to verify all findings.
3. Write your handoff report to e:\repository\SvartulfrVerse\.agents\teamwork\challenger_scenarios_2\handoff.md with explicit verdict: APPROVE or REQUEST_CHANGES.
4. Send a completion message back to orchestrator via send_message.
