# Svartúlfr Verse — Blackwood-Douglas (Wyvern & Modern Fantasy)

Benvenuti nel repository ufficiale di **Svartúlfr Verse** (ambientazione *Blackwood-Douglas / Modern Fantasy*). Questo progetto racchiude l'intera architettura narrativa, le schede personaggio in formato standard JED+, le voci di Lexicon, le definizioni ambientali e le esportazioni per la piattaforma **Wyvern** e per motori di simulazione/roleplay compatibili.

---

## 1. Mappa Strutturale del Repository

```
d:\SvartulfrVerse\
├── .agents/                    # Regole di Progetto per Agenti AI
│   └── rules/                  # 12 Direttive modulari (JED+, World Clock, API, ecc.)
├── AGENTS.md                   # Indice Rapido delle Regole Modulari
├── GEMINI.md                   # Protocollo Operativo Master Unificato
├── CanonDecisions.md           # Registro Decisioni di Canone e Discrepanze
├── README.md                   # Documentazione Generale del Repository (questo file)
├── .gitignore                  # Esclusioni per Git
│
├── docs/                       # Guide Ufficiali e Manualistica di Riferimento
│   ├── Guide_World.md          # Manuale WyvernChat World Creator Guide
│   ├── Svartulfr_World_Doc.md  # Documento Master compilato in prosa del World Svartúlfr
│   └── legacy/                 # Storico Claude, istruzioni superate e memorie
│       ├── Istruzioni_Progetto_v2.md
│       ├── Istruzioni_Workflow_Wyvern_Aggiornate_2026-09-14.md
│       ├── claude-legacy-project-memory-01a03cfa.md
│       └── claude_test_import.json
│
├── Wyvern/                     # Specifiche e Schede Attive per la Piattaforma Wyvern
│   ├── characters/             # Schede Main Cast per personaggio (card.json, world.json)
│   │   ├── Edric_Douglas/
│   │   ├── Erik_Douglas/
│   │   ├── Jasper_Douglas_Bloodmoon/
│   │   ├── Logan_Douglas/
│   │   ├── Malachia_Douglas_Bloodmoon/
│   │   ├── Noah_Douglas_Bloodmoon/
│   │   ├── Ut_Berg/
│   │   ├── Wulfnic_Bloodmoon/
│   │   └── Zefir_Hvitskog/
│   ├── lexicon/                # Voci di Lexicon categorizzate
│   │   └── by_folder/          # 9 file modulari (CHARS_DETAILS, HISTORY, SPECIES, etc.)
│   ├── environments.md         # Definizioni dei 6 macro-ambienti Wyvern
│   └── log_chat/               # Log e trascrizioni di sessioni di chat
│
├── exports/                    # Dati Esportati, Lorebook e Dump Database
│   ├── Svartulfr_Export.json   # Export master raw del World completo
│   ├── entities/               # Esportazioni suddivise per entità Wyvern (JSON)
│   │   ├── Svartulfr_Characters_Complete.json (+ Part1, Part2)
│   │   ├── Svartulfr_Lexicon.json (+ Part1, Part2)
│   │   ├── Svartulfr_Locations.json
│   │   ├── Svartulfr_Environments.json
│   │   └── Svartulfr_Scenarios.json
│   ├── lorebooks/              # Lorebook partizionati generati per SillyTavern/Wyvern
│   │   ├── Svartulfr_Lorebook.json
│   │   ├── Svartulfr_Lorebook_Complete.json
│   │   └── Svartulfr_Lorebook_Part1..3.json
│   └── raw_db_dumps/           # Dump SQLite estratti da Wyldfire (JSON)
│       ├── raw_characters.json
│       ├── raw_environments.json
│       ├── raw_lexicon.json
│       ├── raw_locations.json
│       └── raw_scenarios.json
│
├── scripts/                    # Script e Automazioni di Progetto
│   └── convert_to_lorebook.py  # Script Python per generare e partizionare i Lorebook
│
├── asset/                      # Media e Risorse Visive Organizzate
│   ├── portraits/              # Ritratti dei singoli personaggi (Erik, Logan, Jasper, ecc.)
│   ├── locations/              # Immagini di ambientazioni (Douglas Estate, Verve, ecc.)
│   ├── mappe/                  # Mappe territoriali (Blackwood, Solarton, SUCC, ecc.)
│   ├── banners/                # Banner e immagini di gruppo della famiglia Douglas
│   ├── lys_outfit/             # Schede visuali e varianti outfit di Lys
│   ├── av/                     # Avatar grafici
│   └── archivio/               # Asset grafici storici e versioni precedenti
│
├── Drafts/                     # Bozze di Lavoro, Versioni Precedenti e Sistemi di Lore
│   ├── Character_Cards_V1/     # Schede prima versione (Main Cast & NPC)
│   ├── Core_Docs/              # Documenti di design grezzi (Master_Design, World_Seed, etc.)
│   ├── Legacy_Lorebooks/       # Lorebook legacy (LSE, Underworld, SUCC, DDM)
│   ├── LSE/                    # Lupine Social Ecology (sistemi e meccaniche)
│   ├── Wyvern_Superseded/      # Materiale Wyvern deprecato
│   └── DDM.md                  # Dead Dog Motel crossover lore
│
├── drive/                      # Archivio Ingestione Drive e Fonti Originali
│   ├── Sources/                # 1.163 file HTML e metadati JSON di sessioni e fonti
│   └── ...                     # Trascrizioni testuali grezze
│
└── Wyldfire/                   # Applicazione Desktop SQLite Wyldfire (Sospeso per Regola 12 / §17)
```

---

## 2. Standard Operativi e Regole per Agenti AI

Tutti gli agenti AI e i collaboratori che operano in questo workspace devono seguire tassativamente le **12 Direttive Modulari** documentate in [GEMINI.md](file:///d:/SvartulfrVerse/GEMINI.md) e riassunte in [AGENTS.md](file:///d:/SvartulfrVerse/AGENTS.md):

1. [01. Formato di Consegna e Standard JED+](file:///d:/SvartulfrVerse/.agents/rules/01_formato_consegna_e_jed.md) — Testo pronto da incollare (non JSON complessi), struttura in 4 blocchi + chiusura tematica.
2. [02. Disciplina di Formattazione per Dialoghi ed Esempi](file:///d:/SvartulfrVerse/.agents/rules/02_disciplina_formattazione_dialoghi.md) — Virgolette inglesi doppie per il parlato, no asterischi per le azioni, no em-dash (`—`), divieto di markdown nei testi World.
3. [03. Outfits, Accessori e Coerenza Visiva](file:///d:/SvartulfrVerse/.agents/rules/03_outfits_e_coerenza_visiva.md) — Evitare tratti "sempre visibili", usare il sistema nativo di 5 outfit Wyvern.
4. [04. World Clock e Gestione Timeline](file:///d:/SvartulfrVerse/.agents/rules/04_world_clock_e_timeline.md) — Epoca 21/12/827 d.C., Anno 2024, World-Age 10486470 (5 aprile 2024).
5. [05. Precedenza di Lore e Gestione Discrepanze](file:///d:/SvartulfrVerse/.agents/rules/05_precedenza_lore_e_discrepanze.md) — Precedenza territoriale: Underworld (LA), SUCC (Solarton), Blackwood (Douglas), DDM (Voidspace).
6. [06. Invecchiamento, Longevità e Filone SciFi](file:///d:/SvartulfrVerse/.agents/rules/06_invecchiamento_e_longevita.md) — Founding (stop a 21 anni), Firstborn millenari, Pureblood (200-400 anni), Common (60-80 anni).
7. [07. Epurazione di {{user}} e Creazione Intimacy Profiles](file:///d:/SvartulfrVerse/.agents/rules/07_epurazione_user_e_intimacy_profiles.md) — 0 occorrenze di `{{user}}`, profili intimi confinati in entry Lexicon `memory` separate.
8. [08. Triage Import Lorebook ed Architettura Lexicon World](file:///d:/SvartulfrVerse/.agents/rules/08_triage_lorebook_e_lexicon.md) — Personaggi vivi con Start Position, deceduti con End Position; Global Characters = ON.
9. [09. RPG Stats e Sistemi di Simulazione](file:///d:/SvartulfrVerse/.agents/rules/09_rpg_stats_e_simulation.md) — Modulo RPG Stats in pausa a livello World; tetto livello fissato a 99 per evitare bug.
10. [10. Pipeline Standard delle Card e Configurazione Attitudes](file:///d:/SvartulfrVerse/.agents/rules/10_pipeline_standard_e_attitudes.md) — Sequenza obbligatoria in 13 step per la redazione di schede.
11. [11. Wyvern Web API: Protocolli di Sicurezza e Risoluzione Bug](file:///d:/SvartulfrVerse/.agents/rules/11_wyvern_api_sicurezza_e_bug.md) — Snapshot preventivo, body parziale per PUT, sostituzione array completi, verifica post-scrittura.
12. [12. Lavoro in Locale su Database SQLite Wyldfire (Sospeso)](file:///d:/SvartulfrVerse/.agents/rules/12_lavoro_locale_sqlite_wyldfire.md) — Protocollo di sicurezza e backup numerati (attivo solo su richiesta esplicita).

---

## 3. Gestione e Generazione dei Lorebook

Lo script [scripts/convert_to_lorebook.py](file:///d:/SvartulfrVerse/scripts/convert_to_lorebook.py) consente di processare l'export master [exports/Svartulfr_Export.json](file:///d:/SvartulfrVerse/exports/Svartulfr_Export.json) e generare:
- **Lorebook Unificati e Partizionati** in [exports/lorebooks/](file:///d:/SvartulfrVerse/exports/lorebooks/) (massimo 250 voci per parte per garantire compatibilità con l'import Wyvern).
- **Esportazioni Modulari per Entità** in [exports/entities/](file:///d:/SvartulfrVerse/exports/entities/) (Characters, Lexicon, Locations, Environments, Scenarios).
- **Dump Grezzi del Database** in [exports/raw_db_dumps/](file:///d:/SvartulfrVerse/exports/raw_db_dumps/).

Per eseguire la rigenerazione:
```powershell
python scripts/convert_to_lorebook.py
```

---

## 4. Media e Asset Grafici

Tutti i file multimediali sono categorizzati nella cartella [asset/](file:///d:/SvartulfrVerse/asset/):
- **`portraits/`**: Ritratti ufficiali dei personaggi con coerenza fisionomica di famiglia (Douglas look: capelli scuri, orecchie lupine singole Demi-Umani).
- **`locations/`**: Immagini di Villa Douglas, Dead Zone, Club The Verve, distretti industriali.
- **`mappe/`**: Cartografia di Blackwood City, Solarton, SUCC Campus, Hex Valley.
- **`banners/`**: Banner promozionali e composizioni di gruppo.
- **`lys_outfit/`**: Design e concept visivi per i diversi outfit di Alyssa.
