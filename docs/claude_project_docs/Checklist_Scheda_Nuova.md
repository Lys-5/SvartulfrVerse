# Checklist operativa per una scheda nuova

Aggiornata al 2026-09-06. Le regole stanno nelle istruzioni di progetto; questo
è l'ordine pratico con i valori esatti e le trappole verificate.

---

## 0. Lingua

**Tutto il contenuto del World è in inglese**: description, summary, display
description, outfit, Dialogue Examples, final instructions e motivazioni delle
Attitudes. L'italiano è la lingua della conversazione e di questi documenti, non
del contenuto.

Unica eccezione decisa: gli **Scenari avranno due greeting, uno in italiano e
uno in inglese**.

---

## 1. Prima di scrivere una riga

1. **Tutte le fonti sul tavolo.** Varianti multiple, file di lore, entry Lexicon
   esistenti, agganci già scritti in altre schede. Una scheda iniziata con
   materiale parziale va riscritta da zero quando arriva il resto, non ritoccata.
2. **Controllare se esiste già**, espandendo la cartella. Quasi tutti esistono
   come import grezzi: si riempiono, non si ricreano.
3. **Controllare cosa c'è già dentro da non perdere.** Da settembre 2026 molte
   schede grezze hanno già Attitudes o sezioni aggiunte a mano. Rileggere la
   scheda dal server prima di sovrascrivere.
4. **Epurare `{{user}}`**: generalizzare il ruolo senza mai nominare un
   personaggio del World, rimuovere del tutto cotte e relazioni rivolte al
   giocatore, non trascrivere i blocchi di kink nella description.
5. **Non "correggere" una discrepanza con una fonte esterna senza chiedere.** In
   questo progetto una divergenza dal materiale ufficiale è spesso un
   adattamento voluto. Vedi `Golden_Rule_Canon_Blackwood.md`.

---

## 2. Campi di testo

| Campo | Cosa ci va |
|---|---|
| `long_summary` | JED+: blocco `[ATTRIBUTO: valore; ...]` seguito da sezioni in prosa con titolo in maiuscolo |
| `summary` | Blocco PList di soli tratti, niente prosa |
| `display_description` | Una o due righe: chi è e cosa lo rende interessante |
| `final_instructions` | Come va giocato, più la riga di disciplina di formattazione in coda |

**Sezioni JED+ tipiche:** BACKSTORY, FAMILY, VOICE & BEHAVIOR, più due o tre
sezioni tematiche col nome che serve a quel personaggio, e una sezione finale
che dica la cosa vera su di lui.

**Disciplina di formattazione**, ovunque compaia testo in-character:
mai em-dash, dialogo tra virgolette, azioni e narrazione in testo semplice,
asterischi riservati ai soli pensieri interni, lingue straniere come
`"frase originale"` seguita da `([traduzione])`.

**Niente tratti sempre visibili.** Accessori e dettagli non strutturali vanno
negli outfit o scritti come contestuali, altrimenti il modello li infila anche
in piscina.

---

## 2-bis. Macro: quello che non va scritto a mano

Riferimento completo: `wiki.wyvern.chat/Features/Worlds/handlebars`.

**Regola generale: se un dato cambia con l'avanzare dell'orologio, non si scrive
come numero, si scrive come macro.** Altrimenti va rifatto a mano a ogni salto
temporale, e prima o poi qualcuno se ne dimentica.

| Invece di | Scrivere |
|---|---|
| `AGE: 19` | **`AGE: {{age}}`** |
| "quattro anni fa" su un evento datato | `{{worldAgo <ora>}}` |
| Uno stato che cambia a una certa data | `{{#beforeTimestamp <ora>}}…{{/beforeTimestamp}}` e `{{#afterTimestamp <ora>}}…{{/afterTimestamp}}` |
| Uno stato valido solo in una finestra | `{{#betweenTimestamps <da> <a>}}…{{/betweenTimestamps}}` |
| "manca poco al compleanno" | `{{time_till_birthday}}` |
| La data di oggi in-world | `{{worldDate}}` |

**`{{age}}` richiede il campo Birthdate compilato**, altrimenti non rende
niente. Vanno insieme.

**Non convertire il "anni fa" retorico.** "Ha abbandonato quello standard anni
fa" non ha una data dietro: farne un `{{worldAgo}}` significherebbe inventare
un evento. Il macro si usa solo dove la data esiste davvero.

Altri disponibili quando servono: `{{timeOfDay}}`, `{{#isTimeOfDay "Night"}}`,
`{{#betweenHours 22 4}}`, i macro di party (`{{#partyHasCharacter}}`,
`{{partyMemberNames}}`), quelli di elenco (`{{worldCharacterNames scope="location"}}`,
`{{locationNames tag="…"}}`) e quelli degli slot di scenario (`{{worldChar}}`,
`{{worldCharPronoun}}`).

---

## 3. Outfit: cinque

Contestuali, non decorativi. **Uno alla volta, con un salvataggio ciascuno.**
Almeno uno deve dire qualcosa che la prosa non dice.

---

## 4. Dialogue Examples: cinque

Con la disciplina di formattazione. Almeno uno mostra il personaggio nel suo
momento peggiore o più esposto.

Nota: `number_of_examples_to_use` è **3** di default, quindi con cinque esempi
ne girano tre alla volta.

---

## 5. Start Position e Birthdate  *(RISCRITTA 2026-09-06)*

**Ora zero del World = martedì 21 dicembre 827, la nascita di Wulfnic.**
**Today in game = venerdì 5 aprile 2024** (`world_age` 10.486.470).

Dettagli completi e storia della migrazione in
`World_Clock_Eras_E_Start_Positions.md`.

Start Position e Birthdate sono **ore assolute dall'ora zero**, entrambe positive
per chiunque sia nato dopo il 21 dicembre 827. Per un personaggio vivo la Start
Position è la data di nascita; la End Position si mette solo ai deceduti.

### Se la data di nascita non è nel canon

**Regola decisa dall'utente:** si sceglie la data più adatta confrontando il
**carattere del personaggio con il trittico zodiacale segno solare, ascendente e
segno lunare**, e la si dichiara come invenzione in `creator_notes`.

Il blocco JED+ ha già i campi `BIRTHDAY` e `ZODIAC` per registrarla, nella forma
usata da Jasper: `ZODIAC: Taurus (Sun), Gemini (Ascendant), Libra (Moon)`.

**Da verificare sempre:** che il segno solare dichiarato nel blocco `ZODIAC`
corrisponda davvero alla data di nascita salvata. Al 2026-09-06 dieci schede
hanno un blocco ZODIAC e **tutte e dieci sono coerenti**: quel controllo è a
zero e va tenuto lì.

Evitare il 1° gennaio e i primi del mese, che si riconoscono come segnaposto.

### Schede senza data di nascita, da fare in revisione

Quindici schede hanno `AGE` ma nessun Birthdate e nessun blocco ZODIAC, quindi
non possono usare `{{age}}` finché non gliene diamo una. Da fare **quando si
rivede la scheda**, non prima:

Bailey Rogers, Iordan R. Vess, Finnegan Novak, Barkley Rover, Professor Loewe,
Eris Davies, Jasmin Thompson, Stanley Davies Sr., Hank Thompson, Tate, Janice
Thompson, Nikolaj Jökull, Casey Williams, Jared Thompson, Stanley Davies Jr.

---

## 6. RPG Stats

- Sei stat: MGT, RES, AGI, WIT, PRS, SCT.
- **25 punti da distribuire** su base 1, quindi la somma finale è sempre **31**.
- **Livello = età**, con tetto a **99**: oltre il centinaio il salvataggio del
  blocco RPG fallisce in silenzio.

**Condition e Control, misurati:** Condition dipende **solo** dal Livello, parte
da 56 a Lv.1 e cresce di 1 per livello. Control parte da 46, cresce di 1 per
livello, **ma viene abbassato dalla distribuzione delle stat**. La vecchia
formula con basi 67 e 30 è da scartare.

---

## 7. Attitudes

**Alyssa e Jasper su ogni scheda**, perché sono i due personaggi giocabili. Chi
non li conosce va scritto lo stesso a **Unknown Scent**, con una motivazione che
dice che non si sono mai incontrati.

Oltre a loro, **solo i personaggi citati nel background**, col tier che il testo
giustifica davvero.

- **Target Type = World Character** quando il personaggio esiste come scheda.
  Generic (text) solo per fazioni, gruppi e concetti.
- **Mai The Player (Persona)** per un rapporto specifico: punta a chiunque stia
  giocando, quindi una motivazione scritta su Alyssa colpirebbe anche chi gioca
  Jasper.
- **Intensity va sempre scritta a mano**: lasciata vuota si salva come 1, il
  pavimento della banda. Convenzione: **50** default, **85** dove il rapporto
  *è* il personaggio, **20** per una conoscenza appena accennata.

Via API le attitudes sono un array sul Character, campo `attitudes`, e il campo
`target` resta vuoto: il legame vive in `target_id`.

### Ladder dei tier, etichetta → chiave salvata

| Etichetta | Soglia | Chiave |
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

L'AI riceve **l'etichetta**, non la chiave. **Non toccare la ladder**: la
corrispondenza è posizionale e riordinarla rimappa tutte le attitudes salvate.

Ritmo attuale, da neutro: Trusted a 18 gesti piccoli o 6 momenti forti, Pack a
28 o 10, Beloved a 46 o 16.

---

## 8. Toggle e campi accessori

- **Global Character = ON** su tutti.
- **Species e Occupation**: la nota storica diceva che non persistono. **Non è
  del tutto vero**: Logan le ha impostate e persistono. Dall'interfaccia il
  salvataggio fallisce perché l'app rimanda l'oggetto espanso invece dell'id;
  via API vanno scritte come `species_id` e `occupation_id` e restano.
- Keys, secondary keys, nickname, titoli, pronomi.

---

## 9. Verifica finale, che è la parte che non si salta

**Sempre dopo un reload completo, rileggendo dal server, mai dal form aperto.**

Controllare: zero `{{user}}`, zero em-dash, zero asterischi fuori dai pensieri
interni, tutti i campi ancora presenti con la lunghezza attesa, RPG ancora
abilitato col livello giusto, Attitudes presenti con intensità diversa da 1 e
nessun collegamento rotto.

**Aggiunte 2026-09-06:** Birthdate presente se la scheda usa `{{age}}`; blocco
ZODIAC coerente con la data di nascita; nessun numero d'età scritto a mano dove
poteva starci un macro.

### Tre trappole che hanno già fatto perdere lavoro

1. **Un click sul Save che non registra non dà errore.** Dopo ogni Save,
   verificare entro due secondi che il pulsante sia passato a "Saving...".
   Altrimenti il click è andato nel vuoto e il contenuto non è partito.
2. **Non mescolare interfaccia e API sulla stessa scheda nella stessa sessione.**
   Un salvataggio dell'interfaccia che sembrava non aver fatto niente può partire
   in ritardo e riportare indietro la scheda, sovrascrivendo quello che è stato
   scritto nel frattempo.
3. **Le cartelle si espandono solo dalla chevron**, che è il primo button della
   riga e non ha nome accessibile. Cliccare il nome non fa nulla. Una cartella
   collassata fa sembrare che un personaggio sia sparito.

**Quarta, aggiunta 2026-09-06:** un PUT sul World può rispondere **500 "Maximum
call stack size exceeded" e scrivere comunque**. L'errore non è la prova che il
salvataggio sia fallito: si rilegge e si guarda.

---

## 10. Documentare nel Project

Decisioni di scrittura, agganci creati verso altre schede, discrepanze fra le
fonti e ogni invenzione dichiarata.
