# Original User Request

## Initial Request — 2026-10-16T21:45:20Z

Execute a comprehensive 4-pillar audit, structural data remediation, and live Wyvern API deployment across all 6 standalone Svartúlfr Lorebooks (1,009 entries total).

Working directory: e:\repository\SvartulfrVerse
Integrity mode: development

## Requirements

### R1. Pre-Audit Snapshot and 4-Pillar Structural Inspection
Create a complete safety backup in `scratch/backup_pre_audit_lorebooks/`. Inspect all 6 standalone lorebooks in `FINAL/`:
- Svartúlfr - Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL`)
- Svartúlfr - Lorebook II (`_HfG7TeV6MJyj6bxMwxkpt`)
- Svartúlfr - Lorebook III (`_9zWTGqYJNJ4BCDMj8gfcD`)
- Svartúlfr - Location (`_EjXxkmPVhpCXg8xABpFkK`)
- Svartúlfr - NPC Primary (`_zwEqgEEzh12X6gHVmMKKC`)
- Svartúlfr - NPC Secondary (`_Uht3Ckz44JBDrPnUHq7LV`)

Identify:
1. Spurious NPC metadata (e.g., `npc_info`, `custom_avatar_regex`, `lines_parsed`) present on non-NPC entries (locations, concepts, factions, items).
2. Umbrella keywords (`BROAD_KEYS` such as `solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega`) on NPC entries.
3. Any residual `{{age}}` macros.
4. NPCs lacking avatar portraits or proper regex splitting.

### R2. Automated Remediation Across Repositories
Run automated remediation updating both `entries` and `lexicon` lists in each file:
- Purge spurious fields from non-NPC entries.
- Strip umbrella keywords from NPC trigger keys; ensure `selective: false` unless `secondary_keys` are populated.
- Replace residual `{{age}}` macros with static ages at World-Age 2024.
- Apply the canonical Svartúlfr Crest fallback avatar (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public`) and multiline regex splitting to any NPC without an avatar, recording all affected entries in `scratch/missing_npc_avatars.json`.
- Mirror all modified files from `FINAL/` into `lorebooks/optimized/`.

### R3. Wyvern API Live Deployment & Historical Documentation
Deploy all 6 remediated lorebooks to the Wyvern Web API:
- Issue `PUT /api/lorebooks/{id}` for each of the 6 lorebooks using `scratch/wyvern_token.txt` with a 2.5-second pacing delay between calls.
- Perform a post-deployment `GET /api/lorebooks/{id}` verification confirming HTTP 200 and entry count retention.
- Document the full breakdown of remediations in `CHANGELOG.md`.

## Acceptance Criteria

### Audit & Data Integrity
- [ ] Non-NPC entries contain zero spurious `npc_info` or avatar-parsing fields.
- [ ] Zero umbrella keywords (`BROAD_KEYS`) remain on NPC trigger keys.
- [ ] Zero `{{age}}` macros exist across all 6 lorebook JSON files.
- [ ] 100% of NPC entries have valid avatars, `custom_avatar_regex: true`, `lines_parsed: 1`, and multiline regex patterns.
- [ ] `entries` and `lexicon` arrays in all 6 files are completely identical in length and content.

### Deployment & Verification
- [ ] All 6 lorebooks successfully deployed with HTTP 200 via Wyvern API.
- [ ] Post-deploy GET calls confirm exact entry counts on Wyvern cloud.
- [ ] `CHANGELOG.md` updated with exact counts of remediated entries per lorebook.
