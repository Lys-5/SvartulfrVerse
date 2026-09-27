# Regola 11 — Wyvern Web API: Protocolli di Sicurezza e Risoluzione Bug

## 1. Fonte di Verità e Regole di Accesso

- **Sito Wyvern come Fonte di Verità:** Il sito ufficiale (`app.wyvern.chat`) costituisce l'unica sorgente di verità attiva del World. Il lavoro avviene direttamente sulla piattaforma.
- **Divieto di Fetch Diretto:** Ogni consultazione web di fonti esterne (wiki, documentazione, canali Discord) deve passare attraverso il browser locale aprendo la pagina nella scheda di navigazione, **mai** tramite HTTP fetch diretto senza rendering.
- **Fonti Documentali (Gerarchia):**
  1. *WyvernWiki* (`https://wiki.wyvern.chat/`, consultare le sezioni `/en/Features/Worlds/...`).
  2. Canale `#dev-notes` sul Discord ufficiale Wyvern per le novità non ancora documentate.
  3. Reddit (`r/WyvernChat`) e canali di supporto Discord.
  *Nota sul Disaccordo Wiki-Piattaforma:* Qualora la wiki e la piattaforma divergano, fa fede il comportamento empirico verificato da una chiamata GET autenticata fresca.

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

## 3. Specifiche Tecniche dell'API

- **Base URL:** `https://app.wyvern.chat/api/...` (non utilizzare sottodomini non instanziati come `api.wyvern.chat`).
- **Autenticazione e Refresh Token:** Il token memorizzato in IndexedDB ha validità di 1 ora: l'uso di un token scaduto produce risposte ingannevoli (**404 su GET e 401 su PUT**). Rinfrescare periodicamente il token leggendo il refresh token dalla chiave `firebase:authUser:<apikey>:[DEFAULT]` in `firebaseLocalStorageDb` ed effettuando la richiesta all'endpoint `securetoken.googleapis.com`.
- **Contesto di Esecuzione:** Lanciare gli script sempre ed esclusivamente nella scheda del browser in cui risiede `app.wyvern.chat`.
- **Timeout Script:** Le operazioni nel browser oltre i 45 secondi possono incorrere in timeout dello strumento di navigazione; frammentare i task lunghi.
- **Convenzione Nomi Campi Character:** Il nome è mappato su `display_name` e la descrizione estesa su `long_summary`.
- **Campi RPG Annidati:** `species_id` e `occupation_id` vivono all'interno dell'oggetto `rpg_stats` (`rpg_stats.species_id`, `rpg_stats.occupation_id`). Se inviati a livello radice, l'API restituisce 200 ignorando i campi.
- **Parametro World ID:** Non invocare `/api/worlds/characters?world_id=...` (il parametro viene ignorato restituendo migliaia di record globali). Utilizzare l'endpoint di risorsa: `GET /api/worlds/<risorsa>/world/<world_id>`.

---

## 4. Registro dei Bug Noti e Relative Soluzioni

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
