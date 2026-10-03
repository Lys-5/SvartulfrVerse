# Wyldfire: copia locale del World e stato del database


## Riferimenti fissi

| Cosa | Dove |
|---|---|
| **Editor del World sul sito** | `https://app.wyvern.chat/worlds/edit/_W62KjGjHTJhV3rfV2wPjc` |
| **Status della piattaforma** | `https://status.wyvern.chat/` |
| **Database locale dell'app** | `%APPDATA%\com.wyvern.wyldfire\wyldfire.db` |
| **platform_id del World** | `_W62KjGjHTJhV3rfV2wPjc` (stabile) |
| **id locale del World** | mai scritto a mano, si ricava dal platform_id |

**Modello operativo:** il **sito e' il padrone**, il **database locale e' una
replica di sola lettura** usata per audit e ricerche, e **non si carica mai**
dall'app verso il sito. Cosi' il locale puo' solo essere piu' vecchio, mai in
conflitto.

**La pagina di status va guardata prima di dare la colpa alla piattaforma.**
Controllata il 2026-09-07 alle 00:39: *All systems Operational*, Authentication
100%, Core Website 100%, Database 99,994% su trenta giorni, ultimo disservizio
una settimana fa. Quindi le disconnessioni di stanotte non erano di Wyvern, ma
del canale browser dal nostro lato.

Verificato: 2026-09-06, leggendo direttamente il database dell'app desktop.

---

## Dove stanno i dati

`%APPDATA%\com.wyvern.wyldfire\wyldfire.db`, cioe'
`C:\Users\mande\AppData\Roaming\com.wyvern.wyldfire\wyldfire.db`

E' un **database SQLite** da circa 10,7 MB (piu' `-wal` e `-shm`), con 76
tabelle. Accanto c'e' `files\` con `avatars`, `backgrounds`, `gallery`,
`personas`, `theme_assets`.

E' questo il file che il server MCP leggerebbe. **Si puo' interrogare in sola
lettura con Python** (`sqlite3` e' nella standard library, e sul PC c'e' Python
3.14.5), senza passare dall'interfaccia e senza toccare niente. E' una via di
lettura piu' veloce e piu' affidabile dell'automazione browser, e va usata per
gli audit anche prima che l'MCP funzioni. **Per la scrittura resta l'API con il
token**: scrivere nel db a mano metterebbe il locale fuori sincrono col cloud.

## Identita' del World

| Campo | Valore |
|---|---|
| id locale | **cambia a ogni riscaricamento**, vedi avvertenza sotto |
| `platform_id` | `_W62KjGjHTJhV3rfV2wPjc` (coincide con l'id nell'URL web, stabile) |
| `world_age` | 10.950.000 |

**Avvertenza, costata gia' un falso allarme.** L'id locale e quello di
piattaforma sono **diversi**, e soprattutto **l'id locale cambia quando l'app
riscarica il World**. Il 2026-09-06 pomeriggio era `GjMEyk4nnyqZlfHpdBf-f`, dopo
il riscaricamento delle 00:01 e' diventato `6cfuc64QBr1Flf9nKndFy`. Uno script
che lo tiene scritto dentro **restituisce zero righe**, il che sembra identico a
una perdita di dati.

**Regola: l'id locale non si scrive mai a mano.** Si ricava sempre cosi':

```sql
SELECT id FROM worlds WHERE platform_id = '_W62KjGjHTJhV3rfV2wPjc'
```

**Seconda regola, da un altro errore reale:** nelle ricerche testuali sulle
schede vanno cercate **anche le sigle**, non solo i nomi per esteso. Cercando
"Kappa Sigma Alpha" risultavano zero residenti nella fraternity dei Douglas,
perche' le schede scrivono sempre e solo **KSA**.

## Stato della copia locale: completa e aggiornata

Sincronizzata il 2026-09-06. I contenuti coincidono con quello che c'e' sul
cloud, controllato sui valori esatti scritti nelle ultime sessioni: Vincent
Campbell `long_summary` 9276, Andrew Campbell 9822, Erik Douglas 14730, Alyssa
15480. Combaciano al carattere.

| Contenuto | Quantita' |
|---|---|
| Personaggi | 86 |
| Location | 86 |
| Environment | 13 |
| Voci di Lexicon | 138 |
| Ere | 7 |
| Scenari | **1** |
| Mappe | **2** |

Sui personaggi: 61 su 86 hanno un `long_summary` reale, 36 hanno attitudes, 39
hanno outfit, 38 hanno RPG stats. I 36 con attitudes confermano esattamente
l'audit del 2026-09-03.

## Buchi trovati

**Le mappe caricate sono due, non tre.** Nel World ci sono `Blackwood` e
`California Coast`. **Manca la mappa del SUCC Main Campus**, che esiste come
immagine ma non e' mai stata caricata.

**C'e' un solo scenario, `First College Day`.** Da verificare se e' voluto o se
altri scenari non sono mai stati creati.

**Venticinque schede senza `long_summary` utile** (sotto i 200 caratteri). La
stima precedente di "una cinquantina di schede grezze" era pessimistica: sono
la meta'. Elenco completo:

Alicia Virtuoso, Alistair DeVille, Allegra Lumsden, Cato, Damien Bishop,
Daniel "Danny" Boone, Dominic Rogers, ENVY - Siobhan, Elizabeth Duskwood,
Everett Rottmore, Fade Greymoor, GLUTTONY - Kevin, GREED - Roxie, Harper Aries,
LUST - Dante, Luisa Sanchez Rogers, Mackenzie Sanchez Rogers,
PRIDE - Jean-Luc Virtuoso, Roland Vickers, Ruaraidh "Rory" Ballantine,
SLOTH - Arthur, Sullivan "Sully" Jones, Vasile Ionescu, Viola Carter,
WRATH - Zero.

I sette **peccati capitali** (ENVY, GLUTTONY, GREED, LUST, PRIDE, SLOTH, WRATH)
sono un gruppo omogeneo importato: conviene lavorarli in blocco con una
convenzione comune, non uno alla volta.

**Elizabeth Duskwood ha `long_summary` a zero ma le attitudes gia' scritte**
(1988 caratteri). E' il caso piu' anomalo del World: ha i rapporti e non ha la
scheda.

## Stato dell'MCP

Il lato dati e' pronto. Quello che manca e' solo il binario
`wyldfire-mcp.exe`, che la 0.3.126 **non spedisce**: la tabella dei file
dell'MSI contiene undici file in tutto, `wyldfire.exe` e i dieci tokenizer.
Il percorso in `claude_desktop_config.json` e' gia' stato corretto in
`D:\Wyldfire\wyldfire-mcp.exe`, che e' quello dichiarato dall'app.


---

## Verifica di allineamento con il cloud, 2026-09-07

Confronto diretto fra il database locale e la pagina del World su
`app.wyvern.chat`, letta dal browser.

| Contenuto | Locale | Sito | Esito |
|---|---|---|---|
| Characters | 86 | 86 | coincide |
| Locations | 86 | 86 | coincide |
| Environments | 13 | 13 | coincide |
| Lexicon | 138 | 138 | coincide |
| Scenarios | 1 | 1 | coincide |
| Maps | 2 | 2 | coincide |
| Eras | 7 | non mostrato | non verificabile da quella vista |

Il sito dichiara **All Content 324**, che e' esattamente 86+138+13+86+1.

**Integrita' del locale:** zero personaggi senza `platform_id`, zero mai
sincronizzati, zero modificati dopo l'ultimo sync, zero `sync_conflicts`. Nessuna
modifica locale pendente che possa scontrarsi col cloud.

**Non sono anomalie di download:** Species e Occupations a zero (bug noto della
piattaforma) e 25 schede su 86 con `long_summary` vuoto (le schede grezze gia'
censite).

**Conclusione: il World e' scaricato correttamente e allineato.**


---

## Accesso all'API dal browser: metodo aggiornato, 2026-09-07

### Il token si legge da IndexedDB, non si intercetta piu'

Il vecchio metodo, agganciare `window.fetch` e aspettare che l'app faccia una
richiesta, e' fragile: se la pagina ha gia' caricato non parte piu' niente e si
resta senza token. Il token di Firebase e' pero' gia' sul disco del browser.

```js
const req = indexedDB.open('firebaseLocalStorageDb');
// object store: 'firebaseLocalStorage'
// per ogni riga: row.value.stsTokenManager.accessToken
// header finale: 'Bearer ' + accessToken
```

Funziona subito, senza attese e senza clic.

### Le rotte vere, lette dal traffico dell'app

Lo schema e' `/api/worlds/<risorsa>/world/<world_id>`:

| Cosa | Rotta | Esito |
|---|---|---|
| Personaggi del World | `/api/worlds/characters/world/<W>` | 200 |
| Location | `/api/worlds/locations/world/<W>` | 200 |
| Mappe | `/api/worlds/maps/world/<W>` | 200 |
| Gallery | `/api/worlds/<W>/gallery` | 200 |
| Species / Occupations / Traits | `/api/worlds/rpg/species/<W>` e simili | 200 |
| Singolo personaggio, lettura e scrittura | `/api/worlds/characters/<character_id>` | GET / PUT |
| Linked characters | `/api/worlds/linked-characters/<W>` | **500 fisso**, bug confermato dal vivo |

### Due trappole confermate

**`/api/worlds/characters?world_id=<W>` ignora il parametro.** Risponde 200 ma
restituisce **1577 personaggi di novanta World pubblici**, e il nostro non c'e'
nemmeno. Usarla per contare qualcosa porta a conclusioni completamente sbagliate.

**Senza header `Authorization` la rotta giusta risponde 200 con `[]`.** E'
esattamente la trappola della regola §11: una risposta vuota **non e' la prova
che i dati non ci siano**. Con il token la stessa rotta restituisce gli 86
personaggi.
