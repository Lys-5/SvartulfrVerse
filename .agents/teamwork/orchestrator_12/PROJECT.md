# Project: Svartúlfr Verse — World Characters & World Lexicon Remediation
# World: `_YpX47fNraQFw2dD7TdycJ`

## Architecture
- **World Core**: Wyvern World `_YpX47fNraQFw2dD7TdycJ` ("Svartúlfr — Blackwood & Solarton"), World Clock Epoch `827-12-21 00:00:00 UTC`, current age `10486470` / `10489902`, 6 RPG stats (Might, Resilience, Agility, Wit, Presence, Scouting; base 1 each, 25 distributed, sum 31).
- **World Characters Layer**: 125 characters embedded in `_YpX47fNraQFw2dD7TdycJ`. Must be deduplicated (e.g., delete empty Finnegan Novak `_7Lkgnm4GyaPTrYfNGn1YT`, keep `_Yk9aK6X9WHzrWPCT7mzEK`), formatted with clean JED+ descriptions, non-umbrella activation keys, pronouns, birthdate == start_timeline_position as integer world-hours <= 10486470, level = age capped at 99, and >= 9 contextual outfits per GEMINI.md §4.
- **World Lexicon Layer**: Clean leftover NPC entries in the World Lexicon of `_YpX47fNraQFw2dD7TdycJ` only if a matching World Character verifiably exists. Unmatched NPC entries remain. Standalone Lorebooks (the 6 canonical lorebooks) must remain completely untouched.
- **Live Verification**: Chrome DevTools via CDP on `https://app.wyvern.chat/sim/chat_log_PJx1W1rg3WUzRM7MnQrkN` (Stats tab populated, 0 console errors, 0 failed network calls).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Full Pre-Write Backup | Snapshot all characters and full lexicon of `_YpX47fNraQFw2dD7TdycJ` under `scratch/` before any write. | M1 | R1 |
| 2 | Duplicate Resolution | Audit all characters, detect duplicate display_names, delete empty/redundant records (e.g. Finnegan Novak `_7Lkgnm4GyaPTrYfNGn1YT`). | M2 | R2 |
| 3 | Missing-Data Audit Gate | Cross-reference all characters against canonical sources (`lorebooks/optimized/*.json`, `FINAL/`, `scratch/rpg_full_snapshots/`, `scratch/rpg_snapshots/`). Log blocked characters into `scratch/missing_data.md`. | M3 | R3 |
| 4 | Batch Character Completion | Update all valid characters via partial PUTs: RPG stats (sum 31, level <= 99), integer timeline <= 10486470, clean keys, summary/long_summary, >=9 outfits, text rules. | M4 | R4 |
| 5 | World Lexicon Remediation | Delete NPC entries in World Lexicon matching existing World Characters. Keep unmatched entries and list them. | M5 | R5 |
| 6 | Live CDP /sim Validation | Validate on `https://app.wyvern.chat/sim/chat_log_PJx1W1rg3WUzRM7MnQrkN` via CDP: Stats tab character sheets, 0 console errors, 0 network errors. | M6 | R6 |
| 7 | Immutability & Acceptance Verification | Verify standalone lorebooks unchanged, verify all acceptance criteria via independent re-read script, generate completion report. | M7 | R1-R6 |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | World Backup | Create full JSON backup of characters and lexicon in `scratch/` | none | PLANNED |
| 2 | Duplicate Audit & Resolution | Detect and purge duplicate character records | M1 | PLANNED |
| 3 | Missing-Data Audit | Compile canonical data and generate `scratch/missing_data.md` | M2 | PLANNED |
| 4 | Character Completion | Apply partial PUT updates for RPG stats, timeline, outfits, keys, format | M3 | PLANNED |
| 5 | World Lexicon Cleanup | Identify and delete redundant NPC entries from World Lexicon | M4 | PLANNED |
| 6 | Live CDP Validation | Inspect `/sim` Stats tab, console, network via CDP | M4, M5 | PLANNED |
| 7 | Final Verification & Report | Re-read API, audit acceptance criteria, confirm Lorebooks untouched, report to parent | M1-M6 | PLANNED |

## Interface Contracts & Constraints
- Partial PUT only: Wyvern API silent failure on full PUT body. Only send changed fields.
- Date fields: `birthdate` and `start_timeline_position` must be integer hours from epoch 827-12-21 UTC. NEVER ISO string!
- RPG Level: Capped at 99. Base stats sum to 31.
- Outfits: Minimum 9 contextual outfits per GEMINI.md §4 (casual, business/campus, gala/formal, party/club, beach/terme, sleep, nude, hybrid shift/mutation, full shift/other).
- Anatomy rules: Single ear pair for demi-humans; Sierra Cruz has no legs (slithers); Scarlett Rose candy-pink hair/eyes + scarlet horns.
- Text rules: 0 em-dashes (`—`), 0 markdown bold asterisks (`**`), 0 `{{age}}`.
- Standalone lorebooks: IDs `_gwwCxCfQ6PQaLEjAQVpJL`, `_HfG7TeV6MJyj6bxMwxkpt`, `_9zWTGqYJNJ4BCDMj8gfcD`, `_EjXxkmPVhpCXg8xABpFkK`, `_zwEqgEEzh12X6gHVmMKKC`, `_Uht3Ckz44JBDrPnUHq7LV` MUST NOT BE TOUCHED.

## Code Layout
- `scripts/sync_from_wyvern_web.py` (Token extraction helper)
- `scratch/` (Snapshots, missing_data.md, diagnostics)
- `lorebooks/optimized/*.json` & `FINAL/` (Canonical sources)
- `.agents/teamwork/orchestrator_12/` (Orchestrator metadata, BRIEFING.md, progress.md, GATE_STATUS.md)
