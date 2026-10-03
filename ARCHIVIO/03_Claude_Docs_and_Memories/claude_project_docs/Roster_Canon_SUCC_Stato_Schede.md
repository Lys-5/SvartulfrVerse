# Roster canon SUCC: chi c'è e in che stato è la scheda

Rilevato il 7 settembre 2026 incrociando lo screenshot del roster ufficiale
inviato da Lys con lo stato reale delle schede letto via API.

**Il roster canon è 26 nomi. Ci sono tutti e 26.** Nessuno manca, nessuno è
duplicato. Il problema non è la copertura, è la profondità.

---

## Class of 2024, studenti in evidenza (18)

| Scheda | Stato | Outfit | Dialoghi | Attitudes | Birthdate |
|---|---|---|---|---|---|
| Finnegan Novak | scritta, 10273 | 5 | 0 | 5 | no |
| Andrew Campbell | scritta, 9827 | 5 | **5** | 5 | sì |
| Vincent Campbell | scritta, 9281 | 5 | **5** | 6 | sì |
| Casey Williams | scritta, 7878 | 5 | 0 | 3 | no |
| Jared Thompson | scritta, 7519 | 7 | 0 | 5 | no |
| Tate | scritta, 7498 | 5 | 0 | 2 | no |
| Oskar | scritta, 7260 | 5 | 0 | 4 | no |
| Nikolaj Jökull | scritta, 7181 | 5 | 0 | 2 | no |
| Iordan R. Vess | scritta, 6771 | 5 | 0 | 2 | no |
| Stanley Davies Jr. | scritta, 6219 | 5 | 0 | 6 | no |
| Bailey Rogers | scritta, 4386 | 5 | 0 | 3 | no |
| Janice Thompson | scritta, 4267 | 6 | 0 | 3 | no |
| Chase Anderson | **breve, 2924** | **0** | 0 | **0** | sì |
| Tomas Matthews | **breve, 2238** | **0** | 0 | **0** | sì |
| Santiago Herrera | **breve, 948** | **0** | 0 | **0** | no |
| **Fade Greymoor** | **VUOTA** | 0 | 0 | 0 | no |
| **Mackenzie Sanchez** | **VUOTA** | 0 | 0 | 0 | no |
| **Roland Vickers** | **VUOTA** | 0 | 0 | 0 | no |

## Staff SUCC in evidenza (4)

| Scheda | Stato | Outfit | Dialoghi | Attitudes |
|---|---|---|---|---|
| Dullahan (Coach Dully o' Han) | scritta, 7901 | 5 | **5** | 3 |
| Richard Loewe (Professor Loewe) | scritta, 7563 | 5 | 0 | 3 |
| Ariadne Cirillo (Nurse Cirillo) | scritta, 6527 | 5 | 0 | 2 |
| Barkley Rover (Assistant Coach) | scritta, 5091 | 5 | **5** | 3 |

Nello screenshot ci sono **due caselle staff vuote marcate "x"**, cioè non
riempite nemmeno dalla fonte. È plausibile che una sia **Hideo Reid**, che la
wiki elenca fra lo staff e che abbiamo appena creato come stub, ma è
un'ipotesi e non un dato: lo screenshot non lo dice.

## Alumni, famiglia e amici (4)

| Scheda | Stato | Outfit | Dialoghi | Attitudes |
|---|---|---|---|---|
| Hank Thompson | scritta, 7429 | 5 | 0 | 3 |
| Stanley Davies Sr. | scritta, 4068 | 5 | 0 | 4 |
| Eris Davies | scritta, 3982 | 5 | 0 | **0** |
| Jasmin Thompson | scritta, 3775 | 5 | 0 | **0** |

Anche qui **due caselle "x" vuote** nella fonte.

---

## Cosa dice davvero questa tabella

**1. La copertura è completa, la profondità no.** Ventisei su ventisei esistono,
ma **ventidue su ventisei non hanno un solo Dialogue Example**. Ce li hanno solo
Andrew, Vincent, Dullahan e Barkley. È il buco più uniforme e più grosso di tutto
il roster: il modello ha la biografia di questi personaggi e non ha mai sentito
come parlano.

**2. Tre schede del roster principale sono completamente vuote.** Fade Greymoor,
Mackenzie Sanchez e Roland Vickers sono studenti *in evidenza* della Class of
2024, cioè gente con cui Alyssa e Jasper condivideranno le aule dal 26 agosto, e
oggi sono tre nomi senza niente dietro.

**3. Tre sono troppo corte per reggere una scena.** Santiago Herrera a 948
caratteri è il caso peggiore, ed è un giocatore dei Bulls, quindi comparirà
accanto a Jared e Bailey ogni volta che si parla di football. Chase e Tomas sono
poco sopra, e tutti e tre non hanno outfit, dialoghi né attitudes.

**4. Solo cinque su ventisei hanno una data di nascita.** Andrew, Vincent, Chase,
Tomas e Ariadne. Gli altri ventuno non possono usare `{{age}}` e hanno l'età
scritta a mano o assente.

**5. Nessun conflitto di nomi con la fonte.** "Nurse Cirillo" è la nostra Ariadne
Cirillo, e la sua scheda dice già `JOB: Nurse at the SUCC campus health centre`.
"Coach Dully o' Han" e "Assistant Coach Barkley" corrispondono. L'unico scarto è
**Mackenzie Sanchez** nella fonte contro **Mackenzie Sanchez Rogers** da noi: il
secondo cognome è una nostra estensione, legata a Luisa Sanchez Rogers e Dominic
Rogers che sono personaggi nostri.

---

## Modern Fantasy / Los Angeles Underworld

Lo screenshot della griglia Modern Fantasy contiene **circa 37 ritratti senza
nomi**, più cinque caselle segnaposto con l'icona del lupo. Dall'immagine non si
ricava nessun nome, quindi non ci si può fare un censimento.

Il roster va preso dalla pagina wiki, che è già fra le fonti registrate:
`https://ioverse.fandom.com/wiki/Modern_Fantasy`. Da fare aprendo la pagina nel
browser secondo la §11, non con un fetch.

Quello che sappiamo già di quel dominio: la Ballantine Family e i Sinner sono di
Los Angeles e a Solarton o Blackwood hanno al massimo informatori e mani locali
pagate (deciso il 7 settembre). Quindi quel roster è, per adesso, **materiale di
sfondo**: nessuno di quei personaggi si presenta di persona a Blackwood senza che
sia un evento.

---

## Priorità che ne discende

In ordine, e il criterio è quando il personaggio entra davvero in scena:

1. **Le tre schede vuote del roster principale**: Fade Greymoor, Mackenzie
   Sanchez, Roland Vickers.
2. **Le tre schede troppo corte**: Santiago Herrera per primo, poi Chase e Tomas,
   che hanno già la data di nascita e il trittico zodiacale.
3. **I Dialogue Examples sulle ventidue schede che non ne hanno.** Si può fare a
   blocchi, e su schede già scritte è il passo che rende di più per il tempo che
   costa.
4. **Le ventuno birthdate mancanti**, col metodo del trittico, al momento della
   revisione di ciascuna scheda.
