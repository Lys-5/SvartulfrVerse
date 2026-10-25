# Project: Svartúlfr Verse — Lorebook NPC Full JED+ Restoration & Live Deployment

## Architecture
- **Data Repositories**:
  - `FINAL/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`, 99 entries)
  - `FINAL/Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`, 211 entries)
  - Source Standalone Cards in `FINAL/`:
    * `Erik_Douglas_card.json` (`_QPea6g4Q1QfeYCVHCLMPR`)
    * `Malachia_Douglas_Bloodmoon_card.json` (`_RDfz7XzTpM23LpPALVXHM`)
    * `Noah_Douglas_Bloodmoon_card.json` (`_zFLUjV8aVxQRAfQxGcAcY`)
    * `Logan_Douglas_card.json` (`_T8Ywcr9FEqNf9JxbK6eHP`)
    * `Wulfnic_Bloodmoon_card.json` (`_HEQQbbRFwKdG8QE2Fh1z1`)
    * `Mackenzie_Sanchez_Rogers_card.json` (`_zn24784jfcchQ7EwCyAnm`)
    * `Edric_Douglas_card.json` (`_TbRM3EdxDjHFgqztTbCpL`)
- **Mirror Repository**:
  - `lorebooks/optimized/`
- **Remote Cloud Endpoint**:
  - Wyvern Web API (`https://app.wyvern.chat/api/lorebooks/:id`)
  - Authenticated via Bearer token in `scratch/wyvern_token.txt` (or refreshed via `scratch/refresh_token.py`).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | R1: 7 Core NPCs Full JED+ Restoration | Convert 6 core in Primary and Edric in Secondary to `type: "npc"`, `selective: false`, full JED+ from card JSONs, card avatars, regex, `npc_info`, `ignored_characters`, and update token budgets (Primary 7500, Secondary 5000). | M1 | survey |
| 2 | R2: 310 Entries Layout Homogenization | Encapsulate 3 irregular entries (Bruce, Campus Staff Rat, Adrian) into standard JED+ with initial bracket block, Backstory, and Voice & Behavior. Normalize `VOICE AND BEHAVIOR:` to `VOICE & BEHAVIOR:`. | M1 | survey |
| 3 | R3: Official DCC Avatar Placeholder | Update 200 fallback entries across Primary (42) and Secondary (158) to `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`. Ensure 100% HTTPS avatars. | M1 | survey |
| 4 | R4: Formatting Discipline & Recursion Safeguard | Enforce 0 em-dashes, dialog quotes, plain text narration, 0 `{{age}}`, 0 umbrella `BROAD_KEYS` on NPC keys, and set `exclude_from_recursion: true` on all 310 entries. | M1 | survey |
| 5 | R5: Emblem Cover, Local Mirror & Live Wyvern Deployment | Set House Svartúlfr emblem `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public` as `photoURL` cover on both lorebooks, mirror `FINAL/` to `lorebooks/optimized/`, deploy via PUT with compact payload, verify with live GET, update CHANGELOG.md. | M1 | survey |
| 6 | Gate Verification & Forensic Integrity Audit | Independent Reviewers (2), Challengers (2), and Forensic Integrity Auditor (1) verification of local files and live cloud state. | M2 | survey |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 0 | Survey & Specification | Survey cards, target entries, layout, avatars, cover, API | None | DONE |
| 1 | Implementation & Live Deployment | Execute R1, R2, R3, R4, R5, sync mirror, deploy live PUT, GET verify, update CHANGELOG.md | M0 | IN_PROGRESS |
| 2 | Multi-Agent Review, Empirical Challenge & Audit Gate | 2 Reviewers, 2 Challengers, 1 Forensic Integrity Auditor | M1 | PLANNED |

## Code Layout
- `FINAL/Svartulfr_NPC_Primary.json` — Primary lorebook (owned by Worker during M1)
- `FINAL/Svartulfr_NPC_Secondary.json` — Secondary lorebook (owned by Worker during M1)
- `lorebooks/optimized/` — Mirror directory (owned by Worker during M1)
- `CHANGELOG.md` — Project historical log (owned by Worker during M1)
- `scratch/` — Working scripts and test artifacts
