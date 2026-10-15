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
├── FINAL/                      # Deliverable pronti all'import (vedi §3)
│   ├── Svartulfr_Lorebook_I.json / _II.json / _III.json   # 6 Lorebook (Lexicon)
│   ├── Svartulfr_Location.json
│   ├── Svartulfr_NPC_Primary.json
│   ├── Svartulfr_NPC_Secondary.json
│   ├── Erik_Douglas_card.json                     # 5 Character Card V2 (Main Cast)
│   ├── Logan_Douglas_card.json
│   ├── Jasper_Douglas_Bloodmoon_card.json
│   ├── Malachia_Douglas_Bloodmoon_card.json
│   └── Noah_Douglas_Bloodmoon_card.json
│
├── logs/                       # Log di sessione
│   └── chat/                   # Trascrizioni chat + backup/
│
├── lorebooks/                  # Pipeline di ottimizzazione Lorebook
│   ├── source/                 # 5 export grezzi di partenza (WyvernChat)
│   ├── optimized/              # 5 output puliti della Fase 1
│   └── standalone/             # Lorebook stand-alone (es. Cocketeers.json)
│
├── scripts/                    # Script e automazioni di progetto (Python/JS)
│   ├── optimize_lorebooks.py   # Ottimizzatore non-distruttivo dei Lorebook
│   └── generate_main_cast_cards.py # Genera le 5 Character Card V2 in FINAL/
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
3. [03. Outfits, Accessori e Coerenza Visiva](.agents/rules/03_outfits_e_coerenza_visiva.md) — Evitare tratti "sempre visibili", usare il sistema nativo di 5 outfit Wyvern.
4. [04. World Clock e Gestione Timeline](.agents/rules/04_world_clock_e_timeline.md) — Epoca 21/12/827 d.C., Anno 2024, World-Age di riferimento.
5. [05. Precedenza di Lore e Gestione Discrepanze](.agents/rules/05_precedenza_lore_e_discrepanze.md) — Precedenza per dominio territoriale (Underworld, SUCC, Blackwood, DDM).
6. [06. Invecchiamento, Longevità e Filone SciFi](.agents/rules/06_invecchiamento_e_longevita.md) — Founding, Firstborn millenari, Pureblood (200-400 anni), Common (60-80 anni).
7. [07. Gestione Contenuti, Policy Wyvern e Piena Libertà Espressiva (Unchained)](.agents/rules/07_epurazione_user_e_intimacy_profiles.md) — Libertà espressiva Explicit vincolata solo alla policy ufficiale Wyvern.
8. [08. Triage Import Lorebook ed Architettura Lexicon World](.agents/rules/08_triage_lorebook_e_lexicon.md) — Personaggi vivi con Start Position, deceduti con End Position; confinamento Global Character.
9. [09. RPG Stats e Sistemi di Simulazione](.agents/rules/09_rpg_stats_e_simulation.md) — Modulo RPG Stats; tetto livello a 99 per evitare bug.
10. [10. Pipeline Standard delle Card e Configurazione Attitudes](.agents/rules/10_pipeline_standard_e_attitudes.md) — Sequenza obbligatoria per la redazione di schede.
11. [11. Wyvern Web API: Protocolli di Sicurezza e Risoluzione Bug](.agents/rules/11_wyvern_api_sicurezza_e_bug.md) — Snapshot preventivo, body parziale per PUT, verifica post-scrittura.
12. [12. Lavoro in Locale su Database SQLite Wyldfire (Sospeso)](.agents/rules/12_lavoro_locale_sqlite_wyldfire.md) — Protocollo di sicurezza e backup numerati.
13. [13. Standard Operativo Chat di Gruppo Stand-Alone (/mine)](.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md) — Schema `/mine` 1.000-1.500 token, disaccoppiamento StoryEngine.
14. [14. Standard Operativo di Sessione e Skill Integrate](.agents/rules/14_metodo_operativo_skills_integrate.md) — Pianificazione, allineamento interattivo, ispezione, verifica.

### Riferimenti Ufficiali WyvernWiki per Funzionalità Avanzate e Soluzioni Complesse

Consultare tassativamente queste risorse ufficiali per l'implementazione di logiche complesse, scripting, templating e formattazione:

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

## 3. Pipeline dei Lorebook e Cartella FINAL

Il ciclo di vita dei Lorebook Wyvern segue questi stadi:

1. **Sorgenti grezze** — i 5 export originali di WyvernChat risiedono in [lorebooks/source/](lorebooks/source/):
   `Svartulfr_Lorebook_I.json`, `_II`, `_III`, `Svartulfr_Location.json`, `Svartulfr_NPC_Primary.json`.
2. **Ottimizzazione (Fase 1)** — [scripts/optimize_lorebooks.py](scripts/optimize_lorebooks.py) produce le versioni pulite in [lorebooks/optimized/](lorebooks/optimized/) **senza mai modificare gli originali**. Interventi applicati:
   - Congelamento (`disable: true`) delle schede segnaposto/vuote;
   - Congelamento delle voci intruse del setting Digitalis / Cuttings / Jun (per uid verificato);
   - Rimozione delle keyword "ombrello" (`solarton`, `succ`, `blackwood`, `losangeles`, `underworld`) solo dalle schede NPC;
   - Rimozione del blocco ripetuto `[INSTRUCTIONS: Format discipline ...]`;
   - Priority di sicurezza `0 → 10`.
   ```powershell
   python scripts/optimize_lorebooks.py
   ```
3. **Consegna** — [FINAL/](FINAL/) contiene i 6 Lorebook finali pronti all'import (copia conforme degli ottimizzati).
4. **Conversione in formato Lexicon + estrazione NPC** — [scripts/convert_to_lexicon.py](scripts/convert_to_lexicon.py) converte i 6 file di [FINAL/](FINAL/) dal formato `entries` (SillyTavern) al formato **Lexicon** (oggetto lorebook con array `lexicon`, struttura nativa del sito/API) e sposta tutte le voci `type: npc` dai Lorebook I/II/III nel nuovo `Svartulfr_NPC_Secondary.json`, rimuovendole dalle origini. `NPC_Primary` resta invariato.
   ```powershell
   python scripts/convert_to_lexicon.py
   ```

### Character Card V2 (Main Cast)

Le schede dei 5 personaggi principali (Erik, Logan, Jasper, Malachia, Noah) sono generate da [scripts/generate_main_cast_cards.py](scripts/generate_main_cast_cards.py) nel formato **V2 Character Card** (`spec: chara_card_v2`, lo stesso che Wyvern esporta come PNG) e salvate in [FINAL/](FINAL/).

Fonte dati: l'export live del World ([exports/Svartulfr_Export.json](exports/Svartulfr_Export.json) → `world_characters`), arricchito con gli scenari/first_mes/system_prompt autoriali. Regole applicate: tag canonici World, `mes_example` costruito dagli `speech_examples`, nessun Lorebook collegato, outfits inclusi con la correzione dell'anomalia `{{user}}` → nome personaggio.

```powershell
python scripts/generate_main_cast_cards.py
```

### Gestione, Sincronizzazione e Generazione dei Lorebook (World)

La sincronizzazione autorevole del World avviene via Web API Wyvern e produce l'export master [exports/Svartulfr_Export.json](exports/Svartulfr_Export.json), da cui derivano l'Export Master, le partizioni e la documentazione del World ([scripts/archive_obsolete_sources.py](scripts/archive_obsolete_sources.py), [scripts/convert_to_lorebook.py](scripts/convert_to_lorebook.py)).

### Statistiche del World (riferimento, sincronizzazione web)

- **World ID:** `_CgYT8fHXpDC4crjmegQF7`
- **Anno Corrente:** 2024 (World-Age 0 = 21 dicembre 827 d.C.)
- Le statistiche puntuali (personaggi, lexicon, location, environment, scenari, mappe, ere) sono quelle riportate in [docs/world/Svartulfr_World_Doc.md](docs/world/Svartulfr_World_Doc.md), generato dalla sincronizzazione live.

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
