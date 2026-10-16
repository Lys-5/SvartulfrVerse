# Project: Svartúlfr Lorebooks 4-Pillar Audit & Remediation

## Architecture
- Standalone Lorebooks: 6 JSON files located in `FINAL/`:
  1. `FINAL/Svartulfr_Lorebook_I.json` (`_gwwCxCfQ6PQaLEjAQVpJL`) - Lorebook I (219 entries)
  2. `FINAL/Svartulfr_Lorebook_II.json` (`_HfG7TeV6MJyj6bxMwxkpt`) - Lorebook II (143 entries)
  3. `FINAL/Svartulfr_Lorebook_III.json` (`_9zWTGqYJNJ4BCDMj8gfcD`) - Lorebook III (35 entries)
  4. `FINAL/Svartulfr_Location.json` (`_EjXxkmPVhpCXg8xABpFkK`) - Location (196 entries)
  5. `FINAL/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`) - NPC Primary (106 entries)
  6. `FINAL/Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`) - NPC Secondary (310 entries)
  Total: 1,009 entries.
- Dual list structure in each lorebook: `entries` and `lexicon` (verified completely identical).
- Backup directory: `scratch/backup_pre_audit_lorebooks/` (verified 6/6 intact).
- Output mirror: `lorebooks/optimized/` (verified 100% bit-for-bit identical to FINAL/).
- API Endpoint: `PUT /api/lorebooks/{id}` and `GET /api/lorebooks/{id}` using token from `scratch/wyvern_token.txt` (6/6 HTTP 200, 1,009 / 1,009 cloud entries retained).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Pre-Audit Backup | Create full snapshot of 6 lorebooks in scratch/backup_pre_audit_lorebooks/ | R1 | ORIGINAL_REQUEST §R1 |
| 2 | Pillar 1 Inspection | Detect spurious NPC metadata on non-NPC entries | R1 | ORIGINAL_REQUEST §R1 |
| 3 | Pillar 2 Inspection | Detect umbrella keywords (BROAD_KEYS) on NPC trigger keys | R1 | ORIGINAL_REQUEST §R1 |
| 4 | Pillar 3 Inspection | Detect residual {{age}} macros | R1 | ORIGINAL_REQUEST §R1 |
| 5 | Pillar 4 Inspection | Detect missing avatars / invalid multiline regex on NPCs | R1 | ORIGINAL_REQUEST §R1 |
| 6 | Spurious Metadata Purge | Clean non-NPC entries of npc_info, custom_avatar_regex, lines_parsed | R2 | ORIGINAL_REQUEST §R2 |
| 7 | BROAD_KEYS Strip | Remove umbrella keys from NPCs, ensure selective: false | R2 | ORIGINAL_REQUEST §R2 |
| 8 | {{age}} Macro Replacement | Replace {{age}} macros with static 2024 ages | R2 | ORIGINAL_REQUEST §R2 |
| 9 | Avatar Fallback & Regex Splitting | Apply Svartúlfr Crest avatar + multiline regex; record in scratch/missing_npc_avatars.json | R2 | ORIGINAL_REQUEST §R2 |
| 10 | Entries-Lexicon Synchronization | Guarantee entries and lexicon arrays are completely identical | R2 | ORIGINAL_REQUEST §R2 |
| 11 | Lorebooks Mirroring | Mirror all 6 remediated files into lorebooks/optimized/ | R2 | ORIGINAL_REQUEST §R2 |
| 12 | Live API Deployment | PUT /api/lorebooks/{id} with 2.5s pacing and token | R3 | ORIGINAL_REQUEST §R3 |
| 13 | Post-Deploy Verification | GET /api/lorebooks/{id} confirming HTTP 200 and entry count retention | R3 | ORIGINAL_REQUEST §R3 |
| 14 | Changelog Documentation | Record full audit & remediation counts in CHANGELOG.md | R3 | ORIGINAL_REQUEST §R3 |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Milestone R1 | Safety snapshot and 4-pillar structural inspection of all 6 lorebooks | none | DONE |
| 2 | Milestone R2 | Automated remediation across repositories, synchronization, and mirroring | R1 | DONE |
| 3 | Milestone R3 | Wyvern API deployment, verification, and changelog update | R2 | DONE |

## Code Layout & File Boundaries
- Input files: `FINAL/*.json`
- Backup files: `scratch/backup_pre_audit_lorebooks/*.json`
- Missing avatars record: `scratch/missing_npc_avatars.json`
- Optimized mirror files: `lorebooks/optimized/*.json`
- Deployment script & log: `scratch/deploy_lorebooks_api.py`, `scratch/deployment_log.json`
- Auth token: `scratch/wyvern_token.txt`
- Changelog: `CHANGELOG.md`
- Working/Inspection reports: `.agents/teamwork/`
