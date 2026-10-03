# Scrivere sul World via API dal browser: metodo confermato

Fissato il 2026-09-06, dopo la prima sessione di scrittura riuscita (13 Location
create, 20 modificate, 3 Environment e 1 Character aggiornati, tutto verificato
dopo reload completo). Ampliato il 2026-09-07 con l'attivazione delle entry
Lexicon e le Party Conditions.

Sostituisce i tentativi precedenti. La regola §11 resta valida: **il fetch a mano
senza header di autenticazione restituisce `[]` o 401/403 e non prova niente.**
Questo documento dice come ottenere l'header giusto.

---

## 1. Il token va rinfrescato, non letto

Il token in IndexedDB **scade dopo un'ora** e resta lì scaduto. Leggerlo e usarlo
è la causa dei falsi errori: l'API risponde **404 a una GET** e **401 a una PUT**
quando il token è vecchio, quindi sembra che la route sia sbagliata mentre è solo
scaduta. Ore perse su questo.

Si legge il **refresh token** e si chiede a Firebase uno nuovo:

```js
window.W='_W62KjGjHTJhV3rfV2wPjc';
window.F=window.fetch.bind(window);

window.readIdb=()=>new Promise((res,rej)=>{
  const q=indexedDB.open('firebaseLocalStorageDb');
  q.onerror=()=>rej('idb');
  q.onsuccess=()=>{const db=q.result;
    const tx=db.transaction('firebaseLocalStorage','readonly');
    const g=tx.objectStore('firebaseLocalStorage').getAll();
    g.onsuccess=()=>res({rows:g.result});};});

const d=await window.readIdb();
const r=await window.F('https://securetoken.googleapis.com/v1/token?key=AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw',
 {method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},
  body:'grant_type=refresh_token&refresh_token='+
       encodeURIComponent(d.rows[0].value.stsTokenManager.refreshToken)});
window.TOK='Bearer '+(await r.json()).access_token;
```

La chiave `AIzaSy...` è l'API key pubblica di Firebase e si legge nel nome della
riga di IndexedDB (`firebase:authUser:<apikey>:[DEFAULT]`). Non è un segreto.

**Il token dura un'ora.** In una sessione lunga va rifatto. Se una chiamata
risponde 401 o 404 senza motivo, la prima cosa da fare è rinfrescare, non
cambiare route.

## 2. L'helper

```js
window.RAW=async(m,p,b)=>{
  const o={method:m,headers:{Authorization:window.TOK}};
  if(b){o.headers['Content-Type']='application/json';o.body=JSON.stringify(b);}
  const r=await window.F(p,o); const t=await r.text();
  let j=null; try{j=JSON.parse(t);}catch(e){}
  return {status:r.status,json:j,text:t.slice(0,400)};};
```

## 3. Le route, lette dal bundle dell'app

Non vanno indovinate: stanno nel bundle JS, in chiaro. Si trovano così:

```js
const srcs=[...document.querySelectorAll('script[src]')].map(s=>s.src);
for(const s of srcs){const t=await (await fetch(s)).text();
  let i=-1; while((i=t.indexOf('worlds/locations',i+1))!==-1)
    console.log(t.slice(i-260,i+160));}
```

Schema uniforme per ogni risorsa (`locations`, `environments`, `characters`,
`lexicon`, `scenarios`):

| Operazione | Metodo e path |
|---|---|
| Lista del World | `GET /api/worlds/<risorsa>/world/<world_id>` |
| Singolo | `GET /api/worlds/<risorsa>/<id>` |
| Crea | `POST /api/worlds/<risorsa>` con `world_id` nel body |
| Modifica | `PUT /api/worlds/<risorsa>/<id>` |
| Elimina | `DELETE /api/worlds/<risorsa>/<id>` → 204 |

Extra utili trovati nello stesso punto:
`GET /api/worlds/locations/environment/<env_id>`,
`GET /api/worlds/locations/<id>/marketplace`.

**Lo stesso metodo serve a trovare i nomi dei campi**, non solo le route. Cercare
nel bundle una stringa plausibile e leggere il default object attorno funziona
meglio che indovinare: è così che sono usciti `party_conditions` e
`party_condition_logic`, che non compaiono su una entry finché non sono stati
impostati almeno una volta.

## 4. La trappola grossa: il PUT vuole un body PARZIALE

**Un PUT con l'oggetto completo risponde 200 e non scrive niente.** Nessun
errore, `updated_at` invariato. È il modo peggiore possibile di fallire, perché
sembra riuscito.

```js
// NO: risponde 200, non cambia nulla
await RAW('PUT','/api/worlds/locations/'+id, oggettoInteroRipulito);

// SI: solo i campi che cambiano
await RAW('PUT','/api/worlds/locations/'+id, {environment_id:'_TF4E...'});
```

L'app stessa fa così: nel bundle, `update_location` destruttura `{id, ...resto}`
e manda solo il resto. Il server ignora silenziosamente un body che contiene
campi read-only annidati (`world`, `environment` come oggetto, `created_at`).

**Per appendere testo** si legge il campo, si concatena in JS e si rimanda solo
quel campo. Non si ridigita mai il testo esistente a mano.

## 5. Campi di una Location

`name`, `description`, `context_description`, `brief_context_description`,
`parent_location_id`, `environment_id`, `keys`, `secondary_keys`, `key_logic`,
`case_sensitive`, `whole_words_only`, `key_position`, `insertion_order`, `tags`,
`included_lexicon_entries`, `excluded_lexicon_entries`, `final_instructions`,
`linked_character_pool`, `included_character_pool`,
`min_number_of_characters`, `max_number_of_characters`,
`start_timeline_position`, `end_timeline_position`,
`time_of_day_override`, `calendar_override`, `jobs`.

In lettura `environment` e `parent_location` tornano come **oggetti annidati**;
in scrittura si mandano come **`environment_id` e `parent_location_id`**.

Su un Character il campo lungo della description è `long_summary`, e il nome è
`display_name` (non `name`: cercare `name` sulle schede non trova niente).

---

## 6. Come si attiva davvero una entry Lexicon *(nuovo, 2026-09-07)*

Questa parte è costata un errore vero e va letta prima di toccare `is_global`.

### Global OFF non restringe: spegne

Dalla wiki, e confermato da un test in chat: con **Global OFF una entry esce
dalla scansione a parole chiave del mondo e non si attiva mai da sola**,
qualunque parola compaia. Diventa idonea **solo** se la si aggiunge alla
`included_lexicon_entries` di una Location, di un Environment o di uno Scenario,
e anche allora serve comunque una chiave che matcha, oppure `constant: true`.

**Il campo `attached_world_character_id` non è un canale di attivazione.**
Agganciare una entry alla scheda del suo proprietario non la fa comparire quando
quel personaggio è in scena. Averlo creduto ha spento venti entry per mezza
giornata.

### Le tre leve vere

| Leva | Cosa fa |
|---|---|
| `is_global: true` | mette la entry nella scansione globale. Praticamente obbligatorio, se non è legata a un luogo |
| `keys` + `secondary_keys` + `key_logic` | filtro per parole chiave sugli ultimi N messaggi |
| `party_conditions` | filtro su **chi è nel party** |
| `constant: true` | forza l'inserimento sempre, ignora tutto il resto. Costa token a ogni messaggio |

### Party Conditions, la forma esatta

```js
party_conditions: [ { mode: "has_any" | "has_all" | "has_none",
                      character_ids: ["_id1","_id2"] } ],
party_condition_logic: "AND" | "OR"   // fra più condizioni
```

Nell'interfaccia sono etichettate "Has ANY of", "Has ALL of", "Has NONE of", e la
logica fra condizioni è "AND (all must pass)" oppure "OR (any must pass)".
Un array vuoto significa nessun vincolo.

**È lo strumento giusto per i contenuti personali**: un Intimacy Profile con
`has_any [proprietario]` esiste solo nelle scene in cui quella persona c'è
davvero.

### Attenzione alle chiavi generiche

Con `key_logic: "AND_ANY"` e `secondary_keys` vuote, basta **una qualunque**
delle primarie. Nel nostro World questo aveva prodotto dieci entry con la chiave
`intimacy` e tre con `werewolf`, cioè entry che sparano su parole che compaiono
in continuazione. La forma corretta è **primarie = identificatori della persona,
secondarie = parole dell'argomento**.

### Il macro `{{lexiconEntryNames}}` misura l'eleggibilità, non l'attivazione

Utile per diagnosticare, ma va letto per quello che è: elenca le entry
**candidate** per la scena (le global, quelle nello scope del luogo attivo), non
quelle che hanno effettivamente matchato una chiave. Un test che confronta due
scene può quindi dire se una entry è *spenta*, e non può dire se il filtro a
chiavi funziona.

Per una probe: creare una entry temporanea `constant: true` che dice al modello
di rispondere solo con la riga del macro, e mandarla con il comando `/sys`, che
il modello esegue mentre un messaggio normale lo interpreta come battuta di
scena.

## 7. Perché questo metodo conviene

Rispetto al pilotare l'interfaccia a click: nessun bug del pulsante "Saving..."
appeso (§15), nessun combobox che torna indietro, nessuna cartella da espandere
dalla chevron, e i 40-70 secondi per operazione di pagina diventano frazioni di
secondo.

**Resta valido §14.10:** anche via API si verifica dopo un reload completo,
rileggendo dalle liste del World. È la verifica a dirlo, non lo status 200.

## 8. Cose da non fare

- Non usare `/api/worlds/characters?world_id=`: **ignora il parametro** e
  restituisce ~1577 personaggi da tutti i World pubblici.
- Non fidarsi di uno status 200 su un PUT senza rileggere.
- Non riscrivere un testo lungo digitandolo: leggerlo, modificarlo in JS,
  rimandare solo quel campo.
- **Non spegnere `is_global` credendo di restringere.** Si restringe con
  `party_conditions` e con le chiavi, non togliendo la entry dalla scansione.
- Non usare `**` per il grassetto dentro il testo di una entry: nel World gli
  asterischi sono riservati ai pensieri interni.
