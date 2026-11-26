# Synthesis Specification — Svartúlfr World Creation & Deployment

## 1. Executive Summary & Verification Consensus
The Survey & Specification Mining phase (Milestone 1) is 100% complete and validated across three independent exploratory streams:
1. **API & REST Lifecycle**: Token refresh via `scratch/refresh_token.py` (user `2r4fVpvImte5dbljedLkZJxre2d2`, capacity 5 worlds). Mandatory `User-Agent: Mozilla/5.0` to avoid Cloudflare Error 1010. Two-phase World lifecycle: `POST /api/worlds` (creation) $\to$ `PUT /api/worlds/{id}` (full configuration).
2. **Topological Invariant**: Exactly 188 canonical locations in World topology (8 roots, 180 nested nodes, 0 orphans, max depth 4) cleanly partitioned across the 7 canonical Environments:
   - California Coast: 34 locations
   - SUCC campus: 63 locations
   - Solarton: 27 locations
   - Blackwood: 33 locations
   - Seven Hills: 16 locations
   - DMHA HQ & Guild District: 4 locations
   - Voidspace/Otherworld: 11 locations
   - *The Verve*: 808 Neon Avenue, Bluemoon District (`_hfm1W4nYnXfQEqcNGwNxr`), secret entrance behind Logan's Custom Garage with hydraulic mezzanine swap, black market trade, and 3 wired item lexicon entries (`_YxGJRFDkjdVyeH1mJNM1T`, `_UVX1RAqE8CWz8ywYkT4Fm`, `_BRjbkk8JM3Jw1xyJGgzDH`).
3. **Simulation Engine & Anti-Bloat**:
   - 6 JED+ attributes: MGT, RES, AGI, WIT, PRS, SCT (base 1, budget 25).
   - Combat ruleset: `narrative_tiers`, AGI speed initiative, HP/MP vitals, DC 10 base, crit margin 12.
   - Currencies: US Dollar (`$`, primary) and DMHA Guild Credits (`Cr`).
   - Anti-bloat toggles: `show_party_stats: false`, `show_species_info: false`, `ships: false`, `creature_catcher: false`.
   - Level Cap 99 constraint: Mongoose schema bug prevents levels $\ge 100$.
4. **Prompt Assembly & World Clock**:
   - Reference Epoch: `0827-12-21T00:00:00.000Z`
   - World Age: `10489902` hours (26 August 2024, Monday, 06:00:00 UTC).
   - Assistant: `simple_assistant_xRfBnV7wq48QppqbPPpTM` ("Svartúlfr — Game Master & World Engine").
   - Prompt Assembly: `pha_kWkWUAfTJTF9q72c2bC98` ("Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)").
   - Format discipline: dialog in quotes, plain text actions, thoughts in asterisks, zero em-dashes.
5. **Mirrored Lexicon & Linked Characters**:
   - Flags: `selective: true` with `secondary_keys` using `AND_ANY`, `scan_persona: true`, `whole_words_only: true`, `enableEntryHighlighting: true`.
   - Native suppression: `ignored_characters` and `ignored_personas`.
   - Frontend Zod parity: `entries == lexicon`.
   - 8 Linked Characters from `/characters/mine`: Jasper (`_t4J9aQNJM36cUKAP4wB4U`), Erik (`_QPea6g4Q1QfeYCVHCLMPR`), Logan (`_T8Ywcr9FEqNf9JxbK6eHP`), Malachia (`_RDfz7XzTpM23LpPALVXHM`), Noah (`_zFLUjV8aVxQRAfQxGcAcY`), Edric (`_TbRM3EdxDjHFgqztTbCpL`), Wulfnic (`_HEQQbbRFwKdG8QE2Fh1z1`), Mackenzie (`_zn24784jfcchQ7EwCyAnm`).
6. **Chrome DevTools Validation**: Port 9222 discovery via DevToolsActivePort, non-persistent single-client WebSocket session.

---

## 2. Milestones Execution Strategy
- **Milestone 2 (R1 & R2)**: World Core Bootstrap & Simulation Engine Deployment.
  - Step A: Worker creates World via `POST /api/worlds`.
  - Step B: Worker configures World via `PUT /api/worlds/{id}` with world_age 10489902, calendar, prompts, 6 JED+ attributes, combat ruleset, relationship config, currencies, anti-bloat flags, and linked characters.
  - Step C: Worker saves snapshot in `scratch/world_new_snapshot.json`.
- **Milestone 3 (R3)**: 7 Environments & 188 Hierarchical Locations Ingestion.
  - Step A: Worker creates the 7 canonical Environments via `POST /api/worlds/environments`.
  - Step B: Worker ingests and hierarchically links all 188 Locations via `POST /api/worlds/locations` (or bulk) updating parent_location references and environment foreign keys, including The Verve secret bar.
- **Milestone 4 (R4)**: Popolamento Mirrored Lexicon.
  - Step A: Worker bulk-imports lexicon entries with anti-bloat flags (`selective: true`, `secondary_keys`, `ignored_characters`, `ignored_personas`, `scan_persona: true`, `whole_words_only: true`, `enableEntryHighlighting: true`).
  - Step B: Wire `included_lexicon_entries` for hub rooms.
- **Milestone 5 (R5 & Audit)**: DevTools Visual Validation, Review, Challenge & Forensic Audit.
  - Chrome DevTools console/network inspection on port 9222.
  - 2 Reviewers, 2 Challengers, 1 Forensic Auditor.
  - Gate sign-off and final handoff to parent.
