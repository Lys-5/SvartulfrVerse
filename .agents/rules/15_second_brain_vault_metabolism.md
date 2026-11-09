# Regola 15 — Architettura Second Brain (LLM Wiki 2026), Metabolismo del Vault & Standard Automazioni

Per garantire che la conoscenza del progetto non si degradi né si sfaldi nel tempo, questo repository adotta formalmente i principi del modello **«LLM Wiki / Second Brain 2026»** (Karpathy, CoALA framework, MemGuard):

---

## 1. I Tre Livelli della Conoscenza

1. **Livello 1 — Sorgenti Originali (Immutabili):**
   - Cartella `ARCHIVIO/` (dump grezzi Janitor AI, chat log storici, export grezzi).
   - Gli agenti leggono queste fonti per estrarre la verità storica o recuperare dettagli canonici, ma **non le modificano né le sovrascrivono mai**.
2. **Livello 2 — La Wiki / Cervello Compilato (Navigabile e Curato):**
   - Cartella `FINAL/` e i 6 Lorebook Standalone sincronizzati.
   - È la *Single Source of Truth* viva: schede JED+, NPC integrali, location e cataloghi RPG aggiornati.
3. **Livello 3 — Lo Schema come Contratto (Memoria Procedurale):**
   - `GEMINI.md`, `AGENTS.md` e la directory `.agents/rules/`.
   - Regole rigide verificate dal codice, non semplici raccomandazioni testuali.

---

## 2. Separazione Rigida dei 4 Tipi di Memoria (Anti-Contaminazione CoALA)

Per prevenire l'errore cognitivo di *Heterogeneous Memory Contamination* (MemGuard 2026), gli agenti devono mantenere nettamente separati i quattro registri di memoria:
- **Memoria di Lavoro (Vita breve):** La sessione attiva e i file transitori in `scratch/`. Svuotabile o rigenerabile liberamente.
- **Memoria Episodica (Datata):** Eventi, cronache di sessione e storico modifiche in `CHANGELOG.md`. Ogni evento reca data o World-Age esplicita.
- **Memoria Semantica (Stabile):** Fatti duraturi ed enciclopedici in `FINAL/` (schede JED+, lore di specie, fisionomia).
- **Memoria Procedurale (Regole):** Direttive operative in `.agents/rules/`. Un evento episodico non deve mai tramutarsi in regola universale senza convalida formale.

---

## 3. Il Controllo di Salute (Metabolismo del Vault)

> *"Una regola scritta in un README è un desiderio. Una regola eseguita da un controllo automatico è una legge."*

Lo script autoritativo `scripts/vault_health_check.py` costituisce il metabolismo rigido del vault e verifica sistematicamente i 6 difetti capitali:
1. **Contraddizioni:** Mismatch su altezze canoniche, date di nascita, marchi divini o vincoli anatomici/fisiologici (es. Sierra Cruz).
2. **Affermazioni Scadute:** Sovrascritture o regressioni di canone rispetto alla Single Source of Truth.
3. **Pagine/Entità Orfane:** Riferimenti rotti o buchi di dati (es. entry con descrizione vuota).
4. **Igiene dei Trigger:** Eliminazione totale della macro `{{age}}`, blocco di broad keys generiche su NPC e garanzia della terna di flag (`scan_persona: true`, `whole_words_only: true`, `enableEntryHighlighting: true`).
5. **Parità Byte-for-Byte:** Uguaglianza al 100% tra `entries` e `lexicon` nei Lorebook locali.
6. **Integrità Infrastruttura:** Stato del proxy locale e delle automazioni registrate.

Il controllo di salute viene eseguito periodicamente e integrato come **Task 0** del runner quotidiano di manutenzione (`scripts/daily_maintenance_runner.py`).

---

## 4. Standard Obbligatorio Automazioni Antigravity (Unified Scheduled Sidecar)

- **Divieto del tool `schedule` di chat per automazioni permanenti:** Il tool interno `schedule` crea un cron temporaneo agganciato esclusivamente alla sessione di chat aperta, non appare nel cruscotto UI (`sidecar://dashboard`) e muore alla chiusura del contesto.
- **Unificazione in Singola Master Pipeline (`daily-master-pipeline`):** Tutte le operazioni quotidiane di manutenzione, monitoraggio e arricchimento lore sono consolidate in un'unica automazione atomica registrata in:
  `~/.gemini/config/sidecars/daily-master-pipeline/sidecar.json`
  - Con `"builtin": "schedule"`, `"restart_policy": "always"`, e schedule `"CRON_TZ=Europe/Rome 0 9 * * *"`.
  - Con delimitatore `"--"` prima del prompt per separarlo dalle flag di sistema.
  - Con permessi minimi garantiti (`workspace_uris` e `access_grants`).
  - I 4 precedenti sidecar separati (`daily-character-enrichment`, `daily-wyvern-monitor`, `daily-proxy-free-models`, `daily-omnisync-archive-mining`) sono archiviati in `ARCHIVIO/sidecars_legacy_backup/` e sostituiti dalla pipeline unificata a 5 stadi.
- **Attivazione User-Driven:** L'abilitazione iniziale viene sempre effettuata dall'utente tramite il dashboard nativo ([`sidecar://dashboard`](sidecar://dashboard)).
- **Zero Dipendenze Esterne negli Script Sidecar (`urllib.request` Standard):** Tutti gli script Python invocati dalle automazioni o dall'orchestratore multi-modello devono utilizzare esclusivamente la standard library Python (`urllib.request`, `urllib.error`, `json`, `pathlib`, `time.monotonic()`) per le chiamate HTTP e di sistema, evitando pacchetti esterni non garantiti come `requests`. Ciò assicura compatibilità al 100% sia con `uv run python` (in ambienti `.venv` isolati) sia con l'interprete Python di sistema. Notice anche che ogni dashboard HTML locale autogenerata deve includere un `<link rel="icon" href="data:image/svg+xml,..." />` inline per azzerare errori `404` su `/favicon.ico` durante la validazione Chrome DevTools.

---

## 5. Architettura Multi-Modello a 3 Tier, Registro Open-Provider & Flotta AI PC OMEN

La skill `.agents/skills/multi-model-unified-pipeline/` (`scripts/orchestrator.py` + `references/models_registry.json`) governa l'esecuzione unificata dei 5 stadi giornalieri distribuendo il carico su **3 Tier operativi** più **2 Specialisti Desktop Dedicati**:
1. **Tier 1 (`scout-fast` — Effort `low`/`medium`):**
   - *Modello IDE Primario:* `gemini-3.8-flash` (subagent `flash` / `flash_lite`).
   - *Twin / Proxy `:5005` & Client Desktop:* `gemma-4-31B-it`, `qwen-3.8-27b`, `copilotapp.exe`.
   - *Task:* **Stage 0** (`vault_health_check.py` + scansione dei 5 client AI sul PC OMEN), **Stage 1A** (`daily_wyvern_platform_monitor.py`), **Stage 1B** (`proxy/update_free_models.py`).
2. **Tier 2 (`architect-sync` — Effort `medium`):**
   - *Modelli IDE Primari:* `gemini-4-argon` & `claude-sonnet-5.5` (subagent `inherit`).
   - *Twin / Proxy `:5005` & Client Desktop:* `z-ai/glm-5.3`, `deepseek-chat`, `copilotapp.exe`, `Claude.exe`.
   - *Task:* **Stage 2** (`daily_omnisync_archive_mining.py --skip-mining` per verifica forense `entries == lexicon` byte-for-byte e controllo slot scenari Wyvern).
3. **Tier 3 (`lore-judge` — Effort `high`):**
   - *Modelli IDE Primari:* `claude-opus-5.5` & `gemini-4-argon` (subagent `pro`).
   - *Twin / Proxy `:5005` & Client Desktop:* `nvidia/nemotron-3-ultra-550b-a55b:free`, `z-ai/glm-5.3`, `deepseek-chat`, `Claude.exe`.
   - *Task:* **Stage 3A** (`daily_character_enrichment.py` per monitoraggio chat attiva e arricchimento batch NPC) e **Stage 3B** (`archive_mining_engine.py` per estrazione lore storica in `knowledge/Archive_Recoveries/`).
4. **Specialisti Desktop Dedicati con Vincolo di Scopo Esclusivo (`special_routing_policies`):**
   - **`Grok Bot.exe` — Ecosistema *Groky* (`groky_agenda_work_slots`):** In `Grok Bot.exe` opera **Groky** (assistente principale per Gmail, Agenda Google Calendar con feste italiane/Ásatrú e legenda colori condivisa con Davide, Casa/Google Home con sveglia alle 10:00, Pasti/Spesa) che coordina i 5 sotto-bot: **Hubby Groky** (mail/agenda di Davide e promemoria 20:30), **Purrky** (casa e gatti Rocky e Tatina, umido 19:30), **Game Groky** (serate co-op con Davide), **Code Groky** (progetti di sviluppo/design e riordino PC spostando solo nel Cestino) e **Hire Me Groky** (CV e lavoro). L'Orchestrator di Svartúlfr Verse inoltra a **Groky / Code Groky** **esclusivamente** le richieste di blocco slot di lavoro in agenda per lo sviluppo dell'ambientazione (`agenda_work_slot`, `work_slot_blocking`, `worldbuilding_schedule`), rispettando sempre la regola aurea di Groky: **nessuno invia o cancella nulla senza l'OK esplicito dell'utente**.
   - **`Gemini.exe` (`visual_studio_argon_images`):** Riservato **esclusivamente** (tramite modello **Gemini 4 Argon**) alla creazione e generazione delle immagini dell'ambientazione (`image_generation`, `visual_asset_creation`, `character_portrait`, `location_background`).
5. **Stage 4 (Telemetria & Archiviazione Unificata):**
   - Generazione della Dashboard interattiva HTML (`scratch/unified_pipeline_dashboard.html`), report Markdown unificato (`scratch/daily_maintenance_report.md` e `logs/automations/`) e archiviazione del transcript tramite `python scripts/archive_automation_chat.py --automation daily-master-pipeline`.

