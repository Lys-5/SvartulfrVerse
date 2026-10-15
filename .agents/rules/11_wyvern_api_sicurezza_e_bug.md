# Regola 11 — Wyvern Web API: Protocolli di Sicurezza e Risoluzione Bug

## 1. Fonte di Verità e Regole di Accesso

- **Sito Wyvern come Fonte di Verità:** Il sito ufficiale (`app.wyvern.chat`) costituisce l'unica sorgente di verità attiva del World. Il lavoro avviene direttamente sulla piattaforma.
- **Divieto di Fetch Diretto:** Ogni consultazione web di fonti esterne (wiki, documentazione, canali Discord) deve passare attraverso il browser locale aprendo la pagina nella scheda di navigazione, **mai** tramite HTTP fetch diretto senza rendering.
- **Fonti Documentali (Gerarchia):**
  1. *WyvernWiki* (`https://wiki.wyvern.chat/`, consultare le sezioni `/en/Features/Worlds/...`).
  2. Canale `#dev-notes` sul Discord ufficiale Wyvern per le novità non ancora documentate.
  3. Reddit (`r/WyvernChat`) e canali di supporto Discord.
  *Nota sul Disaccordo Wiki-Piattaforma:* Qualora la wiki e la piattaforma divergano, fa fede il comportamento empirico verificato da una chiamata GET autenticata fresca.

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
