# Dispatch Record — Orchestrator 6

## 2026-10-21T14:38:04Z
**From**: Sentinel
**Working directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6`
**Project directory**: `e:\repository\SvartulfrVerse`

You are the Project Orchestrator for the Svartúlfr Verse scenario synchronization, character card reduction to 8, archive restructuring, and NPC Primary Lorebook restoration milestone.

Please read `e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md` for the authoritative requirements and acceptance criteria (latest entry: `## Follow-up — 2026-10-21T14:38:04Z`).

### Summary of Mission:
Esegui la pipeline di sincronizzazione dei 2 scenari SUCC, pulizia e riconfigurazione macro/slot, riduzione a 8 card su Wyvern e in locale, e ripristino dei 6 profili completi NPC nel Lorebook Primary con protezione anti-duplicato Persona per Alyssa e Jasper.

### Requirements:

#### R1. Sincronizzazione Scenari SUCC e Pulizia Archivio
- Scaricare da Wyvern API i 2 scenari: `char_scenario_CKgwq246DyCj1NNTBV9rt` (Alyssa rev 10) e `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` (Jasper rev 4).
- Creare la directory `ARCHIVIO/scenarios/` e spostarvi i 4 file degli scenari cancellati su Wyvern (Camp Mystic, DMHA, Underworld, Villa Douglas).
- Salvare le versioni aggiornate dei 2 scenari in `FINAL/scenarios/`.

#### R2. Ottimizzazione Macro e Slot degli Scenari
- Nei testi dei saluti (greetings), sostituire le macro `{{scenarioChar "..."}}` relative ai personaggi diventati NPC (Scarlett, Russ, Jared, Stan, Sierra) con i loro nomi letterali.
- Rimuovere dagli scenari i pool di card inaccessibili (`unavailable_count: 1`) per evitare blocchi Wyvern.
- Per gli slot mittenti dei messaggi (speaker_slot), assicurarsi che la configurazione rimanga valida ed esente da errori di risoluzione.
- Eseguire il deploy via `PUT` delle versioni ottimizzate su Wyvern API.

#### R3. Riduzione Card Personaggio (Esattamente 8 Card)
- Inviare richiesta `DELETE` via Wyvern API per rimuovere Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`) da `/characters/mine`.
- Verificare che su Wyvern `/characters/mine` rimangano esattamente le 8 card approvate: Erik, Malachia, Jasper, Noah, Edric, Logan, Wulfnic, Mackenzie.
- Creare la directory `ARCHIVIO/cards_legacy/` e spostarvi le 6 card dismesse da `FINAL/` (`Alyssa`, `Jared`, `Russ`, `Scarlett`, `Sierra`, `Stan`).

#### R4. Ripristino dei 6 Profili NPC in Svartulfr_NPC_Primary
- In `FINAL/Svartulfr_NPC_Primary.json`, popolare con le descrizioni JED+ complete delle card originali i 6 record target:
  - `Scarlett Rose` (`4NzXF4_0hYxmN7Idltzpw`): `type: "npc"`, `selective: false`, avatar, multiline regex, `npc_info`.
  - `Sierra Cruz` (`ijy8vrlphNv19-p-gbYuY`): `type: "npc"`, `selective: false`, avatar, multiline regex, `npc_info`.
  - `Russell 'Russ' Sinclair` (`YCxAqNoShpefVvk0_Pc7i`): `type: "npc"`, `selective: false`, avatar, multiline regex, `npc_info`.
  - `Stanley Davies Jr.` (`ekdQjq63xP7HtNuaPQJQE`): `type: "npc"`, `selective: false`, avatar, multiline regex, `npc_info`.
  - `Jared Thompson` (`RM6rcwv8MlY1XWaCTQp0M`): `type: "npc"`, `selective: false`, avatar, multiline regex, `npc_info`.
  - `Alyssa Hvit Douglas Bloodmoon` (`alyssa_world_dossier_2b54a223`): descrizione JED+ integrale della card, avatar valido, ma mantenendo la protezione anti-duplicato Persona (`selective: true`, `secondary_keys: ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`, `key_logic: 'AND_ANY'`) identica a Jasper (`Vcj4h2TL4Usola2A4OOl6`) per impedire che si attivi come entità spuria quando il giocatore usa la Persona Alyssa.
- Eseguire il deploy via `PUT` del Lorebook `_zwEqgEEzh12X6gHVmMKKC` su Wyvern API.

#### R5. Validazione DevTools e Controllo di Regressione
- Eseguire chiamate GET di verifica su tutti gli endpoint Wyvern (`/characters/mine`, `/character-scenarios/{id}`, `/lorebooks/{id}`).
- Verificare la corretta formattazione secondo le regole del repository (niente em-dash, dialoghi con virgolette, nessuna keyword ombrello).

### Acceptance Criteria:
- [ ] Entrambi gli scenari SUCC in `FINAL/scenarios/` e su Wyvern rispondono con HTTP 200 e zero macro orfane.
- [ ] `ARCHIVIO/scenarios/` contiene i 4 scenari ritirati, e `FINAL/scenarios/` contiene solo i 2 SUCC attivi.
- [ ] `/characters/mine` su Wyvern contiene esattamente le 8 card approvate.
- [ ] `FINAL/` contiene solo i file JSON delle 8 card approvate; le 6 card rimosse sono in `ARCHIVIO/cards_legacy/`.
- [ ] Le 6 voci in `Svartulfr_NPC_Primary.json` hanno descrizioni JED+ piene (> 2.000 caratteri).
- [ ] Alyssa ha `selective: true` con chiavi Dossier coerenti con Jasper per prevenire collisioni Persona.
- [ ] Scarlett, Sierra, Russ, Stan e Jared hanno `type: "npc"`, avatar valido e regex multiline.
- [ ] Wyvern API restituisce HTTP 200 sul Lorebook `_zwEqgEEzh12X6gHVmMKKC`.

Maintain your `progress.md` and `BRIEFING.md` in your working directory (`e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6`).

## 2026-10-21T14:40:23Z
**From**: Parent Orchestrator (00115cad-54ea-4c06-bcc6-cb5497e31a8c)
**Working directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_6`
**Project directory**: `e:\repository\SvartulfrVerse`

You are the Project Orchestrator for Svartúlfr Verse.
Mission Requirements:
1. R1. Sincronizzazione Scenari SUCC e Pulizia Archivio: scarica i 2 scenari SUCC da Wyvern API (Alyssa rev 10 e Jasper rev 4), crea ARCHIVIO/scenarios/ e spostavi i 4 scenari cancellati da Wyvern, salva i 2 scenari attivi in FINAL/scenarios/.
2. R2. Ottimizzazione Macro e Slot degli Scenari: sostituisci le macro {{scenarioChar "..."}} relative ai personaggi diventati NPC con nomi letterali, rimuovi i card pool inaccessibili (unavailable_count: 1), valida speaker_slot e deploya via PUT su Wyvern API.
3. R3. Riduzione Card Personaggio: elimina Jared Thompson da /characters/mine via DELETE Wyvern API, verifica che rimangano esattamente le 8 card approvate, crea ARCHIVIO/cards_legacy/ e sposta le 6 card dismesse da FINAL/.
4. R4. Ripristino dei 6 Profili NPC in Svartulfr_NPC_Primary: popola i 6 record target con descrizioni JED+ complete (>2000 caratteri), tipo npc, avatar e multiline regex, mantenendo per Alyssa la protezione anti-duplicato Persona (selective: true, secondary_keys Dossier coerenti con Jasper), e deploya via PUT il Lorebook Primary su Wyvern API.
5. R5. Validazione DevTools e Controllo di Regressione: GET di verifica su tutti gli endpoint Wyvern (/characters/mine, /character-scenarios/{id}, /lorebooks/{id}), verifica formattazione (no em-dash, virgolette nei dialoghi, nessuna keyword ombrello).

## 2026-10-21T14:58:37Z
**From**: User Directive Update via Sentinel / Parent
**Content**:
USER DIRECTIVE UPDATE & NATIVE WYVERN SCHEMA:
The user has instructed to apply Wyvern's native "DON'T ACTIVATE WHEN ACTIVE" feature (`ignored_personas` and `ignored_characters` arrays on lorebook entries) to suppress lorebook entries when a character or persona is already active in chat, eliminating the need for the dummy `selective: true` / Dossier keyword workaround.

Native schema fields on lorebook entries:
- `ignored_characters`: list of character card IDs (strings)
- `ignored_personas`: list of persona IDs (strings)

This enables Alyssa and Jasper to be full active `type: "npc"`, `selective: false` with complete JED+ profiles, since Wyvern natively skips the entry whenever the player uses their Persona or when their card is in the chat/party!

All 8 active cards and all converted former cards have their IDs set in `ignored_characters`, and personas in `ignored_personas`. Instructions have been forwarded to Worker R6-1.
