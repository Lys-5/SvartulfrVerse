# BRIEFING — 2026-10-20T17:22:00Z

## Mission
Investigate and document the exact JSON schema, required fields, slots, greetings, and Wyvern Web API endpoints for Wyvern Character Scenarios deployment.

## 🔒 My Identity
- Archetype: Explorer
- Roles: Schema & Wyvern API Explorer
- Working directory: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_1
- Original parent: 6f2f7fce-1035-4880-af5b-6087c18617c4
- Milestone: Svartúlfr Verse Character Scenarios

## 🔒 Key Constraints
- Read-only investigation — do NOT implement or modify project code/data
- Write only within e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_1
- Strict formatting rules: zero em-dashes ('—'), dialogue in quotes, plain text narration (no asterisks)
- Must communicate findings to parent via send_message

## Current Parent
- Conversation ID: 6f2f7fce-1035-4880-af5b-6087c18617c4
- Updated: 2026-10-20T17:22:00Z

## Investigation State
- **Explored paths**: ORIGINAL_REQUEST.md, FINAL/Svartulfr_Master_Scenario.json, scratch/live_scenario_latest.json, scratch/test_build_master_scenario_payload.py, scratch/reconfigure_scenario_slots.py, scratch/deploy_all_final.py, scratch/refresh_token.py, Wyvern official docs (Features/Character-Scenarios, Creating, Slots-Greetings-Macros), live Wyvern API endpoints.
- **Key findings**:
  1. Wyvern Character Scenario schema strictly validated: `name` (1-200), `display_description` (0-20000), `scenario` (0-100000), `slots` (1-20), `greetings` (1-100), `messages` (1-20 per greeting).
  2. Slot keys must match `/^[a-zA-Z][a-zA-Z0-9_-]{0,63}$/` and must be relational/role-based.
  3. Slots with canonical cards have `pool: [{"character_id": cid, "weight": 100}]`; slots for NPCs or open roles must have `pool: []` to guarantee `unavailable_count: 0`.
  4. Top-level `greeting.content` and `greeting.speaker_slot` must be strictly identical to `messages[0].content` and `messages[0].speaker_slot`.
  5. Zero em-dashes (`—`) across all strings; dialogue in quotes `"..."`, plain text narration, `*thoughts*`.
  6. API endpoints: `POST /api/character-scenarios`, `GET /api/character-scenarios/{id}`, `PUT /api/character-scenarios/{id}` at `https://app.wyvern.chat/api`.
  7. Auth token in `scratch/wyvern_token.txt` is verified live and active.
- **Unexplored areas**: None regarding schema and API mechanics.

## Key Decisions Made
- Confirmed that NPC-based slots must use `pool: []` to prevent `unavailable_count > 0` errors.
- Documented full JSON template and payload structure for the builder agents.

## Artifact Index
- DISPATCH.md — Initial dispatch message
- progress.md — Liveness heartbeat and activity tracking
- handoff.md — Final comprehensive investigation report
