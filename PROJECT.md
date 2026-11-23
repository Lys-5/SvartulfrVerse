# Project: Svartúlfr Verse Daily Action Plan (5-Block Master Pipeline)

## Architecture
The Svartúlfr Verse architecture operates on the Second Brain / LLM Wiki 2026 tri-tier architecture (Rule 15):
- **Tier 1 (Sources)**: Raw interaction transcripts, session exports, and historical documents in `ARCHIVIO/03_Claude_Docs_and_Memories/`.
- **Tier 2 (Compiled Canonical Knowledge)**:
  - Knowledge vault articles in `knowledge/Lore_Worldbuilding/` and staged recoveries in `knowledge/Archive_Recoveries/`.
  - Machine-readable Standalone Lorebooks in `FINAL/` and `lorebooks/optimized/` (`entries == lexicon` parity, token budgets 5000/7500).
  - Standalone Character Cards in `FINAL/` (JED+ format, 9 outfits minimum, S.P.E.C.I.A.L. stats).
  - User Personas in `FINAL/personas/` (JED+ format, 3+ appearances minimum).
  - Live Platform Parity: Synchronized to https://app.wyvern.chat/mine via Wyvern Web API (`scripts/wyvern_api_client.py`).
- **Tier 3 (Procedural Rules & Schemas)**: Rules codified in `.agents/rules/` and `GEMINI.md`.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Vault Health Engine & Parity Alignment | Zero critical errors on `vault_health_check.py`, token auto-refresh in `wyvern_api_client.py`, Location Lorebook parity (226 entries), Lorebook I parity (242 entries), and User Persona parity | M1 | Survey 1 |
| 2 | Priority NPC JED+ Enrichment & Positive Framing | Enrich Vero Walker, Warg, Vargus "The Red", Bartholomew, and Madge in JED+ format, eliminating negative framing echoes, fixing copy-paste defects (Orco/Macchina) | M2 | Survey 2 |
| 3 | Priority NPC S.P.E.C.I.A.L. & Taxonomy Alignment | Apply 31-species taxonomy (`werewolf`, `orcs`, `human`), S.P.E.C.I.A.L. allocations, Level formulas, and combat traits across the 5 NPCs | M2 | Survey 2 |
| 4 | NPC Lorebook Synchronization | Update `FINAL/` and `lorebooks/optimized/Svartulfr_NPC_Secondary.json` with `entries == lexicon` byte parity and deploy to live lorebook `_Uht3Ckz44JBDrPnUHq7LV` via Web API (anti-413 payload) | M2 | Survey 2 |
| 5 | Historical Archive Lore Mining Batch | Extract and sanitize unmined lore from `03_Claude_Docs_and_Memories` (`Douglas_Family_Register.md`, `Pack_Mom_La_Nursery_E_Elizabeth.md`, `Censimento_Secondo_Genere_E_Prime_Non_E_Un_Rango.md`) into `knowledge/Archive_Recoveries/` | M3 | Survey 3 |
| 6 | Session Standards & DDM Contractor Compliance | Enrich 8 DDM Contractor cards (`Richard Whitlock`, `Hana Valencia`, `Adam Valencia`, `Luka Sutter`, `Dullahan`, `Johan Jakobsen`, `Fenrir`, `Jasper Contractor`) with standard RPG headers and 9 contextual outfits | M4 | Survey 1 |
| 7 | Chat Name & Persona Hygiene | Set `chat_name` on Larek Steeltooth and Mackenzie Fantasy, export live persona `user_persona_xRpkh3JVPkhnpWbcBBfa6` to `FINAL/personas/Alyssa_DDM_Contractor_Persona.json` | M4 | Survey 1 |
| 8 | Missing Image Asset Batch Delivery | Process image assets for Kian, Goran, Radek, Eric, and Javier Reyes: upload existing high-res local images from `assets/characters/secondary_cast/` via Wyvern Cloudflare API, link to lorebook `_zwEqgEEzh12X6gHVmMKKC`, and document PixAI prompt specifications | M5 | Survey 3 |
| 9 | End-to-End Verification & Audit | Verify 100% check pass on `vault_health_check.py`, verify live platform parity across cards, personas, and lorebooks, verify positive framing, and obtain Forensic Auditor CLEAN verdict | M1-M5 | Project Pattern |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Vault Maintenance and Live Platform Parity | Token refresh, Location & Lorebook I parity, Persona parity, initial health check audit | None | DONE |
| M2 | NPC Roster and Lorebook Advancement | JED+ enrichment, S.P.E.C.I.A.L. stats, positive framing, and live sync of the 5 priority NPCs | M1 | DONE |
| M3 | Historical Archive Lore Mining | Mining batch from `03_Claude_Docs_and_Memories` into `knowledge/Archive_Recoveries/` | None | DONE |
| M4 | Session Standards & Special Tasks Compliance | 8 Contractor cards 9 outfits + RPG headers, chat_name compliance, live persona export, 0 critical errors on vault health check | M1, M2 | DONE |
| M5 | Missing Image Asset Creation Batch | Upload & link 5 image assets to Wyvern CDN and document ready-to-run PixAI prompt specifications | M2 | DONE |

## Interface Contracts
### Knowledge Vault ↔ Standalone Lorebooks
- Canonical entities in `knowledge/` and `knowledge/Archive_Recoveries/` match Lorebook entries.
- Activation keys in Lorebooks reflect exact names.
- Zero broad/umbrella keys (`solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega`).

### Standalone Lorebooks ↔ Character Cards & Personas
- JED+ 4-block layout (`[...]` -> `BACKSTORY:` -> `FAMILY & PACK:` / `CLAN AND COMPANY:` -> `VOICE & BEHAVIOR:`) + closing thematic block.
- Single-line PList header `[...]`.
- `entries == lexicon` byte-for-byte identity in all local JSON lorebooks.
- Anti-HTTP 413 strategy on Wyvern API: send `lexicon` + top-level config fields in PUT, omitting duplicate `entries` array on the wire.

### Text & Tone Formatting Discipline
- Zero em-dashes (`—`), use commas or periods.
- Dialogue enclosed strictly in standard double quotes (`"..."`).
- Actions and narration in plain text (no markdown asterisks `*` or `**`).
- Positive framing only for demi-human anatomy (single pair of animal ears on crown, never mention absence of human ears; Sierra Cruz moves by slithering with 4m rainbow serpent coils, zero legs/feet).
- World Clock: Year 2024, World-Age 10486470. Zero Date Reset.

## Code Layout
- `knowledge/Archive_Recoveries/`: Staged Second Brain recovered markdown articles.
- `assets/characters/secondary_cast/`: Local character artwork assets.
- `FINAL/`: Authoritative Character Cards (`*_card.json`), User Personas (`personas/*.json`), and standalone Lorebooks (`Svartulfr_*.json`).
- `lorebooks/optimized/`: Standalone Lorebook mirrors (`Svartulfr_*.json`).
- `scripts/`: Verification, audit, and sync utility scripts (`vault_health_check.py`, `wyvern_api_client.py`, `archive_mining_engine.py`, etc.).
