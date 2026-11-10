# Project: Svartúlfr Verse Emergent Lore Integration

## Architecture
The Svartúlfr Verse knowledge and narrative ecosystem is organized according to the Second Brain / LLM Wiki 2026 tri-tier architecture (Rule 15):
- **Tier 1 (Sources)**: Raw interaction transcripts and session exports (`scratch/chat_export_ftrtAD79eddk9Ue9Jr2WJ.json`, `ARCHIVIO/`).
- **Tier 2 (Compiled Canonical Knowledge)**:
  - Human-readable knowledge vault articles in `knowledge/Lore_Worldbuilding/` (modular markdown, wikilinked).
  - Machine-readable 6 Standalone Lorebooks in `FINAL/` and `lorebooks/optimized/` (`entries == lexicon` parity, token budgets 5000/7500).
  - Standalone Character Cards in `FINAL/` and legacy archives in `ARCHIVIO/cards_legacy/` (JED+ format).
  - User Personas in `FINAL/personas/` (JED+ format).
  - World master snapshot in `docs/world/Svartulfr_World_Doc.md`.
- **Tier 3 (Procedural Rules & Schemas)**: Rules codified in `.agents/rules/` and `GEMINI.md`.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | St. Brugge Private Academy | Gothic prep academy, curriculum (magic, history, alchemy, demonology, runes), attendance of Alyssa & Jasper | M1, M2, M3 | Request, Chat Msg 44-45 |
| 2 | Father Revazhael (Superior Demon) | Ancient Superior Demon, St. Brugge mentor to twins, master of abyssal arts & crystallography, true name secret, ARO member/TIT handyman | M1, M2, M3 | Request, Chat Msg 44-45 |
| 3 | Applied Runic Crystallography | Science fusing Elder Futhark with crystal lattices to suspend/freeze spells losslessly | M1, M2 | Request, Chat Msg 42-45 |
| 4 | Enchanted Resonant Cylinders | Handcrafted flashlight-sized crystal cylinders storing frozen spells, snap activation, individual resonance tuning vs fragile DMHA cylinders | M1, M2, M3 | Request, Chat Msg 42-45 |
| 5 | Abyssal Magic vs Void Magic/Necromancy | Chthonic infernal energy of Superior Demons vs entropic/cold soul magic of Void & Necromancy | M1, M2 | Request, Chat Msg 44-45 |
| 6 | Alyssa Guild Healer & Dungeon Medic | Certified Guild Healer (Rank A, Hunter ID ADB-555), SR3S clearance, dungeon support, Pre-Med at SUCC, Pacifist Vow, crystal glassware | M1, M2, M3 | Request, Chat Msg 42-45 |
| 7 | Jasper Hunter & Runic Translator | Registered Guild Hunter (Rank A, Support/Infiltrator, JDB-555), Sound & Acoustic Engineering, runic translation, harmonic tuning, KSA intimidation | M1, M2, M3 | Request, Chat Msg 25, 42-45 |
| 8 | Theta Iota Theta Suite 3 & Roommates | Suite 3 environment: Sierra Cruz (4m rainbow lamia, limbless locomotion, Grave Mistake poster), Alyssa fur nest & Wolfy plush, Scarlett Rose | M1, M2 | Chat Msg 24-41 |
| 9 | DCC Security & SUCC Campus Integration | Rector Wolfwood pact with Erik Douglas (Bears head coach), Major Kaladin Nargathon coordinating with Chief Warg, biometric drones | M1, M2 | Chat Msg 13-18 |
| 10 | Standalone Lorebook Hygiene & Parity | Byte-for-byte identity `entries == lexicon`, purge broad keys on St. Brugge Location #51, fix Larek Steeltooth #211 schema | M2, M4 | Survey 2 |
| 11 | Character Card & Persona Alignment | Jasper Level 19 fix, removal of outdated collarbone markings, removal of "Novice Healing Mage" label | M3, M4 | Survey 3 |
| 12 | Comprehensive Verification & Integrity Audit | Multi-tier test scripts, zero em-dash, positive framing, forensic audit veto gate, CHANGELOG.md | M4 | Project Pattern |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Vault Second Brain Knowledge Documentation | 6 new modular markdown articles in `knowledge/Lore_Worldbuilding/` + index update | None | DONE |
| M2 | Standalone Lorebooks Emergent Lore Integration | Lorebook I, II, III, Location, NPC Secondary, NPC Primary JSON updates in `FINAL/` and `lorebooks/optimized/` | M1 | DONE |
| M3 | Character Cards & Personas Synchronization | `Jasper_Douglas_Bloodmoon_card.json`, `Alyssa_Douglas_Bloodmoon_card.json`, personas in `FINAL/personas/` | M1, M2 | DONE |
| M4 | Comprehensive Verification, Schema Parity & Forensic Audit | Verification scripts, formatting compliance, adversarial check, forensic audit veto gate, CHANGELOG.md | M1, M2, M3 | IN_PROGRESS |

## Interface Contracts
### Knowledge Vault ↔ Standalone Lorebooks
- Every entity, institution, and discipline defined in `knowledge/Lore_Worldbuilding/` must match exact names and definitions in the corresponding Lorebook JSON entries.
- Activation keys in Lorebooks must directly reflect canonical names in Vault articles.
- No broad/umbrella keywords (`solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega`) allowed on NPC entries.

### Standalone Lorebooks ↔ Character Cards & Personas
- JED+ 4-block layout (`[...]` -> `BACKSTORY:` -> `FAMILY & PACK:` / `CLAN AND COMPANY:` -> `VOICE & BEHAVIOR:`) must match across Cards, Personas, and Lorebook Dossiers.
- Single-line PList header `[...]`.
- Native suppression via `ignored_characters` and `ignored_personas` maintained on all NPC Primary/Secondary entries to prevent player collisions.
- `entries == lexicon` byte-for-byte identity in all JSON lorebooks.

### Text & Tone Formatting Discipline
- Zero em-dashes (`—`), use commas or periods.
- Dialogue enclosed strictly in standard double quotes (`"..."`).
- Actions and narration in plain text (no markdown asterisks `*` or `**`).
- Positive framing only for demi-human anatomy (single pair of animal ears on crown, never mention absence of human ears; Sierra Cruz moves by slithering with 4m rainbow serpent coils, zero legs/feet).
- World Clock: Year 2024, World-Age 10486470 / 10489902. Zero Date Reset.

## Code Layout
- `knowledge/Lore_Worldbuilding/`: Markdown Second Brain encyclopedia articles.
- `FINAL/`: Authoritative Character Cards (`*_card.json`), User Personas (`personas/*.json`), and standalone Lorebooks (`Svartulfr_Lorebook_*.json`, `Svartulfr_NPC_*.json`).
- `lorebooks/optimized/`: Standalone Lorebook mirrors (`Svartulfr_Lorebook_*.json`, `Svartulfr_NPC_*.json`, `Svartulfr_Location.json`).
- `ARCHIVIO/cards_legacy/`: Legacy/reference character cards (`Alyssa_Douglas_Bloodmoon_card.json`).
- `docs/world/`: Monolithic reference snapshot (`Svartulfr_World_Doc.md`).
- `scripts/`: Verification, audit, and sync utility scripts.
