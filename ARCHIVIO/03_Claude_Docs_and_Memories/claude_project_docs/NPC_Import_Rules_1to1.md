# Regole di import per i dati NPC provenienti da bot 1:1

Stabilite da Lys il 02/09/2026, valide per tutti gli NPC ad alta frequenza di scena e per ogni materiale successivo di provenienza analoga.

## Il problema

I dati NPC che Lys fornisce vengono da **character card 1:1**, dove `{{user}}` è il giocatore generico. Nel World Svartúlfr, invece, **`{{user}}` è legato ad Alyssa Douglas-Bloodmoon**. Una traduzione meccanica `{{user}}` → Alyssa creerebbe quindi relazioni mai stabilite: una card che dice "è ossessionato da {{user}}" diventerebbe una dichiarazione che quel personaggio è ossessionato da Alyssa.

Va inoltre tenuto presente che quel materiale è spesso costruito attorno al rapporto con `{{user}}`, quindi l'epurazione non è un ritocco marginale ma tocca il cuore di alcune schede.

## Regola 1 — Generalizzare il ruolo, non nominare nessuno

Ogni riferimento a `{{user}}` va trasformato in una descrizione di **come il personaggio si comporta in quel tipo di rapporto**, senza nominare alcun personaggio del World.

- Sbagliato: "è ossessionato da {{user}}"
- Sbagliato: "è ossessionato da Alyssa"
- Giusto: "si lega in fretta e male a chi gli mostra attenzione"

Così si conserva il valore caratteriale del materiale senza inventare relazioni dentro il World. Nessun riferimento a `{{user}}` deve sopravvivere nel testo inserito.

## Regola 2 — Il materiale NSFW segue gli Intimacy Profile esistenti

Il contenuto sessuale o romantico esplicito legato a `{{user}}` **si mantiene**, con lo stesso registro delle entry `Intimacy Profile` già presenti nel Lexicon, ma **generalizzato e non puntato su nessun personaggio specifico**. È la scelta coerente con quanto il World già contiene.

## Conseguenza operativa

Ogni scheda NPC va toccata una volta sola: outfit e dati aggiuntivi insieme, con l'epurazione applicata prima dell'inserimento e non dopo.

## Campi da compilare su ogni NPC amplificato

Oltre a description, summary e outfit, vanno sistemati anche:

**First / Last Name.** Attenzione: alcune schede importate hanno il **nome completo dentro First Name** e Last Name vuoto. Va separato (trovato così su Janice Thompson).

**Nicknames / Aliases.** Solo quelli attestati nelle fonti. Alimentano il "Quick add from nicknames" dei Trigger Conditions degli outfit, quindi hanno un uso meccanico oltre che descrittivo.

**Middle Names.** Non sono attestati in nessuna fonte. Quelli inseriti sono **inventati** e cambiabili in un secondo: Jared *Wayne*, Janice *Mae*, Stanley *Rafael* (per un Junior il secondo nome coincide con quello del padre, quindi vale anche per Stanley Davies Sr.).

**Titles.** Attenzione: il campo **spezza sulla virgola**, quindi "Quarterback, SUCC Bulls" crea due chip. Inserire titoli brevi e senza virgole.

**RPG Stats.** Convenzione di progetto: **Livello = età anagrafica**, budget fisso **25 punti** sopra la base di 1 per stat. Vanno impostate anche **Species** e **Occupation**, che sui personaggi importati sono a "None". Le stat si assegnano cliccando i pulsanti + e -, non digitando.

| Personaggio | Lv | Species | Occupation | MGT | RES | AGI | WIT | PRS | SCT |
|---|---|---|---|---|---|---|---|---|---|
| Jared Thompson | 22 | Hybrids | Student | 10 | 8 | 5 | 1 | 5 | 2 |
| Stanley Davies Jr. | 21 | Weres/Shapeshifters | Student | 5 | 5 | 3 | 9 | 2 | 7 |
| Janice Thompson | 21 | Demi-humans | Student | 2 | 4 | 6 | 9 | 8 | 2 |

Le stat di Jared erano già presenti ma **con livello 21 invece di 22** e Species/Occupation vuote. Species e Occupation applicano bonus automatici visibili come badge "Sp +2" / "Oc +1" accanto alla stat.

## BUG PIATTAFORMA — Species e Occupation non si salvano

Nella sezione RPG Stats di un Character, i campi **Species** e **Occupation** **non persistono**. Impostati, mostrano il valore corretto; dopo Save e riapertura della scheda tornano entrambi a "None".

Verificato che **non è un problema dell'automazione**: testato sia con eventi sintetici sia con un **click reale del mouse** sul combobox e sull'opzione, su tre personaggi diversi. Livello e punti stat, salvati nello stesso momento e con lo stesso Save, **persistono correttamente**. È quindi un difetto lato piattaforma limitato a questi due campi.

Conseguenza pratica: i **bonus automatici di specie e occupazione** (i badge "Sp +2" / "Oc +1" accanto alle stat) non si applicano. Le stat allocate a mano restano valide. Da segnalare a Wyvern insieme all'errore 500 su `linked-characters`, e da riprovare quando la piattaforma viene aggiornata.

## Occupation mancanti nei Blueprint

Non esiste un'occupazione adatta a **insegnante** o **allenatore**, che servirebbe per Hank Thompson (PE teacher e coach) e Stanley Davies Sr. (insegnante di matematica). Da creare come Occupation Blueprint quando si riprende il lavoro sulla tab RPG: **Teacher** e possibilmente **Coach**.

## Tabella RPG aggiornata

| Personaggio | Lv | MGT | RES | AGI | WIT | PRS | SCT |
|---|---|---|---|---|---|---|---|
| Hank Thompson | 50 | 10 | 6 | 2 | 4 | 7 | 2 |
| Jasmin Thompson | 48 | 4 | 6 | 2 | 7 | 9 | 3 |
| Stanley Davies Sr. | 46 | 6 | 5 | 2 | 8 | 7 | 3 |
| Eris Davies | 43 | 4 | 5 | 3 | 9 | 8 | 2 |

Secondi nomi inventati anche per questi quattro: Hank *Wayne* (coerente con Jared), Jasmin *Lorraine*, Stanley Sr. *Rafael* (obbligato, coincide con quello del figlio Junior), Eris *Ortega* (dal cognome materno, née López Ortega).

## Scala salariale dei Job — revisione 02/09/2026

I salari delle vecchie entry erano stati messi senza una scala comune. Rivisti convertendo tutto in equivalente annuale e riallineati su valori californiani 2024 plausibili.

| Job | Prima | Dopo | Annuo |
|---|---|---|---|
| CEO | $25.000/mese | **$50.000/mese** | $600k |
| Security Commander | $9.000/mese | invariato | $108k |
| Bodyguard | $1.500/settimana | invariato | $78k |
| Master Blacksmith | $6.000/mese | invariato | $72k |
| Teacher | — | **$5.200/mese** (nuovo) | $62k |
| Stage Technician | $1.100/settimana | invariato | $57k |
| Mechanic | $3.000/mese | **$4.800/mese** | $58k |
| Bartender | $900/settimana | invariato | $47k |
| Line Cook | $850/settimana | invariato | $44k |
| General Laborer | $800/settimana | invariato | $42k |
| DJ | **$500/giorno** | **$700/settimana** | $36k |
| Server | $700/settimana | invariato | $36k |
| Student | $100/settimana | **$500/mese** | $6k |
| Divine Guardian, Living Saga, Matriarch, Patriarch | $0 | invariato | uffici, non impieghi |

**Il caso peggiore era il DJ:** a $500 al *giorno* faceva $182.000 l'anno, più di chiunque altro tranne il CEO. Il periodo giornaliero non ha senso per un lavoro a serata: portato a settimanale.

**CEO** era troppo compresso: a $300k stava solo tre volte sopra il Security Commander, poco per chi guida la DCC. Raddoppiato.

**Student** era a $100/settimana. Portato a **$500/mese** come borsa di studio o work-study, il che crea un contrasto voluto con la **Douglas Family Allowance da $500/settimana**: i figli Douglas ricevono senza lavorare più di quattro volte quello che uno studente normale racimola.

## Aggancio Solarton High (canonico, da Lys)

**Hank Thompson e Stanley Davies Sr. insegnano entrambi alla Solarton High School.** Ne consegue che:

- **Alyssa e Jasper**, al primo anno di college e provenienti dalla Solarton High, con ogni probabilità **hanno avuto entrambi come professori**.
- **Edric**, quando andrà alle superiori, **li troverà come suoi professori**.

È un ponte diretto fra la famiglia Douglas e la famiglia Thompson/Davies che prima non esisteva, e va scritto sulle schede di Alyssa, Jasper ed Edric oltre che su quelle di Hank e Stanley.
