# Project: Svartúlfr Verse — NPC Information Alignment & GM Grounding Recalibration

## Architecture
- **Wyvern Lorebooks**:
  - `FINAL/Svartulfr_NPC_Primary.json` & `lorebooks/optimized/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`, 99 entries)
  - `FINAL/Svartulfr_NPC_Secondary.json` & `lorebooks/optimized/Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`, 211 entries)
- **TTRPG Game Master & Assemblies**:
  - `FINAL/assistants/Svartulfr_Game_Master_Assistant.json`
  - `FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json`
  - Master Scenario (`FINAL/scenarios/` & live Wyvern scenario)
- **Frontend / Live Web API**:
  - Wyvern Web UI: `app.wyvern.chat` via CDP on port 9222
  - REST Web API endpoints: `PUT /api/lorebooks/{id}`, `PUT /api/assistants/{id}`, `PUT /api/prompts/{id}`, `PUT /api/scenarios/{id}`

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | R1 CDP Inspection: NPC Information fields | Inspect DOM & payload on app.wyvern.chat for npc_prefix, first_name, middle_names, last_name, nicknames, titles | M1 | ORIGINAL_REQUEST §R1 |
| 2 | R1 CDP Inspection: Gallery mapping & regex | Inspect DOM & network for avatar selection from Lorebook gallery (Cloudflare Images) and avatar_activation_regex compilation | M1 | ORIGINAL_REQUEST §R1 |
| 3 | R2 NPC Info extraction & population | Extract and populate npc_info (first_name, middle_names, last_name, nicknames, titles, npc_prefix) for 210 NPCs from JED+ | M2 | ORIGINAL_REQUEST §R2 |
| 4 | R2 Gallery avatar mapping & assignment | Map and assign each NPC avatar from Lorebook gallery on Cloudflare Images | M2 | ORIGINAL_REQUEST §R2 |
| 5 | R2 Anti-collision & parity preservation | Preserve ignored_characters / ignored_personas and maintain 100% byte-for-byte entries == lexicon parity | M2 | ORIGINAL_REQUEST §R2 |
| 6 | R2 3 Configuration Toggles ON | Set scan_persona: true, whole_words_only: true, and entry highlighting toggles across all entries | M2 | ORIGINAL_REQUEST §2026-10-24T11:31:17Z |
| 7 | R2 Live deployment via PUT | Deploy updated Lorebooks Primary and Secondary to live Wyvern API | M2 | ORIGINAL_REQUEST §R2 |
| 8 | R3 Chronological passivity recalibration | Remove static March 15 2024 date reset hallucinations from GM Assistant and Prompt Assembly | M3 | ORIGINAL_REQUEST §R3 |
| 9 | R3 Absolute grounding on XML & lore | Enforce strict grounding to `<character>`, `<user_persona>`, Lorebooks (no fake pack ranks, demianatomy, Sierra, Scarlett) | M3 | ORIGINAL_REQUEST §R3 |
| 10 | R3 GM deployment via PUT | Deploy updated Assistant, Prompt Assembly, and Scenario live to Wyvern API | M3 | ORIGINAL_REQUEST §R3 |
| 11 | R4 Chrome DevTools DOM/Network check | Verify DOM rendering and 0 network failures (4xx/5xx) on app.wyvern.chat | M4 | ORIGINAL_REQUEST §R4 |
| 12 | R4 GM Live validation test turn | Verify test turn with Game Master confirming date passivity and faithful grounding | M4 | ORIGINAL_REQUEST §R4 |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | M1: R1 Reverse-Engineering & Browser Inspection | Inspect DOM/Network on app.wyvern.chat for NPC Info & Gallery via CDP (port 9222); codify schema contract & test suite (124 tests) | none | **DONE** |
| 2 | M2: R2 Lorebook NPCs Sanitation & Alignment | Sanitize 210 NPCs (npc_info, 3 toggles: scan_persona/whole_words/highlight, gallery avatars, parity, anti-collision, live PUT) | M1 | **DONE** |
| 3 | M3: R3 GM Assistant & Prompt Recalibration | Date passivity & absolute grounding recalibration across GM assistant, assembly, scenario | none | PLANNED |
| 4 | M4: R4 Final DevTools Validation & Live Turn | CDP console/network check, live test turn validation | M2, M3 | PLANNED |

## Interface Contracts
- **NPC Info Schema**:
  ```json
  "npc_info": {
    "first_name": "...",
    "middle_names": ["..."],
    "last_name": "...",
    "nicknames": ["..."],
    "titles": ["..."],
    "npc_prefix": "..."
  }
  ```
- **3 Configuration Toggles Invariant**:
  - `scan_persona`: `true` on every entry.
  - `whole_words_only`: `true` on every entry.
  - `highlight_keys`: `true` / `enable_highlighting: true` on every entry; `enableEntryHighlighting: true` at lorebook root.
- **Avatar Gallery Schema**:
  URL / Cloudflare image ID mapped to `avatar` or gallery asset reference. Root `gallery: []`, `gallery_count: 0`.
- **Lorebook Parity Contract**:
  `JSON.stringify(lorebook.entries) === JSON.stringify(lorebook.lexicon)` byte-for-byte.
- **GM Passivity Contract**:
  No hardcoded dates in system prompt or template; inherit world/session clock passively.
