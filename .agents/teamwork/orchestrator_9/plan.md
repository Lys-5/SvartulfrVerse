# Plan — Lightweight World Creation & Deployment (orchestrator_9)

## Mission
Create and deploy a new lightweight World on Wyvern Web API supporting the existing ecosystem:
- World Clock: Epoch `827-12-21`, World-Age `10489902` (26 August 2024, Monday, 06:00 UTC).
- Prompt Assembly: Integrated system prompt override, LSE/demi-human directives, final instructions with format discipline and d20 resolution.
- Full Simulation Engine: `rpg_stats`, `combat` (Storyteller/D&D), `inventory`, `currency`, `relationships`, 6 JED+ attributes (MGT, RES, AGI, WIT, PRS, SCT), anti-bloat (`show_party_stats: false`, `show_species_info: false`).
- 7 Environments & 188 Hierarchical Locations: California Coast root, SUCC campus, Solarton, Blackwood, Seven Hills, DMHA HQ & Guild District, Voidspace/Otherworld; 188 locations nested with ambient text and room-specific `included_lexicon_entries` (including The Verve secret bar behind Logan's Custom Garage).
- Mirrored Lexicon & Linked Characters: `selective: true`, `secondary_keys`, `ignored_characters`, `ignored_personas`, parity `entries == lexicon`, linked cards from `/mine`.
- Chrome DevTools Validation: Console, DOM, and network verification on `https://app.wyvern.chat`.

## Milestones

### Milestone 1: Survey & Technical Spec Mining
- Dispatch 3 parallel Explorers:
  - `explorer_world_api`: Inspect Wyvern World API schemas (`POST /api/worlds`, `PUT /api/worlds/{id}`), token scripts, existing world payloads and templates in `scratch/`, `FINAL/`, and `knowledge/`.
  - `explorer_locations`: Inspect the 188 location entries in `FINAL/Svartulfr_Location.json` (`_EjXxkmPVhpCXg8xABpFkK`), verify the 7 Environments mapping, nesting hierarchy, ambient text, and The Verve secret bar wiring.
  - `explorer_simulation_lexicon`: Inspect RPG simulation parameters, D20 + S.P.E.C.I.A.L. / 6 JED+ attributes, prompt assembly integration, linked characters in `/characters/mine`, and Chrome DevTools connection capabilities.
- Synthesize findings into `SPECIFICATION.md`.

### Milestone 2: World Core Bootstrap & Prompt Assembly (R1)
- Worker generates payload and creates new World on Wyvern API with:
  - `human_start_date: "0827-12-21T00:00:00.000Z"`, `world_age: 10489902`
  - System prompt override, LSE/demi-human rules, format discipline, d20 dice mechanics.
- Save snapshot in `scratch/`.

### Milestone 3: Full Simulation Engine Configuration (R2)
- Configure `PUT /api/worlds/{id}`:
  - `rpg_stats: true`, `combat: true`, `inventory: true`, `currency: true`, `relationships: true`
  - 6 attributes: MGT, RES, AGI, WIT, PRS, SCT
  - `show_party_stats: false`, `show_species_info: false`

### Milestone 4: 7 Environments & 188 Hierarchical Locations Ingestion (R3)
- Structure 7 canonical environments with parent-child relationships.
- Ingest and nest all 188 locations without orphan nodes.
- Wire The Verve secret bar behind Logan's Custom Garage.
- Attach room-specific `included_lexicon_entries` and ambient text.

### Milestone 5: Mirrored Lexicon Population & Linked Characters (R4)
- Populate lexicon with anti-bloat filters: `selective: true`, `secondary_keys`, `ignored_characters`, `ignored_personas`, strict parity `entries == lexicon`.
- Link all active character cards from `/characters/mine`.

### Milestone 6: DevTools Visual Validation, Adversarial Challenge & Forensic Audit (R5)
- Inspect live DOM, console, and network on `https://app.wyvern.chat` via Chrome DevTools.
- Reviewers verify full schema compliance and absence of broken references or Zod errors.
- Challengers empirically stress-test the World (time clock, simulation stats, location transitions).
- Forensic Auditor verifies authentic implementation (no mocks, genuine API persistence).
- Gate evaluation and final sign-off.
