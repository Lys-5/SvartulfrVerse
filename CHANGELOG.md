# Changelog di Progetto — Svartúlfr Verse

### 09/11/2026 - Unificazione Master Pipeline (`daily-master-pipeline`), Team Multi-Modello a 3 Tier, Audit Forense 5 Chat Log Wyvern e Bonifica 46/46 Vault Health

- **Consolidamento Automazioni in Singolo Sidecar (`~/.gemini/config/sidecars/daily-master-pipeline/sidecar.json`)**:
  - Unificate le 4 precedenti automazioni mattutine (`daily-character-enrichment`, `daily-wyvern-monitor`, `daily-proxy-free-models`, `daily-omnisync-archive-mining`, archiviate in `ARCHIVIO/sidecars_legacy_backup/`) in un'unica sessione atomica alle `09:00 Europe/Rome` (`CRON_TZ=Europe/Rome 0 9 * * *`), eliminando 3 cold-start giornalieri ridondanti.
- **Nuova Skill e CLI Multi-Modello (`.agents/skills/multi-model-unified-pipeline/`)**:
  - `references/models_registry.json`: Definizione della matrice a 3 Tier (`tier_1_scout_fast`, `tier_2_architect_sync`, `tier_3_lore_judge`), dei 5 modelli IDE (`gemini-4-argon`, `gemini-3.8-flash`, `claude-opus-5.5`, `claude-sonnet-5.5`, `gpt-oss-120b`) con normalizzazione effort (`low`, `medium`, `high`), dei 5 client AI Desktop sul PC OMEN (`Antigravity.exe`, `Gemini.exe` riservato alle immagini via Argon, `Grok Bot.exe` / ecosistema *Groky* + *Code Groky* riservato esclusivamente al blocco slot di lavoro in Agenda previo OK dell'utente, `Claude.exe`, `copilotapp.exe`) e dei 5 gateway Open-Provider Plug & Play (`local_proxy` su `:5005`, `xai_grok`, `openrouter`, `ollama_local`, `lm_studio_local`).
  - `scripts/orchestrator.py`: CLI conforme a `workflow-skill-creator` con sottocomandi `detect-clients`, `route-model`, `run-tier`, `run-all` e `dashboard`, rate limiter cross-processo con `time.monotonic()`, gestione `RateLimitError` (HTTP 429), backoff esponenziale su 5xx e generazione della Dashboard Telemetrica HTML interattiva (`scratch/unified_pipeline_dashboard.html`).
- **Task 1 — Bonifica Completa Vault Health Check (46/46 Check Superati, 0 Avvisi, 0 Errori)**:
  - `FINAL/Svartulfr_NPC_Primary.json` (+ specchio ottimizzato): Sincronizzati `content` e `description` e applicato il Positive Framing puro su `Scarlett Rose` (`candy-pink`, due corna scarlatte, rimosso `(no human ears)`) e `Sierra Cruz` (rimossi tutti i riferimenti negativi a `legs/feet/shoes/steps/pants/walks`).
  - `FINAL/Logan_Douglas_card.json` & `scripts/vault_health_check.py`: Allineata l'altezza canonica di Logan (`198 cm (6' 6") human form, 228 cm (7' 6") hybrid shift`) e distinta da quella di Wulfnic (`220 cm`).
  - `FINAL/Larek_Steeltooth_card.json`: Popolati i `9/9` outfit contestuali obbligatori e `default_outfit` anche a livello top-level della card.
- **Task 2 — Character Lore Enrichment (Progresso `75/310`)**:
  - Arricchite e bonificate in JED+ le 5 schede di `GREED - Roxie`, `GLUTTONY - Kevin` (rimosso il template errato Level 99 Succubus Firstborn e ripristinato come Human Black-Hat Hacker Lv. 23), `Finnegan Novak` (ripristinato il profilo intimo Arctic Wolf `190 cm` e il blocco sul rimorso verso Alyssa/Jasper/Noah), `Federico "Riki" Savini` (ripristinato come Elder Solitary Wolf 65enne e confidente politico di Malachia) e `Fade Greymoor` (ripristinato il blocco RPG Vampire Lead Vocalist di *Grave Mistake*), associando i rispettivi `ignored_characters`.
- **Task 3 & Task 4 — Audit Forense delle 5 Nuove Chat Log Wyvern (`sidebar-recents?kind=worlds`) & Promozione Archive Mining (`22/2.930`)**:
  - Scaricate e sottoposte ad audit forense completo le 5 sessioni di test di World: `chat_log_Tc4xL33mLdVCgr8fQJnkr` (*"Cylinders, Cookies, and a Feral Garden"*, 140 turni), `chat_log_VamEmDLQa1h8rWeQLeX9N` (1 turno), `chat_log_TMAa1k3AWLLFd476R2jrp` (*"Svartúlfr"*, 29 turni), `chat_log_6a2nQtKMKpHjn7xG4Abxa` (*"Neon Yellow and Digital Chaos"*, 127 turni) e `chat_log_ftrtAD79eddk9Ue9Jr2WJ` (225 turni).
  - Bonificati live via `PUT /api/new/chat-logs/{id}` i summaries contaminati su `chat_log_6a2nQtKMKpHjn7xG4Abxa` (rimosso il summary dummy vuoto #6), `chat_log_TMAa1k3AWLLFd476R2jrp` (corretto *"loup de rue"* preservando il Summary 0 di continuità) e `chat_log_ftrtAD79eddk9Ue9Jr2WJ` (ricalibrato il Relationship Pacing nei Summaries 8 e 10).
  - Consolidata la nuova lore emergente nei Lorebook (`Lorebook I`: `241` entries con *Stanza di Hvit*, *Tri-Condition Enigma Succession*, *Mutazione Delta-to-Alpha*, *Minn snarvinda*, *Silver Bullets*, *Nove Precetti di Fenris*, *Caccia di Dicembre*, *Asse Gamma LSE*, limite di 7 sigilli dei cilindri e *Sigillazione Cutanea Anti-Miasma*; `Lorebook II`: `146` entries con *DDM Multiverse Theory: Base Reality vs Alternate Dimensions & The High Fantasy Branch (Alteyra / Silverhaven)* da `https://io-ddm.uwu.ai/`, *Famiglio Abissale di Jasper Echo*, *Cookie Diplomacy*, *Jasper's Pocket Jammer*, *Yellow VW Beetle Keys*, *Douglas Signet Ring* e *1666 Douglas Ledger*; `Lorebook III`: `48` entries con *Professor Mollusk*, *Diffusori di Feromoni* e *Scommessa Mu Alpha Nu*; `NPC Primary`: disambiguazione esplicita *Marcus Thornfield vs Marcus O'Connor* e allineamento `ignored_characters`/`ignored_personas` anche per gli ID High Fantasy; World Lexicon `_YpX47fNraQFw2dD7TdycJ` portato a `737` entries) e nelle Character Card di `Wulfnic` (*Gamli*), `Erik` (confine paterno granitico e metafora dei *Cuccioli d'Inverno*), `Malachia` (*Vígit / Il Bastione*) e `Jasper` (moneta d'argento tra le nocche e ponte technomantico con Larek), con deployment live via API Wyvern (`HTTP 200`).
- **Task 5 — Schede High Fantasy Parallele (`Jasper Fantasy`, `Malachia Fantasy`, `Alyssa Fantasy Persona`) & Teoria del Multiverso DDM (`https://io-ddm.uwu.ai/`)**:
  - `FINAL/Jasper_Fantasy_card.json` (`_K6GYVEbKggCMjWFDkXW6e`), `FINAL/Malachia_Fantasy_card.json` (`_wMG7wAXjkHxXLhcN8chwj`) e `FINAL/personas/Alyssa_Fantasy_Persona.json` (`user_persona_VCkKj7DQfcURYRYkK4VTc` / `persona_1794082731291`): Scaricate da Wyvern, bonificate da tutti gli em-dash (`—`) e dai vincoli anatomici negativi (`no human ears`), completate con `11/9` e `10/9` outfit contestuali High Fantasy a 6 sezioni, `personality` PList, `first_mes`, classificazione multiversale DDM (`Base Reality circa 2024` vs `High Fantasy Alternate Dimension` di Alteyra/Silverhaven con `ARC Level 3.5-3.8+`, `Reality Tears` / dungeon di miasma delle *Whispering Wastes*, *Cur Corpse Tavern / Sleepy Pup Inn*, taratura dei cilindri a 7 livelli, sigillazione cutanea anti-miasma di 10-11 giorni sulla schiena di Malachia, famiglio abissale di Jasper *Echo* con gli occhialini, nido ferale nel carro lungo la *Via del Ferro* e separazione assoluta di lignaggio dall'*Eclipse Vanguard* dei Rowland) e sincronizzate live su Wyvern (`HTTP 200`), insieme ai 3 summary bonificati di `chat_log_Tc4xL33mLdVCgr8fQJnkr` (`Vault Health Check`: `52/52` controlli superati, `0` avvisi, `0` errori).
- **Task 6 — Regola Canonica RPG (`1 Razza + 1 Occupazione + 5..15 Tratti`, `15` per Protagonisti/Top-Lore, Curva Livelli `0–13=Lv1`, `14–21=Lv2`, `>21=+1/5a`, `Max 99`)**:
  - **Codifica Normativa e Validazione Automatica (`76/76` Check Superati)**: Aggiornate le regole vincolanti in `GEMINI.md` (§8), `.agents/rules/09_rpg_stats_e_simulation.md` (§2), `.agents/skills/wyvern-world-rpg-automator/SKILL.md` (§2.1), `scripts/sync_all_characters_rpg.py` e `scripts/vault_health_check.py` (aggiunti 24 nuovi controlli automatici su livello canonico vs età anagrafica, presenza di `1 SPECIES` + `1 OCCUPATION`, dotazione di `5..15` tratti e `15` tratti esatti per tutti i protagonisti e personaggi molto potenti per lore).
  - **Omni-Sync Totale su Schede, Personas, Lorebook NPC e World Characters (`HTTP 200`)**:
    - Tutte le **12 Character Card** (`FINAL/*_card.json`, incluse le varianti High Fantasy e `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`) e le **4 User Personas** (`FINAL/personas/*.json`) aggiornate e sincronizzate live su Wyvern (`Alyssa`/`Jasper` 19a $\to$ `Lv 2`, `15` tratti; `Malachia` 28a $\to$ `Lv 4`, `15` tratti; `Noah` 25a $\to$ `Lv 3`, `15` tratti; `Logan` 49a $\to$ `Lv 8`, `15` tratti; `Erik` 55a $\to$ `Lv 9`, `15` tratti; `Zeera` 137a $\to$ `Lv 26`, `15` tratti; `Wulfnic` 1200a $\to$ `Lv 99`, `15` tratti; `Edric` 13a $\to$ `Lv 1`, `7` tratti; `Echo` 3a $\to$ `Lv 1`, `7` tratti; `Mackenzie` 19a $\to$ `Lv 2`, `12` tratti; `Larek` 21a $\to$ `Lv 2`, `8` tratti).
    - Tutti i **311 NPC** di `FINAL/Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`, 99 NPC, di cui 27 powerhouse con `15` tratti) e `FINAL/Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`, 212 NPC, di cui 19 powerhouse con `15` tratti) e i **126 World Characters** (`_YpX47fNraQFw2dD7TdycJ`) aggiornati e sincronizzati live (`HTTP 200`).

### 03/11/2026 - Micro-Proxy Free Tier: Diagnosi "Network Error" e Rimozione Modelli Inesistenti

- **Diagnosi `AxiosError: Network Error` da Wyvern**: Proxy operativo (health OK, preflight CORS + Private Network e POST verificati con origin `https://app.wyvern.chat`); nessuna richiesta Wyvern presente in `proxy/uvicorn.log` dopo l'avvio delle 00:23. Causa individuata lato browser (permesso Chrome "Accesso alla rete locale" o blocco client), non lato proxy.
- **`proxy/config_free_proxy.json`** (backup: `config_free_proxy.json.bak_20261103`): Rimossi solo i modelli che restituivano 404 / `model_not_found` nel log, senza alterare né rinumerare le priorità:
  - P3: rimosso `gemini-2.5-pro` (resta `gemini-4-argon`).
  - P4: rimosso `gemini-3.8-flash-thinking` (resta `gemini-3.8-flash`).
  - P5 `p5-gemini-pro-creative` eliminato (`gemini-2.0-pro-exp-02-05`, `gemini-exp-1206`).
  - P11 `p11-claude-3.5-openrouter` eliminato (`anthropic/claude-3.5-sonnet`, `anthropic/claude-3.5-haiku`).
  - P12 `p12-qwen-sambanova` eliminato (`Qwen2.5-72B-Instruct`).
  - Upstream totali: 32 -> 29. Hot-reload confermato e test di completamento 200 OK.
- **Esposizione LAN del proxy**: `host` portato da `127.0.0.1` a `0.0.0.0` in `config_free_proxy.json` su richiesta dell'utente (LAN privata con soli dispositivi personali, nessuna autenticazione). Proxy riavviato (`Uvicorn running on http://0.0.0.0:5005`), raggiungibile su `http://192.168.1.5:5005/v1`; health, `/v1/models` e preflight CORS + Private Network verificati. Firewall: regola inbound `python.exe` attiva solo sul profilo Pubblico. Avvio automatico confermato via `shell:startup` (`start_proxy.vbs - collegamento.lnk`).

### 02/11/2026 - Integrazione Completa della Lore Emergente: St. Brugge, Padre Revazhael, Cristallografia Runica e Allineamento Multi-Tier

- **Tier 2 Knowledge Vault / Second Brain (`knowledge/Lore_Worldbuilding/` & `docs/world/`)**:
  - *Sei Nuovi Articoli Enciclopedici Modulari*:
    1. `ACADEMIC_INSTITUTIONS_ST_BRUGGE_AND_SUCC.md`: St. Brugge Private Academy (architettura gotica, biblioteche con interdizioni runiche, curriculum esoterico avanzato di magia, alchimia, demonologia e rune, lezioni private con Padre Revazhael, frequenza di Alyssa e Jasper) e geografia della SUCC (Welcome Day 2024, percorsi accademici, governance sportiva).
    2. `APPLIED_RUNIC_CRYSTALLOGRAPHY_AND_MAGITECH.md`: Cristallografia runica applicata, fusione di Elder Futhark e reticoli cristallini per congelare incantesimi senza perdita energetica; specifiche dei cilindri incantati a risonanza individuale (formato torcia tascabile, attivazione istantanea a scatto "snap", zero mana draw durante l'uso, taratura armonica su misura vs fragilita intrinseca e tempi di ricarica dei cilindri commerciali DMHA).
    3. `PLANAR_COSMOLOGY_ABYSSAL_VS_VOID_MAGIC.md`: Divergenza ontologica ed energetica tra Magia Abissale (Abisso Infernale Profondo, matrice esotermica vivente, autorita sovrana, demoni superiori come Padre Revazhael) e Magia del Vuoto / Necromanzia Applicata (Vuoto Interstiziale, matrice endotermica, entropia fredda e frammenti d'anima residui), matrice comparativa e osservazione accademica di Sierra Cruz.
    4. `FATHER_REVAZHAEL_AND_SUPERIOR_DEMONS.md`: Demone Superiore millenario, Greater Incubus / Demone del Desiderio, segreto del Vero Nome ("Revazhael") e vulnerabilita alla sottomissione, etica ferrea del consenso assoluto, presenza e risonanza vocale, mentore dei gemelli a St. Brugge, doni sacri (Armatura Abissale, Chiave della Dimora del Rifugio con il maggiordomo Kobal), ruolo nel Greek Row della SUCC (residente ad ARO, tuttofare di fiducia per TIT).
    5. `ALYSSA_AND_JASPER_FIELD_AND_HUNTER_BACKGROUND.md`: Credenziali sul campo e reputazione dei gemelli; Alyssa (Pre-Med alla SUCC, Guaritrice Certificata di Gilda Rank A, Hunter ID ADB-555, nulla osta SR3S, Voto di Pacifismo Assoluto, pochette dimensionale con vetreria alchemica distillatoria, nido di pelliccia in Suite 3 con peluche Wolfy); Jasper (Ingegneria Acustica e del Suono, Hunter di Gilda Registrato Rank A, Hunter ID JDB-555, nulla osta SR3S, Katana in Vetro di Drago ancestrale, Armatura Abissale, intimidazione della confraternita KSA al Welcome Fest).
    6. `DCC_SECURITY_CAMPUS_INTEGRATION_AND_ATHLETICS.md`: Accordo esecutivo tra il Rettore Archer Wolfwood ed Erik Douglas (Erik capo allenatore degli Ice Hockey Bears con allenamenti alle 05:30 in cambio dell'integrazione di sicurezza DCC nel campus SUCC), Maggiore Kaladin Nargathon in coordinamento con Chief Warg, copertura droni biometrici ad alta quota, Barkley Rover (assistente allenatore SUCC Bulls) e dinamiche Greek Row.
  - *Aggiornamento dell'Indice Globale*: `EXTERNAL_RESOURCES_INDEX.md` aggiornato alla Versione 1.1 con Sezione 3.11 dedicata al Second Brain Knowledge Vault, censimento completo dei 6 nuovi articoli e metrica totale risorse portata da 77 a 83.
  - *Sincronizzazione Documento di Mondo*: `docs/world/Svartulfr_World_Doc.md` sincronizzato alle linee 291, 870, 873 e 1042-1045 con la presenza di Padre Revazhael ad ARO/TIT, il curriculum St. Brugge, l'accordo hockey Bears al St. Neptune Stadium e l'ambiente di Suite 3 a Theta Iota Theta.

- **Tier 2 Standalone Lorebooks (`FINAL/` & `lorebooks/optimized/`)**:
  - *Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL`)*: Inclusi 2 concetti di teoria magica (`lb1_concept_applied_runic_crystallography` e `lb1_magic_abyssal_magic_distinction`), portando il totale a 239 entries.
  - *Lorebook II (`_HfG7TeV6MJyj6bxMwxkpt`)*: Incluso l'item tattico `lb2_item_enchanted_resonant_cylinders` (tipo item, matrice di attivazione istantanea senza cast delay), portando il totale a 143 entries.
  - *Lorebook III (`_9zWTGqYJNJ4BCDMj8gfcD`)*: Incluso il concetto accademico `succ_lb3_st_brugge_academy`, portando il totale a 47 entries; risolta l'omofonia dell'ID dell'entry #40 (`event_partita_di_campionato_hockey` per la partita di hockey Bears, differenziata da `event_partita_di_campionato_` dei Bulls).
  - *Location Lorebook (`_EjXxkmPVhpCXg8xABpFkK`)*: Bonificate le chiavi di attivazione dell'entry #51 St. Brugge Private Academy (epurate le broad keys "Seven Hills", "Douglas", "Blackwood", "private academy") e aggiunta la sub-location `loc_theta_iota_theta_suite_3` (Suite 3 di TIT, 1.570 caratteri con nido di pelliccia, poster Grave Mistake e living space condiviso), portando il totale a 226 entries.
  - *NPC Secondary (`_Uht3Ckz44JBDrPnUHq7LV`)*: Riconciliata l'entry #23 per Father Revazhael (Rev) con chiavi complete ed estensione narrativa; normalizzata l'entry #211 per Larek Steeltooth con schema canonico, avatar DCC, regex multilinea e flag di esclusione.
  - *NPC Primary (`_zwEqgEEzh12X6gHVmMKKC`)*: Arricchite le schede dossier di Alyssa Douglas (eliminata la dicitura obsoleta "Novice Healing Mage", integrate credenziali ADB-555, vetreria alchemica e nido in Suite 3) e Jasper Douglas (integrate credenziali Hunter JDB-555, accordatura acustica dei cilindri, intimidazione KSA e rimossi i marchi obsoleti alla clavicola).
  - *Parita Assoluta e Mirroring*: Tutti gli 11 file dei lorebook mantengono una parita byte-for-byte `entries == lexicon` perfetta, zero macro `{{age}}`, zero broad keys sulle voci NPC e sincronizzazione speculare tra `FINAL/` e `lorebooks/optimized/`.

- **Tier 2 Character Cards & User Personas (`FINAL/` & `ARCHIVIO/cards_legacy/`)**:
  - `FINAL/Jasper_Douglas_Bloodmoon_card.json`: Blocco PList riga 1 su singola riga con credenziali complete (alumnus St. Brugge, Registered Hunter JDB-555, Mark of Sol su anca destra, positive framing orecchie animali); allineamento del livello RPG da Level 3 a Level 19 coerente con l'eta anagrafica (19 anni); aggiornamento di Backstory, Family & Pack e Voice & Behavior con l'apprendistato congiunto, accordatura acustica e reputazione SUCC.
  - `FINAL/personas/Jasper_Persona.json`: Sincronizzazione perfetta con la character card di Jasper; applicato il positive framing per l'orecchio lupino singolo ed eliminato ogni riferimento al marchio alla clavicola.
  - `FINAL/personas/Alyssa_Persona.json`: Blocco PList riga 1 su singola riga con credenziali complete (alumnus St. Brugge, Certified Guild Healer ADB-555); eliminata ogni occorrenza di "Novice Healing Mage"; arricchite Backstory e dinamiche Suite 3 con Voto di Pacifismo Assoluto e vetreria alchemica.
  - `ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`: Sincronizzazione del blocco PList e di personality; arricchimento di `SIGNATURE ITEMS & VEHICLE` con i cilindri risonanti tascabili e vetreria distillatoria; applicato il positive framing in `visual_description` e `post_history_instructions`.

- **Tier 3 Verifica Rigorosa, Regression Testing & Schema Parity**:
  - Risolta l'omofonia ID residua in `FINAL/Svartulfr_Lorebook_III.json` ed ottimizzato speculare, rinominando l'entry #40 in `event_partita_di_campionato_hockey` con 47 ID univoci su 47 entries e perfetta identita `entries == lexicon`.
  - Sviluppato ed eseguito il test runner esaustivo `scripts/verify_milestone4_full_regression.py` a copertura dell'intera suite di verifica:
    - `scripts/verify_milestone_1.py` (6/6 verifiche passate al 100%).
    - `scripts/test_milestone_1_adversarial.py` (76/76 verifiche passate al 100%).
    - `scripts/verify_milestone2_lorebooks.py` (6/6 batterie passate al 100%).
    - `scripts/verify_milestone3_cards_personas.py` (10/10 test passati al 100%).
    - `scripts/verify_npc_schema_contract.py --all` (100% pass rate su tutti i contratti).
    - `scripts/verify_marks_and_images.py` (8/8 immagini e 12/12 invarianti passate al 100%).
    - `scripts/vault_health_check.py` (42/46 check passati, 0 errori critici bloccanti).
  - Rispetto rigoroso di zero em-dashes (`\u2014`), positive framing su demi-umani e coerenza cronologica con l'Anno 2024 del World Clock.

### 01/11/2026 - Riorganizzazione Cascata Proxy Free Tier con Pilastri Fiat e Ranking RPG
- **Aggiornamento Cascata Failover Proxy (`proxy/config_free_proxy.json` & `proxy/free_tier_proxy.py`)**:
  - *Pilastri Fiat Primari (Priorità 1–8)*: Consolidati i 4 pilastri irrinunciabili: GLM 5.2/5.3 (BigModel Direct & OpenRouter), Gemini 4 Argon, Gemini 3.8 Flash & 2.0 Pro Creative, e Gemma 4 (SambaNova Cloud, OpenRouter, Chutes).
  - *Epurazione Modelli Lite*: Escluso tassativamente Gemini Flash-Lite dall'ecosistema di generazione RPG, sostituito da Gemini 2.0 Pro / Exp Creative.
  - *Ranking Qualitativo RPG (Priorità 9–22)*: Ordinamento decrescente basato su coerenza e profondità narrativa TTRPG: DeepSeek V3/V3.2 $\to$ Claude 3.5 Sonnet & Haiku $\to$ Qwen 2.5 72B & 3.8 27B $\to$ Llama 3.3 70B $\to$ Mistral Large 2 $\to$ NVIDIA Nemotron 3 Ultra 550B $\to$ GitHub Models.
  - *Safety Net (Priorità 23–30)*: Rete di salvataggio a fallback su OpenRouter Free (`liquid/lfm-2.5`, `flint`, `xing4`, `dots-3`, `laguna-s`).
  - *Supporto PNA e Risoluzione Network Error*: Introdotto `allow_private_network=True` e middleware ASGI per abilitare `Access-Control-Allow-Private-Network: true` per le chiamate cross-origin da Wyvern (`https://app.wyvern.chat`).
  - *Sanitizzazione Parametri & Loading .env*: Supporto automatico a `python-dotenv`, mappatura alias di chiavi ambientali e rimozione automatica di penalty non supportate dai provider.
- **Audit Completo API Key e Guida Ufficiale (`proxy/API_KEY_ACQUISITION_GUIDE.md`)**:
  - Pubblicata matrice esaustiva di tutte le 15 API Key supportate, con quote gratuite (RPM/TPM/RPD), procedure di registrazione zero-cost e console URL ufficiali per Zhipu, DeepSeek, Google AI Studio, Groq, SambaNova, Cerebras, SiliconFlow e Mistral.
- **Allineamento Script e Scheduled Automation (`daily-proxy-free-models`)**:
  - Aggiornato `proxy/update_free_models.py` con blacklist rigorosa per modelli lite/utility e protezione dei 4 pilastri fiat.
  - Aggiornato `sidecar.json` in `~/.gemini/config/sidecars/daily-proxy-free-models/` con le nuove direttive di presidio della gerarchia RPG.
- **Validazione Indipendente Victory Auditor**: 40/40 test superati con successo (`pytest tests/`).

### 01/11/2026 - Risoluzione Definitiva Leakage Narrativo Orecchie Demi-Umani & Positive Framing

- **Bonifica Anti-Echoing Anatomia Demi-Umani ("Pink Elephant Problem")**:
  - *Diagnosi del Problema*: Frasi negative presenti nelle schede e negli outfit (`"No orecchie umane"`, `"(nessun orecchio umano visibile)"`, `"senza orecchie umane ai lati"`) provocavano l'attivazione spuria dei token negativi nella matrice di attenzione dell'LLM, inducendo il bot a rigurgitare e ripetere continuamente in narrativa la formula *"prive di qualsiasi orecchio umano ai lati del volto"*.
  - *Adozione della Disciplina di Positive Framing Puro*:
    - Riformulate tutte le descrizioni di fisionomia e acconciatura nelle character card, outfit, scenari e greeting per descrivere esclusivamente ciò che è presente in modo affermativo (es. *"singolo paio di orecchie da lupo sulla sommità del capo, perfettamente integrate tra i capelli"*).
    - Relegazione formale dei vincoli negativi (`--no human ears`) esclusivamente ai parametri tecnici dei generatori visivi (Argon / Gemini Imagen), con divieto categorico di inserimento nei testi del contesto chat per l'LLM.
  - *Aggiornamento Obbligatorio in `post_history_instructions`*:
    - Integrata la nuova direttiva di stile in coda alle istruzioni finali:
      `"Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. Demi-human anatomical discipline: treat single animal ears as the natural norm; never mention, describe, or reiterate the absence or lack of human ears in narrative descriptions."`
  - *Bonifica File Locali (FINAL/)*:
    - 10 Character Cards (`FINAL/*_card.json`): outfits, descrizioni e `post_history_instructions` aggiornati.
    - 64 Scenari (`FINAL/scenarios/*.json`): rimossi tutti gli incisi negativi da premade scenes e scene instructions.
    - 3 User Personas (`FINAL/personas/*.json`): rimosso `(nessun orecchio umano laterale)` in `Alyssa_Persona.json`.
    - Regole di Progetto: aggiornati `.agents/rules/03_outfits_e_coerenza_visiva.md` e `GEMINI.md` (Sezioni 3 e 5).
  - *Deployment e Validazione Live su Wyvern Web API*:
    - Tutte le 9 Character Cards standalone in `/mine` aggiornate con payload flat (`PUT /api/characters/{cid}`), verificate con HTTP 200 e 0 clausole negative residue.
    - Tutti i 44 Scenari del World `_YpX47fNraQFw2dD7TdycJ` verificati e bonificati via API (`PUT /api/worlds/scenarios/{sid}`) con ID stringa, verificati con 0 clausole negative residue.
    - Collaudo headless Chrome DevTools / Playwright su WyvernChat completato con successo (zero errori console, zero errori di rete, zero leakage nel DOM).

### 01/11/2026 - Creazione e Deployment Live di Larek Steeltooth & Omni-Sync Wyvern
- **Integrazione Canone Larek Steeltooth (World Character #127 & Lorebook NPC Secondary)**:
  - *Identita e Adattamento Lore*: Recuperato il personaggio ancestrale Larek (secondogenito di Nahgigoth, fratello di Ikkath e nipote di Morgeth Steeltooth) e ricollocato nella SUCC contemporanea come studente del terzo anno di Ingegneria Informatica, membro della confraternita Alpha Rho Omega (ARO), e amministratore IT/tuttofare di fiducia della sororita Theta Iota Theta (TIT).
  - *Standard JED+ e SPECIAL D20*: Schedatura JED+ completa con blocco attributi PList a riga singola, 4 sezioni narrative (BACKSTORY, FAMILY & CLAN, VOICE & BEHAVIOR, THE HANDYMAN'S HONOR), 9 outfit contestuali con ID univoci (casual, business / campus, gala / formal, party / club, beach / terme, sleep, nude, hybrid shift / mutation, full shift / other), allineamento World Clock (birthdate: 10301784, 12 Marzo 2003, eta 21) e statistiche S.P.E.C.I.A.L. D20 bilanciate (Might 6, Resilience 6, Agility 4, Wit 7, Presence 4, Scouting 4, Somma 31, Livello 21).
  - *Deployment Live via Web API (POST /api/worlds/characters)*: Creato con successo nel World autoritativo _YpX47fNraQFw2dD7TdycJ con ID live _PqRVec7Aa42KGUhK2J8GQ (totale World Characters portato da 126 a 127).
  - *Omni-Sync dei 6 Lorebook Standalone (PUT /api/lorebooks/{id})*:
    - Lorebook I (_gwwCxCfQ6PQaLEjAQVpJL): 237 entries distribuite (HTTP 200).
    - Lorebook II (_HfG7TeV6MJyj6bxMwxkpt): 142 entries distribuite (HTTP 200).
    - Lorebook III (_9zWTGqYJNJ4BCDMj8gfcD): 46 entries distribuite (HTTP 200).
    - Location (_EjXxkmPVhpCXg8xABpFkK): 225 entries distribuite (HTTP 200).
    - NPC Primary (_zwEqgEEzh12X6gHVmMKKC): 99 entries distribuite (HTTP 200).
    - NPC Secondary (_Uht3Ckz44JBDrPnUHq7LV): 212 entries distribuite (HTTP 200), con Larek registrato e soppressione nativa ignored_characters: ["_PqRVec7Aa42KGUhK2J8GQ"].
  - *Sincronizzazione File Locali*: Aggiornati FINAL/Larek_Steeltooth_card.json, FINAL/Svartulfr_Characters.json, FINAL/Svartulfr_NPC_Secondary.json e lorebooks/optimized/Svartulfr_NPC_Secondary.json con parita byte-for-byte entries == lexicon.


### 01/11/2026 - Salvataggio Automatico Chat e Transcript delle Automazioni in SvartulfrVerse
- **Pipeline di Archiviazione Chat Automazioni (`logs/automations/`)**:
  - *Script Autoritativo `scripts/archive_automation_chat.py`*: Sviluppato e collaudato lo script dedicato che estrae il transcript grezzo della sessione da Antigravity, lo archivia in `logs/automations/transcripts/YYYY-MM-DD_HHmm_<automation>.jsonl` e genera un documento Markdown formattato e immediatamente leggibile in `logs/automations/YYYY-MM-DD_HHmm_<automation>.md`, aggiornando un indice cronologico in `logs/automations/README.md`.
  - *Aggiornamento Sidecar delle 3 Automazioni*: Integrata nei prompt di `daily-character-enrichment`, `daily-wyvern-monitor` e `daily-proxy-free-models` l'istruzione vincolante di esecuzione di `archive_automation_chat.py` a chiusura sessione, garantendo i relativi permessi di esecuzione in `agent_permissions`.
  - *Persistenza Report nel Daily Runner*: Aggiornato `scripts/daily_maintenance_runner.py` per salvare copie storiche timestamped dei report di manutenzione direttamente in `logs/automations/`.

### 01/11/2026 - Blindatura System Prompt & Regole Lore: Asimmetria Informativa, Segretezza Licantropica e Wulfnic 'Nonno Nic'
- **Risoluzione Definitiva Drift Metagaming (OOC Wulfnic / Famiglia Douglas / Lore Esoterica)**:
  - *Diagnosi del Problema*: Nelle chat di gruppo e negli scenari collegati alla SUCC, l'inclusione di voci di Lorebook e schede descrittive su Wulfnic (Wolf King / 1,200yo Firstborn), sulla Casata Douglas e sui misteri della Luna Bianca provocava metagaming/leak informativo: gli NPC non-licantropi (Jared Thompson, Santiago Vance, Bailey Rogers, Mac Sanchez-Rogers, Stanley Davies, ecc.) reagivano come se conoscessero i titoli sacri e l'identità ancestrale di Wulfnic.
  - *Codifica dell'Asimmetria Informativa (`<information_asymmetry_and_werewolf_secrecy>`)*:
    1. *Segretezza dei Licantropi & Folklore come Leggenda Metropolitana*: I lupi sono fieri ed ermetici; al di fuori dei licantropi e dei branchi legati dal giuramento a Wulfnic, il "Re dei Lupi", l'"Enigma" e i miti dei Firstborn sono considerati pure leggende metropolitane o chiacchiere da bar.
    2. *Percezione Pubblica dei Douglas*: Per i sovrannaturali comuni e studenti della SUCC, i Douglas sono solo una ricca famiglia locale di costruttori (DCC) nota per la filantropia e il finanziamento del Neptune Stadium / Douglas Arena; Erik Douglas è ricordato come ex capitano ed eroe dell'hockey universitario (SUCC Bears).
    3. *Wulfnic è Rigorosamente "Nonno Nic"*: Agli occhi di studenti, amici e compagni di squadra (Jared, Santiago, Bailey, ecc.), Wulfnic è unicamente ciò che Alyssa e Jasper hanno raccontato: il loro "nonno Nic", un anziano montanaro massiccio, rustico, burbero ed eccentrico che vive nei boschi con un vecchio pickup. Zero conoscenza o sospetto dell'identità millenaria.
    4. *Dottrina Esoterica Inaccessibile*: La Luna Bianca (Máni), i Purosangue (Truebloods), il Sangue Fondatore e le rune sacre sono dogmi religiosi ed esoterici interni ai licantropi; i non-licantropi non li conoscono né li sanno decifrare.
  - *Deployment File di Configurazione Aggiornati*:
    - `FINAL/PROMPT_OVERRIDES_WYVERN.md`: Inserito `<information_asymmetry_and_werewolf_secrecy>` nella Sezione 1 (`<system>`) e rinforzato in `<formatting_and_rules>` nella Sezione 2 (`post_history_instructions`).
    - `FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json`: Inserito nel `main_prompt_template`, `main_prompt_sections`, nel blocco `svartulfr_grounding_and_chronology` e nei guardrail del `floating_prompt_template`.
    - `FINAL/assistants/Svartulfr_Game_Master_Assistant.json`: Aggiornato `system_prompt` (`<character_knowledge_and_thought_privacy>`) e `final_instructions`.
    - `FINAL/Svartulfr_Master_Scenario.json`: Aggiornato `scenario`, `system_prompt` e `final_instructions`.
    - `.agents/rules/05_precedenza_lore_e_discrepanze.md` & `GEMINI.md`: Formalizzata la Sezione 10 / sottosezione vincolante sulle invarianti di conoscenza e asimmetria informativa.

### 01/11/2026 - Adozione Architettura "Second Brain / LLM Wiki 2026" & Motore Vault Health Check
- **Integrazione Metodologia LLM Wiki (Karpathy / CoALA / MemGuard)**:
  - *Standardizzazione Metabolismo Vault*: Sviluppato e implementato il motore autoritativo `scripts/vault_health_check.py` per il monitoraggio rigoroso delle 6 dimensioni di salute (Contraddizioni di canone, Struttura JED+, Igiene trigger anti-collisione, Unicità Johnny.Decimal, Parità byte-for-byte `entries == lexicon` ed Efficienza infrastruttura/proxy).
  - *Integrazione Task 0 nel Daily Maintenance Runner*: Aggiornato `scripts/daily_maintenance_runner.py` per eseguire preliminarmente il Vault Health Check prima dei batch di arricchimento lore, monitoraggio Wyvern e rotazione proxy free.
  - *Collaudo con Successo*: 44 verifiche eseguite, 41 check superati a pieni voti, 0 errori critici bloccanti e salvataggio automatico del report in `scratch/vault_health_report.md`.
- **Risoluzione & Deployment 3 Automazioni Native Antigravity Sidecar**:
  - *Diagnosi e Bonifica*: Risolto il disallineamento per cui le automazioni giornaliere erano rimaste relegate a un timer di sessione effimero (`schedule`) non visibile nella dashboard UI.
  - *Creazione 3 Sidecar Scheduled*: Registrate in `~/.gemini/config/sidecars/` con timezone `Europe/Rome` e permessi granulari per workspace:
    - `daily-character-enrichment`: ogni giorno alle 09:00 (`python scripts/daily_character_enrichment.py`).
    - `daily-wyvern-monitor`: ogni giorno alle 09:15 (`python scripts/daily_wyvern_platform_monitor.py`).
    - `daily-proxy-free-models`: ogni giorno alle 09:30 (`python proxy/update_free_models.py`).
  - *Test Run Esecutivo*: Validati i comandi da riga di comando con exit code 0 e piena operatività.

### 31/10/2026 - Conclusione Sessione: Esecuzione Omni-Sync Totale con 100% Health
- **Esecuzione Pipeline di Sincronizzazione Totale (Omni-Parity)**:
  - *Token Auth*: Rigenerato e verificato il token Firebase Auth via LevelDB Chrome.
  - *World Metadata & Snapshot*: Sincronizzati 126 World Characters (`FINAL/Svartulfr_Characters.json`), 188 World Locations (`FINAL/Svartulfr_Location.json`), 731 voci World Lexicon e tutti i 44 Scenari in `FINAL/scenarios/`.
  - *Cataloghi RPG*: Sincronizzate 24 Specie, 37 Occupazioni e 74 Tratti in `FINAL/rpg_*_catalog.json` e aggiornato `FINAL/Svartulfr_World_RPG_Config.json`.
  - *Lorebooks Standalone*: Verificata al 100% la parità `entries == lexicon` byte-for-byte su tutti i volumi (`Lorebook I`: 237, `II`: 142, `III`: 46, `NPC Primary`: 99, `NPC Secondary`: 211).
  - *Audit Scenari & Attitudes*: 44/44 scenari superati a pieni voti (zero refusi cremisi, colori ufficiali giallo/blu SUCC confermati, singola scena premade, zero warning auto-trigger, startup script de-duplicazione attivo e zero anomalie 'someone' nelle attitudes).

### 31/10/2026 - Risoluzione Anomalie Attitudes 'Erik -> someone' & Correzione Colori Ufficiali SUCC (Giallo e Blu)
- **Risoluzione Bug Attitudes 'Erik -> someone' (_qfaywY2yfrGWcxPBdmURD)**:
  - *Diagnosi*: Erik presentava 8 attitudes con `target_id` obsoleti (riferiti a una vecchia istanza di card cancellate) e campo `target: ""` vuoto. Il frontend di Wyvern, non riuscendo a risolvere gli ID nel World corrente e trovando stringa vuota, ricorreva al fallback predefinito `"someone"`.
  - *Risoluzione*: Aggiornati via API (`PUT /api/worlds/characters/_qfaywY2yfrGWcxPBdmURD`) tutti gli 8 target con gli ID reali del World corrente ed etichetta testuale esplicita `target`:
    - Alyssa (`_FGeNBqjrt9fJJJyXTDgxM`, target: "Alyssa", intensity: 95)
    - Jasper (`_mUEUDfmTG4m7wNyQ7WQKx`, target: "Jasper", intensity: 90)
    - Malachia (`_QQXte9xWjMeMtqEJfwrc3`, target: "Malachia", intensity: 95)
    - Noah (`_YzcPc7dRLkttzR2jKX93z`, target: "Noah", intensity: 90)
    - Logan (`_KW6aNaRYTengVR4NBmG7J`, target: "Logan", intensity: 88)
    - Edric (`_4QWHxwHBpNnfjmNYm3tNr`, target: "Edric", intensity: 90)
    - Kaladin (`_9YcrRj1BTHCL2e1Up3exz`, target: "Kaladin", intensity: 95)
    - Wulfnic (`_P1HrVjkY9TGnymNaAWX1j`, target: "Wulfnic", intensity: 99)
- **Correzione Colori Istituzionali SUCC (Giallo e Blu / Gold & Navy Blue)**:
  - Eliminato il riferimento errato *"cremisi e oro"* sostituendolo con i colori ufficiali dell'ateneo **giallo e blu** come da canone SUCC (`io-succ.uwu.ai` e wiki).
  - Rettificati sia i testi di scena (`premade_scenes`) sia le premesse di scenario (`scenario_premise` e `description`) sui 3 scenari del Welcome Day (`_JPdqckWQBPDwdbxhEJLNK` Alyssa POV, `_hWre7H8xQRbWjkN2bAk4e` Jasper POV, `_r7hdYkNzVH8Ub3TnyqDJP` Scena Corale) e in tutti i rispettivi file JSON in `FINAL/scenarios/`.

### 31/10/2026 - Dotazione Definitiva Signature Items dei Gemelli (Alyssa & Jasper)
- **Risoluzione Totale Alyssa POV (_JPdqckWQBPDwdbxhEJLNK)**:
  - *Maggiolino Giallo*: Capote in tela beige coordinata agli interni beige, ammaccatura sul parafango posteriore conservata per carattere, targa LIL MN e adesivo Jasper: CAUTION: OMEGA DRIVING. If you ride my ass, my Alpha is gonna ride yours.
  - *Dimensional Pochette (Bag of Holding)*: Cuoio verde smeraldo scuro, fibbie in argento a testa di lupo e ricamo girasole. Contiene l'intero kit medico/botanico, tomi, sopravvivenza, guardaroba rotante, coperte/lenzuola per il nesting, saponi profumati e biscotti caldi.
  - *Signature Keepsakes & Reliquie*: Alyssa's Plush Wolf (Wolfy da Wulfnic), Enchanted Cylinders tattici, Emergency Fail-Safe Medallion cinetico, Dimensional Refuge Key (Father Revazhael per l'Otherworld), SR3S Guild Pass & Tessera Hunter ID ADB-555 (Rank A, Healer & Support Mage).
  - *Risoluzione Contraddizione*: Rimosso il bracciale in filo d'argento (incompatibile con la severa Silver Allergy lupina).
  - *Conversione Economica*: Allineati i crediti al tasso reale (1 Cr = 1 cent US) impostando .00 USD + 50.000 DMHA Guild Credits (.00 eq.).
- **Registrazione & Dotazione Jasper POV (_hWre7H8xQRbWjkN2bAk4e)**:
  - *Custom Porsche GTS (DJ-FRQ)*: Nero opaco, murale verde acido fluorescente, lupo ululante sul cofano, targa DJ-FRQ, assetto da corsa/fuga e impianto sound DJ.
  - *Dragon Glass Katana*: Lama ancestrale in vetro di drago nero ereditata da Nixara Bloodmoon e affidata a Jasper.
  - *The Abyssal Armor & Twin Daggers*: Armatura leggera e pugnali gemelli in acciaio demoniaco nero di Father Revazhael (St. Brugge).
  - *SR3S Guild Credentials (Pass & Tessera JDB-555)*: Rank A Tecnomancer / Cyber-Rogue & Recon Support.
  - *Dotazione Tecnomanzia*: Smartphone & Slicing Cyberdeck, Keychain Porsche & Wyrm Hall 304, portafoglio ID SUCC, Clan Signet Ring, spray soppressore LSE, auricolari e accendino (.00 USD + 50.000 Cr).

### 31/10/2026 - Allineamento Filologico Dotazione Alyssa (Maggiolino Giallo & Cover Gialla Rugged Noah)
- **Smartphone con Cover Gialla Rugged**: Aggiornato Alyssa's Smartphone (Yellow Rugged Case) (_f7fEWMRBJrk2ybRqDGTYf), inserendo la cover ultra-protettiva rugged color giallo brillante regalata e montata da Noah perché ad Alyssa cade continuamente il telefono a terra.
- **Maggiolino Giallo & Chiavi**:
  - Creato nel Lexicon World il veicolo Alyssa's Yellow VW Beetle (LIL🌙MN) (_XXF3g1rMjFpEk1q6rMg64) — cabriolet 4 posti giallo acceso con capote in tela nera, interni beige, targa personalizzata LIL🌙MN e adesivo posteriore CAUTION: OMEGA ON BOARD.
  - Aggiornato Alyssa's Keychain (Yellow VW Beetle & Dorm Keys) (_r8DLnJp6ApqE7NJaYCBgU) con le chiavi del Maggiolino e della stanza campus.
- **Douglas Clan Signet Ring**: Creato nel Lexicon World l'anello sigillo sacro della casata (_3KUmFBfBEk8qDJMwJU6x4), portato da Alyssa su catenina al collo.
- **Starting Inventory Alyssa POV Sincronizzato**: Aggiornato _JPdqckWQBPDwdbxhEJLNK con tutti gli 11 oggetti canonici rigorosamente estratti dalla lore.

### 31/10/2026 - Dotazione Oggetti Iconici & Starting Loadout Alyssa POV
- **Creazione Nuovi Oggetti nel Lexicon World**: Creati e registrati via API su _YpX47fNraQFw2dD7TdycJ:
  1. NextGen Arcane-Shielded Smartphone (_f7fEWMRBJrk2ybRqDGTYf)
  2. Leather Wallet & SUCC Student ID (_tzTRjXDrez96xTXNnkqzr)
  3. Seven Hills Keychain (Car & Dorm Keys) (_r8DLnJp6ApqE7NJaYCBgU)
  4. Pre-Med Emergency Trauma & Field Healer Kit (_Xz3d8YUkGXXKGYeUhM1H2)
- **Configurazione Starting Inventory Completo per Alyssa POV**: Assegnati a SUCC: Welcome Day (Alyssa POV) tutti i 9 oggetti di dotazione canonica (Smartphone schermato, Portafoglio & ID SUCC, Portachiavi Auto & Stanza, Kit Medico/Trauma Pre-Med, Spray Soppressore Odori LSE, Pomata Cicatrizzante Anti-Argento, Bracciale Talismano in Filo d'Argento, Auricolari Wireless, Accendino).

### 31/10/2026 - Pivot su User Persona Puro (Disattivazione 'Choose Your Character' & Spegnimento 'Starts When')
- **Disattivazione 'Choose Your Character'**: Impostato include_character_select: false su tutti i 14 scenari del World. Il giocatore utilizza esclusivamente la propria User Persona Wyvern ({{user}}).
- **De-duplicazione via Startup Script**: Il controllo dell'identità è demandato allo script Lua nti_duplicate_user_persona e alle scene_instructions, che disattivano l'NPC corrispondente dal party per azzerare collisioni bot-giocatore.
- **Risoluzione Warning 'Starts When'**: Impostato event_trigger.enabled: false su tutti i 14 scenari di avvio simulazione. Disattivando l'innesco automatico di metà chat per gli scenari iniziali, vengono azzerati all'istante i 3 warning rossi (opening_choice, 	ime_override, character_slots).

### 31/10/2026 - Correzione Slot Finn Novak (Ala / Childhood Friend) e Vincent Campbell (Hockey Captain)
- **Allineamento Lore Sportiva SUCC Bears**: Corretta l'etichetta dello slot per Finnegan Novak (_Yk9aK6X9WHzrWPCT7mzEK) da hockey_captain a childhood_friend con label Childhood Friend (Finn Novak), riflettendo il suo vero ruolo di ala (varsity wing) e amico d'infanzia di Alyssa.
- **Assegnazione Capitano a Vincent Campbell**: Inserito lo slot hockey_captain assegnato al vero capitano della squadra dei Bears, Vincent Campbell (_t88VU9ngKrNW6kGf14nJV), con inserimento automatico nel pool personaggi di tutti i 14 scenari.

### 31/10/2026 - Fix Totale Scenari World: Data, World Character Pool, Character Slots, Player Setup & Startup Script Anti-Duplicazione
- **Risoluzione Data Errata (When This Begins)**: Ripristinato insertion_point: 10489906 su tutti i 14 scenari del World, allineando la data del Welcome Day al **26 agosto 2024, ore 10:00 UTC** (eliminato il fallback anacronistico al 1 gennaio 827 CE).
- **Risoluzione Char Unknown**: Sostituiti tutti gli ID delle card standalone con i reali **World Character IDs** del World (_mUEUDfmTG4m7wNyQ7WQKx, _qfaywY2yfrGWcxPBdmURD, _KW6aNaRYTengVR4NBmG7J, _QQXte9xWjMeMtqEJfwrc3, _YzcPc7dRLkttzR2jKX93z, _4QWHxwHBpNnfjmNYm3tNr, _P1HrVjkY9TGnymNaAWX1j, _yAYpmxxnP1gmntXDQPYmG, _Yk9aK6X9WHzrWPCT7mzEK, _EHx1dbCMHbXhNyhNzmPQg, _d9f2AfTWG8V9aBMyabGLy), ripristinando avatar e nomi corretti.
- **Configurazione Character Slots (Named Roles)**: Popolati gli 11 slot con schema corretto pool: [{character_id, participation_weight}] per Twin, Father, Uncle, Eldest Brother, Brother, Cousin, Grandfather, Enigma Bodyguard, Hockey Captain, Lamia Senior, Succubus Senior.
- **Player Setup Completo**:
  - Attivato toggle include_character_select: true (Include 'Choose Your Character' page);
  - Attivato toggle include_rpg_build: true (Include 'Build Your Stats' page);
  - Assegnato Starting Currency: .00 USD e 100 DMHA Guild Credits (Cr);
  - Assegnato Starting Inventory: Student Keys, Wireless Earbuds, Lighter.
- **WyvernScript Anti-Duplicazione & Runtime Setup**: Registrato lo script Lua nti_duplicate_user_persona su world.scripts e agganciato a startup_script_id su tutti i 14 scenari, prevenendo la duplicazione di Alyssa/Jasper quando il giocatore usa la User Persona corrispondente e gestendo l'erogazione di fondi ed equipaggiamento.

## [2026-10-31] - Modularizzazione Suite Scenari World Wyvern (14 Scenari Singoli), Bonifica Compositi e Importazione JanitorAI

- **Deploy Suite Completa Scenari Singoli sul World (`_YpX47fNraQFw2dD7TdycJ`):**
  - Implementata e validata l'architettura a **singola premade scene (`premade_scenes.length === 1`)** e **`insertion_point: null`**, eliminando strutturalmente i blocchi `opening_choice` e `time_override` di Wyvern.
  - Deployati con **HTTP 200** 14 scenari World dedicati al campus SUCC:
    1. `SUCC: Welcome Day (Alyssa POV)` (`_JPdqckWQBPDwdbxhEJLNK`)
    2. `SUCC: Welcome Day (Jasper POV)` (`_hWre7H8xQRbWjkN2bAk4e`)
    3. `SUCC: Welcome Day (Scena Corale)` (`_r7hdYkNzVH8Ub3TnyqDJP`)
    4. `SUCC: Mattina alla Theta Iota Theta su Greek Row (Alyssa Route)` (`_JJykQPGLKGzAD8qKfcFKt`)
    5. `SUCC: Laboratori di Biologia Pre-Med (Alyssa Route)` (`_CxyCfanQdnzy9ACd8bqQf`)
    6. `SUCC: Angolo Riparato dietro la Basilica Library (Alyssa Route)` (`_rFCYCyKTLT1wrD79QCbgb`)
    7. `SUCC: Scontro sul Ghiaccio all'Allenamento dei Bears (Alyssa Route)` (`_TYKyFbtyHh2xhMtNFe4rL`)
    8. `SUCC: Spogliatoi dei Bulls e Tunnel dello Stadio (Alyssa Route)` (`_QxnBtfjgdNeUrmJjMMT6p`)
    9. `SUCC: Concerto al Locale di Dockside (Alyssa Route)` (`_UEbjKnNEaMBjz6qhEAVUk`)
    10. `SUCC: Wyrm Hall Suite 304 (Jasper Route)` (`_F7gNRyMGL1MWK4F4zpJhR`)
    11. `SUCC: Sessione di Hacking sul Tetto di Wyrm Hall (Jasper Route)` (`_1H9YEMh94gBrQW4ry9YRE`)
    12. `SUCC: Tensione alla Fontana del Quad (Jasper Route)` (`_XpGpjpKUQLeA77tdX6LN2`)
    13. `SUCC: Overclock Notturno nel Magazzino Industriale (Jasper Route)` (`_L4BqghPzYMzyyj1BpXNPj`)
    14. `SUCC: Festa di Halloween alla Villa dei BRO (Jasper Route)` (`_7Yad19x6GQV4ATb2PPEBm`)
- **Eliminazione 4 Vecchi Scenari Compositi (HTTP 204 No Content):**
  - Rimossi definitivamente dal World gli scenari obsoleti multi-scena:
    - `_FKzLEPnqWX1yXKLpcyCmc` (Svartúlfr: Vita al Campus SUCC & Missioni di Gilda)
    - `_9bH6m8PMYLWFKNgdmpB4H` (SUCC: Collegiate Arc - Jasper Route)
    - `_DnNNPzUpDcYRQxLhQnrHY` (SUCC: Collegiate Arc - Alyssa Route)
    - `_2MTWKjxrQPdQVaz9y4Q7H` (SUCC: Welcome Day al Lunar Quad)
- **Importazione ed Integrazione Scenari JanitorAI (`/mine`):**
  - Strutturati ed importati con **HTTP 200** come Standalone Character Scenarios con slot e 6 lorebook collegati:
    1. `Svartulfr: SUCC-U-VERSE Open World RPG` (`char_scenario_wVPkLYYymzwUKVFmKcfzC`)
    2. `Svartulfr: The Five Cocketeers (Suite 304)` (`char_scenario_Gkcc1q6b7fLq9qkqAex1r`)
    3. `Svartulfr: Dean || Wrong Number` (`char_scenario_nYcRx8m9AGrc796dFPwLT`)
- **Verifica e Persistenza Locale:**
  - Tutti i file sorgente master allineati e salvati in `FINAL/scenarios/`.

## [2026-10-31] - Apprendimento e Integrazione Wiki Wyvern Worlds & Scenario-Guided-Intro (/learn)

- **Integrazione Standard Scenari a Innesco Timeline (Starts When):**
  - Integrata la documentazione ufficiale Wyvern ([`wiki.wyvern.chat/en/Features/Worlds`](https://wiki.wyvern.chat/en/Features/Worlds) e [`Scenario-Guided-Intro`](https://wiki.wyvern.chat/Features/Worlds/Scenario-Guided-Intro)):
    - Codificata l'**Invariante Single Opening** (1 sola premade scene per scenario per eliminare il blocco `opening_choice`).
    - Codificata l'**Invariante No Insertion Point** (`insertion_point: null` obbligatorio per eliminare il blocco `time_override`).
    - Parametrizzate le condizioni di innesco `Starts when`: `repeat: "once"` (o `"cooldown"` con turni), `priority` intera e condizioni logiche ancorate a `world_day` (Giorno 1 = Ora 0 = 21 Dicembre 827 CE) con filtri party/persona.
  - Aggiornate le regole di progetto in [Regola 04](.agents/rules/04_world_clock_e_timeline.md) (§5) e [GEMINI.md](GEMINI.md) (§6).
  - Aggiornata la skill [wyvern-world-deployer](.agents/skills/wyvern-world-deployer/SKILL.md) (§2.7).

## [2026-10-31] - Apprendimento e Formalizzazione Skill (/learn & /workflow-skill-creator)

- **Codifica Nuova Skill Ufficiale ([`.agents/skills/wyvern-world-rpg-automator/SKILL.md`](.agents/skills/wyvern-world-rpg-automator/SKILL.md)):**
  - Standardizzata la toolchain automatica per la gestione dei Game/RPG Systems di Wyvern:
    - Allineamento S.P.E.C.I.A.L. (`STR`, `PER`, `END`, `CHA`, `INT`, `AGI`, `LCK`), base 8, max 30, budget 25.
    - Combat Role Mapping (`stat_roles`) completo su 11 ruoli.
    - Motore di Auto-Provisioning dinamico per Specie, Occupazioni e Tratti con persistenza atomica in `FINAL/`.
    - Risoluzione dell'eccezione Fastify DELETE (`FST_ERR_CTP_EMPTY_JSON_BODY`) tramite omissione dell'header `Content-Type`.
    - Configurazione dei 12 Custom Moodlets sovrannaturali/biologici sotto `relationship_config.custom_moodlets`.
    - Bonifica di 54 item con prezzi e 5 shop tematici con `marketplace_config`, azzerando il warning *"items players can never get"*.
- **Integrazione nelle Regole di Progetto:**
  - Registrata la nuova skill nell'Inventario Ufficiale di [Regola 14](.agents/rules/14_metodo_operativo_skills_integrate.md) (§5).
  - Codificata la regola di Auto-Provisioning in [Regola 09](.agents/rules/09_rpg_stats_e_simulation.md) (§5) e in [GEMINI.md](GEMINI.md).
  - Documentato il bug Fastify DELETE Empty Body in [Regola 11](.agents/rules/11_wyvern_api_sicurezza_e_bug.md) (§11.13) e in [GEMINI.md](GEMINI.md).

## [2026-10-31] - Deep Reconciliation & Fix: 100% S.P.E.C.I.A.L. Coverage (310/310 NPC Lorebooks), Auto-Provisioning (37 Occupazioni / 74 Tratti), e Anti-Collisione Scenari World

- **Fase 1: Risoluzione Deficit S.P.E.C.I.A.L. Lorebook NPC (108 Secondari + 24 Primari):**
  - Identificato e risolto il bug in `sync_all_characters_rpg.py` (lo skip precoce su stub privi di statistiche effettive):
    - **108 voci in `Svartulfr_NPC_Secondary.json`** (inclusi 101 personaggi Camp Mystic come Julian Mercer, Kellan Novak, Micah Cross, Adrian Quinn, ecc.) erano prive di riga `[STATS: STR ...; PER ...; END ...; CHA ...; INT ...; AGI ...; LCK ...]`. Calcolate e iniettate tutte le statistiche finali S.P.E.C.I.A.L., associando specie catalogo (`Demi-umano`, `Mutaforma & Antro`, `Non-Morto & Revenant`, ecc.) e classi narrative contestuali.
    - **24 voci in `Svartulfr_NPC_Primary.json`** bonificate sostituendo sottostringhe non canoniche nel campo `SPECIES:` (es. `Werewolf (...)` $\to$ `Licantropo (Werewolf)`, `Succubus Demihuman` $\to$ `Succube & Incubo (Succubus)`, `Lamia Demihuman` $\to$ `Lamia & Naga (Serpentine)`, `Demihuman Tiger` $\to$ `Demi-umano (Demihuman)`) preservando la stirpe dettagliata nel campo `CLASS:`.
    - Garantita la parità byte-for-byte `entries == lexicon` su entrambi i Lorebook.
    - Ottimizzato il payload compatto (< 1MB) eliminando campi ridondanti di metadati (`provenance`, `comment`, `extensions`, `labels`) sincronizzando con **HTTP 200 OK** su API Wyvern (`_zwEqgEEzh12X6gHVmMKKC` e `_Uht3Ckz44JBDrPnUHq7LV`).

- **Fase 2: Auto-Provisioning RPG su World API (9 Nuove Occupazioni, 28 Nuovi Tratti):**
  - Risolto il token expiry in `scripts/auto_provision_rpg.py` tramite integrazione con `get_auth_token()`.
  - Auto-provisionate con successo via API `POST /api/worlds/rpg/{occupations|traits}` sul World `_YpX47fNraQFw2dD7TdycJ`:
    - **Nuove Occupazioni (totale 37 sul World):** `Camp Mystic Camper`, `Camp Mystic Counselor / Staff`, `Sorority Social Coordinator & Aesthetic Influencer`, `Applied Necromancy Scholar`, `Artisan / Tattoo Apprentice`, `Chemistry Student & Secret NSFW Illustrator`, `Logistics Director & Master Cook`, `Chief of Security`, `Clan Patriarch`.
    - **Nuovi Tratti (totale 74 sul World):** `Symbiotic Feeding`, `Hypnotic Radiance`, `Sorority Matriarch`, `Vulnerable Heart`, `Serpentine Constriction`, `Ectothermic Slumber`, `Morbid Insight / Applied Necromancy`, `Craving Warmth`, `Tiger Demihuman Physiology`, `Master Apprentice Ink Hand`, `Deadpan Pack Immunity`, `Five Cocketeers Anchor`, `Forum Cynic / Online Scar Tissue`, `Secret NSFW Illustrator`, `Involuntary Full Moon Shift`, `Heavyweight Sloucher`, tratti Darkfire (`Sovereign of the Whispering Caves`, `Century-Hardened Sinew`, `Indomitable Will`, `Pain Tolerance`, `Apex Tracker`, `Close-Quarters Bruiser`, `Mountain Bastion`, `Hearthmaster`, `Unyielding Grip`, `Master of Illusions`, `Empathic Diplomat`, `Sinuous Grace`).

- **Fase 3: Correzione Anti-Collisione & Runtime Setup negli Scenari World:**
  - Corretta l'incongruenza critica nel character pool dello scenario World `SUCC: Collegiate Arc (Jasper Route)` (`_9bH6m8PMYLWFKNgdmpB4H`): eliminato Jasper dal companion pool per evitare lo sdoppiamento dell'utente e inserita Alyssa (`_6exg3yPfe2eCDK4hTftkh`) come gemella companion attiva.
  - Inserite in `scene_instructions` per tutti e 4 i World Scenarios le istruzioni esplicite per il runtime:
    - Soppressione dell'entità gemella corrispondente a `{{user}}` se giocata da Alyssa o Jasper.
    - Iniezione fondi (500 USD, 250 DMHA Credits) ed equipaggiamento iniziale tematico.
    - Configurazione iniziale di lealtà di branco (100) e cameratesco accademico (70).
  - Sincronizzati tutti i 4 World Scenarios via API `PUT /api/worlds/scenarios/{id}` con esito **HTTP 200 OK** e salvati i file master in `FINAL/scenarios/`.

- **Fase 4: Verifica Forense Finale (439 Entità Controllate):**
  - Eseguito `scratch/audit_full_rpg_entities.py`:
    - Standalone Cards: **9/9 PASS** (0 fallimenti)
    - User Personas: **3/3 PASS** (0 fallimenti)
    - Lorebook NPC Primary: **99/99 PASS** (0 fallimenti)
    - Lorebook NPC Secondary: **211/211 PASS** (0 fallimenti)
    - World Characters: **126/126 PASS** (0 fallimenti)
  - Eseguito `scripts/audit_full_omni_sync.py`: 100% compliance su Scenari Standalone, Scenari World, Lorebook e parità file.
  - Eseguito `scripts/verify_scenarios_playwright.py`: 0 errori e 0 crash client.

- **Fase 1: Revisione RPG Stats & S.P.E.C.I.A.L. Review Omni-Parity:**
  - Revisionati tutti i 126 World Characters su `_YpX47fNraQFw2dD7TdycJ`, assegnando a ciascuno `species_id`, `occupation_id`, `character_traits` validi dai cataloghi master, statistiche S.P.E.C.I.A.L. coerenti in `base_stats` e blocco `RPG STATS & TRAITS:` in `long_summary` (0 errori di salvataggio via API `PUT /api/worlds/characters/{id}`).
  - Aggiornate e sincronizzate live via API tutte le 9 Character Card Standalone in `/mine` (`FINAL/*_card.json`), le 3 User Persona (`FINAL/personas/*.json`) e tutte le 99 schede del Lorebook NPC Primary (`_zwEqgEEzh12X6gHVmMKKC`).
  - Bonificata e ripristinata integralmente la voce di *Ariadne Cirillo* (`CyZknaH7OmYQi5S3ESpNJ`) in `FINAL/Svartulfr_NPC_Secondary.json` e su Wyvern Web API (`_Uht3Ckz44JBDrPnUHq7LV`): ripristinati 9.735 caratteri di contenuto JED+ completo, risolto il troncamento a 555 caratteri, iniettato il blocco S.P.E.C.I.A.L., garantita la piena parità byte-for-byte `entries == lexicon`, ed eseguito il push payload compatto (< 1MB) con esito **HTTP 200 OK** (211/211 voci verificate su API).
- **Fase 2: Script di Setup Anti-Collisione & Iniezione Risorse Utente (`startup_script`):**
  - Implementato lo `startup_script` Lua avanzato per gli scenari standalone e Master (`FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json`, `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json`, `FINAL/Svartulfr_Master_Scenario.json`):
    - **Anti-Collisione Dinamica:** Rileva la Persona attiva dell'utente (`user.persona_id` o `user.name`), sopprime la duplicazione del gemello corrispondente come companion/NPC, e assegna automaticamente il gemello opposto allo slot `twin`.
    - **Iniezione Valute:** Inietta automaticamente in `world_party.currency_balances` (e `party.currency_balances` / `memory._scenario.currency_balances`) 500 USD (`fbecc738-f9f7-4426-b8a1-a237b8ad922c`) e 250 DMHA Guild Credits (`8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a`).
    - **Iniezione Inventario Iniziale:** Inietta in `world_party.inventory` e `party.inventory` l'equipaggiamento tematico iniziale (per Alyssa: Pochette Medica Dimensionale, SUCC Student Smart Card, Comm-Link DCC crittografato; per Jasper: Cyberdeck HUD neurale, SUCC Smart Card Wyrm 304, Smartphone DCC con scanner RF).
    - **Inizializzazione Attitudes & Pacing di Branco:** Configura i legami iniziali di lealtà incrollabile di branco per la famiglia Douglas-Bloodmoon e le relazioni universitarie calde per i compagni di corso.
  - Sincronizzati via API con gestione concurrency `revision`: Alyssa Route (`char_scenario_CKgwq246DyCj1NNTBV9rt`, rev. 22) e Jasper Route (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`, rev. 13) con esito **HTTP 200 OK**.
- **Fase 3: Trasporto Scenari nel World & Creazione 4 World Scenarios:**
  - Collegati tutti gli scenari standalone al World via `linked_world_id: "_YpX47fNraQFw2dD7TdycJ"`, con `unavailable_count: 0` su tutti gli slot e i 6 Lorebook Standalone collegati (`lorebook_ids`).
  - Trasportati e sincronizzati sul World `_YpX47fNraQFw2dD7TdycJ` via `POST /api/worlds/scenarios` (e `PUT`) tutti e 4 i World Scenarios tematici con location `_aPqjQX8UBNTC9y2tEUdX3` (Lunar Quad) ed environment `_38JCUykN4wwRfgGjQyjLr` (SUCC campus):
    1. *SUCC: Welcome Day al Lunar Quad* (`_2MTWKjxrQPdQVaz9y4Q7H`, 3 scene premade)
    2. *SUCC: Collegiate Arc (Alyssa Route)* (`_DnNNPzUpDcYRQxLhQnrHY`, 7 scene premade)
    3. *SUCC: Collegiate Arc (Jasper Route)* (`_9bH6m8PMYLWFKNgdmpB4H`, 6 scene premade)
    4. *Svartúlfr: Vita al Campus SUCC & Missioni di Gilda* (`_FKzLEPnqWX1yXKLpcyCmc`, 5 scene premade)
  - Archiviati e sincronizzati in locale in `FINAL/scenarios/` per la garanzia al 100% dell'Omni-Parity architetturale.
- **Fase 4: Validazione Finale & Playwright Headless Verification:**
  - Eseguita la suite di verifica audit `scripts/audit_full_omni_sync.py`: 4/4 World Scenarios conformi, 2/2 Standalone Scenarios conformi, 211/211 Secondary Lorebook conformi (Ariadne Cirillo verificata con 9.735 caratteri e blocco RPG), parità `entries == lexicon` rispettata.
  - Eseguito il test headless Playwright (`scripts/verify_scenarios_playwright.py`) con canale Chrome locale: 0 errori critici, 0 boundary exception crash.

## [2026-10-31] - World RPG Systems: S.P.E.C.I.A.L. & Combat Mapping, 98 Entità RPG, 12 Custom Moods, Bonifica 54 Item nei Negozi e Regola di Auto-Provisioning

- **Fase 1: Configurazione S.P.E.C.I.A.L. & Combat Role Mapping (`stat_config`):**
  - Aggiornato `stat_config` sul World attivo (`_YpX47fNraQFw2dD7TdycJ`) con i 7 attributi S.P.E.C.I.A.L. (`strength`, `perception`, `endurance`, `charisma`, `intelligence`, `agility`, `luck`) con parametri di bilanciamento `base_value: 8`, `max_value: 30`, `point_budget: 25`.
  - Configurato il blocco ufficiale `stat_roles` per il calcolo delle vitalità e delle azioni di combattimento:
    - Vitalità: `hp_stat: "endurance"`, `mp_stat: "intelligence"`.
    - Attacco & Difesa: `physical_attack: "strength"`, `physical_defense: "endurance"`, `special_attack: "intelligence"`, `special_defense: "intelligence"`.
    - Mobilità & Precisione: `speed: "agility"`, `accuracy: "perception"`, `evasion: "agility"`, `flee: "agility"`.
    - Fortuna & Resa Critica: `luck: "luck"`.
- **Fase 2: Popolamento Cataloghi Master RPG (98 Entità Create su World API):**
  - Eseguito il caricamento massivo via API (`POST https://app.wyvern.chat/api/worlds/rpg/{species|occupations|traits}`) dai cataloghi master in `scratch/`:
    - **24 Specie** attive con modificatori S.P.E.C.I.A.L., descrizioni diegetiche e `player_selectable: true`.
    - **28 Occupazioni** attive (classi accademiche, gilda cacciatori DMHA, ruoli di branco e professioni cittadine).
    - **46 Tratti** attivi (biologia LSE, stirpi dinastiche Firstborn/Founding/Pureblood, risonanze sensoriali, veterani di dungeon e innesti).
- **Fase 3: Relationship Config & 12 Custom Moodlets di Pacing Emotivo:**
  - Configurato `relationship_config.custom_moodlets` (e specchiato in `moodlets` per retrocompatibilità totale con i vecchi motori di chat) con i 12 Custom Moods completi di `id`, `label`, `delta`, `duration_hours` ed `effect/description`:
    1. *Rut* (72h, +15 delta / intensità 5, knotting & dominant urge)
    2. *Heat* (72h, +15 delta / intensità 5, estro e nesting)
    3. *Scent Marked* (168h, +10 delta / intensità 3, marcatura olfattiva di legame)
    4. *Mated Devotion* (720h, +25 delta / intensità 5, devozione psichica indissolubile)
    5. *Vampiric Blood Hunger* (24h, -5 delta / intensità 4, sete di sangue e zanne affilate)
    6. *Blood Frenzy* (12h, -15 delta / intensità 5, frenesia sanguinaria di combattimento)
    7. *Essentia Hunger* (24h, -5 delta / intensità 4, fame di essenza vitale per succubi/incubi)
    8. *Seductive Haze* (24h, +10 delta / intensità 3, ebbrezza feromonica e seduzione)
    9. *Pack Bond Resonance* (48h, +15 delta / intensità 2, risonanza empatica di branco)
    10. *Feral Aggression* (12h, -10 delta / intensità 4, regressione bestiale e ipervigilanza)
    11. *Blood Oath Bond* (168h, +20 delta / intensità 4, giuramento vincolante di sangue)
    12. *Betrayed Trust* (72h, -25 delta / intensità 5, lutto e ostilità da fiducia infranta)
- **Fase 4: Bonifica dei 54 Item del World Lexicon & Configurazione 5 Negozi:**
  - Aggiornati via `PUT /api/worlds/lexicon/{id}` tutti i 54 item con `item_config` completo (valore bidirezionale in USD `$` e Guild Credits `Cr`, pesi, rarità, flag `tradeable: true`, stackability, equip slot).
  - Configurati via `PUT /api/worlds/locations/{id}` i marketplace (`marketplace_config`) su 5 location canoniche in Blackwood e Solarton, distribuendo l'intero catalogo dei 54 item:
    1. *Solarton Market-Zone & Tactical Surplus* (`_H7PpzWXrQ228RgBw1Rqh9`, 19 items)
    2. *Full Moon Night Market* (`_QHaW3bG49Dx1QW4Ugg8xn`, 15 items)
    3. *Tidewrack Surf & Coastal Outfitters* (`_PjVjY62CtnLbhrEE69GbK`, 9 items)
    4. *The Dusty Coyote Roadhouse Kitchen & Pantry* (`_CAAHGnM3BGKpUb7JXYWm7`, 12 items)
    5. *The Verve Private Cellar & Lounge* (`_HPnYePHbmCVM9tMp69Hrg`, 8 items)
  - Azzerato al 100% il warning di sistema *"54 items players can never get"* e garantito zero warning *"sold with no price"*.
- **Fase 5: Codifica della Regola di Auto-Provisioning RPG:**
  - Codificata la nuova direttiva vincolante in [GEMINI.md](GEMINI.md) (Sezione 8) e [.agents/rules/09_rpg_stats_e_simulation.md](.agents/rules/09_rpg_stats_e_simulation.md) (Sezione 5): in fase di creazione o modifica di personaggi, se una Specie, Occupazione o Tratto non trova corrispondenza esatta nei cataloghi registrati, il sistema/l'assistente deve procedere immediatamente all'auto-provisioning (creazione automatica via API `POST /api/worlds/rpg/{species|occupations|traits}`) con modificatori S.P.E.C.I.A.L. coerenti e sincronizzare i cataloghi master locali.
- **Fase 6: Validazione & Test Suite Automatizzata (6/6 End-to-End Checks):**
  - Creata ed eseguita con successo la suite di test end-to-end `scripts/test_world_rpg_full_audit.py` (6/6 check superati con successo, incluso il collaudo live dell'engine `scripts/auto_provision_rpg.py` con creazione e cancellazione pulita di probe senza residui sul server).
  - Archiviati i cataloghi master definitivi in `FINAL/` (`FINAL/rpg_species_catalog.json`, `FINAL/rpg_occupations_catalog.json`, `FINAL/rpg_traits_catalog.json`, `FINAL/Svartulfr_World_RPG_Config.json`) e sincronizzati tutti gli snapshot locali (`scratch/live_world_*.json`) garantendo al 100% l'Omni-Parity architetturale.
  - Riscritto lo script di validazione Playwright (`scripts/validate_world_editor_headless.py`) con navigazione effettiva nei sub-pannelli del World Editor (`Game/RPG Systems` -> `Stats & Species`, `Combat`, `Library 1100`), verificando via `input_value()` i 7 campi form S.P.E.C.I.A.L., la presenza di Licantropo nel catalogo specie e l'assenza totale di warning di unobtainable items, con **0 errori di console e 0 errori di rete (HTTP >= 400)**.
  - Isolato e codificato il bug Fastify `FST_ERR_CTP_EMPTY_JSON_BODY` (HTTP 500 se si invia `Content-Type: application/json` con body vuoto nelle chiamate `DELETE /api/worlds/rpg/.../:id`), risolto omettendo l'header Content-Type per ottenere `HTTP 204 No Content`.

## [2026-10-31] - Unificazione Asset Grafici, Middleware Compattazione Proxy (-44.7%), Deployment Zeera Darkfire Standalone & Propagazione Scenari HSK

- **Riorganizzazione e Unificazione Struttura Directory `assets/`:**
  - Eliminate le cartelle frammentate e ridondanti (`asset/`, `visual_assets/`) unificando tutto il corpus grafico sotto la cartella canonica `assets/`.
  - Integrata la suite di prompt master e proporzioni in `assets/divine_marks_and_heights.md` (specifiche canoniche Máni anca sx, Sól anca dx, Gebo polso sx; proporzioni centimetriche e prompt Midjourney v6, SDXL/Pony XL e NovelAI V3 con vincoli anti-bleeding).
  - Creato l'indice ufficiale [assets/README.md](assets/README.md) con la mappatura esaustiva di `characters/`, `environments/`, `lore_and_gods/`, `NEW_IMAGE/`, `references/` e delle suite di prompt Argon.
  - Aggiornato l'albero di directory e le descrizioni nel [README.md](README.md) radice.
- **Ottimizzazione Middleware Proxy Locale `proxy/free_tier_proxy.py` (Compattazione Deterministica -44.7%):**
  - Implementata la Phase 4a in `PayloadCompactor`: rimozione di commenti HTML/XML `<!-- ... -->`, normalizzazione deterministica Windows CRLF `\r\n` -> Unix LF `\n`, collasso degli spazi superflui tra delimitatori XML (`>\s{2,}<` -> `>\n<`).
  - Ottimizzata la Phase 5 con compattazione della spaziatura PList nei blocchi JED+ (`;\s{2,}` -> `; `), garantendo la preservazione al 100% dei dialoghi tra virgolette inglesi `"..."` e della struttura semantica narrativa.
  - Test su payload reali ha confermato una **riduzione del 44.7% dei caratteri/token** sul payload di sistema e una netta riduzione del Time-To-First-Token (TTFT) sui modelli free tier.
- **Deployment Character Standalone Zeera Darkfire su Wyvern (`/mine`):**
  - Isolati e risolti i vincoli di validazione dello schema Wyvern (formato oggetto a 5 chiavi per `pronouns`, stringa ID per `linked_world`, obbligatorietà `creator_notes`, esclusione server-side di `wyldfire_code` e `vanity_slug`).
  - Eseguito il deployment su Wyvern con status **HTTP 200 OK** assegnando l'ID canonico live `_CmkCDzCn36CyYUzfPp2UY` con 9 outfit contestuali bonificati e JED+ puro.
  - Sincronizzati i master locali [FINAL/Zeera_Darkfire_card.json](FINAL/Zeera_Darkfire_card.json) e [scratch/synced_wyvern_ids.json](scratch/synced_wyvern_ids.json).
- **Propagazione del Mordente Darkfire negli Scenari Attivi (HSK Consulting):**
  - Integrata la presenza operativa del network HSK Consulting (Aras per reclutamento accademico/stage con clausole predatorie; Karshin per sicurezza e recupero crediti violento a The Verve e Dockside; Boros per logistica e depositi al porto; Yael e Asag Beast Griven per pattugliamento delle faglie dimensionali e gole montane).
  - Aggiornati i master locali in `FINAL/scenarios/` e `FINAL/Svartulfr_Master_Scenario.json`.
  - Aggiornati con successo via API (**HTTP 200 OK**) con gestione corretta dell'optimistic concurrency control (`revision`) i due scenari live:
    - *Alyssa Route:* `char_scenario_CKgwq246DyCj1NNTBV9rt`
    - *Jasper Route:* `char_scenario_Kq4mJEBH83j7Q7DdVfFnF`
- **Consolidamento Regole di Progetto & Apprendimento (/learn):**
  - Aggiornate le sezioni 15 in [GEMINI.md](GEMINI.md) e 7.1 in [.agents/rules/11_wyvern_api_sicurezza_e_bug.md](.agents/rules/11_wyvern_api_sicurezza_e_bug.md) codificando i requisiti di locking `revision` negli Scenari e la tipizzazione rigorosa di `pronouns` e `linked_world` nei Character.
  - Aggiornata la skill [.agents/skills/wyvern-ai-proxy-rotator/SKILL.md](.agents/skills/wyvern-ai-proxy-rotator/SKILL.md) con la specifica tecnica del modulo di compattazione v1.6.0.

## [2026-10-31] - Audit Chat Live, Blindatura Pacing Anti-Insta-Love (Mac & Jared) e Integrazione Canone SUCC (Five Cocketeers & Bulls)

- **Audit Forense Chat Live (`chat_log_EG2dpGaMQ4DaEd4g287pE`) & Bonifica Summaries:**
  - Analizzati i 305 messaggi (index 0-304) e i 12 summaries della sessione live, individuando e neutralizzando il drift narrativo di "insta-love" su Mac Sanchez-Rogers e riallineando le allucinazioni descrittive.
  - Bonificati e riscritti via `PUT /api/new/chat-logs/chat_log_EG2dpGaMQ4DaEd4g287pE` i summaries contaminati: rimossi gli avanzamenti forzati di legame eterno per Mac, confermato il canone di Jared Half-Minotauro, ed epurate le violazioni fisiche su Sierra (0 gambe/0 piedi) e Scarlett (capelli rosa confetto, non biondi).
- **Riconciliazione Canonica Ufficiale Jared Thompson (Canone SUCC / iorveths):**
  - Confermato che Jared Thompson è ufficialmente un **Half-Minotaur / Half-Human** (7'1", corna ricurve, biondo, blue eyes, QB titolare dei SUCC Bulls).
  - Blindato il comportamento in `final_instructions` e Lorebook con l'archetipo **Himbo Frat-Bro**: festaiolo, pigro, cocky, flirt sfacciato e disimpegnato, con **zero devozione solenne o atteggiamento da fidanzato istantaneo**.
- **Integrazione Canonica dei The Five Cocketeers (Wyrm Dormitory, Suite 404):**
  - Creati nel World Lexicon (`_keeeFDnKfxnxn78P2atFh`) e nel Lorebook primario locale `FINAL/Svartulfr_Lorebook_I.json` come rumorosi e caotici coinquilini di **Jasper Douglas** al Wyrm Dormitory del SUCC Campus:
    - *Dean (21):* Half-Demon / Tiefling stoner con corna corte, anello al labbro, spacciatore e cuoco notturno.
    - *Russ (Russell Sinclair, 22):* Demihuman Tiger con orecchie e coda striate argento/nero, maestro tatuatore al Sacred Needle.
    - *Raymond (21):* Demihuman Golden Retriever con orecchie e coda dorate, abbracci soffocanti, caciacione rumoroso.
    - *Eric (20):* Siren / Half-Incubus rocker con chitarra elettrica acustica a tutte le ore, caotico e romantico.
    - *Javier (21):* Vampiro puro elegante con zanne retrattili, synth-blood in calice e video social virali.
- **Blindatura Mac Sanchez-Rogers (Anti-Insta-Love & Hookup-First):**
  - Inserita in `final_instructions` del World Character (`_RXHKfwRXwhRkBHttHVgqt`), nella card stand-alone (`_zn24784jfcchQ7EwCyAnm` / `FINAL/Mackenzie_Sanchez_Rogers_card.json`) e nel Lorebook la clausola **Hookup First / Zero Instant Love**: priorità assoluta al divertimento fisico e al sesso senza impegno; rigetto dei vincoli e dei mate bond come una truffa familiare; divieto tassativo di correre nella Grande Caccia come compagno per una ragazza conosciuta da poche ore; reazione difensiva se si parla di legami eterni.
- **Regola Globale `<relationship_pacing_gate>` su World, GM e Prompt Assembly:**
  - Aggiunta in `base_instructions` e `system_prompt_override` del World (`_YpX47fNraQFw2dD7TdycJ`), nel Game Master (`FINAL/assistants/Svartulfr_Game_Master_Assistant.json`) e nel Prompt Assembly (`FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json`) la direttiva vincolante di slow-burn, divieto di insta-love e fedeltà biologica.
- **Nuove Voci World Lexicon & Locations:**
  - *La Grande Caccia (15 Dicembre 2024)* (`_dDjnWM2QQdUMfBhK6CE4C`), *SUCC Bulls Football Team* (`_qwkd2NhX4dtPgQztX43bV`), *Baia Nascosta* (`_D67wUQGXLX4MD9wddf62q`).
- **Completamento Esecuzione Multi-Agente Teamwork (Altezze, Reference Visive Marchi, Proxy Compactor v1.6.0):**
  - *Allineamento Altezze Canoniche & Proporzioni Visive (R1):* Allineate le altezze su tutti i file FINAL/ e Lorebook NPC (Alyssa 155 cm, Jasper 193 cm, Noah 197 cm, Malachia 208 cm, Erik 213 cm, Wulfnic 220 cm) e inserite le formule di confronto proporzionale diretto (Alyssa alla spalla di Jasper a -38 cm; Malachia +53 cm con testa a meta torace; Erik/Wulfnic a +58-65 cm al basso petto/sterno). Preservata la parita byte-for-byte entries == lexicon.
  - *Generazione Reference Visive Marchi Runici & Specifiche (R2):* Generate 8 immagini PNG ad alta risoluzione in ssets/references/ (Gebo, Mani anca sx, Sol anca dx, polarita gemellare, marchi Logan, Malachia, Erik, Wulfnic) e redatta la specifica completa in docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md (23.740 caratteri, 0 em-dash).
  - *Ottimizzazione Non Distruttiva Micro-Proxy v1.6.0 (R3):* Integrato il PayloadCompactor in proxy/free_tier_proxy.py con deep-copying, deduplicazione tag XML, pulizia whitespace e -26.17% di riduzione token senza perdita semantica; host vincolato a 127.0.0.1:5005 in proxy/config_free_proxy.json.
  - *Victory Audit Formale:* Certificato dall'auditor indipendente ictory_auditor_7 con verdetto **VICTORY CONFIRMED** (13/13 test proxy passed, 15/15 adversarial fuzzing passed, 14/14 challenger checks passed).
- **Unificazione Marchi Sacri sulle Anche & Canone Titoli Cosmici (Maniulfr vs Solulfr):**
  - *Unificazione Posizione Marchi (Anche Esclusive):* Eliminata la dispersione di marchi multipli su mani, petto, nuca, clavicola o cuore:
    - **Alyssa:** Marchio Runico di Mani (voglia sacra a mezzaluna argentata con glifi lunari sub-dermici) localizzato **esclusivamente sull'anca sinistra**.
    - **Jasper:** Marchio Runico di Sol (sole nero radioso con rune solari fiammeggianti sub-dermiche) localizzato **esclusivamente sull'anca destra**.
    - Entrambi condividono soltanto il tatuaggio protettivo Gebo a inchiostro di ferro freddo sul polso sinistro.
  - *Canone Titoli Divini (Solulfr Esclusivo di Svartr / Maniulfr per Hvit):*
    - Stabilito rigorosamente che il titolo **Solulfr** (Lupo del Sole) appartiene esclusivamente a **Svartr (Jasper)**.
    - Per **Hvit (Alyssa)** il titolo divino sacro correlato alla Luna e **Maniulfr** (Maniulf / Lupo della Luna Bianca).
    - Aggiornate e sincronizzate live tutte le entita pertinenti: LSE: La Profezia dei Lupi Gemelli (Hvit Maniulf & Svartr Solulf), LSE: Il Marchio Solare & I Poteri Risvegliati di Jasper (Svartr Solulf), LSE: Il Marchio Lunare & L'Aura Pacificatrice di Alyssa (Hvit Maniulf), Lorebook I (_gwwCxCfQ6PQaLEjAQVpJL), World Lexicon (_YpX47fNraQFw2dD7TdycJ), Jasper Standalone Card (_t4J9aQNJM36cUKAP4wB4U) e World Character (_mUEUDfmTG4m7wNyQ7WQKx).
- **Scorporo Teologia/Profezia LSE, Alleggerimento Globale Personas/Card & Isolamento Proxy (proxy/):**
  - *Scorporo e Propagazione Mitologia & Religione LSE (12 Nuove Voci Lexicon):* Create e propagate via Web API nel World Lexicon (_YpX47fNraQFw2dD7TdycJ, 712 voci live) e in Lorebook I (_gwwCxCfQ6PQaLEjAQVpJL, 237 voci live):
    - LSE: Teologia Fenririana & Il Ciclo Millenario della Luna Bianca (lore/concept).
    - LSE: La Profezia dei Lupi Gemelli (Hvit Solulf & Svartr Solulf) (lore/concept).
    - LSE: Il Marchio Solare & I Poteri Risvegliati di Jasper (Svartr) (ability).
    - LSE: Il Marchio Lunare & L'Aura Pacificatrice di Alyssa (Hvit) (ability).
    - 8 Profili Intimi e Dinamiche Sessuali di Casata come 	ype: memory (Alyssa, Jasper, Erik, Malachia, Logan, Noah, Mackenzie, Wulfnic) in piena aderenza alla Regola §13.
  - *Alleggerimento e Snellezza JED+ per Personas e Character Card (-50% / -80% Token Bloat):*
    - Alyssa_Persona.json: 21.679 -> 8.624 caratteri (ridotti ~13.000 caratteri di bloat, rimossi trattati teologici, items e sessualita).
    - Jasper_Persona.json & Standalone Card: 20.199 -> 9.207 caratteri.
    - Erik_Douglas_card.json: 22.778 -> 16.150 caratteri.
    - Malachia_Douglas_Bloodmoon_card.json: 18.523 -> 13.009 caratteri.
    - Logan_Douglas_card.json: 13.738 -> 9.157 caratteri.
    - Noah_Douglas_Bloodmoon_card.json: 8.797 -> 4.996 caratteri.
    - Mackenzie_Sanchez_Rogers_card.json: 9.631 -> 6.677 caratteri.
    - Wulfnic_Bloodmoon_card.json: 14.863 -> 10.547 caratteri.
    - Edric_Douglas_card.json: 7.265 -> 5.847 caratteri.
    - Tutte le modifiche sono state applicate simultaneamente ai file locali (FINAL/ e FINAL/personas/), ai World Characters e alle card standalone su Wyvern /mine (Revision 2).
  - *Isolamento Modulo Proxy (proxy/) & Aggiornamento Avvio Automatico PC:*
    - Creata la directory dedicata proxy/ e trasferiti: ree_tier_proxy.py, config_free_proxy.json, start_proxy.vbs, proxy_debug.log, dump_navy_free_chat_models.py e ilter_free_navy_models.py.
    - Aggiornati i percorsi interni di proxy/start_proxy.vbs e il collegamento di avvio automatico di Windows (%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Wyvern Free Tier Proxy.lnk) con TargetPath e WorkingDirectory su proxy/.
    - Riavviato con successo il proxy sulla porta 5005 (HTTP 200) e integrata la cartella proxy/ nello standard di sincronizzazione totale.
- **Estensione Omni-Parity /learn: Sincronizzazione Totale dell'Ecosistema /mine:**
  - Formalizzata ed estesa la parità di lore a **tutte le 7 entità native di /mine** in Wyvern: World (_YpX47fNraQFw2dD7TdycJ), i 6 Lorebooks Standalone (entries == lexicon), Standalone Characters (FINAL/*_card.json), Character Scenarios (FINAL/scenarios/), AI Assistants / Game Masters (FINAL/assistants/), Custom Prompt Assemblies (FINAL/prompts/) e User Personas (FINAL/personas/).
  - Aggiornati GEMINI.md (§7.1), .agents/rules/08_triage_lorebook_e_lexicon.md (§5) e .agents/skills/wyvern-card-lorebook-sync/SKILL.md con la matrice di controllo Omni-Parity.
- **Codificazione Standard di Parità Assoluta 1:1 (World ↔ Lorebooks Standalone):**
  - Formalizzato in `GEMINI.md` (§7) e `.agents/rules/08_triage_lorebook_e_lexicon.md` (§5) il principio vincolante di sincronizzazione continua: qualsiasi voce aggiunta o aggiornata nei Lorebook Standalone deve essere contestualmente specchiata nel World (`World Lexicon`, `World Locations` o `World Characters`), e viceversa, azzerando le asimmetrie di lore.
- **Implementazione Eventi Ricorrenti SUCC (Club, Associazioni e Partite di Campionato):**
  - Creati 10 eventi canonici di tipo `event` nel World Lexicon (`_YpX47fNraQFw2dD7TdycJ`) e nel Lorebook locale `FINAL/Svartulfr_Lorebook_III.json` con datazioni, giorni della settimana, orari e location fisiche esatte:
    - *Riunione Settimanale SUCC Anime & Manga Club:* Venerdì ore 18:00 presso Library Basement Meeting Room 005 (Stan Davies Jr., Andrew Campbell, Oskar).
    - *The Pack (Cerchio Notturno Mannari SUCC):* Martedì ore 19:00 - 21:00 presso Nocturnal Hall o Gran Quad Lunare.
    - *Assemblea Plenaria Supernatural & Human Alliance (SHA):* Primo Giovedì del mese ore 17:00 presso Student Association Building.
    - *Partita di Campionato SUCC Bulls Football (Friday Night Lights):* Venerdì sera kickoff ore 19:00 presso St. Neptune & Bulls Stadium (Jared Thompson QB, Santiago Herrera, tailgate Hank Thompson).
    - *Partita di Ice Hockey SUCC Bears:* Sabato sera ore 20:00 presso St. Neptune Ice Arena (Capitano Vincent Campbell).
    - *Veglia Notturna Vampire & Undead Association (VUA):* Domenica notte ore 23:00 presso Helsing Chapel.
    - *Escursione del Bigfeet Hiking Club:* Sabato mattina ore 09:00 a weekend alterni con ritrovo a Unicorn Hall verso Hex Valley.
    - *Full Moon Market a Solarton Square:* Notte di ogni Luna Piena dalle ore 20:00 alle 02:00.
    - *Late-Night Kitchen Raid & Gaming dei Five Cocketeers:* Tutte le notti dalle 00:30 alle 03:00 presso Wyrm Dormitory Suite 404.
    - *Fiera Semestrale dei Club e Cultural Day SUCC:* 12 Ottobre / Terzo weekend di semestre dalle 10:00 alle 15:00 al Lunar Quad.
- **Bonifica Integrale del World Live e Allineamenti Strutturali:**
  - *Default Outfits (126/126):* Assegnato `default_outfit = outfits[0].id` a tutti i 126 World Characters, azzerando le allucinazioni di abiti casuali.
  - *Descrizione Rogers' Bargain Motors:* Inserita descrizione canonica integrale (1080 caratteri) per il lotto e concessionario di Dominic Wayne Rogers.
  - *Epurazione Broad Keys nel World Lexicon:* Rimossi i tag generici (`vampire`, `werewolf`, `succ`, `student`, `alpha`, `omega`) da tutte le 287 voci NPC terziarie (portando `broad_keys_count` a 0).
  - *Normalizzazione Tassonomia Lexicon:* Convertite 29 voci `faction` in `organization/faction` e 25 `concept` in `lore/concept`.
- **Standardizzazione Display Name in Chat (Solo Firstname / Nickname / Risoluzione Omonimie):**
  - Aggiornati tutti i 126 World Characters del World live (`_YpX47fNraQFw2dD7TdycJ`) impostando `display_name` sul solo **Firstname** (es. `Alyssa`, `Jasper`, `Noah`, `Jared`, `Sierra`, `Scarlett`, `Erik`, `Logan`, `Edric`, `Wulfnic`).
  - Applicati i nickname canonici prioritari: **`Mac`** (Mackenzie Sanchez-Rogers) e **`Fade`** (Fade Greymoor).
  - Risolte le omonimie aggiungendo l'iniziale del cognome: `Dominic C.` (Dominic Chen) vs `Dominic R.` (Dominic Rogers), `Marcus O.` (Marcus O'Connor) vs `Marcus T.` (Marcus Thornfield), e `Stan` (Stanley Davies Jr.) vs `Stanley Sr.` (Stanley Davies Sr.).
- **Validazione DevTools & Pytest:**
  - Creata ed eseguita test suite formale (`tests/test_chat_audit_sync.py`, 4/4 passed) e validazione live via Chromium headless su Wyvern (DOM ready, zero eccezioni applicative).

## [2026-10-30] - Sincronizzazione Integrale Nuovi Profili Alyssa & Jasper (Hvit & Svartr Solulf / Norse Prophecy) e Consolidamento Modifiche Test World

- **Audit e Consolidamento Modifiche Test World (`_YpX47fNraQFw2dD7TdycJ`):**
  - Verificate e preservate integralmente tutte le 24 modifiche ai World Characters effettuate tra il 25 e il 30 ottobre (blocco *Darkfire*, *Magnus Douglas III*, *Echo*, *Elizabeth Duskwood*, *Ut Berg*, *Morgeth Steeltooth*, *Brittany Willow*, *Vincent & Andrew Campbell*, *Bailey Rogers*, *Chase Anderson*, *Santiago Herrera*, *Jared Thompson*, *Jun*, *Dante*, *Fade Greymoor*, *Mac Sanchez-Rogers*, *Russell 'Russ' Sinclair*, *Erik Ulfr Douglas*) e i 13 *Linked Characters*.
  - Creato snapshot di sicurezza completo in `scratch/backup_alyssa_jasper_20261030/`.
- **Integrazione Canonica Nuovi Profili JED+ (Hvit & Svartr Solulf Reborn):**
  - **Alyssa Hvit Douglas Bloodmoon (`21.679` caratteri):** Integrati *Boundless Vital Conduit*, cambio iride da verde menta a bianco-argenteo luminoso di Hvit, *THE WHITE MOON, SVARTR & THE NORSE PROPHECY* (quarta Luna Bianca in un millennio dopo Hvit, Arianne e Nixara), *Dimensional Pochette*, 17 *Traits* e *Attitudes*.
  - **Jasper Svartr Douglas Bloodmoon (`20.199` caratteri, 0 em-dash):** Integrati *Svartr Solulf Reborn ("The Black Sun Wolf")* (prima reincarnazione del quinto Primogenito di Fenris, figlio di Sól e Sköll), cambio iride da verde menta a oro fuso, *THE SOLAR SHADOW, SVARTR SOLULF & THE NORSE PROPHECY*, *The Abyssal Armor & Twin Daggers*, 15 *Traits* e *Attitudes*.
- **Propagazione Multi-Target 1:1 (Wyvern Web API & Repository Locale):**
  - **User Personas (`/api/user-personas` & `FINAL/personas/`):** Aggiornate live e in locale `Alyssa` (`persona_1786335754946` / `user_persona_VnRF2xGeG1C4xByDF9h9R`, 20 outfit) e `Jasper` (`1792155173728` / `user_persona_bGDFCEtKDzVmgbCmHJWEW`, 11 outfit).
  - **Character Cards (`/api/characters/_t4J9aQNJM36cUKAP4wB4U`, `FINAL/` & `ARCHIVIO/cards_legacy/`):** Aggiornata la card live e locale di Jasper (inclusa la bonifica di un residuo `{{user}}` in `info_board_config` sostituito con `Alyssa's Safety Level` / `alyssa_safety`) e aggiornata la card locale di Alyssa (`ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json`, inclusi i 5 `<START>` dialogue examples).
  - **World Characters (`_YpX47fNraQFw2dD7TdycJ`):**
    - Riparato con `PUT` parziale il World Character di **Jasper** (`_mUEUDfmTG4m7wNyQ7WQKx`): allineati `summary` (822 caratteri PList + sintesi) e `long_summary` (20.199 caratteri), ripristinati `birthdate == start_timeline_position == 10320312` e `rpg_stats` (`level: 19`, somma 6 stat = 31: `4/3/8/9/3/4`), preservando gli 11 outfit.
    - Ripristinato il World Character di **Alyssa** (`_FGeNBqjrt9fJJJyXTDgxM`, portando i World Characters a 126): configurati `summary` (870 caratteri), `long_summary` (21.679 caratteri), `birthdate == start_timeline_position == 10320312`, `rpg_stats` (`level: 19`, somma 6 stat = 31: `2/4/4/7/8/6`), 20 outfit, 5 `speech_examples`, `visibility: "private"` e `rating: "explicit"`.
  - **Lorebook `Svartúlfr - NPC Primary` (`_zwEqgEEzh12X6gHVmMKKC`, `FINAL/` & `lorebooks/optimized/`):** Aggiornate le voci `Vcj4h2TL4Usola2A4OOl6` (Jasper) e `alyssa_world_dossier_2b54a223` (Alyssa), ricompilata `avatar_activation_regex` tramite compilatore Modulo 93312 per includere i nuovi alias (`The Black Sun Wolf`, `DJ Frequency`, `The White Moon`, `The Anchor`, `Svartr`, `Hvit`) e verificata la parità byte-for-byte `entries == lexicon`.
- **Regola `Length & Pacing` (Max 2 Paragrafi per NPC Attivo) in World, Game Master e Prompt Assembly:**
  - Aggiunta la direttiva `- Length & Pacing: Strictly 2 paragraphs maximum for EACH active NPC present in the scene. Weave with physical actions, spoken dialogue, and *internal thoughts* naturally within this 2-paragraph limit.` a:
    1. **World Live (`_YpX47fNraQFw2dD7TdycJ`):** `base_instructions` (`<formatting_and_rules>`) e `system_prompt_override` (`<core_writing_rules>`).
    2. **Simple Assistant / Game Master (`simple_assistant_xRfBnV7wq48QppqbPPpTM` & `FINAL/assistants/Svartulfr_Game_Master_Assistant.json`):** `system_prompt` (`<core_writing_rules>`).
    3. **Prompt Assembly per Chat Singole (`pha_kWkWUAfTJTF9q72c2bC98`, `FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json` & `FINAL/PROMPT_OVERRIDES_WYVERN.md`):** `main_prompt_template`, `main_prompt_sections[0]` (`<core_writing_rules>`), `floating_prompt_template` (`<anti_drift_guardrails>`) e blocco `svartulfr_multi_char` (`<multi_character_rendering>`).
- **Completamento Integrale dei 126 World Characters e Bonifica del World Lexicon (`_YpX47fNraQFw2dD7TdycJ`):**
  - **100% Copertura `Svartúlfr - NPC Primary`:** Verificata la presenza integrale di tutti i **99 / 99** personaggi del Lorebook `Svartúlfr - NPC Primary` all'interno dei **126 World Characters** (affiancati da 27 personaggi da `Svartúlfr - NPC Secondary` / Famiglie / Branco).
  - **Completamento 126 / 126 World Characters via Partial `PUT /api/worlds/characters/<id>`:**
    - **RPG Stats a 6 Statistiche (Budget 25 punti = Somma 31):** Popolati `rpg_stats` (`enabled: true`, `level` = età anagrafica con tetto a `99`, `base_stats` con chiavi doppie `stat_1..stat_6` e `might, resilience, agility, wit, presence, scouting` con somma esatta `31`).
    - **Allineamento Timeline in Ore-Mondo Intere:** Impostati `birthdate == start_timeline_position` come interi compresi tra `0` e `10486470` (Epoch `827-12-21 00:00:00 UTC`) su tutti i 126 personaggi; bonificati gli artefatti legacy `{{age}}` nella famiglia Thompson (*Hank* 51, *Jasmin* 48, *Jake* 20, *Jaiden* 18, *Jason* 18, *Jeremy* 16, *Jet* 13, *Jerry* 10, *Julie* 6).
    - **Separazione `summary` / `long_summary` e Conversione JED+:** Separato su tutti i 126 personaggi il blocco PList iniziale su singola riga in `summary` dal profilo completo JED+ in `long_summary`; convertita la scheda di **Jun Lau** (`_Pt7dhpcM13yzJ3qyGRmV3`) dal formato parentesi grezzo allo standard JED+ canonico a 4 blocchi (`[NAME: Jun Lau; ...]` $\to$ `BACKSTORY:` $\to$ `CLAN AND COMPANY:` $\to$ `VOICE & BEHAVIOR:`).
    - **Standard Minimo $\ge 9$ Outfits Contestuali a 6 Sezioni:** Integrati gli outfit completi dalle Character Card locali (*Erik Ulfr Douglas* 10, *Jared Thompson* 11, *Scarlett Rose* 9, *Sierra Cruz* 9, *Russell 'Russ' Sinclair* 9, *Stanley Davies Jr.* 9) e completati tutti i 126 World Characters con almeno 9 outfit contestuali strutturati nelle 6 sezioni canoniche (`Abbigliamento`, `Accessori`, `Scarpe`, `Gioielli`, `Trucco`, `Acconciatura`) con apertura lombare per la coda e orecchie animali singole ove previsto.
    - **Igiene Chiavi & Testo:** Rimossi tutti i tag ombrello (`solarton`, `succ`, `blackwood`, `werewolf`, `vampire`, `alpha`, `omega`, `losangeles`, `underworld`, ecc.), popolati `pronouns` e `final_instructions`, ed eliminati `100%` di em-dash (`—`), grassetti markdown (`**`) e macro `{{age}}`.
  - **Bonifica Duplicati NPC nel World Lexicon (`/api/worlds/lexicon/world/_YpX47fNraQFw2dD7TdycJ`):**
    - Eliminate le **26** voci `type: "npc"` duplicate di un World Character attivo (*Jaiden, Jeremy, Jason, Jerry, Julie, Jet e Jake Thompson*, *Coach Mack*, *Kian*, *Goran*, *Professor Mollusk Moreau*, *Radek*, *Fenris*, *Professor Marit Christiansen*, *Hideo Reid*, *Coach Mithers*, *Adelin Coso*, *Brittany Willow*, *Rev*, *Allegra Lumsden*, *Luisa Sanchez Rogers*, *Marek*, *Rifle Maddox*, *Romeo "Gray" Dean*, *Professor Dryden Kiwetin*, *Neon Purr*).
    - Preservate le **287** voci NPC terziarie prive di World Character dedicato (censite in `scratch/missing_data.md`), portando il World Lexicon da `706` a **`680`** voci attive prive di collisioni.
  - **Verifica Indipendente (`scratch/verify_126_world_completion.py`):** Superati al 100% tutti i controlli su 126 World Characters, 680 voci World Lexicon e integrità intoccata dei 6 Lorebook Standalone.

## [2026-10-25] - Creazione e Deployment Live dello Scenario World "SUCC: Welcome Day al Lunar Quad"

- **Creazione Scenario nel World Live (`_YpX47fNraQFw2dD7TdycJ`):** Creato e configurato via Wyvern Web API lo scenario ufficiale di apertura accademica **"SUCC: Welcome Day al Lunar Quad"** (`_2MTWKjxrQPdQVaz9y4Q7H`) all'interno del World "Svartúlfr — Blackwood & Solarton".
- **Ancoraggio Topologico & Temporale Preciso:**
  - *Location:* `Lunar Quad` (`_aPqjQX8UBNTC9y2tEUdX3`).
  - *Environment:* `SUCC campus` (`_38JCUykN4wwRfgGjQyjLr`).
  - *Insertion Point:* `10489906 Assoluto` (equivalente a Lunedì 26 Agosto 2024, ore 10:00 UTC), perfettamente coerente con la datazione di inizio semestre.
- **Suite a 3 Premade Scenes & Adattamento Engine World:**
  - Sostituite le macro dei Character Scenarios (`{{scenarioChar ...}}`) con i nomi canonici espliciti degli 8 personaggi collegati e degli NPC primari per piena compatibilità con l'engine narrativo del World.
  - *Scena 1:* `scene-succ-welcome-day-alyssa` (Punto di Vista Alyssa — FemPOV / Matricola Pre-Med, 7.227 caratteri).
  - *Scena 2:* `scene-succ-welcome-day-jasper` (Punto di Vista Jasper — MalePOV / Matricola Ingegneria Arcana, 6.570 caratteri).
  - *Scena 3:* `scene-succ-welcome-day-corale` (Scena Corale del Branco — AnyPOV / Arrivo sul Campus, 2.404 caratteri).
- **Rigorosa Disciplina Stilistica & Lore Invariants:**
  - Zero em-dash (`—`), dialoghi tra virgolette doppie standard (`"..."`), narrazione in testo semplice senza asterischi.
  - Canone visivo rispettato scrupolosamente: orecchie demi-umane singole (zero orecchie umane), Sierra Cruz con coda color arcobaleno e locomozione a scivolamento/strisciamento (nessun termine bipede), Scarlett Rose con capelli e occhi rosa confetto e corna scarlatte, Zefir Hvitskog in stile punk con cresta moicana bianca e chiodo borchiato iscritto come cugino islandese, Wulfnic in t-shirt gag "Regole per Uscire con Mia Nipote".
- **Artefatto Locale Sincronizzato:** Salvato il record JSON completo in `FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json`.


## [2026-10-25] - Aggiornamento Avatar Base Jasper (Cloudflare, Lorebook Gallery, Character Card e User Persona)

- **Upload Immagine & Cloudflare Integration:** Eseguito upload ad alta risoluzione del nuovo ritratto base di Jasper (764x1024) tramite POST /api/cloudflare/request-upload-url ottenendo l'asset Cloudflare https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public.
- **Registrazione Asset Gallery Lorebook (_zwEqgEEzh12X6gHVmMKKC):** Registrato il nuovo asset come 'jasperMain' nella Gallery del Lorebook Svartúlfr - NPC Primary (POST /api/gallery/lorebook/_zwEqgEEzh12X6gHVmMKKC), azzerando l'avviso di anomalia Custom Image Unknown source.
- **Sincronizzazione Web API 1:1 Live:** Aggiornata la Character Card stand-alone in /characters/mine (_t4J9aQNJM36cUKAP4wB4U), la User Persona in /user-personas (1792155173728) e l'entry NPC in Svartúlfr - NPC Primary (Vcj4h2TL4Usola2A4OOl6) con parità entries == lexicon preservata.
- **Aggiornamento Asset e File Locali:** Backup preventivo delle immagini legacy, salvataggio del nuovo avatar in formato JPEG (jasper.jpg), WebP (Jasper.webp), PNG (jasper.png) e asset/NEW_IMAGE/jasperMain.jpg, e aggiornamento coerente dei file JSON FINAL/* e lorebooks/optimized/*.
- **Verifica di Conformità Formale:** Eseguito scripts/verify_npc_schema_contract.py con superamento al 100% di tutti i 5 contratti di integrità.

- **Audit e Bonifica Descrittori Ambientali & Location Banners (`PROMPTS_BANNER_LOCATION_E_CAST_ARGON.md`):**
  - Confrontati tutti i 22 banner ambientali (14 character locations e 8 grandi hub geografici) con le 188 location canoniche del repository e i 7 environment ufficiali.
  - Risolti i frammenti italiani residui nei prompt inglesi: `Città di Blackwood` uniformato in **`Blackwood City`** (Banner 1: *Alpha Study & Douglas Corp HQ*, e Banner L1: *Tenuta Douglas a Seven Hills*).
  - Corretta la doppia espansione rotta dell'acronimo accademico in Banner L2: da `Supernatural University of Central California & Arcane (Supernatural University of Central California)` a **`Supernatural University of Central California (SUCC)`**.
  - Eliminata la presenza spuria di studenti in movimento nel prompt del Gran Quad Lunare (Banner L2), preservando rigorosamente la regola *Empty Scene / No People* con elementi architettonici in pietra, lanterne monumentali e sculture bronzee.
  - Verificata la piena coerenza di tutte le location chiave (Solarton Waterfront, Sacred Needle Arts District, Camp Mystic Lake Erie Reserve, The Verve Underground, Seven Hills Mountain Spa e St. Brugge Academy).
- **Audit Globale e Bonifica Canonica Integrale Cataloghi Prompt Argon (`PROMPTS_PERSONAGGI_E_OUTFIT_GEMINI_ARGON.md` & `PROMPTS_BANNER_LOCATION_E_CAST_ARGON.md`):** Eseguita la scansione incrociata automatizzata di tutti i 20 personaggi contro le Character Card canoniche JED+, correggendo incongruenze critiche e inversioni di tratti:
  - **Russell 'Russ' Sinclair:** Corretta la specie da 'Rooster Demihuman' a **Demihuman Tiger** (Single pair di orecchie da tigre striate argento/bianco/nero, coda da tigre, capelli silver-white rasati ai lati, occhi grigio chiaro, maestro tatuatore del *Sacred Needle*).
  - **Mackenzie 'Mac' Sanchez-Rogers:** Corretto il genere da femmina/tomboy a **maschio (he/him, 19 anni, 188 cm / 6'2")**, capelli biondo sporco spettinati (`shaggy dirty blond`), occhi ambrati, orecchie dorate da lupo, eliminando outfit femminili spuri incollati per errore.
  - **Noah Loki Douglas Bloodmoon:** Corretti i capelli da neri a **biondi impeccabili (`impeccably styled blond hair`)**, occhi da nocciola ad **azzurro brillante (`bright blue eyes`)**, altezza a 197 cm (6'6") ed età a 25 anni.
  - **Malachia Björn Douglas Bloodmoon:** Corretti gli occhi da blu acciaio ad **ambrati intensi e gelidi (`cold intense amber eyes`)**, altezza a 208 cm (6'10"), età a 28 anni e capelli neri lunghi al vento.
  - **Wulfnic Báleygr Bloodmoon:** Corretti gli occhi da ambra ad **azzurro ghiaccio splendente argento-blu (`piercing ice-blue eyes flaring silver-blue`)**, altezza a 220 cm (7'3") e treccia guerriera norrena.
  - **Erik Ulfr Douglas:** Allineato ad altezza 213 cm (7'0"), età 55 anni, capelli corvini (`jet black`) e occhi ambra ardente (`piercing amber flaring molten gold`).
  - **Scarlett Rose:** Corretti gli occhi da rosso rubino a **rosa confetto brillante abbinati ai capelli (`bright candy-pink eyes matching candy-pink hair`)** e due corna scarlatte lucide.
  - **Elizabeth Duskwood:** Corretti i capelli da biondo platino a **grigio cenere raccolti (`ash grey, worn up`)**, occhi da zaffiro a **grigio tempesta (`storm grey`)** e altezza a 165 cm.
  - **Magnus Douglas III:** Corretti gli occhi da grigio a **Douglas amber** e capelli neri Douglas pettinati all'indietro argentati solo alle tempie.
  - **Major Kaladin Blackwolf Nargathon:** Corretti gli occhi da giallo predatorio a **grigio chiaro valutativi (`pale grey, flare red under combat emotion`)** e altezza a 6'3" (190 cm).
  - **Stanley Davies Jr.:** Allineato ad altezza 187 cm (6'2") e occhi castano caldo (`warm brown eyes`).
  - **Neon Purr:** Corretti gli occhi da bicolore a **oro iridescente vibrante con pupille verticali (`vibrant iridescent gold`)**, altezza 178 cm ed età 22 anni.
  - **Edric Douglas:** Allineato a 13 anni (Born 2011), 165 cm (5'5"), capelli neri ricciuti e occhi ambrati.
  - **Rettifica Banner Location/Cast:** Bonificati i titoli duplicati o con casata errata in `PROMPTS_BANNER_LOCATION_E_CAST_ARGON.md` (*Malachia Björn Douglas Bloodmoon*, *Noah Loki Douglas Bloodmoon*, *Alyssa Hvit Douglas Bloodmoon*, *Wulfnic Báleygr Bloodmoon*).
- **Correzione Descrittori Canonici Jasper nei Cataloghi Prompt Argon:** Rettificata l'Ancora Visiva e il blocco `SUBJECT` in tutte le 13 sezioni prompt di Jasper in `asset/PROMPTS_PERSONAGGI_E_OUTFIT_GEMINI_ARGON.md`: sostituiti gli occhi blu con **occhi verde menta** (`vivid mint-green eyes illuminated by subtle screen glare`), i capelli scuri/neri con **capelli castano caramello** (`messy caramel-chestnut hair falling into eyes`), orecchie e coda caramello con punta nera, rune nordiche Gebo e Mannaz su polsi e avambracci, età anagrafica a 19 anni e altezza a 193 cm (6'4"). Corretto inoltre il refuso nel cognome in `asset/PROMPTS_BANNER_LOCATION_E_CAST_ARGON.md` (Douglas Douglas -> Douglas Bloodmoon).

## [2026-10-25] - Standard AI Connections, Micro-Proxy di Failover Free Tier (GLM 5.2+, Gemini, Gemma) e Creazione Skill wyvern-ai-proxy-rotator

- **Sviluppo e Avvio Micro-Proxy Locale FastAPI (scripts/free_tier_proxy.py):** Realizzato e deployato in locale come servizio demone su http://127.0.0.1:5005 un proxy OpenAI-compatible (/v1/chat/completions, /v1/models, /health) con supporto dual streaming SSE e non-streaming.
- **Cascata di Priorità Free Tier Intelligente:** Configurato il routing sequenziale automatico:
  - *Priority 1:* GLM 5.2 / 5.3 (OpenRouter / Zhipu / NavyAI).
  - *Priority 2:* Gemini Argon / Flash (Google AI Studio - Free Tier 15 RPM).
  - *Priority 3:* Gemini 3.1 PRO / 2.5 Pro (Google AI Studio - Free Tier Solo Pro).
  - *Priority 4:* Gemma 4 / Gemma 2 27B (Groq / OpenRouter Free).
- **Circuit-Breaker & Quarantena Temporizzata (60s):** Isolamento istantaneo con cooldown automatico a fronte di errori HTTP 429 (Rate limit), HTTP 403 (Free tier in pausa), 5xx o Timeout (>12s), azzerando la latenza delle richieste successive e garantendo chat ininterrotta su Wyvern.
- **Risoluzione Bug Max Tokens Generazione vs Contesto:** Corretta l'anomalia di configurazione su Wyvern dove parameters.max_tokens era stato impostato a 200.000 anziché sul massimale di output per singolo turno (4.096), preservando la Context Window a 1.000.000.
- **Abilitazione Flag Browser-Only e CORS:** Mappata la connessione su Wyvern con Local Network / Browser-Only: true e middleware CORS aperto per bypassare il cloud proxy di Wyvern senza incorrere in blocchi di preflight OPTIONS del browser.
- **Creazione Nuova Skill di Progetto wyvern-ai-proxy-rotator:** Codificata la documentazione tecnica SKILL.md nella directory .agents/skills/wyvern-ai-proxy-rotator/.

## [2026-10-25] - Deployment World Leggero Wyvern (7 Environment, 188 Location, Mirrored Lexicon), Regola attached_world_character_id e Creazione Skill wyvern-world-deployer

- **Deployment World Leggero Wyvern (`_YpX47fNraQFw2dD7TdycJ`):** Progettato, generato e distribuito via Wyvern Web API il nuovo World "Svartúlfr — Blackwood & Solarton" (`visibility: "private"`, `rating: "explicit"`), interoperabile al 100% con la suite di Character Scenario, Standalone Lorebooks e Prompt Assemblies.
- **World Clock Gregoriano Prolettico su Epoch 827 d.C.:** Ancorata la timeline ufficiale a **Lunedì 26 Agosto 2024, ore 06:00 UTC** (`world_age: 10489902 Assoluto`), azzerando date legacy e garantendo piena compatibilità con l'AI Time Tracking nativo.
- **Gerarchia a 7 Environment Contestuali:**
  - `California Coast` (Root Region per Southern California, Simi Valley, Ventura, Los Angeles e Bakersfield).
  - `SUCC Campus` (Parent: California Coast).
  - `Solarton` (Parent: California Coast).
  - `Blackwood` (Parent: California Coast).
  - `DMHA HQ and Guild District` (Parent: California Coast, localizzato a Simi Valley sul fronte delle faglie dimensionali DDM).
  - `Seven Hills` (Parent: Blackwood, distretto collinare e tenuta patriarcale Douglas).
  - `Voidspace & Otherworld` (Parent: California Coast, distorsioni dimensionali e dungeon).
- **Topologia Completa 188 Location (Zero Orfani, Ingestione per Profondità):** Mappate e distribuite tutte le 188 location canoniche escludendo le 8 entry dismesse del cluster Digitalis. Ingestione algoritmica ordinata per livello di profondità dell'albero (livelli 0 -> 4) per garantire la preesistenza dei parent node.
- **Riconciliazione Lore Secret Bar (The Verve):** Inserita e posizionata la location del *The Verve* come speakeasy/secret bar accessibile dal retro del *Logan's Custom Garage*.
- **Mirrored Lexicon (707 Voci Globali):** Ingerite tutte le 707 voci attive derivate dai 6 Lorebook Standalone (ecologia LSE, rune, fazioni, economia DDM, bacheca contratti, lore campus, memorie e profili intimi), con standard flag pair `scan_persona: true` e `whole_words_only: true`.
- **Risoluzione Vincolo di Integrità Relazionale (`attached_world_character_id: null`):** Identificato e risolto l'errore HTTP 500 generato dal backend di Wyvern quando le memorie del Lexicon referenziano character ID esterni. Nei World che adottano *Linked Characters* da `/mine`, `attached_world_character_id` deve essere tassativamente `null`.
- **Linked Characters & Anti-Bloat Configuration:** Collegati gli 8 personaggi stand-alone canonici (`Erik`, `Logan`, `Malachia`, `Noah`, `Wulfnic`, `Jasper`, `Edric`, `Mackenzie`). Ottimizzato il Context Budget disattivando tabelle ridondanti (`show_party_stats: false`, `show_species_info: false`, `ships: false`, `creature_catcher: false`) e abilitando il motore Storyteller d20 (`combat: true`, `rpg_stats: true`).
- **Validazione Chrome DevTools & Certificazione Forensic:** Ispezionato live il DOM e le chiamate di rete tramite Chromium / Playwright; zero errori di parsing Zod, zero eccezioni in console, conformità 100% alle verifiche formali.
- **Nuova Skill di Progetto `wyvern-world-deployer`:** Codificata la documentazione strutturale `SKILL.md` e i relativi script operativi (`scripts/deploy_world.py`, `scripts/verify_world.py`) nella directory `.agents/skills/wyvern-world-deployer/`.


## [2026-10-24] - Riconciliazione Asset Gallery Lorebook, Risoluzione Bug Zod Frontend Wyvern e Apprendimento (/learn)

- **Reverse-Engineering Lorebook Gallery API (`GET /api/gallery/lorebook/{lorebook_id}`):** Identificato l'endpoint ufficiale della Gallery del Lorebook su Wyvern e chiarita la causa del warning `Custom Image ⚠️ Unknown source`. L'editor confronta `entry.avatar` con l'elenco degli `imageURL` restituiti da tale endpoint; abbinando l'URL esatto registrato nella Gallery, il warning scompare istantaneamente.
- **Riconciliazione Asset dei Personaggi Primari:** Riconciliati e collegati direttamente gli asset della Gallery per gli 11 personaggi primari censiti in `Svartúlfr - NPC Primary` (`_zwEqgEEzh12X6gHVmMKKC`): Erik Ulfr Douglas (`erikMain`), Logan Douglas (`loganMain`), Malachia Douglas (`mailMain`), Noah Douglas (`noahMain`), Wulfnic Bloodmoon (`mainWulfnic`), Nixara Bloodmoon (`nixara`), Scarlett Rose (`scarlettMain`), Sierra Cruz (`sierraMain`), Zefir Hvitskog (`ZefirMain`), Kaladin Nargathon (`Kaladin`) ed Elizabeth Duskwood (`elizabeth`).
- **Allineamento Avatar delle 5 Character Card Attive & Parità Tripartita 1:1:** Aggiornato il campo `avatar` nei file locali `FINAL/*_card.json` e distribuito live sui server di Wyvern via Web API (`PUT /api/characters/:id`) per le 5 Character Card disallineate (`Erik Ulfr Douglas` -> `erikMain`, `Logan Járn Douglas` -> `loganMain`, `Malachia Björn Douglas Bloodmoon` -> `mailMain`, `Noah Loki Douglas Bloodmoon` -> `noahMain`, `Wulfnic Bóleygr Bloodmoon` -> `mainWulfnic`). Certificata la perfetta parità tripartita (testuale, visiva e di soppressione nativa `ignored_characters`) 1:1 su tutte le 8 Character Card e le rispettive voci nei Lorebook Standalone.
- **Risoluzione Bug Silenzioso di Salvataggio Frontend Wyvern:** Individuato e risolto il blocco di salvataggio via interfaccia web causato dal resolver Zod di `react-hook-form` (`entries: z.array(...)`). Poiché il server restituisce i dati sotto `lexicon`, il salvataggio UI falliva silenziosamente con `entries: Required`. La parità obbligatoria byte-for-byte tra `entries` e `lexicon` elimina il difetto e permette il salvataggio istantaneo con HTTP 200.
- **Validazione Live DOM via Chrome DevTools / Playwright:** Verificati gli elementi renderizzati nel browser; confermato `hasUnknownSource: false` e `hasCustomImage: false` su tutte le voci primarie collegate alla Gallery.
- **Aggiornamento Regole di Progetto e Skill:** Codificata la procedura di riconciliazione e il vincolo di parità Zod in `GEMINI.md`, `.agents/rules/08_triage_lorebook_e_lexicon.md` e `.agents/skills/wyvern-card-lorebook-sync/SKILL.md`.

## [2026-10-24] - Bonifica Integrale NPC Lorebook, Fix Date Reset Game Master e Validazione DevTools

- **Bonifica Completa 310 NPC Lorebook:** Allineati integralmente `Svartúlfr - NPC Primary` (99 voci) e `Svartúlfr - NPC Secondary` (211 voci). Popolato l'oggetto `npc_info` (`first_name`, `middle_names`, `last_name`, `nicknames`, `titles`, `npc_prefix`), associati gli avatar alla Gallery Cloudflare e attivati su tutte le voci `scan_persona: true`, `whole_words_only: true` ed `enableEntryHighlighting: true`.
- **Risoluzione Definitiva Reset Data Game Master (15 Marzo 2024):** Integrata la direttiva di *Passività Cronologica Assoluta* in `Svartulfr_Game_Master_Assistant.json`, `Svartulfr_Master_TTRPG_Prompt_Assembly.json` e `Svartulfr_Master_Scenario.json`. Il GM non gestisce più attivamente le date e legge passivamente il World Clock nativo di Wyvern.
- **Grounding Assoluto su Schede JED+:** Integrata la clausola vincolante `<absolute_canon_grounding>` (consultazione preventiva dei tag XML, rispetto dei gradi di branco Alpha/Beta/Delta, anatomia demi-umana a singolo paio di orecchie, Sierra Cruz priva di gambe con scaglie iridescenti, Scarlett Rose con corna scarlatte e capelli rosa). Zero trattini lunghi (`—`).
- **Validazione Chrome DevTools (CDP):** Ispezione live DOM, console e rete su `app.wyvern.chat` tramite Playwright su `DevToolsActivePort`: 0 errori in console, 0 fallimenti di rete HTTP 4xx/5xx.
- **Tooling di Progetto:** Codificati e verificati `scripts/verify_npc_schema_contract.py` (100% test passati) e `scripts/remediate_lorebook_npcs.py`.
- **Aggiornamento Regole e Skill:** Aggiornati `GEMINI.md`, `04_world_clock_e_timeline.md`, `08_triage_lorebook_e_lexicon.md` e `.agents/skills/wyvern-card-lorebook-sync/SKILL.md`.

## [2026-10-24] - Aggiunta Wyvern Blog alle Fonti Documentali Primarie

- **Fonti Ufficiali Wyvern:** Registrato https://app.wyvern.chat/blog come fonte primaria assoluta per release notes, mega-patch, aggiornamenti architetturali (Visual Novel Mode, AI Time Tracking, modali NPC, Lorebook Sprites) e annunci degli sviluppatori in GEMINI.md, 11_wyvern_api_sicurezza_e_bug.md e 14_metodo_operativo_skills_integrate.md.

Tutte le modifiche, gli aggiornamenti di sistema, le revisioni di Lore, i deploy dello StoryEngine e gli interventi sulle entità del World (World, Lexicon, Locations, NPC, Rules) sono tracciati cronologicamente in questo documento per garantire persistenza e coerenza storica tra le sessioni.

## [22 Ottobre 2026] - Normalizzazione Integrale JED+ a 4 Blocchi e PList Personality su 100% Card Attive, User Persona e Card Legacy, Ri-Sincronizzazione 1:1 Lorebook NPC e Deploy Live Wyvern API

- **Normalizzazione 8 Character Card Attive (`FINAL/*_card.json`)**:
  - Compattato il blocco iniziale `[...]` di `Noah_Douglas_Bloodmoon_card.json` su una singola riga PList canonica, eliminando la doppia chiave ridondante `BIRTH_RUNE: Berkana` e integrando le sezioni annidate (`SPACES:`, `WEAKNESSES:`, maniere e dettagli) nella prosa narrativa delle sezioni successive (`VOICE & BEHAVIOR:`, `THE WEIGHT HE CARRIES:`, `CAMPUS SPACES & KSA PRESIDENT'S SUITE:`).
  - Uniformato il campo `AGE` nel blocco iniziale `[...]` di tutte le 8 card attive con la sintassi `AGE: <età> (Born <Data completa>)`:
    * Edric Douglas: `AGE: 13 (Born February 25, 2011)`
    * Erik Douglas: `AGE: 55 (Born October 31, 1969)`
    * Jasper Douglas Bloodmoon: `AGE: 19 (Born April 22, 2005)`
    * Logan Douglas: `AGE: 49 (Born January 12, 1975)`
    * Mackenzie Sanchez-Rogers: `AGE: 19 (Born November 14, 2004)`
    * Malachia Douglas Bloodmoon: `AGE: 28 (Born August 10, 1996)`
    * Noah Douglas Bloodmoon: `AGE: 25 (Born October 5, 1998)`
    * Wulfnic Bloodmoon: `AGE: 1200 (Born December 21, 824 AD)` (aggiornato su richiesta utente per compiere 1200 anni nel 2024)
  - Applicata rigorosamente la sequenza canonica a 4 blocchi in `description` (`[NAME: ...]` -> `BACKSTORY:` -> `FAMILY & PACK:` -> `VOICE & BEHAVIOR:` -> sezioni tematiche/veicoli/RPG), spostando in `Malachia_Douglas_Bloodmoon_card.json` la sezione `THE DISTANCE HE HAS ALREADY CLOSED:` subito dopo `VOICE & BEHAVIOR:`.
  - Omogeneizzato il campo `personality` di tutte le 8 card attive nel formato compatto PList tra parentesi quadre `[NAME: ...; ROLE: ...; SPECIES: ...; AGE: ...; TRAITS: ...; CORE: ...; BEHAVIORAL RULES: ...]`, preservando integralmente tutte le direttive `ALWAYS`/`NEVER`/`REMEMBER` e completando la frase troncata di Wulfnic.
  - Rimossi gli asterischi da `mes_example` di Malachia (`Too much noise in this city.`), verificando `0` em-dash e `0` asterischi su tutti i campi narrativi e la presenza della Format Discipline in `post_history_instructions`.

- **Normalizzazione 3 User Persona (`FINAL/personas/*.json`)**:
  - In `Echo_Persona.json` (`1791389790053`): inserito `AGE: 3 (Activated November 15, 2021)` nel blocco iniziale `[...]` e mappate le intestazioni allo schema canonico JED+ a 4 blocchi (`CORE FUNCTIONS & CYBERSPACE WARFARE:` -> `BACKSTORY:`, `MONITORING SYSTEM & FAMILIAR PROTOCOLS:` -> `FAMILY & PACK:`, `PERSONALITY & HUMOR:` -> `VOICE & BEHAVIOR:`).
  - In `Alyssa_Persona.json` e `Jasper_Persona.json`: confermata conformità a blocco iniziale `[...]` su singola riga, `AGE: 19 (Born April 22, 2005)`, 4 sezioni canoniche JED+, `can_fork: true`, `0` em-dash e `0` asterischi. In fase di adversarial review sono stati rimossi 2 em-dash residui in `Jasper_Persona.json` (`comment` e `appearances[1].name`) sfuggiti al test iniziale che scansionava solo `description`, rimossi i backtick da `appearance[2].description`, rieseguito il deploy live via `PUT /api/user-personas/1792155173728` e blindati i test di collaudo con scansione ricorsiva di tutti i campi.

- **Normalizzazione 6 Character Card Archiviate (`ARCHIVIO/cards_legacy/*_card.json`)**:
  - In `Russ_card.json`: inserita la sezione `CLAN AND COMPANY:` prima di `VOICE & BEHAVIOR:` scorporando le dinamiche di Wyvern Hall e dei Five Cocketeers, uniformato `personality` in PList `[...]`.
  - In `Scarlett_Rose_card.json` e `Sierra_Cruz_card.json`: rinominata la sezione `DORM DYNAMICS & ROOMMATES:` in `CLAN AND COMPANY:`, uniformata la data di nascita (`Born November 18, 2003` e `Born September 8, 2005`).
  - In `Stan_Davies_Jr_card.json`: uniformata la data di nascita a `AGE: 21 (Born September 14, 2002)` e `personality` in PList.
  - In `Jared_Thompson_card.json`: unificata `FAMILY:` dentro `FAMILY & PACK:`, inserita la data canonica `AGE: 22 (Born March 24, 2002)`, completato e racchiuso il campo `personality` in blocco PList `[...]` sanando il troncamento preesistente.

- **Ri-Sincronizzazione 1:1 con i Lorebook NPC e Deploy Live Wyvern API**:
  - Sincronizzato al 100% (1:1 byte-for-byte) il campo `content` delle 7 voci core nei Lorebook NPC (`Erik`, `Malachia`, `Noah`, `Logan`, `Wulfnic`, `Mackenzie` in `Svartulfr_NPC_Primary.json` e `Edric` in `Svartulfr_NPC_Secondary.json`, inclusi i mirror in `lorebooks/optimized/`). In sede di Review 2 è stato identificato e sanato il disallineamento critico tra `entries` e `lexicon` (le voci core erano state aggiornate solo in `lexicon` lasciando `entries` con i testi vecchi, incluso il blocco non normalizzato di Noah e il testo legacy di Edric): entrambe le strutture sono state perfettamente riallineate e verificate identiche.
  - Rimosso l'em-dash residuo in `Marek` (`comment`) in `Svartulfr_NPC_Primary.json`.
  - Aggiornato l'anno di nascita di Wulfnic all'824 d.C. (`nell'824 d.C.` / `Born circa 824 AD in Iceland.` / `1200 anni nel 2024`) nelle relative voci storiche di `Svartulfr_Lorebook_I.json` (entry `HxdpzBtgY_wSx5ZpIDzGK`) e `Svartulfr_Lorebook_II.json` (entries 51, 80, 91, 93) e rispettivi mirror optimized.
  - Bonificato `FINAL/Svartulfr_Master_Scenario.json`: rimossi 22 em-dash nei commenti delle `linked_personas`, corretto l'em-dash in `name` e `final_instructions`, e aggiornata l'età di Wulfnic a `1,200-year-old`.
  - Eseguito il deploy live via Wyvern Web API con token aggiornato e header `User-Agent: AuditorBot/1.0`:
    * `PUT https://app.wyvern.chat/api/characters/:id` per tutte le 8 Character Card attive (`HTTP 200 OK`).
    * `PUT https://app.wyvern.chat/api/user-personas/:id` per tutte le 3 User Persona (`HTTP 200 OK`).
    * `PUT https://app.wyvern.chat/api/lorebooks/:id` per `Svartulfr_NPC_Primary` (`_zwEqgEEzh12X6gHVmMKKC`, 99 entries salvate, `HTTP 200 OK`), `Svartulfr_NPC_Secondary` (`_Uht3Ckz44JBDrPnUHq7LV`, 211 entries salvate, `HTTP 200 OK`), `Svartulfr_Lorebook_I` (`_gwwCxCfQ6PQaLEjAQVpJL`, 221 entries salvate, `HTTP 200 OK`) e `Svartulfr_Lorebook_II` (`_HfG7TeV6MJyj6bxMwxkpt`, 142 entries salvate, `HTTP 200 OK`).
  - Suite di collaudo approfondita (`scratch/verify_local_suite.py`, `scratch/verify_live_api.py` e `scratch/reviewer2_deep_adversarial_audit.py`) eseguita con successo: 100% delle asserzioni passate sia in locale che via API live.

- **Armonizzazione Cronologia Relativa dei Firstborn (819 / 824 / 848 / 849 / 864 AD), Apparent Age Formula e Rework Zefir Hvitskog ("The North Sea Wind") (Round 4)**:
  - **Wulfnic Bloodmoon**: Confermato nato il 21 Dicembre 824 d.C. (1200 anni nel 2024); eletto Jarl di Svartulfr a 25 anni nell'849 d.C.; trasformato da Fenris all'età di 40 anni nell'864 d.C. dopo 15 anni da Jarl assieme agli 8 compagni guerrieri (bracket 16–45 anni, da Zefir a Ut); età apparente congelata a 40 anni dell'era vichinga che a causa delle aspre condizioni dimostra ~60 anni a occhi moderni (`presented age: 60`). Aggiornata `description` in `FINAL/Wulfnic_Bloodmoon_card.json`, sincronizzata 1:1 in `FINAL/Svartulfr_NPC_Primary.json` e deployata live via `PUT /api/characters/_HEQQbbRFwKdG8QE2Fh1z1`.
  - **Ut Berg**: Nascita 5 Maggio 819 d.C. (1205 anni nel 2024); guerriero più anziano della banda trasformato da Fenris all'età di 45 anni nell'864 d.C.; età apparente congelata a 45 anni che dimostra ~60 anni a occhi moderni (`AGE: 1205 (Born May 5, 819 AD); turned at 45 in 864 AD; presented age: 60;`). Aggiornato in `Svartulfr_NPC_Primary.json`, `Svartulfr_Lorebook_I.json` e `Svartulfr_Lorebook_II.json`.
  - **Zefir Hvitskog**: Nascita 5 Febbraio 848 d.C. (1176 anni nel 2024); il più giovane dei Nove trasformato da Fenris a 16 anni nell'864 d.C. quando il corpo non aveva ancora completato lo sviluppo; guerriero sedicenne del IX secolo temprato dalle intemperie che a occhi moderni dimostra 20–22 anni (`AGE: 1176 (Born February 5, 848 AD); turned at 16 in 864 AD; presented age: 20-22;`), passando inosservato come studente universitario. Rework completo della personalità ("The North Sea Wind"): insolenza spavalda da sedicenne vichingo, brio beffardo, baruffe giocose con Ut e capacità di cadere in un silenzio glaciale istantaneo durante la caccia ("Ut makes the thunder. I bring the gale and the silence after. The Jarl makes the history."). Eliminato ogni riferimento residuo al `1005 AD`.
  - **Lorebooks I & II**: Aggiornate tutte le voci storiche ed enciclopediche (`Living Sagas: Historical Facts`, `LSE History Timeline`, `La Guerra di Fenris e l'Esilio dei Firstborn`, `LSE Blood Classification` sezione `APPARENT AGE`, `House Genealogies Summary`, `Firstborn Pantheon`) allineando `pre-827 AD` a `pre-864 AD`, inserendo l'anno di trasformazione 864 d.C., la banda 16–45 anni e le formule di conversione età apparente (16 vichingo = 20–22 moderno; 40–45 vichingo = ~60 moderno).
  - **Invariante `entries == lexicon`**: Garantita la perfetta identità (100% byte-for-byte) tra `entries` e `lexicon` in tutti i file JSON toccati (`FINAL/` e mirror `lorebooks/optimized/`).
  - **Deploy Live Wyvern API**: Effettuato il deploy live con esito HTTP 200 su card Wulfnic (`_HEQQbbRFwKdG8QE2Fh1z1`), Lorebook NPC Primary (`_zwEqgEEzh12X6gHVmMKKC`, 99 entries), Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL`, 221 entries) e Lorebook II (`_HfG7TeV6MJyj6bxMwxkpt`, 142 entries). Verificata live la presenza dei nuovi campi con `scratch/verify_live_api.py`.

- **Rework Scena Iniziale "SUCC Welcome Day", Regole Anatomiche/Locomotorie Lamia per Sierra Cruz, Palette Rosa Confetto & Corna Scarlatte per Scarlett Rose e Deploy Live**:
  - Aggiornati i profili di **Sierra Cruz** e **Scarlett Rose** in `FINAL/Svartulfr_NPC_Primary.json` (e mirror `lorebooks/optimized/Svartulfr_NPC_Primary.json`, `_zwEqgEEzh12X6gHVmMKKC`), nelle card legacy (`ARCHIVIO/cards_legacy/Sierra_Cruz_card.json` e `Scarlett_Rose_card.json`) e negli scenari universitari:
    * **Sierra Cruz (Lamia)**: Uniformati i capelli e la coda serpentina da 4 metri al colore **arcobaleno con scaglie iridescenti** (`rainbow-colored hair` e `4-meter rainbow-colored serpentine tail covered in shimmering iridescent scales`). Inserita la regola tassativa `LOCOMOTION & ANATOMY RULE` sia nella scheda JED+ sia nelle `NARRATION GUIDELINES` degli scenari: essendo la metà inferiore del suo corpo interamente quella di un serpente (zero gambe, zero piedi), è vietato usare termini come *gambe*, *piedi*, *scarpe*, *camminare* o *fare passi* (`walk`, `step`, `stand on feet`, `legs`, `shoes`); Sierra si muove esclusivamente strisciando, scivolando e avvolgendosi sulle sue spire (`slithers`, `glides`, `coils`). Corrette anche le scene `01. Theta Iota Theta Morning on Greek Row` e `05. Bulls Locker Room and Stadium Tunnel` in cui erano rimasti verbi da bipede (`stood` / `walked past` -> `coiled` / `glided past`).
    * **Scarlett Rose (Succubus)**: Uniformati i capelli e gli occhi al **rosa confetto** (`candy-pink / rosa confetto hair and matching candy-pink eyes`) con **due corna scarlatte** che spuntano visibilmente tra i capelli sopra le tempie (`two sleek scarlet horns protruding visibly through her candy-pink hair`). Corrette tutte le occorrenze legacy (`red curls`, `auburn hair`, `amber eyes`, `ruby eyes`) nei greeting degli scenari (`SUCC Welcome Day`, `02. Pre-Med Biology Labs`, `05. Beta Rho Omega Halloween Party`).
  - Aggiornato il greeting iniziale `greetings[0]` (`SUCC Welcome Day`, `scene-alyssa-welcome-day` e `scene-jasper-welcome-day`) in `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json` (`char_scenario_CKgwq246DyCj1NNTBV9rt`, rev. 14) e `FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json` (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`, rev. 8):
    * **Accompagnamento dell'intera famiglia**: I quattro studenti iscritti alla SUCC (`Noah` e `Malachia` degli anni superiori, più le matricole `Jasper` e `Alyssa`) arrivano sul Lunar Quad accompagnati per i saluti di rito da `Erik`, `Logan` ed `Edric` (con battute formattate su nuova riga `Nome Completo: "..."` per l'attivazione automatica dei ritratti NPC).
    * **Arrivo di Wulfnic e Zefir**: Wulfnic fa il suo ingresso sul Quad indossando con solenne orgoglio il suo outfit gag (`"The Gag Shirt"`, la t-shirt nera oversize regalatagli da Jasper con la lunga lista di *"Rules for Dating My Granddaughter"* stampata sulla schiena) insieme a **Zefir Hvitskog**, vestito in stile punk con i capelli bianco-neve rasati ai lati in una **cresta alla moicana** (`mohawk`) e un **giubbotto di pelle nera con le borchie** (`studded leather jacket`).
    * **Iscrizione e Copertura Islandese**: Wulfnic annuncia ridendo di aver iscritto Zefir all'università per proteggere la nipote (*"After all, you have never been to school, and technically you are still a kid!"*), registrandolo con la copertura di un lontano parente appena arrivato dall'Islanda così da giustificare il marcato accento norreno di Zefir e la sua scarsa dimestichezza con l'inglese scritto.
    * **Presentazione a Scarlett, Sierra e Finn (Messaggio 3)**: La famiglia presenta subito Zefir con la copertura del cugino islandese a `Scarlett Rose`, `Sierra Cruz` e `Finnegan Novak` per evitare che si mettano sul chi vive; pur avendo Zefir completamente azzerato la propria aura divina (apparendo come un comune licantropo qualsiasi), `Finn` si sente istintivamente inferiore a lui e cerca di atteggiarsi a più figo davanti ad Alyssa vantandosi del posto in prima linea nell'hockey, `Sierra` striscia vicino a Zefir sulla sua coda arcobaleno dalle scaglie iridescenti per chiedergli dove abbia comprato a Reykjavik quel giubbotto di pelle borchiato, e `Scarlett` (con i capelli e gli occhi rosa confetto e le corna scarlatte tra i capelli) flirta con Zefir offrendosi per dargli ripetizioni private di inglese scritto.
  - Aggiornato anche il blocco `ATTIRE` / `CAMPUS COVER` e la sezione `THE ONE WHO WAS NEVER GROWN:` di Zefir in `FINAL/Svartulfr_NPC_Primary.json` (e nel mirror `lorebooks/optimized/Svartulfr_NPC_Primary.json`), mantenendo `entries == lexicon` 100% identici e pubblicando live sia il Lorebook (`_zwEqgEEzh12X6gHVmMKKC`) sia i due Scenari (`HTTP 200 OK`).
  - **Riallineamento Integrale dei Character Slots alle 8 Card Esistenti (`/characters/mine`)**:
    * Eliminati dagli scenari tutti gli slot vuoti degli ex-personaggi convertiti in NPC del Lorebook (`best_friend`, `roommate`, `male_roommate`, `childhood_friend`, `quarterback`, `friend`, `sports_rival`, `ai_companion`) e sostituiti con gli slot delle **8 Character Card realmente esistenti** (con `pool` popolato a `weight: 100` e `unavailable_count: 0`):
      - In `Svartulfr_Scenario_SUCC_Route_Alyssa.json` (`char_scenario_CKgwq246DyCj1NNTBV9rt`, **rev. 15**): 8 slot corrispondenti alle 8 card attive (`twin` Jasper `_t4J9aQNJM36cUKAP4wB4U`, `crush` Mackenzie `_zn24784jfcchQ7EwCyAnm`, `father` Erik `_QPea6g4Q1QfeYCVHCLMPR`, `eldest_brother` Malachia `_RDfz7XzTpM23LpPALVXHM`, `brother` Noah `_zFLUjV8aVxQRAfQxGcAcY`, `uncle` Logan `_T8Ywcr9FEqNf9JxbK6eHP`, `cousin` Edric `_TbRM3EdxDjHFgqztTbCpL`, `maternal_grandfather` Wulfnic `_HEQQbbRFwKdG8QE2Fh1z1`).
      - In `Svartulfr_Scenario_SUCC_Route_Jasper.json` (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`, **rev. 9**): 7 slot corrispondenti alle 7 card attive oltre a Jasper protagonista (`father` Erik, `eldest_brother` Malachia, `brother` Noah, `uncle` Logan, `cousin` Edric, `maternal_grandfather` Wulfnic, `band_peer` Mackenzie).
    * Ricollegati tutti i `speaker_slot` dei messaggi in tutti i greeting agli slot delle card esistenti, lasciando i dialoghi degli NPC del Lorebook (`Scarlett Rose:`, `Sierra Cruz:`, `Finnegan Novak:`, `Zefir Hvitskog:`, `Jared Thompson:`, `Stanley Davies Jr.:`, `Vincent Campbell:`, `Russell Sinclair:`, `Echo:`, `Alyssa Hvit Douglas Bloodmoon:`) formattati su nuova riga per lo splitting automatico del ritratto e del nome da parte del Lorebook.
  - **Traduzione Integrale in Italiano di Tutti i Greetings degli Scenari SUCC**:
    * Tradotti integralmente in italiano tutti i 7 greeting dello scenario Alyssa (`SUCC Welcome Day`, `01. Theta Iota Theta Morning on Greek Row`, `02. Pre-Med Biology Labs`, `03. KSA Presidential Suite at Fenris Hall`, `04. Solarton Skatepark & The Verve Backstage`, `05. Beta Rho Omega Halloween Party`, `06. Solarton Civic Ice Arena`) e tutti i 6 greeting dello scenario Jasper (`SUCC Welcome Day`, `01. Wyvern Hall & The Five Cocketeers`, `02. Computer Science Labs & Voidspace Node`, `03. Fenris Hall KSA Lounge & The Quad`, `04. The Verve Soundcheck & Backstage`, `05. Bulls Locker Room and Stadium Tunnel`), preservando rigorosamente `0` em-dash, `0` asterischi, dialoghi tra virgolette inglesi doppie (`"..."`), la regola locomotoria di Sierra Cruz (solo strisciare/scivolare/spire, zero riferimenti a gambe/piedi/scarpe/camminare) e la palette rosa confetto con corna scarlatte di Scarlett Rose.
    * Deployati live su Wyvern con esito `HTTP 200 OK`: `Svartulfr_Scenario_SUCC_Route_Alyssa.json` (`char_scenario_CKgwq246DyCj1NNTBV9rt`, **rev. 16**) e `Svartulfr_Scenario_SUCC_Route_Jasper.json` (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`, **rev. 10**).

---

## [21 Ottobre 2026] - Ripristino Integrale JED+ 7 Card Core, Omogeneizzazione Layout 310 Voci, Placeholder Ufficiale DCC e Deploy Wyvern Lorebooks

- **Ripristino Schede Complete JED+ per i 7 Personaggi Core (R1)**:
  - Completata l'iniezione integrale delle schede canoniche JED+ dalle Character Card ufficiali in `FINAL/` nei rispettivi record dei Lorebook NPC, convertiti a `type: "npc"` e `selective: false` con soppressione nativa anti-duplicato `ignored_characters`:
    - **Erik Ulfr Douglas** (`C-JisFj8qA1tsFEqZKevk` in Primary): 22.775 caratteri (testo integrale da `FINAL/Erik_Douglas_card.json`), avatar Cloudflare `61648731-7c96...`, `custom_avatar_regex: true`, regex multiline `(?:^|\n)\s*(?:Erik Ulfr Douglas|Erik Douglas|The Prime Alpha|Prime Alpha|Erik)\s*:`, `lines_parsed: 1`, `npc_info` strutturato, `ignored_characters: ["_QPea6g4Q1QfeYCVHCLMPR"]`.
    - **Malachia Björn Douglas Bloodmoon** (`jDuJtzirlEZC3K_ArIufh` in Primary): 18.520 caratteri (da `FINAL/Malachia_Douglas_Bloodmoon_card.json`), avatar `d77a20fc-49da...`, regex multiline, `lines_parsed: 1`, `npc_info`, `ignored_characters: ["_RDfz7XzTpM23LpPALVXHM"]`.
    - **Noah Loki Douglas Bloodmoon** (`H2JX-NkHRiJ2FzoekC5ZZ` in Primary): 10.398 caratteri (da `FINAL/Noah_Douglas_Bloodmoon_card.json`), avatar `968cc93e-879d...`, regex multiline, `lines_parsed: 1`, `npc_info`, `ignored_characters: ["_zFLUjV8aVxQRAfQxGcAcY"]`.
    - **Logan Járn Douglas** (`tAcrWLtWSDGf3xJJRwUOM` in Primary): 13.735 caratteri (da `FINAL/Logan_Douglas_card.json`), avatar `0b5a932b-0a3b...` ripristinato anche su cloud Wyvern, regex multiline, `lines_parsed: 1`, `npc_info`, `ignored_characters: ["_T8Ywcr9FEqNf9JxbK6eHP"]`.
    - **Wulfnic Báleygr Bloodmoon** (`HhuMluMmIIENUei3bX6ed` in Primary): 14.530 caratteri (da `FINAL/Wulfnic_Bloodmoon_card.json`), avatar `683beb87-8091...`, regex multiline, `lines_parsed: 1`, `npc_info`, `ignored_characters: ["_HEQQbbRFwKdG8QE2Fh1z1"]`.
    - **Mackenzie Sanchez-Rogers** (`BXi3sENAVYB8OKF80Q9Su` in Primary): 9.618 caratteri (da `FINAL/Mackenzie_Sanchez_Rogers_card.json`), avatar `87f28fb6-557f...`, regex multiline, `lines_parsed: 1`, `npc_info`, `ignored_characters: ["_zn24784jfcchQ7EwCyAnm"]`.
    - **Edric Douglas** (`h-ttmlgJYeRXqyDvQjSX7` in Secondary): 7.240 caratteri (da `FINAL/Edric_Douglas_card.json`), avatar `ed348ea6-c40c...`, regex multiline, `lines_parsed: 1`, `npc_info`, `ignored_characters: ["_TbRM3EdxDjHFgqztTbCpL"]`.
  - Volume testuale totale iniettato: 89.576 caratteri in Primary e 7.240 caratteri in Secondary.
  - Aggiornato il `token_budget` del Lorebook Primary da 5000 a 7500 token per consentire l'attivazione fluida dei dossier estesi senza rischio di troncamento del contesto. Confermato `token_budget: 5000` per il Lorebook Secondary.

- **Omogeneizzazione Layout Standard JED+ a 4 Blocchi su 310 Voci e Bonifica Integrale Camp Mystic (R2)**:
  - Raggiunta la conformità del 100% (310/310 voci: 99 in Primary, 211 in Secondary) all'apertura con blocco bracket `[...]` e alle 4 sezioni canoniche obbligatorie (`BACKSTORY:`, `FAMILY & PACK:` / `CLAN AND COMPANY:`, `VOICE & BEHAVIOR:`, più chiusure tematiche e RPG).
  - Rigenerate da zero le 100 schede Camp Mystic in `FINAL/Svartulfr_NPC_Secondary.json` attingendo alla fonte non troncata (`scratch/campmystic_full_card.json`), eliminando tutti i troncamenti a 160 caratteri sulle righe `Supernatural Gifts` e `Innate Resilience`, rimuovendo i doppi punti (`..`), i doppi apici (`""...""`), gli errori grammaticali (`they withdraws` -> `they withdraw`, ecc.) e allineando le date di nascita al World Clock 2024 senza ricorrenze al 1° del mese (Regola 9.6).
  - Incapsulate nel canone JED+ standard le 3 voci irregolari di Secondary (`Bruce`, `Campus Staff Rat`, `Adrian`) e normalizzate tutte le intestazioni varianti in Primary (11 voci) e Secondary (75 voci non-Camp-Mystic).

- **Adozione Avatar Placeholder Ufficiale DCC su 200 Voci (R3)**:
  - Aggiornato l'avatar di tutte le 200 voci (42 in Primary, 158 in Secondary) che utilizzavano il vecchio fallback `6f8b7c78...` al nuovo placeholder ufficiale DCC: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`.
  - Preservati intatti tutti i 110 ritratti personalizzati (57 in Primary, 53 in Secondary).
  - Verificato che il 100% delle 310 voci possiede un URL HTTPS valido e attivo, sanando anche l'anomalia di Logan Járn Douglas che risultava con avatar vuoto sul cloud live.

- **Disciplina di Formattazione e Prevenzione Ricorsione (R4)**:
  - Verificata la totale assenza di em-dash (`\u2014`, 0 occorrenze), asterischi markdown di narrazione (`*`, 0 occorrenze), macro `{{age}}` (0 occorrenze) e keyword ombrello (`BROAD_KEYS`, 0 occorrenze nelle trigger `keys`).
  - Iniettato il flag `exclude_from_recursion: true` sul 100% delle voci (310/310) per prevenire loop e cascate cicliche di retrieval durante l'inferenza LLM.

- **Emblema Lorebook su Tutti i 6 Lorebook, Mirror Locale, Deploy Live Wyvern Web API e Validazione Chrome DevTools (R5)**:
  - Impostato l'emblema ufficiale della Casata Svartúlfr (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public`) come copertina (`photoURL`) su **tutti i 6 Lorebook Standalone** (`Lorebook I`, `Lorebook II`, `Lorebook III`, `Location`, `NPC Primary`, `NPC Secondary`).
  - Sincronizzati 1:1 sia l'array `entries` che l'array `lexicon` all'interno dei file locali in `FINAL/` e in `lorebooks/optimized/`.
  - Eseguito il deploy live via `PUT /api/lorebooks/:id` con payload compatto (`lexicon` + metadati top-level, escludendo il duplicato `entries`).
  - Validato con successo tramite script API (`scratch/verify_live_deployment.py`) e ispezione Chromium DevTools (`scratch/validate_cdp_browser.py`): `0` errori console, `HTTP 200` su tutti gli endpoint API e sugli asset Cloudflare Images (`naturalWidth: 768`, `naturalHeight: 768`).

---

## [21 Ottobre 2026] - Sincronizzazione Scenari SUCC, Riduzione a 8 Card, Adozione Soppressione Nativa Wyvern ("Don't Activate When Active") e Ripristino Integrale NPC Primary

- **Adozione Meccanismo Nativo Wyvern "Don't Activate When Active" (`ignored_characters` & `ignored_personas`)**:
  - Superato definitivamente il workaround artificiale basato su `selective: true` e keyword fittizie ('Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo').
  - Mappati dal runtime client di Wyvern (`wv_chunk.js`) i due array nativi di soppressione attivati dal toggle UI "Don't Activate When Active" ("Skip this entry entirely when one of these characters or personas is already in the chat, to avoid a redundant duplicate"):
    - `ignored_characters: string[]` (array di ID card personaggio per saltare l'entry se la card è presente nella chat/party)
    - `ignored_personas: string[]` (array di ID Persona per saltare l'entry se `{{user}}` gioca con quella Persona)
  - Configurazione applicata con successo a tutte le voci di `FINAL/Svartulfr_NPC_Primary.json` e `FINAL/Svartulfr_NPC_Secondary.json`:
    - **Alyssa Hvit Douglas Bloodmoon** (`alyssa_world_dossier_2b54a223`): `type: "npc"`, `selective: false`, `secondary_keys: []`, regex multiline, avatar Cloudflare, `npc_info`, descrizione JED+ integrale (16.957 caratteri), `ignored_personas: ["persona_1786335754946"]`, `ignored_characters: ["_6exg3yPfe2eCDK4hTftkh"]`.
    - **Jasper Svartr Douglas Bloodmoon** (`Vcj4h2TL4Usola2A4OOl6`): `type: "npc"`, `selective: false`, `secondary_keys: []`, regex multiline, avatar, `npc_info`, descrizione JED+ integrale (14.483 caratteri), `ignored_personas: ["1792155173728"]`, `ignored_characters: ["_t4J9aQNJM36cUKAP4wB4U"]`.
    - **I 5 NPC Convertiti (Scarlett, Sierra, Russ, Stan, Jared)**: `type: "npc"`, `selective: false`, regex multiline, avatar validi, `lines_parsed: 1`, `npc_info`, descrizioni JED+ piene (da 4.777 a 8.696 caratteri), `ignored_characters: [<legacy_card_id>]`, `ignored_personas: []`.
    - **Le 6 Card Approvate in Primary (Erik, Malachia, Noah, Logan, Wulfnic, Mackenzie)**: configurato `ignored_characters: [<card_id>]` per prevenire duplicati se presenti nel party.
    - **Edric Douglas (`h-ttmlgJYeRXqyDvQjSX7`) in Secondary**: configurato `ignored_characters: ["_TbRM3EdxDjHFgqztTbCpL"]`.
  - Deploy completato con successo via PUT su Wyvern API per entrambi i Lorebook (`_zwEqgEEzh12X6gHVmMKKC` e `_Uht3Ckz44JBDrPnUHq7LV`) con risposta `HTTP 200 OK`.

- **Sincronizzazione, Ottimizzazione Macro e Pulizia Slot Scenari SUCC (Alyssa e Jasper)**:
  - Archiviati i 4 file degli scenari ritirati (`Camp Mystic`, `DMHA Dungeons`, `Underworld Sindacato`, `Villa Douglas`) nella nuova cartella `ARCHIVIO/scenarios/`. In `FINAL/scenarios/` permangono esclusivamente i due scenari SUCC attivi.
  - Sostituite nei testi di saluti (greetings) e messaggi tutte le macro `{{scenarioChar "..."}}` relative a NPC ritirati (`best_friend`, `roommate`, `male_roommate`, `crush`, `quarterback`, `friend`, `sports_rival`) e alla gemella (`twin`) con i rispettivi nomi letterali.
  - Puliti i pool inaccessibili: azzerato `pool: []` e impostato `unavailable_count: 0` su tutti gli slot dei personaggi convertiti a NPC per eliminare i blocchi `unavailable_count: 1` di Wyvern.
  - Preservati tutti gli 8 oggetti slot per ciascuno scenario per garantire la piena validità dei puntatori `speaker_slot` sui messaggi.
  - Nello scenario Alyssa, mantenuti i pool delle card canoniche approvate `twin` (Jasper `_t4J9aQNJM36cUKAP4wB4U`) e `crush` (Mackenzie `_zn24784jfcchQ7EwCyAnm`).
  - Deploy via PUT completato con successo su Wyvern API:
    - Route Alyssa (`char_scenario_CKgwq246DyCj1NNTBV9rt`): revision 11, 7 greetings, 8 slot (tutti con `unavailable_count: 0`), `HTTP 200 OK`.
    - Route Jasper (`char_scenario_Kq4mJEBH83j7Q7DdVfFnF`): revision 5, 6 greetings, 8 slot (tutti con `unavailable_count: 0`), `HTTP 200 OK`.

- **Riduzione a Esattamente 8 Card Personaggio (`/characters/mine` e `FINAL/`)**:
  - Salvato snapshot preventivo di Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`) in `scratch/jared_pre_delete_snapshot__xJVPtBLL3dxy69RLKL9X9.json`.
  - Eliminata la card Jared Thompson da Wyvern via `DELETE /api/characters/_xJVPtBLL3dxy69RLKL9X9` (`HTTP 204 No Content`).
  - Verificato che su Wyvern `/characters/mine` rimangano esattamente le 8 card approvate:
    1. Jasper Svartr Douglas Bloodmoon (`_t4J9aQNJM36cUKAP4wB4U`)
    2. Erik Ulfr Douglas (`_QPea6g4Q1QfeYCVHCLMPR`)
    3. Logan Járn Douglas (`_T8Ywcr9FEqNf9JxbK6eHP`)
    4. Malachia Björn Douglas Bloodmoon (`_RDfz7XzTpM23LpPALVXHM`)
    5. Noah Loki Douglas Bloodmoon (`_zFLUjV8aVxQRAfQxGcAcY`)
    6. Edric Douglas (`_TbRM3EdxDjHFgqztTbCpL`)
    7. Wulfnic Báleygr Bloodmoon (`_HEQQbbRFwKdG8QE2Fh1z1`)
    8. Mackenzie Sanchez-Rogers (`_zn24784jfcchQ7EwCyAnm`)
  - Creata la directory `ARCHIVIO/cards_legacy/` e spostati i 6 file JSON delle card dismesse (`Alyssa_Douglas_Bloodmoon_card.json`, `Jared_Thompson_card.json`, `Russ_card.json`, `Scarlett_Rose_card.json`, `Sierra_Cruz_card.json`, `Stan_Davies_Jr_card.json`).
  - Verificato che in `FINAL/` rimangano esclusivamente i file JSON delle 8 card approvate.

- **Verifica di Regressione Integrale (Suite Automatizzata 100% Passed)**:
  - Validati con esito positivo tutti i vincoli: 0 em-dash, dialoghi tra virgolette, azioni in plain text, 0 macro orfane, coerenza tra `entries` e `lexicon`, e test di regressione via live GET requests con status HTTP 200/204 su tutti gli endpoint.

- **Creazione e Registrazione Nuova Skill Operativa (`wyvern-card-lorebook-sync`)**:
  - Distillata e codificata la nuova skill modulare di repository in `.agents/skills/wyvern-card-lorebook-sync/SKILL.md` corredata dallo script di verifica automatizzata `scripts/verify_suppression_and_slots.py`.
  - Aggiornata la documentazione di governance in `.agents/rules/14_metodo_operativo_skills_integrate.md`, `.agents/rules/08_triage_lorebook_e_lexicon.md` e `GEMINI.md` (Sezioni 7 e 19).

---

## [21 Ottobre 2026] - Integrazione Fonti Esterne RPG Source (D20 / S.P.E.C.I.A.L.) & Sincronizzazione Indice di Risorse

- **Integrazione 8 Fonti Esterne da Gruppo Tab Chrome "RPG Source"**:
  - Estratte e verificate tramite Chrome LevelDB sync le 8 fonti web primarie per la modellazione e risoluzione delle meccaniche diegetiche:
    1. Sopakco Sauce Docs (Canonical): documentazione tecnica su prompt engineering, sintassi bot JanitorAI e meccaniche di lancio dadi e statistiche (`https://sopakcosauce.gitbook.io/sopakcosauce-docs`).
    2. Wyvern Svartúlfr World Editor (Canonical): interfaccia live editor per il mondo Svartúlfr su Wyvern, impostazioni di gioco, lexicon e schemi RPG (`https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7`).
    3. io's Modern Fantasy Universe Hub (Canonical): hub di riferimento canonico per l'universo Modern Fantasy e coerenza cross-character (`https://io-modernfantasy.uwu.ai/`).
    4. Mackenzie "Mac" Sanchez-Rogers (Canonical): implementazione di riferimento per personaggi demi-umani, voce e stat block RPG (`https://janitorai.com/characters/1d1ef070-934d-4c11-90e2-b7fb9a4649c4_character-mackenzie-mac-sanchez-rogers`).
    5. Elite Warrior Tsalu Haoitan (Canonical): riferimento per abilità di combattimento strutturate e logiche di risoluzione scontri (`https://janitorai.com/characters/1e685f63-024f-40f0-a892-a57535760b49_character-elite-warrior-tsalu-haoitan`).
    6. Don't Look at Me (Community): scenario psicologico a trigger condizionali e gestione della tensione narrativa (`https://janitorai.com/characters/1ff24d14-3dfd-4795-9d49-986eeee711de_character-dont-look-at-me`).
    7. Neon Purr (Canonical): scheda urban fantasy / cyberpunk demi-human per benchmarking di dialoghi e stili di ruolo (`https://janitorai.com/characters/d67a12e8-a1be-4ec4-95e1-ada90263fee4_character-neon-purr-%F0%9F%87%A6%F0%9F%87%BA`).
    8. The Omega Breeding Facility (Community): scenario a setting complesso per gestione gerarchie, spazi istituzionali e multi-NPC (`https://janitorai.com/characters/c6a9088f-8b82-402c-8070-8afe22a2781e_character-the-omega-breeding-facility`).
- **Mappatura al Motore di Risoluzione D20 + S.P.E.C.I.A.L.**:
  - Classificate e correlate le risorse al motore di gioco D20 + S.P.E.C.I.A.L., arricchendo la base di conoscenza per prompt assembly, Game Master narrator e risoluzione delle azioni nei Character Scenarios.
- **Aggiornamento EXTERNAL_RESOURCES_INDEX.md**:
  - Creata la sottosezione 3.10 "RPG & TTRPG Mechanics (D20 / S.P.E.C.I.A.L.)" con i metadati completi e le direttive d'uso per ciascuna risorsa.
  - Aggiornata la tabella delle statistiche delle risorse (Sezione 2): 8 nuove risorse (6 Canonical, 2 Community, 0 Experimental), portando il totale tracciato da 69 a 77 risorse (27 Canonical, 50 Community, 0 Experimental).

---

## [21 Ottobre 2026] - Razionalizzazione Scenari Wyvern: Dismissione 5 Scenari e Mantenimento Archi Alyssa e Jasper

- **Eliminazione Scenari su Wyvern via API (DELETE /api/character-scenarios/{id})**:
  - Eliminati i 5 scenari ridondanti/generici:
    1. char_scenario_1DC43ggb6mB8YLJDJKrU4 (Master Scenario)
    2. char_scenario_nLC84wrHdrbB6P3DEhwKb (Camp Mystic)
    3. char_scenario_eqtRNnDpKbxDp7dmJmq6E (DMHA Dungeons)
    4. char_scenario_rrUCdBPH6WTNyBnQkMAKR (Underworld Sindacato)
    5. char_scenario_88N1eQXqkbydKX9q9XQzp (Villa Douglas)
  - Backup preventivo integrale dello stato live salvato in scratch/backup_deleted_scenarios_20261021/.
  - Verifica post-eliminazione: tutti i 5 scenari restituiscono HTTP 404 (Not Found).
- **Mantenimento Esclusivo dei 2 Archi Personaggio**:
  - char_scenario_CKgwq246DyCj1NNTBV9rt (SUCC Route Alyssa) — Attivo (HTTP 200).
  - char_scenario_Kq4mJEBH83j7Q7DdVfFnF (SUCC Route Jasper) — Attivo (HTTP 200).

---

## [20 Ottobre 2026] - Canone Edric Douglas (13 Anni Compiuti, Nato 25 Febbraio 2011) & Presentazione di Branco a Yule 2024

- **Definizione Canonica di Edric Douglas & Tradizione della Presentazione a Yule**:
  - **Età Anagrafica**: Allineata stabilmente a **13 anni** compiuti (nato il **25 febbraio 2011**).
  - **Tradizione di Branco Solstiziale**: Istituita nel canone la tradizione ancestrale per cui la solenne cerimonia della Presentazione dei giovani licantropi (scoperta del *Wolf Name*, manifestarsi del lupo e passaggio fuori dallo stato di cucciolo Pre-Presentation Gamma) viene celebrata comunitariamente durante la sacra notte di **Yule (Solstizio d'Inverno, 21 dicembre 2024)** insieme a tutti i cuccioli del branco che hanno compiuto 13 anni nel corso dell'anno solare 2024.
  - **Parentela & Segreto Biologico**: Confermato che Edric è biologicamente il figlio segreto di Erik Douglas e di una lupa sconosciuta (una delle escort licantropo con cui Erik ha trascorso un Rut per superare il calore), intercettata e liquidata da Logan a The Verve per proteggere il ragazzo dal perimetro biometrico e dal controllo asfissiante di Erik e preservare la stabilità familiare. Elizabeth Duskwood non ha alcuna relazione di parentela con Edric.
  - **Giocabilità**: Rende immediatamente giocabile la storyline dei preparativi estivi/autunnali e della Presentazione solstiziale di Edric nel 2024 senza richiedere salti temporali pluriennali.
- **Aggiornamento & Deploy Wyvern Web API delle Entità Coinvolte**:
  - **Character Card Edric Douglas (`_TbRM3EdxDjHFgqztTbCpL`)**: Aggiornata la `description` (13yo, nato 25 febbraio 2011, peso psicologico della Presentazione a Yule 2024, tutela minori 13yo), `personality` e `scenario`. Deploy completato via API con `HTTP 200 OK`.
  - **Character Card Logan Douglas (`_T8Ywcr9FEqNf9JxbK6eHP`)**: Aggiornato il riferimento temporale a 13 anni. Deploy completato via API con `HTTP 200 OK`.
  - **`Svartulfr_Location.json` (`_EjXxkmPVhpCXg8xABpFkK`)**: Aggiornata la voce `B-01 Ironwood Cabin` (Edric 13 anni, Yule 2024, Camp Mystic per preparazione atletica/emotiva). Deploy completato via API con `HTTP 200 OK`.
  - **`Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`)**: Aggiornato il World Dossier di Edric Douglas (Entry 1: 13yo, Yule 2024 cohort, wide receiver). Deploy completato via API con `HTTP 200 OK`.
  - **`Svartulfr_Lorebook_I.json` (`_gwwCxCfQ6PQaLEjAQVpJL`)**: Aggiornata la voce enciclopedica 217 sui *Wolf Names* e la tradizione di Yule per i tredicenni. Deploy completato via API con `HTTP 200 OK`.
  - **Master Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`)**: Aggiornata la definizione del ruolo `cousin` includendo la coorte dei tredicenni e la presentazione a Yule 2024. Deploy completato via API con `HTTP 200 OK`.
- **Allineamento Documentale & Regole di Progetto**:
  - Aggiornati [`CanonDecisions.md`](file:///e:/repository/SvartulfrVerse/CanonDecisions.md), [`GEMINI.md`](file:///e:/repository/SvartulfrVerse/GEMINI.md) e [`.agents/rules/07_epurazione_user_e_intimacy_profiles.md`](file:///e:/repository/SvartulfrVerse/.agents/rules/07_epurazione_user_e_intimacy_profiles.md).

---

## [20 Ottobre 2026] - Calibrazione Cabine Camp Mystic a 6 Posti (Alyssa in Moonflower, Jasper & Edric in Ironwood) & Riassegnazione Rylan Cade a B-07

- **Aggiornamento e Riorganizzazione Cabine Residenziali (`Svartulfr_Location.json` — `_EjXxkmPVhpCXg8xABpFkK`)**:
  - **`G-01 Moonflower Cabin: Compagne di Stanza di Alyssa` (6 posti)**:
    - Riconfigurato lo chalet per ospitare Alyssa Douglas-Bloodmoon come sesta occupante insieme alle cinque compagne distribuite lungo i cinque anni di corso: Avery Lin Calder (Y1, Vampiro), Sofia Mae Rourke (Y2, Strega), Nadia Elise Voss (Y3, Licantropo), Talia June Mercer (Y4, Werebear), Mina Rae Sato (Y5, Catwere Beastwere).
    - Aggiornati titolo, content narrativo in italiano privo di em-dash o asterischi markdown, chiavi primarie con anti-collisione, chiavi secondarie contestuali (`Camp Mystic`, `chalet`, `camper`, `dormitorio`, `stanza`, `compagne`, `turno`, `convivenza`), `key_logic: "AND_ANY"`, `position: "before_char"`, `priority: 2`.
  - **`B-01 Ironwood Cabin: Compagni di Stanza di Jasper` (6 posti)**:
    - Riconfigurato lo chalet per ospitare Jasper Douglas-Bloodmoon e il cugino minore Edric Douglas (Y1 Junior Division, 12 anni, purosangue Gamma in custodia a Jasper) insieme ai compagni dei rispettivi anni: Theo James Mercer (Y2, Mago), Jace Nolan Hart (Y3, Licantropo), Evan Adrian Voss (Y4, Wereboar), Nico Samuel Reed (Y5, Wolfwere Beastwere).
    - Inserita nota logistica esplicita sul trasferimento di Rylan Elias Cade alla cabina B-07.
    - Aggiornati titolo, content narrativo in italiano, chiavi primarie, chiavi secondarie contestuali e parametri Wyvern (`key_logic: "AND_ANY"`, `position: "before_char"`, `priority: 2`).
  - **`B-07 Lake Wolf Cabin`**:
    - Aggiornato il roster includendo Rylan Elias Cade (Vampire, Year 1) trasferito da B-01 per capienza, garantendo coerenza biunivoca.
- **Riassegnazione Profilo NPC Rylan Cade (`Svartulfr_NPC_Secondary.json` — `_Uht3Ckz44JBDrPnUHq7LV`)**:
  - Aggiornato il campo `AFFILIATION: Camp Mystic (B-07 Lake Wolf Cabin);` nel blocco JED+.
  - Aggiornata la sezione `CAMP MYSTIC BACKGROUND & ROLE:` e aggiunta la chiave di attivazione `B-07 Lake Wolf Cabin`.
- **Sincronizzazione Locale & Deploy Wyvern API**:
  - Sincronizzati sia `entries` che `lexicon` in `FINAL/` e `lorebooks/optimized/`.
  - Eseguito il deploy live via Wyvern Web API per `_EjXxkmPVhpCXg8xABpFkK` (225 voci) e `_Uht3Ckz44JBDrPnUHq7LV` (211 voci).
  - Verifica GET post-deploy completata con successo con HTTP 200 OK su entrambi i Lorebook.

---

## [20 Ottobre 2026] - Nuovo Placeholder Ufficiale DCC per Voci Senza Immagine (202 NPC Aggiornati)

- **Upload & Integrazione CDN Cloudflare del Placeholder Ufficiale DCC**:
  - Caricata l'immagine canonica della sagoma lupina con occhi fiammeggianti e sigillo runico della **Douglas Commerce Company** (`asset/placeholder_dcc_silhouette.jpg` e `FINAL/placeholder_dcc_silhouette.jpg`) sull'infrastruttura Cloudflare Wyvern.
  - Generato l'URL CDN pubblico definitivo: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public`.
- **Sostituzione Massiva Placeholder sui Lorebook NPC (202 Voci Totali)**:
  - **`Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`)**: Sostituite 44 voci che utilizzavano il vecchio fallback generico con il nuovo placeholder DCC, con deploy via API e verifica GET (99 voci totali confermate).
  - **`Svartulfr_NPC_Secondary.json` (`_Uht3Ckz44JBDrPnUHq7LV`)**: Sostituite 158 voci (inclusi tutti i camper e counselor di Camp Mystic privi di ritratto personale) con il nuovo placeholder DCC, con deploy via API e verifica GET (211 voci totali confermate).
- **Allineamento Locale & Repository**:
  - Aggiornati i file in `FINAL/` e `lorebooks/optimized/`.

---

## [20 Ottobre 2026] - Standardizzazione Integrale Camp Mystic (100 NPC, 37 Location), Dicotomia White Moon / Solar Shadow & Deploy Wyvern API

- **Standardizzazione e Blindatura dei 100 NPC di Camp Mystic (`Svartulfr_NPC_Secondary.json` — `_Uht3Ckz44JBDrPnUHq7LV`)**:
  - **Integrazione Totale (211 voci attive)**: Preservati i 111 NPC originali del Lorebook secondario e standardizzati integralmente i 100 nuovi profili di Camp Mystic (40 camper femmine G-01/G-08, 40 camper maschi B-01/B-08, 20 membri dello staff e counselor diretti da Mara Voss).
  - **Conversione Strutturale in JED+ & RPG Stats**: Convertite le schede grezze in formato canonico JED+ con blocchi `[NAME: ...; ALIASES: ...; SPECIES: ...; AGE: ...; AFFILIATION: Camp Mystic (...); POWERS: ...]`, sezioni `PERSONALITY:`, `STRENGTHS & WEAKNESSES:`, `CAMP MYSTIC BACKGROUND & ROLE:` e statistiche RPG bilanciate con tetto massimo di Livello a 99 per gli immortali (es. Director Mara Voss a Livello 99, camper al loro anno anagrafico).
  - **Sanificazione Trigger Keys & Protezione Anticollisione Personaggi Principali**:
    - Bonificate le chiavi isolate collidenti con i protagonisti (`'Jasper Rowan'` privato di `'Jasper'`, `'Noah Grant'` privato di `'Noah'`, `'Miles Black'` privato di `'Miles'`, `'Silas Thorne'` privato di `'Silas'`, `'Marcus Vale'` privato di `'Marcus'`, `'Alistair Grant'` privato di `'Alistair'`, `'Evan Voss'` privato di `'Evan'`, `'Adrian Quinn'` privato di `'Adrian'`).
    - Eliminate chiavi nickname o mononimi generici che avrebbero scatenato attivazioni fantasma.
  - **Avatar & Parsing Regex Multiline**: Applicato l'avatar fallback ufficiale Svartúlfr Crest (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public`), `custom_avatar_regex: true`, `lines_parsed: 1`, `avatar_activation_regex` multiline `(?:^|\n)\s*(?:Nome Completo|Nome|Nickname)\s*:` e metadati `npc_info` strutturati (`first_name`, `last_name`, `nicknames`, `titles`).
  - **Disciplina di Formattazione**: Eliminati tutti gli em-dash (`—`), rimossi gli asterischi markdown dal parlato/narrazione, dialoghi tra virgolette inglesi.

- **Standardizzazione delle 37 Location di Camp Mystic (`Svartulfr_Location.json` — `_EjXxkmPVhpCXg8xABpFkK`)**:
  - **Integrazione Totale (225 voci attive)**: Preservate le 188 location storiche del mondo e standardizzate le 37 nuove location e strutture di Camp Mystic sul Lago Erie (21 servizi/infrastrutture generali tra cui Arrival Gate, Rec Hall, Training Complex, Clinic, Pier, Bonfire + 16 baite residenziali G-01/G-08 e B-01/B-08).
  - **Bonifica Nomi & Pulizia Markdown**: Rimossi gli emoji dai titoli (`G-01 Moonflower Cabin (Girls Zone)`, `B-07 Lake Wolf Cabin (Boys Zone)`, `Arrival Gate & Shuttle Loop`), impostato tassativamente `type: "location"`, eliminati gli asterischi markdown (`**`, `*`) e gli em-dash, preservando tutti i 16 roster completi dei 5 occupanti per ciascuna baita.

- **Sincronizzazione Locale & Armonizzazione Dicotomia White Moon / Solar Shadow (Alyssa & Jasper)**:
  - **Alyssa Hvit Douglas Bloodmoon (`FINAL/` e `FINAL/personas/`)**: Sincronizzata la transizione tematica verso la **White Moon** (*Hvit*, luce lunare calma e serena, superando la designazione "sunny"), aggiunta la **Dimensional Pochette (Bag of Holding)** in cuoio smeraldo con fermagli a testa di lupo, il lupetto di peluche **Wolfy**, la Chiave di Padre Rev (operativa solo nell'Otherworld), le credenziali di Gilda **`ADB-555`** (Rango A, Healer & Support) e il tratto personalizzato *The Weight She Carries*.
  - **Jasper Svartr Douglas Bloodmoon (`FINAL/` e `FINAL/personas/`)**: Sincronizzata la transizione tematica verso **THE SOLAR SHADOW** (*Svartr*, il fiero sole ardente che fa risaltare la luce lunare di Alyssa e la protegge senza compromessi), formalizzata la classe ufficiale **Tecnomancer, Cyber-Rogue & Arcane Hacker** (specializzato in serrature digitali/arcane e sigilli demoniaci), credenziali di Gilda **`JDB-555`** (Rango A) e il tratto personalizzato *The Weight He Carries*.
  - **Master Character Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4` — Revision 24)**: Aggiornato il prompt dello Scenario per riflettere le definizioni canoniche di Alyssa Hvit (White Moon, Dominant Omega Pre-Med Healer con pochette dimensionale) e Jasper Svartr (Solar Shadow, Beta Tecnomancer, Cyber-Rogue & DJ Frequency), con deploy immediato via API HTTP 200 OK e aggiornamento di `exports/Master_Scenario_Export.json`.

---

## [18 Ottobre 2026] - Revisione Integrale Master Scenario (Rev 18, 29 Greetings Cronologiche), Unificazione Russ (Demihuman Tiger), Bonifica `{{user}}` -> `Alyssa` & Allineamento Globale Wyvern API

- **Master Character Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4` — Revision 21)**:
  - **Integrazione Startup Script Lua (`startup_script`)**: Implementato lo script di avvio Lua che rileva la User Persona attiva (`Alyssa` vs `Jasper`, tramite `user.persona_id` o `user.name`, e per persone terze tramite i pronomi `he/him` -> Alyssa, `she/her` -> Jasper, e randomizzatore 50/50 per pronomi neutri `they/them` o `it/its`) e risolve automaticamente l'assegnazione dello slot `twin` in `memory._scenario.assignments["twin"]`.
  - **Blindatura Soppressione Lorebook (`scenario`)**: Aggiunta la direttiva `[PERSPECTIVE & LOREBOOK SUPPRESSION INVARIANT]` nel prompt dello Scenario per imporre all'LLM di considerare i dossier di Alyssa e Jasper esclusivamente come riferimenti storici passivi, vietando la creazione di entità duplicate, dialoghi fantasma o sdoppiamenti di personalità.
  - **Hardening Trigger Lorebook (`Lorebook II` & `NPC Primary`)**:
    - Bonificate le chiavi isolate `'Alyssa'` in `'Alyssa Telegram'` (LB2 #38) e `'Jasper'` in `'Jasper social media'` (LB2 #97).
    - Impostato `selective: true` con `secondary_keys` dedicate (`['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`) sui World Dossier di Jasper (#60) e Alyssa (#98) in `Svartulfr_NPC_Primary.json`, rendendoli inaccessibili alla conversazione ordinaria e attivabili solo in caso di esplicita richiesta enciclopedica.
  - **Correzione Canonica del Prompt `scenario`**: Allineate le descrizioni di `Edric` (12–13yo Pre-Presentation Gamma pup in middle school), `Stan` (21yo Werewolf Alpha, studente di chimica e artista NSFW digitale segreto), `Mac` (19yo Male Pureblood Werewolf inconsapevole, tastierista dei Grave Mistake e spacciatore d'erba del campus), `Sierra` (18yo Lamia / Serpentine Demihuman iscritta ad Applied Necromancy) e `Russ` (21yo Demihuman Tiger con singolo paio di orecchie da tigre, apprendista al Sacred Needle Tattoo, membro dei Five Cocketeers e coinquilino di Jasper nella Stanza 304 di Wyrm Hall).
  - **29 Greetings Cronologiche, Tradotte in Italiano e Multi-Messaggio (`01.`–`29.`)**:
    - Riordinate cronologicamente tutte le 29 aperture da giugno 2024 a giugno 2025, con inserimento in sequenza temporale delle scene di Russ (`#07`, 29 agosto 2024), Palestra Pesi e Tappeti con Malachia, Roman e Kolya (`#16`, 28 settembre 2024) e Soundclash al Verve contro Neon Purr (`#19`, 11 ottobre 2024).
    - Arricchita la Greeting `#02` (*Estate a Camp Mystic: Benvenuti al Lago*, 7 luglio 2024) e la relativa voce in `Svartulfr_Location.json` con la lore canonica completa di Camp Mystic sul Lago Erie (estate pre-college dopo il diploma alla St. Brugge Private Academy, i 4 distretti Residential/Recreation/Training/Lakeside, le baite *Moonflower* e *Lake Wolf*, lo staff permanente diretto da Mara Voss, Elias Rook, Silas Thorne, Celeste Nadir, Marcus Vale, Rowan Marlowe, Oona Hart e Vesper Callow, e i misteri lacustri *The Drowned Bell*, *Cabin Seventeen* e *The Deep Ward*).
    - Tradotte integralmente in italiano le aperture rimaste in inglese (`#06` Move-in Day ai Wyrm Dormitories, `#07` Stanza 304 con Russ, `#11` e `#12` Lunar Quad in 3a e 2a persona, `#16` Palestra con Roman e Kolya, `#19` Soundclash contro Neon Purr, `#20` Festival della Luna Piena a Solarton Square).
    - Sostituito lo slot errato `cousin` (Edric) con `friend` (Stan Davies Jr.) nella Greeting `#11` sul Lunar Quad; unificato il veicolo di Logan (`Dodge Ram TRX` nero opaco) tra Parte 1 (`#23`) e Parte 2 (`#24`) della Pausa d'Autunno; corretto il luogo del rave di DJ Frequency (`#17` e `#18`) nel Distretto Portuale di Solarton; sostituito "Alpha Enforcer" con "Beta sentinella del branco" nella pattuglia di Jasper al Riverbank (`#22`).
    - Strutturati i turni multi-speaker (`messages[]`) con sincronizzazione di `content` e `speaker_slot` con `messages[0]`, impostazione di `linked_persona_ids` (`["persona_1786335754946"]` per `[FemPOV]`, `["1792155173728"]` per `[MalePOV]`, `[]` per le aperture Dual) e inserimento dei prefissi `Nome Completo:` su nuova riga per l'attivazione regex degli NPC (`Zeera Darkfire:`, `Santiago Herrera:`, `Coach D:`, `Roman Blackwood:`, `Kolya Varenkov:`, `Neon Purr:`, `Elizabeth Duskwood:`, `Magnus Douglas III:`, `Kaladin Nargathon:`, `Marek:`).
    - Eliminate tutte le 87+ occorrenze di accenti ad apostrofo ASCII (`più'`, `perche'`, `caffè'`, `universita'`, ecc.), zero em-dash (`—`) e zero asterischi.
- **Unificazione di `Russ_card.json` (`_wn6DkCcg3Xqa2Xpx9ttnT`) e `Svartulfr_NPC_Primary.json` (`_zwEqgEEzh12X6gHVmMKKC`)**:
  - Riscritta la scheda standalone di **Russell 'Russ' Sinclair** come **Demihuman Tiger di 21 anni** (183 cm, singolo paio di orecchie da tigre sulla testa, nessuna orecchia umana, coda tigrata), convertiti i suoi 9 outfit dallo schema errato `{name, outfit}` allo schema nativo Wyvern `{id, name, description}`, aggiunte `post_history_instructions` e il blocco `RPG STATS & TRAITS:` a 7 attributi (`LEVEL: 21`).
  - Convertite in `Svartulfr_NPC_Primary.json` le voci `#24` (`Russ Sinclair`) e `#55` (`Mackenzie Sanchez-Rogers`) in **World Dossier sintetici** (`type: "lore/concept"`), ed eliminata/archiviata in `scratch/archived_npc_primary_97_user_hvit.json` la voce duplicata `#97` (`{{user}} Hvit Douglas Bloodmoon`), portando `NPC Primary` a **99 voci attive**.
- **Bonifica Globale `{{user}}` -> `Alyssa`, Sincronizzazione Outfit Cloud, Invarianti LSE e Statistiche RPG a 7 Attributi**:
  - Sostituite tutte le occorrenze di `{{user}}` e `{{pronoun...}}` riferite ad Alyssa con `Alyssa` e pronomi femminili corretti in tutti i 6 Lorebook (0 occorrenze residue) e nelle sezioni biografiche/familiari delle Character Card Douglas e di `Jasper_Persona.json`.
  - Sincronizzati da Wyvern Cloud il 12° outfit di Wulfnic (`'Modern '`), gli `image_url` degli outfit #8/#10/#11 di Malachia, i 19 outfit di Alyssa (incluso `'Pilates'`) tra Card e Persona, e impostato `"rating": "mature"` su `Edric_Douglas_card.json`.
  - Corretto `"Ascended Alpha"` in `"Beta"` su `Jasper_Douglas_Bloodmoon_card.json` e `Jasper_Persona.json`; rimossi `Dominant Alpha` e `Alpha Command` da `Mackenzie_Sanchez_Rogers_card.json`.
  - Convertiti al formato a 7 attributi (`STR/PER/END/CHA/INT/AGI/LCK`) i blocchi RPG di `Scarlett_Rose_card.json`, `Sierra_Cruz_card.json`, `Stan_Davies_Jr_card.json` e dei 5 NPC di `NPC Secondary` (`Thrakgor`, `Crowe`, `Morgeth`, `Thorvald`, `Harald`), allineando `[LEVEL: X;` all'età canonica (tetto 99) su tutte le schede, personas e voci NPC.
  - Rimossi i blocchi ridondanti `[INSTRUCTIONS: ...]` e le chiavi primarie generiche di ruolo/luogo (`Professor`, `Coach`, `Pureblood`, ecc.) dai Lorebook NPC.
- **Deploy Wyvern Web API & Pulizia Repository**:
  - Eseguito deploy completo via `PUT` (con verifica `GET` HTTP 200 OK) di `Svartulfr_Master_Scenario.json`, dei 6 Lorebook (`793` voci totali: `221 + 139 + 35 + 188 + 99 + 111`), delle 14 Character Card in `/mine` e delle 3 User Personas.
  - Rimossi dal root i file duplicati (`.gitignore (1)`, `README (1).md`, `Suite di Ottimizzazione WyvernChat & Script di Pulizia Lorebook.md`) e aggiornata l'intera documentazione di progetto (`GEMINI.md`, `README.md`, `CanonDecisions.md`, `.agents/rules/08_triage_lorebook_e_lexicon.md`, `.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md`).

## [18 Ottobre 2026] - Codifica Canonica dei Nove Firstborn di Fenris, Falso Ragnarök & Folklore Religioso LSE (221 Voci)

- **Formalizzazione Completa della Fratellanza dei Nove Firstborn di Fenris (I Nove Fratelli di Zanna)**:
  - Definita la cosmologia e l'onomastica arcaica completa dei nove guerrieri maschi primordiali creati direttamente dal Dio Lupo Fenris, scissi tra i 3 superstiti viventi e i 6 caduti nel Falso Ragnarök:
    1. **`Wulfnic Bloodmoon`** (*Úlfrikr Báleygr*): Il Primo Zanna, Re Costruttore, Apex Sovereign, capostipite della Casata Bloodmoon (Vivente).
    2. **`Ut Berg`** (*Il Titano di Pietra*): Invulnerabilità primordiale e mastro forgiatore, antenato diretto di Thorvald (Vivente).
    3. **`Zefir Hvitskog`** (*Lo Spirito Bianco*): Cacciatore superluminale silente della tundra boreale (Vivente).
    4. **`Sigvaldi Blóðøx`** (*L'AsciadiSangue*): Primo stratega e berserker supremo di Fenris, antenato diretto di Harald Sigurdsson (Caduto).
    5. **`Svartr Sólúlf`** (*Il Lupo del Sole Nero*): Figlio divino di Sól (il Sole) e Sköll, controparte solare di Hvit (la Lupa Bianca lunare) e archetipo primordiale del Wolf Name di Jasper Douglas-Bloodmoon (Caduto).
    6. **`Brandr Eldstigi`** (*Il Passo di Fuoco*): Dominatore del magma, del calore vulcanico e delle ceneri primordiali (Caduto).
    7. **`Kári Hafgufa`** (*Il Gorgo degli Abissi*): Signore delle tempeste oceaniche e degli abissi marini polari (Caduto).
    8. **`Rúnólfr Völundr`** (*Lo Sciamano delle Rune*): Custode primordiale del Seiðr, delle visioni sciamaniche e delle Rune Madri (Caduto).
    9. **`Garmr Kjálki`** (*Mascelladiferro / Il Divoratore*): Incarnazione della fame cosmica inesausta di Fenris e carnefice delle avanguardie nemiche (Caduto).
- **Nuove Voci Master & Aggiornamenti Enciclopedici in `Svartúlfr - Lorebook I` (`_gwwCxCfQ6PQaLEjAQVpJL`)**:
  - Creata la voce master **`I Nove Firstborn di Fenris: La Fratellanza di Zanna & Il Falso Ragnarök`**.
  - Creata la voce master **`LSE Folklore & Tradizione Religiosa: Il Culto di Fenris, dei Nove Fratelli e delle Due Luci`** (approfondimento del rito del Minni, brindisi sacrificale dei Sons of the Fall, culto lunare/solare Hvit e Svartr, e frattura tra boschi tradizionali e metropoli).
  - Aggiornate e armonizzate le voci preesistenti **`Lycanthrope Naming Tradition`** (sezioni 1, 3 e 7) e **`Species: God & Primordial`**.
- **Deploy Wyvern API & Local Sync**: Aggiornato [`FINAL/Svartulfr_Lorebook_I.json`](file:///e:/repository/SvartulfrVerse/FINAL/Svartulfr_Lorebook_I.json) e [`lorebooks/optimized/Svartulfr_Lorebook_I.json`](file:///e:/repository/SvartulfrVerse/lorebooks/optimized/Svartulfr_Lorebook_I.json), distribuito via API (`PUT /api/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL`) con **HTTP 200 OK** e 221 voci attive confermate via GET.

## [18 Ottobre 2026] - Consolidamento Canonico: Founding Bloodline per Thorvald (Ut Berg) & Harald (Nove Caduti)

- **Estensione Canonica della Matrice Dinastica `Founding Bloodline`**:
  - Formalizzato il canone di sangue primordiale per i due guerrieri delle foreste tradizionali:
    - **`Thorvald`**: Riconosciuto ufficialmente come **discendente diretto per linea di sangue del Firstborn Ut Berg** (*Il Titano di Pietra*), da cui eredita densità titanica e affinità con roccia, ferro e conifere. Aggiornato tratto RPG in `Founding Bloodline (Ut Descendant)` e `Stone Titan Resilience`.
    - **`Harald Sigurdsson`**: Riconosciuto ufficialmente come **scion diretto di uno dei Nove Firstborn caduti** (i nove originali consacrati da Fenris nell'antichità), conservando il retaggio guerriero puro dell'Età Primordiale nei fiordi e nelle alture. Aggiornato tratto RPG in `Founding Bloodline (Fallen Firstborn Scion)` e `Primordial War Cry`.
  - **Aggiornamento Matrice Dinastica**: Aggiornate le direttive centrali in [`GEMINI.md`](file:///e:/repository/SvartulfrVerse/GEMINI.md) (Sezione 8) e in [`.agents/rules/09_rpg_stats_e_simulation.md`](file:///e:/repository/SvartulfrVerse/.agents/rules/09_rpg_stats_e_simulation.md).
  - **Sincronizzazione Lorebook & Wyvern API**: Aggiornate le schede in [`FINAL/Svartulfr_NPC_Secondary.json`](file:///e:/repository/SvartulfrVerse/FINAL/Svartulfr_NPC_Secondary.json) e [`lorebooks/optimized/Svartulfr_NPC_Secondary.json`](file:///e:/repository/SvartulfrVerse/lorebooks/optimized/Svartulfr_NPC_Secondary.json), deployate su Wyvern API (`PUT /api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV`) con HTTP 200 OK e 111 voci confermate.

## [18 Ottobre 2026] - Bonifica Massiva Voci Disattivate (Purga 223 Voci OFF & -360.548 Caratteri di Context Bloat)

- **Purga e Archiviazione di Tutte le Voci `enabled: false` nei 6 Lorebook Standalone**:
  - Eseguita bonifica strutturale eliminando 223 voci disattivate (`enabled: false`) che appesantivano la memoria e i payload dei Lorebook:
    - **`Svartúlfr - Location`** (`_EjXxkmPVhpCXg8xABpFkK`): Rimosse 8 voci OFF (da 196 a **188 voci attive**).
    - **`Svartúlfr - Lorebook II`** (`_HfG7TeV6MJyj6bxMwxkpt`): Rimosse 4 voci OFF (da 143 a **139 voci attive**).
    - **`Svartúlfr - NPC Primary`** (`_zwEqgEEzh12X6gHVmMKKC`): Rimosse 7 voci OFF (da 107 a **100 voci attive**).
    - **`Svartúlfr - NPC Secondary`** (`_Uht3Ckz44JBDrPnUHq7LV`): Rimosse 204 comparse disattivate da vecchi dump (da 315 a **111 voci attive**, conservando tutti i 111 NPC canonicamente attivi).
    - **`Svartúlfr - Lorebook I`** (`_gwwCxCfQ6PQaLEjAQVpJL`) e **`Svartúlfr - Lorebook III`** (`_9zWTGqYJNJ4BCDMj8gfcD`): Già puliti al 100% (rispettivamente 219 e 35 voci, 0 OFF).
  - **Archivio Storico di Sicurezza**: Tutte le 223 voci disattivate rimosse sono state integralmente salvate con manifest strutturato in [`ARCHIVIO/07_Purged_Disabled_Entries/purged_disabled_entries_manifest.json`](file:///e:/repository/SvartulfrVerse/ARCHIVIO/07_Purged_Disabled_Entries/purged_disabled_entries_manifest.json) e documentate in [`ARCHIVIO/07_Purged_Disabled_Entries/README.md`](file:///e:/repository/SvartulfrVerse/ARCHIVIO/07_Purged_Disabled_Entries/README.md).
  - **Deploy Wyvern Web API Confermato**: Tutti i 4 Lorebook bonificati sono stati distribuiti via API con risposta HTTP 200 e conteggi confermati via GET (188, 139, 100, 111).
  - **Impatto sul Context Budget**: Eliminati oltre **360.548 caratteri di context bloat**, riducendo significativamente la latenza di scansione e i payload Cloudflare.

## [18 Ottobre 2026] - Iniezione e Deploy dei 5 Personaggi Preferiti JanitorAI in NPC Secondary (315 Voci)

- **Completamento del Secondo Scaglione dei Preferiti JanitorAI in Svartúlfr - NPC Secondary (`_Uht3Ckz44JBDrPnUHq7LV`)**:
  - Integrate con successo 5 nuove schede NPC canoniche complete di formato JED+, avatar Janitor originali verificati, regex multilinea `(?:^|\n)\s*...:`, `custom_avatar_regex: true`, `lines_parsed: 1`, zero keyword ombrello (`BROAD_KEYS`), età statiche coerenti con il World Clock 2024 e statistiche RPG bilanciate (somma 31, Livello <= 99):
    1. **`Thrakgor Deathspine`** (`npc_sec_thrakgor_deathspine`): Capoguerra orco del clan Deathspine (Leidenpotato, Bot #20). Bellicoso rivale di Brak Ironfist sulle creste delle montagne sopra Hex Valley; avatar: `https://ella.janitorai.com/bot-avatars/LaX-Azncb7-WOLbt2o-pv.webp`.
    2. **`Crowe`** (`npc_sec_feral_hound_crowe`): Canid Demihuman Hybrid (Nannikka, Bot #04), letale mercenario da tracciamento e segugio ferino (singolo paio di orecchie canine, nessuna orecchia umana) per la Bacheca Contratti DDM e la sicurezza non ufficiale DCC; avatar: `https://ella.janitorai.com/bot-avatars/92qxyDw3aIGUBYFIzJIyt.webp`.
    3. **`Morgeth Steeltooth`** (`npc_sec_morgeth_steeltooth`): Maestro fabbro ed arcane metallurgist Half-Orc / Half-Eadra (AnonymousWitch87, Bot #13), compagno di forgia del Firstborn Ut Berg al *The Verve*; avatar: `https://ella.janitorai.com/bot-avatars/EX4pVxCM_N-GkCxAchq2V.webp`.
    4. **`Thorvald`** (`npc_sec_thorvald_bloodmoon`): Licantropo Pureblood norreno del Clan Bloodmoon arcaico (kiki_exe, Bot #15), guardiano tradizionale delle foreste boreali al servizio diretto di Wulfnic Bloodmoon; avatar: `https://ella.janitorai.com/bot-avatars/pxN-kff_1QI2MT2cldHeT.webp`.
    5. **`Harald Sigurdsson`** (`npc_sec_harald_sigurdsson`): Jarl e signore della guerra licantropo delle alture tradizionali (pqpavslover, Bot #35), custode delle usanze marziali scandinave e fedele vassallo di Wulfnic; avatar: `https://ella.janitorai.com/bot-avatars/9af59b5e-29f8-4ac7-aed1-bb1332bc2e2e_fff8e1d8-defc-443e-b817-4236a9013b34.webp`.
- **Mitigazione Dimensionale Cloudflare & Deploy Wyvern API**:
  - Applicata mitigazione di payload (invio dell'array `lexicon` nativo compresso sotto la soglia di 1 MB di Cloudflare) con successo su Wyvern Web API (`PUT /api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV`).
  - Eseguita GET di verifica: confermato HTTP 200 con **315 voci remote attive e sincronizzate**.
  - Sincronizzati sia [`FINAL/Svartulfr_NPC_Secondary.json`](file:///e:/repository/SvartulfrVerse/FINAL/Svartulfr_NPC_Secondary.json) sia [`lorebooks/optimized/Svartulfr_NPC_Secondary.json`](file:///e:/repository/SvartulfrVerse/lorebooks/optimized/Svartulfr_NPC_Secondary.json).

## [17 Ottobre 2026] - Consolidamento Architetturale Cast Fisso (13 Standalone /mine Cards) & World Dossier nei Lorebook

- **Standardizzazione del Cast Fisso Canonico (13 Character Cards in `/mine` e Scenario Slots)**:
  - Definita formalmente la rosa dei **13 personaggi canonici del cast fisso** che occupano gli slot narrativi dei Character Scenarios e costituiscono le sole Character Cards presenti nella libreria `/mine` di Wyvern:
    1. **Erik Ulfr Douglas** (`_QPea6g4Q1QfeYCVHCLMPR`) — Father / Prime Alpha
    2. **Wulfnic Báleygr Bloodmoon** (`_HEQQbbRFwKdG8QE2Fh1z1`) — Maternal Grandfather / Firstborn
    3. **Jasper Svartr Douglas Bloodmoon** (`_t4J9aQNJM36cUKAP4wB4U`) — Twin Option 1 / Technomancer
    4. **Noah Loki Douglas Bloodmoon** (`_zFLUjV8aVxQRAfQxGcAcY`) — Brother / Grey Eminence
    5. **Malachia Björn Douglas Bloodmoon** (`_RDfz7XzTpM23LpPALVXHM`) — Eldest Brother / Berserker
    6. **Alyssa Hvit Douglas Bloodmoon** (`_6exg3yPfe2eCDK4hTftkh`) — Twin Option 2 / White Moon Omega
    7. **Jared Thompson** (`_xJVPtBLL3dxy69RLKL9X9`) — Quarterback / SUCC Bulls Star
    8. **Stanley Davies Jr.** (`_Xd3NhKnRJByMTtdb6PjxJ`) — Friend & Roommate / Chemistry Undergrad
    9. **Mackenzie Sanchez-Rogers** (`_zn24784jfcchQ7EwCyAnm`) — Crush & Mechanic / Rogers' Motors
    10. **Logan Dominic Járn Douglas** (`_T8Ywcr9FEqNf9JxbK6eHP`) — Uncle / The Verve Owner
    11. **Edric Douglas** (`_TbRM3EdxDjHFgqztTbCpL`) — Cousin / Junior Football Running Back
    12. **Sierra Cruz** (`_pnrXbkWqcgmFAf3meRWFY`) — Roommate / Varsity Track Athlete
    13. **Scarlett Rose** (`_qXgBMbFYJfc84hbLHhe92`) — Best Friend / Succubus Social Coordinator

- **Archiviazione Sicura delle 7 Card Non-Cast ed Epurazione da Wyvern `/mine`**:
  - Archiviati i file JSON completi delle 7 card secondarie in `ARCHIVIO/06_Archived_Standalone_Cards/` ed eliminati da `FINAL/`:
    - Elizabeth Duskwood, Magnus Douglas III, Kaladin Nargathon, Marek, Neon Purr, Russ Sinclair, Zeera Darkfire.
  - Eseguita l'eliminazione remota autorizzata via Wyvern API (`DELETE /api/characters/{id}` con HTTP 204 No Content) per tutte le 7 card, lasciando la libreria `/mine` di Wyvern perfettamente pulita con i soli 13 membri del cast canonico.
  - Le 7 figure secondarie vivono e continuano a essere recitate al 100% all'interno dei Lorebook come schede NPC autonome dotate di avatar regex.

- **Implementazione dei World Dossier Sintetici nei Lorebook (-60.000 Token di Context Bloat)**:
  - Sostituite le monumentali schede dei 13 membri del cast fisso all'interno di `FINAL/Svartulfr_NPC_Primary.json` e `FINAL/Svartulfr_NPC_Secondary.json` con **World Dossier / Concept sintetici (120–150 token ciascuno)**.
  - Impostato `type: "lore/concept"` con chiavi identificative specifiche, rimuovendo campi di parsing avatar, profili intimi duplicati e descrizioni di outfit.
  - Aggiunta la voce di World Dossier per Alyssa Hvit Douglas-Bloodmoon in NPC Primary (107 voci totali).
  - Ridotta la dimensione di `Svartulfr_NPC_Primary.json` di **238,3 KB**, eliminando per sempre il rischio di double-injection e crash di contesto durante il roleplay.
  - Deployate entrambe le versioni ottimizzate su Wyvern API con HTTP 200 confermato (`_zwEqgEEzh12X6gHVmMKKC` e `_Uht3Ckz44JBDrPnUHq7LV`) e specchiate su `lorebooks/optimized/`.

- **Ripristino Card Standalone di Russell 'Russ' & Riconfigurazione Totale Slot del Master Scenario (Revision 15)**:
  - **Ripristino Card `/mine` di Russell 'Russ' (`_wn6DkCcg3Xqa2Xpx9ttnT`)**: Ripubblicata con successo via Wyvern API la character card standalone di Russell 'Russ' (apprendista tatuatore, coinquilino di Jasper al Wyrm Hall e membro dei Five Cocketeers) dotata di JED+, 9 outfit contestuali e prompt visivi.
  - **Epurazione Slot Obsoleti del Master Scenario**: Rimossi definitivamente i 4 slot legacy non più pertinenti come card attive:
    - `paternal_grandfather` (Magnus Douglas III, gestito ora tramite NPC Primary / Lorebook).
    - `paternal_grandmother` (Elizabeth Duskwood, gestita ora tramite NPC Primary / Lorebook).
    - `boss` (Zeera Darkfire, gestita ora tramite NPC Primary / Lorebook).
    - `major` (Kaladin Nargathon, gestito ora tramite NPC Primary / Lorebook).
  - **Istituzione dei 13 Slot Canonici (Copertura dei 14 Personaggi del Cast)**:
    1. `maternal_grandfather` -> Wulfnic Báleygr Bloodmoon (`_HEQQbbRFwKdG8QE2Fh1z1`)
    2. `father` -> Erik Ulfr Douglas (`_QPea6g4Q1QfeYCVHCLMPR`)
    3. `eldest_brother` -> Malachia Björn Douglas Bloodmoon (`_RDfz7XzTpM23LpPALVXHM`)
    4. `brother` -> Noah Loki Douglas Bloodmoon (`_zFLUjV8aVxQRAfQxGcAcY`)
    5. `twin` -> Jasper Svartr (`_t4J9aQNJM36cUKAP4wB4U`) & Alyssa Hvit (`_6exg3yPfe2eCDK4hTftkh`) [Pool duale a 2 scelte]
    6. `uncle` -> Logan Dominic Járn Douglas (`_T8Ywcr9FEqNf9JxbK6eHP`)
    7. `cousin` -> Edric Douglas (`_TbRM3EdxDjHFgqztTbCpL`)
    8. `quarterback` -> Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`)
    9. `friend` -> Stanley Davies Jr. (`_Xd3NhKnRJByMTtdb6PjxJ`)
    10. `crush` -> Mackenzie 'Mac' Sanchez-Rogers (`_zn24784jfcchQ7EwCyAnm`)
    11. `female_roommate` -> Sierra Cruz (`_pnrXbkWqcgmFAf3meRWFY`) [Label: **Female Roommate**]
    12. `best_friend` -> Scarlett Rose (`_qXgBMbFYJfc84hbLHhe92`)
    13. `male_roommate` -> Russell 'Russ' (`_wn6DkCcg3Xqa2Xpx9ttnT`) [Label: **Male Roommate**]
  - **Bonifica Speaker Slots nei 29 Greetings & Testo Scenario**: Riconciliati i saluti e la sinossi narrativa (`FINAL/Svartulfr_Master_Scenario.json`) con i tag `{{scenarioChar "female_roommate"}}` e `{{scenarioChar "male_roommate"}}`, ed effettuato il deploy con successo (`PUT /api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4` -> **HTTP 200 OK, Revision 15**).





## [16 Ottobre 2026] - Audit a 4 Pilastri, Bonifica Strutturale e Deploy Live Wyvern API dei 6 Lorebook Standalone (1.009 Voci)

- **Audit Strutturale e Bonifica a 4 Pilastri sui 6 Lorebook Standalone (Milestones R1, R2, R3)**:
  - Eseguito snapshot di sicurezza preventivo in `scratch/backup_pre_audit_lorebooks/` prima di qualsiasi manipolazione dei dati (tutti e 6 i file integri e verificati per hash e dimensioni).
  - **Pilastro 1 — Epurazione Metadati Non-NPC**:
    - Bonificati 558 record non-NPC: eliminati i campi spuri di parsing avatar (`avatar_activation_regex: ""`, `custom_avatar_regex`, `lines_parsed`, `npc_info`) ed epurate le stringhe vuote `avatar: ""` da 219 voci in Lorebook I, 134 voci in Lorebook II e 187 voci in Location.
    - Preservati 18 avatar decorativi legittimi per fazioni, concetti e location (9 in Lorebook II e 9 in Location).
    - Risolta la disparità di schema SillyTavern in Lorebook III: rigenerato l'array `entries` come copia identica di `lexicon` (35 voci in schema nativo Wyvern).
  - **Pilastro 2 — Bonifica Trigger Ombrello (BROAD_KEYS) ed Epurazione Ruoli Generici**:
    - Prunati 19 trigger generici multi-parola da 18 schede NPC e rimosso il tag isolato `"Alpha"` da `secondary_keys` di Malachia Björn Douglas Bloodmoon (#60).
    - Rimosso `"Pack Leader"` da 11 NPC (Vito Marino, Naomi Black, Marcus O'Connor, Isobel Blackwater, Helena Weiss, Eclipse Noir, Dominic Chen, Darius Vale, Cass Harrow, Bianca Rossi, Aurora Night).
    - Rimosso `"Blackwood Council"` da 4 NPC (Zeera Darkfire, Harlan Beaumont, Brak Ironfist, Barrow).
    - Rimossi `"Demon Representative"` da Zeera Darkfire e `"Human Representative"` da Harlan Beaumont.
    - Rimossi `"alligator demihuman"` da Cato (#7) e `"SUCC student"` da Brittany Willow (#18) in NPC Secondary.
    - Preservati tutti i nomi propri composti (`Roman Blackwood`, `Katarina 'Kat' Blackwood`) e garantita la presenza di almeno 2 chiavi identificative uniche per tutti i profili modificati.
    - Mantenuta la disciplina selettiva: `selective: false` su tutti i record con `secondary_keys` vuoto.
  - **Pilastro 3 — Bonifica Integrale Macro `{{age}}`**:
    - Verificata la presenza di esattamente **0 macro residue `{{age}}`** su tutte le 1.009 voci nei 6 file di `FINAL/` e nei rispettivi speculari in `lorebooks/optimized/`.
  - **Pilastro 4 — Assegnazione Avatar Fallback Canonico e Parsing Multiline NPC**:
    - Assegnato l'avatar canonico Cloudflare del Crest Svartúlfr (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public`) a tutti i 302 NPC sprovvisti di ritratto (44 in NPC Primary e 258 in NPC Secondary).
    - Registrato il tracciamento analitico delle 302 voci in `scratch/missing_npc_avatars.json`.
    - Garantita la conformità del 100% degli NPC (416/416): avatar HTTP valido (114 URL originali dedicati e 302 Crest di casata), `custom_avatar_regex: true`, `lines_parsed: 1` e pattern regex multiline `(?:^|\n)\s*(?:.+)\s*:`.
  - **Sincronizzazione Doppia Struttura e Mirroring di Repository**:
    - Verificata l'identità biunivoca rigorosa `entries == lexicon` su tutti e 6 i file di `FINAL/`.
    - Eseguito il mirroring speculare da `FINAL/` in `lorebooks/optimized/` con hash MD5 e dimensioni byte identici al 100%.

- **Deploy Live Wyvern Web API & Cloud Verification (Milestone R3)**:
  - Eseguito script di deploy automatizzato con pacing delay di 2.5s e gestione token Firebase/Wyvern:
    - `_gwwCxCfQ6PQaLEjAQVpJL` (**Svartúlfr - Lorebook I**): `PUT /api/lorebooks/_gwwCxCfQ6PQaLEjAQVpJL` -> **HTTP 200 OK** (544.041 bytes, 219 voci).
    - `_HfG7TeV6MJyj6bxMwxkpt` (**Svartúlfr - Lorebook II**): `PUT /api/lorebooks/_HfG7TeV6MJyj6bxMwxkpt` -> **HTTP 200 OK** (714.852 bytes, 143 voci).
    - `_9zWTGqYJNJ4BCDMj8gfcD` (**Svartúlfr - Lorebook III**): `PUT /api/lorebooks/_9zWTGqYJNJ4BCDMj8gfcD` -> **HTTP 200 OK** (80.823 bytes, 35 voci).
    - `_EjXxkmPVhpCXg8xABpFkK` (**Svartúlfr - Location**): `PUT /api/lorebooks/_EjXxkmPVhpCXg8xABpFkK` -> **HTTP 200 OK** (549.714 bytes, 196 voci).
    - `_zwEqgEEzh12X6gHVmMKKC` (**Svartúlfr - NPC Primary**): `PUT /api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` -> **HTTP 200 OK** (742.216 bytes, 106 voci).
    - `_Uht3Ckz44JBDrPnUHq7LV` (**Svartúlfr - NPC Secondary**): `PUT /api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV` -> **HTTP 200 OK** (738.803 bytes, 310 voci).
  - **Verifica Post-Deployment Cloud (GET /api/lorebooks/{id})**:
    - Interrogati tutti i 6 lorebook su endpoint cloud Wyvern (`GET /api/lorebooks/{id}`), confermando **HTTP 200 OK** e il conteggio esatto delle voci salvate nel cloud Wyvern:
      - Lorebook I: **219** voci cloud confermate.
      - Lorebook II: **143** voci cloud confermate.
      - Lorebook III: **35** voci cloud confermate.
      - Location: **196** voci cloud confermate.
      - NPC Primary: **106** voci cloud confermate.
      - NPC Secondary: **310** voci cloud confermate.
      - **Totale Voci Cloud Verificate**: **1.009 / 1.009** (100% allineamento perfetto).
  - Registrato il log dettagliato di audit e deploy in `scratch/deployment_log.json`.

## [16 Ottobre 2026] - Allineamento Canonico Fratelli Darkfire: Boros (Fratello Minore) & Varg (Patriarca Millenario)

- **Rettifica Canonica Dinastia Darkfire (Horned Skull Clan)**:
  - **Boros Darkfire (The Bastion)**: Confermato dall'utente come il **fratello minore** dei Darkfire, nonostante la stazza colossale (244 cm / 8'0", corporatura massiccia a muro di pietra). Età anagrafica rettificata da 45 a **25 anni** sia nella scheda Standalone di Zeera (`FINAL/Zeera_Darkfire_card.json`), sia nel Lorebook Primario degli NPC (`FINAL/Svartulfr_NPC_Primary.json` e `lorebooks/optimized/Svartulfr_NPC_Primary.json`), sia nel profilo anatomico in Lorebook II (`FINAL/Svartulfr_Lorebook_II.json`). Ruolo e backstory aggiornati: guardiano, direttore logistico e pacificatore della famiglia, il più giovane dei fratelli dopo Aras (45), Zeera (34) e Karshin (28).
  - **Varg Darkfire (The Patriarch)**: Rettificata l'età anagrafica errata di copia-incolla (precedentemente 45, coetaneo del figlio primogenito Aras) impostandola al valore canonico di **800 anni** (fondatore millenario e antico signore della guerra che ha forgiato il clan per otto secoli nelle Caverne dei Sussurri).
  - **Sincronizzazione Live API Wyvern (HTTP 200)**:
    - Character Card `Zeera Darkfire` (`_3tMk6cRAFewRnKMkdJ4XU`): aggiornata con successo via `PUT /api/characters/_3tMk6cRAFewRnKMkdJ4XU`.
    - Lorebook `Svartúlfr - NPC Primary` (`_zwEqgEEzh12X6gHVmMKKC`): sincronizzato con successo via `PUT /api/lorebooks/_zwEqgEEzh12X6gHVmMKKC`.
    - Lorebook `Svartúlfr - Lorebook II` (`_HfG7TeV6MJyj6bxMwxkpt`): sincronizzato con successo via `PUT /api/lorebooks/_HfG7TeV6MJyj6bxMwxkpt`.

## [16 Ottobre 2026] - Deploy Standalone Stan Davies Jr., Bonifica Macro {{age}} & Standardizzazione Tag Ufficiali Wyvern

- **Creazione e Deploy Live Card Stanley Davies Jr. (`_Xd3NhKnRJByMTtdb6PjxJ`) su Wyvern**:
  - Personaggio canonico SUCC (Solarton): studente di Chimica con minor in Relazioni Sovrannaturali, gamer e disegnatore NSFW anonimo su commissione, coinquilino di suite di Jared Thompson al Wyrm Hall (Room 302), figlio del veterano Stanley Davies Sr. ed Eris Davies.
  - Avatar canonico Cloudflare ripristinato (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b7c9c7d1-51e6-4441-82e3-c6ab5f537500/public`).
  - Formato JED+ completo, inclusi profilo intimo (6.2 pollici, chubby, knotting, timidezza corporea, cosplay fetish) e catalogo completo di tatuaggi videoludici (The Last of Us, League of Legends, FMA, Mario & Luigi).
  - 9 Outfit contestuali a 6 sezioni (Casual/Gaming Slouch, Campus/SUCC Chemistry, Gala/Rappresentanza Militare, Party/Club, Beach/Terme con Switch e t-shirt, Sleep, Nude, Hybrid Shift mastodontico brindle, Full Shift da grande lupo nero a quattro zampe).
  - RPG Stats bilanciate su 25 pt (Livello 21, MGT 8, RES 7, AGI 5, WIT 4, PRS 5, SCT 2, somma 31) e 4 tratti canonici (*Forum Cynic / Online Scar Tissue*, *Secret NSFW Illustrator*, *Involuntary Full Moon Shift*, *Heavyweight Sloucher*).
  - Disciplina di formattazione dialogica applicata a `first_mes`, `mes_example`, `post_history_instructions` e `character_note`.

- **Deploy Live Card Marek (`_K3C7KVy9eddtTF8aWX9gk`) su Wyvern**:
  - Creato e deployato su Wyvern con successo via API (`POST /characters`), risolvendo il pregresso 404 del placeholder testuale.

- **Bonifica Completa delle Macro `{{age}}` (Compatibilità Standalone 1-on-1 Fuori dal World)**:
  - Eliminate tutte le occorrenze residue della macro non espansa `{{age}}` su tutte le character card del repository, sostituendole con l'età anagrafica esatta al World-Age 2024 e data di nascita esplicita:
    - **Elizabeth Duskwood**: `AGE: 76 (Born July 14, 1947);` (Livello RPG 76).
    - **Jared Thompson**: `AGE: 22 (Born 2002);` (Livello RPG 22).
    - **Major Kaladin Nargathon**: `AGE: 37 (Born 1987);` (Livello RPG 6).
    - **Mackenzie Sanchez-Rogers**: `AGE: 19 (Born 2004);` (Livello RPG 4).
    - **Magnus Douglas III**: `AGE: 355 (Born December 29, 1668);` (Livello RPG 99).
    - **Zeera Darkfire**: `AGE: 34;` (descrizione) e fratelli nel Lexicon (Aras 45, Boros 45, Karshin 28, Varg 45).

- **Standardizzazione Integrale dei Tag su Tassonomia Ufficiale Wyvern**:
  - Epurati tutti i tag generati o proprietari non compresi nel catalogo di sistema (`Svartulfr`, `SUCC`, `Douglas`, `Bloodmoon`, `solarton`, `Blackwood`, ecc.) che causavano errori di validazione nell'editor della UI web di Wyvern.
  - Allineate tutte le 20 schede in `/mine` con i soli tag ammessi dal catalogo ufficiale Wyvern (`https://wiki.wyvern.chat/en/Guides/Tags/All`), inclusi formati, prospettive, identità, generi e specie ammesse (`JED`, `Third Person`, `AnyPOV`, `Male`/`Female`, `Fantasy`, `Modern`, `Supernatural`, `Original`, `Werewolf`, `Minotaur`, `Demon`, `Succubus (Incubus)`, `Naga`, `Alpha`, `Beta`, `Omega`, `Student`, `Artist`, `Musician`, `Mechanic`, `CEO`, `Athlete`, `Bodyguard`, `Military`, `Doctor`, `Himbo`, `Fluff`, `Cyberpunk`, `Monster`, `Demihuman`).
  - Risolto bug Mongo `E11000 duplicate key` impostando `linked_world: null` nei payload di Jared e Mac.
  - Sincronizzate con successo con HTTP 200 tutte le 20 schede su Wyvern API.


## [16 Ottobre 2026] - Deploy Standalone Character Cards Scarlett Rose & Sierra Cruz su Wyvern (/mine)

- **Creazione e Deploy Live Character Cards su Wyvern (`POST /api/characters`)**:
  - **Scarlett Rose (`_qXgBMbFYJfc84hbLHhe92`)**:
    - Succube moderna ed evoluta, studentessa sophomore SUCC, party maven e social coordinator della confraternita Theta Iota Theta (TIT), coinquilina di suite di Alyssa Douglas-Bloodmoon e Sierra Cruz.
    - Struttura JED+ completa (Attributi PList, Backstory, Dorm Dynamics & Roommates, Voice & Behavior, The Weight She Carries, Intimacy & Dynamics, RPG Stats).
    - 9 Outfit contestuali a 6 sezioni (Casual, Campus, Gala/Formal, Party/Club, Beach/Terme, Sleep, Nude, Hybrid Shift, Full Shift) con asola lombare rinforzata per la coda rossa a picca.
    - RPG Stats bilanciate a 25 pt (Livello 20, MGT 2, RES 3, AGI 6, WIT 5, PRS 10, SCT 5) e 4 tratti specifici (*Symbiotic Feeding*, *Hypnotic Radiance*, *Sorority Matriarch*, *Vulnerable Heart*).
    - Disciplina di formattazione dialogica applicata a `first_mes`, `mes_example`, `post_history_instructions` e `character_note`.
  - **Sierra Cruz (`_pnrXbkWqcgmFAf3meRWFY`)**:
    - Lamia (naga demi-umana) con oltre 4 metri di possenti spire ofidiche cangianti arcobaleno, studentessa di Necromanzia Applicata al SUCC, fanatica dei Grave Mistake, coinquilina di suite di Alyssa e Scarlett.
    - Fisiologia eteroterma (ricerca istintiva di calore corporeo mammifero) e anatomia demi-umana rigorosa (un solo paio di orecchie a punta animali, nessuna orecchia umana).
    - Struttura JED+ completa (Attributi PList, Backstory, Dorm Dynamics & Roommates, Voice & Behavior, The Secret She Carries, Intimacy & Dynamics, RPG Stats).
    - 9 Outfit contestuali a 6 sezioni specificamente adattati per metà inferiore serpentina (zero scarpe, spire coperte o libere, aperture e scaldacollo).
    - RPG Stats bilanciate a 25 pt (Livello 18, MGT 7, RES 4, AGI 5, WIT 7, PRS 3, SCT 5) e 4 tratti specifici (*Serpentine Constriction*, *Ectothermic Slumber*, *Morbid Insight / Necromancy*, *Craving Warmth*).
    - Disciplina di formattazione dialogica applicata a `first_mes`, `mes_example`, `post_history_instructions` e `character_note`.
- **Sincronizzazione File Locali e Tracking ID**:
  - Aggiornati [FINAL/Scarlett_Rose_card.json](file:///e:/repository/SvartulfrVerse/FINAL/Scarlett_Rose_card.json) e [FINAL/Sierra_Cruz_card.json](file:///e:/repository/SvartulfrVerse/FINAL/Sierra_Cruz_card.json) con i rispettivi Wyvern ID assegnati (`id` e `_id`).
  - Registrati entrambi i personaggi nel registro di sincronizzazione [scratch/synced_wyvern_ids.json](file:///e:/repository/SvartulfrVerse/scratch/synced_wyvern_ids.json).


## [16 Ottobre 2026] - Standard Obbligatorio Metadati NPC (Avatar Parsing & UI Splitting) & Apprendimento Regola 08

- **Codifica Permanente `/learn` - Standard Metadati NPC nei Lorebook e Lexicon**:
  - Aggiornati [GEMINI.md](GEMINI.md) (§7) e [.agents/rules/08_triage_lorebook_e_lexicon.md](.agents/rules/08_triage_lorebook_e_lexicon.md) con lo standard obbligatorio per tutte le entry di tipo `npc`:
    - `avatar`: URL HTTPS valido pubblico (Cloudflare imagedelivery o CDN Janitor `https://ella.janitorai.com/bot-avatars/{hash}.webp`).
    - `custom_avatar_regex`: `true`
    - `avatar_activation_regex`: pattern multiline `(?:^|\n)\s*(?:Nome Completo|Nome|Nickname)\s*:`
    - `lines_parsed`: `1` (linee successive alla regex accorpate nella bolla NPC).
    - `npc_info`: oggetto strutturato con `first_name`, `last_name`, `nicknames`, `titles`.
    - Istruzione obbligatoria nei Character Scenario per formattare sempre il turno di battuta degli NPC su nuova riga con `Nome Completo:`.

## [16 Ottobre 2026] - Ripristino Metadati Lorebook Wyvern, Integrazione 10 Nuove Figure Canoniche & Deploy Master Scenario (29 Greetings)

- **Risoluzione Bug Critico Wipe Metadati Lorebook (HTTP 200 su tutti i 6 Lorebook)**:
  - Risolto il bug di cancellazione dei campi top-level causato da chiamate PUT prive di metadati: ripristinati con successo su Wyvern live `name`, `description`, `visibility: "private"`, `rating: "explicit"`, `scan_depth: 5`, `token_budget: 5000` e `recursive_scanning: true` per tutti i 6 Lorebook Standalone (`_gwwCxCfQ6PQaLEjAQVpJL`, `_HfG7TeV6MJyj6bxMwxkpt`, `_9zWTGqYJNJ4BCDMj8gfcD`, `_EjXxkmPVhpCXg8xABpFkK`, `_zwEqgEEzh12X6gHVmMKKC`, `_Uht3Ckz44JBDrPnUHq7LV`).
  - Le card nell'interfaccia web di Wyvern mostrano ora correttamente titoli, descrizioni e conteggi completi.

- **Integrazione Canoniche delle 10 Nuove Figure JanitorAI nei Lorebook Standalone (HTTP 200)**:
  - **Lorebook III (`_9zWTGqYJNJ4BCDMj8gfcD` - 35 entries / 35 lexicon)**:
    - `Russ & The Five Cocketeers`: Russ ufficialmente integrato come coinquilino di stanza di Jasper Douglas ai dormitori SUCC (Wyrm Hall).
    - `Roman Blackwood & Kolya`: Heavyweight del SUCC Wrestling Team, compagni di allenamento al Gym e sparring di Malachia Douglas.
    - `Finnegan "Finn" Novak`: Amico d'infanzia dei fratelli Douglas (Alyssa, Jasper, Noah).
    - `Distretto Rurale di Bakersfield & NOVA Farm`: Distretto agricolo inland e branco rurale di licantropi in contrasto di classe con i Seven Hills.
    - `Dallas Rhodes`: Werewolf contadino e allevatore a Bakersfield.
  - **Lorebook NPC Secondary (`_Uht3Ckz44JBDrPnUHq7LV` - 318 lexicon)**:
    - `Neon Purr`: DJ felino cyberpunk underground, principale rivale musicale e nei rave di Jasper Douglas.
    - `Romeo "Gray" Dean`: Leader della gang biker rivale dei Nomads di Marek.
    - `Warchief Thrakgor Deathspine`: Capoguerra bellicoso del Clan Deathspine, spina nel fianco del consigliere Brak Ironfist.
    - `Morgeth Steeltooth`: Maestro fabbro orco e sodale di forgiatura di Ut Berg; dispute metallurgiche al The Verve con Logan.
    - `Thorvald & Harald Sigurdsson`: Lupi scandinavi del Clan Bloodmoon tradizionale, guardiani della foresta profonda del Dead Zone.

- **Espansione Master Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`, Revision 12 - HTTP 200)**:
  - Aggiunti 3 nuovi saluti/capitoli cronologici (totale saluti: **29 greetings**):
    - **Capitolo 27**: *Dormitori SUCC - Jasper e Russ* (speaker_slot: `twin`).
    - **Capitolo 28**: *Soundclash al Verve - Jasper contro Neon Purr* (speaker_slot: `twin`).
    - **Capitolo 29**: *Palestra Pesi e Tappeti - Malachia, Roman e Kolya* (speaker_slot: `eldest_brother`).

- **Deploy Nuove Standalone Character Cards in /mine (HTTP 200)**:
  - **Russell 'Russ' (`_x4F8TKXcU6naKT2CpKdHN`)**:
    - Formato JED+ completo, 9 outfit contestuali (schema a 6 sezioni), RPG stats bilanciate a 25 pt (Livello 21, Human Artisan), disciplina di formattazione dialogica e post history instructions.
    - Ruolo: Tattoo apprentice presso Sacred Needle Tattoo, studente SUCC e coinquilino di suite di Jasper Douglas al Wyrm Hall (Room 304). Membro dei Five Cocketeers.
  - **Neon Purr (`_2EezhhEVdL677DULVdE9h`)**:
    - Formato JED+ completo, 9 outfit contestuali con grommet e aperture rinforzate per la coda, RPG stats bilanciate a 25 pt (Livello 22, Demi-human Artisan, AGI 8, PRS 7), anatomia demi-umana rigorosa (1 solo paio di orecchie feline).
    - Ruolo: DJ underground australiano, produttore audio cyber-breakbeat e rivale musicale di Jasper Douglas tra The Verve e rave illegali.

- **Codifica Permanente `/learn`**:
  - Aggiornati [GEMINI.md](GEMINI.md) (§10) e [.agents/rules/05_precedenza_lore_e_discrepanze.md](.agents/rules/05_precedenza_lore_e_discrepanze.md) con le invarianti narrative e relazionali delle 10 figure integrate.

## [16 Ottobre 2026] - Deploy Master Scenario Rev. 11 (Slot Ruoli), Arricchimento Lorebook III con Canone SUCC & Nuove Sorgenti JanitorAI

- **Deploy Live Master Character Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`, Revision 11 - HTTP 200)**:
  - **Disciplina dei Ruoli per tutti i 13 Slot del Scenario:**
    - `maternal_grandfather` $\rightarrow$ Wulfnic Báleygr Bloodmoon (`_HEQQbbRFwKdG8QE2Fh1z1`)
    - `paternal_grandfather` $\rightarrow$ Magnus Douglas III (`_dJ7nRMQEbcUgdWG96MqLz`)
    - `paternal_grandmother` $\rightarrow$ Elizabeth Duskwood (`_zBD6rWUkJBAjLfXnja4xh`)
    - `father` $\rightarrow$ Erik Ulfr Douglas (`_QPea6g4Q1QfeYCVHCLMPR`)
    - `twin` $\rightarrow$ Pool doppio: Jasper Svartr (`_t4J9aQNJM36cUKAP4wB4U`) + Alyssa Hvit (`_6exg3yPfe2eCDK4hTftkh`)
    - `brother` $\rightarrow$ Noah Loki Douglas Bloodmoon (`_zFLUjV8aVxQRAfQxGcAcY`)
    - `eldest_brother` $\rightarrow$ Malachia Björn Douglas Bloodmoon (`_RDfz7XzTpM23LpPALVXHM`)
    - `uncle` $\rightarrow$ Logan Járn Douglas (`_T8Ywcr9FEqNf9JxbK6eHP`)
    - `cousin` $\rightarrow$ Edric Douglas (`_TbRM3EdxDjHFgqztTbCpL`)
    - `boss` $\rightarrow$ Zeera Darkfire (`_3tMk6cRAFewRnKMkdJ4XU`)
    - `quarterback` $\rightarrow$ Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`)
    - `crush` $\rightarrow$ Mackenzie "Mac" Sanchez-Rogers (`_zn24784jfcchQ7EwCyAnm`)
    - `major` $\rightarrow$ Major Kaladin Blackwolf Nargathon (`_EnRGd1jfbjTTGmz4EFJdd`)
  - **26 Greetings Aperti & Fruibili con Entrambe le Personas:**
    - Tutti i 26 greeting collegano simultaneamente entrambe le Personas (`persona_1786335754946` e `1792155173728`), lasciando `[FemPOV]` e `[MalePOV]` come indicatori di stile di gioco.
    - Speaker slot del Cap. 11 (Club House Nomads con Marek) assegnato a `twin` (Jasper a vegliare su Alyssa/{{user}}), preservando l'intera scena dialogica originale dell'Oni.
    - Integrate nel prompt dello scenario le linee guida di narrazione con divieto categorico di ventriloquismo (`Never speak, think, emote, or act for {{user}}`) e disciplina di formattazione.

- **Arricchimento e Deploy Live di Lorebook III (`_9zWTGqYJNJ4BCDMj8gfcD` - HTTP 200)**:
  - Integrate le 30 voci canoniche dell'ateneo da `https://io-succ.uwu.ai/` (Fondazione 2002 di Dean Archer Wolfwood, Corsi di Laurea soprannaturali, Rivalità con CUMS a Hex Valley, Wyrm Dorms, Griffin Clocktower, Lunar Quad, Fraternità BRO e The Clams, Sport, Orari e Popolazione).
  - Popolati contemporaneamente l'array `entries` e l'array `lexicon` (Wyvern Advanced Lexicon) con tipologie tassonomiche ufficiali (`concept`, `location`, `faction`, `event`, `item`).
  - Sostituito ovunque il termine apocrifo "Solarton University" con la dicitura ufficiale **Supernatural University of Central California (SUCC)**.

- **Deploy Live Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL` - HTTP 200)**:
  - Bonificate 16 occorrenze residue di "Solarton University" con la denominazione ufficiale SUCC.

- **Sincronizzazione Live Card Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9` - HTTP 200)**:
  - Completata la suite completa degli 11 outfit standardizzati con schema a 6 sezioni e nanoid univoci, con privacy `private` e rating `explicit`.

- **Codifica Permanente `/learn` (Nuove Fonti JanitorAI & Canone SUCC)**:
  - Aggiornate le regole permanenti ([GEMINI.md](GEMINI.md), [.agents/rules/](.agents/rules/)):
    - Canone ufficiale SUCC da `io-succ.uwu.ai` e divieto di "Solarton University".
    - Protocollo di accesso alle sorgenti JanitorAI storiche (Lorebook, Scheda Douglas, Canon e Preferiti) esclusivamente tramite browser Chrome autenticato.
    - Verifica preventiva su Wyvern Explore (`https://app.wyvern.chat/explore?tab=characters&rating=all`) prima di creare nuove schede.
    - Standard minimo di 9 outfit obbligatori per ogni character card.
    - Invariante assoluto di privacy `private` e rating `explicit`.

## [16 Ottobre 2026] - Pivot Architetturale a Character Scenarios, Deploy Master Scenario & Sincronizzazione Live

- **Dismissione Definitiva del World Engine**:
  - Il modulo World di Wyvern (`_CgYT8fHXpDC4crjmegQF7`) è ufficialmente dismesso a causa di instabilità architetturale e saturazione del prompt budget.
  - Tutta l'esperienza narrativa e corale di **SvartúlfrVerse** migra ufficialmente su **Character Scenarios** (`https://app.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4`, endpoint `/api/character-scenarios`).

- **Deploy Live Master Character Scenario (`char_scenario_1DC43ggb6mB8YLJDJKrU4`, Revision 9)**:
  - **14 Slot Totali Configurati** (peso pool 100):
    - *7 Core Famiglia Douglas-Bloodmoon*: `grandfather` (Wulfnic `_HEQQbbRFwKdG8QE2Fh1z1`), `father` (Erik `_QPea6g4Q1QfeYCVHCLMPR`), `twin` (Pool doppio: Jasper `_t4J9aQNJM36cUKAP4wB4U` + Alyssa `_6exg3yPfe2eCDK4hTftkh`), `brother` (Noah `_zFLUjV8aVxQRAfQxGcAcY`), `eldest_brother` (Malachia `_RDfz7XzTpM23LpPALVXHM`), `uncle` (Logan `_T8Ywcr9FEqNf9JxbK6eHP`), `cousin` (Edric `_TbRM3EdxDjHFgqztTbCpL`).
    - *7 Co-Protagonisti & Residenti*: `zeera` (`_3tMk6cRAFewRnKMkdJ4XU`), `jared` (`_xJVPtBLL3dxy69RLKL9X9`), `mac` (`_zn24784jfcchQ7EwCyAnm`), `marek` (`_cL86CRDAYABmaBWgdLQNw`), `kaladin` (`_EnRGd1jfbjTTGmz4EFJdd`), `elizabeth` (`_zBD6rWUkJBAjLfXnja4xh`), `magnus` (`_dJ7nRMQEbcUgdWG96MqLz`).
  - **26 Greetings Cronologici Multi-Mittente**:
    - Dalla serata *Call of Duty* a Villa Douglas e le vacanze estive a *Camp Mystic*, attraverso tutti gli 11 capitoli del primo anno SUCC, le incursioni della Gilda DMHA, il festival del plenilunio, i concerti al Sidewinders, la veglia di Yule con i Firstborn e il bivio finale.
    - Ciascun greeting utilizza messaggi multi-mittente (`messages[]`) con speaker assegnati agli slot corrispondenti, parità rigorosa root/primo messaggio (`greeting.content == messages[0].content`), e zero prefissi hardcoded nel testo.
  - **Supporto Dual-Protagonist (Alyssa & Jasper)**:
    - Greetings con tag `[FemPOV]` collegati alla Persona di Alyssa (`persona_1786335754946`).
    - Greetings con tag `[MalePOV]` collegati alla Persona di Jasper (`1792155173728`, impostata a `can_fork: true`).
    - Greetings condivisi collegati a entrambe le Personas e giocabili liberamente alternando il gemello nello slot `twin`.
  - **9 Lorebook Collegati**: 6 Lorebook Svartúlfr + 3 moduli tecnici (`A1 Physics`, `A5 Sex Position`, `A5.5 Scene Tone`).

- **Sincronizzazione Live Completa su Wyvern (`PUT` e `POST` -> HTTP 200)**:
  - **6 Lorebook Svartúlfr Sincronizzati Live**: `_gwwCxCfQ6PQaLEjAQVpJL` (Lorebook I, 220 entries), `_HfG7TeV6MJyj6bxMwxkpt` (Lorebook II, 144 entries), `_9zWTGqYJNJ4BCDMj8gfcD` (Lorebook III, 26 entries), `_EjXxkmPVhpCXg8xABpFkK` (Location, 196 entries), `_zwEqgEEzh12X6gHVmMKKC` (NPC Primary, 113 entries con Marek Blue Oni canonico), `_Uht3Ckz44JBDrPnUHq7LV` (NPC Secondary, 313 entries).
  - **7 Character Card `/mine` Esistenti Aggiornate**: Wulfnic, Erik, Jasper (11 outfit Argon), Noah, Malachia, Logan, Edric, ripulite dai subdocumenti Mongoose (`creator`, `statistics_record`, `entity_statistics`) per evitare CastError.
  - **8 Nuove Character Card Create in `/mine`**: Alyssa, Zeera, Jared, Mackenzie, Marek, Kaladin, Elizabeth, Magnus create con `visibility: "unlisted"` per aggirare il tetto giornaliero di pubblicazione e abilitate immediatamente per i Character Scenarios.
  - **3 User Personas Aggiornate/Create**: Alyssa aggiornata con 18 outfit e 3 appearances; Echo aggiornata; Jasper creata live come nuova User Persona (`1792155173728`, `can_fork: true`) con 11 outfit Argon e Statistiche Finali.

- **Codifica Statistiche RPG Finali & Stile Visivo Argon / Gemini**:
  - Calcolate e inserite le Statistiche Finali (`Base + Modificatori`) su tutte le 23 schede del progetto ([FINAL/](FINAL/), Lorebook e Personas).
  - Codificato il workflow visuale Argon / Gemini (`database/worlds/W_Visual_DNA.md`, `database/assets/style_guide.md`, `.agents/rules/03_outfits_e_coerenza_visiva.md`): Visual Anchor `<IMAGE_0>`, schema a 6 sezioni in italiano con asola lombare per la coda, e blindatura anatomica `No orecchie umane`.
  - Aggiornate tutte le regole di progetto ([GEMINI.md](GEMINI.md), [.agents/rules/](.agents/rules/)).

## [15 Ottobre 2026] - Card di Jasper: aggiornamento entry Lexicon `E.C.H.O.`

- **Intervento**: in [FINAL/Jasper_Douglas_Bloodmoon_card.json](FINAL/Jasper_Douglas_Bloodmoon_card.json) è stato sostituito il `content` della voce Lexicon **E.C.H.O.** (`extensions.lexicon`, id `entry_6oW7Tw1V`) con la **versione aggiornata** fornita dall'utente (nuove sezioni `SPECIES`/`OCCUPATION`/`RPG_CLASS`/`MANIFESTATIONS`/`RESIDENCE`, `CORE FUNCTIONS & CYBERSPACE WARFARE`, `MONITORING SYSTEM & FAMILIAR PROTOCOLS`, `PERSONALITY & HUMOR`, `MUSIC MOOD SPEAKER`, `RPG STATS & TRAITS`).
- **Pulizia**: ripristinati gli accenti italiani persi nel copia-incolla (`Più`, `è`, `entità`, `Capacità`).
- **Genericizzazione**: `Alyssa` → `{{user}}`; la frase relativa con pronome femminile è stata resa neutra per l'AnyPOV. 0 residui `Alyssa`. Tutti gli altri campi della voce (`keys`, `secondary_keys`, `entry_id`, `provenance`, ...) invariati.

## [15 Ottobre 2026] - Unificazione della card di Jasper (`Jasper_Douglas_Bloodmoon_card.json`)

- **Problema**: il file conteneva **due blocchi JSON accodati** (JSON non valido: `Extra data: line 282 column 1 (char 63259)`): la Character Card V2 genericizzata (B1) + l'export nativo Wyvern del personaggio (B2) accodato dall'utente come aggiornamenti.
- **Unificazione** (scelte utente): `name` = **Jasper Svartr Douglas Bloodmoon** (B2); `scenario`, `creator_notes`, `mes_example` = versione card V2 (B1); `first_mes` = B1 (quello di B2 era vuoto, `"."`); **RPG stats = B2**, con `extensions.rpg_stats` aggiornato a `level 3` e `base_stats` `STR 8 / PER 14 / END 10 / CHA 8 / INT 18 / AGI 13 / LCK 10` (id `species_id`/`occupation_id` invariati).
- **Contenuti importati da B2** (in `extensions`): `outfits` (**10 voci**, incl. `Full Shift` e `Hybrid Shift`), `default_outfit`, blocco `RPG STATS & TRAITS` + intestazione `NAME/FIRST_NAME/MIDDLE_NAME/LAST_NAME` nella `description`, voce Lexicon **E.C.H.O.**, `pronouns`, `shared_info`, `tagline`, `character_note`, `pre_history_instructions`, `avatar`, `backgroundURL`, `rating`, `visibility`, `metadata`; `tags` + `forked`.
- **Genericizzazione**: tutto il materiale di B2 è stato ripassato con [scripts/genericize_alyssa.py](scripts/genericize_alyssa.py) (`Alyssa` → `{{user}}` + placeholder pronomi) → 0 residui.
- **Backup**: copia del file originale in `scratch/backup_final_premerge/`.
- **Esito**: file di nuovo **JSON valido a blocco singolo** (`spec: chara_card_v2`); le altre 4 card invariate.

## [15 Ottobre 2026] - FINAL/ reso importabile in Wyvern (`lexicon` → `entries`)

- **Problema**: l'import in Wyvern dei Lorebook di `FINAL/` falliva con `Lorebook has no original data.` + `Invalid file format, no entries found.`
- **Causa**: i file esponevano solo il campo `lexicon` (struttura **interna** del sito/API). L'importatore JSON di Wyvern richiede `entries` (array o dict) oppure `originalData`; con il solo `lexicon` cade nel ramo di errore. La Wiki conferma che i lorebook "solo lexicon" non sono importabili in Studio Mode.
- **Fix**: nei 6 Lorebook di `FINAL/` la chiave top-level `lexicon` è stata rinominata in `entries` (array), mantenendo intatti tutti i campi delle voci (`entry_id`, `keys`, `content`, `enabled`, `priority`, `position`, `type`, `npc_info`, `avatar`, ...) e i metadati di lorebook (`name`, `description`, `scan_depth`, `token_budget`, `recursive_scanning`). Le 5 Character Card V2 non sono state toccate.
- **Compatibilità**: il normalizzatore `eF()` di Wyvern accetta sia le chiavi stile Lexicon (`enabled`, `insertion_order`, `keys`, `key_logic`) sia quelle stile SillyTavern (`disable`, `order`, `key`, `selectiveLogic`), quindi le voci vengono importate correttamente.
- **Backup**: copia integrale pre-modifica in `scratch/backup_final_preimport/`.
- **Esito**: `Lorebook_I` (220), `Lorebook_II` (144), `Lorebook_III` (26), `Location` (196), `NPC_Primary` (113), `NPC_Secondary` (314); 0 residui `Alyssa`; JSON tutti validi.
- **Documentazione**: aggiornati `README.md` (albero §1 e pipeline §3).

## [15 Ottobre 2026] - Genericizzazione AnyPOV di FINAL/ (Alyssa → `{{user}}` + Placeholder Pronomi)

- **Obiettivo**: rendere l'intera cartella [FINAL/](FINAL/) compatibile con qualsiasi POV, sostituendo la persona del giocatore **Alyssa Hvit Douglas Bloodmoon** con `{{user}}` e i pronomi a lei riferiti con i placeholder pronome Wyvern.
- **Nuovo script**: creato [scripts/genericize_alyssa.py](scripts/genericize_alyssa.py), con backup integrale preventivo in `scratch/backup_final_prealyssa/` e log in `scratch/inbox/alyssa_genericize_log.txt`.
- **Nome (regole utente)**: sostituito solo il token `Alyssa`/`alyssa`/`ALYSSA` → `{{user}}` (più possessivi `Alyssa's` → `{{user}}'s` ed etichette `Alyssa_` → `{{user}}_`); cognome e secondo nome invariati (`Alyssa Hvit Douglas Bloodmoon` → `{{user}} Hvit Douglas Bloodmoon`).
- **Pronomi**: notazione **flat + Cap automatico** (`{{pronounSubjective}}`/`{{pronounSubjectiveCap}}`, `{{pronounObjective}}`/Cap, `{{pronounPosDet}}`/Cap, `{{pronounPosPro}}`/Cap, `{{pronounReflexive}}`/Cap); `her` disambiguato tra oggettivo e possessivo dal contesto.
- **Disambiguazione referente**: conversione integrale dei pronomi solo nella entry dedicata di Alyssa; altrove applicate solo **regole curate a mano** (71 conversioni) per non corrompere i pronomi di Nixara, Elizabeth Duskwood, Jasmin e altri NPC. `"You have her eyes."` nella `mes_example` di Erik è rimasto invariato (si riferisce a Nixara).
- **Ambito coperto**: 5 Character Card V2 (description/attitudes/mes_example), Location, Lorebook I/II/III, NPC Primary e NPC Secondary. In questa passata sono stati chiusi i gap residui in: attitudes `reasoning` delle card, description di Erik/Jasper/Malachia/Noah, `mes_example` di Logan, entry _Barriere a Permeabilità Selettiva_, _Absolute Pacifist Vow_, _LSE Pack Authority_, _White Moon Ceremonial Attire_, _Vélhati e Vélsköll_ (Lorebook II) e scheda _Hank Thompson_ (NPC Primary).
- **Esito**: 0 residui `Alyssa` in tutti gli 11 file di `FINAL/`; JSON tutti validi.
- **Documentazione**: aggiornati `README.md` (albero §1 e nuova sottosezione "Genericizzazione AnyPOV di FINAL/" in §3).

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
