# Istruzioni di Workflow — Character Card Wyvern (Svartúlfr | Blackwood-Douglas)

Queste istruzioni codificano il processo di lavoro stabilito per la creazione e l'aggiornamento delle character card su Wyvern per questo progetto. Vanno seguite per ogni personaggio.

---

## 1. Formato di consegna: testo, non JSON

**Default:** fornire testo pronto da incollare nei campi del form dell'interfaccia Wyvern (description, personality, first_mes, mes_example, system_prompt, post_history_instructions, lorebook/NPC entries, outfit, tagline, shared info, ecc.), **non** file JSON completi.

Il JSON va generato solo se:
- l'utente lo chiede esplicitamente, oppure
- serve come riferimento per verificare coerenza tra più campi complessi (in quel caso, chiedere se preferisce il file o solo il riepilogo testuale).

Il file JSON scaricato dall'utente **dopo** il salvataggio su Wyvern è il backup di archivio, non un artefatto che Claude deve mantenere sincronizzato in parallelo.

**Eccezione operativa:** quando Claude scrive direttamente sul World via API (§11), il testo non passa dalla chat. In quel caso si consegna il *riepilogo* di cosa è stato scritto e dove, non il testo integrale.

---

## 2. JED+ come formato standard delle schede

Tutte le character card usano il formato **JED+**: un blocco di attributi tra parentesi quadre, separati da punto e virgola (stile bracket/PList), seguito da sezioni in prosa per backstory, dinamiche familiari, voce/comportamento e temi centrali del personaggio.

```
[NAME: ...; SPECIES: ...; AGE: ...; HEIGHT: ...; ... ]

BACKSTORY: ...

FAMILY & PACK: ...

VOICE & BEHAVIOR: ...

[sezione tematica finale, es. CORE TRAGEDY / THE WEIGHT HE CARRIES / THE SECRET HE CARRIES]
```

Il campo `personality` (`summary` nell'interfaccia) usa invece un blocco compatto di soli tratti tra parentesi quadre (stile PList puro), come riepilogo rapido separato dalla description estesa.

**Nota:** una card importata grezza, con il blocco `<nome_personaggio>` della fonte incollato tale e quale, **non è una scheda lavorata**. Va riscritta in JED+, non ritoccata.

**Età: usare la macro `{{age}}`** nel campo AGE del blocco JED+ di ogni personaggio che ha una data di nascita, invece del numero scritto in chiaro. Il numero scritto a mano invecchia male e va corretto a ogni avanzamento del World. `summary` e `display_description` per ora tengono l'età in chiaro per convenzione, ma è una coda aperta.

---

## 3. Disciplina di formattazione per dialoghi ed esempi

Applicare sempre a `first_mes`, `mes_example`, `alternate_greetings`, Dialogue Examples e qualunque testo di esempio in-character:

- **Mai usare l'em-dash (—).** Usare virgole o punti al suo posto.
- Dialogo tra virgolette (`"..."`).
- Azioni e narrazione in **testo semplice**, senza asterischi.
- Gli asterischi sono riservati **esclusivamente** ai pensieri interni del personaggio (uso attualmente non ancora sfruttato, disponibile per sviluppi futuri).
- Lingue straniere: `"Frase originale"` seguita da `([traduzione])`.
- **Niente markdown dentro i testi del World.** Il grassetto con `**` viola la regola sugli asterischi: vale anche nelle entry Lexicon e nelle description di Location ed Environment, non solo nei dialoghi.

Questa regola va anche scritta esplicitamente in coda a `post_history_instructions` di ogni card, così vale durante la chat vera e non solo negli esempi:

> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."

---

## 4. Evitare oggetti/tratti "sempre visibili"

Lezione imparata da test reali (bende di Malachia, tatuaggi di Logan, catena/anello/occhiali di Erik): qualunque accessorio scritto come "always on" o "never removed" nella description tende a far loopare il modello, che lo inserisce anche in scene dove non avrebbe senso (piscina, cena formale, ecc.).

**Regola:** se un elemento visivo/accessorio non è strutturalmente parte del corpo del personaggio, non scriverlo come costante. Due opzioni, in ordine di preferenza:

1. **Usare il sistema Outfit nativo di Wyvern** (Appearance & Outfits), con outfit distinti per contesto (Allenamento, Casa/Casual, Formale, ecc.), è la soluzione corretta lato piattaforma.
2. Se il sistema Outfit non è ancora popolato per quel personaggio, scrivere il tratto come **contestuale** nella description ("X indossa Y solo quando Z; in altri contesti non è visibile") invece che costante.

**Eccezione ammessa:** un tratto può restare costante se la sua costanza *è* il personaggio e la scheda lo dice esplicitamente. Il cappuccio di Dullahan non scende mai, in nessun contesto, e questo è il punto centrale di chi è. In quel caso va scritto come costante e ribadito negli outfit, non aggirato.

---

## 5. Coerenza visiva di famiglia (Douglas)

Scelta stilistica deliberata confermata dall'utente: i maschi Douglas condividono un "family look" riconoscibile nelle immagini generate, cioè capelli scuri lunghi e arruffati (per accomodare le orecchie da lupo del Partial Shift), stessa palette calda al tramonto e palme di Blackwood City, struttura del viso simile. Tenerne conto quando si valutano nuove immagini o si scrivono i campi `visual_description`/Shared Info per nuovi personaggi maschi della famiglia, pur mantenendo elementi distintivi propri di ciascuno (stile dei tatuaggi, accessori, colore occhi).

**I demi-umani hanno un solo paio di orecchie**, quelle animali, non due. Confermato dall'autore dell'ambientazione originale, che aggiunge che i generatori di immagini sbagliano quasi sempre su questo. Va controllato su ogni immagine.

---

## 6. World Clock  *(CORRETTA — l'epoca precedente era sbagliata)*

- **World-age 0 = 21 dicembre 827 d.C., ore 00:00 UTC.** Il valore è letto direttamente dal World (`human_start_date: 0827-12-21T00:00:00.000Z`, `calendar.start_year: 827`, `start_month_id: dec`, `start_day_of_month: 21`).
- **La vecchia indicazione "1 gennaio 800" era sbagliata** e produce date sfasate di quasi ventotto anni. Se una Start Position sembra assurda, la prima cosa da sospettare è che sia stata calcolata con la vecchia epoca.
- Le ore assolute si calcolano con calendario gregoriano proletico standard: `ore = giorni_trascorsi × 24 + ora_del_giorno`.
- **L'anno corrente del World è il 2024.** `world_age` vale **10486470**, cioè **5 aprile 2024, ore 06:00**. Qualunque riferimento al 2022 nelle fonti è residuo di vecchi setting e va ignorato.

**Come verificare senza sbagliare**, in una riga di JavaScript:

```js
EP = Date.UTC(827,11,21);
data = h => new Date(EP + h*3600000).toISOString().slice(0,10);
ore  = iso => (Date.parse(iso) - EP) / 3600000;
```

Un controllo di sanità che vale sempre: `birthdate` e `start_timeline_position` di un personaggio vivo devono coincidere, e nessuna delle due può essere maggiore di `world_age`.

---

## 7. Triage import Lorebook Entries → World  *(REVISIONATA)*

**I personaggi deceduti non vanno più in Lexicon.** La vecchia regola nasceva dal non poter esprimere un arco temporale di presenza. Ora Wyvern lo permette, quindi:

- **Personaggi vivi** → Character, con **Start Position**.
- **Personaggi deceduti** → Character, con **Start Position e End Position** (modello: Nixara).

**La Start Position va sempre messa, senza eccezioni**, anche per un personaggio contemporaneo che sembra non averne bisogno. Sono già previsti tre scenari fuori tempo: il viaggio di Wulfnic, uno scenario piratesco per Cornelius, e uno futuristico ambientato nel **2499**. Senza Start Position un personaggio del 2024 comparirebbe anche a bordo della nave di Wulfnic.

**La End Position sui personaggi vivi si metterà quando lo scenario futuristico verrà costruito**, non prima. In quel momento andrà decisa caso per caso, tenendo conto che per Jasper, Noah e Malachia il fine vita è ulteriormente rallentato da impianti cibernetici pesanti (nelle schede bozza del futuro la specie è scritta **Cyber-Werewolf**).

| Tipo di entry | Azione |
|---|---|
| Species_Details / Intimacy Profile del personaggio proprietario | **Non importare** (già parte della card collegata) |
| Personaggio vivo, ricorrente in più schede (es. Magnus, Elizabeth, Kaladin) | Importa **una sola volta** come Character con Start Position; riusa e linka nelle altre schede, non duplicare |
| Personaggio deceduto (es. Nixara) | Importa come **Character** con Start **e** End Position |
| Luogo già creato manualmente come Location (es. The Verve) | **Non importare** la versione lorebook equivalente, è un doppione |
| Attività o concetto senza posizione fisica mappata (es. underground fighting ring) | Importa come **Lexicon** |
| Luogo fisico non ancora mappato | Importa come **Location** |
| Gruppo di personaggi off-world che nessuno incontrerà a breve | Accorpa in **una sola entry Lexicon** ricca (es. "The Other Contractors"), scorporabile in Character singole solo se uno entra davvero in scena |

**Placement:** tutti i Character vanno impostati come **Global Character = ON**. Popolare i Character Pool di Location ed Environment si è rivelato inutile, perché in pratica andavano inseriti quasi tutti ovunque, e appesantiva gli Environment senza guadagno.

**Attivazione delle entry Lexicon.** `is_global: false` non restringe una entry: la **spegne**, togliendola del tutto dalla scansione a parole chiave del mondo. Diventa idonea solo se inclusa nella `included_lexicon_entries` di una Location, di un Environment o di uno Scenario, e anche allora serve comunque una chiave che matcha oppure `constant: true`. Il campo `attached_world_character_id` **non è un canale di attivazione**. Per restringere una entry ai contesti giusti si usano:

- `keys` + `secondary_keys` + `key_logic`, con la forma corretta **primarie = identificatori della persona, secondarie = parole dell'argomento**. Chiavi generiche come `intimacy` o `werewolf` messe fra le primarie con `key_logic: AND_ANY` fanno sparare la entry in continuazione.
- `party_conditions`, cioè il filtro su chi è nel party. È lo strumento giusto per i contenuti personali: un Intimacy Profile con `has_any [proprietario]` esiste solo nelle scene in cui quella persona c'è davvero.

Il macro `{{lexiconEntryNames}}` elenca le entry **candidate** per la scena, non quelle che hanno effettivamente matchato una chiave. Serve a diagnosticare una entry spenta, non a validare un filtro.

---

## 8. RPG Stats

**Convenzioni del progetto:**
- Budget punti fisso a **25**, indipendentemente dal Livello. Con base 1 su sei stat, i valori finali sommano sempre a **31**.
- **Livello = età anagrafica**, con il tetto sotto.
- Stat: MGT (Might), RES (Resilience), AGI (Agility), WIT (Wits), PRS (Presence), SCT (Scent).

**Tetto di piattaforma al Livello (bug confermato):** un Livello di **300 fa fallire in silenzio il salvataggio dell'intero blocco RPG**. Nessun errore visibile, il pulsante Save resta appeso su "Saving...", e dopo il reload le RPG Stats risultano di nuovo disabilitate con stat e livello persi. Nello stesso identico save description, outfit, start position e toggle si salvano regolarmente, quindi sembra tutto a posto finché non si riapre la scheda. Livello **99 salva e persiste**, verificato. Il tetto esatto sta fra 100 e 299, non isolato.

**Convenzione conseguente per i longevi:** per chiunque superi il secolo (Zefir, Ut, Wulfnic, Cornelius, Archer, Magnus, Dullahan) usare **Livello 99** e tenere l'età reale nel blocco JED+. La convenzione "Livello = età" vale solo fino a 99.

**Species e Occupation fanno parte del blocco RPG**, e si impostano solo via API (§11 e §15). Vanno messe su ogni scheda che ha le RPG Stats abilitate: il modificatore di specie viene applicato davvero alle stat, quindi lasciarle vuote non è neutro.

**Formula Condition/Control: da riverificare, non affidabile.** La formula registrata in precedenza (`Condition = 67 + 2×(liv−1)`, `Control = 30 + 1×(liv−1)`, da Erik, Logan e Malachia) **non si è riprodotta**: su Dullahan, a Lv.1 con tutte le stat a 1, i valori base erano **56 e 46**, non 67 e 30. Va rifatto un test pulito prima di trattarla come acquisita. Probabile che il pool dipenda anche dalla distribuzione delle stat, e ora sappiamo che **dipende anche dalla specie**, visto che assegnarla cambia i valori.

---

## 9. Gestione discrepanze nei documenti sorgente

Quando le fonti si contraddicono su un dettaglio (altezza, età, tatuaggio, profumo, ruolo in squadra, ecc.):

1. Usare il valore con **maggiore consenso tra le fonti** (es. 2 file su 3 concordi), e a parità di consenso la fonte più forte secondo la scala di §11.
2. Segnalarlo sempre in `creator_notes` della card, con la discrepanza esatta trovata, così resta tracciabile per una futura pulizia dei sorgenti.
3. Non correggere i file sorgente originali senza autorizzazione esplicita dell'utente.
4. **Non inventare mai per riempire un buco.** Se una fonte tace su un dettaglio, o lo si lascia fuori, o lo si segnala come invenzione dichiarata. Una scheda scritta a intuito prima che arrivino le fonti va **riscritta da zero** quando arrivano, non ritoccata: è già successo con Barkley Rover, dove erano sbagliati età, altezza, aspetto, anni di servizio, famiglia e soprattutto il carattere.
5. **Un dettaglio letto una volta e riportato in un documento acquista un'autorità che non ha.** Prima di costruirci sopra, va riverificato alla fonte. È già successo con "Bulls vs Claws", che era una lettura sbagliata di "Bulls vs CLAMS" e per poco non diventava canon per inerzia.
6. **Quando si inventano date** (compleanni, morti, eventi), non usare sempre il 1° gennaio o il 1° del mese. Scegliere date varie e credibili.

---

## 10. Precedenza di lore fra ambientazioni

Il progetto unisce ambientazioni indipendenti scritte da autori diversi:

| Ambientazione | Autore | Dominio |
|---|---|---|
| **Underworld** | esterno | Los Angeles |
| **SUCC / Modern Fantasy** | esterno (io wuvs soap) | Solarton, campus SUCC, Hex Valley, CUMS |
| **Blackwood / Douglas** | Lys | Blackwood City, famiglia e branco Douglas |
| **DDM Inc.** | esterno (io wuvs soap) | Voidspace, un altro universo |

**La precedenza si applica per dominio, non per ambientazione.** Ogni ambientazione è l'autorità sul proprio dominio e non ha voce su quello altrui. In caso di conflitto prevale sempre il materiale ufficiale dell'ambientazione a cui il dominio appartiene, anche contro materiale Blackwood/Douglas.

**DDM Inc. è un caso diverso dagli altri due esterni.** Underworld e SUCC sono *luoghi dentro la California*: confinano con Blackwood, e un conflitto fra loro riguarda chi comanda su una certa zona. DDM invece non è un posto della California, è un universo separato che tocca questo mondo attraverso una sola persona. Quindi:

- Sul **proprio dominio** (meccanica dei Contratti, Original Death, ACES, ARC Level, SERAPHIM, struttura e dipartimenti della Company, reality tears) prevale sempre il materiale DDM.
- Sul **suolo della California** DDM non ha alcuna autorità. Come funzionano i soprannaturali, lo status civile, la SRF, le specie locali, la società di Blackwood e Solarton: decide il materiale locale. **ARC Level, per esempio, non è conosciuto né usato da nessuno a Blackwood o Solarton, e non ha alcun rapporto con le classificazioni locali.**
- **Nessun personaggio locale conosce il vocabolario DDM** se non gliel'ha detto Dullahan. Contractor, ACE, The Cause, Voidspace non sono parole che circolano al campus.
- Dullahan è un corpo estraneo consapevole: usa le regole locali quando è Coach D, le proprie quando è #04.

**Gli adattamenti vanno registrati, non nascosti.** Quando Blackwood si discosta dal canon originale, la cosa va scritta in un documento del Project con la forma "cosa dice la fonte, cosa facciamo noi, perché non è una contraddizione". Il caso più profondo è la longevità dei licantropi (§12): non abbiamo scavalcato il canon originale, gli abbiamo dato il dominio che gli compete, cioè il licantropo comune, e abbiamo tenuto Blackwood dove Blackwood serve, cioè sulle Case e sui Firstborn.

**L'autore dell'ambientazione SUCC ha dichiarato esplicitamente** che *"the rules for modfan are literally… i dont have any rules for myself when it comes to it"*, e ha dato via libera a fan OC, immagini generate e uso dei personaggi canon come comparse. Adattare non è uno strappo, è l'uso previsto. Resta l'obbligo di accreditare quando si copia testo alla lettera.

---

## 11. Fonti, accesso al web e scrittura sul World  *(RISCRITTA)*

### Regola di accesso

**Non usare mai il fetch diretto delle pagine.** Ogni consultazione web passa dal **browser locale**, aprendo la pagina in una scheda e leggendola da lì. Vale per la wiki, per Discord e per qualunque altra fonte.

### Le fonti dell'ambientazione originale, in ordine di forza

1. **I lorebook ufficiali** pubblicati dall'autore su Discord, server *io's bot hub*, canale `lorebooks-and-cards`, post **IOVERSE LOREBOOKS**: `SUCC_-_U_-_VERSE.json`, `Dead_Dog_Motel.json`, `Starfall_1.0.json`, `Post-Apocalyptic_2.0.json`. Sono testo scritto e distribuito dall'autore come materiale di riferimento.
2. **Le risposte dell'autore** (`io wuvs soap`) nei thread del canale forum `ioverse-q-n-a`. Stesso livello dei lorebook: è l'autore che risponde, non un riassunto. Il modo efficiente di leggerli è la ricerca Discord con i filtri `da:` autore e `in:` canale, che isola le risposte dal rumore delle domande.
3. **Il portale ufficiale SUCC** (`io-succ.uwu.ai`).
4. **La wiki Fandom** e il resto del materiale di terzi.

Nota: i thread **ASTRAL IMPERIUM Q&A**, **THE EDGE Q&A** e **GENERAL IOVERSE QUESTIONS** sono praticamente vuoti, solo placeholder e indici. Non vale la pena rileggerli. Il canale `succ-and-modern-fantasy` è chiacchiera di community sugli OC dei fan, non canon.

### Documentazione di piattaforma

- **WyvernWiki**: `https://wiki.wyvern.chat/`
- **r/WyvernChat**: `https://www.reddit.com/r/WyvernChat`, community e workaround non documentati ufficialmente. Le ricerche mirate danno risultati rumorosi, affinare i termini caso per caso.
- **Discord WyvernChat**, canale forum `bugs-and-support` per i bug del sito, `wyldfire-bugs-and-support` per quelli dell'app desktop. Il post fissato *HOW TO REPORT ISSUES* contiene il template da usare per ogni segnalazione. **Prima di aprire un bug si cerca se esiste già**, con `in:bugs-and-support <termine>`.

**Priorità delle fonti di piattaforma in caso di conflitto**, dalla più forte alla più debole:
1. Un comportamento osservato e verificato dopo reload completo in questa conversazione.
2. Un export reale scaricato da Wyvern dopo un salvataggio.
3. WyvernWiki.
4. Reddit e Discord.

### Scrivere sul World via API dal browser

Un `fetch` scritto a mano senza header di autenticazione restituisce `[]` oppure 401/403, e **una risposta vuota così non è la prova che i dati siano spariti**. Con l'header giusto invece l'API funziona, ed è enormemente più veloce e più affidabile del pilotare l'interfaccia a click.

- **Il token va rinfrescato, non letto.** Quello in IndexedDB scade dopo un'ora e resta lì scaduto: usarlo produce **404 sulle GET e 401 sulle PUT**, quindi sembra che la route sia sbagliata mentre è solo scaduta. Si legge il refresh token dalla riga `firebase:authUser:<apikey>:[DEFAULT]` di `firebaseLocalStorageDb` e si chiede a `securetoken.googleapis.com` un access token nuovo. Va rifatto dopo ogni reload di pagina e ogni ora.
- **Le route** hanno uno schema uniforme per ogni risorsa (`characters`, `locations`, `environments`, `lexicon`, `scenarios`): lista `GET /api/worlds/<risorsa>/world/<world_id>`, singolo `GET /api/worlds/<risorsa>/<id>`, crea `POST /api/worlds/<risorsa>` col `world_id` nel body, modifica `PUT /api/worlds/<risorsa>/<id>`, elimina `DELETE`. Su un Character il campo lungo è `long_summary` e il nome è `display_name`, non `name`.
- **Due route non seguono lo schema:** `GET /api/worlds/rpg/species/<world_id>` e `GET /api/worlds/rpg/occupations/<world_id>` per i blueprint RPG del World.
- **La trappola grossa: il PUT vuole un body parziale.** Un PUT con l'oggetto completo risponde 200 e non scrive niente. Si mandano solo i campi che cambiano.
- **Attenzione ai campi annidati.** `species_id` e `occupation_id` **non** sono campi di primo livello del Character: vivono dentro `rpg_stats`. Mandati al primo livello il PUT risponde 200 e li scarta in silenzio. Si legge `rpg_stats`, lo si estende e si rimanda solo quello. È lo stesso modo di fallire del PUT completo: **lo status 200 non è una prova**.
- **Per appendere testo** si legge il campo, si concatena in JavaScript e si rimanda solo quel campo. Non si ridigita mai a mano il testo esistente.
- **Non usare `/api/worlds/characters?world_id=`**: ignora il parametro e restituisce oltre 1500 personaggi da tutti i World pubblici.
- **Anche via API vale §14.11:** si verifica dopo un reload completo, rileggendo dalle liste del World. È la verifica a dirlo, non lo status 200.

---

## 12. Invecchiamento, longevità e filone SciFi  *(REVISIONATA)*

### Founding Bloodline e Divine Blood

Le varianti "SciFi" trovate nei documenti legacy (Erik su una città-nave, Logan nell'Undertrade, Malachia "Vanguard Commander", ecc.) **non sono rumore da scartare**: sono un filone narrativo futuro non ancora sviluppato, reso plausibile dalla quasi-immortalità di questi personaggi.

- Crescita completa raggiunta intorno ai 21 anni, dopo di che l'invecchiamento rallenta fino a fermarsi quasi del tutto. I personaggi Founding/Divine Blood adulti sono sostanzialmente fermi salvo diversa indicazione.
- Sangue Founding: Malachia, Noah, Jasper, Alyssa. Divine Blood: Wulfnic, Ut, Zefir.
- **Il Divine Blood non rallenta, si è fermato.** I Firstborn portano l'età che avevano nel momento in cui Fenris li ha presi. **Wulfnic e Ut** erano guerrieri adulti e portano la faccia di un quarantenne *del loro secolo*, che un occhio moderno archivia intorno ai sessanta.
- **Zefir ha 1019 anni**, non 1200 come diceva la versione precedente di questa regola (nato il 5 febbraio 1005). È il più giovane dei Nove e l'unico preso prima della fine della crescita, quindi dimostra ancora diciotto o diciannove anni. Era però **maggiorenne per legge norrena**: non era un bambino secondo il proprio secolo, era un adulto dell'XI secolo che il XXI secolo non riesce a vedere come tale.

### Common Bloodline: non rientrano in questa meccanica

Vivono **60-80 anni**, pari o poco sotto la media umana, e invecchiano cronologicamente come un umano. È il canon dell'autore originale (*"about the same, actually maybe slightly less then average human lifespan"*, più la spiegazione del *"hot blooded, burning out sooner"* e delle morti per conflitto), e vale per la stragrande maggioranza dei licantropi che si incontrano a Solarton e a Blackwood.

Invecchiano però **visibilmente** molto più lentamente: crescita normale fino a 25 anni, poi circa **un anno di aspetto ogni cinque vissuti** (un Common di 50 dimostra 30, uno di 70 poco più di 34), con un cedimento rapido negli ultimi anni di vita. Il collasso finale è esattamente il "burning out" visto dall'altro lato: tengono la forma del proprio prime quasi fino alla fine, e poi bruciano.

La fertilità dei Common cala **dai 35 anni**, non dai 50.

### La conseguenza che conta scrivendo

**L'aspetto non dice niente sulla classificazione del sangue**, a nessuno dei due capi della scala. Un Common dimostra vent'anni meno di quelli che ha, un Firstborn mille. Chi dimostra trent'anni può essere un Common di cinquanta con quindici anni davanti, un Pureblood di duecento o uno dei Nove. **Nessun personaggio può dedurre il sangue di un altro guardandolo.** L'età si legge dal portamento, dall'odore e da cosa uno ha vissuto, mai dalla faccia. I Common si leggono bene fra loro; umani ed estranei sbagliano in entrambe le direzioni, e di solito per difetto.

Sulle schede di personaggi Common adulti l'aspetto va scritto sull'**età apparente**, non su quella anagrafica, e la scheda dovrebbe dirlo.

---

## 13. Epurazione di `{{user}}` dal materiale importato  *(REVISIONATA — regola vincolante)*

**`{{user}}` va tolto ovunque, senza sostituirlo con un nome.** In questo World `{{user}}` non è una persona fissa: è Alyssa Douglas solo in alcuni scenari, in altri può essere la fidanzata di Jasper, o Jasper stesso, o altro ancora. Qualunque relazione scritta su `{{user}}` verrebbe quindi applicata a chiunque stia giocando, e in molti casi punterebbe contenuto romantico o sessuale di un personaggio adulto verso una matricola di diciannove anni.

**Procedura obbligatoria su ogni import:**

1. **Generalizzare il ruolo, mai nominare un personaggio del World.** "{{user}}, l'allenatrice di cheerleading" diventa "chiunque gestisca il programma di cheerleading in una data stagione".
2. **Rimuovere integralmente cotte, relazioni e tensione sessuale rivolte a `{{user}}`** quando il personaggio è adulto e il giocatore sarebbe uno studente, e a maggior ragione quando è staff. Non attenuare: rimuovere. Il buco narrativo si riempie con altro materiale del personaggio.
3. **Non trascrivere i blocchi anatomici e di kink espliciti** nella description. Se servono, vanno come Intimacy Profile separato secondo il triage §7, con `party_conditions` sul proprietario. Nella description resta al massimo una riga sobria e non grafica.
4. **Aggiungere, dove il personaggio ha autorità su studenti**, una riga esplicita sul suo rapporto con loro, che chiuda la porta invece di lasciarla socchiusa.
5. **Non usare "The Player (Persona)" nelle Attitudes per rapporti specifici di una persona** (§16). Punta a chiunque stia giocando, quindi è lo stesso errore di `{{user}}` in un altro campo.
6. **Verificare a fine lavorazione** che la stringa `{{user}}` non compaia più in nessun campo della card.
7. **Documentare in `creator_notes`** cosa è stato rimosso e perché.

Casi già trattati con questa regola: Dullahan (allenatrice di cheerleading con "unbearable sexual tension"), Barkley Rover (cotta in una variante, fidanzato nell'altra), Richard Loewe (riga sugli impulsi verso `{{user}}`, trasformata nella sezione THE LINE senza destinatario).

---

## 14. Pipeline standard di una card

Ordine di lavorazione, da seguire per ogni personaggio. Ogni passo si verifica prima di procedere.

1. **Raccogliere tutte le fonti prima di scrivere.** Varianti multiple, file di lore, lorebook ufficiali (§11), risposte dell'autore, entry Lexicon esistenti, agganci già scritti in altre schede. Non iniziare la scheda con materiale parziale (§9.4).
2. **Controllare se il personaggio esiste già** nel World, espandendo la cartella. Molti sono presenti come import grezzi o segnaposto vuoti: vanno riempiti, non ricreati, per non generare duplicati.
3. **Epurare `{{user}}`** secondo §13.
4. **Scrivere i campi:**
   - `long_summary` in JED+ (§2), con `{{age}}` nel campo AGE
   - `summary` come blocco PList di soli tratti
   - `display_description`, una o due righe che dicano chi è e cosa lo rende interessante
   - nickname, titoli, keys, pronomi
5. **Outfit: cinque, contestuali** (§4). Dall'interfaccia vanno aggiunti **uno alla volta con un salvataggio ciascuno**, altrimenti si sovrascrivono. Almeno uno dovrebbe dire qualcosa che la prosa non dice.
6. **Default Outfit**, da scegliere fra i cinque. L'interfaccia lo segna come *Required* e senza di esso il modello improvvisa l'abbigliamento in ogni scena che non attiva un outfit contestuale. Si sceglie quello che il personaggio indossa quando non sta facendo niente di particolare, non il più bello.
7. **Start Position** calcolata dal World Clock (§6), sempre. End Position solo se deceduto (§7).
8. **RPG Stats** (§8): abilitare, distribuire i 25 punti, impostare il Livello, e assegnare **Species e Occupation** via API dentro `rpg_stats` (§11), perché dall'interfaccia non si salvano.
9. **Dialogue Examples: cinque**, con la disciplina di formattazione di §3. Almeno uno dovrebbe mostrare il personaggio nel suo momento peggiore o più esposto.
10. **Attitudes** secondo §16.
11. **Global Character = ON.**
12. **Verifica finale dopo reload completo della pagina**, non dopo il salvataggio: zero `{{user}}`, zero em-dash, zero asterischi, tutti i campi ancora presenti, RPG ancora abilitato, Default Outfit impostato. **Un salvataggio che sembra riuscito non è una prova.**
13. **Documentare nel Project** le decisioni di scrittura, gli agganci creati e le discrepanze trovate.

---

## 15. Bug e trappole note della piattaforma

Da tenere presenti durante la lavorazione.

| Problema | Comportamento | Come conviverci |
|---|---|---|
| **Save appeso** | Il pulsante resta su "Saving..." molto spesso | Il contenuto di solito si salva comunque. Ricaricare la pagina e verificare, non ripetere il salvataggio alla cieca |
| **Species / Occupation non si salvano dall'interfaccia** | Impostati dai due combobox e salvati, dopo il reload tornano a None. **Non è un problema del modello dati:** i due campi vivono dentro `rpg_stats` e scritti lì via API persistono, sopravvivono al reload, compaiono nell'interfaccia e applicano davvero i modificatori di specie alle stat. Il difetto è nel percorso di salvataggio dell'interfaccia, che non li manda | **Scriverli via API dentro `rpg_stats`** (§11). Non lasciarli a None: il modificatore di specie cambia le stat |
| **Livello RPG oltre ~100** | Fa fallire in silenzio tutto il blocco RPG (§8) | Tetto a 99 |
| **Outfit salvati insieme** | Aggiunti in un solo salvataggio si sovrascrivono a vicenda | Uno alla volta, un salvataggio ciascuno |
| **`linked-characters` 500** | `GET /api/worlds/linked-characters/<world_id>` risponde **500 "Maximum call stack size exceeded"**, cioè ricorsione infinita lato server. È la stessa area del "Failed to link character" segnalato da altri | Nessun workaround, non blocca il lavoro sulle card |
| **PUT con oggetto completo** | Risponde 200 e non scrive niente (§11) | Mandare solo i campi che cambiano |
| **Token scaduto** | GET risponde 404 e PUT 401, quindi sembra una route sbagliata | Rinfrescare il token prima di cambiare route |
| **Cartelle collassate** | Si espandono **solo cliccando la chevron, il primo button della riga**. Cliccare il nome non fa nulla, nemmeno con un click reale. Una scansione che non trova righe fa credere che un personaggio sia sparito | Espandere sempre la cartella prima di concludere che una card manchi. Ha già causato un falso allarme su Dullahan |
| **Combobox** | Non rispondono agli eventi sintetici: il valore sembra impostato e poi torna indietro | Click di mouse reali, oppure apertura e navigazione da tastiera con verifica dell'elemento evidenziato prima di confermare |
| **Parent Location** | Su una Location nuova non offre opzioni finché la Location non è stata salvata almeno una volta | Salvare, riaprire, impostare il parent |
| **Prestazioni** | 40-70 secondi per operazione di pagina, oltre il timeout degli strumenti | Il lavoro di solito va a buon fine lo stesso: verificare lo stato invece di ripetere l'operazione |

**Prima di segnalare un bug**, cercare nel forum `bugs-and-support` se esiste già (§11). Al 2026-09-07 risultano già segnalati da altri: Species/Occupation che non si salvano (patchato a giugno e poi tornato), e il "Failed to link character". Restano da segnalare: il tetto al Livello RPG, gli outfit che si sovrascrivono, il Parent Location vuoto, le cartelle che si aprono solo dalla chevron, e il Save appeso.

**Locale e sito sono entità separate.** Wyldfire, l'app desktop, ha un proprio database locale e carica su Wyvern solo con un gesto esplicito (*Publish to Wyvern*, o il sync delle chat). Modificare il locale non modifica il sito, e quello che si vede in locale può essere più vecchio di quello che c'è online. **Il sito è la sorgente di verità.**

---

## 16. Attitudes su ogni scheda

Fa parte della pipeline §14, come passo 10, subito dopo i Dialogue Examples.

**Regola:** ogni scheda ha almeno le Attitudes verso **Alyssa e Jasper**, che sono i due personaggi giocabili del roster "Choose Your Character". Chi non li conosce va scritto lo stesso, a **Unknown Scent**, con una motivazione che dice che non si sono mai incontrati. Sapere che due personaggi non si conoscono è informazione quanto il contrario, e senza quella riga il modello improvvisa.

Oltre a loro si mettono **solo i personaggi effettivamente citati nel background della scheda**, col tier che il testo giustifica davvero. Non si inventano rapporti per riempire (§9.4).

**Come si compila una Attitude:**

1. **Target Type = World Character** ogni volta che il personaggio esiste come scheda. Il tipo **Generic (text)** serve per fazioni, gruppi e concetti, per esempio la stance verso *Humans First*, e va valutato caso per caso mentre si lavora ogni NPC, non applicato a tappeto.
2. **Tier** dalla ladder del World: Blood Enemy, Enemy, Rival, Distrusted, Wary, Unknown Scent, Acknowledged, Trusted, Pack, Pack-bonded, Beloved.
3. **Intensity**: il campo lasciato vuoto si salva come **1**, cioè il pavimento della banda, non a metà come dice la wiki. Va sempre compilato a mano. Convenzione: **50** di default, **85** dove il rapporto *è* il personaggio, **20** per una conoscenza appena accennata.
4. **Reasoning**: una o due frasi che dicano da dove viene il sentimento.

**The Player (Persona) non si usa** per rapporti specifici di una persona: punta a chiunque stia giocando, quindi una motivazione scritta su Alyssa verrebbe applicata anche a chi gioca Jasper. Si usa solo per stance vere verso qualunque giocatore, tipo lo staff verso uno studente qualsiasi.

**Non toccare mai la ladder dei tier** senza rifare tutte le attitudes: la corrispondenza fra etichetta e chiave salvata è posizionale, quindi aggiungere, togliere o riordinare un gradino rimappa il significato di tutto ciò che è già salvato.
