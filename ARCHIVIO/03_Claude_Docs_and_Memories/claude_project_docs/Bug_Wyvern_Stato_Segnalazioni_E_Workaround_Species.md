# Bug Wyvern: cosa è già segnalato, cosa no, e il workaround per Species/Occupation

Verificato il 2026-09-07 leggendo `#bugs-and-support` sul server Discord
WyvernChat, più un test diretto sull'API. **Il risultato più importante non è la
ricognizione: è che il bug Species/Occupation ha un workaround che funziona, e
la §15 delle istruzioni ("lasciarli a None") è stata corretta di conseguenza.**

---

## 0. Aggiornamento 2026-09-13: move delle voci Lexicon, confermato risolto

L'utente ha riportato che le voci Lexicon ora si spostano senza dover
ricaricare la pagina per vedere il cambiamento. Fatto un test completo per
verificarlo: individuate le **22 voci Lexicon "Uncategorized"** (168 voci
totali, 146 già in una delle 14 cartelle esistenti), classificate una per una
nella cartella tematica più coerente e scritte via PUT parziale su
`content_folders.lexicon` (World, non Character: stesso schema di
`content_folders.characters` usato per i Character).

**Assegnazioni fatte:**

- **Houses & Bloodlines** (+3): "Cosa Solarton sa delle Case, e cosa non sa",
  "La casa della Longhouse: doni e volontarie", "The Douglas Face".
- **LSE — Society & Hierarchy** (+2): "La Legge di Wulfnic: il diciannovesimo
  anno", "Humans First".
- **LSE — Faith & Mythology** (+1): "Vélhati e Vélsköll (SEGRETO, non
  rivelare)".
- **Species & Races** (+1): "Project BlackWolf: il sigillo e l'unico civile
  che sa" (è la lore sulla lineage modificata, coerente con la categoria).
- **Blackwood City** (+5): i cinque eventi datati di famiglia Douglas (passaggio
  Pack Mom di Alyssa, Disneyland con Logan, compleanno dei gemelli/festa di
  Wulfnic, road trip con Logan, pranzo della domenica).
- **SUCC Campus** (+9): l'accordo Wolfwood-Douglas, fondazione SUCC 1887, CUMS
  Campus & Teams, Admitted Student Days, Decision Day, Full Moon Festival,
  primo giorno alla SUCC, Halloween University Party, e la band Grave Mistake
  (nata da studenti SUCC, trattata come cultura di campus).

**Lasciata volutamente fuori:** "ZZ DEBUG PROBE (temporanea, da cancellare)".
È una entry di test dichiarata tale nel proprio nome e contenuto ("DEBUG
PROBE... ignore it completely"), non lore reale: da cancellare, non da
classificare. Segnalata qui per tracciabilità, azione di cancellazione lasciata
all'utente.

**Verifica dopo reload completo della pagina** (non solo dopo il salvataggio,
come da §11): rilette le 14 cartelle e i conteggi tornano esattamente come
previsto (Society & Hierarchy 15→17, Faith & Mythology 6→7, Houses &
Bloodlines 7→10, Blackwood City 7→12, SUCC Campus 8→17, Species & Races
9→10). Le "Uncategorized" sono passate da 22 a 1 (solo il DEBUG PROBE, lasciato
apposta). **Il move risulta quindi effettivamente risolto e verificato**, non
solo riportato: scritto via API e confermato persistente dopo reload
completo, il gradino più alto della scala di affidabilità di §11.

---

## 1. Il workaround per Species e Occupation

### Come stanno davvero le cose

`species_id` e `occupation_id` **non sono campi di primo livello** sul
Character. L'oggetto Character non li contiene affatto: vivono **dentro
`rpg_stats`**, accanto a `base_stats`, `level` ed `experience`.

Un PUT che li manda al primo livello risponde **200 e li butta via in
silenzio**. È lo stesso modo di fallire del PUT con oggetto completo (§11): lo
status non dice niente.

```js
// NO: 200, e alla rilettura i campi non ci sono
await RAW('PUT','/api/worlds/characters/'+id,{species_id:S, occupation_id:O});

// SI: si legge rpg_stats, si estende, si rimanda solo quello
const cur = (await RAW('GET','/api/worlds/characters/'+id)).json.rpg_stats;
await RAW('PUT','/api/worlds/characters/'+id,
  {rpg_stats: Object.assign({}, cur, {species_id:S, occupation_id:O})});
```

Gli id delle specie e delle occupazioni si leggono da due route che non
seguono lo schema delle altre risorse:

- `GET /api/worlds/rpg/species/<world_id>`
- `GET /api/worlds/rpg/occupations/<world_id>`

Nel nostro World ci sono **10 specie** (Demi-humans, Demons, Fae, Human,
Hybrids, Magic-capable Humans, Primordial, Undead, Vampire,
Weres/Shapeshifters) e **17 occupazioni** (Bartender, Bodyguard, CEO, DJ,
Divine Guardian, General Laborer, Line Cook, Living Saga, Master Blacksmith,
Matriarch, Mechanic, Patriarch, Security Commander, Server, Stage Technician,
Student, Teacher). I blueprint quindi si salvano benissimo: il problema era
solo l'assegnazione al personaggio.

**Nota 2026-09-13: questo workaround è comunque sospeso lato gioco per ora**,
non perché sia rotto ma perché l'utente ha disattivato `rpg_stats` a livello
World dopo test sulla Simulation (vedi
`Simulation_World_Features_Disattivate_2026-09-13.md`). Il meccanismo resta
valido e i dati già scritti restano sulle schede.

### Verificato fino in fondo

Testato su **Elizabeth Duskwood**. Dopo il PUT, reload completo della pagina,
rilettura dall'API e **apertura della scheda nell'interfaccia**: la sezione RPG
Stats mostra Species **Weres/Shapeshifters** e Occupation **Matriarch**, e il
modificatore di specie è applicato davvero, MGT porta il badge **Sp +2** e il
Control è passato a **146**. Non è un campo orfano scritto in un angolo del
database: la piattaforma lo usa.

### Lavoro che questo apre

**38 dei 39 personaggi con RPG Stats non hanno specie né occupazione.**
L'unica a averle è Elizabeth, dal test. Assegnarle è un lavoro di giudizio
personaggio per personaggio, non una sostituzione meccanica, e va fatto quando
si decide di farlo, non di slancio. **In pausa dal 2026-09-13** insieme al
resto del passo RPG Stats.

---

## 2. Default Outfit: chiuso il 2026-09-07

Il buco era grosso: **25 dei 40 personaggi con outfit non avevano il Default
Outfit**, che l'interfaccia segna come *Required*. Senza di esso il modello
improvvisa l'abbigliamento in ogni scena che non attiva un outfit contestuale,
e fra i mancanti c'erano schede che consideravamo finite.

**Assegnati tutti e 25 via API** (`default_outfit`, che vuole l'**id**
dell'outfit, non il nome), verificati dopo reload completo: 40 su 40 hanno un
default, zero id orfani, e il controllo nell'interfaccia su Elizabeth conferma
"House Formal" con l'avviso giallo sparito.

**Criterio usato:** il default è quello che il personaggio indossa quando la
scena non specifica niente, cioè **il posto in cui è più probabile incontrarlo**,
non il vestito migliore che ha. Per lo staff ha vinto l'abito da lavoro
(Ariadne il Health Centre, Archer l'ufficio, Loewe la Lecture Hall, Dullahan e
Barkley Practice/Sideline, Hank Coach), per gli studenti il campus o il dorm,
per chi si incontra in casa il vestito domestico (Stanley Sr. At Home, Jasmin
The House, Eris "Presentable", che è letteralmente la sua faccia pubblica).

**I quattro casi in cui la scelta non era ovvia**, e vale la pena saperlo:

- **Nixara** è deceduta e tre dei suoi cinque outfit sono eventi datati (la
  Grande Caccia del 1994, il matrimonio del 1996, "As Erik Remembers Her"). Ha
  preso **Villa Douglas**, cioè la vita quotidiana, perché il default deve essere
  lo stato normale e non un momento.
- **Cornelius**: **Colonial Working Dress**, non l'investitura né il ritratto.
- **Elizabeth e Magnus**: **House Formal** per entrambi. Villa Douglas è una casa
  formale e loro due sono quelli che la rappresentano, quindi il vestito da
  ricevere è il loro stato normale, non un'eccezione.
- **I tre commilitoni di Kaladin** (Rafael, Kade, Miles) hanno tutti e tre
  **On Base**: Field è la missione, Off Duty è il tempo libero, Shifted è la
  forma lupo. Il neutro è la base.

La pipeline §14 ha ora il Default Outfit come **passo 6**, subito dopo gli
outfit, e la verifica finale lo controlla.

---

## 3. I nostri bug già segnalati da altri

| Nostro bug | Segnalazione trovata | Stato |
|---|---|---|
| Species / Occupation non persistono | **"RPG Species, Occupation and Traits dont get saved on characters in my world"**, di Mucc [EU], 2 giugno 2026 | **NevDev ha risposto lo stesso giorno: "hello! i actually just patched this"**. Tre mesi dopo il bug è ancora lì, quindi o la patch ha coperto solo una parte, o c'è stata una regressione. Commentato il 7 settembre con il dettaglio di `rpg_stats`. Thread seguito |
| `linked-characters` 500 | **"Unable to link characters to specific world"**, di LagunArt [HOPE], 6 settembre 2026, tag *In Progress* | Sintomi identici ai nostri: dalle impostazioni del bot sembra collegato e salvato, dopo il reload è scollegato; dal World risponde "Failed to Link character". Commentato il 7 settembre con l'errore esatto. Thread seguito |
| Blueprint RPG che non si creano | **"RPG Blueprints"**, di MARTHA | Aperto. Dice "created successfully" ma il contatore resta a 0. Da noi i blueprint invece si creano, quindi non è il nostro caso, ma è la stessa area |
| Move delle voci Lexicon | Non tracciata con un link di thread specifico | **Risolto**, confermato con test diretto il 2026-09-13 (vedi §0) |

**L'errore preciso del linked-characters**, che nessuno aveva ancora messo nel
thread: `GET /api/worlds/linked-characters/<world_id>` risponde **500** con
`{"error":"Internal Server Error","message":"Maximum call stack size exceeded"}`.
È uno stack overflow, quindi ricorsione non limitata, probabilmente qualcosa di
circolare nel grafo dei linked characters e non un problema del singolo
personaggio.

---

## 4. I nostri bug che nessuno ha ancora segnalato

Cercati con `in:bugs-and-support` sui termini rilevanti, zero risultati
pertinenti. Vanno scritti con il template del post fissato *HOW TO REPORT
ISSUES* (Issue / What you tried to do / What happened instead / Error / Steps to
reproduce / Setup / Tried already).

1. **Livello RPG oltre ~100 fa fallire in silenzio l'intero blocco RPG.** Livello
   300 rifiutato, livello 99 salva e persiste, il tetto esatto sta fra 100 e
   299. Il pulsante resta appeso su "Saving...", nessun errore, e dopo il reload
   le RPG Stats risultano di nuovo disabilitate con stat e livello persi. Nello
   stesso identico save description, outfit, start position e toggle si salvano
   regolarmente. **È il più grave dei nostri, perché fallisce sembrando riuscito.**
2. **Gli outfit aggiunti in un solo salvataggio si sovrascrivono a vicenda.** Vanno
   inseriti uno per volta con un salvataggio ciascuno.
3. **Parent Location non offre opzioni finché la Location non è stata salvata
   almeno una volta.** Su una Location nuova la tendina è vuota.
4. **Le cartelle della lista contenuti si espandono solo cliccando la chevron**, non
   il nome. Cliccare l'etichetta non fa nulla nemmeno con un click reale.
5. **Il pulsante Save resta appeso su "Saving..." molto spesso**, pur avendo salvato.
   Nessuna segnalazione trovata con questa descrizione.

---

## 5. Bug del World segnalati da altri che ci riguardano da vicino

Non sono nostri, ma è utile sapere che esistono prima di dare la colpa a noi
stessi quando succedono:

- **World tagline keeps resetting to null**
- **World Details Deleted**
- **Worlds: can't remove all world characters from location/scenario**
- **Worlds Characters/Scenarios Invisible**
- **Worlds bug with lexicon import**
- **World char outfit trigger doesn't update image**
- **Worlds markdown not exporting fully**
- **AI Assistant: Approved changes fail and reflect `_DO_NOT_APPROVE` on 'Update
  timeline event'** (l'errore è `WorldTimelineEvent not ...`). Riguarda gli
  update sugli eventi di timeline; gli add funzionano.
- **AI Assistant can't see beyond the first 50 characters**, di Tydorius.
- **Failure of Lexicon Tool Synchronization**, di S_e_T: i tool
  `add/update/delete_lexicon_entry` dell'AI Assistant riportano SUCCESS e non
  scrivono niente. È l'analogo, lato assistente, del nostro PUT che risponde 200
  e non scrive.
- **Memory Scan Lexicon chat carryover issue**: un lexicon da memory scan
  sovrascritto da un nuovo roleplay con la stessa card. Ci riguarda, visto che i
  memory scan li usiamo.

---

## 6. Canali utili sul server WyvernChat

`bugs-and-support` (forum, con tag: Chat Mode, Story Mode, General UI Issue,
Profiles, Scenario Mode, Other, più gli stati Resolved e In Progress),
`support-and-questions`, `unresolved-threads`, `wyldfire-bugs-and-support`
(separato, per l'app desktop), `wiki-suggestions`, `feature-requests`,
`account-support`, `worlds-workshop`.

**I bug del sito e quelli di Wyldfire hanno canali diversi.** I nostri sono
tutti del sito.
