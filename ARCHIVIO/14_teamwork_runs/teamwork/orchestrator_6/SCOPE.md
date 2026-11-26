# SCOPE — Svartúlfr Verse: Scenarios Sync, Card Reduction to 8, Lorebook Primary Restoration & Regression Verification

## Target Milestone
Pipeline di sincronizzazione dei 2 scenari SUCC, pulizia e riconfigurazione macro/slot, riduzione a 8 card su Wyvern e in locale, ripristino dei 6 profili completi NPC nel Lorebook Primary con protezione nativa anti-duplicato Wyvern ("DON'T ACTIVATE WHEN ACTIVE" via `ignored_personas` e `ignored_characters`) per Alyssa e Jasper, deploy via Wyvern API e validazione di regressione.

## Feature Inventory & Requirements

| # | Requirement | Scope & Description | Target Entity / File | Status |
|---|-------------|---------------------|----------------------|--------|
| R1 | Sincronizzazione Scenari SUCC e Pulizia Archivio | Scaricare 2 scenari da Wyvern API (Alyssa rev 11: `char_scenario_CKgwq246DyCj1NNTBV9rt`, Jasper rev 5: `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`). Creare `ARCHIVIO/scenarios/` e spostarvi i 4 scenari cancellati da Wyvern (Camp Mystic, DMHA, Underworld, Villa Douglas). Salvare i 2 scenari aggiornati in `FINAL/scenarios/`. | `FINAL/scenarios/`, `ARCHIVIO/scenarios/` | DONE |
| R2 | Ottimizzazione Macro e Slot degli Scenari | Sostituire macro `{{scenarioChar "..."}}` relative a NPC (Scarlett, Russ, Jared, Stan, Sierra) con nomi letterali. Rimuovere card pool inaccessibili (`unavailable_count: 1`). Convalidare `speaker_slot` e deployare via PUT su Wyvern API. | `char_scenario_CKgwq246DyCj1NNTBV9rt`, `char_scenario_Kq4mJEBH83j7Q7DdVfFnF` | DONE |
| R3 | Riduzione Card Personaggio (Esattamente 8) | Inviare DELETE via Wyvern API per rimuovere Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`) da `/characters/mine`. Verificare che rimangano esattamente le 8 card approvate: Erik, Malachia, Jasper, Noah, Edric, Logan, Wulfnic, Mackenzie. Creare `ARCHIVIO/cards_legacy/` e spostarvi le 6 card dismesse da `FINAL/` (`Alyssa`, `Jared`, `Russ`, `Scarlett`, `Sierra`, `Stan`). | Wyvern `/characters/mine`, `FINAL/`, `ARCHIVIO/cards_legacy/` | DONE |
| R4 | Ripristino 6 Profili NPC in Svartulfr_NPC_Primary | In `FINAL/Svartulfr_NPC_Primary.json`, popolare con descrizioni JED+ complete (>2000 caratteri) i 6 record: Scarlett Rose, Sierra Cruz, Russell 'Russ' Sinclair, Stanley Davies Jr., Jared Thompson, Alyssa Hvit Douglas Bloodmoon. Applicare lo schema nativo Wyvern "DON'T ACTIVATE WHEN ACTIVE" (`ignored_personas` e `ignored_characters`) per Alyssa e Jasper, consentendo `type: 'npc'` e `selective: false` senza workaround Dossier. Deploy via PUT di `_zwEqgEEzh12X6gHVmMKKC` su Wyvern API. | `FINAL/Svartulfr_NPC_Primary.json`, Lorebook `_zwEqgEEzh12X6gHVmMKKC` | DONE |
| R5 | Validazione DevTools e Controllo di Regressione | GET di verifica su tutti gli endpoint Wyvern (`/characters/mine`, `/character-scenarios/{id}`, `/lorebooks/{id}`). Verificare formattazione (no em-dash, dialoghi con virgolette, nessuna keyword ombrello). Aggiornare `CHANGELOG.md`. | Wyvern API & `CHANGELOG.md` | DONE |

## Milestones & Status
| # | Step | Description | Status |
|---|------|-------------|--------|
| 1 | Survey & Discovery | 3 Explorers analizzano live API, token, file locali, slot, macro, card IDs e Lorebook Primary | DONE |
| 2 | Implementation | Worker esegue R1, R2, R3, R4, R5, aggiorna file locali, deploya via API Wyvern e aggiorna CHANGELOG | DONE |
| 3 | Review | 2 Reviewers indipendenti verificano schema, conformità API, integrità JED+, macro e card | DONE |
| 4 | Challenge | 2 Challengers testano edge case, chiamate API live, assenza macro orfane, e conteggio esatto card | DONE |
| 5 | Forensic Audit | Auditor forense verifica autenticità chiamate API, non-hardcoding, e piena conformità regole | DONE |
| 6 | Gate & Handoff | Valutazione unanime del gate in GATE_STATUS.md (PASS) e handoff finale al parent | DONE |
