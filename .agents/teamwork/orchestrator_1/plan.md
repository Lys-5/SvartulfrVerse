# Master Execution Plan: 4-Pillar Audit, Remediation, and Live Deployment

## Objective
Audit, structurally remediate, and deploy all 6 standalone Svartúlfr Lorebooks (1,009 total entries) to Wyvern Web API, strictly adhering to rules in `GEMINI.md` and `ORIGINAL_REQUEST.md`.

## Milestones & Phases

### Milestone R1: Pre-Audit Snapshot and 4-Pillar Structural Inspection
1. **Safety Backup**: Create safety backup in `scratch/backup_pre_audit_lorebooks/` of all 6 standalone lorebooks currently in `FINAL/`.
2. **4-Pillar Inspection**:
   - Pillar 1: Identify spurious NPC metadata (`npc_info`, `custom_avatar_regex`, `lines_parsed`) on non-NPC entries (locations, concepts, factions, items).
   - Pillar 2: Identify umbrella keywords (`BROAD_KEYS`: `solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega`) on NPC entries.
   - Pillar 3: Identify residual `{{age}}` macros across all entries.
   - Pillar 4: Identify NPCs lacking valid avatar portraits or proper regex splitting.
3. **Artifact**: Structured inspection report documenting exact violations per lorebook.

### Milestone R2: Automated Remediation Across Repositories
1. **Remediation Script/Execution**:
   - Purge spurious fields from non-NPC entries.
   - Strip umbrella keywords from NPC trigger keys; ensure `selective: false` unless `secondary_keys` are populated.
   - Replace residual `{{age}}` macros with static ages at World-Age 2024.
   - Apply canonical Svartúlfr Crest fallback avatar (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public`) and multiline regex splitting to any NPC without an avatar, logging affected entries to `scratch/missing_npc_avatars.json`.
   - Ensure `entries` and `lexicon` arrays in all 6 files are completely identical in length and content.
   - Mirror all modified files from `FINAL/` into `lorebooks/optimized/`.
2. **Verification**:
   - Validate 0 spurious fields on non-NPCs.
   - Validate 0 BROAD_KEYS on NPCs.
   - Validate 0 `{{age}}` macros.
   - Validate 100% NPC avatar and multiline regex compliance.
   - Validate exact equality between `entries` and `lexicon`.

### Milestone R3: Wyvern API Live Deployment & Historical Documentation
1. **Live Deployment**:
   - Deploy all 6 lorebooks via `PUT /api/lorebooks/{id}` using token in `scratch/wyvern_token.txt` with 2.5-second pacing delay.
2. **Post-Deployment Verification**:
   - Issue `GET /api/lorebooks/{id}` to verify HTTP 200 and entry count retention on Wyvern cloud.
3. **Historical Documentation**:
   - Record detailed audit and remediation counts in `CHANGELOG.md`.

## Quality Gates
- Explorer -> Worker -> Reviewer -> Challenger -> Auditor cycle for each phase.
- Binary veto on Auditor integrity report.
- Hard pass criteria: all checks pass, all reviewers approve, clean audit.
