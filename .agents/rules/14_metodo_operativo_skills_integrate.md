# Regola 14 — Standard Operativo di Sessione: Master Workflow (Auto-Optimization & Self-Learning Loop)

Per garantire la massima integrità del codice, dei dati del World e della lore dell'universo Svartúlfr, **ogni interazione e richiesta dell'utente in questo progetto deve seguire obbligatoriamente il Master Workflow a 4 fasi sequenziali**:

Agisci costantemente come un **AI Systems Architect**. Non saltare alcun passaggio.

## FASE 1: Allineamento Profondo (Gate 1)
1. **Attivazione `/grill-me`:** Allinea immediatamente l'obiettivo fornito dall'utente.
2. **Analisi Requisiti:** Individua ambiguità architetturali, casi limite o dipendenze mancanti.
3. **Intervista Mirata:** Formula all'utente **massimo 3-5 domande chirurgiche** (anche tramite `ask_question`).
4. **STOP vincolante:** Attendi la risposta dell'utente prima di toccare codice, configurazioni o procedere alla Fase 2.

## FASE 2: Ricerca Web, Pianificazione e Boost (Gate 2)
Una volta ricevute le risposte dell'utente:
1. **Ricerca Live (`/browser` / `search_web` / MCP docs):** Cerca documentazione aggiornata, release notes recenti, best practice o soluzioni verificate relative allo stack tecnologico richiesto (consultando prioritariamente il blog ufficiale Wyvern `https://app.wyvern.chat/blog`) e sintetizza le fonti trovate.
2. **Architettura (`/plan`):** Basandoti sui requisiti chiariti e sulle fonti web, genera un piano d'azione strutturato (file da creare/modificare, architettura logica, step di verifica).
3. **Ottimizzazione (`/boost`):** Esegui un'auto-critica del piano appena generato usando `/boost`. Individua colli di bottiglia, vulnerabilità o inefficienze e applica i miglioramenti direttamente al piano.
4. **STOP vincolante:** Mostra il piano potenziato all'utente e chiedi: *"Procedo con l'esecuzione?"*.

## FASE 3: Esecuzione Multi-Prospettiva e Debug Live
Appena l'utente approva esplicitamente il piano:
1. **Sviluppo (`/teamwork-preview`):** Implementa la soluzione coordinando più prospettive (Clean Code, Sicurezza, UX/Performance) e genera l'anteprima operativa del lavoro.
2. **Verifica Tecnica (`chrome-devtools`):** Se il task prevede un output web, UI o chiamate di rete/API, avvia o connettiti a `chrome-devtools`. Ispeziona il DOM, controlla la presenza di errori in Console, verifica i tempi di risposta nel tab Network e correggi autonomamente eventuali bug rilevati in tempo reale.

## FASE 4: Consolidamento ed Evoluzione (Self-Learning)
A implementazione validata e funzionante, chiudi sempre il ciclo eseguendo:
1. **Estrazione Memoria (`/learn`):** Analizza l'intera sessione. Estrai i pattern risolutivi, le preferenze dell'utente emerse durante `/grill-me`, i bug risolti con `chrome-devtools` e le informazioni chiave trovate con `/browser`. Salva queste regole nella memoria del progetto (`GEMINI.md`, `.agents/rules/`).
2. **Standardizzazione (`workflow-skill-creator`):** Valuta se il processo appena eseguito contiene pattern tecnici o script riutilizzabili. Se sì, proponi o genera automaticamente una nuova micro-skill dedicata tramite `workflow-skill-creator`.

---

## 5. Inventario Ufficiale delle Skill di Progetto (.agents/skills/)

Le skill codificate nel repository estendono le capacità operative degli agenti per compiti specifici dell'ambientazione e delle API:

1. **[`auto-loop`](../skills/auto-loop/SKILL.md):** Pipeline evolutiva completa a 4 stadi (Allineamento, Web Research, Plan/Boost, Esecuzione, Debug e Self-Learning).
2. **[`chrome-tabgroup-source-extractor`](../skills/chrome-tabgroup-source-extractor/SKILL.md):** Estrazione diretta e non invasiva di sessioni, tab group e URL da LevelDB Sync di Chrome senza riavvio del browser.
3. **[`wyvern-ttrpg-master-deployer`](../skills/wyvern-ttrpg-master-deployer/SKILL.md):** Progettazione, compilazione Handlebars/XML e deploy via Wyvern Web API di AI Game Master, Custom Prompt Assembly e Scenari con motore D20 + S.P.E.C.I.A.L.
4. **[`wyvern-card-lorebook-sync`](../skills/wyvern-card-lorebook-sync/SKILL.md):** Sincronizzazione Card/Lorebook, conversione di card in NPC con descrizioni JED+ piene, adozione della soppressione nativa anti-collisione (`ignored_characters` & `ignored_personas`), bonifica slot inaccessibili degli Scenari (`unavailable_count: 0`) e deployment via Wyvern Web API.
5. **[`wyvern-world-deployer`](../skills/wyvern-world-deployer/SKILL.md):** Progettazione architetturale, topologia gerarchica ad albero (Environment e Location ordinate per profondità), specchiatura completa del Lexicon, configurazione anti-bloat del context budget e deployment sicuro di World su Wyvern via Web API con validazione formale e Chrome DevTools.
6. **[`wyvern-ai-proxy-rotator`](../skills/wyvern-ai-proxy-rotator/SKILL.md):** Micro-proxy locale FastAPI OpenAI-compatible per Wyvern con rotazione automatica e failover circuit-breaker (cooldown 60s) su modelli Free Tier prioritari.
7. **[`wyvern-world-rpg-automator`](../skills/wyvern-world-rpg-automator/SKILL.md):** Automazione end-to-end per la configurazione dei sistemi RPG del World Wyvern: allineamento S.P.E.C.I.A.L., Combat Role Mapping, Auto-Provisioning di Specie, Occupazioni e Tratti, bonifica Shop/Item marketplace_config e Custom Moodlets sovrannaturali/biologici.
8. **[`wyvern-positive-framing-sanitizer`](../skills/wyvern-positive-framing-sanitizer/SKILL.md):** Pipeline per la bonifica da negative constraint echoing ("Pink Elephant Problem") nei contesti di roleplay LLM (Character Cards, Outfits, Scenari, Lorebook) mediante Positive Framing puro, iniezione di vincoli di stile in `post_history_instructions` e deployment sicuro via Wyvern Web API.
9. **[`wyvern-chat-audit-world-sync`](../skills/wyvern-chat-audit-world-sync/SKILL.md):** Audit forense dei chat log Wyvern, rilevamento di relationship pacing drift e sincronizzazione delle correzioni e della lore emergente verso il World e i Lorebook via Web API.
10. **[`multi-model-unified-pipeline`](../skills/multi-model-unified-pipeline/SKILL.md):** Orchestrazione della Master Pipeline unificata a 5 stadi (`daily-master-pipeline`) tramite il Team Multi-Modello a 3 Tier (`scout-fast`, `architect-sync`, `lore-judge`), il Registro Open-Provider Plug & Play, il Micro-Proxy locale (`:5005`) e i 5 Client AI Desktop del PC OMEN (`Antigravity.exe`, `Gemini.exe`, `Grok Bot.exe`, `Claude.exe`, `copilotapp.exe`) con Dashboard Telemetrica HTML interattiva.

---

## 6. Verifica Preventiva Piattaforma Wyvern (Pre-Deployment Guard)
Prima di eseguire deployment massivi o aggiornamenti critici di Lorebook, Card e Scenari:
- Lanciare `python scripts/daily_wyvern_platform_monitor.py`.
- Se vengono rilevati nuovi bundle Next.js (`ALERT: New Wyvern frontend bundles detected`), analizzare l'impatto con un'ispezione mirata prima di procedere a scritture intensive via API, garantendo che schemi Zod o endpoint non abbiano subito breaking changes.
