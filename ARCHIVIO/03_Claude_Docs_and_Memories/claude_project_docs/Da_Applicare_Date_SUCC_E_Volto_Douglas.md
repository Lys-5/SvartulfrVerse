# Date SUCC e volto della linea Douglas: applicato

Deciso e applicato il 2026-09-07. **Tutto verificato dopo reload completo**,
rileggendo dal server.

---

## 1. Le date della SUCC

**Fondazione 1887. Apertura agli studenti umani 2002.** Sono le date del
lorebook ufficiale dell'autore, e il 2002 è confermato anche dal portale.

### Perché le vecchie non reggevano

La nota di canon che avevamo scritto diceva due cose false.

*"Una fonte più vecchia diceva 1887 ed è superata."* Al contrario: 1887 è il
lorebook, cioè la fonte più forte sul dominio SUCC. **Il 1908 non veniva da
nessuna fonte SUCC: veniva dal confine della nostra Modern Era**, che comincia
il 31 dicembre 1907. Era una data nostra riusata come se fosse una fonte.

*"Il 2002 è posteriore al primo incontro fra Erik e Nixara al college."* Vero e
irrilevante: il 1992 nella scheda di Erik è la fine della sua capitaneria dei
Bears (1988-1992), e Nixara è una Bloodmoon, quindi licantropa. Nessuno dei due
aveva bisogno di un campus aperto agli umani. **L'adattamento era costruito su
un problema che non esiste**, ed è stato rimosso.

### Cosa è cambiato

| Dove | Cosa |
|---|---|
| Lexicon `1908 Fondazione della SUCC` | Rinominata **`1887 Fondazione della SUCC`**, testo riscritto, chiave `1908` → `1887`, nota di canon rifatta |
| Lexicon `1992 La SUCC apre agli studenti umani` | Rinominata **`2002 La SUCC apre agli studenti umani`**, testo riscritto, chiave `1992` → `2002`, adattamento rimosso e spiegato |
| Lexicon `Rivalry with CUMS` | "began in 1992" → 2002 |
| Environment CUMS | due occorrenze, 1992 → 2002 |
| Location `Archer Wolfwood Hall` | 1992 → 2002 |
| Character `Archer Wolfwood` | vedi sotto |

**Residui legittimi:** il 1992 di Erik (Bears), e i due riferimenti dentro le
note di canon, che devono citare la data rimossa per spiegare la correzione. Il
"1908" di Elizabeth e il "1867" di Nixara erano **falsi positivi**: sequenze
dentro id con timestamp, non date.

### Due cose che il 1887 ha aggiunto gratis

Un ateneo per soli soprannaturali fondato nel 1887 cade **in piena Age of
Secrecy**, ed è esattamente il tipo di istituzione che quell'era produce. E il
2002 dà una cronologia utile: nel 2024 chi studia a SUCC è la **seconda
generazione di un esperimento di ventidue anni**, e i genitori di molti studenti
hanno frequentato un ateneo dove gli umani non potevano entrare, Erik e Nixara
compresi.

---

## 2. Archer Wolfwood, nato nel 1846

Il 1887 spezzava la catena su cui è costruita la sua scheda: nato a New Orleans
nel 1867, "in his thirties" quando le leggi Jim Crow smontavano la città, andato
a ovest nel 1908 a quarantun anni. Con la fondazione al 1887 avrebbe avuto venti
anni ed essere ancora in Louisiana.

**Scelta dell'utente: spostare la nascita al 14 maggio 1846.** Così ha
quarantun anni nel 1887 e fonda davvero l'università, e la catena non solo
regge, migliora: i suoi trent'anni diventano il **1876-1886**, cioè il crollo
della Ricostruzione e le legislature dei Redeemers, che è storicamente il
momento esatto in cui quelle leggi vengono scritte.

Applicato: `BIRTHDAY: May 14, 1846`, birthdate e Start Position portate a
**8927064**, "forty-one in 1887", "went west in 1887", "he was born there in
1846", "a hundred and fifty-six" al momento dell'apertura del 2002, e il
Dialogue Example rinominato "The thing he did in 2002". Ha **178 anni** nel
2024, contro i 157 di prima. Irrilevante per un Pureblood, e la scheda già
diceva "reads as a man in his sixties, and has for a very long time".

**Una modifica di prosa fatta apposta:** "he spent a childhood in streets where a
dozen peoples lived on top of each other and the arrangement, imperfectly and
loudly, worked" è diventato "he spent **his twenties** in streets...". Con la
nascita nel 1846 l'infanzia cadeva nella New Orleans anteguerra, e quella frase
avrebbe finito per dire che la convivenza funzionava in una città schiavista.
Spostata ai suoi vent'anni, la finestra formativa diventa il **1866-1876**, cioè
la Ricostruzione, che è il periodo in cui quella frase è vera.

---

## 3. Il volto della linea Douglas

Errore trovato dall'utente in chat: **Magnus aveva capelli bianco-argento**,
mentre i colori signature della linea sono **capelli neri e occhi ambra**.

### Stato trovato

- **Cornelius**: già corretto in due outfit ("the Douglas black hair worn long",
  "Black hair, amber eyes, no smile"), ma **senza campo HAIR/EYES** nel blocco
  JED+.
- **Magnus**: `HAIR/EYES: Silver-white hair, pale amber eyes`, più l'outfit House
  Formal con "Silver-white hair combed back". **L'errore vero.**
- **Erik, Logan, Malachia**: già corretti.
- **Edric**: **nessun campo HAIR/EYES**.

### Cosa è stato scritto

Aggiunti i campi mancanti a Cornelius ed Edric. Magnus corretto in tutti e tre i
punti (JED+, summary, outfit): **nero pettinato all'indietro, argentato solo
alle tempie**, occhi ambra. Ho tenuto l'argento alle tempie perché a
trecentocinquantacinque anni serve qualcosa che lo distingua come il più vecchio
dei quattro, e Logan a quarantanove ha già "greying at the temples", quindi il
dettaglio esiste già in famiglia. **Se lo vuoi completamente nero si cambia in
un minuto.**

### La nuova entry Lexicon `The Douglas Face`

Global ON. Ripetere due campi su cinque schede dà al modello i dati ma non
l'osservazione, e nessun personaggio la farebbe mai notare in scena. La entry
dice la cosa esplicitamente: che **Magnus, Erik, Malachia ed Edric affiancati
leggono meno come quattro parenti che come lo stesso uomo fotografato in quattro
momenti della vita**, che gli estranei lo trovano vagamente inquietante senza
saper dire perché, e che la famiglia ha smesso di accorgersene.

Contiene anche la riga che tiene in piedi il segreto di Logan: **siccome il
colore è universale in famiglia, non prova niente su nessuno.** La somiglianza
in questa linea la porta l'osso, non il pigmento, e le uniche osservazioni che
valgono qualcosa riguardano la forma di una faccia, non il colore.

### Edric: la versione soft, scelta dall'utente

Ripresa da una vecchia sistemazione: **Edric è identico a Malachia alla stessa
età**. Nella sua scheda c'è ora la sezione `THE FAMILY FACE`, scritta come una
constatazione da vecchia foto di famiglia, non come qualcosa che qualcuno fa
notare con intenzione. La gente lo dice ogni tanto, è gentile, e non va oltre:
un ragazzo che somiglia a suo cugino non è un fatto che richieda spiegazioni.

**Perché funziona meglio della versione affilata:** Malachia è figlio di Erik,
quindi dire che Edric somiglia a Malachia veicola la stessa identica
informazione genetica di dire che somiglia a Erik, ma la dice in un modo che non
punta il dito. Fra cugini una somiglianza è normale; fra un ragazzo e suo zio è
una domanda. L'indizio resta sul tavolo senza obbligare nessuno a raccoglierlo,
e il segreto resta di Logan.

**Il regalo inaspettato:** la sezione chiude con "He tells people he has his
mother's eyes", che aggancia il Dialogue Example già esistente, *"I mean, I got
my mom's eyes, everybody says that."* La scheda di Edric dice che sua madre è
una donna che se n'è andata e non è mai tornata, e che Logan non ne parla.
Quindi **nessuno può avergli mai detto che ha gli occhi di sua madre**: se l'è
inventato. Ed è falso due volte, perché quegli occhi sono l'ambra Douglas che
hanno tutti. Non ho toccato la battuta: adesso regge da sola.
