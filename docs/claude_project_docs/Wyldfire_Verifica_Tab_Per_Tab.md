# Wyldfire desktop: verifica tab per tab del World

Verifica del 2026-09-07, fatta aprendo l'app e guardando ogni scheda, con
riscontro incrociato sul database locale.

**Conclusione: quasi tutto c'è.** Il controllo precedente era stato fatto mentre
l'app stava ancora scaricando: la sincronizzazione si è chiusa alle **00:01**.
Nulla di quello che sembrava "VOID da rifare completamente" va rifatto.

---

## Come funziona davvero il rapporto locale/sito

**Precisazione dell'utente, che corregge un mio allarme eccessivo:** l'app
desktop e il sito sono **due entità separate**. Modificare il locale **non
modifica il sito** finché non si preme **Upload**.

Quindi salvare per sbaglio dentro Wyldfire non danneggia il cloud, e un locale
rovinato si ripara riscaricando. Il rischio non sparisce, però: si **sposta più
avanti**, al momento dell'upload.

### La regola che ne discende, ed è la più importante di tutto il documento

**Una sessione di lavoro sceglie un lato solo.**

- Se si lavora **via API sul sito**, come facciamo per le schede, allora il
  locale va **riscaricato prima** di riaprire l'app, e **non si carica mai** da
  uno stato vecchio: un Upload da un locale disallineato sovrascriverebbe il
  lavoro fatto sul cloud.
- Se si lavora **nell'app**, si finisce il lavoro, si carica, e solo dopo si
  torna a toccare il sito.

Mescolare i due lati nella stessa sessione è l'unico modo realistico di perdere
lavoro in questo sistema.

### Modello operativo scelto: sito padrone, locale replica di lettura

Domanda dell'utente: quale dei due conviene ai miei strumenti. La risposta onesta
e' che i due lati sono bravi in meta' del lavoro ciascuno, quindi la divisione e'
netta e non e' un compromesso.

**Lettura e audit: il database locale, senza confronto.** Una query SQL legge e
incrocia tutti i campi delle 86 schede in pochi secondi. Niente interfaccia,
niente attese di 40-70 secondi per pagina, niente cartelle da espandere, nessuno
dei bug noti. E' cosi' che sono usciti il conteggio delle attitudes, i residenti
delle case greche e i campi vuoti.

**Scrittura: il sito, via API autenticata.** E' il percorso gia' collaudato,
`GET/PUT /api/worlds/characters/<id>` con il token letto dalle richieste
dell'app, con verifica di round-trip. Scrivere direttamente nel database locale
sarebbe tecnicamente possibile ma **sbagliato**: l'app tiene il proprio stato di
sincronizzazione (`synced_at`, `local_modified_at`), il file e' aperto in WAL
mentre lavora, e una modifica alle sue spalle o viene ignorata o confonde il
sync.

**Regola che ne discende: il sito e' il padrone, il locale e' una replica di
sola lettura, e non si carica mai.** Cosi' la divergenza non puo' nemmeno
formarsi: il locale puo' solo essere piu' vecchio, mai piu' recente. Dopo ogni
sessione di scrittura via API si **riscarica** prima di rileggere.

**Punto debole da tenere d'occhio:** la scrittura dipende dall'accesso al sito
dal browser. Il browser interno **rifiuta `app.wyvern.chat`** e l'estensione di
Chrome si e' disconnessa due volte stanotte. Se quel canale non regge, la
scrittura si ferma; la lettura no, perche' passa dal database.

### Due pagine da non salvare in locale, e soprattutto da non caricare

**Relationships.** Il toggle "Enable Relationships" appare **spento**, ma nel
database `relationship_config` dice `enabled: true` e contiene le magnitudes
configurate, Regular 2/12/24 e Severe 6/30/168. La pagina mostra uno stato che
non corrisponde al dato: un salvataggio da lì scrive `enabled: false`, e un
upload successivo lo porterebbe sul sito.

**Travel Routes.** Due rotte con From e To vuoti. Nel database le rotte hanno gli
id delle location come **platform id**, e l'app non riesce a risolverli sui
propri id locali. Un salvataggio scriverebbe due rotte senza origine né
destinazione.

Entrambe vanno segnalate a Wyvern insieme agli altri bug.

---

## SETTINGS

**World Info: completo.** Nome, avatar, background, descrizione da 3231
caratteri, rating Explicit, creato 26/08, aggiornato 07/09. Unico vuoto: la
**tagline**, che è un campo facoltativo mai compilato.

**Simulation: parziale, e l'utente aveva ragione.**

- World Features corretti: Inventory, Currency, RPG Stats, Combat, Cross-World
  Ships e Party Stats attivi, Creature Catcher spento.
- About Your World: testo completo.
- World Time Span **10950000**, cioè 1250 anni documentati. Timeline Start
  1 gennaio 800, fine storia registrata 3 marzo 2049.
- **Start Date: vuoto.** È la mappatura sul calendario reale, facoltativa.
- **System Prompt Override: vuoto.**
- **Writing Style & Tone: vuoto.** Confermato, ed è da scrivere: presente, terza
  persona, asterischi solo per i pensieri, backtick per i testi scritti,
  virgolette per i dialoghi.

**Linked Characters:** nessuno, come atteso.

---

## SYSTEMS

**Economy: popolata.** US Dollar configurato, inventario gestito dall'AI attivo,
e **quattro marketplace**: Administration, Dockside, Medusa, The Verve.
**Tutti e quattro hanno zero listing**, quindi esistono ma sono vuoti.

**Travel Routes:** due rotte presenti ma illeggibili, vedi avvertenza sopra.

**Stat Definitions: completo, niente da rifare.** Might/MGT, Resilience/RES,
Agility/AGI, Wits/WIT, Presence/PRS, Scent/SCT, tutte abilitate. Allocazione
Point Buy, **budget 25**, base 1, massimo 10, vitali **Condition** e **Control**.
È esattamente la convenzione di progetto (§8).

**Combat:** la pagina mostra Narrative Tiers con DC base 10, crit margin 10, HP
base 50 e MP base 20. Ma nel database `combat_ruleset` è **vuoto**: quelli sono i
**valori di default** proposti dall'interfaccia, non una configurazione salvata.
Non è andato perso niente, semplicemente non è mai stato personalizzato.

**Species, Occupations, Traits: davvero vuoti.** "No species yet", "No
occupations yet", "No traits yet". Per Species e Occupation è il bug di
piattaforma già noto (§15), che li fa sparire anche sul web. I Traits non li
abbiamo mai creati.

**InfoBoard: popolato.** Categorie, chiavi e custom prompt override attivo.

---

## VISUAL & NARRATIVE

**Maps: già aggiornate.** La mappa di Blackwood caricata è **la nuova versione
blu e oro**, non la vecchia. Ha 0 pin e 0 rotte.

**Eras: complete.** Tutte e sette con date e descrizioni: Age of Myth, Age of the
Firstborn, Age of Expansion, Age of Houses, Age of Kingdoms, Age of Secrecy,
Modern Era.

**Relationship Trees:** nessuno, come atteso.

**Timeline Events:** funzione nuova, vuota.

**Gallery: zero immagini.** Da capire se è vuota anche sul sito.

**Pages:** funzione nuova, marcata SOON.

---

## CONTENT

Verificato contro il sito e coincidente: **324 elementi totali**, 86 Characters,
138 Lexicon, 13 Environments, 86 Locations, 1 Scenario, 2 Maps, 7 Eras.

Sulla scheda campione, Andrew Campbell, è presente tutto: Start Position
10538088, birthdate −191280 con la data leggibile, pronomi, cinque outfit, cinque
Dialogue Examples, cinque Attitudes, RPG a **Lv.22**.

**I due veri buchi sulle schede:**

1. **~~Global Character spento su 85 schede su 86~~. FALSO ALLARME, e va letto
   al contrario.** Interrogando il sito con il token, `is_global` risulta **true
   su tutte e 86 le schede**. Sul cloud è già a posto. È il **database locale**
   ad avere il campo sbagliato, 1 su 86, e l'app mostra quel valore.

   **Questo è un bug di sincronizzazione vero e potenzialmente distruttivo:**
   l'app scarica `is_global` sbagliato, quindi se si modificasse una scheda
   nell'app e poi si premesse Upload, si spegnerebbe Global Character su 85
   personaggi del sito. Va segnalato a Wyvern come priorità, ed è la ragione più
   forte per la regola "il sito è il padrone, dal locale non si carica mai".
2. **Default Outfit non impostato.** L'app avvisa "Please select a default
   outfit". Da controllare sulle 39 schede che hanno outfit.

Il campo **Pronoun Set** in cima alla scheda mostra "Select pronoun set" e sembra
vuoto, ma i pronomi correnti sono elencati subito sotto. È un preset non
selezionato, non un dato mancante: è il falso allarme più facile da prendere.

---

## Cosa fare, in ordine

1. **Non salvare, e soprattutto non caricare**, dalle pagine Relationships e
   Travel Routes finché il bug non è chiarito.
0. **Regola di sessione:** si lavora su un lato solo, sito o app, mai su
   entrambi. Prima di riaprire l'app dopo un lavoro via API, riscaricare.
2. ~~Accendere Global Character su tutte le schede~~. **Non serve: sul sito è
   già acceso su tutte e 86.**
3. **Scrivere Writing Style & Tone** in Simulation.
4. Decidere se popolare i quattro marketplace e se rifare le due rotte di
   viaggio con origine e destinazione corrette.
5. Impostare il **default outfit** dove manca.
