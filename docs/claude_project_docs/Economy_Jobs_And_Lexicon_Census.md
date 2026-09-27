# Economia Wyvern, Job e censimento Lexicon

Parte 16 del lavoro sul World Svartúlfr | Urban. Aggiornato 01/09/2026.
Da consolidare in `claude/Review_Pending_Status.md` al prossimo backup.

---

## PARTE 16 — Economia: allowance, job di The Verve, e il censimento del Lexicon

**RICERCA WIKI — NON ESISTE UN MECCANISMO "ALLOWANCE" NATIVO.** Confermato leggendo `Items-Currency-Markets` e `Property-Furnishings-Market` (fetch diretto 403, letti dal browser autenticato). L'unica fonte di reddito ricorrente su Wyvern è la **Lexicon entry di tipo Job**, con un blocco **Job Config**: Wage, Currency, Pay Period (Daily/Weekly/Monthly/custom), Scope (Global = Job Board mondiale / Local = solo dove è offerta), e "Only paid while at the workplace". L'ipotesi dell'utente era corretta.

**ALTRE MECCANICHE ECONOMICHE DISPONIBILI** (non ancora usate): le Location possono essere `Purchasable` e/o `Rentable` con **rent** (per gli affittuari) e **property tax / bills** (per i proprietari), periodo Daily/Weekly/Monthly/custom; il settlement avviene solo quando **avanza il tempo in-world** (viaggio o `>rest`/`>advance-time`) e ogni ciclo trascorso viene applicato, senza saltarne nessuno; se il giocatore non copre un costo la differenza diventa **debito** tracciato nel Ledger e nota all'AI. Esiste un tipo Lexicon **`furniture`** che il filtro dell'interfaccia non espone. Comandi giocatore: `>takejob`, `>quitjob`, `>paydebt`, `>rent`, `>buy`, `>use`, `>gift`.

**DOVE STA LA CONFIGURAZIONE (importante, la wiki è fuorviante).** La wiki parla di "Coordinates tab" e di una "Marketplace section" nella Location. In realtà tutto sta in **Locations → [location] → Simulation Overrides**, in fondo al pannello: `Enable Marketplace`, `Purchasable Property`, `Jobs Offered Here`. Non è nell'editor delle Maps.

**CURRENCY.** Già esistente e non andava creata: **US Dollar**, simbolo `$`, 2 decimali, UC Rate 1. In `Simulation → World Features` risultano già attivi Inventory & Items, Currency & Economy, RPG Stats, Combat, Cross-World Ships, Party Stats, Relationships; disattivo solo Creature Catcher.

**DOUGLAS FAMILY ALLOWANCE — creata.** Job, **$500 / Weekly**, **Scope Local**, **"Only paid while at the workplace" ON**, agganciata a **Villa Douglas** in Jobs Offered Here. Scelta dell'utente: i soldi non si ricevono via bonifico, si ritirano di persona. Il testo è stato riscritto di conseguenza: Erik paga in contanti dallo studio della villa e paga solo a chi va a prenderli, non ha mai detto perché e nessuno in famiglia ha mai avuto bisogno che glielo spiegasse; saltare la settimana non produce arretrati e non viene commentato. Keywords: allowance, Douglas allowance, family allowance, weekly allowance, stipend.

**JOB PER THE VERVE — 5 nuove entry create**, tutte Job / US Dollar / Weekly / Local / workplace-bound:
- **Bartender** $900 — competenze non scritte sul cartello: quali specie metabolizzano l'alcol in secondi, argento fuori dal vassoio delle guarnizioni, e che un lupo che ha smesso di parlare è un problema peggiore di uno che urla.
- **Server** $700 — l'etichetta che nessuno mette per iscritto: non si allunga il braccio davanti a un vampiro, non si perde di vista il bicchiere di un demi-human, ci si annuncia prima di avvicinarsi a un tavolo di lupi da dietro.
- **Line Cook** $850 — porzioni pesanti, argento vietato in cucina, la stazione del sangue ha coltelli e stoccaggio propri.
- **Stage Technician** $1100 — mezzo mestiere e mezzo risk management: strobo programmati intorno alle specie che vanno in crisi, volume tenuto sotto la soglia umana perché un branco sente i bassi nei denti, rigging controllato due volte a mano ogni sera.
- **General Laborer** $800 — uno dei pochi settori di Blackwood dove essere visibilmente non-umano **alza** la paga invece di abbassarla.

**JOB PREESISTENTI — già tutti configurati**, nessun intervento necessario: Bodyguard $1500/week, DJ $500/day, Mechanic $3000/month, CEO $25000/month, Student $100/week (tutti Global).

**JOBS OFFERED HERE @ THE VERVE — 8 job agganciati e salvati:** Bartender, Server, Line Cook, Stage Technician, General Laborer, Bodyguard, DJ, Mechanic.

**CENSIMENTO LEXICON PER TIPO** (108 prima di questo lavoro, **114** dopo): concept 58, memory 19, mob 9, item 7, vehicle 7, job 5→11, event 3. **Tutte le entry erano in Uncategorized**, quindi la riclassificazione parte da zero.

**DUE SCOPERTE DAL CENSIMENTO:**
1. Le entry `Species_Details` e `Intimacy Profile` **sono già tutte di tipo Memory**. Il lavoro residuo non è una conversione di tipo ma solo impostare l'**Attached Character** su ognuna delle 19 entry memory.
2. Gli **Occupation RPG Blueprint sono 11**, non solo "Student" come annotato in precedenza: Bodyguard, CEO, DJ, Divine Guardian, Living Saga, Master Blacksmith, Matriarch, Mechanic, Patriarch, Security Commander, Student. Le Species sono 10 (le 9 note + **Primordial**).

**DECISIONE UTENTE — CLASSIFICAZIONE FOLDER: TEMATICA PER DOMINIO**, non per tipo nativo. Motivo: la lista Lexicon **espone già i filtri per tipo** come pulsanti automatici (All | concept | event | item | job | memory | mob | vehicle), quindi folder omonime duplicherebbero un filtro esistente e lascerebbero 58 entry su 108 in un'unica folder. Le 12 folder decise, con la distribuzione attesa:
LSE — Biology & Physiology (9), LSE — Society & Hierarchy (16), LSE — Faith & Mythology (6), LSE — History & Reference (7), Houses & Bloodlines (6), Blackwood City (7), SUCC Campus (8), Digital & Social (6), Species & Races (9), Character Files (15), Items & Vehicles (14), Jobs & Occupations (11).

**BUG DI OVERWRITE — PEGGIORATO E CARATTERIZZATO MEGLIO.** Ha colpito **due volte** in questa sessione, distruggendo `Server` (sovrascritta da `Line Cook`) e `Stage Technician` (sovrascritta da `General Laborer`), entrambe poi ricreate. **Il doppio guard sui campi vuoti NON è sufficiente**, e nemmeno un "reset" navigando su un'altra tab e tornando indietro. Osservato anche un blocco duraturo del pulsante su **"Saving..."** che congela il form e fa scattare i timeout del tool.
**Procedura affidabile stabilita:** dopo ogni Save, **ricaricare l'intera pagina** prima di creare la entry successiva, e spezzare la creazione in **4 chiamate separate** (New+guard / tipo+nome+contenuto+AddJobConfig / config+keywords / Save) per non superare il timeout di 45s. Verificare sempre il contatore N+1 **e** la presenza del nome nella lista enumerata: il contatore da solo non basta, perché un overwrite lascia il totale coerente.

---

## PARTE 16b — Il flusso corretto Blueprint → Lexicon, e il merge delle entry scollegate

**FLUSSO CORRETTO INDICATO DALL'UTENTE (da seguire d'ora in poi).** Le job e le species **non** si creano direttamente nel Lexicon. Si crea prima il **Blueprint** in `RPG → Occupations` (o `Species`), poi si clicca il **bottone libro** sulla riga del blueprint (`title="Create lore entry"`): Wyvern genera la Lexicon corrispondente **e la collega**, con il messaggio `Lore entry "X" created and linked`. La entry generata va poi impostata a **type Job** (per le occupation) o **type Mob** (per le species) e riempita con descrizione e Job Config.

**IL BADGE BLU È IL SEGNALE DI VERIFICA.** Nella lista dei blueprint, accanto al nome compare un badge blu con un numero: è il conteggio delle lore entry collegate. **Nessun badge = nessuna Lexicon collegata.** Il bottone libro resta cliccabile anche quando una entry collegata esiste già, quindi non è lui a dire se serve: va guardato il badge, altrimenti si creano doppioni.

**ERRORE COMMESSO E CORRETTO.** Avevo creato le 5 job di The Verve direttamente nel Lexicon, quindi erano **prive di collegamento** al blueprint. Correzione eseguita: create le 4 Occupation mancanti, cliccato il libro su tutte e 5, **spostato il contenuto lungo e la Job Config nelle entry generate e collegate**, e cancellate le 5 versioni scollegate.

**CONSEGUENZA DA RICORDARE:** i `Jobs Offered Here` di una Location puntano a **ID**, non a nomi. Cancellando le 5 entry originali i riferimenti su **The Verve** sono rimasti **orfani**, visibili come stringhe tipo `_bn4gC61MU4YgyRWfaJMmH` al posto del nome. Sono stati rimossi e riagganciati alle entry corrette. **Regola: se si cancella una Lexicon di tipo Job, controllare sempre le Location che la offrono.**

**EFFETTO COLLATERALE DEL PRIMO CLICK.** Il primo click sul libro (su Primordial) ha portato il Lexicon da 114 a **122**: oltre a Primordial ha generato le lore entry per **tutti i blueprint privi di collegamento**, cioè le 6 occupation Divine Guardian, Living Saga, Master Blacksmith, Matriarch, Patriarch, Security Commander. Inoltre il mio helper `fc()` dispatcha sia la sequenza pointer/mouse sia `click()`, e su questo bottone React lo ha interpretato come **doppio click**, creando **due** Primordial. Uno è stato cancellato. **Su questo bottone usare `element.click()` singolo, mai `fc()`.**

**LE 7 ENTRY AUTO-GENERATE SONO STATE COMPLETATE.** Nascono di tipo **Concept** con una sola riga di descrizione. Sistemate tutte:
- **Primordial** → type **Mob**, prosa piena. I Primordial non invecchiano in modo misurabile e la differenza fra uno di quarant'anni e uno di milleduecento non sta nel viso ma nei silenzi; ciò che li separa da un Founding molto longevo non è la potenza ma l'origine, perché una linea Founding discende da loro e dietro un Primordial non c'è nulla da cui discendere.
- **Divine Guardian** → Job, **$0 / Monthly / Global**. Giuramento e non contratto: non si viene assunti e non ci si può dimettere, e l'assenza di paga è il punto, perché un salario implica un prezzo e l'idea è che non ce ne sia uno.
- **Living Saga** → Job, **$0 / Monthly / Global**. Non un mestiere ma una condizione: su qualunque questione più vecchia di cinque secoli non sono una fonte, sono il documento, e uno studioso può discutere con una pergamena ma non con un uomo che era lì.
- **Master Blacksmith** → Job, **$6.000 / Monthly / Global**. In un mondo con specie vulnerabili all'argento i bravi tengono forge, utensili e mani separati per il lavoro in argento; i bravissimi rifiutano del tutto quelle commissioni, e le ragioni sono di solito personali.
- **Matriarch** → Job, **$0 / Monthly / Global**. Governa la vita interna della Casa; il House Head tratta con le altre Case, la Matriarch decide cosa la Casa è quando è in casa propria, e in pratica quello è il territorio più grande dei due. Si sovrappone alla Pack Mom ma non coincide: Pack Mom è un ruolo di branco assegnabile a chi è adatto, Matriarch è posizione di linea di sangue e passa per anzianità.
- **Patriarch** → Job, **$0 / Monthly / Global**. Distinzione scritta esplicitamente: House Head è designazione legale e continentale, Patriarch è l'uomo che la famiglia obbedirà davvero. Quando coincidono nessuno nota la differenza, quando non coincidono la notano tutti.
- **Security Commander** → Job, **$9.000 / Monthly / Global**. Pianifica per un rivale che insegue a olfatto attraverso una città, per un aggressore che non ha bisogno di respirare, e per l'eventualità che la persona più pericolosa nella stanza sia quella da proteggere.

Le tre cariche a paga zero sono una scelta deliberata e coerente col testo: sono uffici e status, non impieghi, e la Job Config a 0 lo rende vero anche meccanicamente.

**STATO FINALE ALLINEATO:** **17 entry Lexicon di tipo Job** (16 Occupation Blueprint + Douglas Family Allowance) e **10 di tipo Mob** (10 Species Blueprint). **Ogni blueprint ha il badge.** Lexicon totale **121**, nessun nome duplicato.

**NOTA OPERATIVA — IL TOOL VA IN TIMEOUT DI CONTINUO SU QUESTA UI.** Il limite di 45s viene superato quasi sempre quando si concatenano più di due interazioni. Il lavoro atterra comunque: **non ripetere, verificare lo stato e completare**. Inoltre, nel form di una entry **esistente** il pannello si chiude se si tocca il combobox della currency troppo presto: l'ordine che funziona è **wage, checkbox, Pay Period, Scope, e la currency per ultima**.
