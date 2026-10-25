---
name: wyvern-ttrpg-master-deployer
description: >-
  Pipeline per la progettazione, compilazione Handlebars/XML, deployment via
  Wyvern Web API e validazione con Chrome DevTools di AI Game Master (Assistant),
  Custom Prompt Assembly e Character Scenarios con motore D20 + S.P.E.C.I.A.L.
---

# Wyvern TTRPG Master & Prompt Assembly Deployer

Questa skill codifica e automatizza la pipeline per la creazione, la compilazione modulare, il deployment su Wyvern Web API e la verifica via Chrome DevTools di entità Game Master (`simple-assistant-config`), Prompt Assembly multilivello (`prompt-assembly`) e Character Scenarios (`character-scenarios`).

---

## 1. Architettura delle Entità Wyvern

### 1.1 Assistant / Game Master (`kind: "narrator"`)
- **Endpoint:** `POST /api/simple-assistant-config` e `PUT /api/simple-assistant-config/:id`
- **Identificativo:** `simple_assistant_...`
- **Ruolo:** Agisce da Living World Engine (narrazione terza persona presente, gestione ambiente e PNG secondari, sovranità assoluta di `{{user}}`, zero puppeting, privacy dei pensieri `*...*`).
- **Invarianti di Formattazione:** Dialoghi tra virgolette `"..."`, azioni in testo semplice (senza asterischi), zero trattini lunghi (divieto assoluto em-dash `—`), formato dialoghi PNG su riga autonoma `Nome: "..."`.

### 1.2 Custom Prompt Assembly (`pha_...`)
- **Endpoint:** `POST /api/prompt-assembly` e `PUT /api/prompt-assembly/:id`
- **Architettura a 4 Livelli:**
  1. `main_prompt_template`: Handlebars con macro di base (`{{system}}`, `{{#if wiBefore}}`, `<character name="{{char}}">`, `<user_persona name="{{user}}">`, `{{#if summary}}`, ecc.).
  2. `lore_template`: Template XML polimorfico con selettori Handlebars condizionali (`{{#if (eq type "npc")}} <npc name="{{name}}"> {{content}} <special_stats>{{rpg_stats}}</special_stats> </npc> ... {{/if}}`), delimitato da `lore_template_header` e `lore_template_footer` (`<world_context...>`).
  3. `floating_prompt_template`: Fluttuante al 4% di profondità (`floating_depth_percent: 4`) con ruolo obbligatorio **`user`** (`floating_role: "user"`) per annullare l'English Drift e i bias di compiacenza.
  4. `blocks`: Array di sezioni post-history ordinate con ruolo HTTP **`user`** (user boundaries, multi-character format, risoluzione D20, feed digitali situazionali, closer italiano).

---

## 2. Motore Meccanico D20 + S.P.E.C.I.A.L.

1. **Attributi Canonici:** `STR`, `PER`, `END`, `CHA`, `INT`, `AGI`, `LCK`.
2. **Formula del Modificatore:**
   $$\text{Mod} = \left\lfloor \frac{\text{Stat} - 10}{2} \right\rfloor$$
3. **Classi di Difficoltà (CD / DC):** 10 (Facile), 15 (Media), 20 (Difficile), 25 (Estrema), 30 (Eroica).
4. **I 4 Gradi di Risoluzione:**
   - *Successo Critico:* Nat 20 o Margine $\ge +10$ rispetto alla CD.
   - *Successo Pieno:* Totale $\ge \text{CD}$.
   - *Successo con Costo / Fallimento Parziale:* Margine tra $-1$ e $-4$.
   - *Fallimento Critico:* Nat 1 o Margine $\le -10$.
5. **Isolamento Diegetico:** I calcoli devono comparire esclusivamente nel blocco isolato all'inizio o alla fine del messaggio:
   ```markdown
   > [TEST: <Attributo> (D20: <Tiro> + <Mod> = <Totale> vs DC <Target>) -> ESITO: <SUCCESSO / FALLIMENTO / SUCCESSO CRITICO / FALLIMENTO CRITICO>]
   ```
   La prosa successiva è puramente letteraria e priva di numeri o percentuali.

---

## 3. Pipeline Operativa di Deployment in 4 Fasi

### Fase 1: Verifica Token ed Esplorazione Schemi
1. Verificare la validità del Bearer token in `scratch/wyvern_token.txt`. Se risponde HTTP 500 (`Unauthorized`), eseguire `python scratch/refresh_token.py` (scambio con Google Firebase Secure Token API) senza interrompere il flusso.
2. Recuperare lo schema live o l'entità di confronto tramite `GET /api/simple-assistant-config/:id` o `GET /api/prompt-assembly/:id`.

### Fase 2: Costruzione e Validazione Statica dei Payload
1. Costruire il file JSON locale in `FINAL/assistants/` o `FINAL/prompts/`.
2. Eseguire scansione automatica per:
   - Assenza assoluta di em-dash unicode (`—` / `\u2014`) nei corpi testo e prompt.
   - Presenza del Sandwich Linguistico Italiano in testa e in coda.
   - Configurazione esplicita di `visibility: "private"`.
   - Ruolo `user` su floating prompt e blocchi terminali.

### Fase 3: Esecuzione Chiamata API & Verifica di Persistenza
1. Effettuare la chiamata `POST` (o `PUT`) a `https://app.wyvern.chat/api/...`.
2. Verificare l'esito `HTTP 200 OK` o `HTTP 201 Created` ed estrarre l'ID generato (`simple_assistant_...` o `pha_...`).
3. Eseguire una `GET` autenticata fresca rileggendo l'ID sul cloud di Wyvern per confermare byte per byte la persistenza dei dati.

### Fase 4: Validazione DOM, Rete e Console (Chrome DevTools)
1. Connettersi alla sessione Chrome aperta (porta 9222) o verificare la console di navigazione.
2. Ispezionare il DOM per confermare la corretta resa dei campi, assenza di allarmi di validazione form e assenza di errori runtime JavaScript (`console.error`).
3. Registrare i metadati di deployment in `CHANGELOG.md` e aggiornare le regole del repository.

---

## 4. Utility Scripts

La skill include utility script dedicati in `scripts/` conformi al pattern CLI:

### 4.1 `scripts/verify_chat_overrides.py`
CLI modulare per interrogare le API di Wyvern, validare assistant, assembly e chat, e gestire il refresh automatico dei token:

```bash
# Refresh automatico token Firebase
python .agents/skills/wyvern-ttrpg-master-deployer/scripts/verify_chat_overrides.py refresh-token

# Verifica Simple Assistant / Game Master
python .agents/skills/wyvern-ttrpg-master-deployer/scripts/verify_chat_overrides.py verify-assistant --id simple_assistant_xRfBnV7wq48QppqbPPpTM --output scratch/verified_assistant.json

# Verifica Prompt Assembly
python .agents/skills/wyvern-ttrpg-master-deployer/scripts/verify_chat_overrides.py verify-assembly --id pha_kWkWUAfTJTF9q72c2bC98 --output scratch/verified_assembly.json

# Audit Completo End-to-End
python .agents/skills/wyvern-ttrpg-master-deployer/scripts/verify_chat_overrides.py full-audit --assistant-id simple_assistant_xRfBnV7wq48QppqbPPpTM --assembly-id pha_kWkWUAfTJTF9q72c2bC98 --chat-id chat_log_qUdWrgx232YGtwDE2318a --output scratch/audit_report.json
```

### 4.2 `scripts/inspect_chrome_cdp.js`
Script Node.js per interagire in sicurezza con il Chrome Remote Debugger Protocol:
- Individua la porta attiva leggendo `DevToolsActivePort`.
- Connette via WebSocket al target specificato.
- Ispeziona lo stato dei controlli (toggles, switches, badges).
- Chiude immediatamente la connessione con `ws.close()` e `process.exit(0)` per rispettare la regola del single-client.

### 4.3 `scripts/sync_scenarios_suite.py`
CLI Python per la sincronizzazione atomica dei Character Scenarios con protezione di concorrenza `revision`:
- Recupera via GET fresca lo snapshot dello scenario per prevenire HTTP 409.
- Assegna la suite unificata dei 15 Lorebook (`_gwwCxCfQ6PQaLEjAQVpJL`, `_HfG7TeV6MJyj6bxMwxkpt`, `_9zWTGqYJNJ4BCDMj8gfcD`, `_EjXxkmPVhpCXg8xABpFkK`, `_Uht3Ckz44JBDrPnUHq7LV`, `_zwEqgEEzh12X6gHVmMKKC`, `_GV1KyHVY1RMbCnWgLkzDG`, `_GbWJbkhgLzWexMHrjyUUc`, `_FaVcHfmrqcaJq8pa3WmRw`, `_BbrRgrcdGPMLEbBU2b6xk`, `_gchmML4Q478zdFjhXf8rN`, `_brNyzEdhzNAyxK8xC8hhm`, `_YtKLMTwyMxNf1DNYqBx1t`, `_b9HgpUXtAW8VmTy82BPDV`, `_c8bEm1bWphwqFBXWRPrV8`).
- Inietta le Persona offerte nei rispettivi greetings (`linked_persona_ids`) per consentire il forking istantaneo (Alyssa e Jasper).
- Invia il `PUT` autenticato con Bearer token e persiste i dati nei JSON locali (`FINAL/scenarios/*.json` e `FINAL/Svartulfr_Master_Scenario.json`).

---

## 5. Rate Limiting e Gestione Token

- **Rate Limits Web API:** L'API di Wyvern ammette un regime confortevole per le operazioni ordinarie (fino a 2-3 req/s). Rispettare un backoff esponenziale in caso di transient error.
- **Auto-Refresh Firebase Token:** Se l'API restituisce HTTP 500 con body `Unauthorized`, rinnovare tempestivamente il token tramite `scratch/refresh_token.py` e ritentare la chiamata senza richiedere l'intervento dell'utente.

---

## 6. Errori Comuni e Best Practice

1. **Chrome DevTools Single-Client Hang:**
   Chrome non ammette connessioni simultanee al debugger sullo stesso target. Se una connessione esterna resta appesa, tutte le successive chiamate andranno in timeout. Assicurarsi che ogni script chiami esplicitamente `ws.close()`.
2. **Divieto Assoluto Em-Dash (`—`):**
   I prompt per Assistant e Assembly non devono mai contenere l'em-dash unicode (`\u2014`). Usare virgole, due punti o punti.
3. **Ruoli HTTP nei Blocchi Assembly:**
   I blocchi terminali e il floating prompt devono avere rigorosamente ruolo `user`. L'uso del ruolo `system` per i blocchi fluttuanti viene spesso de-prioritizzato o ignorato dai modelli di ultima generazione.
4. **Requisito `can_fork: true` su Persona Offerte:**
   Qualsiasi Persona offerta in uno scenario tramite `linked_persona_ids` deve avere `can_fork: true` verificato via `/api/user-personas/:id`, altrimenti l'API restituisce `HTTP 400 Bad Request`.
5. **Concorrenza `revision` negli Scenari (HTTP 409 Conflict):**
   Ogni aggiornamento `PUT /api/character-scenarios/:id` deve includere il contatore `revision` incrementato, recuperato tramite una GET fresca immediatamente prima dell'invio.
