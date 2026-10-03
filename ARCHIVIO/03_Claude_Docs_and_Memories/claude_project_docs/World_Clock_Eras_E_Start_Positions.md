# World Clock: ora zero alla nascita di Wulfnic. Migrazione completata

Deciso dall'utente e applicato il 2026-09-06. **Sostituisce la §6 delle
istruzioni di progetto**, che diceva ora zero = 1 gennaio 800.

---

## L'impostazione definitiva

**Ora zero = martedì 21 dicembre 827, la nascita di Wulfnic Bloodmoon.**
**Today in game = venerdì 5 aprile 2024.**

| Campo | Valore |
|---|---|
| `human_start_date` | `0827-12-21` |
| `calendar.start_year` | `827` |
| `calendar.start_month_id` | `dec` |
| `calendar.start_day_of_month` | `21` |
| `calendar.day_names` | **`Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday`** |
| `world_age` | **10.486.470** = 5 aprile 2024, ore 06:00 |

Il calendario ha i campi **Start Month** e **Start Day of Month** oltre a Start
Year, quindi l'ora zero può cadere in un giorno qualsiasi dell'anno e non solo al
1 gennaio. Me li ero persi, e avevo proposto di ripiegare sul 1 gennaio 827: non
serviva.

---

## Perché i giorni della settimana sono ruotati

**Wyvern non calcola il giorno della settimana dalla data: conta i giorni
trascorsi dall'ora zero, fa modulo 7, e usa quel numero come indice nella lista
`day_names`.** Quindi `day_names[0]` deve essere il giorno che era l'ora zero.

Il 21 dicembre 827, nel gregoriano prolettico, era un **martedì**. Con la lista
standard che comincia da Monday, l'app trattava l'ora zero come lunedì e tutto il
World risultava **indietro di un giorno**: il compleanno di Alyssa veniva reso
"Thursday, April 22, 2005" invece che Friday.

**Ruotando la lista di una posizione**, così che cominci da Tuesday, tutto torna.

### L'ipotesi della convenzione americana non regge, ed è verificabile

Sembrava plausibile che Wyvern usasse la convenzione USA con la **domenica come
primo giorno** invece del lunedì, visto che lo scarto era esattamente di un
giorno. Ma il modello non sopravvive al controllo, per due motivi.

**Va nella direzione sbagliata.** Con un indice domenica-primo (Sun=0, Mon=1 …
Fri=5) letto su una lista lunedì-prima, un venerdì verrebbe reso *sabato*: un
giorno **avanti**. Noi osservavamo un giorno **indietro**.

**È falsificata dallo stato attuale.** Con la lista ruotata che comincia da
Tuesday, un indice domenica-primo per venerdì darebbe `day_names[5]` = **Sunday**.
L'app invece rende **Friday**, che è quello che dà il modello "giorni dall'ora
zero, modulo 7".

**Perché sembrava una questione di convenzione.** Prima della migrazione l'ora
zero era il 1 gennaio 2024, che **era davvero un lunedì**. La lista standard
lunedì-prima quindi funzionava per puro caso, e il meccanismo restava invisibile.
Il bug si è manifestato solo spostando l'ora zero su un giorno diverso.

### La verifica

Sei date su quattro giorni della settimana diversi, controllate con il modello e
poi due di esse riaperte nell'interfaccia dopo il reload:

| Data | Indice | Reso dall'app | Vero |
|---|---|---|---|
| Noah, 5 ottobre 1999 | 0 | Tuesday | Tuesday |
| Cornelius, 14 agosto 1631 | 2 | Thursday | Thursday |
| **Alyssa, 22 aprile 2005** | 3 | **Friday** ✓ letto nell'editor | Friday |
| Erik, 31 ottobre 1969 | 3 | Friday | Friday |
| **Malachia, 10 agosto 1996** | 4 | **Saturday** ✓ letto nell'editor | Saturday |
| oggi, 5 aprile 2024 | 3 | Friday | Friday |

Malachia serviva proprio a questo: essendo un sabato e non un venerdì, esclude
che il caso di Alyssa fosse una coincidenza fortunata.

### Due avvertenze

**Non "sistemare" quella lista.** Sembra sbagliata e non lo è: è l'unico modo di
dire a Wyvern che giorno della settimana era l'ora zero.

**Il pulsante "Reset to Earth" nella scheda Calendar la rimetterebbe a
lunedì-prima**, ri-rompendo tutti i giorni della settimana del World. Se un
giorno l'ora zero cambia, la rotazione va rifatta a mano.

---

## Cosa c'era prima: due ancore in conflitto

Il World era spaccato in due gruppi, ciascuno coerente con un'ancora diversa,
senza che niente lo segnalasse.

| Gruppo | Ancora | Cosa c'era dentro |
|---|---|---|
| **A** | 1 gen 2024 (`calendar.start_year`) | Le 44 date di nascita, e sette Start Position di Location ed Environment |
| **B** | 1 gen 800 (`human_start_date`) | `world_age`, le 7 Eras, le posizioni di 8 personaggi, gli Scenari, le entry Lexicon |

La scheda **Simulation** leggeva l'800; tutti i **selettori di data** leggevano
il calendario, cioè il 2024. È **un bug di piattaforma da segnalare a Wyvern**:
due schermate rispondono in modo diverso alla stessa domanda e nulla avverte che
sono in disaccordo.

## La migrazione

Due costanti, ricavate dalle date note e verificate una per una.

| Gruppo | Operazione | Costante |
|---|---|---|
| B | sottrarre | **245.184** |
| A | sommare | **10.484.184** |

**La verifica che le convalida entrambe insieme:** i gemelli nascono il giorno in
cui muore Nixara. La **data di nascita di Alyssa** stava nel Gruppo A, la **morte
di Nixara** nel Gruppo B. Partendo da due numeri diversi e due costanti diverse,
dopo la migrazione atterrano **entrambe su 10.320.312**, cioè 22 aprile 2005.

Altre verifiche passate: Erik 31 ottobre 1969, Cornelius 14 agosto 1631 in
entrambi i gruppi, Nixara 9 giugno 1975, Dullahan 1724, Villa Douglas 1666,
SUCC 1887.

### Cosa è stato migrato

| Cosa | Quante |
|---|---|
| World Eras | 7 |
| Date di nascita | 44 |
| Start/End Position di Character | 8 |
| Start Position di Location | 4 |
| Start Position di Environment | 3 |
| Start/End Position di Lexicon | 10 |
| `event_config` delle entry Event | 8 |
| `insertion_point` degli Scenari | 2 |

### Stato finale, verificato dopo reload completo

**Le sette ere:**

| Era | Da | A |
|---|---|---|
| Age of Myth | 800-01-01 | 827-01-01 |
| Age of the Firstborn | 827-01-01 | 999-12-24 |
| Age of Expansion | 999-12-24 | 1300-01-04 |
| Age of Houses | 1300-01-04 | 1450-01-09 |
| Age of Kingdoms | 1450-01-09 | 1665-12-22 |
| Age of Secrecy | 1665-12-22 | 1907-12-31 |
| Modern Era | 1907-12-31 | ongoing |

L'Age of Myth e la prima parte dell'Age of the Firstborn stanno ora in negativo,
il che è corretto: precedono la nascita di Wulfnic, che è l'ora zero.

**Gli otto eventi 2024** cadono tutti sulla data giusta, dal 13 aprile al 31
ottobre. **I due scenari**: "What Do You Want To Do" al 5 aprile 2024, "First
College Day" al 26 agosto 2024. **Le due entry storiche**: Founding of SUCC
1992, Nocturnal Crisis 1999.

---

## Nota di metodo: tre errori in due ore, tutti dello stesso tipo

Vale la pena scriverlo perché è un pattern e non tre incidenti.

1. Ho "corretto" la data di fondazione di SUCC dal 1992 al 2002 applicando la
   regola di precedenza, senza sospettare che fosse un adattamento voluto.
2. Ho letto la scheda Simulation, ho trovato "Timeline Start: January 1, 800",
   e ho concluso che sette Start Position negative fossero rotte. Erano corrette:
   erano ancorate al calendario, non a quel campo.
3. Ho proposto di ripiegare l'ora zero sul 1 gennaio 827 perché credevo che il
   calendario sapesse esprimere solo l'anno. Ci sono anche mese e giorno.

Tutti e tre hanno la stessa forma: **ho trovato una risposta netta e ho smesso di
cercare.** La schermata giusta, la regola giusta, il campo giusto, ognuno vero
per il suo pezzo e falso per il resto.

Il correttivo non è "guardare l'interfaccia", che facevo già. È **guardare
l'interfaccia nel punto esatto in cui vive il dato che sto per cambiare, e
guardarci prima di cambiarlo, non dopo.** Le Start Position si verificano
nell'editor di una Location. Le date di nascita nell'editor di un personaggio.
Non nella scheda Simulation, che parla d'altro.

La questione della domenica-primo è il controesempio utile: un'ipotesi
plausibile, che spiegava lo scarto osservato, e che è bastato provare a
falsificare per scartarla in due passaggi. Meglio testare che discutere.
