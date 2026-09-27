# Configurazione del sistema Relationships

Data: 2026-09-03. **Ladder riverificata il 2026-09-06 leggendo
`relationship_config.tier_ladder` direttamente dall'oggetto World via API: due
chiavi erano sbagliate in questo documento.** Vedi la sezione Ladder.

## Attivazione

Il toggle master **non** sta sulla scheda Relationships, come dice la wiki, ma
in **Simulation → World Features**, dove è una checkbox insieme alle altre
funzioni del World. **Relationships: attivo.** Attivo anche il blocco inline
`Relationships (>like/>love/>dislike/>hate/>mood)`, quindi l'AI sa di poter
emettere quei comandi.

Altre World Features attive: Inventory & Items, Currency & Economy, RPG Stats,
Combat System, Cross-World Ships, Party Stats in Prompt. Disattiva: Creature
Catcher.

## Falso allarme risolto: "Beloved" e `romantic_interest`

La chiave salvata sul server per il tier più alto è `romantic_interest`, il che
aveva fatto sospettare che Erik risultasse in interesse romantico verso i
propri figli. **Non è così.** La wiki è esplicita: *"The tier name is what the
sidebar shows, what the AI sees in the relationship block, and what appears in
the Tier dropdown"*. L'AI legge l'etichetta della ladder, cioè **Beloved**. La
chiave è solo il nome interno dello slot di piattaforma. **Nessuna correzione
necessaria sui legami familiari.**

**Confermato definitivamente il 2026-09-06** leggendo la config del World, dove
la riga è letteralmente `{"id":"romantic_interest","label":"Beloved","min_points":92}`.

Stessa cosa per il template: usa `{{subject}}` e `{{target}}`, che la wiki
indica come le variabili **preferite** proprio per le righe
personaggio→personaggio, mentre `{{name}}`/`{{user}}` sono retrocompatibilità.
Il template del World è quindi già quello moderno e corretto.

## Layer attivi

Tutti e cinque: Persistent level, Temporary moods, Moods fade over time,
**Seed from authored attitudes**, Show panel to player. Decay shape: Ease out.

Il quarto è quello che rende sensato tutto il lavoro sulle Attitudes: le
attitudes autorate diventano i punti relazione di partenza alla creazione della
partita. Non sovrascrivono uno stato già esistente da una sessione precedente.

## Magnitudini, impostate a slow burn su entrambe le vie (03/09/2026)

| | Permanent | Mood size | Mood hours |
|---|---|---|---|
| Regular (`>like` / `>dislike`) | 3 → **2** | 12 | 24 |
| Severe (`>love` / `>hate`) | 15 → **6** | 30 | 120 → **168** |

Motivo: con i valori precedenti bastavano **sette momenti forti per passare da
estraneo a Beloved e cinque per arrivare a Enemy**, cioè la via corta era di
fatto un interruttore mentre quella lunga era ben tarata.

Con i nuovi valori, partendo da neutro:

| Traguardo | Gesti piccoli | Momenti forti |
|---|---|---|
| Acknowledged (15) | 8 | 3 |
| Trusted (35) | 18 | 6 |
| Pack (55) | 28 | 10 |
| Pack-bonded (75) | 38 | 13 |
| Beloved (92) | 46 | 16 |

Le ore dei moodlet Severe sono salite a 168, una settimana in-world: un evento
forte sposta meno il permanente ma colora l'aria molto più a lungo. Verificato
persistito dopo reload.

## Ladder dei tier — CORRETTA il 2026-09-06

Letta da `relationship_config.tier_ladder` sull'oggetto World. **Questa tabella
sostituisce la precedente, che aveva due chiavi sbagliate e una vuota.**

| Etichetta | Soglia | Chiave interna |
|---|---|---|
| Blood Enemy | -100 | `nemesis` |
| Enemy | -70 | `enemy` |
| Rival | -45 | `despised` |
| Distrusted | -25 | `hated` |
| Wary | -10 | `disliked` |
| Unknown Scent | 0 | `stranger` |
| Acknowledged | 15 | `acquaintance` |
| Trusted | 35 | `friend` |
| Pack | 55 | `close_friend` |
| Pack-bonded | 75 | `best_friend` |
| Beloved | 92 | `romantic_interest` |

**Cosa c'era di sbagliato prima.** Il documento indicava `blood_enemy` per Blood
Enemy (la chiave vera è `nemesis`), `rival` per Rival (è `despised`), e lasciava
vuota la casella di Distrusted (è `hated`). Le chiavi `blood_enemy` e `rival`
**non esistono**: scriverle in un'attitude produce un tier non valido.

**Perché sbagliavo.** La ladder di default della piattaforma ha **quattordici**
gradini (nemesis, enemy, despised, hated, disliked, stranger, acquaintance,
friend, close_friend, best_friend, romantic_interest, lover, partner, soulmate).
La ladder del World ne ha **undici**, e la personalizzazione **rietichetta i
primi undici id di piattaforma senza rinominarli**. Quindi le tre chiavi in più
(lover, partner, soulmate) semplicemente non si usano, e le etichette negative
sono scalate di una posizione rispetto a quello che il nome della chiave
suggerirebbe.

**Conseguenza sui dati già salvati, tutta buona.** Nelle 153 attitudes del World
ci sono 2 `despised` e 1 `hated`, che leggendo la chiave sembravano "disprezzato"
e "odiato" e sono invece **Rival** e **Distrusted**. Nessuno nel World è odiato
da nessuno.

**Attenzione, invariata:** la corrispondenza etichetta→chiave è posizionale.
Aggiungere, togliere o riordinare un gradino della ladder rimappa il significato
di **tutte le attitudes già salvate**. Non toccare la ladder senza rifare le
attitudes.

Nota: Beloved è una banda stretta, 92-100. Ci si arriva con fatica e si scende
con poco.

## Mood custom (7)

| Nome | Size | Ore |
|---|---|---|
| Protective | 20 | 48 |
| Scent-marked | 15 | 72 |
| Cowed | 25 | 6 |
| Heat-clouded | 30 | 24 |
| Pack-anxious | 15 | 48 |
| Suspicious | 10 | 168 |
| Awed | 20 | 12 |

## Relationship Block

- Heading: vuoto, corretto, perché i wrapper tag sostituiscono l'intestazione
  markdown.
- Wrapper: `<PackBonds>` … `</PackBonds>`
- Riga per personaggio:
  `{{subject}} toward {{target}}: {{tier}}{{#if mood}}, currently {{mood}}{{/if}}{{#if reason}}. {{reason}}{{/if}}`
- Instructions: il testo sul sentire come fatto chimico e pubblico, che dice
  all'AI di non nominare mai tier, mood o numeri e di mostrarli con postura,
  prossimità e odore. Include già la nota che le righe fra due NPC contano
  quanto quelle che coinvolgono il giocatore.

## Come si scrive un'attitude via API

Le attitudes **non sono una risorsa separata**: sono un array sul Character,
campo `attitudes`. Si aggiornano con un PUT parziale sul personaggio
(`PUT /api/worlds/characters/<id>` con solo `{attitudes:[...]}`), rileggendo
prima l'array esistente e riscrivendolo intero, perché il campo si sostituisce
in blocco.

Forma di un elemento:

```js
{ id: 'attitude-<univoco>',
  target_type: 'world_character',
  target: '',              // sempre vuoto: e' un campo di display
  target_id: '<id del personaggio bersaglio>',
  tier: 'close_friend',    // la CHIAVE, non l'etichetta
  intensity: 55,
  reasoning: '...' }
```

**`target` vuoto non è un errore.** Tutte le 153 attitudes del World lo hanno
vuoto e `target_id` popolato. Il legame vive in `target_id`. Me ne ero allarmato
per sbaglio: sembrava che puntassero al nulla.

## Intensità: il difetto da sanare

L'attitude ha una quarta parte oltre a bersaglio, tier e motivazione:
**Intensity (1-100)**, che posiziona il punto di partenza *dentro* la banda del
tier. La wiki dice che se non impostata dovrebbe cadere a metà banda; **in
questa build il campo lasciato vuoto si salva come 1**, cioè il pavimento.

**Convenzione adottata:** 50 di default, **85** dove il rapporto *è* il
personaggio (Malachia verso Alyssa, Logan verso Edric, Marcus verso Kaladin),
**20** per una conoscenza appena accennata.

## Regola per le Attitudes sulle schede (decisa dall'utente)

1. **Alyssa e Jasper vanno su ogni scheda**, perché sono i due personaggi
   giocabili del roster "Choose Your Character". Anche chi non li conosce
   affatto va scritto, a **Unknown Scent**, con una motivazione che dice che
   non si sono mai incontrati: sapere che non si conoscono è informazione
   quanto il contrario.
2. Oltre a loro, **solo i personaggi citati nel background della scheda**, con
   il tier più adatto a quello che il testo dice davvero.
3. Bersaglio sempre **World Character**, mai Generic (text), quando il
   personaggio esiste come scheda.
4. **The Player (Persona) va evitato** per rapporti specifici di una persona:
   punta a chiunque stia giocando, quindi una motivazione scritta su Alyssa
   verrebbe applicata anche a Jasper. Vedi `Attitudes_Audit_2026-09-03.md`, che
   elenca le cinque schede da correggere.

## Copertura attuale

36 schede su 86 hanno attitudes, per 153 attitudes totali. **Cinquanta schede
non ne hanno nessuna**, quindi non rispettano il punto 1 della regola. Erik ne
ha 10, Logan 8, Malachia 7. Jasper ne ha 6 dal 2026-09-06.
