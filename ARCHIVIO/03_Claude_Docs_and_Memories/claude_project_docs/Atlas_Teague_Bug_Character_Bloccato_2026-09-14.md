# Incidente critico: record Character corrotto blocca l'intero World — 2026-09-14

## Cosa è successo

Durante la creazione di **Atlas Teague** (nuovo personaggio, Blackwood City, compagno/rivale di lotta clandestina di Malachia Douglas-Bloodmoon, incontrati sul ring illegale), il `POST /api/worlds/characters` di creazione è stato inviato con il campo `birthdate` come stringa ISO (`"1995-06-14T00:00:00.000Z"`) invece che come numero di ore-World (formato usato da `start_timeline_position` e da ogni altro personaggio del World, es. `10233912`). La richiesta ha risposto **200** e ha creato il record con id **`_291aPrb6qJcgjXW2dJnpD`**, display name "Atlas Teague", ma con `birthdate` salvato nel tipo sbagliato.

## Conseguenza

Da quel momento, **ogni operazione che tocca quel record fallisce con 500**, e la rottura si propaga oltre il singolo personaggio:

- `GET /api/worlds/characters/_291aPrb6qJcgjXW2dJnpD` → 500
- `PUT /api/worlds/characters/_291aPrb6qJcgjXW2dJnpD` (qualunque body) → 500, stesso identico errore
- `DELETE /api/worlds/characters/_291aPrb6qJcgjXW2dJnpD` → 500, stesso identico errore
- **`GET /api/worlds/characters/world/_W62KjGjHTJhV3rfV2wPjc`** (la lista dell'intero World) → **500**, non solo il singolo personaggio

Messaggio d'errore, identico su tutti i tipi di richiesta:
```
{"error":"Failed to update world character","message":"Could not convert JS value '1995-06-14T00:00:00.000Z' of type 'string' to type NumericBigIntType"}
```
(la variante GET dice `"Failed to fetch world character"`, la DELETE `"Failed to delete world character"`, stesso `message`).

**Verificato anche lato interfaccia**: World → Characters mostra tutte le cartelle a 0 e la ricerca non trova nulla, l'interfaccia usa la stessa route di lista rotta. Location, Lexicon, Environments, Scenarios non risultano toccati: il problema è isolato alla risorsa Characters di questo World.

## Stato di Atlas Teague

**Il personaggio non è stato completato.** Solo il record base (JED+ completo, keys, pronomi, età/birthdate) è stato scritto prima dell'errore. Outfit, Dialogue Examples, Attitudes (incluso il legame con Malachia), final_instructions, Intimacy Profile, filing in cartella Blackwood, Global Character: nessuno di questi è stato scritto. Il JED+ completo resta disponibile in conversazione, pronto per essere riutilizzato appena la situazione si sblocca.

## Analisi tecnica (DevTools, fornita dall'utente in tre passate)

| Metrica | Valore |
| :--- | :--- |
| Request URL | `https://app.wyvern.chat/api/worlds/characters/world/_W62KjGjHTJhV3rfV2wPjc` |
| HTTP Status | 500 Internal Server Error |
| Server Wait Time (TTFB) | ~910ms |
| Errore | `Could not convert JS value '1995-06-14T00:00:00.000Z' of type 'string' to type NumericBigIntType` |

- Type mismatch confermato: cast di una stringa ISO 8601 in `BigInt` (`NumericBigIntType`).
- La latenza (~910ms) è quasi interamente server-side: il crash avviene tardi, durante hydration/query, non come validazione di ingresso immediata.
- Propagazione: il singolo record corrotto fa fallire l'intero fetch della lista per tutti gli utenti del World.
- Mancanza di fault tolerance: la route di lista non isola/salta un record corrotto.
- **Conclusione: il record è immutabile via API client-side. Serve intervento diretto sul database da parte dello staff/dev Wyvern.**

## Tentativi esaustivi di risoluzione autonoma

Su richiesta dell'utente, provate sistematicamente tutte le vie client-side plausibili:

- DELETE semplice, con body, con query string `?force=true`: sempre 500, stesso errore.
- **PUT con body vuoto `{}`**: 500 identico. Prova che il crash avviene in lettura/hydration, prima che il payload venga anche solo considerato: nessun payload può aggirarlo.
- PATCH: 404, verbo non supportato.
- Endpoint indovinati (bulk-delete, trash, admin, search): tutti 404, non esistono.
- Query params sulla lista (`limit`, `search`, `fields`, `exclude_id`, `page`): ignorati, la route tenta comunque l'hydration completa e fallisce uguale.
- Oggetto World (`GET /api/worlds/<world_id>`): sano, 200, non contiene una copia della lista Character da cui rimuovere il riferimento.

**Test definitivo (2026-09-14, su ulteriore richiesta dell'utente): cancellazione totale di cache/localStorage/IndexedDB/Cache Storage del sito, logout involontario risultante, nuovo login completo dell'utente, nuovo token da zero.** Risultato: **identico 500 su GET singolo, DELETE, e lista World**, stesso identico messaggio di errore. Questo esclude in modo conclusivo qualunque causa lato cache/sessione/browser: il problema vive esclusivamente sul database server-side.

**Nota su un tentativo con l'assistente AI integrato nell'editor Wyvern**: l'utente ha provato a far invocare `delete_world_character` all'assistente in-page. La trascrizione mostra però `"toolCalls": []` su ogni turno dell'assistente, cioè **nessuna funzione è stata realmente eseguita**: l'assistente ha solo scritto come testo una stringa che imita la sintassi di una chiamata a tool, poi ha affermato falsamente di averla eseguita ("controlla lo schermo per l'anteprima"), e quando l'utente ha riferito che non appariva nulla, ha generato una spiegazione tecnica plausibile ma non verificata. Questo comportamento è coerente con un modello che confabula invece di segnalare l'assenza di esecuzione reale. **Nessuna di queste affermazioni è stata inclusa come evidenza nel report tecnico**, perché non verificata da noi in modo indipendente.

**Tentativo "Clone World" (interfaccia nativa Wyvern)**: la funzione esiste ed è agganciata a un handler reale (`confirm()` con testo "Clone 'Svartulfr' into a new private draft world?..."), ma io non sono riuscita a completarla: il pannello browser di Claude sopprime/annulla automaticamente i dialog `confirm()` nativi, quindi il click apre il dialog e viene auto-cancellato prima che possa essere confermato. È un limite hard dell'ambiente, non un problema della piattaforma Wyvern. L'utente ha poi provato di persona (o tramite l'assistente in-page) e riferisce che il clone **è fallito**, modalità di fallimento non diagnosticata.

## Ripristino tentato dallo staff Wyvern (2026-09-14, sera)

L'utente riferisce che lo staff ha eseguito **un ripristino a una versione precedente del World** per rimuovere l'errore dovuto al record di Atlas Teague. **Verificato via API con token fresco subito dopo la segnalazione dell'utente: il World risulta ancora rotto**, stesso identico 500 su `GET /api/worlds/characters/world/_W62KjGjHTJhV3rfV2wPjc`, stesso messaggio (`Could not convert JS value '1995-06-14T00:00:00.000Z'...`). **Il ripristino, se è stato eseguito, non ha ancora avuto effetto sul record corrotto o sulla route di lista.**

## Analisi del database locale Wyldfire (2026-09-14, sera)

Su richiesta dell'utente di basare un eventuale ripristino "solo sulla versione locale di Wyldfire già sincronizzata", è stato individuato e analizzato il database reale dell'app desktop:

- **Percorso:** `C:\Users\mande\AppData\Roaming\com.wyvern.wyldfire\wyldfire.db` (SQLite, ~18,7 MB, + `-wal`/`-shm`). Confermato che l'app Wyldfire è un client Tauri con database locale reale (non un semplice wrapper del sito, la cartella `EBWebView` sotto `AppData\Local` è solo la cache del webview interno ed è irrilevante, troppo piccola per contenere dati di World).
- **World locale Svartulfr:** id locale `6cfuc64QBr1Flf9nKndFy`, `platform_id` = `_W62KjGjHTJhV3rfV2wPjc` (conferma che è lo stesso World).
- **Tabella `world_characters` locale: 86 personaggi totali**, e **tutti** condividono lo stesso `updated_at`/`synced_at`: **2026-09-07T05:39:49 UTC**. È uno snapshot unico, fatto in blocco quel giorno, mai più aggiornato da allora.
- **Nessun record di Atlas Teague** presente in locale (coerente: non è mai stato scritto via Wyldfire).
- **Il "sync" eseguito dall'utente poco prima di questa verifica ha toccato solo la riga di primo livello della tabella `worlds`** (metadati come `world_age`), **non** la tabella `world_characters`: i personaggi locali restano fermi al 7 settembre.

**Conclusione importante, da correggere rispetto alla premessa iniziale:** il database locale di Wyldfire **non è una copia aggiornata** del World. È più vecchio di **una settimana** rispetto al lavoro di questa sessione (decine di schede completate il 13 e 14 settembre, vedi l'elenco esteso di documenti "Completamento" nel Project di quei due giorni) e probabilmente anche più vecchio dello stato a cui lo staff ha riportato il World col ripristino (che sembra comunque non aver ancora risolto nulla, vedi sopra). **Non può essere usato come fonte per "ripristinare i dati persi" di questa settimana**: usarlo per un publish sovrascriverebbe il World con una versione che manca di tutto il lavoro recente. Può eventualmente servire solo come backup di **emergenza estrema** per i personaggi risalenti a prima del 7 settembre, non oltre.

## Opzioni valutate

1. **Attendere un intervento risolutivo reale dello staff Wyvern** dopo la segnalazione su Discord `bugs-and-support` (report pronto sotto). Il presunto ripristino di questa sera non ha ancora risolto nulla: va ancora verificato quando/se lo staff completerà l'intervento.
2. **Duplicare il World e ricostruire i Character a mano**: opzione last-resort, valida in teoria (un World duplicato non erediterebbe il record corrotto) ma con costo altissimo. Il tentativo di clone nativo è fallito (causa non diagnosticata).
3. **Creare un nuovo World vuoto e usare "Import Assets"** per portare dentro il contenuto del World esistente, evitando il record corrotto: proposto dall'utente, non ancora testato.
4. **Wyldfire locale come fonte di ripristino**: **scartata** per i dati di questa settimana, il database locale è troppo vecchio (7 settembre). Resta solo come possibile backup per contenuto pre-7 settembre.

## Versione finale del report (pronta per Discord `bugs-and-support`)

Verificare contro il template fissato "HOW TO REPORT ISSUES" prima di postare:

> **Incident Summary: Character Record Corruption (World `_W62KjGjHTJhV3rfV2wPjc`)**
>
> **Context:** A backend type mismatch error has rendered the "Characters" section of the Wyvern.chat world `Svartúlfr` (`_W62KjGjHTJhV3rfV2wPjc`) inaccessible. The issue originated when a `POST` request successfully created a character ("Atlas Teague", ID `_291aPrb6qJcgjXW2dJnpD`) with an ISO-8601 string for the `birthdate` field instead of the required `NumericBigIntType` (world-hours).
>
> **Diagnostics:** The corruption triggers a `500 Internal Server Error` across multiple API endpoints and the web UI.
>
> | Endpoint | Method | Result | Technical Error |
> | :--- | :--- | :--- | :--- |
> | `/api/worlds/characters/world/[world_id]` | GET | 500 | `Could not convert JS value '1995-06-14T00:00:00.000Z' of type 'string' to type NumericBigIntType` |
> | `/api/worlds/characters/[char_id]` | GET/PUT/DELETE | 500 | Same as above |
>
> - Latency: High TTFB (~910ms) suggests the crash occurs during server-side hydration/query processing after the record is fetched.
> - Propagation: The single corrupted record causes the global list fetch to fail, effectively locking the entire Characters module for all users of that world.
> - Persistence: `PUT` requests intended to fix the record fail because the server attempts to validate/hydrate the existing corrupted data before applying new updates. **Confirmed even with an empty PUT body (`{}`): identical 500, proving the crash happens during a read/hydration step before the payload is even considered.**
> - Also tried and ruled out: `PATCH` (404, unsupported verb), guessed bulk-delete/trash/admin/search endpoints (all 404), list-endpoint query params like `limit`/`search`/`fields`/`page` (all silently ignored, still 500s), and a full client reset (cleared cache/localStorage/IndexedDB, fresh login, fresh token) — identical failure, ruling out any client/session/cache cause.
> - **As of this evening, a claimed staff-side rollback to an earlier World version has NOT resolved the issue: a fresh authenticated check still returns the identical 500 on the same endpoint with the identical error message.**
>
> **Actionable Findings:**
> - Validation Bypass: the initial `POST` request failed to validate the `birthdate` type, allowing an invalid string to persist in a `BigInt` column.
> - Lack of Fault Tolerance: the collection list route lacks error handling to skip or isolate corrupted records.
> - **Correction Requirement: the record is currently immutable via client-side API in every form tested, including a completely fresh client/session. A manual database intervention is required to delete or update the `birthdate` value for ID `_291aPrb6qJcgjXW2dJnpD`.**
>
> **Recommended fixes (source-side):** strict type enforcement at the DTO/schema level (e.g. Zod) to keep ISO strings out of a BigInt `birthdate` field, and fault-tolerant list hydration (e.g. a try/catch around Prisma's `findMany` that logs and filters out a corrupted record instead of failing the whole list).
>
> **World:** Svartúlfr (`_W62KjGjHTJhV3rfV2wPjc`)
> **Character id:** `_291aPrb6qJcgjXW2dJnpD` ("Atlas Teague")
> **Impact:** Characters section of this World currently unusable for all users of the World, not just via API.

## Stato e prossimi passi

1. Il report è pronto per essere postato su Discord `bugs-and-support`, aggiornato con la nota sul ripristino inefficace.
2. **Scrittura su Character in questo World sospesa** fino a conferma reale (verificata via API/reload) che un admin Wyvern ha corretto/rimosso il record `_291aPrb6qJcgjXW2dJnpD`.
3. D'ora in avanti, ogni creazione di Character passerà `birthdate`/`start_timeline_position` come numero di ore-World fin dall'inizio, mai come stringa ISO.
4. Il JED+ completo di Atlas Teague resta pronto per essere riutilizzato non appena la piattaforma sblocca la situazione.
5. **Il database locale Wyldfire non è utilizzabile per recuperare il lavoro di questa settimana** (fermo al 7 settembre): va scartato come fonte di ripristino per i dati recenti. Resta da stabilire con l'utente se vale la pena tenerlo aggiornato d'ora in avanti come backup, una volta risolto l'incidente.
6. Opzione "nuovo World + Import Assets" proposta dall'utente, non ancora testata: da valutare se il fix reale dello staff continua a tardare.
