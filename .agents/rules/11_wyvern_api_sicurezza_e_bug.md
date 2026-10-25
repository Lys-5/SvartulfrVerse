# Regola 11 — Wyvern Web API: Protocolli di Sicurezza e Risoluzione Bug

## 1. Fonte di Verità e Regole di Accesso

- **Sito Wyvern come Fonte di Verità:** Il sito ufficiale (`app.wyvern.chat`) costituisce l'unica sorgente di verità attiva del World. Il lavoro avviene direttamente sulla piattaforma.
- **Divieto di Fetch Diretto:** Ogni consultazione web di fonti esterne (wiki, documentazione, canali Discord) deve passare attraverso il browser locale aprendo la pagina nella scheda di navigazione, **mai** tramite HTTP fetch diretto senza rendering.
- **Fonti Documentali (Gerarchia):**
  1. *Wyvern Blog & Patch Notes* (`https://app.wyvern.chat/blog`): Fonte primaria e ufficiale per release notes, mega-patch, aggiornamenti architetturali (es. Visual Novel Mode, AI Time Tracking, modali NPC e Lorebook Sprites) e annunci degli sviluppatori.
  2. *WyvernWiki* (`https://wiki.wyvern.chat/`, consultare le sezioni `/en/Features/Worlds/...`).
  3. Canale `#dev-notes` sul Discord ufficiale Wyvern per le novità non ancora documentate.
  4. Reddit (`r/WyvernChat`) e canali di supporto Discord.
  *Nota sul Disaccordo Wiki-Piattaforma:* Qualora la wiki, il blog e la piattaforma divergano, fa fede il comportamento empirico verificato da una chiamata GET autenticata fresca.

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

## 2. Protocollo di Sicurezza per le Scritture via API

Le API di Wyvern consentono operazioni mirate estremamente rapide ed affidabili se eseguite rispettando i seguenti vincoli di sicurezza:

### Operazioni di Lettura (GET)
Sempre consentite senza autorizzazione preventiva. Costituiscono lo strumento raccomandato per audit, verifica di id reali, controlli di integrità e mappatura delle relazioni.

### Modifiche Mirate (PUT / POST)
Consentite quando attuano le richieste dell'utente. Sequenza obbligatoria:
1. **Snapshot Pre-Scrittura:** Eseguire una GET fresca dell'entità per salvare lo stato precedente (conservato in memoria e registrato nel documento di riepilogo del Project per operazioni su più entità).
2. **Identificazione tramite `id` Univoco:** Mai fare affidamento sui nomi delle entità (il World può ospitare omonimie o entità orfane). Lavorare unicamente sull'`id` validato presente nella lista attiva del World.
3. **Payload Parziale (Trappola del PUT Completo):** Inviare **esclusivamente** i campi oggetto di modifica. Un `PUT` contenente l'intero oggetto dell'entità restituisce HTTP 200 ma scarta silenziosamente le modifiche senza persistere nulla.
4. **Sostituzione Totale degli Array:** Gli array (`outfits`, `attitudes`, `speech_examples`, `keys`, `party_conditions`, `tags`) non supportano il merge incrementale: un payload con un singolo elemento sovrascrive e cancella tutti gli altri preesistenti. Leggere sempre l'array esistente, aggiornarlo in memoria e ritrasmettere l'array completo.
5. **Verifica Post-Scrittura con GET Fresca:** Uno status HTTP 200 non costituisce prova di persistenza dei dati. Verificare sempre rileggendo l'entità per `id` con una GET autenticata fresca.

### Operazioni di Massa (> 10 Entità)
Presentare preventivamente all'utente il piano dettagliato (entità, campi, valori proposti, criteri di calcolo) e attendere approvazione esplicita. Eseguire l'operazione a **lotti di massimo 25 entità**, memorizzando lo stato di avanzamento per consentire riprese pulite in caso di interruzione.

### Cancellazioni (DELETE)
Consentite **esclusivamente su richiesta esplicita dell'utente** con specifica indicazione dell'entità o categoria da rimuovere. Non esiste cestino di ripristino.
- Salvare l'intero contenuto dell'entità nel documento del Project prima di invocare il DELETE.
- Eseguire una singola cancellazione per chiamata (mai DELETE in loop automatici).
- Mai cancellare entità come effetto collaterale implicito di altre operazioni.

### Operazioni Vietate via API senza Richiesta Esplicita
- PUT con payload dell'oggetto completo.
- Modifiche ai parametri globali del World (`world_features`, calendario, `world_age`, parametri di viaggio e simulazione).
- Accesso a risorse esterne o di altri utenti.

---

## 3. Protocollo Anti-Data Loss per Lorebook Stand-Alone (/mine)

1. **Divieto Assoluto di Overwrite Massivo:** È fatto divieto tassativo a qualsiasi script o assistente AI di eseguire riscritture complete o sovrascritture di massa dell'array `lexicon` sui Lorebook stand-alone (`/api/lorebooks/:id`).
2. **Integrità dei Lorebook:** I Lorebook stand-alone in `/mine` costituiscono Single Source of Truth storica e manuale. Qualsiasi sincronizzazione o inserimento deve avvenire in modalità "append puntuale" singola voce, con verifica preventiva di schema e mai in sostituzione cieca dell'intero archivio.
3. **Backup Preventivo Obbligatorio:** Prima di qualsiasi operazione di scrittura su entità di libreria, scaricare e persistere una copia integrale JSON su disco locale.
4. **Context Budget Awareness:** Nelle richieste al World, monitorare che la somma dei metadati statici non superi mai i 5.000 token prima della chat history per evitare il troncamento della richiesta da parte del backend di Wyvern.
5. **Preservazione Obbligatoria Metadati Top-Level nei Lorebook:** L'endpoint `PUT /api/lorebooks/:id` non effettua merge parziale dei metadati. L'invio di un payload contenente solo `{ lexicon: [...] }` cancella silenziosamente i campi top-level (`name`, `description`, `scan_depth`, `token_budget`, `recursive_scanning`, `visibility`, `rating`, `is_private`). In qualsiasi operazione di aggiornamento di un Lorebook stand-alone è obbligatorio trasmettere l'intero payload di configurazione (recuperato con GET preventiva fresca o da snapshot locale) unitamente all'array `lexicon`.

---

## 4. Tipizzazione Rigorosa di `priority` e Validazione Schemi Zod

Il backend di Wyvern valida le voci di contesto, lorebook, scenari e lexicon tramite schemi Zod che impongono per il campo `priority` il tipo `z.number()`.
- L'assegnazione di valori stringa (es. `priority: "0"`, `"10"`, `"high"`) scatena un errore HTTP 500 fatale (`Expected number, received string, path: ["priority"]`) che inibisce la ricezione o l'invio di messaggi in chat.
- In ogni script o funzione di creazione/modifica entità, convertire esplicitamente: `priority: Number(val) || 0`.

---

## 5. Protocollo di Pulizia Post-Diagnostica (Zero-Footprint Testing)

Quando vengono avviate procedure di diagnosi, indagine o test che comportano la creazione programmata di entità temporanee via API (chat log di test come `chat_log_...`, party usa-e-getta o scenari sandbox):
1. **Tracciamento:** Lo script o l'agente deve memorizzare immediatamente in memoria o su scratch gli ID di ogni entità temporanea creata.
2. **Cancellazione Tempestiva:** A diagnosi completata (o in caso di errore), è obbligatorio eseguire la cancellazione sistematica delle entità create (`DELETE /api/new/chat-logs/:id`) per garantire che l'account e la libreria dell'utente rimangano perfettamente puliti e privi di artefatti orfani.

---

## 6. Specifiche Tecniche dell'API

- **Base URL:** `https://app.wyvern.chat/api/...` (non utilizzare sottodomini non instanziati come `api.wyvern.chat`).
- **Autenticazione e Refresh Token:** Il token memorizzato in IndexedDB ha validità di 1 ora: l'uso di un token scaduto produce risposte ingannevoli (**404 su GET e 401 su PUT**). Rinfrescare periodicamente il token leggendo il refresh token dalla chiave `firebase:authUser:<apikey>:[DEFAULT]` in `firebaseLocalStorageDb` ed effettuando la richiesta all'endpoint `securetoken.googleapis.com`.
- **Contesto di Esecuzione:** Lanciare gli script sempre ed esclusivamente nella scheda del browser in cui risiede `app.wyvern.chat`.
- **Timeout Script:** Le operazioni nel browser oltre i 45 secondi possono incorrere in timeout dello strumento di navigazione; frammentare i task lunghi.
- **Convenzione Nomi Campi Character:** Il nome è mappato su `display_name` e la descrizione estesa su `long_summary`.
- **Campi RPG Annidati:** `species_id` e `occupation_id` vivono all'interno dell'oggetto `rpg_stats` (`rpg_stats.species_id`, `rpg_stats.occupation_id`). Se inviati a livello radice, l'API restituisce 200 ignorando i campi.
- **Parametro World ID:** Non invocare `/api/worlds/characters?world_id=...` (il parametro viene ignorato restituendo migliaia di record globali). Utilizzare l'endpoint di risorsa: `GET /api/worlds/<risorsa>/world/<world_id>`.

---

## 7. Registro dei Bug Noti e Relative Soluzioni

| Comportamento Anomalo | Sintomo Riscontrato | Soluzione Operativa / Mitigazione |
|---|---|---|
| **Save Appeso in UI** | Il pulsante di salvataggio rimane indefinitamente su "Saving..." | I dati spesso risultano salvati sul backend. Ricaricare la pagina (F5) ed eseguire una GET di controllo; non cliccare a raffica. |
| **Species e Occupation da UI** | Selezionati dai combobox, dopo il reload tornano a `None` | Il form web non li inoltra. Salvarli unicamente via API iniettandoli nell'oggetto `rpg_stats`. |
| **Livello RPG Elevato** | Livelli $\ge 100$ causano il blocco irreversibile del salvataggio RPG | Imporre un tetto massimo a Livello 99 per chiunque superi il secolo di vita. |
| **Array Sovrascritti da UI** | Salvare più outfit simultaneamente dall'interfaccia ne salva uno solo | Da UI, salvare un outfit per volta con salvataggio intermedio. Via API, mandare l'array completo in un unico PUT. |
| **Endpoint `linked-characters`** | Errore 500 "Maximum call stack size exceeded" | Evitare la chiamata; non pregiudica l'operatività sulle singole card. |
| **PUT Completo Fallimentare** | Inviare l'intero JSON risponde 200 ma non aggiorna il database | Inviare solo payload parziali con i campi variati. |
| **Entry Lexicon Orfane** | La ricreazione di una card (nuovo id) lascia le vecchie Lexicon agganciate al vecchio id | Riconnettere o aggiornare `attached_world_character_id` e `party_conditions` puntandoli al nuovo id attivo. |
| **Falsi Negativi Ricerca UI** | La ricerca nel pannello laterale chat segnala "No elements match" | Utilizzare l'editor a pagina intera del World oppure eseguire una query GET via API. |
| **Cartelle Collassate UI** | Cliccare sul testo della cartella non la apre | Cliccare esclusivamente sulla freccetta/chevron (primo elemento button della riga), oppure usare l'API. |
| **Parent Location Vuota** | Creando una nuova Location il menu Parent non mostra opzioni | Salvare la location una prima volta come bozza, riaprirla e associare il parent. |
| **Wipe Metadati Lorebook PUT** | Inviare un PUT su `/api/lorebooks/:id` con solo `{ lexicon }` svuota `name`, `scan_depth` e `token_budget` | Trasmettere sempre i metadati completi del Lorebook (`name`, `description`, `scan_depth: 5`, `token_budget: 5000`, `recursive_scanning: true`) assieme al lexicon. |
| **Priority come Stringa (Errore Zod 500)** | `Expected number, received string, path: ["priority"]` blocca l'invio/ricezione di messaggi in chat | Forzare sempre la tipizzazione numerica `priority: Number(val) || 0` in tutte le entità e nei lexicon. |
| **Orfani da Testing (Zero-Footprint)** | Le chat e i party creati per test diagnostici restano visibili nella UI utente | Eseguire sempre il teardown sistematico (`DELETE /api/new/chat-logs/:id`) al termine di ogni sessione di test. |
| **PUT Character con Subdocumenti Mongoose (CastError)** | `Argument passed in must be a string of 12 bytes or 24 hex characters or an integer` | Nei `PUT /api/characters/:id` escludere sempre subdocumenti e record statistici Mongoose (`creator`, `statistics_record`, `entity_statistics`, `sprite_set`). Inviare solo array pulito di `EDITABLE_FIELDS`. |
| **Campo `pronouns` in Character Card** | `Expected object, received string` | Su Wyvern `pronouns` deve essere un oggetto completo `{ pronoun_subjective, pronoun_objective, pronoun_possessive_determiner, pronoun_possessive_pronoun, pronoun_reflexive }`, non una stringa come `"he/him"`. |
| **Daily Public Publish Limit (Limite 5 Card)** | `Daily public character publish limit reached` blocca la creazione via POST | Per le nuove card ad uso scenario, impostare sempre `visibility: "unlisted"` o `"private"`, aggirando il tetto giornaliero di pubblicazione pubblica e rendendole immediatamente disponibili nei Character Scenarios. |
| **Disallineamento Root/First Message Scenario** | `Validation error` o sovrascritture anomale nel primo messaggio del greeting | In `/api/character-scenarios`, `greeting.content` e `greeting.speaker_slot` a livello radice del greeting devono essere rigorosamente identici a `greeting.messages[0].content` e `greeting.messages[0].speaker_slot`. |
| **HTTP 413 Payload Too Large su Lorebook PUT** | `HTTP Error 413: Payload Too Large` durante il salvataggio di un Lorebook | Non includere nel payload JSON sia l'array legacy `entries` sia l'array canonico `lexicon` (raddoppia la dimensione). Inviare solo `lexicon` unitamente ai metadati top-level. |
| **Errore Caricamento Immagini su Singola Entry Lorebook** | L'upload diretto di file immagine/avatar nei singoli slot delle entry genera errori o fallimenti di persistenza | **Workflow Obbligatorio Gallery:** Non caricare file direttamente sulle singole entry. Caricare prima le immagini nella **GALLERY del Lorebook**, e successivamente selezionare l'immagine desiderata dalla Gallery per ciascuna entry (`entry.avatar`). |
| **HTTP 409 Conflict su Scenario PUT** | `HTTP Error 409: Conflict` durante l'aggiornamento di un Character Scenario | Lo scenario mantiene un contatore `revision` incrementale. Prima di inviare un `PUT`, eseguire sempre una `GET` autenticata fresca per recuperare l'ultimo intero di `revision`, fonderlo nel payload e trasmettere. |
| **Attivazione Involontaria Dossier Lorebook** | Un World Dossier enciclopedico si attiva in chat parlando del personaggio già presente come card/slot | Impostare tassativamente `selective: true` sui World Dossier del cast principale con `secondary_keys` dedicate archivistiche (`['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`), e bonificare le chiavi trigger isolate mono-parola (es. `'Alyssa'` -> `'Alyssa Telegram'`). |
| **HTTP 500 Unauthorized (Token Scaduto)** | Wyvern risponde con HTTP 500 e body `{"message": "Unauthorized", "code": "INTERNAL_ERROR"}` | Il Bearer token in `scratch/wyvern_token.txt` è scaduto. Eseguire automaticamente `python scratch/refresh_token.py` (scambio con Google Firebase Secure Token API) per rigenerare il token e ripetere la chiamata. Non interrompere il flusso né chiedere token all'utente. |
| **`can_fork: false` su Persona Proposta (HTTP 400)** | `HTTP 400 Bad Request: Only your own forkable personas can be offered` durante il salvataggio o l'avvio scenario | Verificare che ogni Persona collegata a uno scenario in `linked_persona_ids` abbia tassativamente `can_fork: true` su `/api/user-personas/:id`. Senza questo flag Wyvern inibisce l'assegnazione e il forking della Persona al giocatore. |
| **ID Persona Non Risolto (HTTP 404 su Persona GET)** | Chiamare `/api/user-personas/:id` con ID interni o hash non canonici restituisce 404 | Utilizzare sempre l'ID canonico numerico/ufficiale della Persona (es. `persona_1786335754946` per Alyssa e `1792155173728` per Jasper) anziché chiavi interne di database. |
| **Dispersione Persona Proposta (Mancata Offerta in Chat)** | Il banner "Offer a persona to play as" non compare avviando la chat da uno scenario | L'opzione non è un campo globale di scenario ma risiede dentro ciascun greeting: configurare `linked_persona_ids` per ogni singolo greeting in `greetings[]`. |

---

## 8. Protocollo Obbligatorio di Auto-Refresh Token Firebase (HTTP 500 Unauthorized)

- **Sintomo del Bug:** Quando il Bearer token di autenticazione scade, la Web API di Wyvern non risponde con HTTP 401, ma genera un ingannevole `HTTP 500 Internal Server Error` con payload:
  `{"error":"Internal Server Error","message":"Unauthorized","details":{"message":"Unauthorized","code":"INTERNAL_ERROR"}}`
- **Protocollo Automatico di Ripristino:**
  1. È tassativamente vietato interrompere l'operazione o chiedere all'utente un nuovo token manuale.
  2. L'assistente deve eseguire tempestivamente lo script `python scratch/refresh_token.py`.
  3. Lo script contatta la Google Firebase Secure Token API (`https://securetoken.googleapis.com/v1/token`) utilizzando il `refresh_token` permanente in `scratch/refresh_token.txt` e aggiorna silenziosamente `scratch/wyvern_token.txt` con un id_token fresco valido per un'altra ora.
  4. L'assistente ripete immediatamente la chiamata API interrotta.
- **Host Ufficiale Endpoints:** Utilizzare sempre `https://app.wyvern.chat/api/` (es. `/lorebooks/{id}`, `/character-scenarios/{id}`) e non `api.wyvern.chat`.

---

## 9. Endpoints e Schemi per Assistant e Custom Prompt Assembly

Con l'introduzione dei Game Master e dei preset di assemblaggio personalizzati, l'interazione via API adotta due endpoint autoritativi:

### 9.1 Simple Assistant Config (`POST /api/simple-assistant-config`, `PUT /api/simple-assistant-config/:id`)
- **Modello:** `SimpleAssistantConfig` (prefisso ID `simple_assistant_...`).
- **Campi Obbligatori:**
  - `title`: Nome identificativo dell'assistant.
  - `description`: Breve sintesi d'intento.
  - `kind`: `"narrator"` (per Game Master / Storyteller di scena) oppure `"sidechat"`.
  - `system_prompt`: Direttive primarie di sistema (Italian Sandwich, anti-puppeting, regole D20 S.P.E.C.I.A.L., multi-NPC `Nome: "..."`).
  - `final_instructions`: Chiusura post-history vincolante.
  - `visibility`: `"private"`, `"unlisted"`, `"friends"`, `"public"`.
  - `rating`: `"none"`, `"mature"`, `"explicit"`.
  - `tags`: Array di stringhe di categorizzazione.
  - `avatar`: URL immagine hostata su Cloudflare Wyvern.
- **Ambito Operativo Lorebook:** Negli Assistant, le istruzioni governano la narrazione; i Lorebook (`lorebook_ids`) si collegano a livello di Scenario e Chat, venendo formattati a runtime dal Prompt Assembly.

### 9.2 Custom Prompt Assembly (`POST /api/prompt-assembly`, `PUT /api/prompt-assembly/:id`)
- **Modello:** `PromptAssembly` (prefisso ID `pha_...`).
- **Architettura a 4 Livelli:**
  1. `main_prompt_template`: Handlebars template con macro (`{{system}}`, `{{#if wiBefore}}`, `<character name="{{char}}">`, `<user_persona>`, `{{#if summary}}`, ecc.).
  2. `lore_template`: Template XML polimorfico con selettori condizionali Handlebars (`{{#if (eq type "npc")}} <npc name="{{name}}"> {{content}} <special_stats>{{rpg_stats}}</special_stats> </npc> ... {{/if}}`), delimitato da `lore_template_header` (`<world_context...>`) e `lore_template_footer` (`</world_context>`).
  3. `floating_prompt_template`: Template fluttuante iniettato a profondità configurabile (`floating_depth_percent: 4`), configurato obbligatoriamente con `floating_role: "user"` per annullare English Drift e bias di compiacenza.
  4. `blocks`: Array ordinato di sezioni post-history (`label`, `role: "user"`, `order`, `enabled: true`, `content`).
- **Regola di Ruolo HTTP `user`:** Configurare i blocchi terminali e il floating prompt con ruolo `user` per forzare la massima priorità attentiva nei modelli moderni (Claude 3.5, GPT-4o, Qwen 2.5).

---

## 10. Chat Overrides e Protocollo DevTools CDP (Chrome Remote Debugging Single-Client Rule)

### 10.1 Architettura Overrides di Sessione Chat (`Overrides & Extras`)
All'interno di ciascuna sessione chat (accessibile da `Open Settings > AI Models > AI Settings & Overrides > Overrides & Extras`), Wyvern gestisce tre moduli di override per personalizzare la generazione:
1. **Narrator Turn:**
   - Gestito dallo switch `#narratorShowNpcThoughtsToggle` (`data-state="checked"`).
   - Selettore del profilo Narratore (`narrator_profile_id`): deve puntare all'Assistant registrato (es. `simple_assistant_xRfBnV7wq48QppqbPPpTM` - *"Svartúlfr — Game Master & World Engine"*).
   - Prospettiva di narrazione: impostata su `Third person`.
2. **Prompt Assembly Preset:**
   - Attivato dallo switch `#advancedPostHistoryToggle` (`data-state="checked"`).
   - Collegato al preset registrato (es. `pha_kWkWUAfTJTF9q72c2bC98` - *"Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)"*).
3. **Easy Parameters:**
   - Attivato dallo switch `#easyParametersToggle` (`data-state="checked"`).
   - Profilo di campionamento consigliato (*Storyteller / Balanced Roleplay*):
     - `Temperature`: `0.95` (o `1.0`)
     - `Min-P`: `0.08`
     - `Repetition Penalty`: `1.05`
     - `Presence Penalty`: `0.05`
     - `Min Tokens`: `100`

### 10.2 Protocollo CDP (Chrome DevTools Protocol) e Regola del Single-Client
Quando si eseguono verifiche automatizzate o ispezioni DOM sulla sessione browser attiva di Wyvern tramite Chrome Remote Debugging (`--remote-debugging-port=9222`):
1. **Discovery Porta Attiva:**
   Leggere sempre il file locale `%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort`. La prima riga contiene la porta effettiva e la seconda riga il percorso del browser WebSocket (`/devtools/browser/{guid}`).
2. **Connessione Diretta WebSocket:**
   Nelle versioni recenti di Chrome, le richieste HTTP verso `/json/version` o `/json/list` possono restituire `404 Not Found` per motivi di sicurezza di origine. La connessione deve essere aperta direttamente via WebSocket all'URL estratto da `DevToolsActivePort`.
3. **Regola Invalicabile del Single-Client (Hang Prevention):**
   Chrome ammette tassativamente **un solo client debugger attivo per volta** su un dato target. Qualsiasi script parallelo che tenta di connettersi resterà bloccato all'handshake.
   *Direttiva:* Ogni script di ispezione CDP Node.js/Python deve obbligatoriamente invocare `ws.close()` e `process.exit(0)` subito dopo aver completato la lettura o la manipolazione, evitando connessioni pendenti che bloccano l'agente o l'utente.

---

## 11. Specifiche Tecniche Character Scenarios: Suite 15 Lorebook & Offer a Persona to Play As

### 11.1 Suite Canonica a 15 Lorebook (`lorebook_ids`)
Gli scenari Wyvern (`/api/character-scenarios/:id`) supportano stabilmente la suite completa di 15 Lorebook senza limiti architetturali, purché la sequenza sia preservata e le voci rispettino le norme di igiene sulle keyword (zero `BROAD_KEYS` su NPC):
1. `_gwwCxCfQ6PQaLEjAQVpJL` — Lorebook I
2. `_HfG7TeV6MJyj6bxMwxkpt` — Lorebook II
3. `_9zWTGqYJNJ4BCDMj8gfcD` — Lorebook III (SUCC & Underworld)
4. `_EjXxkmPVhpCXg8xABpFkK` — Location
5. `_Uht3Ckz44JBDrPnUHq7LV` — NPC Secondary
6. `_zwEqgEEzh12X6gHVmMKKC` — NPC Primary
7. `_GV1KyHVY1RMbCnWgLkzDG` — A0 Behavioral Realism
8. `_GbWJbkhgLzWexMHrjyUUc` — A1 Physics
9. `_FaVcHfmrqcaJq8pa3WmRw` — A2 Social Realism
10. `_BbrRgrcdGPMLEbBU2b6xk` — A3 Medical Realism
11. `_gchmML4Q478zdFjhXf8rN` — A4 Cultural Realism
12. `_brNyzEdhzNAyxK8xC8hhm` — A5 Sex Position
13. `_YtKLMTwyMxNf1DNYqBx1t` — A5.5 Scene Tone
14. `_b9HgpUXtAW8VmTy82BPDV` — A6 World Realism
15. `_c8bEm1bWphwqFBXWRPrV8` — A7 Queer Realism

### 11.2 Gestione Per-Greeting di `linked_persona_ids` e Requisito `can_fork: true`
1. **Granularità nei Greetings:**
   La funzionalità "Offer a persona to play as" risiede all'interno di ciascun elemento dell'array `greetings` dello scenario:
   - `greeting.linked_persona_ids`: array di stringhe contenente gli ID canonici delle Persona (es. `['persona_1786335754946', '1792155173728']`).
   - L'API idrata automaticamente l'array speculare `greeting.linked_personas` (`persona_id`, `name`, `avatar`, `title`, `comment`).
2. **Obbligo Assoluto `can_fork: true`:**
   Prima di inserire un ID persona in `linked_persona_ids`, verificare via GET su `/api/user-personas/:id` che `can_fork` sia impostato a `true`. Se assente o false, l'API Wyvern rigetta il salvataggio dello scenario restituendo `HTTP 400 Bad Request: Only your own forkable personas can be offered`.
3. **Prevenzione Conflitti di Concorrenza (Anti HTTP 409 Conflict):**
   Il salvataggio tramite `PUT /api/character-scenarios/:id` richiede tassativamente il recupero preventivo dell'ultimo intero `revision` con una GET fresca autenticata prima dell'invio del payload.

---

## 12. Estrazione Non-Invasiva Risorse Web da Chrome Sync LevelDB (Offline Tab Groups)

### 12.1 Limiti CDP e Single-Client Lock
Quando Chrome è avviato con debugging remoto abilitato (`--remote-debugging-port=9222`), l'ispezione runtime presenta frequenti ostacoli sistemici:
1. **Single-Client Lock:** L'IDE host (es. Antigravity) mantiene spesso una connessione WebSocket attiva sul target debugger. Ulteriori tentativi di connessione paralleli restano in hang indefinito fino al timeout.
2. **Restrizioni di Origine Chrome 118+:** Chiamate HTTP verso `/json` o `/json/version` possono restituire `404 Not Found` se le intestazioni `Host` o `Origin` non corrispondono ai parametri di sicurezza ristretti del browser.
3. **Divieto di Riavvio / Kill:** Uccidere o riavviare Chrome per forzare parametri CLI (`--remote-allow-origins=*`) è inaccettabile poiché causa perdita di stato, form non salvati e disturbo operativo per l'utente.

### 12.2 Architettura di Estrazione Sync LevelDB
Chrome memorizza la struttura dei gruppi di schede salvati ("Saved Tab Groups") e le relative entità URL nel database LevelDB di sincronizzazione locale:
- **Percorso Windows:** `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Sync Data\LevelDB\*.ldb` e `*.log`.
- **Meccanismo di Risoluzione:**
  1. Scansione in sola lettura (modalità binaria `rb`) dei file `.ldb` e `.log` per rintracciare il nome del gruppo (es. `"RPG Source"`).
  2. Identificazione del GUID univoco associato al gruppo tab (formato `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).
  3. Correlazione delle entità tab sincronizzate che contengono il GUID e parsing chirurgico di URL e titoli associati.
  4. Esclusione deterministica di tab appartenenti a gruppi adiacenti tramite verifica del perimetro di delimitazione tra GUID e URL.
- **Skill Dedicata:** Operazione automatizzata tramite la micro-skill standardizzata `.agents/skills/chrome-tabgroup-source-extractor/` (`scripts/extract_tabgroup.py`).

### 12.3 Integrazione nel Knowledge Index di Progetto
Ogni volta che vengono acquisite nuove fonti web esterne per il progetto:
1. **Aggiornamento Statistiche (Sezione 2):** Ricalcolare e aggiornare i totali esatti in `EXTERNAL_RESOURCES_INDEX.md` (distinguendo Canonical, Community ed Experimental).
2. **Sottosezione Tematica (Sezione 3):** Censire ogni risorsa con nome in grassetto, URL in backtick, livello di autorità e note operative d'uso.
3. **Tracciamento Cronologico (`CHANGELOG.md`):** Registrare l'integrazione citando l'acquisizione LevelDB e la mappatura al motore di gioco (D20 / S.P.E.C.I.A.L.).
4. **Disciplina Tipografica:** Nessun em-dash (`—`) nelle sezioni aggiunte o modificate.




---

## 13. Standard Operativo AI Connections Wyvern & Micro-Proxy di Failover

### 13.1 Architettura Connessioni Esterne e Parametro Browser-Only
- **Flag Browser-Only per Endpoints Locali:** Quando si utilizzano proxy locali, gateway di rotazione su `127.0.0.1` o host LAN, impostare tassativamente `browser_only: true` (Local Network / Browser-Only) nel Provider di Wyvern. Questa opzione ordina al frontend nel browser di effettuare la chiamata HTTP direttamente dal client all'indirizzo locale, senza passare dai server cloud di Wyvern.
- **Supporto CORS Obbligatorio sui Proxy Locali:** I server gateway locali (FastAPI, Express o script dedicati) devono implementare l'abilitazione esplicita di `CORSMiddleware` con `allow_origins=["*"]`, `allow_credentials=True`, `allow_methods=["*"]` e `allow_headers=["*"]`. Ciò previene il blocco delle chiamate preflight `OPTIONS` emesse da `https://app.wyvern.chat`.

### 13.2 Disciplina Rigorosa dei Max Tokens (Generazione vs Contesto)
Nelle configurazioni di Wyvern (`AI Connections -> Connections`) è categorico distinguere due parametri con ruoli radicalmente diversi:
1. **Context Window (`max_tokens` a livello top-level):** Definisce l'ampiezza massima della memoria e della cronologia valutata (es. `1000000` per GLM-5 o Gemini).
2. **Generation Max Tokens (`parameters.max_tokens`):** Definisce il limite massimo di token generabili per singolo turno di risposta dal modello.
   - *Valore Obbligatorio:* Mantenere rigorosamente tra `2048` e `8192` (valore ottimale di default: `4096`).
   - *Errore Critico Evitato:* Inserire il valore della context window (es. `200000` o `1000000`) nel parametro `parameters.max_tokens` provoca l'immediato rigetto della chiamata da parte delle API upstream con errori di schema o budget di generazione ecceduto.

### 13.3 Circuit-Breaker e Quarantena Temporizzata (60s)
I gateway multiprovider o i proxy di failover devono implementare una quarantena temporizzata automatica (cooldown) di almeno 60 secondi:
- **Trigger:** Errori HTTP `429` (Rate limit esaurito), `403` (Quota esaurita o piano free in pausa temporanea), `5xx` (Server down) o Timeout di connessione (`>12s`).
- **Comportamento:** Il modello in errore viene posto in cooldown in-memory. Le richieste successive per i 60 secondi successivi saltano istantaneamente l'upstream guasto senza attendere timeout di rete, instradandosi immediatamente sulla priorità successiva della cascata.
- **Hot-Reload:** Il file di configurazione (`config_free_proxy.json`) deve essere monitorato tramite timestamp `mtime` per ricaricare le chiavi inserite dall'utente senza riavviare il servizio demone.
