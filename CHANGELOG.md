# Changelog di Progetto — Svartúlfr Verse

Tutte le modifiche, gli aggiornamenti di sistema, le revisioni di Lore, i deploy dello StoryEngine e gli interventi sulle entità del World (World, Lexicon, Locations, NPC, Rules) sono tracciati cronologicamente in questo documento per garantire persistenza e coerenza storica tra le sessioni.

## [15 Ottobre 2026] - Character Card V2 dei Personaggi Principali (Main Cast)

- **Generazione card**: creato `scripts/generate_main_cast_cards.py`, che genera le 5 **Character Card V2** (`spec: chara_card_v2`, lo stesso formato che Wyvern esporta come PNG) dei personaggi principali — Erik Douglas, Logan Douglas, Jasper Douglas Bloodmoon, Malachia Douglas Bloodmoon, Noah Douglas Bloodmoon — e le salva in `FINAL/` (`Erik_Douglas_card.json`, `Logan_Douglas_card.json`, `Jasper_Douglas_Bloodmoon_card.json`, `Malachia_Douglas_Bloodmoon_card.json`, `Noah_Douglas_Bloodmoon_card.json`).
- **Fonte dati**: export live del World (`exports/Svartulfr_Export.json` → `world_characters`; `description = long_summary`, `personality = summary`) arricchito con gli scenari/first_mes/system_prompt autoriali della pipeline storica (`scripts/sync_characters_cards.py`).
- **Regole applicate (scelte utente)**: tag **canonici World**; `mes_example` costruito dai 5 `speech_examples` di ciascuno; **nessun Lorebook collegato** (`character_book` omesso); outfits inclusi in `extensions.outfits` con correzione dell'anomalia della fonte (`{{user}}` → nome personaggio, es. Jasper). `post_history_instructions` = `final_instructions` del World + disciplina di formattazione; `extensions` include `outfits`, `attitudes`, `rpg_stats`, `birthdate`, `start_timeline_position`, `keys`, `depth_prompt`.
- **Anomalia dati segnalata**: i tag canonici del World per **Erik** sono ridotti al solo `blackwood` (i fratelli ne hanno 5-10), lasciati invariati come da scelta "tag canonici World".
- **Documentazione**: aggiornati `README.md` (albero §1 e nuova sottosezione "Character Card V2 (Main Cast)" in §3).

## [15 Ottobre 2026] - Conversione dei Lorebook in Formato Lexicon & Estrazione NPC Secondary

- **Conversione formato**: i file di `FINAL/` passano dal formato `entries` (SillyTavern) al formato **Lexicon** (oggetto lorebook con array `lexicon`: `name`, `description`, `scan_depth`, `token_budget`, `recursive_scanning`, `lexicon`). Nuovo script `scripts/convert_to_lexicon.py`, che usa come base le entry Lexicon dello snapshot del sito (`scratch/backup_consolidated_snapshot/lorebook_*.json`, allineate 1:1 per indice) e rilegge i campi mutabili dal file ottimizzato.
- **Mappatura campi**: `comment → name`, `key → keys`, `keysecondary → secondary_keys`, `disable → enabled` (invertito), `caseSensitive → case_sensitive`, `matchWholeWords → whole_words_only`, `matchPersonaDescription → scan_persona`, `selectiveLogic → key_logic`, `probability → activation_chance`, `extensions.rpg → extensions.rpg`; i campi `extensions.wyvern.{position, insertion_order, priority, provenance, regex_patterns}` promossi a top-level; `type = "npc"` con blocco `npc_info` per le schede personaggio.
- **Estrazione NPC**: creato `FINAL/Svartulfr_NPC_Secondary.json` (314 voci `type: npc`) raccogliendo le schede dai Lorebook I (32), II (106) e III (176) e rimuovendole dalle origini. `Svartulfr_NPC_Primary.json` (113) lasciato invariato. Inclusi anche 3 NPC tipizzati come tali sul sito ma privi dell'header `[NAME:` (Bruce, Campus Staff Rat, Adrian — Lorebook II).
- **Esiti**: `FINAL/` ora contiene 6 Lorebook in formato Lexicon — Lorebook_I (220), Lorebook_II (144), Lorebook_III (26), Location (196), NPC_Primary (113), NPC_Secondary (314). Le versioni `entries` restano recuperabili in `lorebooks/optimized/` e `lorebooks/source/`.
- **Documentazione**: aggiornati `README.md` (albero cartelle §1 e pipeline §3 con il nuovo stadio 4).

## [15 Ottobre 2026] - Riorganizzazione Repository & Consegna Lorebook FINAL

- **Riorganizzazione Strutturale del Repository**:
  - Ripulito il root: i file sciolti (script ad-hoc `extract*.py`, `fix.py`, `script.py`, dump e ispezioni JSON/TXT) spostati in `scratch/inbox/`; gli input scraping JanitorAI (`janitor_links.txt`, `janitor_ids.txt`, `scraped_characters_batch.json`) in `scratch/scraping/`; le mappe (`map_blackwood.jpg`, `map_california.jpg`) in `asset/environments/`.
  - Nuova cartella `lorebooks/` con pipeline `source/` (5 export grezzi), `optimized/` (5 output Fase 1) e `standalone/` (lorebook non-World).
  - `logs/` ridotta ai soli log di sessione (`logs/chat/`); rimossa la vecchia `logs/wyvern_ottimizzati/` (confluita in `lorebooks/optimized/`).
  - `docs/` riorganizzata in sottocartelle tematiche: `data/`, `guides/`, `lexicon/`, `proposals/`, `world/`. Lo snapshot `snapshots_2026-10-03/` spostato in `ARCHIVIO/05_Snapshots_and_Extractions/`.
  - Rinomina dei 5 Lorebook da nomi tecnici (`[WyvernChat] Svartlfr---...-export.json`) a nomi puliti (`Svartulfr_Lorebook_I/II/III.json`, `Svartulfr_Location.json`, `Svartulfr_NPC_Primary.json`).
- **Script Aggiornati ai Nuovi Percorsi**: `scripts/optimize_lorebooks.py` (spostato da `logs/`, legge da `lorebooks/source/` e scrive in `lorebooks/optimized/` con match per nome pulito), `scripts/extract_for_jed.py`, `scripts/scrape_all_ws.py`, `scripts/test_playwright.py`.
- **Ottimizzazione Lorebook (Fase 1, non-distruttiva)** applicata ai 5 export: placeholder disabilitati (204), voci intruse Digitalis/Cuttings/Jun congelate (13), keyword ombrello rimosse dalle schede NPC (326), blocchi `[INSTRUCTIONS]` ridondanti rimossi (321), priority di sicurezza `0 -> 10` (271). Gli originali in `lorebooks/source/` restano intatti.
- **Consegna**: creata la cartella `FINAL/` con i 5 Lorebook aggiornati pronti all'import.
- **Documentazione**: allineati `README.md` (struttura reale, pipeline Lorebook, 14 regole) e `AGENTS.md` (conteggio regole corretto a 14, link relativi funzionanti); rimossi i link morti `d:/SvartulfrVerse/...`.

## [14 Ottobre 2026] - Aggiornamento Regole di Progetto (/learn): Verifica Preventiva alla Fonte & Skill Operative Integrate

- **Regola 05 (§3) & GEMINI.md (§9.8) - Protocollo di Verifica Preventiva alla Fonte e Divieto Assoluto di Inferenza**:
  - Vietato proporre o scrivere specie, classi, età, LSE, parentele, ruoli o poteri sulla base di deduzioni, intuito o memorie parziali.
  - Obbligo di leggere integralmente la scheda sorgente originale (Wyvern/Kakihara, JanitorAI, `ARCHIVIO/`, Lorebook) e di citare la fonte per ogni attributo fondamentale.
  - Se il dato manca nella fonte: dichiararne l'assenza e chiedere decisione canonica all'utente.
  - Origine: correzione utente sulla bozza del Batch 3 (Radek/Goran/Kian orchi puri, Marek Blue Oni, Dominic/Bailey Rogers incubi, Federico Savini licantropo Alpha).
- **Nuova Regola 14 & GEMINI.md (§19) - Standard Operativo di Sessione e Skill Integrate**:
  - Principi di `/plan`, `/grill-me`, `/browser`, `/chrome-devtools`, `/teamwork-preview`, `/boost` adottati come standard per ogni interazione.
  - Indici di `AGENTS.md` e `GEMINI.md` aggiornati.

## [14 Ottobre 2026] - Aggiornamento Regole di Progetto (/learn): Integrità Lore, Tipizzazione Zod & Zero-Footprint Testing

- **Codifica Regola 09 & GEMINI.md (§8) - Protocollo di Formulazione RPG & Dossier Integrale Obbligatorio**:
  - Divieto assoluto di generare o proporre tratti/classi basandosi su dati parziali o inferenze dal nome.
  - Imposizione della lettura integrale preliminare di `long_summary`, `description`, `voice & behavior`, `attitudes` e voci Lexicon associate.
  - Matrice tassonomica vincolante delle stirpi: `Divine Blood` (riservato esclusivamente a Wulfnic, Zefir, Ut); `Founding Bloodline` (Nixara, Firstborn e 2a gen Douglas-Bloodmoon); `Pureblood Lineage` (Douglas, Duskwood, Wolfwood, Rogers).
  - Invarianti assolute LSE: Noah Delta (zero tratti Alpha), Jasper/Logan Beta (zero tratti Alpha), Malachia Dominant Alpha (_Pack Leader_, _Ascended Enigma_, _Apex Core Resonance_), Erik Prime Alpha (_Pack Leader_, _Dominant Alpha_, _Alpha Command_), Kemonomimi Demi-Umani (zero shift, zero allergia argento, orecchie singole animali).
- **Codifica Regola 11 & GEMINI.md (§11, §15) - Preservazione Metadati Lorebook, Tipizzazione Zod & Zero-Footprint**:
  - **Preservazione Obbligatoria Metadati Top-Level nei Lorebook**: L'endpoint `PUT /api/lorebooks/:id` non esegue merge parziale. Trasmissione obbligatoria dell'intero blocco di configurazione (`name`, `description`, `scan_depth: 5`, `token_budget: 5000`, `recursive_scanning: true`, `visibility`, `rating`, `is_private`) assieme al lexicon.
  - **Tipizzazione Rigorosa di `priority` e Validazione Schemi Zod**: Il backend Wyvern impone `z.number()` su `priority`. I valori stringa generano errori HTTP 500 fatali (`Expected number, received string, path: ["priority"]`). Forzata la conversione `priority: Number(val) || 0`.
  - **Protocollo di Pulizia Post-Diagnostica (Zero-Footprint Testing)**: Obbligo di tracciamento e cancellazione sistematica (`DELETE /api/new/chat-logs/:id`) di qualsiasi chat log o party usa-e-getta creato durante le procedure di test e debugging.

## [14 Ottobre 2026] - Risanamento e Bilanciamento RPG Ecosistema: Batch 2 (Firstborns, Militari Blackwolf, Alleati e Clan) [100% PASS]

- **Bonifica Canonica e Allineamento Stirpi Batch 2 (8 Personaggi)**:
  - **Zefir Hvitskog**: Firstborn ombra silenziosa, _Divine Blood (Firstborn)_ + _Founding Bloodline_, _Primordial Enigma_, _Dominant Alpha_, _Alpha Command_, _Apex Predator Divine Core_, _Night Stalker_, Livello 99 (>1000 anni).
  - **Ut Berg**: Firstborn colosso titanico, _Divine Blood (Firstborn)_ + _Founding Bloodline_, _Primordial Enigma_, _Dominant Alpha_, _Alpha Command_, _Apex Predator Divine Core_, _Berserker Internal Furnace_, occupazione aggiornata a _Guild Tank_, Livello 99 (>1000 anni).
  - **Major Kaladin Blackwolf Nargathon**: Comandante Sicurezza DCC, Subject Zero di Project Blackwolf, Dominant Alpha, _Modified / Lab Lineage_, _S.R.F. Veteran_, _Dungeon Veteran_, occupazione _DCC Security / PMC_, Livello 6 (38 anni).
  - **Archer Wolfwood**: Aristocratico casata Wolfwood, Dominant Alpha, _Pureblood Lineage_, _Ancient Heritage_, _Old Money / Aristocrat_, _Mastermind_, occupazione _DCC Security / PMC_, Livello 34 (174 anni).
  - **Mackenzie Sanchez-Rogers**: Brawler protettivo street-smart, Dominant Alpha, _Pureblood Lineage_ (paterno Rogers) + _Common Lupine Blood_ (materno Sanchez), _Rebel Heart_, occupazione _Street Scrapper / Rogue_, Livello 4 (25 anni).
  - **Finnegan Novak (Finn)**: Ala sinistra SUCC Bears hockey, atleta Kemonomimi, specie _Demi-umano (Demihuman)_, occupazione _Pro Athlete / Fighter_ (epurato da Pack Mom e da tutti i tratti licantropici/shifter), Livello 3 (21 anni).
  - **Zeera Darkfire**: CEO HSK Consulting, Capoclan Teschio Cornuto, specie _Demone & Infernale_, occupazione _Diplomat_, _Ancient Heritage_, _Mastermind_, _Puppeteer Mana Strings_, Livello 6.
  - **Jared Thompson**: Starting quarterback SUCC Bulls, ibrido Mezzominotauro, specie _Minotauro & Centauro_, occupazione _Pro Athlete / Fighter_ (epurato da Pack Mom e da tutti i tratti licantropici), Livello 3 (22 anni).
- **Propagazione a Cascata Verificata (3 Layer)**:
  - **World Character Cards**: 100% GET post-scrittura superata (stats sum 81, tratti string ID conformi).
  - **Schede Stand-Alone in `/mine`**: Aggiornati con successo **Mackenzie Sanchez-Rogers** (`_HqzMU3zVrgHaHBFKw4nQA`), **Zeera Darkfire** (`_tJ8zaBLAb6n7XAyd8qhHQ`) e **Jared Thompson** (`_G4126zBQhWEtFkKCG3Dw3`) con blocco `RPG STATS & TRAITS:` JED+ e zero em-dash.
  - **Lorebook `Svartúlfr - NPC Primary` (`_LBkRWNpPxpdn6dxYaDU2b`)**: Aggiornate tutte le 8 voci del Lorebook con metadati top-level preservati.

## [14 Ottobre 2026] - Risanamento e Bilanciamento RPG Ecosistema: Batch 1 (Casa Douglas, Anziani & Echo) [100% PASS]

- **Creazione Tratto Ufficiale `Pack Leader` (`_mJezfhzrdYDq8k7GWaGzm`)**:
  - Creato tramite API nel World RPG Traits (`stat_modifiers: { charisma: 2, endurance: 2, strength: 1 }`).
  - Assegnato formalmente a **Erik Ulfr Douglas** (Pack Leader in carica) e a **Malachia Björn Douglas Bloodmoon** (futuro Pack Leader designato, insieme a _Ascended Enigma_ ed _Apex Core Resonance_).
- **Bonifica Subgender LSE & Stirpi Dinastiche Batch 1 (11 Personaggi)**:
  - **Erik Ulfr Douglas**: Aggiornato a Prime Alpha (eliminata macro-anomalia Beta), tratti _Pack Leader_, _Dominant Alpha_, _Alpha Command_, _Apex Core Resonance_, _Mastermind_, _Pureblood Lineage_. Corretta la data di nascita a 31 Ottobre 1972 (`10035648`, 52 anni nel 2024 $\rightarrow$ Livello 9).
  - **Logan Dominic Járn Douglas**: Aggiornato a Pureblood Beta (eliminata anomalia Alpha), occupazione _Right Hand (Advisor/Peacekeeper)_, tratti _LSE Beta Biology_, _Pureblood Lineage_, _Feral Blood_, _Knight in Sour Armor_, _Rebel Heart_, Livello 9 (49 anni).
  - **Jasper Svartr Douglas Bloodmoon**: Allineato come Beta (eliminati tratti Alpha), _Founding Bloodline_ + _Pureblood Lineage_, _Technomantic Data Resonance_, _Tech Savvy_, _Mastermind_, _Familiar Soulbound Synergy_, Livello 3 (19 anni, gemello di Alyssa).
  - **Malachia Björn Douglas Bloodmoon**: Vanguard TANK, Dominant Alpha, _Founding Bloodline_ + _Pureblood Lineage_, _Ascended Enigma_, _Apex Core Resonance_, _Pack Leader_, _Berserker Internal Furnace_, Livello 4 (28 anni).
  - **Noah Loki Douglas Bloodmoon**: Delta, Eminenza Grigia & Tattico, _Founding Bloodline_ + _Pureblood Lineage_, _Mastermind_, _Trickster Mentor_, _Eternal Optimist_ (zero tratti Alpha), Livello 4 (25 anni).
  - **Elizabeth Duskwood**: Dominant Omega (eliminato Alpha Command), Pack Mom reggente & DCC Med Director, _Pureblood Lineage_, _Pre-Med / Healer_, Livello 14 (76 anni).
  - **Magnus Douglas III**: Patriarca Secolare, Dominant Alpha, _Alpha Command_, _Pureblood Lineage_, Livello 99 (>350 anni).
  - **Lord Cornelius Douglas**: Fondatore, Dominant Alpha, _Alpha Command_, _Pureblood Lineage_, Livello 99 (>400 anni).
  - **Nixara Hvit Bloodmoon**: Ancestrale White Moon, Dominant Omega (eliminato Alpha Command), _Founding Bloodline_ ONLY (zero Divine Blood, zero Pureblood), Livello 99.
  - **Wulfnic Báleygr Bloodmoon**: Primordial Alpha dei Firstborn, _Divine Blood (Firstborn)_ + _Founding Bloodline_, _Primordial Enigma_, _Alpha Command_, _Apex Predator Divine Core_, Livello 99 (>1000 anni).
  - **Echo**: Macchina & Sintetico, Technomancer / Cyber-Mage, 7 tratti cybernetici allineati a Jasper, Livello 3.
- **Propagazione a Cascata Verificata (4 Layer)**:
  - **World Character Cards**: 100% GET post-scrittura PASS con statistiche bilanciate a 81 e tratti assegnati.
  - **Schede Stand-Alone `/mine`**: Aggiornati i 5 Douglas (`Jasper`, `Malachia`, `Noah`, `Erik`, `Logan`) con blocco `RPG STATS & TRAITS:` completo e conforme via body parziale `{ description }`.
  - **Lorebook `Svartúlfr - NPC Primary` (`_LBkRWNpPxpdn6dxYaDU2b`)**: Aggiornate tutte le 11 voci con i nuovi tratti e statistiche, preservando intatti tutti i metadati top-level (`name`, `scan_depth: 5`, `token_budget: 5000`, `recursive_scanning: true`).
  - **User Persona Echo (`1791389790053`)**: Sincronizzata con il blocco RPG e ID lorebook preservati.

## [14 Ottobre 2026] - Tradizioni Dinastiche Licantropi (Wolf Names & Birth-Runes), Ristrutturazione Persona Echo e Sincronizzazione Totale

- **Unificazione Chat Log Wyvern (`Family` + `Digitalis`)**:
  - Unificati i due log esportati da Wyvern in un unico file JSONL continuo: [`Family_Digitalis_chat_log.jsonl`](file:///E:/repository/SvartulfrVerse/logs/Family_Digitalis_chat_log.jsonl) (476 righe totali: 1 header unificato + 246 messaggi da `Family` + 229 messaggi da `Digitalis`).
  - Preservata l'integrità byte-for-byte dei singoli messaggi e metadati (`extra`, `swipe_info`, `director_state_snapshot`, timestamp cronologici dal 12 al 14 Ottobre 2026).
  - Creato archivio di sicurezza in [`logs/backup/`](file:///E:/repository/SvartulfrVerse/logs/backup/) contenente i file originali separati (`Family_chat_log_BhJ4EfrwmPWXRXw8Pf1tK.jsonl` e `Digitalis__chat_log_xnAWPnEUX9CCc7pmV6JTq.jsonl`).
- **Codifica delle Nuove Tradizioni Dinastiche e Mitologia Primordiale**:
  - **`Lycanthrope Naming Tradition`**: Creata voce nel World Lexicon (`_q136ajAq8qR3EkNeYhR2C`, `is_global: true`) e aggiunta in append su `Svartúlfr - Lorebook I` (`_xJUNQC3BBTAbJfRGfWnF1`). Codifica l'adozione del secondo nome del lupo alla Presentazione a 13 anni, il mito primordiale di Hvit (figlia di Máni e Hati, prima compagna di Wulfnic) reincarnata nelle White Moon (Nixara Hvit e Alyssa Hvit), la controparte solare di Svartr (figlio di Sól e Sköll, assunto da Jasper Svartr), i Firstblood unificati (che usano il nome vichingo originale) e i giovani pre-presentazione (come Edric).
  - **`Lycanthrope Birth-Rune Ritual`**: Creata voce nel World Lexicon (`_ryRgj7b33yXNeN14WBfDJ`, `is_global: true`) e aggiunta in append su `Svartúlfr - Lorebook I`. Codifica il rituale del 5° giorno post-parto: incisione sul polso sinistro tramite dente di serpente e inchiostro al carbone di legna sacra e cold iron (ferro freddo contro corruzioni astrali).
- **Allineamento Alyssa Hvit Douglas Bloodmoon**:
  - **Persona (`persona_1786335754946`)**: Integrato il nome completo, `MIDDLE_NAME: Hvit (Wolf Name, Presentation at 13)` e il campo `BIRTH_RUNE: Gebo (5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink, Twin Bond)`.
  - **World Character Card (`_MXcEC8Y6B3BNm3b1ttHj6`)**: Aggiornato `display_name: "Alyssa Hvit Douglas Bloodmoon"`, `first_name: "Alyssa"`, `middle_names: ["Hvit"]`, `last_name: "Douglas Bloodmoon"` e `long_summary` sincronizzato.
  - **Lorebook `NPC Primary` (`_LBkRWNpPxpdn6dxYaDU2b`)**: Aggiornato nome voce in `Alyssa Hvit Douglas Bloodmoon`, estese le chiavi di ricerca con `Hvit` e sincronizzato l'header JED+.
- **Ristrutturazione Persona Echo & Allineamento World / Lorebook**:
  - **Persona Echo (`1791389790053`)**: Configurate 3 Appearances strutturali (1: `Base` Holographic Audio Wave 971 car., 2: `Combat Drone` AR Magitech 836 car., 3: `Cyberspace Avatar` 726 car.), 4 Outfits allineati (Audio Wave, Combat Grid Drone, Smartphone UI, Cyberspace Full) e JED+ armonizzato con `MANIFESTATIONS: ...`.
  - **World Character Card (`_xHdRRxnHqqGzayzW2E1jN`)**: Popolati i 4 Outfits e sincronizzato `long_summary`.
  - **Lorebook `NPC Primary` (`_LBkRWNpPxpdn6dxYaDU2b`)**: Sincronizzato l'header JED+ e le chiavi di ricerca dell'entità.
- **Propagazione Dinastica dei Wolf Names e Birth-Runes (World Characters, /mine & NPC Primary)**:
  - **Jasper**: `Jasper Svartr Douglas Bloodmoon`, `middle_names: ["Svartr"]`, `BIRTH_RUNE: Gebo` (sincronizzato sia nel World che nella scheda /mine e NPC Primary).
  - **Malachia**: `Malachia Björn Douglas Bloodmoon`, `middle_names: ["Björn"]`, `BIRTH_RUNE: Thurisaz` (sincronizzato World, /mine e NPC Primary).
  - **Noah**: `Noah Loki Douglas Bloodmoon`, `middle_names: ["Loki"]`, `BIRTH_RUNE: Kenaz` (sincronizzato World, /mine e NPC Primary).
  - **Erik**: `Erik Ulfr Douglas`, `middle_names: ["Cornelius", "Ulfr"]`, `BIRTH_RUNE: Tiwaz` (sincronizzato World, /mine e NPC Primary).
  - **Logan**: `Logan Járn Douglas`, `middle_names: ["Dominic", "Járn"]`, `BIRTH_RUNE: Eihwaz` (sincronizzato World, scheda stand-alone /mine `_BQ4THBW3BKL2RN9Xy4YHb` e NPC Primary).
  - **Elizabeth**: `Elizabeth Duskwood`, `BIRTH_RUNE: Berkano` (sincronizzata World e NPC Primary).
  - **Kaladin**: `Kaladin Blackwolf Nargathon`, `middle_names: ["Blackwolf"]`, codifica militare `WOLF_CODENAME: Blackwolf (Military Call-Sign / Subject Zero)` (primo soggetto sperimentale, ha dato il call-sign all'intero Project Blackwolf; World e NPC Primary).
  - **Marcus**: `Marcus Thornfield`, `middle_names: ["Iron"]`, codifica militare `WOLF_CODENAME: Iron (Military Call-Sign / Gamma-7)` (cohort di Kaladin nel Project Blackwolf, World e NPC Primary).
  - **Magnus**: `Magnus Douglas III`, `BIRTH_RUNE: Othala (Ancestral Heritage & Dynastic Sovereignty)` (World e NPC Primary).
  - **Cornelius**: `Lord Cornelius Douglas`, `BIRTH_RUNE: Othala (Dynasty Founding & Ancestral Bloodline)` (World e NPC Primary).
  - **Finn**: `Finnegan Novak`, categorizzazione canonica `SPECIES: Demi-Human Arctic Wolf (Kemonomimi, Non-Shifter)` (bullizzato da bambino come "mezzo-lupo" per l'incapacità di mutare; zero birth-rune o wolf name licantropico).
  - **Roman**: `Roman Blackwood`, categorizzazione `SPECIES: Wolf Demi-Human` (Kemonomimi, non-shifter, no rune).
  - **Nixara**: `Nixara Hvit Bloodmoon`, `middle_names: ["Hvit"]`, `BIRTH_RUNE: Perthro`.
  - **Wulfnic**: `Wulfnic Báleygr Bloodmoon`, entità Firstblood unificata, `BIRTH_RUNE: Othala`.
  - Tutte le modifiche applicate con successo (200 OK) e verificate con GET post-scrittura.
- **Audit Formattazione Lorebook II, III e Location (648 Voci)**:
  - Eseguita scansione integrale su `Svartúlfr - Lorebook II` (250 voci), `Svartúlfr - Lorebook III` (202 voci) e `Svartúlfr - Location` (196 voci): conformità confermata, zero em-dash residui, zero grassetti markdown non ammessi.
- **Verifica Live Prompt Context Budget (<5.000 Token)**:
  - Eseguita simulazione live con `scripts/test_live_prompt_budget.js`: overhead statico fisso confermato a 2.123 caratteri (~607 token), garantendo oltre il 75% della finestra di contesto per la chat history.
- **Backup Locale Consolidato (Disaster Recovery Snapshot)**:
  - Salvati 13 file JSON in `scratch/backup_consolidated_snapshot/`: World Metadata, World Characters (113), World Lexicon (705), World Locations (196), i 5 Lorebook (1.013 voci totali), le 2 User Personas (Alyssa ed Echo), le 8 schede stand-alone `/mine` e il manifest di verifica.
- **Risoluzione Bug Wyvern PUT Lorebook & Ripristino Nomi/Configurazioni**:
  - Risolto bug di sovrascrittura parziale dei Lorebook: ripristinati con successo `name`, `scan_depth: 5`, `token_budget: 5000` e `recursive_scanning: true` su `Svartúlfr - NPC Primary` (`_LBkRWNpPxpdn6dxYaDU2b`) e `Svartúlfr - Lorebook I` (`_xJUNQC3BBTAbJfRGfWnF1`), preservando tutte le voci (113 e 252).
  - Codificata la regola anti-data loss in [GEMINI.md](file:///e:/repository/SvartulfrVerse/GEMINI.md) e [.agents/rules/11_wyvern_api_sicurezza_e_bug.md](file:///e:/repository/SvartulfrVerse/.agents/rules/11_wyvern_api_sicurezza_e_bug.md) imponendo la trasmissione obbligatoria dei metadati top-level su ogni PUT.
- **Audit Integrale di Sicurezza Globale (100% PASS - 0 Errori, 0 Avvisi)**:
  - Eseguita scansione automatica approfondita su tutte le 8 componenti dell'ecosistema: World Metadata (nome e descrizioni OK), World Characters (113 personaggi, 5 globali Douglas, 106 long summaries attivi, 12 lupi verificati), World Lexicon (705 voci, 32 globali, titoli di rito ripristinati), World Locations (196 valide), schede stand-alone in `/mine` (8 schede, zero em-dash, JED+ conforme), User Personas (Alyssa 3 appearances/18 outfits/5 lorebooks; Echo 3 appearances/4 outfits), StoryEngine Svartulfr OS (v112, disaccoppiamento circolare attivo), tutti i 5 Lorebook (nomi, scan 5, budget 5000, recursive true confermati).

---

## [14 Ottobre 2026] - Ottimizzazione Persona Alyssa: Differenziazione Strutturale tra Appearances ed Outfits

- **Architettura a Doppio Livello (Appearances vs Outfits)**:
  - **Appearances (Biologia & Anatomia Pura, Senza Immagine)**:
    - `Base` (`appearance_6_pa6kZ9BzwLC05qO5Fuk`): Espansa da stub di 183 caratteri a scheda corporea completa da 1.523 caratteri (155 cm, clessidra 95-55-95 cm, pelle chiara ipersensibile, orecchie lupine singole caramello, coda caramello con punta nera, occhi verde menta, marcatura lunare di Mani, aroma di miele e moonflower).
    - `Hybrid` (`appearance_gLMMhcPOERIB-Ybzqjywa`): 1.531 caratteri di pura anatomia da lupo mannaro bipede di 185 cm, integrando le correzioni manuali dell'utente sul mantello castano-caramello serico e il petto/ventre bianco lunare a forma di cuore, zampe digitigradi, polpastrelli scuri, artigli d'ebano venati d'oro, tartufo nero lucido, epurato da tag di vestiario/trucco.
    - `full-shift` (`appearance_9ea9ur0IXwhQPcO_yb9CB`): 1.518 caratteri di pura anatomia quadrupede da lupo dire wolf gigante (Hvit), con mantello castano-caramello caldo, marcatura lunare a mezzaluna sulla groppa sinistra, gorgiera bianca con marcatura a cuore, anello Douglas su cordino di cuoio scuro al collo, epurato da tag di vestiario/trucco.
  - **Outfits (Vestiario, Avatar Swap & Prompt <Outfit>)**:
    - 16 outfit di abbigliamento civile/tattico/accademico preservati integralmente con relative immagini e descrizioni stilistiche.
    - `hybrid` (`outfit_nPERIvpkjbT9anBosZYMJ`) e `fullshift` (`outfit_s0b5DFsbIKbNQibgsOV8v`): Riconfigurati come trigger visivi leggeri (rispettivamente 475 e 387 caratteri, prima ~1.300 caratteri), preservando l'avatar portrait ad alta risoluzione e il `display_name_override: "Hvit"`, indicando l'assetto visivo e lo status di nudità ferina/vesti lacerate senza duplicare le 1.500 battute anatomiche iniettate dall'Appearance attiva.
  - **Impostazioni di Default e JED+**:
    - `default_appearance` impostata su `Base` (`appearance_6_pa6kZ9BzwLC05qO5Fuk`).
    - `default_outfit` impostato su `summer` (`outfit_UT8FhemAi1PDZeh0Q11wC`).
    - Header JED+ della main description armonizzato con riferimento esplicito alle tre forme fisiche (`SHIFTS: Active physical form defined by Appearance (Base, Hybrid, full-shift)`), preservando intatti tutti i 14.850 caratteri di lore, dinamiche familiari e profilo di intimità.
  - **Persistenza e Integrità API**:
    - Chiamata `PUT /api/user-personas/persona_1786335754946` eseguita con successo (200 OK) e verificata via GET; tutti i 5 Lorebook collegati preservati e attivi.

---

## [14 Ottobre 2026] - World Lean Architecture (Taglio Token >90%), Confinamento Roster e Regole /learn Anti-Data Loss

- **Risoluzione Sovraccarico di Token & Troncamento Cronologia nel World**:
  - **Triage Globale Lexicon**: Eseguito `scripts/remediate_world_lexicon_global_flags.js` per aggiornare 583 voci di Lexicon a `is_global: false`, preservandone integralmente il `content`. Solo 30 concetti cosmologici e biologici fondamentali (LSE, fisiologia, argento/aconito, calendario SUCC) mantengono `is_global: true`. Risparmiati oltre 170.000 token per turno.
  - **Confinamento World Characters**: Eseguito `scripts/remediate_world_characters_global_flags.js` impostando `is_global: false` su 31 personaggi secondari. Solo i 5 Douglas principali (Alyssa, Jasper, Noah, Malachia, Erik) rimangono globali; tutti gli altri si caricano unicamente per presenza fisica nella Location o nel Party.
  - **Snellimento Features & World Prompts**: Disattivata l'iniezione automatica di tabelle nel prompt (`show_party_stats: false`, `show_species_info: false`), mantenendo attive le logiche di calcolo (`rpg_stats: true`, `inventory: true`, `combat: true`). Ridotto il testo delle istruzioni avanzate del World da 6.683 a 2.123 caratteri eliminando le liste duplicate dallo StoryEngine.
- **Disaccoppiamento StoryEngine Svartulfr OS & Chat di Gruppo (/mine)**:
  - Rimosso l'array `worlds` e `lorebooks` dalla definizione interna dello StoryEngine (`engine_HCTPXhL8xr89wUY9r9dYU`), impedendo richiami circolari e duplicazioni di dati nelle sessioni stand-alone.
  - Pubblicata la nuova revisione ufficiale: **`engine_revision_qaEawQwTJX2KjHhJhLzBU`** (v108).
- **Codifica Regole di Progetto (/learn)**:
  - **Regola 11 & GEMINI.md (§11)**: Istituito il _Protocollo Anti-Data Loss per Lorebook Stand-Alone_, con divieto tassativo di sovrascritture massive via API e obbligo di backup preventivo.
  - **Regola 08 & GEMINI.md (§7)**: Sostituita la vecchia direttiva "Global Character = ON" con la _World Lean Architecture_ e la soglia di sicurezza di 5.000 token prima della chat history.
  - **Nuova Regola 13 & GEMINI.md (§18)**: Codificato lo standard operativo per le Chat di Gruppo stand-alone in `/mine`.
- **Audit & Verifica Finale**:
  - Eseguito `scripts/verify_lean_world_status.js`: 100% test superati (30 lexicon globali, 5 character globali, prompt sotto 3.000 caratteri, 0 em-dash).

---

## [14 Ottobre 2026] - Fix Wyvern UI Panel Input Sanitizer (type="text" vs Unsupported type="date"/"time")

- **Risoluzione Errore Wyvern UI "Unsupported input type"**:
  - Il parser/sanitizer JSX proprietario di Wyvern all'interno dei pannelli StoryEngine rifiuta i tag `<input type="date">` e `<input type="time">`.
  - Convertiti entrambi i campi di input in `<input type="text">` standard con placeholder contestuali (`placeholder="YYYY-MM-DD"` e `placeholder="HH:MM"`), mantenendo i preset rapidi e la validazione universale sul World Calendar (827 d.C. – 3000+).
- **Deploy & Attivazione World**:
  - Revisione pubblicata: **`engine_revision_VKHUJJHXbGq4GhyQbXAVA`** (v107, `visibility: private`).
  - World Attachment aggiornato e verificato su **`_CgYT8fHXpDC4crjmegQF7`** (alias: `svartulfr_os`, enabled: true).

---

## [14 Ottobre 2026] - StoryEngine Universal Calendar (827 CE – 3000+), Sincronizzazione Bidirezionale & Fix Sintassi JSX panel.tsx

- **Calendario Gregoriano Universale per lo StoryEngine**:
  - Implementato l'algoritmo matematico universale prolettico per coprire l'intera timeline canonica del World: dal **21 Dicembre 827 d.C., ore 00:00 UTC (Epoca 0)** fino all'anno 3000 e oltre.
  - Calcolo astronomico continuo delle fasi lunari su ciclo sinodico (29.53 giorni = 708.73 ore) con attivazione automatica del buff Full Moon.
  - Calcolo deterministico del ciclo notte/giorno (`night_active = true` dalle 20:00 alle 06:00).
- **Sincronizzazione Bidirezionale del World Clock**:
  - Modificato lo script Lua `script_after_turn_sync`: monitora qualsiasi delta temporale (`accHours ~= prevTracked`), garantendo che salti temporali in avanti o retrocessioni forzate nel passato (tramite _Override Timestamps_ nativo) aggiornino sempre l'orologio dello Smartphone OS.
  - Aggiornati i parametri di `cmd_advance_time` per accettare `target_date` (YYYY-MM-DD) e `target_time` (HH:MM), rimuovendo i limiti inferiori su `hours` per supportare rewind.
- **Selettore Calendario Interattivo nello Smartphone OS**:
  - Inserito nel widget Timeline della schermata Home il sottomenu a comparsa _📅 Universal World Calendar (827 CE – 3000+)_ con date-picker, time-picker e preset istantanei (26 Aug 2024 SUCC, 14 Oct 2023 Legacy, 21 Dec 827 Origin, 31 Oct 2499 SciFi).
- **Risoluzione Bug Sintassi JSX in `panel.tsx`**:
  - Risolto l'errore `Unexpected token, expected "," (996:6)` causato da un tag `<div>` non bilanciato nel container Timeline che chiudeva prematuramente la root e posizionava la dock fuori dal blocco JSX.
  - Verificato con `tsc`: 100% bilanciamento perfetto di tutti i tag JSX (0 errori di sintassi).
- **Deploy & World Attachment**:
  - Pubblicata la revisione finale: **`engine_revision_cTLTCPhH7TTfcy3aNYpkQ`** (v104).
  - World Attachment aggiornato con successo su **`_CgYT8fHXpDC4crjmegQF7`** (HTTP 200).

---

## [14 Ottobre 2026] - Hardening Visibilità: Tutte le Entità del World e di /mine Impostate su "Private"

- **Audit & Configurazione Visibilità Globale**:
  - **World Svartúlfr** (`_CgYT8fHXpDC4crjmegQF7`): Confermato `visibility: private`. Tutte le entità native (Locations, Environments, Scenarios, World Characters, Lexicon) sono protette e visibili unicamente al creatore.
  - **StoryEngine Svartulfr OS** (`engine_HCTPXhL8xr89wUY9r9dYU`): Confermato `visibility: private`.
  - **Tutti i 10 Personaggi Stand-Alone in `/mine`**: Verificati e impostati su `visibility: private`:
    - _Jasper Douglas Bloodmoon_ (`_t4J9aQNJM36cUKAP4wB4U`)
    - _Zeera Darkfire_ (`_tJ8zaBLAb6n7XAyd8qhHQ`)
    - _Erik Douglas_ (`_EWqmxx3Q1fdK97AVBRqEW`)
    - _Noah Douglas Bloodmoon_ (`_AjphrWj2BMT9KJTx4KETE`)
    - _Malachia Douglas Bloodmoon_ (`_yQeae3DnARft2RH4gaFNx`)
    - _Dra'kon | Bred by Va'shar aliens_ (`_yVzJt1zC4QXzPpqddAxW7`)
    - _Jared Thompson_ (`_G4126zBQhWEtFkKCG3Dw3`)
    - _Mackenzie Sanchez-Rogers_ (`_HqzMU3zVrgHaHBFKw4nQA`)
    - _Logan Douglas_ (`_BQ4THBW3BKL2RN9Xy4YHb`)
    - _The Monster Cock Almanac_ (`_3ArjC3zNNVpJHbfhYQccG`)
  - **Tutti i 3 Lorebook Stand-Alone**: Aggiornati via API a `visibility: private`:
    - _Svartúlfr - Lorebook_ (`_J8x7fwRrpa9C6Wct6hb7p`)
    - _Svartúlfr - NPC Primary_ (`_kPzhnGxaRgCMdmgrwWjbY`)
    - _Svartúlfr - Location_ (`_V6jT3gPWDCPdxT2bCedeG`)

---

## [14 Ottobre 2026] - Reattività Dinamica StoryEngine: Scan Turn Exposure, Automazione Turni (phase: "after"), Script Lua & Smartphone OS Reattivo

### 1. Risoluzione Dati Statici & Integrazione Piena con Scan Turn

- **Root Cause Risolta**:
  - I comandi dello StoryEngine erano configurati con `actor: "player"`, che per architettura nativa di Wyvern esclude categoricamente l'azione da **Scan Turn**. Lo scanner automatico/manuale dell'AI non aveva nessun comando da proporre o eseguire.
  - Mancavano regole su `phase: "after"`: nessuna logica veniva eseguita al termine della generazione dei messaggi per tracciare il tempo, la notte o gli eventi.
- **Comandi Esposti a Scan Turn & Tools Narratore (`actor: "both"`, `llm_tool_enabled: true`)**:
  - `cmd_advance_time`: Avanza le ore simulate nel World/Phone, aggiorna l'orologio dello smartphone (`clock_time`), il ciclo giorno/notte (`night_active`), la fase lunare (`moon_phase`, `moon_full_active`) e scala i giorni al picco biologico LSE (`lse_cycle_days_left`).
  - `cmd_receive_pack_message`: Permette all'AI o al giocatore di inviare e ricevere messaggi su Telegram da Erik, Noah, Jasper, Echo, Malachia e Alyssa, salvandoli nella memoria permanente dell'engine e incrementando il badge dei non letti.
  - `cmd_post_succbook`: Pubblica post dinamici sul feed social universitario SuccBook riflettendo eventi sportivi, gossip, annunci sanitari della Dr. Duskwood e vita di campus.
  - `cmd_use_suppressor`: Azione rapida di inalazione cilindro soppressore ferormonale.

### 2. Automazione Post-Turno & Script Lua (`phase: "after"`)

- **Regola `rule_after_turn_sync` (`phase: "after"`)**:
  - Esegue lo script Lua `script_after_turn_sync` al termine di ogni turno di chat, analizzando `turn.generated_message`.
  - **Riconoscimento Notte/Giorno**: Rileva transizioni notturne ("midnight", "night fell", "evening") impostando `night_active = true`; rileva mattino/alba ("sunrise", "next morning") impostando `night_active = false` e allineando l'ora a inizio giornata.
  - **Riconoscimento Fasi Lunari**: Rileva citazioni della Luna Piena attivando istantaneamente `moon_phase = "Full Moon"` e `moon_full_active = true` (buff licantropi).
  - **Tracciamento Soppressori**: Se il testo narrativo descrive l'inalazione di un soppressore, scala automaticamente la dose da `scent_suppressors_count`.

### 3. Smartphone OS UI (`panel_smartphone_os`): Reattività e Controller Temporale

- **Orologio & Data Dinamici nella Notch Superiore**:
  - L'orario `08:14` hardcoded è stato sostituito dal binding reattivo `{clockTime}` (`values.clock_time`).
  - L'indicatore di rete è stato affiancato dalla data simulata dinamica `{simDate}` (`values.sim_date`).
- **Feed Telegram & SuccBook Reattivi**:
  - Sostituiti gli array statici in `useState` con il binding prioritario a `engine.values.pack_chat_messages` e `engine.values.succbook_posts`.
  - L'invio di messaggi da parte dell'utente invoca `cmd_receive_pack_message`, persistendo la cronologia nella memoria dello StoryEngine.
- **Controller Temporale Rapido sul Dashboard Home**:
  - Aggiunto un widget rapido con pulsanti touch: `[ +1h Step ]`, `[ +4h Skip ]`, `[ +8h Shift ]` e `[ 🌕 Full Moon ]`, consentendo al giocatore di testare e far avanzare istantaneamente il tempo, il giorno/notte e la luna direttamente dall'interfaccia.

### 4. Deploy & Versioning Piattaforma Wyvern

- Pubblicata nuova revisione ufficiale **v96**: `engine_revision_KxC3tLJjLChN7UbYahtNT`.
- Aggiornato l'attachment dello StoryEngine su World `_CgYT8fHXpDC4crjmegQF7` (`engine_attachment_6LDggG4w1BaQH1zQNeJwY`) con la revisione v96 e valori iniziali scalari sincronizzati per il 26 Agosto 2024.

---

## [14 Ottobre 2026] - Bonifica Almanac, Triage Minor NPC Lexicon (Edric & Jet) & Initial Value Overrides StoryEngine (26 Agosto 2024 SUCC)

### 1. Bonifica Content Policy "The Monster Cock Almanac" (`_3ArjC3zNNVpJHbfhYQccG`)

- **Epurazione Rule 3 (No Necrophilia or Guro)**:
  - Riscritti integralmente `description`, `scenario`, `first_mes` e `post_history_instructions` rimuovendo tutte le istanze di danno fisico estremo, mutilazioni, violenza non consensuale e schiavitù sessuale ("split in half", "rape", "maim", "kill", "breeding slave").
  - Convertito il contesto in commedia erotica ad altissimo consenso (monster dildo research, test di elasticità e stanchezza euforica).
- **Gestione Rule 8 (No Stolen Characters)**:
  - In seguito alla revisione dei moderatori di Wyvern che vieta la pubblicazione pubblica di bot importati da terzi senza autorizzazione ("You may keep the imported content as private for personal use only, but do not re-submit this content"), la scheda è stata stabilizzata con visibilità `unlisted` per uso personale sicuro, azzerando qualunque rischio di ban.

### 2. Triage & Migrazione Minor NPC: Edric Douglas & Jet Thompson

- **Tutela dei Minori & Policy #1 Wyvern**:
  - I due personaggi minorenni (Edric Douglas, 12 anni; Jet Thompson, 13 anni) sono stati rimossi dai Character nativi giocabili del World (`_YJQ4cjdrT7brm7HWVkf3K` e `_eVGFKNJmJX8Cw7rc2D81A` eliminati via `DELETE`).
  - Il roster dei World Character è passato a 106 entità attive.
- **Creazione Voci Lexicon (`type: "npc"`)**:
  - **Edric Douglas** (`_WVM34aF29T4k8qtCzAcQ9`): Inserito come voce di Lexicon NPC con JED+, avatar ufficiale, legami col padre Logan e la cugina Alyssa, rivalità sportiva con Jet, e clausola tassativa di protezione minori.
  - **Jet Thompson** (`_PzcJLb9ttMCLAfz9A1jUW`): Inserito come voce di Lexicon NPC con JED+, legami con la famiglia Thompson, football junior e clausola di protezione minori.

### 3. StoryEngine: Initial Value Overrides per Primo Scenario SUCC (26 Agosto 2024)

- **Allineamento Revisione & Host Attachment**:
  - L'attachment dello StoryEngine sul World (`engine_attachment_JfFhGAL1ze6Qhd7F1Uppy`) è stato aggiornato all'ultima revisione pubblicata v94 (`engine_revision_TDTqefGCebnpgXaX2hX3V`).
- **Configurazione `initial_values` Override**:
  - `moon_phase`: `"Third Quarter (Waning)"` (calcolato astronomicamente per il 26 Agosto 2024)
  - `moon_full_active`: `false`
  - `night_active`: `false` (avvio mattutino di Move-in Day)
  - `lse_biology_status`: `"Dormant"` (~20 giorni al picco stagionale)
  - `lse_cycle_days_left`: `20`
  - `scent_suppressors_count`: `3` (fornitura sanitaria obbligatoria del campus)
  - `pack_reputation`: `25` (baseline matricola)
  - `rift_threat_level`: `"Class 1 - Stable"`
  - `pack_chat_unread`: `3` (notifiche di benvenuto da Erik, Noah, Jasper)
  - `succbook_unread_posts`: `5` (avvisi di campus & Move-in Day)
  - `succ_track`: `"pre_med"`
  - `pack_role`: `"sentinel"`
  - `underworld_role`: `"fixer"`
- **Ancoraggio Temporale Scenario "SUCC: Move-in Day at Wyrm Dormitories" (`_X1gtPxULeEV9Mj1prnzCr`)**:
  - Impostato `start_timeline_position: 10489904` (equivalente al 26 Agosto 2024, ore 08:00 UTC).

## [14 Ottobre 2026] - Sincronizzazione Totale /mine (8 Schede Stand-Alone, Lorebook a 498 Voci) & Armonizzazione Prompt & AI > Advanced

### 1. Sincronizzazione Lorebook Esterno in `/mine` (Svartúlfr - Lorebook)

- **Espansione da 348 a 498 Voci Attive**: Aggiornato il Lorebook standalone `_J8x7fwRrpa9C6Wct6hb7p` su `/api/lorebooks/_J8x7fwRrpa9C6Wct6hb7p`:
  - Aggiornate 348 voci storiche esistenti sovrascrivendo i contenuti corretti dal World Lexicon (inclusi i dormitori Wyrm, le regole sulla nutrizione, le confraternite e la rivalità CUMS);
  - Integrate 150 nuove voci mancanti create nel World Lexicon (job tematici, negozi, item iconici, SUCC Master Calendar, Luisa Sanchez-Rogers, Nurse Ariadne Cirillo).
  - Epurazione totale di em-dash (`—` sostituito da `, `) e rispetto delle regole di formattazione.

### 2. Allineamento 8 Schede Stand-Alone in `/mine` al World

- **Sincronizzazione Completa (Single Source of Truth)**: Eseguito `scripts/sync_all_mine_cards_fresh.js` sulle 8 character card stand-alone dell'utente:
  - _Jasper Douglas Bloodmoon_ (`_t4J9aQNJM36cUKAP4wB4U`)
  - _Erik Douglas_ (`_EWqmxx3Q1fdK97AVBRqEW`)
  - _Noah Douglas Bloodmoon_ (`_AjphrWj2BMT9KJTx4KETE`)
  - _Malachia Douglas Bloodmoon_ (`_yQeae3DnARft2RH4gaFNx`)
  - _Logan Douglas_ (`_BQ4THBW3BKL2RN9Xy4YHb`)
  - _Zeera Darkfire_ (`_tJ8zaBLAb6n7XAyd8qhHQ`)
  - _Jared Thompson_ (`_G4126zBQhWEtFkKCG3Dw3`)
  - _Mackenzie "Mac" Sanchez-Rogers_ (`_HqzMU3zVrgHaHBFKw4nQA`)
- **Parametri Sincronizzati**: Campi `description` JED+, `personality` PList compatto, `first_mes`, `mes_example`, `scenario`, `outfits` arricchiti, `post_history_instructions`, aggancio tassativo ai 3 Lorebook ufficiali (Lorebook `_J8x7fwRrpa9C6Wct6hb7p`, NPC Primary `_kPzhnGxaRgCMdmgrwWjbY`, Location `_V6jT3gPWDCPdxT2bCedeG`) e collegamento diretto a `story_engine_id: 'engine_HCTPXhL8xr89wUY9r9dYU'` (v92).

### 3. Allineamento Prompts del World in "Prompt & AI > Advanced"

- **Sinergia Totale con lo StoryEngine v92**: Eseguito `scripts/update_world_advanced_prompts.js` per aggiornare i campi del World (`_CgYT8fHXpDC4crjmegQF7`):
  - **`base_instructions`**: Aggiunta la sezione `<story_engine_integration>` per coordinare i log dello smartphone, i buff lunari, il monitoraggio LSE (feromoni, calore/rut, soppressori), il registro voti e le missioni DMHA con la narrazione della scena. Regola esplicita sulle orecchie singole dei demiumani (solo orecchie animali).
  - **`final_instructions`**: Rafforzata la sezione `<digital_communications>` esplicitando che notifiche Telegram, post di SUCCbook e taglie del Guild Board sono renderizzati dinamicamente dai pannelli UI senza inquinare la narrazione con ASCII fittizi.
  - **`system_prompt_override`**: Aggiunta la sezione `<story_engine_synergy>` per garantire che l'LLM reagisca attivamente agli alert automatici (Full Moon Buff, avviso fuga feromonica, tensione da esami).
  - **`context_description`**: Convalidata la lore integrata tra Blackwood City, la contea e Solarton con SUCC e CUMS.

## [14 Ottobre 2026] - Integrazione 4 Scenari SUCC nel World & StoryEngine Dynamic Campus Life Rules (v92)

### 1. Registrazione dei 4 Nuovi Scenari Ufficiali di SUCC nel World

- **Creazione e Configurazione via API**: Creati 4 nuovi Scenari sul World `_CgYT8fHXpDC4crjmegQF7` (`POST /api/worlds/scenarios`), con ambientazione geografica precisa, `premade_scenes` narrative pulite (disciplina dialoghi e divieto em-dash `—` / asterischi) e istruzioni Game Master:
  - **`SUCC: Fall Semester - Open Campus (Third Person)`** (ID `_631nnhRfdhBcG4d12rkrJ`): Seconda settimana d'autunno, mattina al Lunar Quad, vista corale di studenti demiumani, fae e atleti.
  - **`SUCC: Fall Semester - Open Campus (Second Person)`** (ID `_mtXQEnhUh8nXN6fq2Vj6D`): Variante d'apertura in seconda persona ("You") per immersione diretta.
  - **`SUCC: Move-in Day at Wyrm Dormitories`** (ID `_X1gtPxULeEV9Mj1prnzCr`): Giorno dei traslochi alle residenze Wyrm tra scatoloni, minotauri facchini, studenti arpie e controlli anti-argento.
  - **`Solarton: Full Moon Festival in Town Square`** (ID `_g8BB1wgRrEYXpKawY43BE`): Serata di plenilunio a Solarton Square tra carnevale, bancarelle carnivore di street food, luci e soundcheck punk.

### 2. StoryEngine (v92) — Regola Dinamica di Campus & Direttive Roster

- **Regola Nativa di StoryEngine**: Registrata `rule_succ_random_event_trigger` (_SUCC Dynamic Campus Life & Random Encounters_) per stimolare organicamente durante le sessioni a Solarton:
  - Comunicazioni improvvise (chiamate dei genitori, messaggi di coach o compagni di corso);
  - Incidenti fisici di campus (mana-coffee rovesciato su appunti, collisioni d'ali/code nei corridoi affollati);
  - Incontri casuali d'atleti (Bulls, Bears), musicisti (Grave Mistake) o membri dei club;
  - Comportamenti e peculiarità di specie (rettili al sole, movimenti d'orecchie e code sotto stress).
- **Integrazione Prompt Template GM**: Aggiornato `prompt_template` dello StoryEngine con le direttive del roster campus (studenti, atleti, band, docenti e adulti di Solarton).
- **Nuova Revisione Pubblicata**: StoryEngine aggiornato alla versione `v92` e revisione ufficialmente pubblicata su Wyvern.

## [13 Ottobre 2026] - Integrazione Massima Lore SUCC (Triage 60 Voci, Nuovi Lexicon, Ripopolamento Voci Vuote, Epurazione Formattazione)

### 1. Triage Completo Blocco SUCC (60 Voci)

- **Analisi e Mappatura Incrociata**: Eseguito triage sistematico del payload grezzo SUCC (`scratch/succ_payload.json`, 60 voci, uid 0–60) incrociandolo con le 688 voci di Lexicon, i 108 Character e le 188 Location attive nel World:
  - **Personaggi (27)**: Già presenti nativamente come Character card d'eccellenza in formato rigoroso JED+ (Jared, Stan Jr., Casey, Nikolaj, Janice, Tate, Oskar, Hank, Stan Sr., Eris, Dullahan, Barkley Rover, Professor Loewe, Vincent, Andy, Finn, Roland, Fade, Santiago, Iordan, Dominic Rogers, Bailey, Viola Carter, Tomas Matthews, Mac Sanchez-Rogers, Chase Anderson, Jasmin Thompson). Nessun downgrade a testo grezzo non-JED+.
  - **Nuove Voci Lexicon Create (3)**:
    - `SUCC Master Calendar & Diurnal Cycle` (ID `_Py1N2Lh64D4c8gkkMatpA`, `lore/concept`): Ritmicità diurna per fasce orarie (06:00-08:00 fino alle 02:00-06:00), flusso settimanale, eventi plenilunari, esami e Solar Festival.
    - `Luisa Sanchez-Rogers` (ID `_CFTFWPR8UJDAkc9fA6Q2Q`, `memory` collegata a Mac `_YY8VbpgzYk4dfFAL78rM3`): Profilo della sorella maggiore transgender, carpentiere, protettiva, archetipo trade school butch.
    - `Nurse Ariadne Cirillo` (ID `_gwCGDnDYbf9Wgak1BDrax`, `lore/concept`): Staff infermieristico del Campus Health Center della SUCC, ibrido Drider/Succube, etnia greca, dominanza clinica, meticolosità nelle cure e nel benessere del campus.
  - **Ripopolamento Voci di Lexicon Vuote (3)**:
    - `SUCC: Sistema Residenziale & Dormitori del Campus di Solarton` (ID `_NXA2RPpp6RHTVtxRa9pD7`): Popolata con i dettagli architettonici, layout a suite, insonorizzazione acustica per ululati, microclimi per specie e regole dei Wyrm Dormitories.
    - `SUCC: Ristorazione Universitaria & Nutrizione Metabolica Multi-Specie` (ID `_cHWapLYF6kyLTaaw8a4pF`): Dettagliate le linee alimentari per carnivori puri, ematofagi, erbivori e umani, con standard di sicurezza anti-argento e anti-aconito.
    - `DMHA: Dotazione Standard & Balistica Runica per Cacciatori` (ID `_DG4frH4W3yqNMzJXYVVPU`): Standard balistici, calibri d'ordinanza, munizioni salgemma, argento e ferro freddo.

### 2. Bonifica Formattazione e Rigoroso Rispetto delle Regole del World

- **Epurazione XML e Markdown**: Rimosse tag XML (`<succ_bulls>`, `<degrees>`, `<vampire_legislation>`, ecc.), asterischi di grassetto (`**`) e trattini em-dash (`—`) da 11 entry esistenti (`Anti-Vampire Legislation`, `1999 Nocturnal Crisis`, `SUCC BULLS`, `SUCC BEARS`, `Student Body Population`, `Sports @ SUCC`, `Supernatural Degrees`, `Rivalry with CUMS`, `Frats & Sororities`, `2002 La SUCC apre agli studenti umani`, `CUMS Campus & Teams`).
- **Verifica via Fresh GET**: Persistenza validata al 100% con status 200 su tutti gli ID del Lexicon. Zero asterischi, zero em-dash, zero violazioni sintattiche.

## [13 Ottobre 2026] - Copertura Totale Travel Routes (188/188 Location Connesse, 192 Rotte Attive, Distanze Flavor e Free Travel OFF)

### 1. Copertura 100% di tutte le 188 Location del World

- **Audit e Risoluzione Connettività**: Eseguito audit approfondito (`scripts/find_zero_route_locations.js`) che ha rilevato 73 sotto-location prive di una rotta esplicita registrata in `travel_routes` (poiché affidate all'implicita relazione gerarchica genitore-figlio). Con `free_travel: false`, l'assenza di rotte esplicite per le sotto-location poteva impedire lo scorrimento del tempo durante gli spostamenti locali.
- **Creazione di 73 Nuove Rotte di Connessione Locale**: Eseguito `scripts/ensure_all_locations_have_routes.js` per dotare ogni singola struttura, ala di dormitorio, confraternita, laboratorio didattico, camera e sotto-distretto di almeno una rotta esplicita bidirezionale:
  - **Wyrm Dormitories**: Tutte le ali (North Wing Human, South Wing Supernatural, West & East Wings Mixed, Sun/Moon Rooms, Blood Bank) collegate all'atrio centrale dei dormitori.
  - **Greek Row**: Tutte le 9 sedi di confraternita/sorellanza (ARO, ASS, BEE, BRO, DOE, KSA, MAN, MOO, TIT, FOX) collegate all'arteria principale del Greek Row.
  - **Bricklane Mall**: Tutti i negozi e gallerie (Yeti Shack, The Long Table, Suds & Such, Medusa, La Segunda Luna, A&Co.) collegati alla galleria coperta del centro commerciale.
  - **SUCC Campus & Dipartimenti**: Science Quarter (Bio Labs, Specimen Containment, Greenhouse), Basilica Library (Trophy Room, Magical Sections, Study Rooms, Anime Club), Archer Wolfwood Hall (Classrooms, Lecture Hall), Bulls Stadium (Football Field, Ice Rink) e tutti gli edifici didattici (Building A, B, C, Law Theatres, Administration, Gallery, The Pack, SSC, club) collegati con rotte dedicate.
  - **CUMS**: Connessioni interne per Evirein Academy of Magic, Magick Research Labs, Nocturnal Hall e Nightwine Hall.
  - **Blackwood City**: Strutture collegate ai rispettivi distretti (The Nursery a Villa Douglas, Old Cedar Clearing e Market-Zone a Oldtown, Hospital e School ad Arcadia, Aetheris Clinic ad Uptown, L'Iris d'Oro ed Eidolon Creative Suites a Paradise, Club House e Fighting Ring a Ironworks, The Void a Cable District, The Horns e Diner del Sud a Dockside, Yarrow River a Blackwood Forest, Crystal Caves, Dragonide Sanctum e Silver Marshes a The Otherworld).
  - **DDM Inc. // Voidspace**: Connessioni omniversali dedicate per The Lower Levels, The Euclidean Division e Dullahan's Quarters all'interno del QG DDM.
- **Risultato Finale**: **188 location connesse su 188 (0 location con zero rotte)**, per un totale di **192 rotte attive**.

### 2. Conservazione Tassativa di Free Travel = OFF

- **Regola di Simulazione Temporale**: Confermato `free_travel: false` a livello di World per impedire il teletrasporto istantaneo tra macro-regioni e consentire il calcolo dinamico e veritiero del trascorrere del tempo (ore di viaggio, alternanza giorno/notte, consumi e fatica).

### 3. Calibrazione Distance (Flavor) su Tutte le Rotte

- **Compilazione Completa del Campo `distance`**: Tutte le 192 rotte dispongono ora di valori numerici di distanza flavor coerenti e realistici (0 rotte con distanza mancante).

### 4. Allineamento Topologico Mappa Ufficiale Blackwood City (Seven Hills Hub per la Foresta)

- **Allineamento Seven Hills con Foresta e Branco Bloodmoon**: Confermato che le connessioni montane e selvagge partono direttamente da **Seven Hills**:
  - `Seven Hills` <-> `Blackwood Forest` (1 ora, 6 miglia).
  - `Seven Hills` <-> `Bloodmoon Pack Territory` (1 ora, 8 miglia).
  - `Seven Hills` <-> `Arcadia` (0 ore, 3 miglia).
- **Correzione Riferimenti Eredità**: Risolti 5 puntamenti orfani della configurazione legacy (riallineati ID corretti di Solarton Ferry Terminal, Hex Valley, Indoor Pool & Sauna e Wyrm Dormitories).
- **Nuove Connessioni Create**:
  - **Blackwood City**: Collegamenti diretti verso The Cable District, St. Brugge Private Academy, The Otherworld (varco nascosto da Blackwood Forest), Bluemoon, Sugar Moon Bakery in Arcadia, Braceria McKay, The Horns e Apartment C.
  - **Solarton**: Collegamenti verso Clinica Ortus, Le Refuge des Chats (La Dimora del Rifugio), Static & Ink, Dullahan's Condo, Solarton High School, The Open Casket, Rogers' Bargain Motors, e dai poli centrali (Square e Mall) verso Directions & Dragons, Flat sopra il negozio, The Lunar Pharmacy, Full Moon Market, Kerrigan Butchers, Claws Steel & Ink e Tidewrack Surf.
  - **SUCC Campus**: Collegamenti da Lunar Quad ad Archer Wolfwood Hall, Helsing Chapel, Unicorn Hall e accesso diretto dalla Basilica Library a The Roasted Bean.
  - **Hex Valley**: Rete completa tra fermata traghetto, valle, Hex Valley Estates e campus di CUMS.
  - **Zone di Transito**: Collegamenti per Ventura Square, The Halfway House, Simi Valley Grid e Trial Dungeon Hive Apex Rift.
  - **Bakersfield**: Connessioni da Bakersfield Square a The Dusty Coyote Diner, Rhodes Farm, Parco Roulotte di Oildale, Campi Petroliferi di Kern River, Kern River Canyon e Mercato Contadino.
  - **Los Angeles**: Rete da Pershing Square a Hollywood, Beverly Hills, Rory's Estate, Skid Row, Osservatorio Griffith, Fort MacArthur, Molo 42 e The Neon Mirage.
  - **Camp Mystic**: Raggiungibile via strada panoramica sia da Blackwood City (1h, 28 mi) sia da Solarton (1h, 32 mi).
  - **DDM Inc. // Voidspace**: Varco dimensionale riservato ed occultato (`hidden: true`, medium `omniversal`) da Dead Dog Motel Stanza 00 verso Voidspace e corridoi del QG DDM.
- **Verifica via Fresh GET**: Persistenza convalidata al 100% con 119 rotte attive e `free_travel: false`.

## [13 Ottobre 2026] - Configurazione Simulation Overrides su tutte le 188 Location del World (Property, Marketplace con 40 Item Iconici, 16 Job)

### 1. Creazione Item Iconici nel Lexicon (40 Nuovi Oggetti Tematici Registrati)

- **Creazione e Registrazione**: Eseguito `scripts/create_iconic_shop_items.js` per popolare il Lexicon con 40 oggetti iconici e tematici suddivisi per categoria (Consumable, Equipment, Material, Trade Good, Key Item) e prezzi calibrati in dollari ($ USD):
  - **Sugar Moon Bakery**: Pasticceria al miele di luna, filoni a crosta d'argento, infusi distensivi camomilla e erbe lunari, ciambelle glassate luna piena.
  - **The Roasted Bean**: Espresso doppio al mana, frullato iperproteico per therianthropi, cold brew nitro per concentrazione.
  - **The Lunar Pharmacy**: Flaconi spray soppressori feromonici LSE, pomate dermiche per ustioni da argento, fiale neutralizzanti per aconito, ampolle rigenerative cellulari.
  - **Directions & Dragons**: Set dadi poliedrici in ossidiana bilanciati, schermi del master fonoisolanti, miniature in peltro del signore dei lupi.
  - **The Dusty Coyote Diner**: Burger mostro deluxe del coyote, caffe americano nero a rabbocco continuo, fette calde di torta pecan.
  - **Kerrigan & Sons Butchers**: Costate ribeye con osso da 2 libbre per therianthropi, salsicce affumicate di cinghiale selvatico, confezioni di midollo osseo crudo.
  - **Claws Steel & Ink**: Burri lenitivi all'aloe e vitamina E per cura post-tatuaggio, piercing industrial in titanio chirurgico nero.
  - **Tidewrack Surf & Rental**: Tavole corte in fibra di carbonio ad alto impatto, mute oceaniche termiche in neoprene (4/3mm), paraffina biologica al cocco.
  - **Full Moon Market**: Bracciali talismanici in filo d'argento intrecciato, barattoli di muschio lunare luminescente di Hex Valley, borse artigianali da cintura in cuoio invecchiato.
  - **Rhodes Farm Stand**: Galloni di latte intero crudo di pascolo, forme di formaggio affumicato alla quercia, burro montato a mano.
  - **Cable District Garages**: Lubrificante catene al grafene ad alte prestazioni, chiavi inglesi runiche rinforzate, toppe da gilet in pelle Ironhorn Nomads.
  - **La Dimora del Rifugio (Le Refuge des Chats)**: Latti caldi all'erba gatta speziata, biscotti empatici curativi per famigli.
  - **The Verve & Sidewinders**: Riserva Douglas bourbon 18 anni, champagne millesimato crystal noir, shot di tequila agave oro e cocktail neon ad alto voltaggio.

### 2. Creazione ed Allineamento Job Offerti (16 Contratti Lavorativi nel Lexicon)

- **Profili di Impiego Registrati**: Eseguito `scripts/create_iconic_jobs.js` per creare 16 contratti con stipendio settimanale bilanciato, requisiti e descrizioni contestuali:
  - Apprendista pasticciere e banco (Sugar Moon), barista monitor campus (The Roasted Bean), assistente famigli (Le Refuge des Chats), tecnico dispensario (The Lunar Pharmacy), meccanico moto pesanti (Cable District), commesso e master giochi da tavolo (Directions & Dragons), bracciante mungitore (Rhodes Farm), garzone macellaio e affumicatore (Kerrigan Butchers), cuoco di linea short-order (Dusty Coyote), bartender notturno (Sidewinders), cameriere lounge VIP (The Verve), apprendista tatuatore (Claws Steel & Ink), addetto noleggio surf (Tidewrack), catalogatore grimoire (Basilica Library), facchino di caveau (Team Ukiyo), caposquadra sentieri e istruttore (Camp Mystic).

### 3. Configurazione Simulation Overrides su tutte le 188 Location (45 Aggiornate, 143 Convalidate)

- **Esecuzione Batch Mirata**: Eseguito `scripts/update_all_locations_sim.js` via API Wyvern (`PUT /api/worlds/locations/:id`).
- **Property (Alloggi, Dormitori, Appartamenti e Residenze)**:
  - Configurati affitti settimanali e opzioni di acquisto su 24 alloggi canonici: Wyrm Dormitories (e ali Ovest/Est, Sud, Nord a $380-$450/settimana), Additional Student Housing ($350), Confraternite e Sorellanze del Greek Row ($460-$530), Dormitori CUMS Artemis e Apollo ($600), Nocturnal e Nightwine Hall ($650), Apartment C ($550/settimana o acquisto a $180,000), Flat sopra Directions & Dragons ($600), Coastal Residential ($1,200/settimana o acquisto a $350,000), Hex Valley Estates ($2,500/settimana o $1,200,000), Parco Roulotte di Oildale ($120/settimana o $25,000), Eidolon Suites ($1,800), Dead Dog Motel ($150), Villa Douglas Guest Wing ($1), Dullahan's Condo ($800 o $280,000), Rory's Estate ($5,000 o $3,500,000).
- **Marketplace (Botteghe e Negozi Attivi)**:
  - Attivati 14 shop con inventari tematici, prezzi override e margini di riacquisto bilanciati (buy rate 0.4 - 0.65).
- **Jobs Offered Here**:
  - Assegnati i 16 ID contrattuali alle rispettive location di impiego.
- **Pulizia Location Pubbliche**:
  - Per tutte le restanti 143 location di transito, studio, aule universitarie, laboratori, parchi e foreste, i moduli di proprietà e mercato sono stati impostati esplicitamente su `enabled: false`.
- **Verifica Empirica**: Rilettura campionaria via fresh GET ha confermato persistenza al 100% senza alcuna anomalia o errore.

## [13 Ottobre 2026] - Risoluzione Globale Voci Lexicon/Items Unnamed (90/90 Ripristinate) & Configurazione Modificatori Tratti RPG (5/5 Applicati)

### 1. Risoluzione Voci Lexicon & Items Unnamed (90/90 Riparate via API)

- **Causa dell'Anomalia**: Durante i precedenti batch upload dei blocchi di Lexicon (Famigli SUCC, Magia Urbana, Dottrina DMHA e Fisiologia Mutaforma), le voci erano state trasmesse con la chiave `title:` invece del campo canonico dello schema Wyvern `name:`. Questo generava un valore `name: ""` che nell'interfaccia web provocava il rendering fallback di `Untitled memory`, `Untitled lore/concept` e `Unnamed` nella tabella `Game/RPG Systems > Items` (tutti i 10 item del World sono voci di Lexicon con `type: 'item'`).
- **Risoluzione Automatica**: Eseguito script dedicato (`scripts/fix_all_unnamed_lexicons.js`) con mappatura esatta 1-a-1 tra ID entità e titoli ufficiali registrati. Tutti i 90 record (inclusi i 10 Item DMHA e SUCC) sono stati aggiornati via `PUT /api/worlds/lexicon/:id`.
- **Verifica**: Scansione post-intervento su tutte le 631 voci del Lexicon del World ha confermato **0 voci unnamed rimanenti**.

### 2. Configurazione Modificatori Statistici Tratti RPG (5 Tratti Senza Modificatori Risolti)

- **Identificazione**: Ispezione su tutti i 45 tratti del World (`/api/worlds/rpg/traits/_CgYT8fHXpDC4crjmegQF7`) ha rilevato 5 tratti registrati con `stat_modifiers: {}` ("No modifiers"):
  1. `Apex Predator Divine Core` (`_NL4ANGp2gjKtbAgRTFxbD`): Applicati `{ strength: 3, endurance: 3, perception: 2, charisma: 2 }` (Tratto dei Nove Firstborn).
  2. `Berserker Internal Furnace` (`_L2xQk9j8RnMKUgGnCVWRR`): Applicati `{ strength: 3, endurance: 3, agility: 1, intelligence: -1 }` (Tratto Berserker di Malachia Douglas).
  3. `Familiar Soulbound Synergy` (`_kUV13hFp2R2a4aYEXq3c4`): Applicati `{ perception: 2, intelligence: 2, charisma: 1 }` (Tratto custodi e famigli SUCC).
  4. `Puppeteer Mana Strings` (`_C8XXTwLd1mmF33EkQMUyD`): Applicati `{ agility: 2, intelligence: 2, perception: 1, strength: -1 }` (Tratto burattinaio di Angelo Moreno).
  5. `Technomantic Data Resonance` (`_AQ6Qy4KHMDgFWKPHDJeqb`): Applicati `{ intelligence: 3, perception: 2, strength: -1 }` (Tratto tecnomante di Jasper Douglas).
- **Verifica**: Tutti i 45 tratti del World dispongono ora di modificatori statistici bilanciati coerenti con le 7 caratteristiche RPG del sistema.

## [13 Ottobre 2026] — Story Engine Svartulfr OS (`engine_HCTPXhL8xr89wUY9r9dYU` — v90): Riscrittura Integrale in Inglese, Risoluzione Dipendenze e Pubblicazione Revisione Ufficiale Conforme alla Documentazione Wyvern

### 1. Riscrittura Completa in Lingua Inglese (Allineamento Moderatori Wyvern)

- **Metadata Pubblici**: `tagline` ("Interactive Werewolf Pack Smartphone OS, LSE Biology Tracker & Academic Portal") e `description` strutturata con panoramica esaustiva delle funzionalità (Telegram Douglas Pack, SUCC/CUMS Academic Portal, DMHA Hunter Guild, BioTrack LSE, SuccBook & Echo Mood Player) e sezione esplicita di conformità alle Wyvern Safety & Content Policies per accelerare la revisione del team di moderazione.
- **Componente React TSX (`ui_panels[0].code`)**: Riscritti al 100% in lingua inglese tutti i testi dell'interfaccia (status notch, pulsanti, tab, messaggi preimpostati Telegram, schede accademiche degli studenti, taglie dei cacciatori DMHA, notifiche del feed campus SuccBook e player audio Echo).
- **Variabili, Regole e Comandi**:
  - Tradotti identificatori ed etichette (`Current Moon Phase`, `Lupine Social Ecology Status`, `Scent Suppressors Count`, `Active DMHA Mission`, ecc.).
  - Comandi ed esecuzioni tradotte (`cmd_use_suppressor`, label "Inhale Pheromone Suppressor").
  - Status template e Prompt Directives completamente in inglese.

### 2. Risoluzione Blocco Dipendenze Private (HTTP 403 / "A StoryEngine world dependency is unavailable")

- **Causa**: Il World e i Lorebook dell'utente avevano visibilità ristretta (`friends`) e nessuna revisione pubblica pubblicata. Dichiarare dipendenze private o non-pubblicate in uno StoryEngine impostato come `public` provocava il rifiuto categorico della pubblicazione da parte del backend di Wyvern.
- **Risoluzione**: Impostati `worlds: []` e `lorebooks: []` nell'Engine standalone. In conformità con la documentazione ufficiale Wyvern (`/Features/StoryEngine`), l'engine opera come modulo universale indipendente attaccabile a qualsiasi chat o sessione.

### 3. Pubblicazione della Revisione Ufficiale

- Pubblicata con successo via endpoint `POST /api/story-engines/:id/publish` con identificativo **`engine_revision_fpzXfWnjYeLHTGUNQz6L7`**.
- Lo StoryEngine risulta live con `status: "published"`, revisione congelata e pronta per l'approvazione pubblica senza blocchi.

## [13 Ottobre 2026] — Importazione Canonica di 16 Character Cards nel World Svartúlfr (Ukiyo, Crimsonmaw, C.U.M.S.) & Epurazione Segnalibri Wyvern

### 1. Importazione & Conversione Canonica (16/16 Character Cards Native Create nel World)

Il roster dei personaggi nativi del World di Svartúlfr (`_CgYT8fHXpDC4crjmegQF7`) è stato ampliato da 92 a **108 personaggi**, completando la conversione integrale secondo gli standard JED+, LSE, RPG stats bilanciate (81 pt totali, cap Lv 99) e World Clock:

- **Ukiyo Series (Kakihara):**
  - **Radek (`_B1zMtdnV7qaJRBK9WEL3d`):** Orco, Leader del Team Ukiyo & Guild Vanguard DPS (Lv 8, 81 pt stats, tratti `Apex Core Resonance`, `Dungeon Veteran`, `Tactical Insight`, home location: Cable District).
  - **Goran (`_ktBmqzxz61EF6rb3AN483`):** Minotauro, Heavy Frontline Defender del Team Ukiyo (Lv 6, 81 pt stats, tratti `Gentle Giant`, `Dungeon Veteran`, `Unbreakable Guard`, home location: Cable District).
  - **Kian (`_nePY987DCPUFXyDWeUNaj`):** Mezzelfo, Scout & Long-Range Mana Sniper del Team Ukiyo (Lv 5, 81 pt stats, tratti `Lupine Senses`, `Dungeon Veteran`, `Trickster Mentor`, home location: Cable District). Separato con successo dalla vecchia composite card.
  - **Marek (`_DNaUEjdBpeYph6pMYAkrt`):** Minotauro, Enforcer degli Ironhorn Nomads & Master Mechanic (Lv 7, 81 pt stats, tratti `Gentle Giant`, `Apex Core Resonance`, `Dungeon Veteran`, home location: Cable District Garages).
  - **Jaelyn (`_U7VT178yyRfe1cp4enCcw`):** Demi-umana Gatta (singolo paio di orecchie feline), Barista presso Le Refuge des Chats & Sugar Moon Bakery (Lv 4, 81 pt stats, tratti `Empathic Resonance`, `Moonflower Bloom`, home location: Arcadia).
  - **Neve (`_1KnH8wwhgrJnLwN2kHUUx`):** Demi-umana Gatta (singolo paio di orecchie feline), Commessa e Pasticciera presso Sugar Moon Bakery (Lv 4, 81 pt stats, tratti `Empathic Resonance`, `Moonflower Bloom`, home location: Arcadia).
  - **Bessie May (`_PjHFLQMac61EK6cKLe1pK`):** Demi-umana Mucca (singolo paio di orecchie bovine e corna ricurve), Artigiana lattiero-casearia alla Solarton Valley Dairy Farm (Lv 4, 81 pt stats, tratti `Gentle Giant`, `Moonflower Bloom`, home location: Solarton Valley Farm).
- **Crimsonmaw Pack (ℙ𝕙𝕒𝕟𝕥𝕒𝕩𝕞):**
  - **Liam O’Connor (`_LmqU1jwEmNQfaYEAyMr4r`):** Lupo Mannaro dell'antica Pureblood House O’Connor, Enforcer alleato del Branco Douglas a Blackwood City (Lv 6, 81 pt stats, tratti `Lupine Senses`, `Feral Blood`, `Apex Core Resonance`, home location: Villa Douglas).
  - **Hugh Rivers (`_eAbjAhEaYr8PftMBb7dHY`):** Lupo Mannaro, Street Scrapper e Sentinel del Branco Crimsonmaw al confine tra Solarton e Blackwood (Lv 5, 81 pt stats, tratti `Feral Blood`, `Night Stalker`, `Lupine Senses`, home location: Industrial Outskirts).
- **California University of Magical Studies — C.U.M.S. (Nairene - Academy of Magic):**
  - **Amerian de Vian (`_3rnaj38dFAxEhr97mAWVq`):** Drow Elf, Studente SUCC/CUMS di Duello Arcano e Magia Notturna (Lv 5, 81 pt stats, tratti `Night Stalker`, `Arcane Resonance`, home location: CUMS Solarton `_Caw9nRwKf4Gx9VzW21QJj`).
  - **Ashton Crowley (`_e8FEAfCdNTDhgzbEgbHCB`):** Umano, Studente CUMS di Illusione e Infiltrazione (Lv 4, 81 pt stats, tratti `Trickster Mentor`, `Arcane Resonance`, home location: CUMS Solarton).
  - **Aeril Royen (`_nQcTbkw3et4TEBeq9C7pB`):** Tritone / Merfolk, Studente CUMS di Idromanzia e Manipolazione dei Fluidi (Lv 4, 81 pt stats, tratti `Symbiotic Feeder`, `Arcane Resonance`, home location: CUMS Solarton).
  - **Caien Vaelion (`_Jd6y7d8c33Dkbxz3PHER8`):** Elfo della Luce, Studente CUMS di Evocazione Solare e Barriere Divine (Lv 5, 81 pt stats, tratti `Empathic Resonance`, `Arcane Resonance`, home location: CUMS Solarton).
  - **Lestat Oreven (`_Rj9yqTj19KHGNaqrcGf6r`):** Umano, Nobile Aristocratico & Studente CUMS di Magia del Sangue ed Ombra (Lv 5, 81 pt stats, tratti `Aristocratic Presence`, `Apex Core Resonance`, home location: CUMS Solarton).
  - **Xaiden Nershatar (`_dhPb7ngYawDLXFTnDqMmw`):** Demone Infernale, Professore Associato di Combattimento Tattico e Duelli Magici presso CUMS (Lv 9, 81 pt stats, tratti `Apex Core Resonance`, `Dungeon Veteran`, `Tactical Insight`, home location: CUMS Solarton).
  - **Zaire Ziisis (`_6aDV48T1fekTFVzLxjJDR`):** Drago Antico, Rettore e Preside della California University of Magical Sciences (Lv 99 [cap Wyvern per età millenaria 1184 anni], 81 pt stats, tratti `Apex Core Resonance`, `Aristocratic Presence`, `Tactical Insight`, home location: CUMS Solarton).

### 2. Rispetto delle Direttive e Disciplina di Formattazione

- **Zero Macro `{{age}}`:** Ogni scheda include età anagrafica corrente e data di nascita esplicita (es. `AGE: 26 (Born 14 May 1998);`), garantendo funzionamento perfetto anche nelle chat stand-alone fuori dal World.
- **Fisionomia Demi-Umani (Orecchie Singole):** Per Jaelyn, Neve e Bessie May è stato sancito esplicitamente il divieto di orecchie umane: possiedono un solo paio di orecchie animali.
- **Disciplina Tipografica:** Dialoghi racchiusi tra virgolette inglesi doppie `"..."`, azioni e narrazioni in testo semplice senza asterischi, asterischi riservati ai soli pensieri interni, divieto assoluto dell'em-dash (`—`).

### 3. Epurazione Segnalibri Wyvern `/mine` (14/14 Rimossi con Successo)

- Rimossi dall'inventario personale dei segnalibri (`/api/inventory/characters/:id`) tutti i 14 segnalibri originali convertiti e integrati nel World.
- Conteggio residuo dei segnalibri personaggi in `/mine`: ridotto da 41 a **27** (preservando solo le schede di terze parti off-world come Dartalia di StatuoTW e altri universi indipendenti).

### 4. Allineamento Story Engine & Rilascio Pannello Unificato: Svartulfr Smartphone OS (`engine_HCTPXhL8xr89wUY9r9dYU` — v76 → v81)

- **Risoluzione Errori Linter Monaco & Piena Conformità TypeScript (v77-v78):**
  - Risolto l'errore Monaco `Cannot find name 'useState'` con l'import esplicito consentito dalla sandbox: `import React, { useState } from 'react';`.
  - Risolto il blocco rosso di parse errors eliminando tutti gli escape errati (`\'ingresso`, `\'Subterranean...`) convertiti in stringhe pulite a doppi apici (`"..."`).
  - Risolti gli errori TypeScript strict `TS7053` e `TS2345` tipizzando `STUDENTS_DATA` e `HUNTERS_DATA` come `Record<string, any>`, e tipizzando `acceptedMissionId` come `useState<string | null>(null)`.
- **Risoluzione "Unsupported panel style" & Migrazione a Tailwind Universale (v79-v80):**
  - La sandbox di Wyvern rigetta le proprietà CSS avanzate o non sicure negli oggetti `style={{ ... }}` inline (`gridTemplateColumns`, `outline`, `boxShadow`, `textTransform`, ecc.).
  - Convertito interamente lo stile grafico nei componenti nativi e classi **Tailwind CSS (`className="..."`)**, azzerando qualsiasi oggetto `style={{ ... }}` non conforme.
- **Perfezionamento Spaziature, Padding e Badge Voti (v81):**
  - **Eliminazione Classi Decimali:** Identificato che il bundle Tailwind di Wyvern non compila valori frazionari (`px-3.5`, `py-2.5`, `p-2.5`, `py-0.5`, `px-1.5`, `pt-0.5`), che causavano padding a `0px`. Sostituite al 100% con classi a numeri interi universali (`p-3`, `p-4`, `px-4`, `py-2`, `py-3`, `gap-2`, `gap-3`).
  - **Badge Voti Accademici:** Trasformati i badge dei voti (`A+`, `A`) da pillole ovali schiacciate a riquadri stabili da 40x32px (`w-10 h-8 rounded-xl flex items-center justify-center font-bold text-xs bg-emerald-950 text-emerald-300 border border-emerald-600`), con testo centrato e arioso.
  - **Selettore Studente:** Aggiunto padding verticale (`py-1` e `px-3 py-2 rounded-xl`), impedendo il clipping in altezza dei pulsanti in cima.
  - **Bottom Dock:** Posizionata la bolla del badge notifica `3` in coordinate relative corrette (`-top-1 -right-3`) sopra l'icona `💬`, separata dall'etichetta `Chat`.
- **Piena Conformità alla Sandbox Ufficiale Wyvern React TSX:**
  - Rimosse tutte le API browser non permesse (`document`, `window`, `Date.now`, `setTimeout`, `setInterval`);
  - Rimossi tutti i listener ed hook non supportati (`useEffect`, `onKeyDown`);
  - Gli input handler ricevono direttamente il valore tipizzato senza dipendere da eventi DOM sintetici (`onChange={val => ...}`);
  - Invocazione ufficiale dei comandi del motore tramite `await engine.runCommand('cmd_use_suppressor')` con auto-refresh delle statistiche live;
  - Layout pilotato da `engine.values` ed `engine.mode`.
- **Unificazione dei Pannelli in un Unico Smartphone OS Realistico:** I 3 precedenti pannelli sparsi della sidebar sono stati condensati in un unico, immersivo pannello interattivo in stile smartphone moderno (**Svartulfr Smartphone OS** — `panel_smartphone_os`, icon `layout`, ~60 KB di logica React):
  - **Scocca & Status Bar Reattiva:** Top bar stile iOS/Android con orologio di sistema, connessione _DCC 5G_, Dynamic Island con fase lunare live (🌙/🌕), indicatore e alert per i soppressori ferormonali (🧪 x3) e barre segnale/batteria (98%).
  - **Schermata Home Dashboard:** Widget data e ora del World (5 Aprile 2024, Solarton & Blackwood), allerta Rift attiva, widget ormonale LSE (Heat/Rut peak) con pulsante rapido per inalare inibitori via comando motore, widget Reputazione Branco Douglas (progress bar), mini widget player audio Echo e griglia di 8 applicazioni con badge notifiche dinamici.
  - **App 💬 Telegram (Douglas Pack Chat):** Chat criptata della famiglia Douglas con messaggi differenziati per ruolo e colore (Papà Erik, Noah, Jasper, Echo, Malachia) e casella di testo interattiva per comporre e inviare risposte istantanee nel feed tramite il pulsante Invia.
  - **App 🎓 Portale Universitario (SUCC & C.U.M.S.):** Sistema unificato con selettore dinamico per studenti (Alyssa Pre-Med, Jasper Ingegneria, Noah PR, Malachia Tattica, e CUMS Duellanti Arcani come Amerian, Ashton, Caien, Aeril, Lestat). Monitora CFU (barra su 180 crediti), GPA/Media, stage curriculare e schede dei singoli corsi con voti ufficiali.
  - **App ⚔️ Registro Gilda DMHA (Hunter Registry):** Selettore cacciatori (Alyssa, Jasper, Malachia Apex Berserker, Team Ukiyo d'élite [Radek, Goran, Kian], Noah). Visualizza crediti gilda, specialità e una bacheca missioni interattiva con pulsante _"Accetta / In Corso"_ per incarichi a Blackwood, Cable District, Hex Valley e Apex Trials.
  - **App 🐾 BioTrack LSE & Monitoraggio Branco:** Quadro biologico dettagliato per il ciclo ferormonale, scorte di soppressori con pulsante _"Inala Dose"_ (decremento via `cmd_use_suppressor` e feedback olfattivo live per 8 ore) e scheda con le regole d'impatto della Luna Piena (+2 MGT/RES, +1 AGI).
  - **App 🌐 SUCCbook (Social Campus Network):** Feed social con post e gossip del campus (SUCC Bulls Athletics, Le Refuge des Chats di Arcadia con i croissant di Jaelyn, rave clandestini a Solarton) e pulsante interattivo ❤️ _"Mi piace"_ con contatore live.
  - **App 🎵 Echo Music Mood Speaker:** Terminale multimediale magitech del famiglio digitale Echo con riproduzione/pausa e 4 preset di atmosfera sonora (Dungeon Synth, Relax & Intimacy, High Adrenaline Combat, Campus Coffeehouse).
  - **Bottom Navigation Dock:** Docking bar inferiore permanente per navigare all'istante tra _Home_, _Chat_, _Studio_, _Gilda_ e _LSE_.
- **Connessione World & 4 Lorebook di Svartúlfr Preservata al 100%:** World `_CgYT8fHXpDC4crjmegQF7` e tutti e 4 i Lorebooks (`NPC Primary`, `NPC Secondary`, `Lorebook`, `Location`) connessi deterministicamente con condizione `always`.
- **Prompt Directive Espansa (v76):** Integrati C.U.M.S., Team Ukiyo, Ironhorn Nomads, Arcadia demi-umana e Branco Crimsonmaw.

### 5. Esportazioni Locali Sincronizzate

- [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json): aggiornato a **108 World Characters**.
- [exports/Story_Engines_Export.json](file:///e:/repository/SvartulfrVerse/exports/Story_Engines_Export.json): aggiornato con la versione 76 di Svartulfr OS.
- [mine_inventory.json](file:///e:/repository/SvartulfrVerse/mine_inventory.json): aggiornato a 0 lorebook bookmarked e 27 character bookmarked.

---

### 1. Epurazione Lorebook & Character Bookmarked Già Integrati (Wyvern /mine Inventory)

- **Pulizia Inventario Segnalibri Lorebooks (19/19 Rimossi):** Rimosse dall'inventario personale dei segnalibri (`/api/inventory/lorebooks/:id`) tutte le 19 raccolte tematiche esterne assimilate nel World di Svartúlfr e nei 4 Lorebook Portabili (`Camp Mystic`, `Mystics`, `Mystics Extras`, `Technomancer`, `Sculpter`, `Druid`, `The Warper`, `Shadow Lord`, `Puppet Master`, `Dreamwalker`, `Shapeshifter`, `Graviton`, `Aegis City Hunters`, `Berserker Bloodline`, `Cybers And Cyberspace`, `The Familiar Species`, `Spell Compendium`, `Apex Predator`, `LA: New Moon Compendiu`).
- **Audit e Unbookmarking Character Bookmarked (41 Rimasti, Barrow Rimosso):**
  - Eseguito audit incrociato completo sui 43 personaggi presenti nei segnalibri di Wyvern:
    - **Barrow (`_nbEC7qk3NgU1LDfpQN9BW`, Kakihara):** Riscontrata la presenza della scheda ufficiale nel World (`_LEeEzdCCyGjQ8kfVkcra8`). Aggiornata la scheda nativa del World eliminando la macro `{{age}}` in favore dell'età anagrafica e data di nascita esplicita (`AGE: 42 (Born 9 November 1981);`), formattato il blocco compatto `summary` in PList JED+, e assegnati i 4 tratti coerenti (`Gentle Giant`, `Dungeon Veteran`, `The Weight He Carries`, `Knight in Sour Armor`). Rimosso con successo il segnalibro della scheda originale esterna (`DELETE /api/inventory/characters/_nbEC7qk3NgU1LDfpQN9BW`).
    - **Altri Personaggi Segnalibro (41 Rimanenti):** Mantenuti intatti nei segnalibri personali per future consultazioni o importazioni (es. _Ukiyo Series_ di Kakihara: Radek, Goran & Kian, Jaelyn, Marek, Neve, Bessie May; _Crimsonmaw_ di ℙ𝕙𝕒𝕟𝕥𝕒𝕩𝕞: Liam O'Connor, Hugh Rivers; e i bot esterni da altri universi come Dartalia o Academy of Magic).

### 2. Personas di Alyssa ed Echo (/api/user-personas)

- **Alyssa (`persona_1786335754946`):**
  - Sincronizzata la scheda Persona con l'intera estensione RPG: classe `Guild Support (Combat Medic / Healer)`, 13 tratti simultanei (biologia Dominant Omega White Moon, Founding Bloodline, medicina d'emergenza, familiar synergy, rigenerazione, sensi lupini, status aristocratico, veterana di dungeon e studentessa SUCC).
  - 18 Outfits completi sincronizzati e collegati i 3 Lorebooks di Svartúlfr per il contesto in chat 1-on-1.
- **Echo (`1791389790053`):**
  - Definita la scheda Persona integrale di Echo in formato JED+: specie `Macchina & Sintetico (Sentient Cyber-Entity / Digital Familiar)`, classe `Technomancer / Cyber-Mage Assistant`, 5 tratti RPG (`Cyber-Augmented`, `Tech Savvy`, `Technomantic Data Resonance`, `Familiar Soulbound Synergy`, `Night Stalker`), statistiche base (STR 9, PER 15, END 10, CHA 11, INT 16, AGI 12, LCK 11).
  - Creati 4 outfit/manifestazioni digitali (Default Audio Wave, Combat Grid Drone, Smartphone Interface, Cyberspace Full Avatar).
  - Collegati i 3 Lorebooks di Svartúlfr alla Persona di Echo.
- **Echo World Character (`_xHdRRxnHqqGzayzW2E1jN`):**
  - Creata ex novo la Character Card nativa di Echo nel World di Wyvern (`world_characters`, totale elevato a **92 personaggi**), completa di RPG stats, classe, tratti e avatar ufficiale.

### 2. Stand-Alone Characters in `/mine` (8 Personaggi Sincronizzati)

- **Allineamento Diretto dal World:** Jasper, Erik, Noah, Malachia, Logan, Zeera, Jared e Mackenzie ("Mac") sono stati sincronizzati punto per punto tra `/mine` e il World:
  - Descrizioni estese JED+ e blocchi compatti `personality` aggiornati con le nuove classi (es. Malachia Guild Berserker, Jasper Technomancer, Zeera House Head).
  - Collegamento formale attivo a `linked_world: "_CgYT8fHXpDC4crjmegQF7"`.
  - Agganciati i 4 Lorebooks di Svartúlfr a tutte le schede per garantire massima coerenza anche nelle chat stand-alone fuori dal World.

### 3. I 4 Lorebook di Svartúlfr in `Lorebook > Created` (Lore Portabile Fuori dal World)

- **Svartúlfr - Location (`_V6jT3gPWDCPdxT2bCedeG`):** Aggiornato a **190 voci**, integrando Camp Mystic sul Lago Erie e tutte le location del World.
- **Svartúlfr - Lorebook (`_J8x7fwRrpa9C6Wct6hb7p`):** Incrementato da 237 a **348 voci** (+111 nuove voci dal World) con tutti i nuovi poteri, fazioni, mostri, chimere, magia urban fantasy estesa (Gravitone, Warper, Sculpter, Druidismo, Dreamwalker, Spell Compendium) e classi (Berserker, Puppet Master, Technomancer).
- **Svartúlfr - NPC Primary (`_kPzhnGxaRgCMdmgrwWjbY`):** 101 voci primarie allineate.
- **Svartúlfr - NPC Secondary (`_b6ezzLBynKkdLCKqN8M1U`):** 313 voci secondarie e terziarie con classi e tratti RPG.

### 4. Story Engine Svartulfr OS (`engine_HCTPXhL8xr89wUY9r9dYU`)

- **Versione 71:** Collegato deterministicamente al World `_CgYT8fHXpDC4crjmegQF7` (`definition.worlds`) e ai 3 Lorebooks di Svartúlfr (`definition.lorebooks`).
- **Prompt Directive Espansa:** Integrate le regole per la Fornace Interna del Berserker (Malachia), la Tecnomanzia e il Digital Familiar Echo con Music Mood Speaker (Jasper), i fili di mana e simulacri del Puppet Master (Angelo) e la riserva estiva di Camp Mystic.

### 5. Esportazioni Locali Bidirezionali Consolidate (`exports/`)

- [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) (6.05 MB — 92 characters, 631 lexicon, 188 locations, 4 scenarios).
- [exports/User_Personas_Export.json](file:///e:/repository/SvartulfrVerse/exports/User_Personas_Export.json) (Alyssa ed Echo con 18 e 4 outfits).
- [exports/Mine_Characters_Export.json](file:///e:/repository/SvartulfrVerse/exports/Mine_Characters_Export.json) (10 personaggi stand-alone sincronizzati).
- [exports/Story_Engines_Export.json](file:///e:/repository/SvartulfrVerse/exports/Story_Engines_Export.json) (Svartulfr OS v71).
- [exports/Mine_Lorebooks_Export.json](file:///e:/repository/SvartulfrVerse/exports/Mine_Lorebooks_Export.json) (4 Lorebooks Creati sincronizzati con 952 voci totali).

---

## [13 Ottobre 2026] — Estensione RPG Totale nel Lexicon: Allineamento di 312 NPC Terziari e 14 Creature, Mostri & Boss Squarcio

### 1. Creature, Mostri, Mob e Boss dei Dungeon (14/14 Voci Lexicon — 100% Successo)

- **Allineamento Tassonomico e Strutturale:** Ciascuna voce di tipo `creature` nel Lexicon di Wyvern è stata configurata con nome normalizzato, specie RPG idonea (`lexicon_species_id`), occupazione tematica (`lexicon_occupation_id`) ed estensione RPG (`extensions.rpg`):
  - **Virus Beasts (`_C13f22wRTEM3jFe1B9bGz`):** _Macchina & Sintetico_, _Technomancer / Cyber-Mage_, Lv 35, tratti `Cyber-Augmented`, `Tech Savvy`, statistiche tarate su INT/PER.
  - **Boss Dungeon DMHA / Apex Behemoth (`_r8D1YdXXWczwfb23pzqTY`):** _Drago & Drake_, _Guild Vanguard (DPS)_, Lv 85 (Boss Grado S / Catastrofe), tratti `Apex Core Resonance`, `Blood Craze`, `Dungeon Veteran`, statistiche titaniche (STR 18, END 17, PER 13).
  - **Elementali DMHA (`_QDNczNxHGjzdTQC8qJFR1`):** _Mutante & Ibrido_, _Defender_, Lv 40, tratti `Apex Core Resonance`, `Gentle Giant`.
  - **Drider DMHA (`_NWwzXdykqgRn7bz9BH3Cm`):** _Aracnide & Drider_, _Hunter / Provider_, Lv 45, tratti `Night Stalker`, `Feral Blood`.
  - **Non-Morti DMHA / Ghoul Urbani (`_TPjPELkJxeBU3cpftkf6H`):** _Non-Morto & Revenant_, _Street Scrapper / Rogue_, Lv 28, tratti `Feral Blood`, `Symbiotic Feeder`.
  - **Yokai DMHA / Spiriti Orientali (`_xMLY7zdLqVdNMEnfYymmQ`):** _Kitsune & Neko_, _Scout_, Lv 42, tratti `Lupine Senses`, `Trickster Mentor`.
  - **Demoni Minori DMHA (`_ha21xWTkj7yKRTHJc4zPT`):** _Demone & Infernale_, _Street Scrapper / Rogue_, Lv 35, tratti `Feral Blood`, `Night Stalker`.
  - **Criptidi DMHA / Shadow Entities (`_xVhVGPEkazJHN9fn97Hhj`):** _Mutante & Ibrido_, _Scout_, Lv 46, tratti `Night Stalker`, `Apex Core Resonance`.
  - **Chimere DMHA / Bio-Armi (`_81DVqUkcyBbhbM69bb8gn`):** _Mutante & Ibrido_, _Guild Vanguard_, Lv 58, tratti `Modified / Lab Lineage`, `Feral Blood`, `Blood Craze`.
  - **Infezioni Miasma DMHA (`_7q84e4Lhtnb83HjTcXt6n`):** _Mutante & Ibrido_, _Guild Support_, Lv 32, tratti `Symbiotic Feeder`, `Apex Core Resonance`.
  - **Vilitanos DMHA (`_XPhjYq64NJYCbhMgj4jeL`):** _Mutante & Ibrido_, _Hunter / Provider_, Lv 44, tratti `Night Stalker`, `Feral Blood`.
  - **Bestiario DMHA / Registro Scientifico (`_dcFa7apQDzBF2t9Br28N7`):** _Umano_, _Academic / PhD Candidate_, Lv 50, tratti `Nerdy / Bookworm`, `Old Money / Aristocrat`.
  - **Ice Satyrs (`_b66ztLLgNRKTyfafhqRg7`):** _Minotauro & Centauro_, _Defender_, Lv 38, tratti `Gentle Giant`, `Feral Blood`.
  - **Asag Beast (`_FkXtyrhQMhCpg7N6gm1Wm`):** _Mutante & Ibrido_, _Guild Vanguard_, Lv 65, tratti `Apex Core Resonance`, `Feral Blood`, `Dungeon Veteran`.

### 2. NPC Terziari nel Lexicon (312/312 Voci Lexicon — 100% Successo)

- **Parser Euristico JED+ e Testuale:** Analisi completa di JED brackets (`SPECIES:`, `OCCUPATION:`, `AGE:`) e background per tutte le 312 voci di tipo `npc`:
  - **Specie Popolate:** Umano (227), Licantropo (20), Demi-umano (20), Demone (8), Minotauro/Satiro (8), Orco/Oni (6), Mutante/Ibrido (5), Elfo (3), Fae (3), Angelo (3), Vampiro (3), Sirena/Tritone (2), Kitsune (1), Drago (1), Divinità Primordiale (Fenris, 1).
  - **Occupazioni Assegnate:** SUCC Students & Civilians (242), Docenti/Coach/Professori (14), DCC Security & Bodyguards (13), Cacciatori DMHA (6), Artigiani & Costruttori (2), Diplomatici & PR (2), Underworld Fixers, Street Scrappers, Healers e Primordial Sovereigns.
  - **Livello RPG Dinamico:** Calcolato dall'anagrafica reale con tetto canonico a Lv 99 (Fenris Lv 99, Faculty/Docenti Lv 40-55, Operativi e Cacciatori Lv 30-45, Studenti Lv 18-22).
  - **Statistiche e Tratti:** Assegnati 1-8 tratti multipli coerenti (es. biologia licantropa, status nobiliare, veterano dungeon, orientamento medico o tecnologico) e statistiche base bilanciate su 25 punti addizionali su base 8.
- **Resilienza API & Auto-Refresh Token:** Implementato meccanismo di refresh automatico del Bearer Token di Firebase contro la scadenza oraria (risolto il falso 404 nativo di Wyvern documentato in GEMINI.md §11).

### 3. Sincronizzazione Master Export

- Master export [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) sincronizzato integralmente via API web (dimensione aggiornata a **6.03 MB** con 326 voci Lexicon RPG attive).

---

## [13 Ottobre 2026] — Sblocco Limite Tratti RPG (99 Max) & Allineamento Totale su 91 Personaggi (Classi, Tratti Multipli & Statistiche)

### 1. Sblocco Limite Tratti del World (`stat_config.max_traits`)

- **Rimozione del Collo di Bottiglia:** Il parametro `max_traits` in `stat_config` del World `_CgYT8fHXpDC4crjmegQF7` è stato elevato da 10 a **99**, consentendo a ciascun personaggio di accumulare e riflettere tutti i tratti biologici, di rango, psicologici e di classe pertinenti al proprio background narrativo.

### 2. Allineamento Integrale dei 91 Personaggi del World (100% Successo — 0 Errori)

- **Scansione Incrociata Profili & Backstory:** Analizzato il testo di ciascuna scheda (`long_summary`, `summary`, dinamiche di branco, specie e professione) e applicato un aggiornamento sistematico:
  - **Specie RPG:** Risoluzione automatica tra le 24 specie canoniche (Licantropo, Demi-umano, Vampiro, Succube, Drago, Mutaforma, Demone, Elfo, Umano).
  - **Occupazioni Specializzate:** Assegnate le classi più idonee tra le 28 disponibili (es. _Guild Berserker_ per Malachia, _Puppet Master_ per Angelo, _Technomancer_ per Jasper, _Firstborn Apex Sovereign_ per Wulfnic/Ut/Zefir, _Guild Vanguard/Tank/Support_, _DCC Security_, _Pack Leader_, _Diplomat_, _SUCC Student_).
  - **Tratti Multipli Simultanei:** Fino a 13 tratti ricchi per personaggio (es. Malachia, Alyssa e Jasper con 13 tratti completi tra biologia LSE, specializzazioni di caccia, ferormoni e status; Erik con 11 tratti; Noah con 10 tratti; Firstborn con 8-9 tratti primordiali).
  - **Statistiche Base Bilanciate:** Applicata la formula di bilanciamento su 25 punti addizionali distribuiti su base 8 (totale 81 punti statistica) tarati su archetipi (Berserker su STR/END/AGI, Tank su END/STR/PER, Technomancer/Puppet su INT/PER/AGI, Healer su LCK/CHA/PER, Diplomat su CHA/PER/INT, Scout su AGI/PER/STR).

### 3. Sincronizzazione Master Export

- Master export [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) sincronizzato e allineato all'API di Wyvern (5.88 MB).

---

## [13 Ottobre 2026] — Espansione Canonica dei 17 Lorebook: Apex Firstborn, Berserker, Puppet Master, Technomancer/Cybers, Magia Estesa & Scenario Camp Mystic

### 1. Blocco 1: Eroi, Boss dei Dungeon & Capacità Speciali (16 Voci di Lexicon)

- **Apex Predator $\rightarrow$ Firstborn & Boss Catastrofe (5 voci):**
  - _Wulfnic Bloodmoon, Ut Berg e Zefir Hvitskog:_ Codificate le fisiologie di grado Apex consacrate da Fenris (immunità all'invecchiamento e veleni, velocità superluminale e predazione silente per Zefir, titanismo e invulnerabilità per Ut, sguardo paralizzante per Wulfnic).
  - _DMHA Boss Dungeon:_ Linee guida per Entità Apex e Boss di Squarcio di Grado S/Catastrofe con scudi d'assorbimento e protocolli di confinamento coordinati.
- **Berserker Bloodline $\rightarrow$ Malachia Douglas Bloodmoon (3 voci):**
  - Codificata la classe _Berserker_ di Malachia: la _Fornace Interna_ (metabolismo termico a consumo di ferro), lo _Stato di Furia Berserker_ e la _Trinità dell'Infinito_ (forza scalare, insensibilità al dolore e aura di calore fumante).
- **Puppet Master $\rightarrow$ Angelo Moreno (3 voci):**
  - Definita la classe _Puppet Master_ e l'Aspetto Mentale per Angelo Moreno: _Fili di Mana Psichici_ (Puppeteer Strings) per il controllo di simulacri e bambole, _Demonic Gaze_ e _Sovereign Mind Core_ (labirinto mentale con archivio di memoria inviolabile).
- **Cybers & Technomancer $\rightarrow$ Jasper Douglas, Echo & Cyberspazio (5 voci):**
  - _Jasper Douglas:_ Riconosciuto come _Tecnomanzonte_ della Villa e amministratore della Rete Neurale DCC (fusione tra circuiti hardware, fibra ottica e matrici runiche).
  - _Echo:_ Definita come intelligenza e creatura _Cyber_ nativa del Cyberspazio profondo.
  - _Cyberspazio:_ Struttura delle _Data Streets_, torri server, distretti archivistici e minacce di _Virus Beasts_ (malware vivente combattuto con armi antivirus).

### 2. Blocco 2: Famigli & Magia Urban Fantasy Estesa (13 Voci di Lexicon)

- **The Familiar Species $\rightarrow$ Gestione Animali da Compagnia nel Mondo Magico (3 voci):**
  - Tassonomia e biologia dei famigli al SUCC, _Rito di Vincolo_ con sincronia empatica/telepatica bilaterale e protocolli di cura, alimentazione elisirica e clinica veterinaria arcana.
- **Discipline di Magia Urban Fantasy Avanzata (10 voci):**
  - _Gravitone:_ Manipolazione della densità e deflessione balistica cinetica.
  - _Mutaforma Fluido:_ Fisiologia non-canina e trasmutazione cellulare mimica.
  - _Dreamwalker:_ Viaggio e combattimento nel Piano Astrale Onirico durante la fase REM.
  - _The Warper:_ Piegamento spazio-temporale a corto raggio (Blink tattico) e micro-squarci.
  - _Shadow Lord:_ Umbracinesi, fusione nell'ombra e armi di tenebra congelata.
  - _Druidismo & Botanica Bellica:_ Fitochimica arcana, radici stritolatrici e guarigione organica.
  - _Sculpter:_ Rimodellazione plastica di materiali inorganici (asfalto, pietra, metallo) e costrutti di sentinella.
  - _Spell Compendium:_ Tassonomia unificata degli incantesimi accademici del SUCC dal I Circolo ai Circoli Superiori, con uso di catalizzatori e focus runici.

### 3. Blocco 3: Scenario Ufficiale "Camp Mystic" & Nuova Location Regionale

- **Nuova Location: `Camp Mystic` (`_yPxa34RwGz9wbjm1zjhLJ`):**
  - Riserva boschiva sul Lago Erie: 4 distretti residenziali, chalet in legno rinforzato e pietra fluviale, moli d'attracco per canoe, cancellata in travi di quercia e ferro runico, e barriere antimostro perimetrali.
- **4° Scenario Ufficiale: `Camp Mystic: Vacanze Estive & Addestramento sul Lago` (`_a9yMR9Q3NJzLeXLGnQpbX`):**
  - Configurato con scena introduttiva completa (`scene-camp-mystic-arrival`), party composto da Alyssa, Jasper, Noah, Malachia, Jared e Mac, location iniziale a Camp Mystic e wizard RPG con selezione personaggio attiva.

### 4. Associazioni Incrociate Personaggi, Classi RPG & Nuovi Tratti Specializzati

- **Nuove Occupazioni RPG Create:**
  - `Guild Berserker (Vanguard)` (`_d7mHQJKnQqQNzwdwnqMdM`): Assegnata a **Malachia Douglas Bloodmoon** (+4 MGT, +3 RES, +1 AGI).
  - `Puppet Master (Mind Weaver)` (`_4mxkMwTthmXt9AqXXdxfE`): Assegnata ad **Angelo Moreno** (+4 WIT, +2 PRS, +2 SCT).
  - `Technomancer / Cyber-Mage` (`_3mrK4LGktdtUHGbf6CWNp`): Assegnata a **Jasper Douglas Bloodmoon** (+4 WIT, +3 SCT, +1 AGI).
  - `Firstborn Apex Sovereign` (`_b8KfUNHq4z3bFw6jKkmzf`): Assegnata a **Wulfnic Bloodmoon**, **Ut Berg** e **Zefir Hvitskog** (+5 MGT, +5 RES, +4 AGI, +4 SCT, +2 LUK).
- **Nuovi Tratti Specializzati RPG Creati & Assegnati:**
  - `Berserker Internal Furnace` (`_L2xQk9j8RnMKUgGnCVWRR`): Associato a **Malachia Douglas**.
  - `Puppeteer Mana Strings` (`_C8XXTwLd1mmF33EkQMUyD`): Associato ad **Angelo Moreno**.
  - `Technomantic Data Resonance` (`_AQ6Qy4KHMDgFWKPHDJeqb`): Associato a **Jasper Douglas**.
  - `Apex Predator Divine Core` (`_NL4ANGp2gjKtbAgRTFxbD`): Associato a **Wulfnic**, **Ut** e **Zefir**.
  - `Familiar Soulbound Synergy` (`_kUV13hFp2R2a4aYEXq3c4`): Associato ad **Alyssa Douglas**.
- **Legame Diretto Lexicon $\leftrightarrow$ Personaggi (Regola di Lys):**
  - Convertite 12 voci specifiche in `type: "memory"` e collegate via `attached_world_character_id` ai rispettivi personaggi: Wulfnic, Ut, Zefir, Malachia (x2), Angelo (x3), Jasper (x2) e Alyssa (x2).

### 5. Sincronizzazione Master Export

- Master export [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) aggiornato:
  - **631 Voci di Lexicon** (da 602);
  - **188 Location** (da 187);
  - **4 Scenari Ufficiali** (da 3);
  - **28 Occupazioni RPG** (con Berserker, Puppet Master, Technomancer, Apex Sovereign);
  - **45 Tratti RPG** (con i 5 nuovi tratti canonici);
  - Dimensione file: **6.11 MB**.

---

## [13 Ottobre 2026] — Integrazione 74 Voci di Lexicon da "LA: New Moon" (SUCC) & "Aegis City Hunters" (DMHA) & Audit LSE

### 1. Integrazione Sistematica Lorebook Accessori

- **Declinazione SUCC (36 Nuove Voci di Lexicon):** Estratte ed armonizzate le conoscenze del lorebook _LA: New Moon Compendium_ come approfondimenti accademici e biologici del college:
  - _Biologia & Fisiologia Mutaforma (16 voci):_ Tassonomia e rigenerazione therianthrope, risonanza di branco, curve biologiche lunari, regolamento dieta/igiene olfattiva predatoria, vulnerabilità ad aconito e argento, fisiologia dei Beastwere e Diritto della Vera Forma, riserva di trasformazione e abbigliamento a memoria elastica.
  - _Ordinamento Accademico & Sicurezza (12 voci):_ Statuto di santuario accademico, codice di condotta inter-specie, rete SUCCbook, ordinamento CFU, sessioni d'esame straordinarie di plenilunio, farmacia d'ateneo e alloggi differenziati.
  - _Umani Dotati & Scienze Arcane (8 voci):_ Fenomenologia del risveglio nei giovani umani, tassonomia poteri psichico-elementali, costi metabolici e termoregolazione, schermature mentali e laboratori di teoria runica.
- **Declinazione DMHA (38 Nuove Voci di Lexicon):** Estratte ed armonizzate le conoscenze di _Aegis City Hunters_ nel contesto operativo della Gilda dei Cacciatori del DMHA:
  - _Armamenti & Balistica della Gilda (10 voci):_ Sistemi d'arma vincolata animica (Messors), generatori portatili di campo barriera (Mana Fields), dottrina del Velo, munizioni Silver-Hollowpoint, lame mana-conductive, visori spettrali per squarci e manuale tascabile di de-escalation.
  - _Bestiario Classificato & Anomalie (12 voci):_ Registro bestiario ufficiale DMHA, classificazione predatori Vilitanos, protocolli possessioni e poltergeist, aberrazioni parassitarie da miasma, chimere clandestine, non-morti, drider di faglia ed elementali fuori controllo.
  - _Divisioni Governative & Fazioni Ombra (10 voci):_ Crimson Crimes Division (CCD), Società Balor, culto del Prime Order, compagnia mercenaria Scarlet Fog, agenzia investigativa ausiliaria Serenson, Tessitori Ermetici, bonifica sanitaria e ufficio riscossione taglie.
  - _Operativi Notabili & Registri d'Onore (6 voci):_ Registro d'onore cacciatori d'elite, contratti di Classe Catastrofe (Grado S), squadre d'assalto, incursori furtivi e protocolli di mutuo soccorso con la Sicurezza DCC (Douglas).

### 2. Audit di Conformità Canonica e Coerenza LSE

- **Zero Conflitti LSE:** Verificata la piena coerenza delle 74 nuove voci con le 44 voci canoniche LSE esistenti (cicli di calore, rut, ferormoni e soppressori).
- **Anatomia Demi-Umani (Orecchie Singole):** Confermato il vincolo anatomico su tutti i testi (i demi-umani possiedono un solo paio di orecchie: quelle animali, zero orecchie umane).
- **Disciplina Tipografica:** Zero em-dash residui, virgolette doppie standard e assenza di markdown non consentito.

### 3. Sincronizzazione Master Export

- Master export [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) aggiornato da 528 a **602 voci di Lexicon native** (dimensione 6.04 MB).

---

## [13 Ottobre 2026] — Caricamento Bulk Asset nella World Gallery (159 Immagini Totali) & Sincronizzazione Completa

### 1. Caricamento Automatico Asset in Cloudflare & World Gallery

- **Scansione Completa Directory `asset/`:** Identificate 159 immagini totali (WebP, PNG, JPG/JPEG) suddivise tra:
  - `asset/characters/avatars_legacy/` (74 avatar legacy con tag `avatar`, `character`, `legacy`);
  - `asset/characters/` (illustrazioni di personaggi con tag `character`);
  - `asset/environments/` (mappe, sfondi e location con tag `environment`, `location`, `background`);
  - `asset/lore_and_gods/` (simboli sacri, Fenris, deità con tag `lore`, `deity`, `mythology`).
- **Pipeline di Upload:**
  1. Richiesta `POST /api/cloudflare/request-upload-url` con metadati e contesto `gallery`;
  2. Caricamento binario multipart/form-data sull'uploadURL Cloudflare;
  3. Registrazione `POST /api/worlds/:world_id/gallery` con titolo formattato, descrizione e tag pertinenti.
- **Risultato Upload:** **158 / 158 immagini caricate con successo (0 fallimenti)**, portando la Gallery ufficiale del World a **159 asset registrati e operativi**.

### 2. Sincronizzazione Master Export

- Master export [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) (5.91 MB) completamente allineato all'API live di Wyvern.

---

## [13 Ottobre 2026] — Implementazione Factions, Ricalcolo Livelli a Scaglioni Quinquennali, Migrazione Morfologica in Appearances & Home Locations

### 1. Sistema Factions su Tutti i 91 Personaggi

- **Conversione Faction Lexicon:** Aggiornato il campo `type` di tutte le 23 fazioni del Lexicon in `faction` nativo per renderle conformi al selettore dell'interfaccia Wyvern.
- **Binding Factions (91 / 91 - 100%):** Assegnate le fazioni d'appartenenza a ciascun personaggio del World:
  - Famiglia e Branco Douglas $\rightarrow$ _Douglas Commercial Coalition (DCC)_.
  - Clan Darkfire $\rightarrow$ _Horned Skull Clan_.
  - Famiglia Thompson $\rightarrow$ _The Thompson Family_.
  - Grave Mistake $\rightarrow$ _Grave Mistake_.
  - Ballantine Family $\rightarrow$ _Ballantine Family_.
  - The Sinners $\rightarrow$ _The Sinners_.
  - Atleti e Confraternite SUCC $\rightarrow$ _SUCC BULLS_ e _SUCC BEARS_.
  - Gilda dei Cacciatori $\rightarrow$ _DMHA (Dungeon & Monster Hazard Administration)_.

### 2. Ricalcolo Livelli RPG (Progressione a Scaglioni Quinquennali)

- **Nuova Curva di Livellamento:**
  - Età $\le 13$ anni: **Livello 1** (es. Edric Douglas, 12 anni $\rightarrow$ Lv 1).
  - Età da 14 a 18 anni: **Livello 2** (es. Jasper Douglas, 18 anni $\rightarrow$ Lv 2).
  - Età 19 anni: **Livello 3** (es. Alyssa Douglas Bloodmoon, 19 anni $\rightarrow$ Lv 3).
  - Incremento: $+1$ livello ogni 5 anni di età (es. Noah, Malachia, Mac, Danny $\rightarrow$ Lv 4; Logan, Erik $\rightarrow$ Lv 9 e 10; Firstborn millenari ancorati a Lv 99).
- Aggiornati sia il campo top-level `level` sia il campo annidato `rpg_stats.level` su tutti i 91 personaggi.

### 3. Migrazione Forme Licantrope in "Appearances" & Ripristino Outfits

- **Sezione Morfologica Dedicata (`appearances`):** Per tutti i 43 licantropi e mutaforma del World, rimossi _Hybrid Shift_ e _Full Shift_ dalla lista degli `outfits` e creati i tre stati somatici in `appearances`:
  - `Base`: Aspetto umanoide base con singoli tratti anatomici lupini.
  - `Hybrid Shift`: Forma ibrida bipede colossale da combattimento con muscolatura densa, pelliccia, artigli e fauci.
  - `Full Shift`: Forma quadrupede completa da lupo gigante da caccia e assalto.
- **Ripristino Outfits Mac e Jared:** Ripopolati e salvati con descrizioni complete dai dump di riferimento (5 outfit narrativi per Mac, 7 outfit completi per Jared).

### 4. Copertura Totale Home Locations (91 / 91 - 100%)

- Risolte le 20 schede rimaste senza dimora:
  - Darkfire $\rightarrow$ _The Cable District_ (`_RVRf9PtEdwhGt3rGGFjMC`).
  - Dominic Rogers $\rightarrow$ _Rogers' Bargain Motors_ (`_CAhgArEXA2eBDQPpPe1gE`).
  - Danny Boone $\rightarrow$ _Rory's Estate_ (`_TLEaxwQCB24kQYfYHy8pq`).
  - Russ Sinclair $\rightarrow$ _Claws Steel & Ink_ (`_3tNeXcGBfcUX6J1mtjqAw`).
  - Jet Thompson $\rightarrow$ _Coastal Residential_ (`_UeKEhHTnCP6yQk7mhMVU1`).
  - Studenti SUCC $\rightarrow$ _Apollo Dorms_, _Artemis Dorms_, _Wyrm Dormitories_, _Theta Iota Theta_, _Beta Rho Omega_.
  - Harrison Black $\rightarrow$ _Bluemoon_, Cassian Aralas $\rightarrow$ _Hex Valley_, Marlowe Voss $\rightarrow$ _Oldtown_.

### 5. Audit Finale e Sincronizzazione Master Export

- Sincronizzato l'export master in [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) (5.91 MB).

---

## [12 Ottobre 2026] — Copertura 100% RPG System: Stats, Specie, Occupazioni e Tratti su Tutti i 91 Personaggi

### 1. Parametri di Bilanciamento e Conformità ai Criteri di Sistema

- **Statistiche a 7 Attributi (Svartulfr Formula):** Tutte le statistiche sono state calibrate sul budget fisso ufficiale di Wyvern (`base_value: 8`, `point_budget: 25`, somma totale identica a **81 punti** distribuita tra `strength`, `perception`, `endurance`, `charisma`, `intelligence`, `agility`, `luck`).
- **Livello Anagrafico & Tetto a 99:** Livello impostato esattamente sull'età anagrafica calcolata dal World Clock (`(10486470 - birthdate) / (24 * 365.25)`), applicando il cap rigoroso a `level: 99` per tutti i personaggi millenari o ultracentenari (Zefir, Ut, Wulfnic, Cornelius, Magnus, Dante, Angelo, Siobhan, ecc.) per prevenire il blocco del modulo RPG.
- **Profili Personalizzati per il Main Cast:**
  - **Alyssa Douglas Bloodmoon:** Carisma 16, Intelligenza 13, Fortuna 10 (confermata fortuna sfacciata), Percezione 11, Resistenza 11, Agilità 11, Forza 9 (Supporto/Guaritrice Arcano).
  - **Jasper Douglas Bloodmoon:** Agilità 14, Percezione 13, Carisma 13, Intelligenza 12, Resistenza 12, Forza 11, Fortuna 6 (DPS/Vanguard & DJ).
  - **Malachia Douglas Bloodmoon:** Forza 16, Resistenza 15, Carisma 14, Percezione 13, Agilità 11, Intelligenza 10, Fortuna 2 (Enforcer Prime & Tank).
  - **Noah Douglas Bloodmoon:** Carisma 15, Forza 14, Resistenza 13, Agilità 12, Intelligenza 11, Percezione 11, Fortuna 5 (Golden Boy & Pack Leader in seconda).
  - **Erik Douglas:** Carisma 17, Forza 16, Resistenza 15, Percezione 13, Intelligenza 11, Agilità 9, Fortuna 0 (Patriarca Alpha).

### 2. Collegamento Dinamico Specie, Occupazioni e Tratti

- **Specie & Occupazioni:** Collegate tutte le 91 schede ai rispettivi record relazionali RPG (`species_id` e `occupation_id` sia top-level che annidati in `rpg_stats`), garantendo che il selettore Wyvern non mostri campi vuoti o `None`.
- **Assegnazione Tratti (Array di ID):** Integrati i tratti RPG per tutti i 21 personaggi che ne erano sprovvisti, portando la presenza di `character_traits` al 100% (91/91).

### 3. Audit Finale e Sincronizzazione Master Export

- **Audit Finale (GET su server live):**
  - `rpg_stats`: 91 / 91 (100%)
  - `character_traits`: 91 / 91 (100%)
  - `species_id`: 91 / 91 (100%)
  - `occupation_id`: 91 / 91 (100%)
- Sincronizzato l'export master in [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) (5.86 MB).

---

## [12 Ottobre 2026] — StoryEngine Interattivo: Smartphone OS, Libretto Accademico SUCC & Bacheca Gilda DMHA

### 1. Interattività Completa Pannello Smartphone (`panel_smartphone_os`)

- **Architettura a Schermi Multipli:** Implementata navigazione dinamica a stati (`screen: 'home' | 'telegram' | 'succbook'`) senza ricaricare il pannello.
- **Telegram Douglas:** I banner e i badge di nuovi messaggi aprono la chat di gruppo _Family Douglas_ con messaggi in-character (Erik, Noah, Jasper, Malachia) e una barra di input con invio fittizio reattivo.
- **SUCCbook Feed:** Le notifiche aprono il feed del campus con comunicazioni del rettorato, feste della Confraternita Delta-Fang, avvisi del laboratorio alchemico ed eventi studenteschi.

### 2. Libretto Accademico SUCC Dinamico & Party-Aware (`panel_succ_academics`)

- **Filtraggio Automatico del Party:** Il pannello ispeziona dinamicamente i partecipanti attivi nella chat / nel party.
- **Esclusione Automatica Non-Studenti:** Mac (che non va all'università) e i membri adulti della famiglia vengono automaticamente esclusi dai tab.
- **Tab Dinamici per Studenti Attivi:** Mostra i tab esclusivamente per gli universitari presenti (Alyssa, Jasper, Noah, Malachia, Jared, Edric, Viola), con GPA personalizzato (3.98 per Alyssa, 3.85 per Jasper, ecc.), CFU/ECTS, esami sostenuti e tirocini.
- **Toggle Rapido:** Aggiunto selettore rapido tra i soli presenti nel party e l'intero gruppo di studio del branco.

### 3. Registro Cacciatori & Bacheca Contratti DMHA Interattiva (`panel_dmha_guild`)

- **Fireteam & Profili Membri:** Rilevamento dei soli cacciatori DMHA presenti nel party (Alyssa, Jasper, Malachia, Noah, Mac, Jared, Kaladin) con dettagli sul rango (da S a C), licenza, kill confermate e rateo di successo.
- **Bacheca Contratti Dinamica:** Elenco interattivo di 5 missioni con ricompense in crediti e livello di rischio.
- **Gestione Incarichi in Tempo Reale:** Aggiunti bottoni funzionali per `Accetta / Prenota Incarico` (stato `PRENOTATA / IN CORSO`), `Completa (+CR)` (accredito crediti e marcatura `COMPLETATO`) e `Abbandona` (rilascio contratto).

### 4. Deploy e Pubblicazione Wyvern

- Pubblicata la nuova revisione StoryEngine `engine_revision_bDBG3d9JHeBh2nj78ywYp` (versione 67) associata al World `_CgYT8fHXpDC4crjmegQF7`.
- Sincronizzato ed esportato il file master [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json) (5.7 MB).

---

## [12 Ottobre 2026] — Risoluzione Errore Creazione Chat Log (BSON ObjectId Cast) & Pulizia Inventari Fantasma

### 1. Root Cause dell'Errore `Argument passed in must be a string of 12 bytes or a string of 24 hex characters or an integer`

- **Diagnosi Approfondita:** L'errore MongoDB BSON si verificava durante la chiamata `POST /api/new/chat-logs/world` all'avvio dello scenario 3 (_Alyssa's Story: Cronache del Primo Anno_).
- **Doppia Causa Identificata:**
  1. **Phantom Lexicon References in `default_inventory`:** Jasper (`_x3VY2kcbaDbKyCqywGeET`), Malachia (`_rAcN9GXD1Le4WxY28e49W`), Zefir (`_FJhtBq4xUM4aUWpaJAPYF`) e Ut (`_NYtBzeKNkm3pedHMnYaka`) contenevano riferimenti a oggetti di inventario eliminati o inesistenti nel Lexicon (`_746G8T2RVL2tRExw337cq`, `_8WaPQUH42VgQz2xVXaJF7`, `_GNAP7tw8UWry76Dww36FR`, `_xbjVJJ3aNC4W9Uz4nNn4d`, `_XNkgRjKF6XRnKqgJjkUR3`). Durante l'inizializzazione del party e dei partecipanti, il backend di Wyvern tentava di risolvere tali ID tramite un fallback a `new ObjectId(lexicon_entry_id)`, fallendo sui NanoID non-hex.
  2. **Orphan Characters in `included_character_pool`:** Lo Scenario 3 conteneva 3 ID di personaggi obsoleti e cancellati dal World (`_c9RzyCnzzLey247dtph9x`, `_ykqALFc4CQN14zTrMQpat`, `_J3pEpeWqWFQBPtN3mjrDW`).

### 2. Risoluzione Applicata e Verifica Empirica

- **Epurazione Inventari:** Azzerato `default_inventory: []` via `PUT /api/worlds/characters/:id` per Jasper, Malachia, Zefir e Ut.
- **Bonifica Character Pool Scenario 3:** Ripulito `included_character_pool` e `resolved_characters` eliminando le voci orfane e mantenendo i 18 personaggi canonici validi.
- **Test di Validazione:**
  - Eseguiti test `POST /api/new/chat-logs/world` sia minimi sia con l'intero payload inviato dal browser (con `greeting_id: scene-alyssa-story-1-1`, valori dei campi, persona): **HTTP 200 OK**, chat log `chat_log_jYwGLNYLfd3PbdwKHgwgR` creato e inizializzato regolarmente.
  - Risincronizzato l'export master in [exports/Svartulfr_Export.json](file:///e:/repository/SvartulfrVerse/exports/Svartulfr_Export.json).

---

## [12 Ottobre 2026] — Risoluzione Intro Scenari Wyvern & Configurazione Completa 24 Specie RPG

### 1. Snellimento Wizard di Introduzione & Risoluzione Conflitti RPG

- **Rimozione Domande Ridondanti:** Eliminate le pagine custom `p_species_select` e `p_occupation_select` da `introduction_pages` (ridotte da 12 a 10 pagine pulite) e dai campi `intro_fields` del World e dei 3 Scenari. La selezione di Specie e Occupazione viene demandata interamente al modulo nativo Wyvern RPG (`p_rpg_build`), prevenendo duplicazioni di input.
- **Fix Propagazione `fields` negli Scenari:** Risolto il bug di Wyvern in cui la selezione di uno scenario non ereditava i campi del World cercando `H.fields`: sincronizzati tutti i 7 campi attivi nei 3 Scenari ufficiali.

### 2. Configurazione Completa e Popolamento delle 24 Specie RPG

- **Risoluzione Campi Vuoti nel Sistema RPG:** Identificate le 21 voci di specie create come stub vuoti (`name: ""`, `desc: "undefined"`, `stat_modifiers: {}`).
- **Popolamento Completo via REST API (`/api/worlds/rpg/species`):**
  - Configurate con nomi completi, descrizioni lore-accurate e modificatori di statistiche bilanciati su tutti e 7 gli attributi (`strength`, `perception`, `endurance`, `charisma`, `intelligence`, `agility`, `luck`).
  - Specie canonizzate: Licantropo, Demi-umano, Umano, Vampiro, Elfo & Sidhe, Demone, Fata & Fae, Angelo, Drago & Drake, Orco & Oni, Succube & Incubo, Minotauro & Centauro, Tritone & Sirena, Kitsune & Neko, Mutaforma, Non-Morto, Lamia & Naga, Aracnide & Drider, Macchina & Sintetico, Mutante & Ibrido, Divinità & Primordiale.
  - Nessun campo vuoto o "No modifiers" residuo nel selettore delle specie di Wyvern.

---

## [12 Ottobre 2026] — Implementazione StoryEngine "Svartulfr OS" e Diagnosi Architettura Wyvern

### 1. StoryEngine: Architettura e UI Panels

- **Creazione Engine Ufficiale:** Creato ed evoluto lo StoryEngine `Svartulfr OS` (`engine_HCTPXhL8xr89wUY9r9dYU`) targettato per `world` e `character` (`target: "both"`).
- **Separazione e Restyling dei 3 Pannelli UI React:**
  - `panel_smartphone_os` (**Svartulfr Smartphone 5G**): Interfaccia OS mobile per `{{user}}`, notifiche Telegram Douglas, social SUCCbook, tracker fase lunare e ciclo LSE biologico, pulsante interattivo rapido per inalazione soppressori ferormonali.
  - `panel_succ_academics` (**Libretto SUCC & Carriera Accademica**): Integrazione metrica GPA (`3.72 / 4.00`), CFU conseguiti (28 CFU), elenco insegnamenti con voti in lettere (A, B, C), orario lezioni e opportunità tirocini (DCC Security / Hunters Guild).
  - `panel_dmha_guild` (**Registro Gilda DMHA & Caccia Rift**): Separazione completa dalla carriera universitaria. Tracciamento Rango cacciatore (Rango C), saldo crediti (1.450 crediti), storico cacce completate (7), bacheca contratti attivi e inventario bottino/armi.
  - **Design & Spacing:** Applicato padding interno (`12px 14px`), border curvature (`rounded-xl` / `8px`), palette scura zincata coerente (`#18181b`, border `#27272a`) e spacing anti-sovrapposizione per prevenire testo appiccicato ai bordi del viewport.

### 2. Runtime Variables & Simulation State

- Configurate 22 variabili reattive nello StoryEngine:
  - Parametri astronomici: `moon_phase`, `moon_full_active`, `day_night_cycle`.
  - Biologia LSE: `lse_biology_status` (Dormant/Pre-Heat/Heat/Rut), `lse_cycle_days_left`, `pheromones_suppressors_count`.
  - Dinamiche di Branco: `pack_standing`, `pack_chat_unread`, `succbook_unread_posts`.
  - Rifts & Sicurezza: `active_rift_alert`, `rift_danger_level`.
  - Accademia SUCC: `succ_gpa`, `succ_credits`, `succ_courses`, `succ_internships`.
  - DMHA Guild: `guild_rank`, `guild_credits`, `guild_quests_completed`, `guild_active_quest`, `guild_available_quests`, `guild_loot`.

### 3. Triage Lorebook Extra e Dipendenze Engine

- **Lorebook Esterni:** Scollegati dall'engine i lorebook esterni `LA: New Moon Compendiu` (`_U9TVTNMFk3R1VdAUV9yhP`) e `Aegis City Hunters` (`_1fPzRX9nz4LgtkcQWVha8`) per estrarne le regole direttamente nel Lexicon nativo di SUCC e DMHA.
- **Ripristino Lorebook Canonici:** Mantenuto il set di 21 lorebook tematici canonici (Svartúlfr Locations, Lorebook generale, NPC Primari e Secondari, Camp Mystic, classi e archetipi sovrannaturali).

### 4. Diagnosi Blocco Piattaforma: _"Public hosts require published accessible StoryEngines"_

- **Identificazione del Vincolo:** Wyvern impedisce il salvataggio di StoryEngine (`PUT /api/story-engines/hosts/{hostType}/{hostId}`) su host che possiedono lo status `approved` (come il World `Svartúlfr`, `_CgYT8fHXpDC4crjmegQF7`), qualora l'engine collegato non risulti pubblicamente accessibile.
- **Causa Tecnica:** Un'entità impostata su `visibility: "public"` entra nello stato `moderation_status: "pending"`. Fintanto che non riceve approvazione globale o non viene gestita come modulo approvato, il backend di Wyvern rigetta l'aggancio all'host con errore HTTP 400.
- **Azioni Intraprese:**
  - Isolati e mappati via reverse engineering dei bundle Next.js gli endpoint nativi:
    - `GET /api/story-engines/hosts/{hostType}/{hostId}`
    - `PUT /api/story-engines/hosts/{hostType}/{hostId}` con payload `{ attachments: [...] }`.
  - Verificati i requisiti di schema per `preset_id` (stringa obbligatoria) e `expected_version` per le chiamate PUT/publish.

### 5. Refactoring UI Panels (Tailwind + Shadcn) & Risoluzione Errori Chat

- **Risoluzione Syntax Error CSS:** Corretta la stringa malformata con doppio apice (`border: '1px solid '#92400e'`) in `panel_succ_academics`.
- **Superamento del Blocco "Unsupported panel style":**
  - Riscontrato che il renderer sandbox dei pannelli Wyvern rigetta oggetti `style={{ ... }}` con proprietà CSS non supportate.
  - Riscritti tutti e 3 i pannelli (`panel_smartphone_os`, `panel_succ_academics`, `panel_dmha_guild`) adottando unicamente classi Tailwind native e i componenti Shadcn integrati nel runtime Wyvern (`<Card>`, `<CardHeader>`, `<CardTitle>`, `<CardDescription>`, `<CardContent>`, `<Badge>`, `<Button>`).
- **Allineamento Schema Icone:** Corrette le icone dei pannelli per rispettare l'enum Zod dell'API Wyvern (`layout`, `book`, `swords` invece di valori non previsti come `smartphone` o `sword`).
- **Pulizia Cassetto StoryEngines Chat:** Impostato `hidden: true` sulla variabile `quests` e sulle variabili di stato JSON per impedire a Wyvern di iniettare dump di dati grezzi nel cassetto superiore della chat.
- **Correzione Mappatura Variabili Runtime & Dati Astronomici (Revisione `engine_revision_pGVbrmBULL6wXtWdpEcD9`):**
  - Risolto disallineamento tra gli ID delle variabili del pannello e dell'engine: corretto `scent_suppressors_count` (anziché `pheromones_suppressors_count`), `pack_reputation` (85/100 · Riconosciuto anziché fallback), `rift_threat_level` e il comando `cmd_use_suppressor` collegato al tasto _Inala Dose_.
  - Integrati i dettagli astronomici reali per la timeline (26 Agosto 2024, 21:15 Nightfall): visualizzazione `Ultimo Quarto Calante (~48% · Gemelli)`, badge reattivo `🌙 Notte` al subentrare delle ore notturne, e sincronizzazione del template di stato per i buff notturni dei Vampiri/Undead.
- **Adattamento Dinamico su `{{user}}` e Persona Attiva (Revisione `engine_revision_XXqLH3CP4BejFVN1YawVP`):**
  - **Risoluzione Hardcoding Libretto Accademico (`panel_succ_academics`):** Eliminato l'elenco statico di corsi. Il pannello ora riconosce automaticamente la persona attiva (o permette la selezione rapida in-panel dei percorsi accademici):
    - **Alyssa Douglas (Pre-Med / Scienze Mediche & Demi-Umani):** Corsi dedicati ad Anatomia Comparata Demi-Umani (Prof. Moreau), Farmacologia Arcana & Inibitori Ferormonali (Prof. Loewe), Traumatologia d'Emergenza & Ferite da Argento (Prof. Vane), Diritto Sanitario e tirocinio presso l'Infermeria SUCC e la Divisione Medica DCC della Dr.ssa Elizabeth Duskwood (GPA 3.92).
    - **Jasper Douglas (Ingegneria Arcana & Meccanica Avanzata):** Ingegneria dei Materiali & Balistica Silver-Tech, Geometria Non-Euclidea & Meccanica dei Rift, Runecore Engineering, con stage presso l'R&D Sistemi Tattici e Droni DCC.
    - **Percorso Tattico / Custom:** Curriculum di scienze tattiche e incursioni sotterranee.
  - **Risoluzione Hardcoding Gilda dei Cacciatori (`panel_dmha_guild`):**
    - Rimossa la missione fittizia arbitrariamente marcata come `IN CORSO`. Il pannello ora legge lo stato effettivo da `dmha_active_mission` e, in assenza di contratti attivi, mostra chiaramente lo status `NESSUNA (STANDBY / LIBERA)` con tutti i contratti in bacheca marcati come `DISPONIBILE`.
    - Rango e statistiche calibrati su `{{user}}`: per Alyssa e Jasper imposta automaticamente il rango canonico **Rango A** (Cacciatore d'Elite) con statistiche di crediti e missioni commensurate al loro livello.
  - **Aggiornamento Prompt Template del Narratore:** Aggiunta sezione obbligatoria `=== ADATTAMENTO DINAMICO DEL PROFILO ACCADEMICO E DI CACCIA DI {{user}} ===` nel `prompt_template` dell'engine per vincolare l'LLM a dedurre materie, esami e rango direttamente dalla biografia/scheda del personaggio attivo.
- **Restyling UI Dark Theme & Coordinamento Palette (Revisione `engine_revision_6fVaU1Pr2T3C1MnaUKDJB`):**
  - **Superamento dell'Effetto "Wireframe":** Eliminate le doppie linee bianche e i bordi rigidi che creavano un aspetto da scheletro grafico vuoto. Introdotti sfondi a strati morbidi (`bg-[#0e0e11]` per il container principale, `bg-[#16161c]` per le card interne) con bordature soffuse (`border-[#232329]`).
  - **Applicazione Palette Coordinata su Nero (Classi Tailwind Precompilate di Wyvern):**
    - Individuato tramite analisi del bundle CSS che Wyvern non supporta valori arbitrari JIT (es. `bg-[#16161c]` o `text-[#d4d4d4]`), i quali rendevano gli sfondi trasparenti (nero piatto) e costringevano gli elementi a ereditare bordi bianchi wireframe di default.
    - Mappate e applicate le classi native verificate dal foglio di stile di Wyvern:
      - `#d4d4d4` (bianco grigino): `text-zinc-300` / `text-zinc-200` / `text-zinc-100`.
      - `#a8c7fa` (blu chiaro): `text-sky-300` con badge `bg-blue-950 text-sky-300`.
      - `#87bc8f` (verdino): `text-emerald-400` con badge `bg-neutral-950 text-emerald-400`.
      - `#e5c07b` (giallino): `text-amber-300` con badge `bg-yellow-900 text-amber-200`.
      - `#facc15` (giallo highlight): `text-yellow-400` e badge GPA `bg-yellow-900 text-yellow-300`.
    - Superfici scure piene applicate con `bg-neutral-900` e `border-0` su tutte le righe interne: rimosso l'effetto wireframe a scatole bianche, sostituito da card scure piene con contrasto morbido su sfondo `bg-black`.
  - **Risoluzione Spaziatura e Margini ("Testo Appiccicato"):** Incrementato il padding interno a `p-4` sulle card e `p-3.5` sui singoli record, con interlinea rilassata (`leading-snug` / `leading-relaxed`) e margini adeguati per impedire qualsiasi collisione visiva tra lettere, badge e bordi dei contenitori.

### 6. Scollegamento Lorebook e Pubblicazione Ufficiale Engine Revision

- **Scollegamento Dipendenze Esterne:** Seguendo l'architettura dei motori pubblici approvati (es. _Lord of the Mysteries_, _Digitalis_), l'array `definition.lorebooks` è stato impostato a `[]`, rimuovendo i 21 lorebook con visibilità privata o non ancora approvati che causavano l'errore `403 A StoryEngine lorebook dependency is unavailable`.
- **Pubblicazione Eseguita con Successo (HTTP 200):** Pubblicata la revisione ufficiale `engine_revision_AfY736np8rYK7UULPPT4g` per `Svartulfr OS` (`engine_HCTPXhL8xr89wUY9r9dYU`), versione 50 (`status: "published"`, pronto per l'attivazione in chat e per la validazione finale da parte di Wyvern).

### 7. Importazione Voci Canoniche nel World Lexicon

Importate direttamente nel Lexicon del World `Svartúlfr` (`_CgYT8fHXpDC4crjmegQF7`) 5 nuove voci enciclopediche canoniche adattate dalle fonti esterne (_LA: New Moon Compendium_ e _Aegis City Hunters_), perfettamente armonizzate con l'ambientazione e prive di markdown (`**`) o em-dash (`—`):

1. **`SUCC: Codice Studentesco & Convivenza Predatori e Prede`** (`_HqqbF9nck9wCNB7rtrdLC`): Regolamentazione della convivenza multi-specie nel campus di Solarton, zone franche e tutela della privacy nei dormitori.
2. **`SUCC: Protocollo di Sicurezza Luna Piena`** (`_dBJXFfzdbjXFRUnLLQKf2`): Gestione accademica flessibile, mensa notturna ad alto apporto calorico, aree boschive per la corsa libera (_Howling Fields_) e supporto medico non coercitivo.
3. **`SUCC: Normativa Ferormoni, Soppressori & Duelli Accademici`** (`_XJPw9mNMcPqEkH6cUt1Pg`): Disciplina sull'uso di inibitori e soppressori di odore per aerosol, divieto di manipolazione chimica e regole d'ingaggio per il Dueling Club.
4. **`DMHA: Protocollo Operativo di Caccia & Dispositivi di Contenimento Mana`** (`_eVJnRxCHkKHrtPWFjTar7`): Dotazione e posizionamento dei generatori di Campo Mana (Repulsion Fields) per occultare le operazioni di caccia e preservare il Velo dalla popolazione civile mortale.
5. **`DMHA: Codice di Giurisdizione Tattica DCC & Gilda dei Cacciatori`** (`_raytzFKRDDT3cyf9Hxb4x`): Coordinamento operativo e confini di giurisdizione tra milizia di branco Douglas, Security Division DCC del Major Kaladin Nargathon, Crimson Crimes Division (CCD) e Gilda dei Cacciatori.

### 8. Bonifica e Snellimento del World

- **Epurazione Meccanica Legacy Social:** Rimosso il blocco obbligatorio `<live_feed_mechanic>` dalle `final_instructions` del World, che forzava l'inclusione di 3-9 commenti fittizi al termine di ogni risposta. Tale dinamica è ora interamente delegata e gestita dai pannelli interattivi dello StoryEngine (`Svartulfr OS`).
- **Preservazione Formattazione In-Scene:** Conservata la guida stilistica opzionale per le comunicazioni digitali in-scene (`<in_scene_digital_formats>`) per chat Telegram, messaggi privati e social.
- **Allineamento Disciplina di Formattazione:** Inserita la clausola standard vincolante sulle virgolette per il parlato, testo piano per le azioni e divieto assoluto dell'em-dash. Snapshot di sicurezza archiviato prima dell'applicazione.

### 9. Allineamento Questionario World Introduction & Compilazione Variabili StoryEngine

- **Espansione Questionario di Inizio (Introduction Pages & Fields):** Riorganizzato il flusso d'introduzione del World `Svartúlfr` (`_CgYT8fHXpDC4crjmegQF7`) estendendolo da 8 a 12 schermate tematiche con diramazione condizionale (`visible_when`) e regole di corrispondenza (`match_rules`), consentendo la compilazione diretta delle variabili di stato dello StoryEngine fin dall'avvio della chat:
  - **Biologia & Rango Secondario LSE (`field-secondary-sex`):** Assegna `player_secondary_sex` e popola deterministicamente `lse_biology_status` (Alpha $\rightarrow$ "Pre-Rut / Vigile", Beta $\rightarrow$ "Dormant / Stabile", Omega $\rightarrow$ "Pre-Heat / Sensibile", Delta $\rightarrow$ "Dormant / Vigile", Standard $\rightarrow$ "Non-Lupino (N/A)"), dosi iniziali soppressori di odore (`scent_suppressors_count`: da 0 a 4) e giorni residui al picco (`lse_cycle_days_left`).
  - **Fazione di Partenza (`field-origin`):** Assegna `player_origin`, coordinate geografiche d'avvio (Villa Douglas, DMHA HQ, Campus SUCC, Docks), fondo cassa iniziale (500 USD) e reputazione di branco Douglas (`pack_reputation`: 85 per Douglas, 35 per DMHA, 30 per SUCC, 15 per Underworld).
  - **Ramo Branco Douglas (`field-pack-role`):** Selezione ruolo nella Tenuta (Sentinella Baia, Esecutore Tattico, Infermeria Medica, Logistica Civile) con calibrazione reputazione e dotazione soppressori.
  - **Ramo Cacciatori DMHA (`field-dmha-rank` & `field-role`):** Selezione Rango di caccia (da Rango D a Rango S) che valorizza `dmha_hunter_rank`, crediti di gilda iniziali (`dmha_guild_credits`: fino a 7.500 CR), storico missioni (`dmha_missions_completed`) e ruolo tattico (Vanguard, Striker, Infiltrator, Combat Medic, Specialist) con borsa d'ingaggio di 10.000 crediti DMHA.
  - **Ramo Accademico SUCC (`field-succ-track`):** Selezione indirizzo di studi (Pre-Med, Ingegneria Arcana, Scienze Tattiche, Miasma Toxicology) che valorizza `succ_track`, media accademica di partenza (`succ_gpa`: da 3.60 a 3.92) e crediti formativi maturati (`succ_cfu_earned`).
  - **Ramo Bassifondi Underworld (`field-underworld-role`):** Selezione specializzazione (Fixer, Contrabbandiere di Core, Mercenario Freelance) con accredito crediti e status nel sottobosco criminale.
- **Sincronizzazione Variabili StoryEngine (Revisione `engine_revision_7qxkfbf1Nn4Jj2bNnBbE7`):**
  - Dichiarate formalmente nell'engine `Svartulfr OS` (`engine_HCTPXhL8xr89wUY9r9dYU`, v60) le nuove variabili reattive `succ_track`, `pack_role` e `underworld_role`.
  - Aggiornato il componente React `panel_succ_academics` affinché inizializzi automaticamente il piano di studi e la visualizzazione del libretto leggendo prioritariamente `engine.values.succ_track` configurato nel questionario del World.
  - Pubblicata la nuova revisione ufficiale con status `published`.

### 10. Audit Finale, Bonifica Tipografica & Completamento Lorebook Esterni

- **Bonifica Em-Dash Residui:**
  - Rimosso l'em-dash presente nella `context_description` del World (`_CgYT8fHXpDC4crjmegQF7`) nella descrizione del Major Kaladin Nargathon, convertito in virgola come da Regola 3.
  - Bonificata la voce di Lexicon `Species: God & Primordial` (`_pf9FRybEA1Y7naxw7TDQE`), eliminando l'em-dash nella clausola sui Primordiali.
- **Completamento Importazione da LA: New Moon Compendium & Aegis City Hunters:**
  - Create e collegate al World 3 nuove voci canoniche nel Lexicon per colmare gli aspetti sistemici di vita universitaria e caccia:
    1. **`SUCC: Ristorazione Universitaria & Nutrizione Metabolica Multi-Specie`** (`_cHWapLYF6kyLTaaw8a4pF`): Organizzazione della mensa centrale di Solarton, menù ipercalorici per licantropi (fino a 5.000 kcal e apporto ferrico pre-plenilunio), dispensario ematico sintetico certificato DCC Medical Ward per vampiri ed emovori, e aree botaniche separate a tutela olfattiva per fauni e minotauri.
    2. **`DMHA: Dotazione Standard & Balistica Runica per Cacciatori`** (`_DG4frH4W3yqNMzJXYVVPU`): Specifiche sull'armamento dei cacciatori della Gilda, munizionamento Silver-Hollowpoint anti-rigenerazione, lame runiche mana-conductive anti-corrosione da chitina e visori spettrali eterici per l'individuazione di squarci Classe 1 e 2.
    3. **`SUCC: Sistema Residenziale & Dormitori del Campus di Solarton`** (`_NXA2RPpp6RHTVtxRa9pD7`): Architettura degli alloggi studenteschi, ali rinforzate a isolamento acustico e strutturale per risvegli e corse notturne, ali neutre con filtri a carboni attivi e soppressori ambientali per Omega e umani, e coprifuoco biometrico dopo le ventidue.
- **Verifica Statistica e Integrità del World (Export Sincronizzato):**
  - Totale Voci Lexicon: **528** (zero duplicati, zero em-dash, zero istruzioni/prompt residui gestiti dall'engine).
  - Totale Locations: **187** (zero em-dash).
  - Totale Personaggi Nativi: **91**.
  - Master export `exports/Svartulfr_Export.json` sincronizzato e allineato al 100% con l'API live di Wyvern.

### 11. Armonizzazione e De-duplicazione tra World ed Engine (3 Aree Core)

- **Player Start & Questions:**
  - **Allineamento Valuta Wallet & Crediti Gilda:** Eliminata l'assegnazione forzata e indiscriminata di 10.000 crediti fissi in `field-role`. Integrato in `field-dmha-rank` il binding scalare `grant_currency` (da 500 CR per Rango D fino a 7.500 CR per Rango S) affinché il saldo del wallet nativo del World (`currencies`) corrisponda con precisione millimetrica ai crediti visualizzati nel registro caccia dell'Engine (`dmha_guild_credits`).
- **Scripts & Adv. Features:**
  - **Disattivazione Navi Cross-World:** Impostato `allow_ship_arrivals: false` (allineato alle regole di progetto dove le navi multi-mondo sono estranee al canone).
  - **Pulizia Inline Commands (`inline_command_config`):** Rimossa la voce `scent suppressors` da `item_use`. La somministrazione dei soppressori di odore è gestita come risorsa biologica LSE nativa dall'engine (`scent_suppressors_count` con comando rapido collegato al pulsante _Inala Dose_ nel pannello OS).
- **Prompt & AI:**
  - **Epurazione Testo di Ambientazione Duplicato:** Rimosso il blocco dei 5 paragrafi storici di World Lore da `StoryEngine.prompt_template` (già presente e centrale in `World.context_description`), evitando di iniettare per due volte la medesima prosa a ogni turno di chat.
  - **Semplificazione Formati Digitali:** Sostituito il pesante blocco di 50 righe di mockup ASCII da `World.final_instructions` con una direttiva narrativa snella. I feed Telegram del Branco, SUCCbook e bacheca caccia sono delegati interamente ai componenti React nativi di `Svartulfr OS`.
  - **Nuova Revisione Engine Pubblicata:** Eseguito deploy con successo della revisione **`engine_revision_axcEkt8qRtgNDYDgQXT1C`** (versione 62).

### 12. Esplicitazione Chiavi StoryEngine & Dati di Sistema nelle Schede Canoniche (Alyssa & Jasper)

- **Allineamento Regola 2 (Risoluzione Macro `{{age}}`):**
  - Sostituita la macro `{{age}}` con l'età anagrafica e data di nascita esplicita sia per Alyssa che per Jasper: `AGE: 19 (Born April 22, 2005);` (allineato all'ora Epoch 10320312).
- **Integrazione Chiavi di Stato nelle Schede Personaggio (`long_summary` & `summary`):**
  - **Alyssa Douglas Bloodmoon (`_MXcEC8Y6B3BNm3b1ttHj6`):**
    - Inserita nel blocco JED+ e nella nuova sezione `SYSTEM & ENGINE KEYS` l'esplicitazione formale delle chiavi dell'engine:
      - Biologia LSE: `player_secondary_sex = "omega"`, `lse_biology_status = "Pre-Heat / Sensibile"`, `scent_suppressors_count = 4`, `lse_cycle_days_left = 10`, `werewolf_lunar_buff = true`.
      - Dinamiche di Branco: `player_origin = "pack_douglas"`, `pack_role = "medical_support"`, `pack_reputation = 95/100`, `pack_chat_unread = 5`.
      - Carriera SUCC: `succ_track = "pre_med"`, `succ_gpa = "3.92"`, `succ_cfu_earned = 38`, `succbook_unread_posts = 7`, tirocinio infermeria SUCC e reparto DCC della Dr.ssa Elizabeth Duskwood.
      - Gilda DMHA: `dmha_hunter_rank = "Rango A"` (Hunter Elite / Field Medic), `dmha_guild_credits = 4850 CR`, `dmha_missions_completed = 18`, `dmha_active_mission = "none"` (Standby / Libera).
  - **Jasper Douglas Bloodmoon (`_x3VY2kcbaDbKyCqywGeET`):**
    - Inserita nel blocco JED+ e nella nuova sezione `SYSTEM & ENGINE KEYS` l'esplicitazione formale delle chiavi dell'engine:
      - Biologia LSE: `player_secondary_sex = "beta"`, `lse_biology_status = "Dormant / Stabile"`, `scent_suppressors_count = 1`, `lse_cycle_days_left = 30`, `werewolf_lunar_buff = true`.
      - Dinamiche di Branco: `player_origin = "pack_douglas"`, `pack_role = "tactical_enforcer"`, `pack_reputation = 90/100`, `pack_chat_unread = 3`.
      - Carriera SUCC: `succ_track = "engineering"`, `succ_gpa = "3.85"`, `succ_cfu_earned = 42`, `succbook_unread_posts = 4`, stage R&D Sistemi Tattici e Balistica DCC.
      - Gilda DMHA: `dmha_hunter_rank = "Rango A"` (Vanguard Tech & Recon Support), `dmha_guild_credits = 3600 CR`, `dmha_missions_completed = 14`, `dmha_active_mission = "none"` (Standby / Libera).
  - **Pulizia Tipografica:** Rimossi tutti gli em-dash residui nelle descrizioni e aggiornati i campi `summary` con i tag sintetici delle chiavi.

### 13. Audit di Allineamento Alyssa (Persona vs World Character) & Integrazione Outfit

- **Verifica Incrociata dei Testi Narrativi:**
  - Eseguita comparazione integrale tra la Persona attiva dell'utente (`current_persona`) e la scheda Character nativa di **Alyssa Douglas Bloodmoon** (`_MXcEC8Y6B3BNm3b1ttHj6`).
  - Confermata la perfetta corrispondenza e identità al 100% di tutte le sezioni di Lore e prosa JED+: `BACKSTORY`, `FAMILY & PACK`, `VOICE & BEHAVIOR`, `THE WHITE MOON & THE PACIFIST VOW`, `THE SUNSHINE SHE BRINGS`, `SEXUALITY & INTIMACY` e l'inventario `SIGNATURE ITEMS & VEHICLE`.
  - La scheda World integra in aggiunta la risoluzione esplicita della data di nascita (`AGE: 19 (Born April 22, 2005);`) e il blocco direttive `SYSTEM & ENGINE KEYS` per l'aggancio deterministicamente reattivo dello StoryEngine.
- **Allineamento Guardaroba & Outfits (18/18):**
  - Riscontrato che la Persona possedeva 18 outfit configurati mentre la scheda nativa del World ne contava 17, mancando del 18° outfit da serata.
  - Aggiunto via API e sincronizzato il 18° outfit ufficiale **`Clubbing Night`** (`outfit-alyssa-clubbing-night`):
    - **Avatar / Immagine:** `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/8786df65-425f-4aba-6377-d91d4ad95900/public`.
    - **Descrizione:** Abbigliamento da club con maglia a rete nera sopra reggiseno a fascia giallo girasole fasciante per seno DD-cup, minigonna plissettata jeans con apertura sartoriale posteriore per coda lupina caramello e nera, sandali a zeppa, pochette con tracolla a catena, smokey eye da club, treccine e tatuaggio Gebo al polso.
  - Il set di outfit di Alyssa nel World raggiunge la parità assoluta 1:1 (18 outfit su 18) con la Persona.
- **Sincronizzazione Master Export:** Aggiornato `exports/Svartulfr_Export.json` con lo snapshot live post-scrittura.

### 14. Risoluzione Schermata Vuota Questionario Step 5 (Specie) & Step 11 (Occupazione)

- **Diagnosi del Blocco Step 5 ("Specie di Origine"):**
  - Riscontrato che la schermata dello Step 5 risultava completamente vuota/nera a causa dell'uso di `type: "species_select"`, che interrogava l'array `world.species` popolato con 24 ID obsoleti non presenti nel Lexicon nativo del World.
- **Implementazione del Campo Canónico `field-species`:**
  - Creato e censito in `intro_fields` il nuovo campo `field-species` (`type: "select"`) con **21 specie canoniche** corredate da etichette estese e descrizioni di Lore (Licantropo, Demi-umano Kemonomimi, Umano, Vampiro, Elfo, Demone, Fata, Angelo, Drago, Orco/Oni, Succube, Minotauro, Tritone, Kitsune, Shifter, Non-Morto, Lamia, Arachne, Macchina, Mutante, Divinità/Primordiale).
  - Configurato il binding deterministico con memorizzazione istantanea delle variabili `player_species` e `species_label`.
  - Convertita la pagina `p_species_select` a `type: "select"` collegata a `field_id: "field-species"`.
- **Risoluzione Preventiva Step 11 (`field-occupation`):**
  - Applicata la medesima architettura alla schermata della carriera RPG: creato il campo `field-occupation` (`type: "select"`) con i 10 ruoli e specializzazioni operative canoniche di Svartúlfr (Vanguard, Striker, Combat Medic, Arcane Spellcaster, Infiltrator, Runecore Engineer, Alchemist, Info-Broker, Fixer, Academic Scholar), con salvataggio delle variabili `player_occupation` e `occupation_label`.
  - Convertita la pagina `p_occupation_select` a `type: "select"` con aggancio a `field_id: "field-occupation"`.
- **Persistenza & Sincronizzazione:** Aggiornato il World via API (HTTP 200) e risincronizzato il master export in `exports/Svartulfr_Export.json`.

---

## [Sessioni Precedenti — Settembre/Ottobre 2026] — Fondamenta, RPG Systems & Unchained Policy

### Sistema World Clock & Timeline

- Fissata World-Age 0 al 21 Dicembre 827 d.C., ore 00:00 UTC.
- Anno corrente canonico del World: **2024** (World-Age di riferimento: 10.486.470 ore).
- Risolte incongruenze anagrafiche per le generazioni dei Douglas e allineamento `start_timeline_position` con `birthdate`.

### Sistemi RPG e Bilanciamento

- Budget statistico: 25 punti allocabili (totale 31 con base 1 su tutte le 6 stat: MGT, RES, AGI, WIT, PRS, SCT).
- Livello RPG ancorato all'età anagrafica (con hard-cap tassativo a 99 per prevenire bug di salvataggio Wyvern su ultracentenari).
- Riattivazione selettiva delle feature World: inventory, currency, rpg_stats, combat, relationships attive; Creature Catcher e Cross-World Ships disattivati.

### Disciplina Tipografica & Policy Unchained

- Applicazione ferrea dello standard JED+ su tutte le schede personaggio native e linked.
- Bando dell'em-dash (`—`), dialogo sempre tra virgolette inglesi doppie standard (`"..."`), narrazione in testo piano senza asterischi.
- Sblocco Unchained: rimozione di ogni censura artificiale su dinamiche adulte, chimica romantica, istinti LSE e combattimento crudo, nel pieno rispetto delle linee rosse Wyvern (Tolleranza Zero su minori reali, divieto bestialità reale, no NSFL).
