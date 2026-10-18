# Svartúlfr Verse — Blackwood-Douglas (Wyvern & Modern Fantasy)

Benvenuti nel repository ufficiale di **Svartúlfr Verse** (ambientazione _Blackwood-Douglas / Modern Fantasy_). Questo progetto racchiude l'intera architettura narrativa, le schede personaggio in formato standard JED+, le voci di Lexicon, le definizioni ambientali e le esportazioni per la piattaforma **Wyvern** e per motori di simulazione/roleplay compatibili.

---

## 1. Mappa Strutturale del Repository

```
e:\repository\SvartulfrVerse\
├── .agents/rules/              # 14 Direttive modulari per Agenti AI (01-14)
├── AGENTS.md                   # Indice Rapido delle Regole Modulari
├── GEMINI.md                   # Protocollo Operativo Master Unificato
├── CanonDecisions.md           # Registro Decisioni di Canone e Discrepanze
├── CHANGELOG.md                # Storico cronologico delle modifiche
├── README.md                   # Documentazione Generale del Repository (questo file)
├── SvartulfrVerse.code-workspace
├── .gitignore
│
├── ARCHIVIO/                   # Archivio storico (materiale superato o grezzo)
│   ├── 01_Drafts/              # Bozze, vecchie schede, materiali Drive, takeout, LSE
│   ├── 02_Drive_and_Raw_Sources/# Fonti grezze (Sources HTML/JSON, Modern Fantasy)
│   ├── 03_Claude_Docs_and_Memories/ # Project knowledge, conversazioni e memorie Claude
│   ├── 04_Wyvern_Local_Legacy/ # Materiale Wyvern locale deprecato
│   └── 05_Snapshots_and_Extractions/ # Snapshot, entity/lorebook/raw_db_dumps, backup
│
├── asset/                      # Media e Risorse Visive
│   ├── characters/             # Avatar e ritratti (main_cast, secondary_cast, ecc.)
│   ├── environments/           # Mappe e ambientazioni (Blackwood, SUCC, costa, ecc.)
│   └── lore_and_gods/          # Simboli, emblemi, banner
│
├── docs/                       # Documentazione e dati di lavoro
│   ├── data/                   # Dataset JED e raw (14_NPCs, Group A/B, Filtered, ecc.)
│   ├── guides/                 # Guide ufficiali (Guide_World.md)
│   ├── lexicon/                # Proposte Lexicon (DDM, Kinks, Magic, Monster)
│   ├── proposals/              # Proposte schede (Alyssa, Douglas Family, Location)
│   └── world/                  # Svartulfr_World_Doc.md, Svartulfr_RPG_Config.md
│
├── exports/                    # Export live da Wyvern (World, Personas, Mine, Engine)
│   ├── Svartulfr_Export.json   # Export master del World (Web API Sync)
│   ├── User_Personas_Export.json
│   ├── Mine_Characters_Export.json / Mine_Lorebooks_Export.json
│   └── Story_Engines_Export.json
│
├── FINAL/                      # Deliverable pronti all'import e sincronizzati via API (vedi §3)
│   ├── Svartulfr_Master_Scenario.json             # Master Character Scenario (13 slot, 29 greetings)
│   ├── PROMPT_OVERRIDES_WYVERN.md                 # I 4 Prompt Overrides ufficiali Wyvern
│   ├── Svartulfr_Lorebook_I.json                  # Lorebook I (221 entries)
│   ├── Svartulfr_Lorebook_II.json                 # Lorebook II (139 entries)
│   ├── Svartulfr_Lorebook_III.json                # Lorebook III (35 entries)
│   ├── Svartulfr_Location.json                    # Location (188 entries)
│   ├── Svartulfr_NPC_Primary.json                 # NPC Primary (99 entries)
│   ├── Svartulfr_NPC_Secondary.json               # NPC Secondary (111 entries)
│   ├── *_card.json                                # 14 Character Cards canoniche (/mine)
│   └── personas/                                  # 3 User Personas (Alyssa, Jasper, Echo)
│
├── logs/                       # Log di sessione
│   └── chat/                   # Trascrizioni chat + backup/
│
├── lorebooks/                  # Pipeline di ottimizzazione Lorebook
│   ├── source/                 # 5 export grezzi di partenza (WyvernChat)
│   ├── optimized/              # 6 Lorebook ottimizzati sincronizzati con FINAL/ (793 entries)
│   └── standalone/             # Lorebook stand-alone (es. Cocketeers.json)
│
├── scripts/                    # Script e automazioni di progetto (Python/JS)
│   ├── optimize_lorebooks.py   # Ottimizzatore non-distruttivo dei Lorebook
│   ├── generate_main_cast_cards.py # Genera le Character Card V2 in FINAL/
│   └── genericize_alyssa.py    # Script storico di conversione placeholder
│
└── scratch/                    # Area di lavoro temporanea (script e dump ad-hoc)
    ├── inbox/                  # File sciolti pre-esistenti (ex-root)
    └── scraping/               # Input scraping JanitorAI (link, batch)
```

---

## 2. Standard Operativi e Regole per Agenti AI

Tutti gli agenti AI e i collaboratori che operano in questo workspace devono seguire tassativamente le **14 Direttive Modulari** documentate in [GEMINI.md](GEMINI.md) e riassunte in [AGENTS.md](AGENTS.md):

1. [01. Formato di Consegna e Standard JED+](.agents/rules/01_formato_consegna_e_jed.md) — Testo pronto da incollare (non JSON complessi), struttura in 4 blocchi + chiusura tematica.
2. [02. Disciplina di Formattazione per Dialoghi ed Esempi](.agents/rules/02_disciplina_formattazione_dialoghi.md) — Virgolette inglesi doppie per il parlato, no asterischi per le azioni, no em-dash (`—`), divieto di markdown nei testi World.
3. [03. Outfits, Accessori e Coerenza Visiva](.agents/rules/03_outfits_e_coerenza_visiva.md) — Evitare tratti "sempre visibili", standard minimo 9 outfit contestuali Wyvern.
4. [04. World Clock e Gestione Timeline](.agents/rules/04_world_clock_e_timeline.md) — Epoca 21/12/827 d.C., Anno 2024–2025 (Freshman Year alla SUCC).
5. [05. Precedenza di Lore e Gestione Discrepanze](.agents/rules/05_precedenza_lore_e_discrepanze.md) — Precedenza per dominio territoriale (Underworld, SUCC, Blackwood, DDM).
6. [06. Invecchiamento, Longevità e Filone SciFi](.agents/rules/06_invecchiamento_e_longevita.md) — Founding, Firstborn millenari, Pureblood (200-400 anni), Common (60-80 anni).
7. [07. Gestione Contenuti, Policy Wyvern e Piena Libertà Espressiva (Unchained)](.agents/rules/07_epurazione_user_e_intimacy_profiles.md) — Libertà espressiva Explicit vincolata solo alla policy ufficiale Wyvern.
8. [08. Triage Import Lorebook ed Architettura Lexicon World](.agents/rules/08_triage_lorebook_e_lexicon.md) — 6 Lorebook Standalone (793 entries), zero `BROAD_KEYS`, regex avatar NPC obbligatoria.
9. [09. RPG Stats e Sistemi di Simulazione](.agents/rules/09_rpg_stats_e_simulation.md) — Statistiche Finali a 7 attributi (`STR/PER/END/CHA/INT/AGI/LCK`); tetto livello a 99.
10. [10. Pipeline Standard delle Card e Configurazione Attitudes](.agents/rules/10_pipeline_standard_e_attitudes.md) — Sequenza obbligatoria per la redazione di schede.
11. [11. Wyvern Web API: Protocolli di Sicurezza e Risoluzione Bug](.agents/rules/11_wyvern_api_sicurezza_e_bug.md) — Snapshot preventivo, body parziale per PUT, verifica post-scrittura.
12. [12. Lavoro in Locale su Database SQLite Wyldfire (Sospeso)](.agents/rules/12_lavoro_locale_sqlite_wyldfire.md) — Protocollo di sicurezza e backup numerati.
13. [13. Standard Operativo Character Scenarios & Architettura Unificata](.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md) — Scenario Unico Multi-Greeting (`char_scenario_1DC43ggb6mB8YLJDJKrU4`), 13 slot, 14 card `/mine`, 29 aperture cronologiche.
14. [14. Standard Operativo di Sessione e Skill Integrate](.agents/rules/14_metodo_operativo_skills_integrate.md) — Pianificazione, allineamento interattivo, ispezione, verifica.

### Riferimenti Ufficiali WyvernWiki per Funzionalità Avanzate e Soluzioni Complesse

Consultare tassativamente queste risorse ufficiali per l'implementazione di logiche complesse, scripting, templating e formattazione:

- **Character Scenarios**: [Features/Character-Scenarios](https://wiki.wyvern.chat/en/Features/Character-Scenarios)
- **World & Architecture Hub**: [Features/Worlds](https://wiki.wyvern.chat/Features/Worlds)
- **Advanced Lexicon (Categorize Entries & Register NPCs)**: [Advanced/Lexicon](https://wiki.wyvern.chat/en/Advanced/Lexicon)
- **Pronoun Pruned Prose (PPP) Character Guide**: [Guides/PPP-Character-Format](https://wiki.wyvern.chat/en/Guides/PPP-Character-Format) e [Features/Worlds/Characters](https://wiki.wyvern.chat/en/Features/Worlds/Characters)
- **Handlebars nei World**: [Features/Worlds/handlebars](https://wiki.wyvern.chat/en/Features/Worlds/handlebars)
- **Advanced Handlebars**: [Advanced/Handlebars](https://wiki.wyvern.chat/en/Advanced/Handlebars)
- **Lua nei World**: [Features/Worlds/Lua](https://wiki.wyvern.chat/en/Features/Worlds/Lua)
- **Advanced Lua**: [Advanced/Lua](https://wiki.wyvern.chat/en/Advanced/Lua)
- **Story Engine Lua-Handlebars**: [Features/StoryEngine/Lua-Handlebars](https://wiki.wyvern.chat/en/Features/StoryEngine/Lua-Handlebars)
- **Inline Chat Commands**: [Features/Worlds/Inline-Chat-Commands](https://wiki.wyvern.chat/en/Features/Worlds/Inline-Chat-Commands)
- **Boosts & Supporter Shoutouts**: [Features/Worlds/boosts-supporter-shoutouts](https://wiki.wyvern.chat/en/Features/Worlds/boosts-supporter-shoutouts)
- **How to Chat Guide**: [Guides/How-to-Chat](https://wiki.wyvern.chat/en/Guides/How-to-Chat)
- **Prohibited Content Guide (Safety & Content Policy)**: [Policies/Prohibited-Content-Guide](https://wiki.wyvern.chat/en/Policies/Prohibited-Content-Guide)

---

## 3. Architettura Character Scenarios, 6 Lorebook e Cartella FINAL

Con la migrazione definitiva dal modulo World ai **Character Scenarios**, la cartella [FINAL/](FINAL/) costituisce la Single Source of Truth sincronizzata bidirezionalmente con le API di Wyvern:

1. **Master Character Scenario (`FINAL/Svartulfr_Master_Scenario.json` — ID `char_scenario_1DC43ggb6mB8YLJDJKrU4`)**:
   - Riunisce in un unico scenario i **13 slot funzionali** (coperti dalle 14 Character Card in `/mine`, con pool bilanciato su `twin` per Jasper e Alyssa) e **29 Greetings cronologiche** (`01.`–`29.`, da giugno 2024 a giugno 2025) interamente redatte in italiano, con supporto nativo multi-messaggio (`messages[]`) e attivazione regex degli NPC.
2. **I 6 Lorebook Standalone (`FINAL/` e `lorebooks/optimized/` — 793 voci attive totali, 0 disattivate)**:
   - `_gwwCxCfQ6PQaLEjAQVpJL` — `Svartulfr_Lorebook_I.json` (221 entries: Ecologia LSE, Rune, Casate, Nove Firstborn e Lore primaria).
   - `_HfG7TeV6MJyj6bxMwxkpt` — `Svartulfr_Lorebook_II.json` (139 entries: Bacheca Contratti, Economia, Oggetti, DDM Voidspace).
   - `_9zWTGqYJNJ4BCDMj8gfcD` — `Svartulfr_Lorebook_III.json` (35 entries: Campus SUCC, CUMS, Confraternite, Sport, Underworld).
   - `_EjXxkmPVhpCXg8xABpFkK` — `Svartulfr_Location.json` (188 entries: Location strutturate).
   - `_zwEqgEEzh12X6gHVmMKKC` — `Svartulfr_NPC_Primary.json` (99 entries: NPC primari, World Dossier sintetici del cast fisso e memorie intime).
   - `_Uht3Ckz44JBDrPnUHq7LV` — `Svartulfr_NPC_Secondary.json` (111 entries: NPC secondari e terziari con Statistiche Finali a 7 attributi).
   - *Nota su `Alyssa` vs `{{user}}`*: Nelle voci di Lorebook e nelle sezioni di lore familiare delle schede, la gemella Omega è sempre indicata col suo nome canonico **Alyssa Hvit Douglas Bloodmoon** (zero macro `{{user}}` o `{{pronoun...}}` nei Lorebook), così da garantire piena coerenza sia quando il giocatore interpreta Alyssa (`[FemPOV]`) sia quando interpreta Jasper (`[MalePOV]`).
3. **Le 14 Character Card Canoniche in `/mine` (`FINAL/*_card.json`)**:
   - `Alyssa_Douglas_Bloodmoon_card.json` (`_6exg3yPfe2eCDK4hTftkh`, 19 outfits)
   - `Edric_Douglas_card.json` (`_TbRM3EdxDjHFgqztTbCpL`, 9 outfits, rating `mature`)
   - `Erik_Douglas_card.json` (`_QPea6g4Q1QfeYCVHCLMPR`, 10 outfits)
   - `Jared_Thompson_card.json` (`_xJVPtBLL3dxy69RLKL9X9`, 11 outfits)
   - `Jasper_Douglas_Bloodmoon_card.json` (`_t4J9aQNJM36cUKAP4wB4U`, 11 outfits, Beta Technomancer)
   - `Logan_Douglas_card.json` (`_T8Ywcr9FEqNf9JxbK6eHP`, 10 outfits)
   - `Mackenzie_Sanchez_Rogers_card.json` (`_zn24784jfcchQ7EwCyAnm`, 11 outfits)
   - `Malachia_Douglas_Bloodmoon_card.json` (`_RDfz7XzTpM23LpPALVXHM`, 11 outfits)
   - `Noah_Douglas_Bloodmoon_card.json` (`_zFLUjV8aVxQRAfQxGcAcY`, 9 outfits, Delta Strategist)
   - `Russ_card.json` (`_wn6DkCcg3Xqa2Xpx9ttnT`, 9 outfits, 21yo Demihuman Tiger & Five Cocketeers)
   - `Scarlett_Rose_card.json` (`_qXgBMbFYJfc84hbLHhe92`, 9 outfits)
   - `Sierra_Cruz_card.json` (`_pnrXbkWqcgmFAf3meRWFY`, 9 outfits, 18yo Lamia / Applied Necromancy)
   - `Stan_Davies_Jr_card.json` (`_Xd3NhKnRJByMTtdb6PjxJ`, 9 outfits, 21yo Werewolf Alpha)
   - `Wulfnic_Bloodmoon_card.json` (`_HEQQbbRFwKdG8QE2Fh1z1`, 12 outfits)
4. **Le 3 User Personas (`FINAL/personas/`)**:
   - `Alyssa_Persona.json` (`persona_1786335754946`, 19 outfits)
   - `Jasper_Persona.json` (`1792155173728`, 11 outfits)
   - `Echo_Persona.json` (`1791389790053`, 4 outfits)

---

## 4. Media e Asset Grafici

Tutti i file multimediali sono categorizzati nella cartella [asset/](asset/):

- **`characters/main_cast/`**: ritratti ufficiali del Main Cast (Alyssa, Erik, Jasper, Logan, Malachia, Noah, Ut, Wulfnic, Zefir).
- **`characters/secondary_cast/`**: ritratti del cast secondario e NPC.
- **`characters/avatars_legacy/`** e **`characters/group_shots/`**: avatar storici e composizioni di gruppo.
- **`environments/`**: cartografia e scenari (Blackwood, Solarton/SUCC, costa, Douglas Estate, The Verve).
- **`lore_and_gods/`**: emblemi, simboli e banner.

---

## 5. Manutenzione

- Lo storico di ogni modifica va registrato in [CHANGELOG.md](CHANGELOG.md).
- Le decisioni di canone e le risoluzioni di discrepanza vanno annotate in [CanonDecisions.md](CanonDecisions.md).
- I file di lavoro temporanei (script ad-hoc, dump, ispezioni) vanno tenuti in [scratch/](scratch/) e non nel root del repository.
