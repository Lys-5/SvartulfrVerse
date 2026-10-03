# Modifiche al World: sessione mappe e location — CHIUSA

Compilato il 2026-09-06. **Tutto applicato e verificato dopo reload completo**,
via API dal browser (metodo in `Wyvern_API_Metodo_Scrittura.md`).

Il World è passato da **86 a 114 Location**. **Zero Location orfane.**

---

## A. Location create — FATTO (28)

### Bricklane, il borgo commerciale di Solarton (12 nuove)

| Nome | Cosa è |
|---|---|
| **A&Co.** | La boutique di **Angelo Moreno**. Pronto moda tagliato per ali, code, corna, zoccoli e orecchie. Insegna di tre caratteri e un punto, con **la e commerciale in fucsia**: chi non conosce Angelo non ci legge niente, chi lo conosce legge Angelo and Company. È la vetrina di **Eidolon Creative**, non la sede |
| **Yeti Shack** | Gelati e granite accanto a Medusa. Aperto tardi e a febbraio, quindi punto d'incontro di default |
| **Claws Steel & Ink** | Tatuaggi e piercing. Specializzato in corpi che cambiano: disegni che reggono il partial shift, leghe scelte per specie. Ci lavora **Javier Sinclair** |
| **Directions & Dragons** | Libreria soprannaturale: manuali, mappe, guide sul campo, corde e lanterne. Metà clienti giocano il martedì, metà ci vanno davvero |
| **Flat above Directions & Dragons** | Location figlia. L'appartamento condiviso e disastroso di **Mac** |
| **Kerrigan & Sons Butchers** | Macelleria. Metà banco è per chi non lo cuoce. Tre generazioni di rifiuto scrupoloso di qualunque fornitura non tracciata, che in questa contea è una posizione e non una policy |
| **The Lunar Pharmacy** | Farmacia lunare. Soppressori, argento, sedativi dosati per un metabolismo veloce, integratori ematici. **Resta aperta durante la luna piena**, ed è il servizio più usato |
| **The Long Table** | Caffè da studio. Tavoloni condivisi, presa a ogni posto, silenzio per regola della casa dopo le nove. Le sedie in fondo hanno lo schienale aperto per le ali |
| **Tidewrack Surf & Rental** | Surf e noleggio. Mute tagliate per code e gambe digitigrade, tavole più pesanti dello standard. Non è pubblicizzato, è semplicemente sulla rastrelliera |
| **La Segunda Luna** | Taqueria notturna. Apre alle nove, chiude quando finisce la fila. **È l'ultimo cibo di Solarton**, quindi è dove finisce la notte e dove gente che non condividerebbe un marciapiede finisce nella stessa coda alle due |
| **Suds & Such** | Lavanderia a gettoni. Cestelli maggiorati, due macchine riservate al pelo per cartello scotchato. Aperta tutta la notte e **la bacheca all'ingresso regge metà dell'economia informale della città** |
| **Static & Ink** | Dischi e fumetti, due attività che dividono un pavimento e una cassa e litigano da anni sulla vetrina. Lo scaffale della piccola editoria locale è dove si legge cosa pensa davvero la città di sé |

### La linea del traghetto (4 nuove)

| Nome | Cosa è |
|---|---|
| **Bay Area** | **Non esisteva nel World**, creata come distretto di Solarton perché serviva un genitore allo scalo. Il fronte d'acqua: boardwalk, banchine di lavoro, barche da pesca, due officine e il terminal. È l'unica parte di Solarton che è sveglia presto |
| **Solarton Ferry Terminal** | Capolinea costiero, alla foce dello Yarrow, dentro la Bay Area. Tre corse al giorno d'estate, una d'inverno |
| **Dockside Ferry Landing** | Capolinea di Blackwood, incastrato fra le chiatte da carico. Non è un porto, è traffico fluviale, e la distinzione conta per chi ci lavora |
| **Hex Valley Ferry Stop** | Scalo intermedio sul fondovalle, sotto i vigneti. Un pontile, una campana su un palo, una pista che sale alle tenute. Si carica più roba che gente |

### Fraternity & Sorority Row: le otto case mancanti

ARO, BRO, MAN, ASS, MOO, DOE, FOX, BEE. Ognuna dice la propria posizione sulla
Row e chi ha di fronte, così la geografia non vive solo nei documenti. Residenti
canon citati dove esistono.

**DOE, FOX e BEE restano invenzione dichiarata (§9.4)** e il loro testo lo
rispetta: solo posizione, vicinato e la logica dei nomi animali. Nessuna storia,
nessuna tradizione, nessun residente inventato.

### Campus CUMS (3 nuove)

**Artemis Dorms** (femminile), **Apollo Dorms** (maschile), **Magick Research
Labs**. Nightwine Hall esisteva già. Tutte e quattro ora sotto l'Environment CUMS.

---

## B. Location riscritte — FATTO (9)

| Location | Cosa è cambiato |
|---|---|
| **Bricklane Mall** | Non più centro commerciale: **borgo all'aperto** di edifici bassi indipendenti su una griglia di vicoli in mattoni rossi, due cortili alberati, niente catene |
| **Medusa** | Non più negozio di abbigliamento: **parrucchiere**. Taglia i capelli "whichever part of you they may grow from": criniere, code, piume, il pelo in partial shift. La detoelettura di stagione rende più del taglio |
| **Yarrow River** | Nasce sotto il **tasso sacro**, esce dalla foresta a nord di Seven Hills, scende lungo Blackwood fino a Dockside, sfocia poco a nord di Solarton |
| **Passenger Ferry Solarton Line** | Riscritta con i **tre scali**. Una barca, fondo piatto, un giorno pieno per tratta. È molto più lenta della 101: la si prende per cosa attraversa, ed è l'unico servizio di linea che tocca tre giurisdizioni senza una strada |
| **Bloodmoon Longhouse** | Aggiunti il tasso, l'**enclave di una ventina di capanne norrene** e l'unico accesso dal sentiero di Villa Douglas |
| **Villa Douglas** | Aggiunto il **sentiero sterrato** che sale ai boschi. Blocco `<Villa_Douglas>` intatto |
| **Archer Wolfwood Hall** | Aggiunto il **Dean Archer Wolfwood** e il 2002 |
| **KSA House** | Casa dei Douglas da tre generazioni, Erik ex presidente, Noah presidente, la pressione su Jasper, il precedente di Logan. E la geografia: dalla casa che presiede, **Noah vede la porta di Alyssa** |
| **Basilica Library** | Le **stanze riscaldate per studenti a sangue freddo** |

---

## C. Environment — FATTO. Zero orfane

Assegnate tutte e 14 le Location orfane del piano originale, più tre correzioni
che il piano non prevedeva perché non le avevamo viste.

**Yarrow River → Blackwood Forest.** **Passenger Ferry → Zone di Transito e
Confine**, che è l'unico Environment onesto per una linea che ne attraversa tre.

### Due bug di assegnazione trovati e corretti

Sono lo stesso errore, ripetuto, e nessuno dei due era nel piano.

1. **Fraternity & Sorority Row era assegnata a Hex Valley.** La Row è sul campus
   di Solarton. Se non l'avessi vista, le dieci case sarebbero nate
   nell'Environment dell'università rivale.
2. **Undici Location del campus SUCC erano sotto Hex Valley**: Bulls Stadium, St.
   Neptune Stadium, Wyrm Dormitories, Main Pool, Gym & Changing Facilities,
   Sports Fields, Gallery, Helsing Chapel, Building C e i due parcheggi. Tutte
   spostate su SUCC.

Fra queste ci sono **entrambi gli stadi e il dormitorio di Alyssa, Jasper e
Javier**. Erano nella valle dei vampiri.

**Dopo la correzione, Hex Valley contiene una sola Location: lo scalo del
traghetto.** Che è corretto, perché CUMS ha il proprio Environment.

---

## D. Environment arricchiti — FATTO

**Bloodmoon.** Registro linguistico: *"The Dead Zone"* è il soprannome
colloquiale, non il toponimo. Chi usa il nome per esteso in conversazione o è un
estraneo o sta prendendo le distanze, e si sente.

**CUMS.** Aggiunti origine e registro della rivalità *(2002, "longstanding,
'friendly' rivalry" virgolette comprese)* **più tutti i dati ufficiali**: Clams e
Beavers, V.U.A., 42% almeno in parte vampiro, orario crepuscolare, le quattro
strutture.

**SUCC.** Le lauree, Non-Euclidean Architectural Studies inclusa.

**Solarton: nessuna modifica.** La scarsità di vampiri c'era già. Il piano
chiedeva di aggiungere una cosa già scritta.

---

## Lexicon — FATTO

- **Nuova entry "CUMS Campus & Teams"**, con tutti i dati ufficiali, globale.
- **"Rivalry with CUMS"** aggiornata con l'origine 2002 e i due accoppiamenti:
  Bulls contro Clams, Bears contro Beavers.
- **"Frats & Sororities"** riscritta: prima elencava **cinque** case su dieci.
  Ora ha tutte e dieci, i residenti canon, la disposizione della Row e la riga
  che chiude il conflitto: **non esistono capitoli fuori da Solarton.**

---

## E. Schede personaggio — FATTO

**Javier Sinclair.** "Claw&Steel" ×2 → **"Claws Steel & Ink"**. Corretta anche
"nel centro commerciale di Solarton", diventata falsa quando Bricklane ha smesso
di essere un centro commerciale.

**Sierra.** La scheda diceva *"Applied Necromancy at SUCC's Blackwood City
satellite campus"* e *"RESIDENCE: Theta Iota Theta sorority house, Blackwood
City"*. **Non esiste nessun campus satellite e la TIT è solo a Solarton.**
Corretto in "SUCC, Solarton campus" e "Theta Iota Theta sorority house,
Fraternity & Sorority Row, Solarton". Verificato che "satellite campus" non
compaia più in nessuna scheda, Location o entry Lexicon. **Scarlett Rose non
aveva l'errore**: nella sua scheda Blackwood City è solo la sua origine.

**"quadrapeds": non esiste nel World.** Cercato in tutte le Location e tutte le
schede. Unicorn Hall scrive correttamente "quadrupedi". Il refuso sta
sull'**immagine della mappa del campus**, e va corretto rigenerandola.

**Da fare quando si lavora su Mac:** la sua scheda **non nomina** Directions &
Dragons né l'appartamento. Quel dettaglio vive in un file sorgente, non nella
card. La Location c'è, la riga di residenza va aggiunta.

---

## F. Mappe — FATTO dall'utente

Regionale e Blackwood caricate manualmente. Resta la mappa del campus SUCC, e
quando saranno pronte Solarton, Hex Valley e Bloodmoon Territory.

---

## G. Decisioni: tutte chiuse

1. **Boutique di Angelo: A&Co.**, e commerciale fucsia. Creata.
2. **Negozi: tenuti tutti e sette.** Creati.
3. **Yarrow → Blackwood Forest. Traghetto → tre scali**, Dockside, Hex Valley,
   Bay Area. Creati.
4. **CUMS: dati ufficiali acquisiti.** Inseriti in Environment, Lexicon e quattro
   Location.
5. **KSA: risolta**, è la confraternita di famiglia dei Douglas.
6. **TIT: risolta**, sta solo a SUCC Solarton. Scheda di Sierra corretta.
7. **"Claws": era un mio errore di lettura.** Il portale dice **BULLS vs CLAMS**,
   riverificato alla fonte il 2026-09-06. Non esiste nessuna squadra chiamata
   Claws, e per poco non diventava canon per inerzia. Dettaglio in
   `SUCC_Setting_Canon.md`.

---

## Resta aperto, ma non blocca niente

**KSA House non ha residenti** nelle schede oltre a Noah come presidente, ed è la
casa di fronte alla TIT, quindi quella che Alyssa vede dalla finestra. Si popola
o si decide che è chiusa. È un'occasione, non un buco.

**La V.U.A. di CUMS e la Vampire & Undead Association di SUCC** sono due
organizzazioni distinte con nomi quasi identici, ed entrambe esistono nel World.
Segnalato ovunque serva, ma vale la pena saperlo prima di scrivere una scena in
cui qualcuno dice solo la sigla.
