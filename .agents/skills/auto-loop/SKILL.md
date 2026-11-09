---
name: auto-loop
description: Pipeline evolutiva completa (Allineamento, Web Research, Plan, Esecuzione, Debug e Self-Learning)
---

# Master Workflow: Auto-Optimization & Self-Learning Loop

Agisci come un AI Systems Architect. Quando questo workflow viene invocato, esegui rigorosamente le seguenti 4 fasi in ordine sequenziale utilizzando le skill di sistema. Non saltare alcun passaggio.

## FASE 1: Allineamento Profondo (Gate 1)
1. Attiva immediatamente la logica di `/grill-me` sull'obiettivo fornito dall'utente.
2. Analizza la richiesta, individua ambiguità architetturali, casi limite o dipendenze mancanti.
3. Fai all'utente **massimo 3-5 domande chirurgiche**.
4. **STOP:** Attendi la risposta dell'utente prima di procedere alla Fase 2.

## FASE 2: Ricerca Web, Pianificazione e Boost (Gate 2)
Una volta ricevute le risposte dell'utente:
1. **Ricerca Live (`/browser`):** Usa il browser per cercare documentazione aggiornata, release notes recenti, best practice o soluzioni verificate relative allo stack tecnologico richiesto. Sintetizza le fonti trovate.
2. **Architettura (`/plan`):** Basandoti sui requisiti chiariti e sulle fonti web, genera un piano d'azione strutturato (file da creare/modificare, architettura logica, step di verifica).
3. **Ottimizzazione (`/boost`):** Esegui un'auto-critica del piano appena generato usando `/boost`. Individua potenziali colli di bottiglia, vulnerabilità o inefficienze nel codice previsto e applica i miglioramenti direttamente al piano.
4. **STOP:** Mostra il piano potenziato all'utente e chiedi: *"Procedo con l'esecuzione?"*.

## FASE 3: Esecuzione Multi-Prospettiva e Debug Live
Appena l'utente approva il piano:
1. **Sviluppo (`/teamwork-preview`):** Implementa la soluzione coordinando più prospettive (Clean Code, Sicurezza, UX/Performance) e genera l'anteprima operativa del lavoro.
2. **Verifica Tecnica (`chrome-devtools`):** Se il task prevede un output web, UI o chiamate di rete, avvia o connettiti a `chrome-devtools`. Ispeziona il DOM, controlla la presenza di errori in Console, verifica i tempi di risposta nel tab Network e correggi autonomamente eventuali bug rilevati in tempo reale.

## FASE 4: Consolidamento ed Evoluzione (Self-Learning)
A implementazione validata e funzionante, chiudi sempre il ciclo eseguendo:
1. **Estrazione Memoria (`/learn`):** Analizza l'intera sessione. Estrai i pattern risolutivi, le preferenze dell'utente emerse durante `/grill-me`, i bug risolti con `chrome-devtools` e le informazioni chiave trovate con `/browser`. Salva queste regole nella memoria del progetto per ottimizzare le sessioni future.
2. **Standardizzazione (`workflow-skill-creator`):** Valuta se il processo appena eseguito contiene pattern tecnici o script riutilizzabili. Se sì, proponi o genera automaticamente una nuova micro-skill dedicata tramite `workflow-skill-creator`.

---

## Matrice di Orchestrazione Multi-Modello a 3 Tier & Unified Master Pipeline

Quando esegui o pianifichi task complessi o automazioni ricorrenti (`multi-model-unified-pipeline` / sidecar `daily-master-pipeline`), applica il routing gerarchico a 3 Tier registrato in `.agents/skills/multi-model-unified-pipeline/references/models_registry.json`:

| Tier | Ruolo Operativo | Modelli IDE Primari & Effort | Modelli Gemelli (`:5005`) & Client PC OMEN | Stage Unificati Assegnati |
| :--- | :--- | :--- | :--- | :--- |
| **Tier 1 (`scout-fast`)** | Health check, regex, monitoraggio bundle e lista modelli | `gemini-3.8-flash` (`low` / `medium`, subagent `flash` / `flash_lite`) | `gemma-4-31B-it`, `qwen-3.8-27b` (`:5005`) • `Gemini.exe` | **Stage 0** (`vault_health_check.py` + Scan PC OMEN Clients)<br>**Stage 1A** (`daily_wyvern_platform_monitor.py`)<br>**Stage 1B** (`proxy/update_free_models.py`) |
| **Tier 2 (`architect-sync`)** | Parità strutturale `entries == lexicon`, sync API e refactoring | `gemini-4-argon`, `claude-sonnet-5.5` (`medium`, subagent `inherit`) | `z-ai/glm-5.3`, `deepseek-chat` (`:5005`) • `copilotapp.exe` | **Stage 2** (`daily_omnisync_archive_mining.py --skip-mining`) |
| **Tier 3 (`lore-judge`)** | Sintesi narrativa JED+, audit forense chat e recupero lore | `claude-opus-5.5`, `gemini-4-argon` (`high`, subagent `pro`) | `grok-4`, `nvidia/nemotron-3-ultra-550b-a55b:free`, `z-ai/glm-5.3` (`:5005`) • `Grok Bot.exe`, `Claude.exe` | **Stage 3A** (`daily_character_enrichment.py`)<br>**Stage 3B** (`archive_mining_engine.py`) |

