# Istruzioni di Workflow — Character Card Wyvern (Svartúlfr | Blackwood-Douglas)

Queste istruzioni codificano il processo di lavoro stabilito per la creazione e l'aggiornamento delle character card su Wyvern per questo progetto. Vanno seguite per ogni personaggio.

---

## 1. Formato di consegna: testo, non JSON

**Default:** fornire testo pronto da incollare nei campi del form dell'interfaccia Wyvern (description, personality, first_mes, mes_example, system_prompt, post_history_instructions, lorebook/NPC entries, outfit, tagline, shared info, ecc.), **non** file JSON completi.

Il JSON va generato solo se:
- l'utente lo chiede esplicitamente, oppure
- serve come riferimento per verificare coerenza tra più campi complessi (in quel caso, chiedere se preferisce il file o solo il riepilogo testuale).

Il file JSON scaricato dall'utente **dopo** il salvataggio su Wyvern è il backup di archivio, non un artefatto che Claude deve mantenere sincronizzato in parallelo.

**Eccezione operativa:** quando Claude scrive direttamente sul World via API (§11), il testo non passa dalla chat. In quel caso si consegna il *riepilogo* di cosa è stato scritto e dove, non il testo integrale, più il documento di riepilogo nel Project con i valori precedenti dei campi toccati (§11, "Uso sicuro dell'API").

**Eccezione operativa 2 (lavoro in locale), sospesa dal 22/09:** vale solo se l'utente riattiva esplicitamente il lavoro sul database SQLite locale di Wyldfire (§17). In quel caso vale la stessa logica dell'eccezione precedente: il testo non passa dalla chat campo per campo, si consegna il riepilogo in un documento del Project.

---

## 2. JED+ come formato standard delle schede

Tutte le character card usano il formato **JED+**: un blocco di attributi tra parentesi quadre, separati da punto e virgola (stile bracket/PList), seguito da sezioni in prosa per backstory, dinamiche familiari, voce/comportamento e temi centrali del personaggio.

[NAME: ...; SPECIES: ...; AGE: ...; HEIGHT: ...; ... ]

BACKSTORY: ...

FAMILY & PACK: ...

VOICE & BEHAVIOR: ...

[sezione tematica finale, es. CORE TRAGEDY / THE WEIGHT HE CARRIES / THE SECRET HE CARRIES]


Per personaggi senza legame di branco (aziendali, indipendenti, civili) la sezione "FAMILY & PACK" si sostituisce con l'equivalente pertinente (es. "CLAN AND COMPANY" per Zeera), mantenendo comunque la struttura in quattro blocchi più la chiusura tematica.

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

Questa regola va anche scritta esplicitamente in coda a `post_history_instructions` (campo `final_instructions` via API) di ogni card, così vale durante la chat vera e non solo negli esempi:

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

## 6. World Clock

- **World-age 0 = 21 dicembre 827 d.C., ore 00:00 UTC.** Il valore è letto direttamente dal World (`human_start_date: 0827-12-21T00:00:00.000Z`, `calendar.start_year: 827`, `start_month_id: dec`, `start_day_of_month: 21`).
- Le ore assolute si calcolano con calendario gregoriano proletico standard: `ore = giorni_trascorsi × 24 + ora_del_giorno`.
- **L'anno corrente del World resta il 2024.** `world_age` vale **10486470**, cioè **5 aprile 2024, ore 06:00**, riconfermato via API il 14 settembre. Qualunque riferimento al 2022 nelle fonti è residuo di vecchi setting e va ignorato.

**Come verificare senza sbagliare**, in una riga di JavaScript nel browser autenticato:

```js
EP = Date.UTC(827,11,21);
data = h => new Date(EP + h*3600000).toISOString().slice(0,10);
ore  = iso => (Date.parse(iso) - EP) / 3600000;
```

Un controllo di sanità che vale sempre: `birthdate` e `start_timeline_position` di un personaggio vivo devono coincidere, e nessuna delle due può essere maggiore di `world_age`.

---

## 7. Triage import Lorebook Entries → World

**I personaggi deceduti non vanno più in Lexicon.** La vecchia regola nasceva dal non poter esprimere un arco temporale di presenza. Ora Wyvern lo permette, quindi:

- **Personaggi vivi** → Character, con **Start Position**.
- **Personaggi deceduti** → Character, con **Start Position e End Position** (modello: Nixara).

**La Start Position va sempre messa, senza eccezioni**, anche per un personaggio contemporaneo che sembra non averne bisogno. Sono già previsti tre scenari fuori tempo: il viaggio di Wulfnic, uno scenario piratesco per Cornelius, e uno futuristico ambientato nel **2499**. Senza Start Position un personaggio del 2024 comparirebbe anche a bordo della nave di Wulfnic.

**La End Position sui personaggi vivi si metterà quando lo scenario futuristico verrà costruito**, non prima. In quel momento andrà decisa caso per caso, tenendo conto che per Jasper, Noah e Malachia il fine vita è ulteriormente rallentato da impianti cibernetici pesanti (nelle schede bozza del futuro la specie è scritta **Cyber-Werewolf**).

| Tipo di entry | Azione |
|---|---|
| Species_Details / Intimacy Profile del personaggio proprietario | **Non importare** nella description (già parte della card collegata); gli Intimacy Profile vanno come Lexicon separata secondo §13.3 |
| Personaggio vivo, ricorrente in più schede (es. Magnus, Elizabeth, Kaladin) | Importa **una sola volta** come Character con Start Position; riusa e linka nelle altre schede, non duplicare |
| Personaggio deceduto (es. Nixara) | Importa come **Character** con Start **e** End Position |
| Luogo già creato manualmente come Location (es. The Verve) | **Non importare** la versione lorebook equivalente, è un doppione |
| Attività o concetto senza posizione fisica mappata (es. underground fighting ring) | Importa come **Lexicon** |
| Luogo fisico non ancora mappato | Importa come **Location** |
| Gruppo di personaggi off-world che nessuno incontrerà a breve | Accorpa in **una sola entry Lexicon** ricca (es. "The Other Contractors"), scorporabile in Character singole solo se uno entra davvero in scena |
| Lore di specie generale (biologia, cultura, sottogruppi) non legata a un singolo personaggio | Importa come **Lexicon di tipo `lore/concept`**, `is_global: true`, panoramica ampia senza dettagli anatomici/intimi (vedi riga sotto per quelli) |
| Meccanica riproduttiva/anatomica/intima di una specie intera (non di un personaggio) | Entry Lexicon separata, tipo `memory`, `is_global: false`, keys primarie sul nome della specie + secondarie sull'argomento (accoppiamento, fertilità, anatomia), registro biologico/enciclopedico, non narrativo |

**Entry Type del World Lexicon (verificato il 22/09).** La tassonomia valida è quella della pagina wiki `wiki.wyvern.chat/en/Features/Worlds/Lexicon`, **non** quella di `/en/Advanced/Lexicon`, che riguarda Chat Lexicon e Character Lexicon (NPC/Item/Location/Event/Concept/Memory/Other, feature diversa, non usata qui). Valori per il World:
- testo puro: `lore/concept`, `organization/faction`, `memory`, oppure nessun tipo;
- con pannelli di configurazione aggiuntivi: `item`, `furniture`, `creature`, `move`, `nature`, `ability`.

Il vecchio "tipo `mob`" citato in versioni precedenti di questa regola non esiste nella tassonomia: le entry di specie generale vanno in `lore/concept`, `creature` solo per veri mob/nemici.

**Regola di Lys (22/09): ogni entry Lexicon che fa riferimento a un unico personaggio** (Intimacy Profile, Digital Interactions, Attitudes & Relationships, ricordi personali) va impostata con **Entry Type = Memory** e collegata al personaggio tramite il campo **Attached Character** (`attached_world_character_id`). Le entry `memory` che coinvolgono più personaggi (eventi datati, chat di gruppo, tradizioni di un gruppo) restano senza Attached Character.

**Placement:** tutti i Character vanno impostati come **Global Character = ON**. Popolare i Character Pool di Location ed Environment si è rivelato inutile, perché in pratica andavano inseriti quasi tutti ovunque, e appesantiva gli Environment senza guadagno.

**Attivazione delle entry Lexicon.** `is_global: false` non restringe una entry: la **spegne**, togliendola del tutto dalla scansione a parole chiave del mondo. Diventa idonea solo se inclusa nella `included_lexicon_entries` di una Location, di un Environment o di uno Scenario, e anche allora serve comunque una chiave che matcha oppure `constant: true`. Il campo `attached_world_character_id` **non è un canale di attivazione**. Per restringere una entry ai contesti giusti si usano:

- `keys` + `secondary_keys` + `key_logic`, con la forma corretta **primarie = identificatori della persona (o della specie), secondarie = parole dell'argomento**. Chiavi generiche come `intimacy` o `werewolf` messe fra le primarie con `key_logic: AND_ANY` fanno sparare la entry in continuazione.
- `party_conditions`, cioè il filtro su chi è nel party. È lo strumento giusto per i contenuti personali: un Intimacy Profile con `has_any [proprietario]` esiste solo nelle scene in cui quella persona c'è davvero.

Il macro `{{lexiconEntryNames}}` elenca le entry **candidate** per la scena, non quelle che hanno effettivamente matchato una chiave. Serve a diagnosticare una entry spenta, non a validare un filtro.

---

## 8. RPG Stats  *(AGGIORNATA — sistema in pausa dal 13/09, riconfermato il 14/09)*

**Stato attuale: `world_features.rpg_stats` è `false` a livello World.** L'utente ha disattivato l'intero sistema di Simulation tranne Relationships dopo test diretti (vedi `Simulation_World_Features_Disattivate_2026-09-13.md`), e lo stato è stato riverificato via API il 14 settembre: ancora spento, nessun cambiamento.

**Conseguenza pratica per la pipeline:** il passo §14.8 (RPG Stats) è **in pausa di default su ogni nuova scheda**, finché l'utente non riattiva il toggle a livello World. Non abilitare, non distribuire punti, non impostare Livello/Specie/Occupazione su una scheda nuova senza indicazione esplicita contraria per quella sessione. Se capita di dimenticarsene e popolarli comunque (come successo il 14/09 su sei schede), non c'è nulla da disfare: i dati restano sulla card, semplicemente inattivi lato gioco finché il toggle resta OFF, e sono pronti per quando/se verrà riattivato. Verificare comunque lo stato del toggle a inizio sessione se si prevede di lavorare su RPG Stats.

**Convenzioni del progetto, valide quando il sistema sarà riattivato:**
- Budget punti fisso a **25**, indipendentemente dal Livello. Con base 1 su sei stat, i valori finali sommano sempre a **31**.
- **Livello = età anagrafica**, con il tetto sotto.
- Stat: MGT (Might), RES (Resilience), AGI (Agility), WIT (Wits), PRS (Presence), SCT (Scent). Nel salvataggio via API i sei valori vivono come `base_stats.stat_1`...`stat_6`; la corrispondenza MGT→stat_1, RES→stat_2, AGI→stat_3, WIT→stat_4, PRS→stat_5, SCT→stat_6 è dedotta per analogia con altre schede del World e non è stata confermata contro la UI, da verificare se si vuole certezza assoluta.

**Tetto di piattaforma al Livello (bug confermato):** un Livello di **300 fa fallire in silenzio il salvataggio dell'intero blocco RPG**. Nessun errore visibile, il pulsante Save resta appeso su "Saving...", e dopo il reload le RPG Stats risultano di nuovo disabilitate con stat e livello persi. Livello **99 salva e persiste**, verificato più volte, anche di recente. Il tetto esatto sta fra 100 e 299, non isolato.

**Convenzione conseguente per i longevi:** per chiunque superi il secolo (Zefir, Ut, Wulfnic, Cornelius, Archer, Magnus, Dullahan, e ora anche Vito Marino e Marcus O'Connor dopo la promozione a Pureblood, vedi §12) usare **Livello 99** e tenere l'età reale nel blocco JED+. La convenzione "Livello = età" vale solo fino a 99.

**Species e Occupation fanno parte del blocco RPG**, e si impostano solo via API (§11 e §15). Vanno messe su ogni scheda che ha le RPG Stats abilitate: il modificatore di specie viene applicato davvero alle stat, quindi lasciarle vuote non è neutro. Il blueprint delle Occupation è limitato (18 voci al 14/09: Bartender, Bodyguard, CEO, DJ, Divine Guardian, General Laborer, Line Cook, Living Saga, Master Blacksmith, Matriarch, Mechanic, Musician, Patriarch, Security Commander, Server, Stage Technician, Student, Teacher) e per molte occupazioni reali di una scheda (es. istruttore tattico indipendente, boss di un'organizzazione industriale) non c'è una corrispondenza esatta: scegliere la più vicina disponibile e non forzarne una palesemente sbagliata.

**Formula Condition/Control: da riverificare, non affidabile.** La formula registrata in precedenza (`Condition = 67 + 2×(liv−1)`, `Control = 30 + 1×(liv−1)`, da Erik, Logan e Malachia) **non si è riprodotta**: su Dullahan, a Lv.1 con tutte le stat a 1, i valori base erano **56 e 46**, non 67 e 30. Va rifatto un test pulito prima di trattarla come acquisita. Probabile che il pool dipenda anche dalla distribuzione delle stat, e ora sappiamo che **dipende anche dalla specie**, visto che assegnarla cambia i valori.

---

## 9. Gestione discrepanze nei documenti sorgente

Quando le fonti si contraddicono su un dettaglio (altezza, età, tatuaggio, profumo, ruolo in squadra, ecc.):

1. Usare il valore con **maggiore consenso tra le fonti** (es. 2 file su 3 concordi), e a parità di consenso la fonte più forte secondo la scala di §11.
2. **Segnalarlo in un documento del Project**, con la discrepanza esatta trovata, così resta tracciabile per una futura pulizia dei sorgenti. **Correzione 14/09: non esiste un campo `creator_notes` nello schema Character di Wyvern** (verificato sull'oggetto restituito dall'API, assente su tutte le schede lette finora). La documentazione delle discrepanze va quindi nel Project, non su un campo della card che non esiste.
3. Non correggere i file sorgente originali senza autorizzazione esplicita dell'utente.
4. **Non inventare mai per riempire un buco.** Se una fonte tace su un dettaglio, o lo si lascia fuori, o lo si segnala come invenzione dichiarata. Una scheda scritta a intuito prima che arrivino le fonti va **riscritta da zero** quando arrivano, non ritoccata: è già successo con Barkley Rover, dove erano sbagliati età, altezza, aspetto, anni di servizio, famiglia e soprattutto il carattere.
5. **Un dettaglio letto una volta e riportato in un documento acquista un'autorità che non ha.** Prima di costruirci sopra, va riverificato alla fonte. È già successo con "Bulls vs Claws", che era una lettura sbagliata di "Bulls vs CLAMS" e per poco non diventava canon per inerzia. Vale anche per i documenti del Project stessi: il 22/09 un audit del 14/09 diceva "Ariadne già sistemata", ma la card era stata ricreata il 18/09 con un id nuovo e il lavoro era da rifare.
6. **Quando si inventano date** (compleanni, morti, eventi), non usare sempre il 1° gennaio o il 1° del mese. Scegliere date varie e credibili.
7. **Quando l'utente lascia esplicitamente una scelta a discrezione di Claude** (es. "stabiliamo l'età in base a quella più adatta alla personalità"), proporre un valore motivato e attendere conferma prima di scrivere sul World, invece di procedere silenziosamente. Vale soprattutto per età, date, e qualunque numero che diventa poi un vincolo di continuity per schede future.

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

**Personaggi importati da varianti fantasy/altri contesti dell'utente** (non canon esterno, ma altro materiale creativo proprio dell'utente, es. Zeera, Yael, Huck) seguono una logica diversa dalla precedenza di dominio: sono riscritture libere, non vincolate al materiale sorgente se non per aspetto, personalità e voce. Backstory, occupazione e agganci al World vanno **ricostruiti da zero** per calzare su Blackwood, non semplicemente "tradotti". Vedi §13 per cosa va comunque escluso a prescindere dalla riscrittura.

**Gli adattamenti vanno registrati, non nascosti.** Quando Blackwood si discosta dal canon originale, la cosa va scritta in un documento del Project con la forma "cosa dice la fonte, cosa facciamo noi, perché non è una contraddizione". Il caso più profondo è la longevità dei licantropi (§12): non abbiamo scavalcato il canon originale, gli abbiamo dato il dominio che gli compete, cioè il licantropo comune, e abbiamo tenuto Blackwood dove Blackwood serve, cioè sulle Case e sui Firstborn.

**L'autore dell'ambientazione SUCC ha dichiarato esplicitamente** che *"the rules for modfan are literally… i dont have any rules for myself when it comes to it"*, e ha dato via libera a fan OC, immagini generate e uso dei personaggi canon come comparse. Adattare non è uno strappo, è l'uso previsto. Resta l'obbligo di accreditare quando si copia testo alla lettera.

---

## 11. Fonti, accesso al web e lavoro sul World  *(AGGIORNATA 22/09 — il sito torna fonte principale, API solo per lettura e modifiche mirate)*

**Nota di metodo (dal 22/09):** il **sito Wyvern** (`app.wyvern.chat`) torna a essere la fonte di verità e il canale di lavoro principale. Il lavoro sul database locale di Wyldfire è sospeso (§17). Sul sito si lavora in due modi, entrambi scrivono direttamente sul World pubblicato:

- **dall'interfaccia web**, per il lavoro di scrittura esteso o creativo su una scheda e per tutto ciò che l'utente vuole seguire a schermo;
- **via API dal browser autenticato**, esclusivamente per **lettura dei dati** e per **modifiche mirate**, secondo le regole di sicurezza qui sotto.

### Regola di accesso

**Non usare mai il fetch diretto delle pagine.** Ogni consultazione web passa dal **browser locale**, aprendo la pagina in una scheda e leggendola da lì. Vale per la wiki, per Discord e per qualunque altra fonte.

### Le fonti dell'ambientazione originale, in ordine di forza

1. **I lorebook ufficiali** pubblicati dall'autore su Discord, server *io's bot hub*, canale `lorebooks-and-cards`, post **IOVERSE LOREBOOKS**: `SUCC_-_U_-_VERSE.json`, `Dead_Dog_Motel.json`, `Starfall_1.0.json`, `Post-Apocalyptic_2.0.json`. Sono testo scritto e distribuito dall'autore come materiale di riferimento.
2. **Le risposte dell'autore** (`io wuvs soap`) nei thread del canale forum `ioverse-q-n-a`. Stesso livello dei lorebook: è l'autore che risponde, non un riassunto. Il modo efficiente di leggerli è la ricerca Discord con i filtri `da:` autore e `in:` canale, che isola le risposte dal rumore delle domande.
3. **Il portale ufficiale SUCC** (`io-succ.uwu.ai`).
4. **La wiki Fandom** e il resto del materiale di terzi.

Nota: i thread **ASTRAL IMPERIUM Q&A**, **THE EDGE Q&A** e **GENERAL IOVERSE QUESTIONS** sono praticamente vuoti, solo placeholder e indici. Non vale la pena rileggerli. Il canale `succ-and-modern-fantasy` è chiacchiera di community sugli OC dei fan, non canon.

### Documentazione di piattaforma

**La fonte documentale principale è la WyvernWiki, `https://wiki.wyvern.chat/`.** Prima di lavorare su qualunque funzione della piattaforma (campi di una card, Lexicon, Location, Environment, Scenari, Timeline, Attitudes, RPG, sistemi del World) si consulta la pagina wiki pertinente, dal browser locale, e ci si attiene a quella: nomi dei campi, valori ammessi (es. gli Entry Type del Lexicon), comportamento atteso. Le decisioni di lavoro prese in base alla wiki citano la pagina nel documento di riepilogo del Project.

- **Dove guardare nella wiki:** per i World la guida vera sta sotto `/en/Features/Worlds/...` (pagina indice `/en/Features/Worlds`, capitoli tipo `/en/Features/Worlds/Lexicon`). Le pagine sotto `/en/Advanced/...` descrivono spesso le feature di chat/character, che hanno nomi simili ma regole diverse: prima di applicarle a un World, controllare che non esista la pagina equivalente sotto Worlds. La wiki è in beta e aggiornata spesso (data "Last edited" in cima a ogni pagina): una pagina letta in una sessione precedente va riletta se la decisione dipende da un dettaglio.
- **r/WyvernChat**: `https://www.reddit.com/r/WyvernChat`, fonte secondaria per community e workaround non documentati ufficialmente. Le ricerche mirate danno risultati rumorosi, affinare i termini caso per caso.
- **Discord WyvernChat**, fonte secondaria. Canale forum `bugs-and-support` per i bug del sito, `wyldfire-bugs-and-support` per quelli dell'app desktop, `#dev-notes` per le modifiche importanti non ancora riportate in wiki. Il post fissato *HOW TO REPORT ISSUES* contiene il template da usare per ogni segnalazione. **Prima di aprire un bug si cerca se esiste già**, con `in:bugs-and-support <termine>`.

**Ordine delle fonti documentali:** 1. WyvernWiki; 2. `#dev-notes` su Discord (per novità non ancora in wiki); 3. Reddit e resto di Discord.

**Quando la wiki e la piattaforma non concordano:** fa fede il comportamento osservato e verificato (dopo reload completo o con una GET autenticata fresca) in questa conversazione, poi un export reale scaricato da Wyvern dopo un salvataggio. La discrepanza con la wiki si annota nel Project (e in §15 se è stabile), così resta chiaro che la wiki su quel punto è indietro. Esempio già noto: l'Intensity lasciata vuota nelle Attitudes si salva come 1, non a metà banda come dice la wiki (§16).

### Uso sicuro dell'API

**Lettura: sempre consentita, senza chiedere.** GET su liste e singole entità per audit, conteggi, diagnosi, confronti, preparazione di un piano e verifica dopo ogni scrittura. È il modo preferito per sapere com'è davvero il World: più affidabile delle cartelle e delle ricerche dell'interfaccia (§15).

**Modifiche mirate: consentite quando rientrano in ciò che l'utente ha chiesto.** Una modifica mirata tocca campi precisi di entità precise, identificate per id. Procedura obbligatoria:

1. **Snapshot prima di scrivere.** GET fresca dell'entità e conservazione dei valori precedenti dei campi che cambiano (in memoria nella pagina e, per ogni operazione su più entità, nel documento di riepilogo del Project). Senza snapshot non si scrive.
2. **Identificare per id, mai per nome.** Il World contiene duplicati con lo stesso nome ed entry orfane collegate a personaggi ricreati (§15). Prima di scrivere si controlla che l'id sia quello presente nella lista attiva del World.
3. **Body parziale**: solo i campi che cambiano (vedi trappole sotto).
4. **Array**: leggere l'array corrente, modificarlo in memoria, rimandarlo intero.
5. **Verifica con GET fresca** dopo la scrittura. Lo status 200 non è una prova.

**Operazioni in blocco** (più di una decina di entità nella stessa passata, o una modifica a tappeto su una categoria): prima si presenta all'utente il piano, cioè quali entità, quali campi, quali valori e come sono stati decisi, e si attende l'ok. Poi si esegue a **lotti di massimo 25**, salvando il progresso in una variabile della pagina così che un lotto interrotto si possa riprendere senza ripetere né saltare nulla, e si chiude con una verifica globale sulla lista del World. I casi ambigui (nome non risolvibile, duplicati, id non trovato) si segnalano e non si indovinano.

**Creazioni (POST):** consentite quando l'utente chiede una scheda o una entry nuova. Prima si controlla via GET che non esista già (anche con varianti del nome), per non generare duplicati.

**Cancellazioni (DELETE): solo su richiesta esplicita dell'utente** che nomina l'entità o la categoria da eliminare. Non esiste un cestino, quindi:
- prima di cancellare, il contenuto completo dell'entità va salvato nel documento di riepilogo del Project;
- una cancellazione per chiamata, mai in un ciclo;
- mai una cancellazione come effetto collaterale non chiesto (per esempio eliminare il "doppione" dopo un merge che l'utente non ha chiesto).

**Mai via API senza richiesta esplicita:** PUT con l'oggetto completo, modifiche alle impostazioni del World (`world_features`, calendario, `world_age`, travel, simulation), qualunque operazione su World o contenuti di altri utenti.

### Dettagli tecnici dell'API

Un `fetch` scritto a mano senza header di autenticazione restituisce `[]` oppure 401/403, e **una risposta vuota così non è la prova che i dati siano spariti**. Con l'header giusto invece l'API funziona, ed è enormemente più veloce e più affidabile del pilotare l'interfaccia a click.

- **Base URL confermata:** `https://app.wyvern.chat/api/...` (non un dominio `api.wyvern.chat` separato, che risponde 404).
- **Il token va rinfrescato, non letto.** Quello in IndexedDB scade dopo un'ora e resta lì scaduto: usarlo produce **404 sulle GET e 401 sulle PUT**, quindi sembra che la route sia sbagliata mentre è solo scaduta. Si legge il refresh token dalla riga `firebase:authUser:<apikey>:[DEFAULT]` di `firebaseLocalStorageDb` e si chiede a `securetoken.googleapis.com` un access token nuovo. Va rifatto dopo ogni reload o navigazione della pagina e ogni ora.
- **Eseguire gli script sempre nella scheda di `app.wyvern.chat`, indicandola esplicitamente.** Se nel browser sono aperte altre schede (wiki, Discord), uno script lanciato senza scheda esplicita può girare su quella sbagliata e trovare un IndexedDB vuoto.
- **Limite di tempo degli script:** oltre circa 45 secondi lo strumento interrompe l'esecuzione. Le operazioni lunghe vanno spezzate a lotti (vedi sopra).
- **Le route** hanno uno schema uniforme per ogni risorsa (`characters`, `locations`, `environments`, `lexicon`, `scenarios`): lista `GET /api/worlds/<risorsa>/world/<world_id>`, singolo `GET /api/worlds/<risorsa>/<id>`, crea `POST /api/worlds/<risorsa>` col `world_id` nel body, modifica `PUT /api/worlds/<risorsa>/<id>`, elimina `DELETE`. Su un Character il campo lungo è `long_summary` e il nome è `display_name`, non `name`.
- **Due route non seguono lo schema:** `GET /api/worlds/rpg/species/<world_id>` e `GET /api/worlds/rpg/occupations/<world_id>` per i blueprint RPG del World.
- **La trappola grossa: il PUT vuole un body parziale.** Un PUT con l'oggetto completo risponde 200 e non scrive niente. Si mandano solo i campi che cambiano.
- **Attenzione ai campi annidati.** `species_id` e `occupation_id` **non** sono campi di primo livello del Character: vivono dentro `rpg_stats`. Mandati al primo livello il PUT risponde 200 e li scarta in silenzio. Si legge `rpg_stats`, lo si estende e si rimanda solo quello. È lo stesso modo di fallire del PUT completo: **lo status 200 non è una prova**. Sulle entry Lexicon invece `type` e `attached_world_character_id` sono campi di primo livello.
- **Gli array si sostituiscono per intero, non si fanno il merge.** `outfits`, `attitudes`, `speech_examples`, `titles`, `keys`, `tags`, `party_conditions`: un PUT che manda solo l'elemento nuovo **cancella** tutti gli altri già presenti. Prima di un PUT su un array esistente, leggere l'array corrente, aggiungere/modificare l'elemento voluto, e rimandare l'array intero.
- **Per appendere o inserire testo** si legge il campo, si modifica la stringa in JavaScript e si rimanda solo quel campo. Non si ridigita mai a mano il testo esistente.
- **Non usare `/api/worlds/characters?world_id=`**: ignora il parametro e restituisce oltre 1500 personaggi da tutti i World pubblici.
- **Un "successo" dell'interfaccia non è una prova nemmeno lui.** Il 22/09 un salvataggio dall'interfaccia ha mostrato il toast di successo mentre la PUT andava a un'altra entry con lo stesso nome. Si verifica sempre con una GET per id.
- **Anche via API vale la verifica finale (§14.12):** si verifica dopo un reload completo, o con una GET autenticata fresca, rileggendo dalle liste del World. È la verifica a dirlo, non lo status 200.

---

## 12. Invecchiamento, longevità e filone SciFi

### Founding Bloodline e Divine Blood

Le varianti "SciFi" trovate nei documenti legacy (Erik su una città-nave, Logan nell'Undertrade, Malachia "Vanguard Commander", ecc.) **non sono rumore da scartare**: sono un filone narrativo futuro non ancora sviluppato, reso plausibile dalla quasi-immortalità di questi personaggi.

- Crescita completa raggiunta intorno ai 21 anni, dopo di che l'invecchiamento rallenta fino a fermarsi quasi del tutto. I personaggi Founding/Divine Blood adulti sono sostanzialmente fermi salvo diversa indicazione.
- Sangue Founding: Malachia, Noah, Jasper, Alyssa. Divine Blood: Wulfnic, Ut, Zefir.
- **Il Divine Blood non rallenta, si è fermato.** I Firstborn portano l'età che avevano nel momento in cui Fenris li ha presi. **Wulfnic e Ut** erano guerrieri adulti e portano la faccia di un quarantenne *del loro secolo*, che un occhio moderno archivia intorno ai sessanta.
- **Zefir ha 1019 anni**, non 1200 come diceva la versione precedente di questa regola (nato il 5 febbraio 1005). È il più giovane dei Nove e l'unico preso prima della fine della crescita, quindi dimostra ancora diciotto o diciannove anni. Era però **maggiorenne per legge norrena**: non era un bambino secondo il proprio secolo, era un adulto dell'XI secolo che il XXI secolo non riesce a vedere come tale.

### Pureblood Houses

Lifespan **200-400 anni** (tabella `LSE_01_Species.md`, mai messa in discussione a differenza dei Common sotto). Genetica stabile, invecchiamento lento ma non completamente fermo come nei Founding: un Pureblood molto anziano può comunque mostrare segni di età reale (capelli bianchi, viso segnato), semplicemente distribuiti su una scala temporale molto più lunga di un Common. Non esiste ancora una formula precisa messa alla prova per questa curva: al momento si sceglie un'età apparente coerente con la storia del personaggio senza calcolo rigido, stesso approccio adottato per i Common sotto.

**Decisione 14/09: si possono promuovere famiglie esistenti da Common a Pureblood** quando la storia lo giustifica e l'utente lo conferma esplicitamente. Precedente: le famiglie **Marino** (Vito, Ironworks) e **O'Connor** (Marcus, Oldtown) promosse a Pureblood per dare loro un'origine reale da immigrati di lunga data (Marino dal sud Italia anni '20, O'Connor dall'Irlanda inizio '800), motivato dal fatto che Blackwood, essendo più antica di Solarton, può permettersi qualche Pureblood in più oltre ai Douglas. Ogni promozione del genere richiede: aggiornare `SPECIES` nel JED+, ricalcolare `birthdate`/`start_timeline_position` per la nuova età reale, e se le RPG Stats sono già impostate, portare il Livello a 99 (vedi §8).

### Common Bloodline: non rientrano in questa meccanica

Vivono **60-80 anni**, pari o poco sotto la media umana, e invecchiano cronologicamente come un umano. È il canon dell'autore originale (*"about the same, actually maybe slightly less then average human lifespan"*, più la spiegazione del *"hot blooded, burning out sooner"* e delle morti per conflitto), e vale per la stragrande maggioranza dei licantropi che si incontrano a Solarton e a Blackwood.

Invecchiano però **visibilmente** molto più lentamente: crescita normale fino a 25 anni, poi circa **un anno di aspetto ogni cinque vissuti** (un Common di 50 dimostra 30, uno di 70 poco più di 34), con un cedimento rapido negli ultimi anni di vita. Il collasso finale è esattamente il "burning out" visto dall'altro lato: tengono la forma del proprio prime quasi fino alla fine, e poi bruciano.

La fertilità dei Common cala **dai 35 anni**, non dai 50.

**Nota pratica 14/09, su indicazione dell'utente: quando una fonte fornisce solo un'"età apparente" per un personaggio,** quel numero va trattato come il dato di aspetto fisico da scrivere in scheda, mentre l'età reale (anagrafica) va scelta da chi costruisce la scheda in base a cosa serve meglio alla personalità e alla storia, non ricalcolata a rigore dalla formula sopra. La formula resta lo strumento di riferimento per verosimiglianza, non un vincolo assoluto da rispettare cifra per cifra. Qualunque età reale scelta così va comunque proposta e confermata dall'utente prima di scriverla sul World (§9.7), specialmente se comporta il superamento della soglia dei 100 anni (che a sua volta comporta la promozione implicita a Livello RPG 99, §8, e potenzialmente la domanda se il personaggio debba passare a Pureblood, vedi sopra).

### La conseguenza che conta scrivendo

**L'aspetto non dice niente sulla classificazione del sangue**, a nessuno dei due capi della scala. Un Common dimostra vent'anni meno di quelli che ha, un Firstborn mille. Chi dimostra trent'anni può essere un Common di cinquanta con quindici anni davanti, un Pureblood di duecento o uno dei Nove. **Nessun personaggio può dedurre il sangue di un altro guardandolo.** L'età si legge dal portamento, dall'odore e da cosa uno ha vissuto, mai dalla faccia. I Common si leggono bene fra loro; umani ed estranei sbagliano in entrambe le direzioni, e di solito per difetto.

Sulle schede di personaggi Common adulti l'aspetto va scritto sull'**età apparente**, non su quella anagrafica, e la scheda dovrebbe dirlo.

---

## 13. Epurazione di `{{user}}` e di contenuto non riutilizzabile dal materiale importato  *(ESTESA)*

**`{{user}}` va tolto ovunque, senza sostituirlo con un nome.** In questo World `{{user}}` non è una persona fissa: è Alyssa Douglas solo in alcuni scenari, in altri può essere la fidanzata di Jasper, o Jasper stesso, o altro ancora. Qualunque relazione scritta su `{{user}}` verrebbe quindi applicata a chiunque stia giocando, e in molti casi punterebbe contenuto romantico o sessuale di un personaggio adulto verso una matricola di diciannove anni.

**Procedura obbligatoria su ogni import:**

1. **Generalizzare il ruolo, mai nominare un personaggio del World.** "{{user}}, l'allenatrice di cheerleading" diventa "chiunque gestisca il programma di cheerleading in una data stagione".
2. **Rimuovere integralmente cotte, relazioni e tensione sessuale rivolte a `{{user}}`** quando il personaggio è adulto e il giocatore sarebbe uno studente, e a maggior ragione quando è staff. Non attenuare: rimuovere. Il buco narrativo si riempie con altro materiale del personaggio.
3. **Non trascrivere i blocchi anatomici e di kink espliciti** nella description. **Regola generale (14/09, non più solo un'opzione per il materiale importato): questo contenuto non va scartato, va spostato come Intimacy Profile separato per QUALUNQUE personaggio**, con `party_conditions` sul proprietario, secondo il formato già in uso su gran parte del World (vedi sotto). Nella description resta al massimo una riga sobria e non grafica.

   **Formato confermato via API, osservato su schede già esistenti (Erik, Logan, Malachia, Bailey, Dominic, Venera, Santiago, Roland, Mac, Fade, Adelin, Chase, Stanley, Zero, Jean-Luc, Dante, Arthur):** entry Lexicon `name: "Intimacy Profile - <Nome>"`, **`type: "memory"` (Entry Type = Memory, obbligatorio)**, **`is_global: true`** (non `false`: l'entry resta nella scansione globale del World, è il `party_conditions` a restringerla alle scene dove il proprietario è davvero presente, non l'`is_global`), `keys: ["<Nome>"]`, `secondary_keys: ["intimacy","dating","relationship","romance","flirting","attracted","sex"]`, `key_logic: "AND_ANY"`, `priority` intorno a 50 (100 per le schede con lo stile a blocchi sotto), `party_conditions: [{character_ids: ["<id del personaggio>"], mode: "has_any"}]`, e **`attached_world_character_id` impostato sull'id dello stesso personaggio (campo Attached Character, obbligatorio per regola di Lys del 22/09**, anche se resta non un canale di attivazione, vedi §7). L'id va sempre quello **attuale** del personaggio nella lista Character: se la card è stata ricreata, l'id vecchio lascia l'entry orfana. Due registri di scrittura osservati, entrambi validi, da scegliere caso per caso: **a blocchi** con etichette tipo `<Nome>_INTIMACY_BASELINE`, `_BODY_REACTIONS`, `_VULNERABILITY_SHAPE`, `_VOICE_IN_INTIMACY`, `_HARD_LIMITS_AND_HARD_YESES`, `_AFTERMATH` (stile Erik, più sistematico, utile per personaggi con una psicologia sessuale complessa o un trauma specifico legato all'intimità); **in prosa** continua, tre o quattro paragrafi su drive, dinamiche preferite, limiti e cosa lo eccita davvero, senza misure anatomiche numeriche esplicite (stile Dominic Rogers, più adatto alla maggior parte dei casi). Non esiste ancora una regola su quale stile scegliere: buon senso in base alla complessità psicologica del personaggio.

   **Nota di continuità:** questa regola è stata chiarita il 14/09 dopo la lavorazione di Zeera, Huck e Brak Ironfist, sulle cui schede il contenuto anatomico/kink esplicito del materiale sorgente era stato inizialmente scartato. Il 22/09, su richiesta di Lys, il contenuto riusabile (solo kink/anatomia, mai l'arco `{{user}}`) è stato recuperato nei rispettivi Intimacy Profile.
4. **Aggiungere, dove il personaggio ha autorità su studenti**, una riga esplicita sul suo rapporto con loro, che chiuda la porta invece di lasciarla socchiusa.
5. **Non usare "The Player (Persona)" nelle Attitudes per rapporti specifici di una persona** (§16). Punta a chiunque stia giocando, quindi è lo stesso errore di `{{user}}` in un altro campo.
6. **Verificare a fine lavorazione** che la stringa `{{user}}` non compaia più in nessun campo della card.
7. **Documentare nel Project** cosa è stato rimosso e perché (non esiste un campo `creator_notes` sulla card, vedi §9.2).

**Estensione 14/09, applicata su Zeera e Harlan "Huck" Beaumont:** quando una card sorgente contiene tratta di persone, sfruttamento sessuale, rapporti non consensuali, o un intero arco narrativo di attrazione/cotta romantica costruito specificamente attorno a `{{user}}` (non solo qualche riga isolata), **quel materiale non va portato nella scheda nuova in nessuna forma**, nemmeno trascritto per poi "ripulirlo": va escluso fin dalla lettura della fonte. Questo vale a prescindere dal fatto che il personaggio venga riconvertito per un ruolo completamente diverso nel World (es. un mercante di schiavi diventato CEO di un'agenzia di personale, un romance interest militare diventato un rappresentante politico indipendente): la riconversione del ruolo non richiede e non giustifica portare avanti il contenuto sessuale/non consensuale originale, nemmeno come "retaggio del personaggio". Si porta avanti solo ciò che è riusabile senza quel contenuto: aspetto fisico in versione non esplicita, tratti di personalità, voce, e gli elementi di trama che reggono anche senza la componente romantica o sessuale rimossa.

Casi già trattati con questa regola: Dullahan (allenatrice di cheerleading con "unbearable sexual tension"), Barkley Rover (cotta in una variante, fidanzato nell'altra), Richard Loewe (riga sugli impulsi verso `{{user}}`, trasformata nella sezione THE LINE senza destinatario), Zeera (mercante di schiavi Vax, rapporto non consensuale con `{{user}}` e blocchi anatomici espliciti, riconvertito in CEO di un'agenzia di personale con il passato di schiavismo trattato come retaggio culturale della specie, non come pratica attuale del personaggio), Harlan "Huck" Beaumont (arco romantico/sessuale completo verso `{{user}}` con sezione kink esplicita, riconvertito in rappresentante umano del Concilio indipendente da ogni fazione, mantenendo solo aspetto, ruolo militare e personalità spogliata dalla direzione romantica), Marek (arco del vicino di casa `{{user}}` escluso integralmente, 22/09).

---

## 14. Pipeline standard di una card

Ordine di lavorazione, da seguire per ogni personaggio. Ogni passo si verifica prima di procedere. Il lavoro avviene sul sito (interfaccia o API mirata, §11).

1. **Raccogliere tutte le fonti prima di scrivere.** Varianti multiple, file di lore, lorebook ufficiali (§11), risposte dell'autore, entry Lexicon esistenti, agganci già scritti in altre schede, e per ogni campo o funzione della piattaforma la pagina pertinente della WyvernWiki (§11). Non iniziare la scheda con materiale parziale (§9.4). Se il materiale copre solo nome/ruolo/relazioni senza personalità o backstory, chiederlo esplicitamente all'utente prima di inventare (§9.7).
2. **Controllare se il personaggio esiste già** nel World, interrogando la lista Character via API con un filtro sul nome (più affidabile delle cartelle dell'interfaccia). Molti sono presenti come import grezzi o segnaposto vuoti: vanno riempiti, non ricreati, per non generare duplicati.
3. **Epurare `{{user}}` e contenuto non riutilizzabile** secondo §13.
4. **Scrivere i campi:**
   - `long_summary` in JED+ (§2), con `{{age}}` nel campo AGE
   - `summary` come blocco PList di soli tratti
   - `display_description`, una o due righe che dicano chi è e cosa lo rende interessante
   - nickname, titoli, keys, pronomi
5. **Outfit: cinque, contestuali** (§4). Via API si manda l'array completo in un solo PUT (§11); dall'interfaccia vanno invece aggiunti **uno alla volta con un salvataggio ciascuno**, altrimenti si sovrascrivono. Almeno uno dovrebbe dire qualcosa che la prosa non dice.
6. **Default Outfit**, da scegliere fra i cinque. L'interfaccia lo segna come *Required* e senza di esso il modello improvvisa l'abbigliamento in ogni scena che non attiva un outfit contestuale. Si sceglie quello che il personaggio indossa quando non sta facendo niente di particolare, non il più bello.
7. **Start Position** calcolata dal World Clock (§6), sempre. End Position solo se deceduto (§7).
8. **RPG Stats (§8): in pausa di default finché `world_features.rpg_stats` resta `false`.** Verificare lo stato del toggle a inizio sessione se rilevante. Quando attivo: abilitare, distribuire i 25 punti, impostare il Livello, e assegnare **Species e Occupation** via API dentro `rpg_stats` (§11), perché dall'interfaccia non si salvano.
9. **Dialogue Examples: cinque**, con la disciplina di formattazione di §3. Almeno uno dovrebbe mostrare il personaggio nel suo momento peggiore o più esposto.
10. **Attitudes** secondo §16.
11. **Global Character = ON.**
12. **Verifica finale dopo reload completo della pagina, o con una GET autenticata fresca via API**: zero `{{user}}`, zero em-dash, zero asterischi, zero grassetto markdown, tutti i campi ancora presenti, RPG ancora abilitato se pertinente, Default Outfit impostato, eventuale Intimacy Profile con Entry Type Memory e Attached Character sull'id attuale. **Un salvataggio che sembra riuscito non è una prova.**
13. **Documentare nel Project** le decisioni di scrittura, gli agganci creati, le discrepanze trovate e, per le modifiche via API su più entità, i valori precedenti dei campi toccati.

---

## 15. Bug e trappole note della piattaforma

Da tenere presenti durante la lavorazione.

| Problema | Comportamento | Come conviverci |
|---|---|---|
| **Save appeso** | Il pulsante resta su "Saving..." molto spesso | Il contenuto di solito si salva comunque. Ricaricare la pagina e verificare, non ripetere il salvataggio alla cieca |
| **Species / Occupation non si salvano dall'interfaccia** | Impostati dai due combobox e salvati, dopo il reload tornano a None. **Non è un problema del modello dati:** i due campi vivono dentro `rpg_stats` e scritti lì via API persistono, sopravvivono al reload, compaiono nell'interfaccia e applicano davvero i modificatori di specie alle stat. Il difetto è nel percorso di salvataggio dell'interfaccia, che non li manda | **Scriverli via API dentro `rpg_stats`** (§11), come modifica mirata. Non lasciarli a None quando le RPG Stats sono attive: il modificatore di specie cambia le stat |
| **Livello RPG oltre ~100** | Fa fallire in silenzio tutto il blocco RPG (§8) | Tetto a 99 |
| **Outfit/array salvati insieme dall'interfaccia** | Aggiunti in un solo salvataggio si sovrascrivono a vicenda | Dall'interfaccia, uno alla volta con un salvataggio ciascuno. Via API, mandare sempre l'array completo desiderato in un solo PUT (§11) |
| **`linked-characters` 500** | `GET /api/worlds/linked-characters/<world_id>` risponde **500 "Maximum call stack size exceeded"**, cioè ricorsione infinita lato server. È la stessa area del "Failed to link character" segnalato da altri | Nessun workaround, non blocca il lavoro sulle card |
| **PUT con oggetto completo** | Risponde 200 e non scrive niente (§11) | Mandare solo i campi che cambiano |
| **Token scaduto** | GET risponde 404 e PUT 401, quindi sembra una route sbagliata | Rinfrescare il token prima di cambiare route |
| **Entry duplicate per nome e entry orfane** | Quando una card viene ricreata (nuovo `character_id`), le sue entry Lexicon collegate restano puntate al vecchio id; a volte ne nasce una seconda con lo stesso nome. L'orfana sparisce dalla lista del World ma resta leggibile per id, e l'interfaccia può salvare su una entry diversa da quella che si crede di modificare. Casi confermati il 22/09: Zeera, Ariadne Cirillo, "Vax", "The Roasted Bean" | Lavorare sempre per id; prima di modificare, confermare che l'id sia nella lista attiva del World; dopo, verificare con GET per id |
| **Ricerca Lexicon nel pannello laterale della chat** | Dà falsi negativi ("No elements match") anche per entry esistenti | Usare l'editor a pagina intera del World, oppure una GET sulla lista via API |
| **Cartelle collassate** | Si espandono **solo cliccando la chevron, il primo button della riga**. Cliccare il nome non fa nulla, nemmeno con un click reale. Una scansione che non trova righe fa credere che un personaggio sia sparito | Espandere sempre la cartella prima di concludere che una card manchi. Ha già causato un falso allarme su Dullahan. In alternativa, interrogare la lista Character via API e filtrare per nome, più affidabile |
| **Combobox** | Non rispondono agli eventi sintetici: il valore sembra impostato e poi torna indietro | Click di mouse reali, oppure apertura e navigazione da tastiera con verifica dell'elemento evidenziato prima di confermare, oppure una modifica mirata via API |
| **Textarea dell'interfaccia** | Impostare il valore via JavaScript con eventi sintetici mostra il toast di successo ma non salva; i tasti di navigazione (Backspace, Home, Ctrl+A) spesso non vengono registrati | Posizionare la selezione via JavaScript e inserire il testo con battitura reale, oppure modifica mirata via API |
| **Parent Location** | Su una Location nuova non offre opzioni finché la Location non è stata salvata almeno una volta | Salvare, riaprire, impostare il parent |
| **Prestazioni** | 40-70 secondi per operazione di pagina, oltre il timeout degli strumenti | Il lavoro di solito va a buon fine lo stesso: verificare lo stato invece di ripetere l'operazione. Per modifiche puntuali su campi già definiti, l'API mirata non soffre di questo limite |
| **`world_features.rpg_stats` disattivato** | Non è un bug, è una scelta esplicita dell'utente dopo test sul sistema di Simulation (§8) | Verificare lo stato prima di lavorare sulle RPG Stats, non riattivarlo di propria iniziativa |
| **Nessun campo `creator_notes` sul Character** | Lo schema API non lo prevede | Documentare le discrepanze nel Project (§9.2), non sulla card |

**Prima di segnalare un bug**, cercare nel forum `bugs-and-support` se esiste già (§11). Al 2026-09-07 risultano già segnalati da altri: Species/Occupation che non si salvano (patchato a giugno e poi tornato), e il "Failed to link character". Restano da segnalare: il tetto al Livello RPG, gli outfit che si sovrascrivono dall'interfaccia, il Parent Location vuoto, le cartelle che si aprono solo dalla chevron, il Save appeso, e le entry Lexicon orfane dopo la ricreazione di una card.

**Locale e sito sono entità separate.** Wyldfire, l'app desktop, ha un proprio database locale e carica su Wyvern solo con un gesto esplicito (*Publish to Wyvern*, o il sync delle chat). Modificare il locale non modifica il sito, e quello che si vede in locale può essere più vecchio di quello che c'è online. **Il sito è la sorgente di verità.** Una pubblicazione dal locale può ricreare card con id nuovi e lasciare orfane le entry collegate: dopo ogni pubblicazione da Wyldfire conviene un controllo via API delle entry con `party_conditions` o `attached_world_character_id` che puntano a id non più presenti.

---

## 16. Attitudes su ogni scheda  *(CHIARITA — ladder personalizzata è solo etichettatura)*

Fa parte della pipeline §14, come passo 10, subito dopo i Dialogue Examples.

**Regola:** ogni scheda ha almeno le Attitudes verso **Alyssa e Jasper**, che sono i due personaggi giocabili del roster "Choose Your Character". Chi non li conosce va scritto lo stesso, con il tier più basso della ladder (vedi sotto), con una motivazione che dice che non si sono mai incontrati. Sapere che due personaggi non si conoscono è informazione quanto il contrario, e senza quella riga il modello improvvisa.

Oltre a loro si mettono **solo i personaggi effettivamente citati nel background della scheda**, col tier che il testo giustifica davvero, comprese le relazioni reciproche fra Pack Leader/Council member citate nel materiale sorgente (es. co-leadership, alleanze commerciali, ostilità territoriali): se una relazione è menzionata su una scheda ma manca sul lato dell'altro personaggio coinvolto, aggiungerla anche lì. Non si inventano rapporti per riempire (§9.4).

**Come si compila una Attitude:**

1. **Target Type = World Character** ogni volta che il personaggio esiste come scheda. Il tipo **Generic (text)** serve per fazioni, gruppi e concetti, per esempio la stance verso *Humans First*, e va valutato caso per caso mentre si lavora ogni NPC, non applicato a tappeto.
2. **Tier: due livelli sovrapposti, non uno solo.** Il campo `tier` salvato dall'API usa un set di chiavi grezze e stabili di default della piattaforma (osservate sul World: `stranger`, `acquaintance`, `friend`, `close_friend`, `best_friend`, `disliked`, `despised`, `hated`, `enemy`, `rival`, `wary`, `acknowledged`, `romantic_interest`). Il World ha **già attivata** una ladder di etichette personalizzate a tema LSE (Blood Enemy, Enemy, Rival, Distrusted, Wary, Unknown Scent, Acknowledged, Trusted, Pack, Pack-bonded, Beloved), ma questa **rietichetta soltanto** le chiavi grezze in interfaccia, non le sostituisce e non introduce nuove chiavi da scrivere via API. **Conferma dell'utente, 14/09.** In pratica: scrivere via API una delle chiavi grezze osservate (es. `stranger` per "mai incontrato"), e l'interfaccia mostrerà l'etichetta personalizzata corrispondente alla sua posizione nella ladder. Non serve indovinare o inventare una stringa tipo `unknown_scent`, non esiste come chiave salvata. Non serve nemmeno rimappare le Attitudes già scritte quando la ladder personalizzata cambia, perché la chiave sottostante non cambia.
3. **Intensity**: il campo lasciato vuoto si salva come **1**, cioè il pavimento della banda, non a metà come dice la wiki. Va sempre compilato a mano. Convenzione: **15** per chi non si è mai incontrato, **50** di default per una relazione professionale ordinaria, **85** dove il rapporto *è* il personaggio, **20-25** per una conoscenza appena accennata.
4. **Reasoning**: una o due frasi che dicano da dove viene il sentimento.

**The Player (Persona) non si usa** per rapporti specifici di una persona: punta a chiunque stia giocando, quindi una motivazione scritta su Alyssa verrebbe applicata anche a chi gioca Jasper. Si usa solo per stance vere verso qualunque giocatore, tipo lo staff verso uno studente qualsiasi.

**Se in futuro si scoprisse che la ladder personalizzata NON è solo un'etichettatura** (cioè che esiste davvero un secondo set di chiavi distinto da scrivere), la nota del punto 2 va corretta e tutte le Attitudes già scritte con le chiavi grezze andrebbero rivalutate, perché la corrispondenza fra etichetta e chiave salvata sarebbe allora posizionale e sensibile a ogni modifica della ladder.

---

## 17. Lavoro in locale su database Wyldfire (SQLite)  *(SOSPESO dal 22/09)*

**Stato:** dal 22/09 questa modalità **non è più il default**. Il sito Wyvern è di nuovo la fonte di verità e il canale di lavoro (§11). Il database locale si usa solo se l'utente lo chiede esplicitamente per una fase specifica; in quel caso valgono le regole sotto, conservate per riferimento.

Motivo della sospensione: le pubblicazioni dal locale al sito hanno ricreato card con id nuovi e lasciato orfane entry Lexicon collegate (Zeera, Ariadne Cirillo), con perdita silenziosa di configurazione (`party_conditions`, `type`, Attached Character) scoperta solo giorni dopo.

**Percorso e identificatori fissi:**
- File locale di lavoro: una copia del database staged dal dispositivo dell'utente (percorso reale sul dispositivo: `C:\Users\<utente>\AppData\Roaming\com.wyvern.wyldfire\wyldfire.db`).
- `world_id` e `creator_id` del World vanno confermati a inizio sessione se non già noti, non assunti da una sessione precedente senza verifica.

**Ciclo di lavoro obbligatorio per ogni batch di scritture (solo se la modalità viene riattivata):**
1. **Backup numerato** del file `.db` prima di qualunque `UPDATE`/`INSERT`/`DELETE` (es. `wyldfire.db.backupN-<timestamp>`), mai sovrascrivere il file di lavoro senza backup precedente.
2. Scrittura tramite script Python/sqlite3, mai a mano riga per riga nell'interfaccia Wyldfire per operazioni di massa.
3. **Verifica post-scrittura programmatica**: `PRAGMA integrity_check`, più un conteggio o una query mirata che confermi il numero di righe attese.
4. **Conferma esplicita che l'app Wyldfire desktop sia chiusa** sul dispositivo dell'utente prima di sincronizzare (via domanda diretta), perché l'app tiene il proprio file aperto e una scrittura concorrente rischia di corrompere o perdere le modifiche.
5. Trasferimento del file aggiornato verso il dispositivo dell'utente, sovrascrivendo il percorso reale del database Wyldfire (con conferma esplicita di sovrascrittura, dato che è un file già esistente).
6. **Controllo che non restino file `-wal`/`-shm` residui** accanto al database sul dispositivo dopo la scrittura: la loro presenza indica una transazione non finalizzata correttamente.
7. Solo a sync completata e verificata, scrivere il documento di riepilogo nel Project, mai prima.
8. **Dopo la pubblicazione sul sito**, controllo via API delle entry orfane (§15).

Le regole di formato campo-per-campo, la logica degli array (sostituzione intera, non merge) e gli schemi dei nomi campo restano quelli di §11, applicati alle colonne SQLite corrispondenti.
