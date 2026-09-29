# Handover Sessione — 29 Settembre 2026

## 1. Stato Attuale del World (Live Wyvern & Repo Locale)
- **World ID:** `_CgYT8fHXpDC4crjmegQF7` (Svartúlfr)
- **World Age Corrente:** `10486470` (5 aprile 2024, ore 06:00 UTC)
- **Conteggio Entità Live:**
  - **Characters:** **104** (G1: 17 Main Cast, G2: 87 Secondari, G3: 0 NPC - sfoltiti/archiviati nel Lexicon)
  - **Locations:** **155** (100% mappate, zero duplicati)
  - **Environments:** **2**
  - **Scenarios:** **11** (100% titolati con catch hook e tagline, location agganciate)
  - **Lexicon Entries:** **569** (zero duplicati, voci grezze epurate, Kobal NPC e nuovi item integrati)
  - **Simulation Features:** Tutte attive (`rpg_stats: true`, `inventory: true`, `currency: true`, `combat: true`, `show_party_stats: true`)

---

## 2. Lavoro Eseguito nella Sessione Odierna

### A. Triage ed Importazione Session Lore da Lorebook Esterno
- **Promozione a Personaggi G2 (5 entità):**
  - **Radek** (`_4bazKCAbPMmc19HzHAphC`): Leader Team Ukiyo / Werewolf Vanguard
  - **Goran** (`_JQGgmwyA3qRaTLWck3GjX`): Tank Team Ukiyo / Minotaur Vanguard
  - **Kian** (`_kc7TyfPDQwUALKXcmTMxQ`): DPS Team Ukiyo / Half-Elf Infiltrator
  - **Barrow ("The Bull")** (`_LEeEzdCCyGjQ8kfVkcra8`): Master Builder, Rappresentante Demi-Umano al Concilio, Guardiano di The Horns
  - **Marek ("The Iron Hammer")** (`_cDx2yGNtVbCCDUCHcUUxG`): Enforcer Ironhorn Nomads / Biker Oni
- **Creazione 7 Nuove Location:**
  - *La Dimora del Rifugio (Safe Haven)*, *Clinica Ortus*, *Cable District*, *Base Operativa Team Ukiyo*, *Club House Ironhorn Nomads*, *Braceria McKay*, *Dungeon Hive Apex Trial*.
- **Creazione 15 Nuove Entry Lexicon:**
  - Kobal integrato come `npc` nel Lexicon (ID `_r2xQZAb9mNkY9wP1LqR7t`).
  - 8 Item equipaggiabili con pannelli e key (`item`): Piuma di Fenice, Nucleo Abissale, Spacca-Incantesimi Prismatico, Elisir Lunare, Amuleto Ancora, Cera d'Api Sacra, Spina Enigmatica, Pass di Gilda SR3S.
  - 6 Fazioni e concetti (`organization/faction` & `lore/concept`): Team Ukiyo, Ironhorn Nomads, Distretto dei Cavi, Marchio di Protezione, Gerarchia dei Dungeon, Protocollo di Sicurezza Gilda.

### B. Risoluzione Doppioni e Pulizia Rimanenze
- **Barrow:**
  - Identificato e risolto il conflitto tra la scheda canonica del Concilio (`_LEeEzdCCyGjQ8kfVkcra8`) e la scheda temporanea creata dall'import (`_V9JeyRrEFDyApmx3rJNeL`).
  - Aggiornato Barrow canonico con tag ricchi, 4 outfit specifici (cantiere, vigilia all'alba, seduta concilio, gilet storico) e 3 attitudes (Alyssa, Marek, Jasper).
  - Reindirizzata l'Attitude di Marek verso l'ID canonico `_LEeEzdCCyGjQ8kfVkcra8`.
  - Eliminata la scheda duplicata (`DELETE /api/worlds/characters/_V9JeyRrEFDyApmx3rJNeL` -> 204).
- **Lexicon Duplicati Grezzi:**
  - Eliminate le entry duplicate grezze contenenti residui di tag XML (`<jean_luc>` e `<dante_nsfw>`):
    - `_M9jgVAFHHMJhYXUcgmhcG` eliminata &rarr; preservata la versione JED+ `_n7zrhF94htP72dqE1xmwV`.
    - `_Padg7gBCkypyY9wVhWV1L` eliminata &rarr; preservata la versione JED+ `_BMADq7QK8eUxEXVh37x7E`.
- **Audit Finale:** Zero doppioni su tutte le tabelle.

### C. Correzione Date di Nascita e Timeline World Clock
- **Risolto Bug di Alyssa:**
  - `birthdate` era corrotto a `-166200` (motivo per cui l'interfaccia web mostrava agosto invece di aprile).
  - Corretto a **`10320312`** (22 aprile 2005, ore 00:00 UTC), perfettamente sincronizzato con il gemello Jasper.
- **Sanate le altre 8 anomalie storiche:**
  - **Edric Douglas** (`_YJQ4cjdrT7brm7HWVkf3K`): `10380312` (25 febbraio 2012, 12 anni esatti).
  - **Elizabeth Duskwood** (`_EwPN1te7qtUKYEx4NLgag`): `9822648` (14 luglio 1948).
  - **Lord Cornelius Douglas** (`_rJKYcCt61hQa8XRamHEdM`): `7044624` (14 agosto 1631; decesso `9018888`, 3 novembre 1856).
  - **Magnus Douglas III** (`_jeJTbxLcrYWXNWYPDx4ph`): `7372272` (29 dicembre 1668).
  - **Marcus Thornfield** (`_PCC1PLfcGrdw2VfMnhVcL`): `10154736` (2 giugno 1986).
  - **Nixara Bloodmoon** (`_fmzBDjDn3Gnq2hXKy7tY6`): `10058472` (9 giugno 1975; decesso `10320312`, 22 aprile 2005).
  - **Ut Berg** (`_NYtBzeKNkm3pedHMnYaka`): `0` (Firstborn consacrato, Epoca).
  - **Fenris** (`_wpMTPQ2VVA2pWqJ3cMztJ`): `0` (Origine primordiale, Epoca).

### D. Scenari Catch Hook Overhaul (11 Scenari)
Rinnovati tutti i titoli e tagline per massimizzare il coinvolgimento narrativo:
1. `_Kn2DFVwyUgkVGz9UWUnBF`: *Fumo di Gomma, Birra e Cloro: Il Branco dei Nomads* (agganciato a *Club House Ironhorn Nomads* `_DJxYBCM7rNrXMj1WracGM`)
2. `_7X4UXynjEUKbQhPDHxVRr`: *Patti nell'Ombra: L'Audizione Segreta con Zeera*
3. `_X86JF72TG4p2DYqw7LzRp`: *Maschere, Brividi e Sorority: Notte di Sangue alla Theta*
4. `_nMaPEAzNA8rQc82NFgXRU`: *Basso Distorto e Sguardi da Lupo: Sabato Sera al Sidewinders*
5. `_XWFqGmaTPkbpbFQzargbf`: *Impatto sul Campo dei Bulls: Lo Scontro con Jared*
6. `_p1Ffq22CTwVywz1CFQBfF`: *Oltre i Cancelli della Villa: Il Primo Passo a Solarton*
7. `_h7N17PhK4ag3GxM8Bgr8g`: *Overclock Notturno: Il Rave Clandestino di DJ Frequency*
8. `_h7UQKNmxNJP8e7Jq1mEVL`: *Asfalto e Libertà: Due Settimane On the Road con Logan*
9. `_F3AKNnAjh2UwUaJe9kc6A`: *L'Ombra del Primo Padre: Il Compleanno dei Gemelli Douglas*
10. `_XwKb3hg1wG7gNgAdfGETr`: *Reclute sotto Scorta: Visita Tattica al Campus SUCC*
11. `_RL8HD1PbxLzNARyrHqqAn`: *Il Bivio del Patriarca: L'Ultima Scelta prima di Maggio*

### E. Configurazione Integrale RPG Simulation (104/104 Personaggi)
- Applicato il sistema RPG secondo la **Regola 8**:
  - Budget fisso a **25 punti** (statistiche base a 1 &rarr; somma totale di `stat_1`..`stat_6` tassativamente a **31**).
  - Livello anagrafico coerente, con **tetto a 99** per gli ultracentenari (elimina il bug di Wyvern che corrompeva il salvataggio per level $\ge 100$).
  - Campi annidati `rpg_stats.species_id` e `rpg_stats.occupation_id` scritti via API.
  - Tratti personalizzati scritti in `character_traits`.
  - Inventari iniziali (`default_inventory`) collegati direttamente agli ID delle voci item del Lexicon (Borsa Medica per Alyssa, Katana e Armatura Abissale per Jasper, Pass di Gilda SR3S per i membri di gilda, armi ancestrali per Ut e Zefir).
- **Copertura finale:** 104 su 104 personaggi configurati e verificati con GET.

### F. Sincronizzazione Locale
- Master Export: `exports/Svartulfr_Export.json` risincronizzato dal vivo (4.076.578 bytes).
- Lorebook Modulari: `exports/lorebooks/` e `exports/entities/` completamente rigenerati.
- Schede Personaggi Locali: `Wyvern/characters/` sincronizzate.

---

## 3. Coda Aperta e Attività per Domani Mattina

1. **Test Sessione Live di Gioco con Simulation Attiva:**
   - Testare in chat su Wyvern il comportamento del bot con la simulation abilitata (gestione inventario in tempo reale, riconoscimento dei tratti di specie ed esiti delle prove sulle statistiche RPG).
2. **Eventuali Rifiniture Outfit e Dettagli Visivi:**
   - Verificare gli avatar delle nuove location o dei nuovi NPC di Gilda se si desidera generare nuove illustrazioni.
3. **Controllo Relazioni e Dinamiche Emergenti:**
   - Monitorare l'evoluzione delle Attitudes tra Alyssa/Jasper e i nuovi membri della Gilda / Ironhorn Nomads (Marek, Barrow, Team Ukiyo).
