# DISPATCH — 2026-10-24T22:20:00Z

You are the Project Orchestrator (orchestrator_9) for SvartulfrVerse.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_9
The authoritative user request is recorded in: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md

Your mission is to orchestrate and execute all requirements specified under the latest user request (timestamp 2026-10-24T22:18:38Z):

## Requirements

### R1. Bootstrap & Configurazione World Core
Creare un nuovo World dedicato su Wyvern con epoch `827-12-21`, World-Age `10489902` (26 Agosto 2024, lunedì, ore 06:00 UTC), e Prompt Assembly integrato (system prompt override, direttive LSE/demi-umani e final instructions con format discipline e risoluzione d20).

### R2. Full Simulation Engine Configuration
Configurare i moduli di simulazione su `PUT /api/worlds/{id}` attivando `rpg_stats`, `combat` (stile Storyteller/D&D), `inventory`, `currency`, `relationships`, impostando i 6 attributi JED+ (MGT, RES, AGI, WIT, PRS, SCT) e prevenendo il context bloat (`show_party_stats: false`, `show_species_info: false`).

### R3. Ingestione dei 7 Environment & 188 Locations Gerarchiche
Mappare e strutturare la topologia completa sui 7 Environment canonici:
1. California Coast (Root: LA, Bakersfield, Ventura, Hex Valley, Route 101)
2. SUCC campus (Parent: California Coast — 129 Hocus Way, aule, dormitori, laboratori, impianti sportivi)
3. Solarton (Parent: California Coast — Solarton Square, Bricklane Mall, Sidewinders, residenziale)
4. Blackwood (Parent: California Coast — Uptown, Arcadia, Bluemoon, Oldtown, Dockside, Ironworks, Bloodmoon Forest)
5. Seven Hills (Parent: Blackwood — Quartiere residenziale del Branco, Villa Douglas, tenuta e campi di addestramento)
6. DMHA HQ & Guild District (Parent: California Coast / Simi Valley — epicentro disturbi magici e apertura delle faglie dei dungeon, comando cacciatori DMHA, taglie, armerie runiche, CCD)
7. Voidspace/Otherworld (DDM Inc., Dead Dog Motel, Trial Dungeons 1-18, fratture di realtà generate dalle faglie)
Distribuire e annidare le 188 location canoniche (incluso The Verve secret bar sul retro di Logan's Custom Garage) con ambient text e cablaggio delle `included_lexicon_entries` specifiche per ogni nodo.

### R4. Popolamento Mirrored Lexicon & Linked Characters
Importare le voci di Lexicon con flag anti-bloat (`selective: true`, `secondary_keys`, `ignored_characters`, `ignored_personas`, parità `entries == lexicon`) e collegare le Character Card da `/mine`.

### R5. Validazione Visiva con Chrome DevTools
Validare il World su Wyvern ispezionando console, DOM e network requests per confermare l'assenza di errori di schema Zod o broken references.

## Acceptance Criteria
- [ ] Nuovo World creato con ID univoco e snapshot salvato in `scratch/`.
- [ ] Parametri temporali corretti (`world_age: 10489902`, 26 Agosto 2024, lunedì, ore 06:00 UTC).
- [ ] 7 Environment configurati e 188 Locations mappate senza nodi orfani.
- [ ] The Verve configurato come secret bar con ingresso sul retro del Logan's Custom Garage.
- [ ] Lexicon popolato con flag `ignored_characters` e parità `entries == lexicon`, con `included_lexicon_entries` cablate per stanza.
- [ ] Simulazione attiva con 6 statistiche JED+ e combat abilitato.
- [ ] Ispezione browser (console + network) priva di errori di validazione o 4xx/5xx.

Maintain your plan.md and progress.md in your working directory, coordinate your subagents according to GEMINI.md and project rules, and report back when finished.
