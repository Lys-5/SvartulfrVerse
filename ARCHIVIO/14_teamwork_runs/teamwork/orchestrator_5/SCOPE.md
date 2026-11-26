# SCOPE — Character Scenarios: 15 Lorebooks Suite & Persona Selection Integration

## Target Milestone
Update all 7 Character Scenarios (Villa Douglas, Camp Mystic, DMHA Dungeons, Underworld Sindacato, SUCC Route Alyssa, SUCC Route Jasper, Master Scenario) both live on Wyvern via Web API and locally in repository JSON files, assigning the unified 15 Lorebook suite, configuring "Offer a persona to play as" (`linked_persona_ids`) per scenario rules, updating CHANGELOG.md, and validating via Chrome DevTools (CDP).

## Scenarios Inventory
1. `Svartulfr_Scenario_Villa_Douglas.json` (Dual)
2. `Svartulfr_Scenario_Camp_Mystic.json` (Dual)
3. `Svartulfr_Scenario_DMHA_Dungeons.json` (Dual)
4. `Svartulfr_Scenario_Underworld_Sindacato.json` (Dual)
5. `Svartulfr_Scenario_SUCC_Route_Alyssa.json` (Single - Alyssa)
6. `Svartulfr_Scenario_SUCC_Route_Jasper.json` (Single - Jasper)
7. `Svartulfr_Master_Scenario.json` (Master - Dual + Tagged POV greetings)

## Invariants & Requirements

### R1. Unified Suite of 15 Lorebooks
All 7 scenarios must have `lorebook_ids` set to the exact 15 IDs:
- `_gwwCxCfQ6PQaLEjAQVpJL` (Svartúlfr - Lorebook I)
- `_HfG7TeV6MJyj6bxMwxkpt` (Svartúlfr - Lorebook II)
- `_9zWTGqYJNJ4BCDMj8gfcD` (Svartúlfr - Lorebook III)
- `_EjXxkmPVhpCXg8xABpFkK` (Svartúlfr - Location)
- `_Uht3Ckz44JBDrPnUHq7LV` (Svartúlfr - NPC Secondary)
- `_zwEqgEEzh12X6gHVmMKKC` (Svartúlfr - NPC Primary)
- `_GV1KyHVY1RMbCnWgLkzDG` (A0 Behavioral Realism)
- `_GbWJbkhgLzWexMHrjyUUc` (A1 Physics)
- `_FaVcHfmrqcaJq8pa3WmRw` (A2 Social Realism)
- `_BbrRgrcdGPMLEbBU2b6xk` (A3 Medical Realism)
- `_gchmML4Q478zdFjhXf8rN` (A4 Cultural Realism)
- `_brNyzEdhzNAyxK8xC8hhm` (A5 Sex Position)
- `_YtKLMTwyMxNf1DNYqBx1t` (A5.5 Scene Tone)
- `_b9HgpUXtAW8VmTy82BPDV` (A6 World Realism)
- `_c8bEm1bWphwqFBXWRPrV8` (A7 Queer Realism)

### R2. "Offer a persona to play as" Configuration (`linked_persona_ids`)
- Alyssa Persona ID: `persona_1786335754946`
- Jasper Persona ID: `1792155173728`
- **Dual Scenarios** (Villa Douglas, Camp Mystic, DMHA Dungeons, Underworld Sindacato):
  Assign `['persona_1786335754946', '1792155173728']` to ALL greetings.
- **SUCC Route Alyssa**:
  Assign `['persona_1786335754946']` to ALL greetings.
- **SUCC Route Jasper**:
  Assign `['1792155173728']` to ALL greetings.
- **Master Scenario**:
  Assign `['persona_1786335754946', '1792155173728']` to shared/neutral greetings.
  Preserve dedicated single persona on tagged greetings:
  - Greetings with `[FemPOV]` or female-specific context -> `['persona_1786335754946']`
  - Greetings with `[MalePOV]` or male-specific context -> `['1792155173728']`

### R3. Live API & Local Persistence
- Perform GET to fetch current state and revision for each scenario.
- PUT to `https://app.wyvern.chat/api/character-scenarios/:id` with Bearer token.
- Update local files: `FINAL/scenarios/*.json` and `FINAL/Svartulfr_Master_Scenario.json`.
- Update `CHANGELOG.md`.

### R4. Chrome DevTools (CDP) Validation
- Connect via Chrome DevTools on port 9222.
- Inspect scenario editor DOM to verify accordion 'Offer a persona to play as' and presence of the 15 lorebooks.
- Verify zero network errors (HTTP 4xx/5xx) and zero JS runtime errors.

## Milestones & Status
| # | Step | Description | Status |
|---|------|-------------|--------|
| 1 | Survey & Discovery | Explorers analyze local files, live scenario IDs, schema details, and greeting structures | DONE |
| 2 | Implementation | Worker executes API updates, local JSON syncing, and CHANGELOG update | DONE |
| 3 | Review | Dual Reviewers verify schema compliance, API live responses, and local file consistency | DONE |
| 4 | Challenge | Dual Challengers test linked_persona_ids edge cases, greeting tags, and 15 lorebook parity | DONE |
| 5 | Integrity Forensics | Auditor verifies authentic API interaction, non-hardcoding, and genuine persistence | DONE |
| 6 | Chrome DevTools Verification | Worker/Reviewer validates UI DOM & console via CDP on port 9222 | DONE |
| 7 | Gate & Handoff | Gate evaluation and final handoff to Sentinel | DONE |
