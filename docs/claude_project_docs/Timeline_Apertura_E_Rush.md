# Timeline del World: apertura 5 aprile 2024 e calendario degli eventi

Deciso dall'utente il 2026-09-06. **Questa pagina vince su qualunque altro
documento che dia una data di apertura diversa, o che dia Alyssa e Jasper per
residenti di una casa greca.**

---

## Principio

**Tutto il World è scritto come vero al 5 aprile 2024.** Descrizioni, schede,
Location ed Environment raccontano lo stato delle cose a quella data.

**Tutto quello che viene dopo è una entry Lexicon di tipo Event con una data
programmata**, così il World sa da solo quando una cosa avviene e non serve
riscrivere le schede a ogni salto temporale.

## Il World Clock

**`world_age` = 10.731.648 ore = venerdì 5 aprile 2024.** Impostato e verificato
dopo reload completo.

> **Nota sul salvataggio.** Il PUT ha risposto **500, "Maximum call stack size
> exceeded"**, e ha scritto lo stesso. Variante del bug del Save appeso (§15):
> verificare rileggendo, non ripetere.

Valore precedente: 10.950.000, cioè **3 marzo 2049**, sbagliato di
ventiquattro anni e mezzo. **Lo spostamento indietro era sicuro**, verificato
prima: solo 8 Character e 7 fra Location ed Environment hanno una Start
Position, e nessuna cade dopo il 2024. Le uniche End Position sono Lord
Cornelius (1856) e Nixara (2005), entrambe passate.

## Come si programma un evento (meccanica confermata)

Un Lexicon di tipo `event` ha **due sistemi temporali distinti**, e servono a
cose diverse:

| Campo | Cosa fa |
|---|---|
| `start_timeline_position` / `end_timeline_position` | Finestra in cui la entry è **eleggibile per lo scan normale** del lexicon. Serve per i fatti storici: la entry non esiste prima di quella data |
| `event_config` | **Programmazione a calendario.** È questa che fa comparire l'evento nel blocco *Pending Events* del prompt quando si avvicina o scade |

Forma di `event_config`:

```js
event_config: {
  scheduled_position: 10731840,      // ore assolute del World
  scheduled_end_position: 10731864,  // fine. Con all_day = inizio + 24
  all_day: true,
  show_to_ai: true                   // e' questo che lo mette in Pending Events
}
```

Nell'interfaccia sono i campi **Calendar Event Properties**: Scheduled, Year,
Month, Day, All day, Show to AI. Il toggle "Scheduled" è acceso semplicemente
quando `scheduled_position` è un numero.

**Nota della piattaforma da tenere presente:** il calendario condiviso del party
mostra solo eventi creati in sessione dal widget Calendar. Una entry autorata a
livello di World, come le nostre, **non compare lì** finché non viene agganciata
a un party. Questo non toglie niente allo scopo: `show_to_ai` la fa comunque
arrivare al modello nel blocco Pending Events.

## Gli otto eventi creati

Tutti `type: event`, `is_global: true`, `all_day: true`, `show_to_ai: true`,
verificati dopo reload.

| Data | Entry | Ore |
|---|---|---|
| sab 13 apr 2024 | Admitted Student Days (SUCC) | 10.731.840 |
| lun 22 apr 2024 | Compleanno dei gemelli e festa di Wulfnic (4 giorni) | 10.732.056 |
| mer 1 mag 2024 | Decision Day | 10.732.272 |
| lun 15 lug 2024 | Road trip con Logan | 10.734.072 |
| lun 19 ago 2024 | Full Moon Festival | 10.734.912 |
| dom 25 ago 2024 | Pranzo della domenica | 10.735.056 |
| lun 26 ago 2024 | Primo giorno alla SUCC | 10.735.080 |
| gio 31 ott 2024 | Halloween University Party | 10.736.664 |

**Il 5 giugno non è stato creato.** L'utente lo ha messo in elenco senza dire
cosa sia, e non si inventa per riempire un buco (§9.4). Appena si sa cosa
succede, si aggiunge.

I giorni della settimana sono tutti verificati. Il 13 aprile è un **sabato** e
il 25 agosto è una **domenica**: entrambe reggono da sole quello che gli si
chiede di essere.

## Il calendario delle ammissioni: come l'ho interpretato

L'utente ha scritto "1 maggio, scadenza invio domande". **L'ho reso come
scadenza di risposta, non di invio**, ed è una scelta che va confermata.

Il motivo: negli Stati Uniti il 1 maggio è il *National College Decision Day*,
il giorno entro cui chi è stato ammesso deve accettare un posto. Le domande per
l'autunno 2024 scadevano fra novembre 2023 e gennaio 2024. E gli **Admitted
Student Days sono per definizione riservati a chi è già stato ammesso**: se il 13
aprile c'è un open day per ammessi, il 1 maggio non può essere la scadenza delle
domande.

Con la lettura "giorno della risposta" la sequenza dell'utente diventa un arco a
tre tempi che funziona da solo: **le lettere sono già arrivate, il 13 aprile si
va a vedere il posto, il 1 maggio si risponde.** E non contraddice l'anno
sabbatico: i gemelli hanno fatto domanda durante il sabbatico, per entrare ad
agosto.

Se preferisci l'altra lettura, cambia una riga nella entry Decision Day.

## Le lune piene: due conferme e una correzione

Calcolate sul mese sinodico e riportate all'ora della California (PDT, UTC-7).

| Mese | Picco in California |
|---|---|
| aprile 2024 | **martedì 23 aprile, 09:50** |
| agosto 2024 | **lunedì 19 agosto, 12:46** |
| ottobre 2024 | giovedì 17 ottobre, 14:14 |

**Il Full Moon Festival del 19 agosto cade esattamente sulla luna piena.**
Perfetto, non serve toccare niente.

**Correzione: la luna piena di aprile è il 23, non il 24.** La finestra della
festa, 22-25 aprile, la copre comunque, quindi il piano regge: cambia solo su
quale notte cade il momento in cui il branco è al massimo. **Il 23 è la notte
buona**, ed è anche il giorno dopo il compleanno, che è meglio del giorno stesso:
si arriva alla luna piena avendo già passato una giornata insieme.

**Halloween 2024 non è di luna piena**, quella di ottobre è il 17. È scritto
esplicitamente nella entry, perché toglie l'alibi comodo a chiunque combini
qualcosa quella notte. Il 31 ottobre è anche il compleanno di Erik.

## Le date d'ancoraggio che il World già contiene

Verificate leggendo le schede, non assunte.

- **Nixara Bloodmoon**: Start 9 giugno 1975, End 22 aprile 2005. Il suo
  diciannovesimo compleanno è il **9 giugno 1994**.
- **Alyssa e Jasper** nascono il 22 aprile 2005, il giorno in cui Nixara muore.
- **Erik Douglas** nasce il 31 ottobre 1969.

**Il parallelo del 1994 regge, ed è più duro di quanto sembri.** Wulfnic rifà per
i nipoti la festa che fece per la figlia, alla stessa età, trent'anni dopo. Ma
quella festa è l'origine del legame che ha prodotto i gemelli, e quindi
indirettamente della morte di Nixara. **Il compleanno dei gemelli è
l'anniversario della morte della madre**, e Wulfnic sta scegliendo di celebrarlo
rifacendo la festa che ha messo in moto quella storia, davanti a un continente di
testimoni, con la nipote che il culto considera Hvit tornata. Non è un richiamo
affettuoso, è un uomo che riavvolge il nastro. Ed è scritto nella entry.

I branchi arrivano perché Wulfnic è **Alpha of Alphas del Nord America**: quando
convoca, si va.

## Lo scenario di apertura: "What Do You Want To Do"

Creato il 2026-09-06. Venerdì 5 aprile 2024, 18:20, cucina di Villa Douglas.
`insertion_point` 10.731.648. Personaggi giocabili: **Alyssa e Jasper**, entrambi.

Scenario lite, una scena sola. La casa è vuota, cosa che di venerdì sera non
succede mai. Erik è rientrato alle quattro, cosa che di venerdì non fa mai. Le
lettere di ammissione sono nell'atrio da tre settimane, sotto il sigillo del
clan, e nessuno le ha spostate: in questa famiglia le cose importanti si lasciano
in mezzo al corridoio finché qualcuno non ha il coraggio di raccoglierle.

Erik fa il caffè con la macchina sbagliata perché quella giusta è di Noah e ha
undici pulsanti. Dice che il diploma è di giugno scorso e che fra due mesi è un
anno. Dice che non gliel'ha chiesto per dieci mesi e che glielo sta dicendo, non
rinfacciando. Conta i giorni al primo maggio, perché contare qualcosa lo tiene
occupato, ed è la terza volta che li conta oggi.

Poi dice **"Non vi sto dicendo cosa scegliere"**, lo sente uscire come un ordine,
vede benissimo di averlo detto come un ordine, e non sa come si dice altrimenti.

**"Quindi ve lo chiedo. Cosa volete fare."**

La scena finisce lì. Nessuno dei due gemelli risponde, perché sono entrambi
giocabili e la risposta è del giocatore. In coda, il Narratore ricorda che fra
diciassette giorni compiono diciannove anni e che Wulfnic ha già cominciato a
chiamare i branchi, e che Erik lo sa e non lo tira fuori adesso, perché sta
facendo una cosa sola per volta, che per lui è già uno sforzo.

## Cosa NON è deciso all'apertura

Il 5 aprile 2024 Alyssa e Jasper **non hanno una confraternita, non hanno un
alloggio al campus, e non hanno ancora nemmeno scelto l'università.** Vivono a
Villa Douglas.

Due inviti arriveranno ad agosto, e **nessuno dei due esiti è deciso**:

- **Scarlett Rose proporrà ad Alyssa la Theta Iota Theta.**
- **Noah spingerà Jasper alla rush della Kappa Sigma Alpha.**

Si giocano on-game. Non scrivere nessuno dei due gemelli come membro, residente o
vicino di casa sulla Row finché non è successo in partita.

---

## Correzioni fatte per allineare il World al 5 aprile

### Quattro affermazioni di residenza premature

Avevo scritto la Row come se i gemelli fossero già sistemati. Tre errori su
quattro erano miei.

| Dove | Diceva | Dice ora |
|---|---|---|
| **Alpha Rho Omega** | "Finn e Alyssa vicini di casa immediati" | Il portico ARO guarda i gradini della TIT, quindi Finn è vicino di **chiunque** ci abiti in una data stagione |
| **Theta Iota Theta** | "La confraternita dove risiede Alyssa" (preesistente) | Riscritta: casa da party, informale, popolare fra le succubi. Residenti Sierra e Scarlett |
| **Kappa Sigma Alpha** | "Noah vede la porta di casa di Alyssa" | "vede la porta della Theta Iota Theta". E **Noah spingerà Jasper alla rush** |
| **Lexicon Frats & Sororities** | "Alyssa lives here" | Rimosso, e aggiunta la sezione **PLEDGING, AND WHERE THE TWINS ACTUALLY ARE** |

**La lezione.** Una geografia coerente ti fa scrivere conseguenze che sembrano
ovvie. "Finn è ad ARO, Alyssa è alla TIT, quindi sono vicini di casa" è
un'inferenza corretta da una premessa che nessuno aveva stabilito. Il vicinato
Finn-Alyssa **non è canon: è una posta in gioco**, e vale molto di più così.

### La scheda di Jasper, riscritta due volte

La sezione **THE HOUSE ACROSS THE ROAD** era stata scritta per un'apertura ad
agosto ("rush is this week", "comincia a SUCC domattina"). Con l'apertura al 5
aprile è stata rifatta: la rush è a fine agosto, lui non ha nemmeno scelto
l'ateneo, e quello che esiste adesso è **l'assunzione**, che ha cominciato a fare
rumore. Erik l'ha nominato due volte quest'anno nel tono di chi conferma una data
di consegna. **Noah ha cominciato a dire "quando entri" invece di "se entri"**, e
non è un lapsus, perché Noah su queste cose non ha lapsus.

Chiude con: *non ha detto di no, ha tutta l'estate per continuare a non dirlo, e
intende usarla tutta.*

### Lo scenario "First College Day" aveva la data sbagliata

`insertion_point` valeva **5712 ore, cioè 26 agosto dell'anno 800**, mentre il
testo della scena dice "Lunedì 26 agosto 2024". Era una data inserita senza
l'offset dell'anno. Corretto a **10.735.080**.

È la stessa classe di errore delle quattro Location con Start Position negativa,
vedi sotto.

---

## Errore mio, e come è stato scoperto: la fondazione del 1992

Nella entry Lexicon **Founding of SUCC** c'era scritto che Archer Wolfwood aprì
SUCC agli umani nel **1992**. Il portale ufficiale dice **2002**, riverificato
alla fonte. Applicando §10 l'ho "corretta" a 2002, propagando il 2002 anche in
Rivalry with CUMS, Archer Wolfwood Hall e l'Environment CUMS.

**Era sbagliato correggerla. Il 1992 è un adattamento deliberato del progetto**,
fatto per far tornare la lore del primo incontro fra Nixara ed Erik al college.
L'utente me l'ha ricordato e **ho ripristinato tutti e quattro i punti al 1992**,
verificato: nel World non compare più nessun 2002.

**Perché ci sono cascato, e cosa cambiare.** `Solarton_Canon_E_Conflitti.md` dice
già la regola giusta: *un adattamento deliberato è ammesso, e ogni adattamento va
registrato lì*. Ma quell'adattamento **non era registrato da nessuna parte**,
quindi dall'esterno era indistinguibile da un errore di trascrizione, ed è
esattamente il caso che quella regola esiste per prevenire.

**Regola operativa che ne segue:** prima di "correggere" una data o un dato del
World contro una fonte esterna, controllare se è un adattamento voluto. Se non è
scritto da nessuna parte, chiedere invece di correggere. Una discrepanza con la
fonte ufficiale non è di per sé un errore: in questo progetto è spesso una
decisione.

**Adattamento ora registrato:** l'apertura di SUCC agli studenti umani è nel
**1992**, non nel 2002 del portale, per far coincidere l'ateneo aperto con gli
anni in cui Erik (capitano dei Bears 1988-1992) e Nixara si incontrano.

---

## Da fare

- **Definire il 5 giugno 2024** e creare la entry Event corrispondente.
- **Le quattro Location con Start Position negativa.** The Verve (-162.816),
  Lunar Quad (-1.016.856), Villa Douglas e Seven Hills (-3.138.144) cadono prima
  dell'800 d.C.: Villa Douglas risulterebbe fondata nel 442. Sembrano offset
  all'indietro rispetto a "adesso" (-358 anni da 2024 fa 1666, coerente con una
  Blackwood coloniale del Seicento e una villa vecchia di 400 anni) messi dove
  andava un valore assoluto. Non blocca niente, ma sono sbagliate.
- **Confermare la lettura del 1 maggio** come giorno della risposta.
- **La scheda di Scarlett Rose** deve reggere il fatto che proporrà la TIT ad
  Alyssa. Da verificare se il gancio c'è già.
- **La scheda di Alyssa** non contiene affermazioni di alloggio: va bene così, e
  conviene che resti così finché non si gioca.
