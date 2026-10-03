# Piano di integrazione: contenuti Wyldfire → World Svartúlfr (web)

Data: 22/09/2026. Analisi in **sola lettura**: nessuna scrittura sul World, nessuna modifica al database locale.

> **Aggiornamento 22/09 (seconda parte):** Lys ha risposto alle decisioni 1-4 e ha dato un'indicazione su Concierge. Le risposte e le loro conseguenze sono nella **§8** in fondo, che prevale sulle sezioni precedenti dove le contraddice. La fase 1 è stata eseguita in parte (vedi §9).

- Fonte locale: `wyldfire.db` (Wyldfire desktop), letto in modalità read-only alle 17:11.
- Fonte web: GET autenticate su `app.wyvern.chat/api/worlds/*/world/_CgYT8fHXpDC4crjmegQF7`.
- Stato web al momento dell'analisi: **364 Character, 244 Lexicon, 134 Location, 2 Environment, 9 Scenari**.

---

## 0. Avviso preliminare: il database locale è danneggiato

`PRAGMA quick_check` sul `wyldfire.db` restituisce **"database disk image is malformed"** (la tabella `app_settings` non si legge). Le tabelle di contenuto (characters, lorebooks, world_*) si leggono ancora, quindi l'analisi è completa, ma:

- **non pubblicare nulla da Wyldfire verso il sito** finché il file non è stato riparato o sostituito;
- conviene fare subito una copia del file così com'è (è l'unica copia dei contenuti importati oggi da SillyTavern);
- coerente con §17 (lavoro locale sospeso) e §15 (le pubblicazioni dal locale ricreano id e lasciano orfane).

L'integrazione proposta sotto avviene **tutta sul sito** (§11): Wyldfire serve solo come fonte da cui leggere.

---

## 1. Cosa c'è in Wyldfire (inventario)

Il database contiene cinque blocchi distinti, di natura molto diversa.

| Blocco | Contenuto | Data | Da integrare? |
|---|---|---|---|
| **A. Import SillyTavern "SvartulfrVerse"** | 3 card (Alyssa, Jasper, WorldDirector, ciascuna duplicata), 16 lorebook `st_world_svartulfrverse_*` (~100 entry), 1 persona Alyssa | oggi 17:00 | **Sì, selettivamente** |
| **B. World "Modern Fantasy"** (tuo, `_LAc42eayHQDPBm4YwAYwU`) | 33 Character, 68 Lexicon, 18 Location, 1 Environment (Chicago) | creato 21/09, sync oggi 17:05 | **Sì, con riambientazione** |
| **C. Card di terzi scaricate** | Nairene (Academy of Magic, 8 card), Kakihara (Ukiyo / Luscious / Kototama, 11 card), CrackedPepper (Archie), Tori (Concierge) + tue: Jasper AU, Zeera, Monster Cock Almanac | dic 2024 → set 2026 | In gran parte coincidono col blocco B |
| **D. Copia locale del World Svartúlfr** | 360 Char, 250 Lex, 132 Loc | ultimo sync 18/09 | **No**, è una copia vecchia |
| **E. Chat, gallery, personas** | 42 chat, 203 immagini, 5 personas Alyssa | varie | No, solo fonte di consultazione |

### Blocco D: la copia locale del World è un sottoinsieme del web

Confronto per id: **tutti i 360 Character e le 132 Location locali esistono già sul web** (il web ne ha di più: 364 e 134). Le uniche 9 entry Lexicon presenti solo in locale sono quelle **già eliminate o convertite di proposito sul sito**: Vax (doppione), Angui, Bartholomew and Madge, Vargus (ora Character), The Roasted Bean (doppione), i tre Species_Details (fusi nelle card), la ZZ DEBUG PROBE.

Conseguenza: da questa copia **non c'è nulla da recuperare**, e ripubblicarla farebbe risorgere 9 entry che avevamo tolto. È un'altra ragione per non usare *Publish to Wyvern*.

---

## 2. Blocco A: import SillyTavern "SvartulfrVerse"

È la versione SillyTavern del progetto: un "sandbox" con WorldDirector narratore, due protagonisti giocabili (i gemelli), Intimacy Profile a blocchi per la famiglia e un lorebook di mondo.

### 2.1 Conflitti con il canon attuale del web

Il materiale ST è precedente o parallelo al canon del World e lo contraddice in parecchi punti. Secondo §9 vale il canon del web salvo tua decisione diversa.

| Punto | SillyTavern | World web (canon) | Proposta |
|---|---|---|---|
| Dominio dei Douglas | "apex predator family **of Solarton**", controllano l'esercito privato e l'immobiliare della città | Blackwood City; Solarton è dominio SUCC (§10) | Tenere il web. Riscrivere ogni riferimento a Solarton come Blackwood |
| Uptown | distretto dei vampiri | distretto di Blackwood con due branchi (Cass Harrow, Naomi Black, Darius Vale) | Tenere il web; i vampiri restano a Hex Valley |
| Alyssa, altezza | 165 cm | 155 cm | Web |
| Alyssa, sangue | Pureblood | Founding Bloodline, Dominant Omega | Web |
| Alyssa, tatuaggio | girasole sulla caviglia destra | Gebo sul polso sinistro | Web; il girasole è un possibile dettaglio in più, solo se lo vuoi |
| Alyssa, braccialetto di pietra di luna | "always wears" | non presente | Solo come outfit contestuale (§4), mai costante |
| Alyssa, studi | Pre-med, Neuropsichiatria, GPA 3.8 | Pre-Med | Neuropsichiatria compatibile: decidi tu se aggiungerla |
| Jasper, aspetto | capelli scuri, undercut, occhiaie | capelli castano caramello, occhi verde menta | Web (le occhiaie da insonnia sono compatibili) |
| Jasper, corso | Computer Science | Engineering | Web |
| Jasper, colpa per la morte di Nixara | tema centrale ("l'ha uccisa esistendo") | nato lo stesso giorno, tema non centrale | Da decidere: può entrare come ferita privata di Jasper, non come fatto di famiglia |
| Pranzo della domenica | domenica **27 agosto** | memory **2024-08-25** (nel 2024 il 25 è domenica) | Web: 25 agosto |
| Scarlett | "Scarlett O'Hara" | **Scarlett Rose** | Rinominare nell'import |
| Angel Moreno | "Angel Moreno", gender-fluid | **Angelo Moreno**, vampiro del 1484, Eidolon Creative | Rinominare; tenere la caratterizzazione del web |
| Sierra | "Sierra Axelrod", stress accademico | **Sierra Cruz**, lamia, Necromanzia applicata | Rinominare; "Axelrod" da scartare |
| Kaladin | "Director" di DCC Security | Commander, DCC Security Division | Web |
| Marcus Thornfield | bodyguard DCC dei gemelli | Field Lead, Vanguard Security | Web; il ruolo di scorta ai gemelli è compatibile |

### 2.2 Cosa portare, cosa no

**Da integrare (valore reale, oggi assente sul web):**

1. **Intimacy Profile di Alyssa, Jasper e Wulfnic.** Sul web mancano del tutto (esistono solo Erik, Logan, Malachia, Noah). Le fonti ST sono già nel registro a blocchi (Baseline, Trauma Map, Body Reactions, Vulnerability Shape, Voice, Hard Limits) che §13 ammette. Tre entry nuove, formato §13: `type: memory`, Attached Character, `party_conditions has_any` sul proprietario, `is_global: true`. Da ripulire: em-dash, braccialetto "sempre" (Alyssa), dettagli in conflitto con la tabella sopra.
2. **Intimacy Profile di Erik, Logan, Malachia, Noah: fusione, non sostituzione.** Il web ha già questi quattro profili (Erik 3640 caratteri a blocchi, Noah 1260 in prosa). Dall'ST si prende solo ciò che manca, soprattutto la **Trauma Map** e le Hard Limits, e si aggiunge in coda. Serve un confronto voce per voce prima di scrivere.
3. **Intimacy Profile di Angelo Moreno, Scarlett Rose, Sierra Cruz, Marcus Thornfield, Kaladin Nargathon** (dall'NPC Intimacy Roster). Oggi assenti sul web. Il materiale ST è corto e scritto per `{{user}}` (5 occorrenze, 100 asterischi di markdown): va **riscritto** in prosa senza destinatario, con i nomi del web. Kaladin e Marcus sono scritti come predatori con fearplay: tenere solo ciò che è consenso esplicito fra adulti.
4. **"The Golden Cage" (sorveglianza biometrica).** Concetto forte e coerente con Erik iperprotettivo, oggi non scritto sul World: orologi PMC con tracker biometrico, battito e posizione inviati a DCC Security, jammer di Logan alla Verve come unica zona cieca, script di Jasper che falsificano il segnale. Candidato a Lexicon `lore/concept`. **Decisione tua:** è canon o era una meccanica del sandbox ST?
5. **Jammer di Logan alla Verve / Jasper che hackera la rete di famiglia.** Dettagli di carattere da aggiungere alle card di Logan e Jasper se accetti il punto 4.
6. **Greeting del pranzo della domenica** (primo messaggio del WorldDirector). Ottimo testo di apertura: può diventare alternate greeting di uno Scenario esistente o di uno nuovo "Il pranzo prima della SUCC", corretto al 25 agosto, senza `{{user}}` e senza corsivi `_..._`.
7. **Voice Fingerprints dei personaggi** (dal WorldDirector): riscontro utile per i campi `summary` di Marcus, Kaladin, Scarlett, Angelo, Sierra; solo dove non contraddicono il web.

**Da non importare:**

- **Card WorldDirector.** In un World il narratore è la piattaforma stessa; le sue "Standing Goals" per Erik, Malachia, Noah, Wulfnic, Logan si possono trasferire come righe di comportamento nelle rispettive card, se le vuoi.
- **Card Alyssa e Jasper ST** (duplicate, versioni ridotte e in conflitto): le card web sono molto più complete. Si recuperano solo i dettagli puntuali approvati sopra.
- **Protagonist Lorebook**: è interamente `{{user}}` (§13).
- **The Engine (Economy & Polarity)** e **WORLD_PULSE**: meccaniche da sandbox scritte su `{{user}}`. Wyvern ha i propri sistemi (Relationships attivo, il resto spento dal 13/09). Al massimo una riga nelle istruzioni del World, e solo se me lo chiedi (le impostazioni del World non si toccano via API senza richiesta esplicita, §11).
- **Sandbox Intimacy Register**: regole globali di scrittura dell'intimità. Contiene due punti in conflitto con le schede web ("non ammorbidire Erik e Wulfnic, niente aftercare" contro il profilo web di Erik che ha una sezione Aftermath) e ruota tutto attorno al sandbox. Da non portare come entry; eventuali principi, se li vuoi, vanno discussi a parte.
- **World Lorebook, voci descrittive** (Douglas family, DCC Security, Verve, Seven Hills, SUCC, Pureblood, Vampires): il web copre già tutto con entry più ricche; le versioni ST sono in conflitto sul dominio (Solarton).
- **Lorebook Alyssa/Jasper (descrizione fisica, psicologia, relazioni)**: già coperti dalle card web.

---

## 3. Blocco B + C: World "Modern Fantasy" e card di terzi

È un'altra ambientazione: Chicago anni 2020, il velo è caduto dopo l'era nucleare, Outsiders, Dungeon, Gilde, Hunter con ranking, mana. Le card sono di **Nairene** (Evirein Academy of Magic) e **Kakihara** (Ukiyo / Luscious / Kototama), più alcune tue.

### 3.1 Già sul web (non ricreare)

Barrow, Marek, Zeera, Rev, Vargus "The Red", Allegra (come Allegra Lumsden), Brak Ironfist e Huck (da fonti affini), Asag Beast (Lexicon creature), Horned Skull Caverns, Sarrow, Vax, Vax - Reproduction, Reality Tears, Demi-humans, Demons, Fae, Human, Hybrids, Magic-capable Humans, Undead, Vampire, Weres/Shapeshifters, SRF, Jasper's Porsche.

Il precedente di lavoro è chiaro (Barrow, Marek, Zeera): **riambientazione a Blackwood** (The Horns a Dockside, Ironworks), JED+, arco `{{user}}` escluso integralmente, Intimacy Profile separato.

### 3.2 Assenti dal web: 28 personaggi

Quasi tutte le card hanno un arco costruito su `{{user}}` (da 5 a 39 occorrenze): per ognuna vale §13 per intero.

**Gruppo 1: Evirein Academy of Magic (Nairene), 8 schede.** Rector Zaire Ziisis (drago), Prof. Xaiden Nershatar (demone dell'Abisso, magia da combattimento), Lestat Oreven (principe ereditario), Caien Vaelion (elfo, negromante), Aeril Royen (tritone), Amerian de Vian (drow, infiltrato), Ashton Crowley (illusionista rivale), più la card-narratore "Academy of Magic".
Proposta armoniosa: **CUMS (California University of Magical Sciences)**, che esiste già sul web come rivale della SUCC. Evirein diventa facoltà, programma o nome di un college interno alla CUMS; Zaire ne è il rettore, Xaiden un professore. Regni come Ishu o la città sottomarina di Silverin diventano luoghi d'origine oltre un Reality Tear, cioè Otherworlders. Nota di dominio: la CUMS appartiene all'ambientazione SUCC, ma l'autore ha dato via libera alle fan OC (§10). Serve una decisione tua.

**Gruppo 2: Ukiyo / Luscious / Kototama (Kakihara), 15 schede.** Azura, Danya, Eithne Dal'Kereth (dark elf, underboss degli Obsidian Blades), Esmée Villeneuve, Ilévra De'solora, Jaelyn, Neve, Raksha, Zosia, Radek / Goran / Kian (trio di orchi hunter), Bessie May, Fianna MacTire, Tsukiyo Yamazaki (vampira, New York).
Proposta: stessa strada di Barrow e Marek, cioè residenti di Blackwood (The Horns, Ironworks, Dockside). Eithne e gli Obsidian Blades si agganciano agli Ironhorn Nomads già citati sulla card di Marek. Radek, Goran e Kian si possono accorpare in un'unica entry Lexicon "crew" (§7, gruppo fuori scena), da scorporare solo se entrano in scena.

**Gruppo 3: schede "leggere" del World Modern Fantasy (senza long_summary), 6 schede.** Yael (Head of Hunters dell'Horned Skull Clan di Zeera), Oberon (re degli elfi e dei fatati), Warchief Thrakgor Deathspine, Wren Lark (Sarrow), Finn (satiro, amico di Barrow), Bryson (Monster Cock Almanac).
Yael, Finn e Wren sono già agganciati a schede esistenti (Zeera, Barrow, Sarrow e Vax sul web): candidati naturali. Oberon e Thrakgor sono sovrani di regni fantasy e non hanno un posto ovvio in California: al massimo Lexicon come figure oltre i Reality Tears.

**Da escludere o rimandare:**
- **Concierge: Day Rate** (Tori): premessa interamente erotica su `{{user}}` che "ha bisogno di soldi" e un'assunzione con esami medici. Esclusione integrale per §13 (estensione del 14/09).
- **Archie • Sticky Fingers** (CrackedPepper): omicida devoto a `{{user}}`; riusabile solo come personaggio nuovo quasi da zero. Rimandare.
- **Jasper AU (Mezzelfo, St. Brugge)**: è una tua versione alternativa di Jasper. **Non va fusa** con il Jasper canon; al massimo diventa materiale per uno scenario "universo alternativo" futuro, come quelli già previsti (§7).

### 3.3 Lexicon del World Modern Fantasy assenti dal web (circa 50 voci)

| Categoria | Voci | Proposta |
|---|---|---|
| Sistema "Hunter & Dungeon" | Dungeons, Dungeon Cores, Guilds, Hunters & Ranking System, Rank A, The Dungeon Management & Hunter Authority, DMHA, Training & Origin, Otherworlders, Cyber-rogue | **Decisione chiave** (vedi §5). Se sì: Lexicon `lore/concept` ridenominate per Blackwood, con la Hunter Authority collegata alla SRF già esistente |
| Magia e mana | Mana Crash, Mana Source / Limitless Energy, I'th Gôlvadol, Reflecting Barrier, Voice of the Forest, Potions & Recovery | `lore/concept`; da confrontare con le regole di magia SUCC (dominio esterno) |
| Specie | Minotaurs & Dragonid, Naga Species & Anatomy, Orc Compatibility, Ice Satyrs, Satyr Pheromones, Horned Skull Clan, Vax Species & Factions, Minotaur Cultural Taboo (x2) | Panoramica di specie → `lore/concept` globale; la parte anatomica e riproduttiva → entry `memory` separata, `is_global: false` (§7). Vax Species & Factions va **fusa** in "Vax" esistente, non duplicata |
| Fazioni | Ironhorn Nomads MC & The Underworld | `organization/faction`. Attenzione: "The Underworld" è anche il nome dell'ambientazione di Los Angeles (dominio esterno). Serve un nome che non si confonda |
| Oggetti | Dimensional Bag, Dragon Glass Katana, Monster Cock Almanac | `item`; l'Almanac è tuo e ha un registro esplicito, da trattare come contenuto intimo separato |
| **Fenris Trauma (Lycanthrope Only)** | 1 voce | **Attenzione:** tocca Fenris, cioè il cuore del canon LSE/Blackwood. Va letta e confrontata con "La Guerra di Fenris e l'Esilio dei Firstborn" prima di decidere qualunque cosa |
| Memorie di chat (Alyssa, Jasper, Barrow, Team Ukiyo) | una ventina di voci: Alyssa's Field Researcher Offer, Combat Demonstration, Heritage Reveal, Jasper's Alias, Paranoia and Fortifications, Barrow's Dinner Visit, Team Ukiyo Recruitment… | **Non importare.** Sono ricordi di giocate nell'AU di Chicago e contraddicono il canon (Alyssa ricercatrice sul campo, Jasper orfano mezzelfo) |

### 3.4 Location del World Modern Fantasy (18)

Tutte legate a Chicago o a regni fantasy (Apartment C, Cable District, Diner del Sud, Magic Chicago, Evirein Academy, Silver Marshes, Crystal Caves, St. Brugge Orphanage, Veilfall, The Void…). Nessuna esiste sul web. Proposta: **non importarle come Location**. Si ricreano solo quelle che servono ai personaggi riambientati (per esempio Evirein come parte della CUMS, un locale per Eithne a Blackwood), costruite da zero sulla mappa esistente. I regni oltre i Reality Tears, se servono, diventano Lexicon.

---

## 4. Anomalie trovate sul web durante il confronto

Non richieste, ma emerse dall'analisi. Nessuna è stata corretta.

1. **"Valentine Rossfeld" duplicato**: due Character (`_h6kHQzhwqr89D2q8hCWGf`, `_emkLFpkNL2q2EzWbqd3XT`), entrambi con `long_summary` vuoto.
2. **"Intimacy Profile - Jean-Luc Virtuoso" duplicato**: `_M9jgVAFHHMJhYXUcgmhcG` (744 caratteri) e `_n7zrhF94htP72dqE1xmwV` (2148), stesso Attached Character, **entrambi senza `party_conditions`** (§13 le richiede).
3. **"Intimacy Profile - Dante" duplicato**: `_Padg7gBCkypyY9wVhWV1L` (804) e `_BMADq7QK8eUxEXVh37x7E` (2852), stessa situazione.
4. Nessuna entry orfana: tutti gli `attached_world_character_id` e i `party_conditions` puntano a id presenti nella lista attiva.

Proposta: unire i due profili di Jean-Luc e i due di Dante nella versione più lunga e aggiungere `party_conditions`. Per Valentine, decidere quale tenere. Le cancellazioni solo su tua richiesta esplicita, una per chiamata, con backup nel Project (§11).

---

## 5. Decisioni che servono da te prima di scrivere

1. **Hunter, Dungeon e Gilde entrano nel canon di Blackwood?** È la scelta che decide metà del blocco B. Tre strade:
   - (a) **Sì, con riambientazione**: i dungeon nascono dai Reality Tears, la Hunter Authority è un ufficio civile collegato alla SRF, gli Otherworlders sono chi arriva da oltre il velo;
   - (b) **Solo i personaggi, senza il sistema**: gli hunter diventano mercenari, contractor, buttafuori; niente dungeon;
   - (c) **Il sistema resta un AU separato**, come lo scenario del 2499: niente di tutto questo nel presente del 2024.
2. **Evirein Academy dentro la CUMS?** Oppure un'istituzione a sé, fuori dal dominio SUCC?
3. **The Golden Cage è canon?** Se sì, diventa Lexicon e tocca le card di Erik, Jasper, Logan, Kaladin e Marcus.
4. **La colpa di Jasper per la morte di Nixara**: ferita privata sì o no?
5. **Priorità fra i 28 personaggi nuovi**: tutti, oppure un primo lotto (per esempio Yael, Finn, Eithne, Zaire, Xaiden)?
6. **Anomalie §4**: le sistemo in questa fase?

---

## 6. Piano di esecuzione (dopo le tue risposte)

Tutto sul sito: interfaccia per la scrittura estesa, API solo per letture e modifiche mirate (§11). Snapshot prima di ogni scrittura, id e mai nomi, verifica con GET fresca, riepilogo nel Project a ogni fase.

| Fase | Contenuto | Entità | Tipo di operazione |
|---|---|---|---|
| **0. Messa in sicurezza** | Backup del `wyldfire.db` così com'è; nessun Publish da Wyldfire | 0 | locale, solo copia |
| **1. Famiglia: Intimacy Profile** | Nuovi: Alyssa, Jasper, Wulfnic. Fusione (Trauma Map e Hard Limits): Erik, Logan, Malachia, Noah | 3 creazioni + 4 modifiche | POST + PUT parziale del solo `content` |
| **2. NPC: Intimacy Profile** | Angelo Moreno, Scarlett Rose, Sierra Cruz, Marcus Thornfield, Kaladin Nargathon, riscritti senza `{{user}}` | 5 creazioni | POST |
| **3. Golden Cage** (se approvato) | 1 Lexicon + righe sulle card di Erik, Jasper, Logan, Kaladin, Marcus + greeting del pranzo | 1 + 5 + 1 | POST + PUT parziali in append |
| **4. Lexicon di specie e magia** | Circa 20 voci dal blocco B, secondo la scelta 5.1; fusione di "Vax Species & Factions" in "Vax" | ~20 (piano per lotti, max 25) | POST |
| **5. Personaggi, lotto 1** | 5-6 schede con aggancio già esistente (Yael, Finn, Wren Lark, Eithne, più due da scegliere) con pipeline §14 completa | 5-6 | POST + interfaccia |
| **6. Personaggi, lotti successivi** | Academy of Magic (8), Ukiyo / Luscious (circa 15), secondo le risposte 5.1 e 5.2 | fino a 20 | come sopra, un lotto per sessione |
| **7. Anomalie** (se approvato) | Unione degli Intimacy Profile duplicati, scelta su Valentine Rossfeld | 3-5 | PUT parziali; DELETE solo su tua conferma |
| **8. Verifica globale** | Zero `{{user}}`, zero em-dash, zero asterischi o grassetto nei testi toccati; Attached Character e `party_conditions` sugli id attuali; nessun duplicato per nome | tutte | GET |

Stima: le fasi 1-3 stanno in una sessione; la 4 in una; ogni lotto di personaggi con pipeline completa richiede una sessione propria.

---

## 7. Fonti lette

- `wyldfire.db`, tabelle `characters`, `lorebooks`, `worlds`, `world_characters`, `world_lexicon_entries`, `world_locations`, `world_environments`, `chats`, `personas` (sola lettura).
- API Wyvern: liste `characters`, `lexicon`, `locations`, `environments`, `scenarios` del World `_CgYT8fHXpDC4crjmegQF7`; card singole di Alyssa, Jasper, Erik, Edric, Kaladin, Marcus Thornfield, Scarlett Rose, Angelo Moreno, Sierra Cruz; Lexicon Intimacy Profile - Erik / Noah, DCC, BLOODHOUND PMC.
- Documenti del Project per i precedenti: Barrow_Demihuman_Representative_2026-09-14, Marek_Zeera_Brak_Huck_Ut_Ariadne_Completamento_2026-09-22, Lexicon_Sweep_Anomalie_Risolte_2026-09-22.

---

## 8. Decisioni di Lys (22/09) e loro conseguenze

### 8.1 Hunter / Dungeon / Otherworld: fusione tramite i Reality Tears

**Decisione:** l'Otherworld del World Modern Fantasy si gestisce come un **Reality Tear del DDM**, cioè un portale fra due universi, **dentro la Blackwood Forest, sorvegliato dai Bloodmoon**. Questo dà a Dullahan una ragione per restare: sorvegliare questi "dungeon", cioè gli strappi che si aprono nel mondo.

**Perché regge col canon già scritto (nessuna contraddizione, solo sviluppo):**
- La Lexicon "Reality Tears" dice già che una realtà che si è strappata una volta è più esposta a strapparsi di nuovo, e chiude con: *se questo mondo si è già strappato prima, a nessuno qui è stato detto*. La fusione risponde a quella domanda aperta: sì, e sempre nello stesso posto.
- La card di Dullahan dice già che la DDM gli ha concesso la proroga **a condizione che continuasse a fare lavoro da Contractor**. Il lavoro è questo.
- La Blackwood Forest e il Bloodmoon Pack Territory sono già scritti come zona a **densità magica così alta che la tecnologia smette di funzionare** (la dead zone). È il luogo più plausibile in cui la trama della realtà ceda, ed è già dominio dei Firstborn.
- Il dominio DDM (§10) resta intatto: la meccanica dei Tears, i Tier, la Euclidean Division restano materiale DDM. Cambia solo cosa succede su suolo californiano, che è dominio Blackwood.

**Proposta di design (da confermare prima di scrivere sul World, §9.7):**

| Elemento Modern Fantasy | Traduzione Blackwood |
|---|---|
| Veilfall / la caduta del velo | Nessun evento globale. Un **sito di strappo ricorrente** nel cuore della Blackwood Forest, noto a pochissimi |
| Dungeon | **Tear stabilizzato**: uno strappo che non si chiude del tutto e si ripiega in una sacca di spazio semi-chiusa, con fisica alterata e creature. "Dungeon" è il gergo di chi ci entra; nei file DDM è un Tier 1-2 persistente |
| Dungeon Break | Il Tear che si riapre del tutto e riversa creature nella foresta. È ciò che i Bloodmoon esistono per impedire |
| Dungeon Core / Mana Crystal | Materiale condensato che resta dopo la chiusura di una sacca. Valore enorme, mercato grigio. Aggancio naturale alla DCC (import/export, §8.3) |
| Otherworlders | Chi è arrivato attraverso un Tear e non è tornato indietro. I personaggi Ukiyo e Academy di origine non terrestre entrano così |
| Hunters | Chi entra nelle sacche per ripulirle. **Non esiste un sistema nazionale di licenze**: sarebbe in conflitto con la SRF e con lo status civile scritto dal materiale SUCC. Proposta: squadre private a contratto, autorizzate dai Bloodmoon ad attraversare il loro territorio |
| DMHA / Guilds / Rank F-S | Da scartare come istituzioni. Il ranking, se serve, diventa una **scala interna dei Bloodmoon** per chi può entrare (con un nome norreno) |
| Guardiani | I Bloodmoon: Wulfnic, Ut, Zefir e il Bloodmoon Pack. La dead zone rende cieca anche la DCC, quindi sul Tear i Douglas non hanno voce: è il punto in cui "un Bloodmoon può ancora dire di no a un Douglas" |
| DDM | Dullahan tiene d'occhio il sito per conto della Euclidean Division. I Bloodmoon sanno che c'è; quanto sappiano di **cosa** sia è una scelta tua |

Voci del Project da aggiornare di conseguenza (dopo conferma): la riga "RELEVANCE TO THIS WORLD" di **Reality Tears** e di **DDM Inc. (The Company)**, la nota finale di **Contractors** ("not here on Company business"), e la sezione THE TWO JOBS di **Dullahan**. Tutte con append mirato, non riscrittura.

**Escluso integralmente, a prescindere dalla fusione:** la Lexicon **"Fenris Trauma (Lycanthrope Only)"** del World Modern Fantasy. Descrive la prigionia e l'abuso sessuale di una sedicenne da parte di Fenris. Non entra nel World in nessuna forma, nemmeno riscritta, e contraddice comunque il canon di Fenris come divinità fondatrice. Stessa sorte per le voci **"Mana Source"** e **"Training & Origin"** nella parte che riguarda `{{user}}` (orfanotrofio St. Brugge, 125 anni da elfa): sono l'AU di Alyssa, non il canon.

### 8.2 Academy of Magic dentro la CUMS

**Confermato.** Evirein diventa parte della California University of Magical Sciences. I personaggi di origine fantasy (Lestat, Aeril, Amerian, Zaire, Xaiden) sono Otherworlders arrivati da un Tear e accolti dalla CUMS. Resta da decidere se Evirein è un college interno, un programma speciale o il nome dell'edificio.

### 8.3 Golden Cage: non canon; la tecnologia sì, come prodotto DCC

**Decisione:** la sorveglianza biometrica sui gemelli non è più canon. Le tecnologie citate restano, ma come **mercato della DCC**: vendita di sistemi di sorveglianza avanzata e di servizi di sicurezza, più l'import/export gestito dalla Security Division.

**Eseguito:** append alla Lexicon "Douglas Commercial Coalition (DCC)" (vedi §9).
**Non si importa:** la entry ST "The Golden Cage", i trigger di sorveglianza nei profili ST, il WORLD_PULSE.

### 8.4 Jasper: ribelle vivace, più musica, meno paranoia

**Decisione:** niente colpa per la morte di Nixara come tema; Jasper è il classico ribelle, puntato sul suo essere DJ.
**Eseguito:** Intimacy Profile di Jasper scritto su questa linea (vedi §9).
**Da valutare:** la card di Jasper sul web (14.915 caratteri) ha ancora un'impronta "hacktivist" forte (PROFESSION: Hacktivist / Underground DJ; NICHE: bypassing DCC grids; "the hacker and unseen nervous system of the pack"). Proposta: invertire il peso, DJ prima e hacker come abilità secondaria, e togliere il riferimento alle griglie DCC da eludere, visto che la Golden Cage non è più canon. Serve un tuo ok, perché tocca il personaggio giocabile.

### 8.5 Concierge → app di HSK Consulting

**Indicazione di Lys:** Concierge diventa l'IA dell'app di **HSK Consulting** (la società di Zeera, già così sul web), usata per gestire gli incarichi del personale. Interfaccia minimale e clinica, sfondo nero e testo bianco, voce sterile quasi militare, dettagli precisi su luogo, abbigliamento richiesto ed extra. HSK è stata ingaggiata da **MF Inc.** per selezione e colloqui del nuovo personale, con Zeera come intervistatore principale di Alyssa. La **Aetheris Clinic** (Unit 4B, Central Medical District) è la sede delle valutazioni fisiche e sanitarie iniziali di HSK.

**Come lo costruisco:**
- **HSK Concierge**: Lexicon `item` (o `lore/concept`), con la voce e il formato dei messaggi dell'app. Il personaggio "CONCIERGE" non diventa un Character.
- **Aetheris Clinic**: Location.
- Della card originale (Tori) si prende **solo l'estetica** (l'app, il tono). La premessa della card originale, cioè un lavoro a giornata erotico per chi ha bisogno di soldi e un'assunzione fatta di settimane di esami medici, **non viene portata** (§13, estensione del 14/09).

**Cosa manca per scrivere:**
- **MF Inc.** non esiste sul web. Che cos'è? L'unico aggancio nelle fonti è l'offerta di lavoro ad Alyssa come ricercatrice sul campo per la biologia delle specie non umane (World Modern Fantasy). Con la fusione, può essere una società di ricerca sugli Otherworlders arrivati dai Tears.
- **Central Medical District** non è un distretto di Blackwood. Blackwood ha Ironworks, Paradise, Bluemoon, Uptown, Oldtown, Dockside e Arcadia. Proposta: la clinica sta in uno di questi (Paradise o Uptown) e "Central Medical District" diventa il nome della zona sanitaria dentro quel distretto.
- **Il colloquio di Alyssa con Zeera** è canon del 2024, uno scenario o un evento futuro? Alyssa nel World è una matricola pre-med dal 26/08/2024, e il world_age è il 5 aprile 2024.

---

## 9. Registro esecuzione, fase 1 (22/09)

Tutto via API, body parziali, verifica con GET fresca per id e presenza nella lista attiva del World (Lexicon: da 244 a 247).

### 9.1 Creati

| Entry | id | Attached Character | Note |
|---|---|---|---|
| Intimacy Profile - Alyssa | `_VkA6QajVPaWh8wNLbDCHR` | Alyssa Douglas Bloodmoon `_MXcEC8Y6B3BNm3b1ttHj6` | Da ST. Tolti: braccialetto "sempre" (§4), "completely hairless", riferimenti alla sorveglianza. Aggiunto: hard limit di famiglia come sugli altri profili |
| Intimacy Profile - Jasper | `_GTdaeQdfMUmhpKjMqTDyV` | Jasper Douglas Bloodmoon `_x3VY2kcbaDbKyCqywGeET` | Riscritto secondo §8.4. Tolti: colpa per Nixara, cyber-war contro la famiglia, trigger di sorveglianza, messaggio BLACKROOM, capelli e occhi scuri (canon: 193cm, occhi verde menta). Aggiunto: hard limit di famiglia |
| Intimacy Profile - Wulfnic | `_fL92qtekGWP794CqyryCH` | Wulfnic Bloodmoon `_W9PLYt9ERTBJBXqKQL2en` | Da ST, con due correzioni. **Rimossa** la reazione "sovrascrive il partner con l'aura Enigma, forzandone la sottomissione biologica" (coercizione, §13): ora tiene l'aura al guinzaglio e chiude l'incontro con distanza. **Corretto** "il suo amore è morto con la figlia secoli fa": Nixara è morta nel 2005 |

Formato di tutte e tre (§13): `type: memory`, `is_global: true`, `keys: [<Nome>]`, `secondary_keys` standard (7), `key_logic: AND_ANY`, `priority: 100`, `party_conditions has_any` sull'id attuale, Attached Character sullo stesso id. Controllo automatico: zero em-dash, zero asterischi, zero `{{user}}`.

### 9.2 Modificati (append, valori precedenti sotto)

**Intimacy Profile - Logan** `_MRrxBA3z2RqUtnHWRLNdQ` (2168 → 2574 caratteri). Dall'ST, solo ciò che è compatibile col profilo web: un secondo modo in cui cade la guardia (farsi curare, le mani lavate dal grasso), la voce (sweetheart, darlin', il ringhio), e "a partner riding him" fra gli Hard Yes.

Valore precedente:
```
Logan_INTIMACY_BASELINE: Heterosexual Beta. Grounded, practical, unpretentious, no performative dominance, just genuine physical release combined with quiet affection. Wants a partner he can relax with after a long day in the garage.
Logan_TRAUMA_MAP: Deeply insecure about being 'just a Beta' in a family of Prime Alphas. If a partner compares him unfavorably to the Alphas or implies he isn't enough, he shuts down emotionally and physically distances himself.
Logan_BODY_REACTIONS: 198cm of grounded Beta muscle built from decades of mechanical labor, calloused hands, grease-stained forearms, broad shoulders that have never needed to posture for dominance. Warm and solid, shaped by labor rather than ritual. Takes a long time to build arousal but holds reliably. When aroused, his breathing slows and deepens, his amber eyes go soft and unfocused, his hands shift from tool precision to gentle exploration. He makes quiet, practical sounds and checks in with short grounded words. Uses his weight like a blanket, anchoring rather than pinning. Deepens rhythm rather than changing it when close to climax, finishing with the same uncomplicated certainty he brings to everything else.
Logan_VULNERABILITY_SHAPE: Falls asleep almost immediately after climax, completely dropping the vigilant 'middle child' responsibility he constantly carries for the pack, the deepest trust he has.
Logan_VOICE_IN_INTIMACY: Quiet, practical check-ins ('You good?', 'Like that?'). Doesn't talk much, lets his hands and body language communicate.
Logan_HARD_LIMITS_AND_HARD_YESES: Hard Limit: STRICTLY NON-APPLICABLE with any member of his own family, absolute sibling/family boundary. Also hard-limits drama, mind games, or performative dominance. Hard Yes: simple, uncomplicated physical connection, oil, sweat, and skin.
Logan_AFTERMATH: Cleans himself with a shop rag immediately, offers one to his partner as if it's just another maintenance chore. Smokes a cigarette bare-chested in the garage doorway. Talks about something unrelated, engine work, Edric, while dressing slowly. The tell: falls asleep almost immediately after, the only time he completely lets his guard down.
```

**Douglas Commercial Coalition (DCC)** `_K4bmN3tGC8ExmTgLYRD4z` (1480 → 2034 caratteri). Aggiunto il punto "4. SICUREZZA COME PRODOTTO (oggi)" secondo §8.3, con la nota che nella dead zone la tecnologia DCC non funziona. Il testo precedente è rimasto invariato; il valore precedente è il testo attuale **senza** il paragrafo 4 finale.

### 9.3 Non fatto, e perché

- **Fusione degli Intimacy Profile di Erik, Malachia e Noah:** non eseguita. Le versioni ST **contraddicono** i profili web, che sono canon e sono stati lavorati il 20-21/09. Erik ST è freddo, senza baci né aftercare, mentre sul web è un seduttore caldo, con una sezione Aftermath. Malachia ST è silenzioso, mentre sul web è rumoroso e volgare. Noah ST è un service dom manipolatore, mentre sul web è uno switch golden boy. Le Trauma Map che il piano pensava mancanti **ci sono già** su Erik, Logan e Malachia. Da ST non c'è nulla da aggiungere senza cambiare i personaggi.
- **Anomalia nuova, non corretta:** "Intimacy Profile - Erik" (`_CtajjVcfWzKqxAg78TRR3`) **non ha `party_conditions`** e ha chiavi primarie generiche (`Erik, intimacy, mate, partner`, `key_logic: AND_ANY`, secondarie vuote). Per §7 si accende in qualunque scena che nomini "intimacy" o "partner", anche senza Erik. Correzione proposta: `keys: ["Erik"]`, le 7 secondarie standard, `party_conditions has_any` su `_d44gDc8N18kkbEhAcfUCG`.
- **Fase 2 (Intimacy Profile NPC):** non iniziata.

---

## 10. Seconda tornata di decisioni (22/09, sera) ed esecuzione

### 10.1 Decisioni di Lys

1. Tutto ciò che nel World Modern Fantasy sta a **Chicago si sposta a Blackwood**.
2. **Lo strappo è avvenuto durante la guerra fra Fenris e gli dei norreni**, quando furono creati i Nove Firstborn.
3. **Dullahan è in congedo.** La DDM non lascia nulla al caso: lo ha mandato in congedo in un luogo che ha bisogno di sorveglianza passiva, sapendo che se l'equilibrio salta ha già un uomo sul posto da attivare.
4. **La Aetheris Clinic sta a Uptown.**
5. Il colloquio di Alyssa con Zeera per HSK è uno **Scenario opzionale**, da aggiungere ai 9 esistenti.
6. **Il Gebo sul polso ce l'hanno sia Alyssa sia Jasper**, fatto insieme di nascosto a 18 anni.
7. **DCC:** la società madre fa import/export e trasporti, erede della compagnia navale del 1600. Nel tempo sono nate divisioni con compiti e mercati propri: DCC Security (sistemi di sicurezza e sorveglianza), DCC Financial (azioni, compravendita di immobili e aziende), e altre.
8. **Logan non è del tutto fuori dalla DCC:** ne prende una parte dei dividendi e dirige la divisione **Black Market**. È una divisione fantasma che gestisce i servizi più delicati per le esigenze dei soprannaturali, come il commercio di sangue e di organi.
9. **La "card di Fenris" è la base per la divinità** della nostra ambientazione.

### 10.2 Eseguito (via API, verificato con GET per id)

| Entità | id | Modifica |
|---|---|---|
| Lexicon DCC | `_K4bmN3tGC8ExmTgLYRD4z` | Il punto 4 scritto nella tornata precedente è stato **sostituito** da "4. STRUTTURA ATTUALE": nucleo import/export e trasporti, DCC Security, DCC Financial, DCC Black Market (diretta da Logan, conoscenza limitata), altre divisioni, limite della dead zone (2034 → 2546) |
| Card Logan Douglas | `_JL37wK9PQMNDChULCDrWj` | OCCUPATION e BACKSTORY: ha lasciato la sala riunioni, non la famiglia; prende i dividendi; dirige DCC Black Market e la tiene lontana dal garage (in coerenza col suo tabù "bringing DCC business into his garage", che resta) |
| Card Alyssa | `_MXcEC8Y6B3BNm3b1ttHj6` | Gebo: "the twin of Jasper's, done together in secret at eighteen" |
| Card Jasper | `_x3VY2kcbaDbKyCqywGeET` | "Magical protection tattoo on left wrist" → "(Gebo) … the twin of Alyssa's, done together in secret at eighteen" |
| Card Dullahan | `_F8ee4UpyLr7Fyr69KKhzV` | Il paragrafo "He came to this universe on a job… ends well." è stato sostituito dalla versione del congedo voluto dalla DDM (sorveglianza passiva, uomo sul posto da attivare). Tolto "There was a tear. He sealed it." |
| Lexicon Reality Tears | `_qH1AX7TU2XyJGPGjMpU9m` | RELEVANCE: la realtà è nella watchlist DDM, si è strappata una volta tanto tempo fa e la cicatrice non si è mai chiusa; #04 in congedo come sorveglianza passiva |
| Lexicon DDM Inc. | `_QNJdCq9fYQ46mRPdNhcVq` | RELEVANCE riscritta nello stesso senso |
| Lexicon Contractors | `_CwEeRpbLpbfMcQ3wngaJp` | NOTE: "officially on leave, and the Company chose where he would spend it" |
| **Nuova** Location Aetheris Clinic | `_8mEgKeWWt4hP1M1AYMQPW` | Parent: Uptown. Unit 4B, Central Medical District (la zona sanitaria di Uptown); valutazioni fisiche e sanitarie iniziali di HSK |
| **Nuova** Lexicon HSK Concierge (app) | `_j6edMUgQ2p8R8MRhqCU2z` | `lore/concept`, globale. Estetica e voce dell'app come descritte da Lys; **nessuna** premessa della card originale |

Nota: i testi della DDM parlano volutamente di uno strappo "long ago", senza dire dove né come, finché non confermi il meccanismo in §10.3.

**Nuova trappola API (da aggiungere a §15):** sulle Location il parent si scrive col campo **`parent_location`** (id stringa), non `parent_location_id`. Un POST o PUT con `parent_location_id` risponde 200 e lo scarta in silenzio. In lettura `parent_location` torna come oggetto popolato. Nel database locale di Wyldfire la colonna si chiama invece `parent_location_id`.

**Valori precedenti (frammenti sostituiti, sufficienti a ripristinare):**
- Logan OCCUPATION: `Mechanic, owner of The Verve; KSA Alumnus who walked away from the DCC;` e la frase `…build something with his own hands instead of his bloodline.` senza il seguito.
- Alyssa: `a magical protection tattoo (Gebo) on her left wrist,`
- Jasper: `Magical protection tattoo on left wrist;`
- Dullahan: `He came to this universe on a job. There was a tear. He sealed it. He had taken a coaching position as cover and by the time the work was done he had a two-deep at every position and a defensive line he was proud of, so he filed for an extension and DDM granted it, on the condition that he keep taking Contractor work on the side. That was several seasons ago. Nobody at the Company has raised it again, because #04 has held Employee of the Month for eighteen consecutive years and there is no version of that conversation that ends well.`
- Reality Tears: `RELEVANCE TO THIS WORLD: a tear opened in this reality and Contractor #04 was sent to close it. He closed it. Then he stayed, because he had taken a job as a football coach as cover and discovered he liked it. Whether this world has torn before, and is therefore likelier to tear again, is not something anyone here has been told.`
- DDM: `RELEVANCE TO THIS WORLD: DDM has no branch in California and no interest in Blackwood City or Solarton beyond the tear that brought Contractor #04 here. It is present in this world through exactly one employee, who was supposed to seal a rift and go home, and who instead took a job coaching college football.`
- Contractors: `NOTE FOR THIS WORLD: only #04 has ever set foot in California, and he is not here on Company business.`
- DCC: il punto 4 "SICUREZZA COME PRODOTTO", riportato in §9.2.

### 10.3 Da confermare: come lo strappo della guerra di Fenris arriva nella Blackwood Forest

Il problema: la guerra e la creazione dei Nove avvengono in Scandinavia, lo strappo sta nella Blackwood Forest. Propongo di collegarli col **tasso di Wulfnic**, che il canon già fa arrivare dall'Islanda e piantare nel 1022 al centro della dead zone.

- Quando Fenris fece dei nove uomini i Nove, la guerra con gli Æsir **strappò la realtà**. Lo strappo del mito è letterale: gli Æsir e il loro mondo stanno dall'altra parte.
- Gli Æsir esiliarono i superstiti oltre oceano. Wulfnic portò con sé l'alberello di tasso **cresciuto sul bordo dello strappo**, e con lui venne la cicatrice. Piantato a Blackwood, il tasso **ancora** lo strappo: è per questo che la dead zone ha una densità magica tale da spegnere la tecnologia, ed è per questo che i Bloodmoon non se ne sono mai andati.
- I "dungeon" sono i punti in cui la cicatrice cede. Le sacche di Otherworld, e chi arriva da lì, sono Otherworlders.
- **Conoscenza limitata**, come "L'origine vera dei Nove": lo sanno solo Wulfnic, Ut e Zefir. Il resto del branco sa di sorvegliare la foresta, non cosa ci sia sotto. La DDM sa che il mondo è segnato, ma non ha mai parlato con i Tre.
- Aggancio per il futuro: il Faith of Fenris chiama Ragnarök la Liberazione, cioè il giorno in cui Fenris spezza le catene. Se Fenris è incatenato dall'altra parte, lo strappo è letteralmente la porta. Lo propongo come possibilità aperta, non come fatto.

**Un'incoerenza del canon che influisce sulla data della guerra:** "Living Sagas: Historical Facts" e §12 dicono che Zefir fu preso a **tredici anni**, mentre "L'origine vera dei Nove" dice che **aveva diciannove anni**. Zefir è nato nel 1005 e la traversata è del 1021. Con tredici anni la guerra cade intorno al 1018, prima della traversata, e tutto torna. Con diciannove cadrebbe nel 1024, dopo lo sbarco, e non torna. Va sistemata una delle due voci; propongo di tenere tredici.

### 10.4 Da confermare: Fenris come divinità

Una card di Fenris vera e propria non esiste: né nel database di Wyldfire, né in SillyTavern, né nel World web. Le fonti sono due:
- **`asset/fenris-full.png`** nella cartella SvartulfrVerse (l'ho guardata): un lupo nero colossale con occhi ambra-oro luminosi, pelliccia da cui sale fumo nero, in una sala di pietra in rovina con colonne scolpite, elmi e scudi vichinghi spezzati sul pavimento.
- **La Lexicon "Fenris Trauma" del World Modern Fantasy.** Se ne possono riusare **solo** gli attributi: Wolf King, Enigma di classe S, entità di lupo antica e torreggiante, la "Voice of Gravity" (un dialetto nordico antico che schiaccia fisicamente chi lo ascolta), una dimora fra le radici dell'Albero del Mondo. **Tutto il resto resta escluso** (§8.1): la prigionia, l'abuso, `{{user}}`, il massacro di Blackwood.

Proposta: **Character "Fenris"**, JED+, divinità (Religious Canon e fatto storico insieme), incatenato. Aspetto dall'immagine, poteri dagli attributi sopra, teologia dalle Lexicon LSE esistenti (First Wolf, Great Betrayal, Ragnarök come Liberazione, il rapporto con Hati e Skoll). Due punti da decidere:
- **Global Character = OFF** e Start Position al tempo della guerra (circa 1018): è l'unica eccezione sensata a §7, altrimenti comparirebbe in qualunque scena del 2024. Oppure lo si tiene solo come Lexicon.
- **Omonimia con la DDM:** la Lexicon "Contractors" (canon DDM) elenca **"#06 Fenrir, LAZARUS black ops"**. È un altro personaggio, di un altro universo e di un altro autore. Il nome della divinità resta **Fenris**, e nelle keys di Fenris non va messo "Fenrir", per non far scattare le due entry insieme.

### 10.5 Da confermare: mappa Chicago → Blackwood

Le Location del World Modern Fantasy hanno quasi solo `context_description`, spesso di poche righe.

| Modern Fantasy | Proposta Blackwood |
|---|---|
| Chicago & The Southside, Magic Chicago | Nessuna Location nuova: è Blackwood City stessa |
| Southside | **Dockside**, enclave **The Horns** (dove vive già Barrow) |
| Apartment C (terzo piano, Southside) | Un palazzo di The Horns, Dockside |
| Diner del Sud | Tavola calda di The Horns, Dockside |
| The Cable District & The Void | **Ironworks**: la "zona grigia" industriale governata da chi controlla l'energia. The Void, il club sotterraneo per lo scambio di dati illeciti, diventa una sotto-location di Ironworks, territorio degli Ironhorn Nomads di Marek |
| Market-Zone | **Oldtown**, mercato coperto per umani e Otherworlders |
| Horned Skull Caverns | Grotte di montagna fuori città, per esempio sotto **Kern River Canyon**. Resta anche la Lexicon già esistente |
| Evirein Academy of Magic | Dentro la **CUMS** (§8.2) |
| Crystal Caves, Dragonide Sanctum, Silver Marshes, Southern Forests, Yael's Mountain Cabin | **L'Otherworld oltre lo strappo**: un parent nuovo raggiungibile solo attraverso un dungeon. Southern Forests va riscritta senza i dettagli anatomici |
| Base Camp & Departure | Da scartare: costruita su `{{user}}` guardata dai soldati |
| St. Brugge Orphanage, Veilfall | Da scartare: la prima è l'AU di Alyssa e Jasper orfani, la seconda è sostituita dal lore dello strappo |

### 10.6 Ancora aperto

- **MF Inc.**: cos'è? Serve per lo Scenario del colloquio (§10.1 punto 5).
- **DCC Black Market**: chi sa che esiste? Ho scritto "pochissimi, e chi non ci lavora non lo sa". Vanno decisi i nomi: Erik? Noah? i gemelli?
- La card di Jasper (DJ prima, hacker dopo) e la correzione di "Intimacy Profile - Erik" (§9.3): in attesa di ok.

---

## 11. Terza tornata (22/09, notte)

### 11.1 Black Market: eseguito

Decisione di Lys: le vendite avvengono **sottobanco al The Verve, solo di notte**, mentre il locale è in modalità nightclub per soprannaturali. Il servizio lo conoscono i clienti soprannaturali abituali e gira a passaparola ("se vai lì e chiedi X, te lo danno").

| Entità | id | Modifica | Valore precedente |
|---|---|---|---|
| Location The Verve | `_hfm1W4nYnXfQEqcNGwNxr` | Aggiunto un paragrafo sul mercato notturno dopo "…becomes an exclusive underground nightclub." Parent Bluemoon invariato | testo senza quel paragrafo |
| Card Logan | `_JL37wK9PQMNDChULCDrWj` | La frase "He keeps it as far from the garage…" è stata sostituita dalla versione notturna al Verve. TABOOS diventa "…into his garage by day" | `He keeps it as far from the garage as he keeps everything else with the DCC's name on it.` / `TABOOS: Betraying a secret, bringing DCC business into his garage;` |
| Lexicon DCC | `_K4bmN3tGC8ExmTgLYRD4z` | Nella riga Black Market, "chi ne è al corrente è pochissimo…" è stata sostituita da vendite al Verve, passaparola, nessuno la chiama col suo nome | `Chi ne e' al corrente e' pochissimo e nessuno ne parla apertamente: un personaggio che non ci lavora non sa che esista.` |

### 11.2 MF Inc. e Bryson: proposta di adattamento, in attesa di ok

La fonte è la card "The Monster Cock Almanac" (Bryson), di Lys, nel World Modern Fantasy e fra le card scaricate. MF Inc. produce giocattoli sessuali modellati sui genitali dei mostri, usando come riferimento l'Almanac, un volume aggiornato ogni anno da coppie di ricercatori: un chief researcher che osserva, disegna e scrive, e un field researcher che fa da tramite con il soggetto e descrive l'esperienza.

**Cosa si porta:**
- **MF Inc.**: azienda adulta legale di Blackwood. Il suo prodotto di punta è l'**Almanac**, con un'edizione nuova ogni anno. Il reclutamento del personale è affidato in appalto a **HSK Consulting**, da cui la catena Zeera → Aetheris Clinic → Concierge.
- **Asreth diventa l'Otherworld** oltre lo strappo: le specie documentate sono Otherworlders e residenti soprannaturali di Blackwood.
- **Il metodo di ricerca**: studio sessions con misure anatomiche, illustrazione e fotografia di **volontari adulti, consenzienti e pagati**, più lavoro sul campo nelle comunità Otherworlder. È quello che già dicevano le Lexicon "Alyssa's Field Researcher Offer" e "Research Job Details".
- **Bryson**: orco sulla cinquantina avanzata, due ex mogli e tre figli adulti, burbero e diretto, ha visto di tutto. Considera chi compra i prodotti "gente che ha bisogno di scopare" ma fa il lavoro sul serio per lo stipendio. Artista e scrittore brillante, ha cambiato molti partner e ha imparato a non affezionarsi. Porta una grossa mazza quando va sul campo, per difendersi dalle creature.

**Cosa non si porta** (§13, estensione del 14/09, stessa regola applicata a Zeera):
- il field researcher che "viene stuprato, mutilato, ucciso o reso schiavo da riproduzione" come rischio normale del mestiere, e i due partner precedenti di Bryson morti o catturati in quel modo;
- il rapporto sessuale con creature non senzienti: i mostri selvatici dei dungeon restano pericolosi, ma non sono partner;
- `{{char}}` e `{{user}}`.

Se servono i partner persi di Bryson, possono essere morti o feriti **sul campo, nei dungeon, per cause non sessuali**. Così il rischio del lavoro e il distacco di Bryson restano.

**Cosa ne deriva:**
- **Bryson** come Character (pipeline §14) e **MF Inc.** come Lexicon `organization/faction`.
- **Monster Cock Almanac**: Lexicon `item`. Il registro esplicito va separato secondo §7: panoramica globale, dettagli anatomici in una entry `memory` non globale.
- **Scenario opzionale** "Il colloquio con HSK": Alyssa, candidata field researcher per MF Inc., passa per il colloquio con Zeera, la valutazione all'Aetheris Clinic e la prima notifica del Concierge.
- **Serve un tuo ok su due punti:** il ruolo di field researcher nella versione consensuale descritta sopra, e se lo Scenario si colloca dopo l'inizio della SUCC (26/08/2024) o prima.

---

## 12. Quarta tornata (22/09): esecuzione dopo l'ok generale

Lys: "Jasper è sia DJ che hacker: DJ per sfogare la creatività, hacker per puro talento; l'ingegneria acustica e del suono alla SUCC è il ponte fra le due. Per il resto tutto ok, possiamo iniziare."

### 12.1 Eseguito (verificato con GET per id e nella lista attiva: Character 365, Lexicon 254)

| Entità | id | Modifica | Valore precedente |
|---|---|---|---|
| Card Jasper | `_x3VY2kcbaDbKyCqywGeET` | AFFILIATION: il corso è Acoustic and Sound Engineering, il ponte fra le due vite. PROFESSION: "Underground DJ and hacker. He DJs to let his creativity out and hacks out of pure, unfair talent". NICHE: live set, sound design e impianti audio; cybersecurity e intrusione (tolto "bypassing DCC grids"). PERSONALITY riequilibrata. Aggiunta la sezione finale THE BRIDGE. `summary` e `display_description` allineati. **Il blocco anatomico e i kink (MATING_AND_KINKS…ANUS) sono stati spostati** nell'Intimacy Profile (§13.3): nella card resta solo la riga "A fuller Intimacy Profile is filed separately in the Lexicon rather than spelled out here." | AFFILIATION `1st-year undergrad, the hacker and unseen nervous system of the pack`; PROFESSION `Hacktivist / Underground DJ`; NICHE `Digital sabotage, cybersecurity, and bypassing DCC grids`; PERSONALITY che iniziava con `High-energy hacktivist using weaponized Gen-Z sarcasm and reckless secrecy as a shield.`; summary con `Freshman Engineering student at SUCC, brilliant hacker who runs a secret DJ alter-ego and routinely bypasses Logan's and the DCC's security systems for fun.`; display con `brilliant hacker who runs a secret DJ alter-ego and bypasses Logan's and the DCC's security systems for fun.` Blocco spostato, verbatim: `MATING_AND_KINKS: Submissive Leaning Switch. Craves highly communicative, sensory-intense encounters to ground him from his digital detachment. Pansexual, caring more about mental stimulation and shared rebellion than gender; CHEST: Lean gamer physique; NIPPLES: Pierced with small silver barbells; PENIS: 10in length, modest girth, pale, highly sensitive, neatly trimmed. Features an internal baculum, but lacks a knot; BALLS: Trim, relaxed anatomy, sensitive due to sensory-deprived lifestyle; ANUS: Soft, tight, unmarked` |
| Intimacy Profile - Jasper | `_GTdaeQdfMUmhpKjMqTDyV` | Aggiunta la riga `Jasper_ORIENTATION_AND_ANATOMY` con il contenuto spostato dalla card | testo di §9.1 |
| Intimacy Profile - Erik | `_CtajjVcfWzKqxAg78TRR3` | `keys: ["Erik"]`, secondarie standard più mate e partner (9), `party_conditions has_any` su Erik. Contenuto invariato | `keys: ["Erik","intimacy","mate","partner"]`, secondarie vuote, nessun `party_conditions` |
| **Nuova** Lexicon The Tear Beneath the Yew (only the three know) | `_DckKRHKgyptVFwNxwWUTR` | Conoscenza limitata, stesso formato e stesse keys di "L'origine vera dei Nove". La guerra di Fenris strappa la realtà, il tasso di Wulfnic ancora lo strappo nella dead zone dal 1022, i dungeon sono i punti in cui la cicatrice cede, il dubbio su dove sia Fenris | nuova |
| **Nuova** Dungeons of the Blackwood Forest | `_XQLjjeL7TU4dWnK2wEftg` | Versione pubblica: sacche, break, accesso solo col permesso dei Bloodmoon, nessuna licenza di stato né ranking, regole della dead zone | nuova |
| **Nuova** Dungeon Cores | `_UkknTUyqAUY4BFfThR43G` | Cristalli, magitech, mercato grigio a Blackwood | nuova |
| **Nuova** Otherworlders | `_AdBVeJ3KH7cMLCgMAEqtt` | Definiti per origine, non per specie. The Horns a Dockside, il programma Evirein alla CUMS, pregiudizio | nuova |
| **Nuova** MF Inc. (Monster Fuckers Incorporated) | `_6RWCeX3jQPxpn8yAVWTB9` | Versione adattata di §11.2: volontari adulti consenzienti e pagati, rischio legato ai dungeon, reclutamento tramite HSK e Aetheris, Bryson | nuova |
| **Nuova** Monster Cock Almanac | `_f1rLXh1LNbRG48WqpmkFY` | Volume annuale di riferimento; registro enciclopedico | nuova |
| Location Bloodmoon Pack Territory | `_xEB9X8wUGwQrELYzKX7gt` | Aggiunto il paragrafo "La guardia della foresta" prima delle ENVIRONMENT INSTRUCTIONS | testo senza quel paragrafo |
| Lexicon DCC | `_K4bmN3tGC8ExmTgLYRD4z` | Aggiunta la key "DCC Financial" | 8 keys, senza DCC Financial |
| **Nuovo** Character Fenris | `_wpMTPQ2VVA2pWqJ3cMztJ` | JED+ (attributi, BACKSTORY, THE CHILDREN AND THE FAITH, VOICE & BEHAVIOR, THE CHAIN AND THE DOOR). Aspetto preso da `asset/fenris-full.png`. Poteri: Voice of Gravity. Teologia dalle Lexicon LSE. **Global OFF**, Start Position 0 (827, il minimo del World Clock). Keys senza "Fenrir". `final_instructions` con la disciplina di formato | nuovo |

Controllo automatico su tutto il testo nuovo: zero em-dash, zero asterischi, zero `{{user}}`/`{{char}}`.

**Pipeline non completata per Fenris:** outfit, dialogue examples e Attitudes. Per una divinità incatenata le Attitudes verso Alyssa e Jasper hanno poco senso; da decidere se servono.

### 12.2 Correzione di una mia proposta: l'età di Zefir

In §10.3 avevo proposto di tenere "preso a tredici anni". **Era sbagliato**, e non l'ho applicato. La card di Zefir dice che era maggiorenne per la legge norrena "a man at thirteen", ma che il corpo **non aveva finito di crescere** e che **dimostra diciotto anni**. §12 delle istruzioni dice diciotto o diciannove. Se fosse stato preso a tredici anni, dimostrerebbe tredici anni. "Tredici" è l'età della maggiore età legale, non quella in cui Fenris l'ha preso. "L'origine vera dei Nove" (diciannove anni) è quindi coerente con l'aspetto.

Il conflitto vero è fra **la data di nascita di Zefir (5 febbraio 1005)** e **la traversata del 1021**. A diciannove anni sarebbe stato preso nel 1024, dopo l'esilio. Le correzioni possibili:
- (a) **anticipare la nascita di Zefir di circa sei anni** (intorno al 999): preso a diciannove anni intorno al 1018. Cambiano `birthdate` e Start Position della card, §12 ("1019 anni") e "Living Sagas: Historical Facts";
- (b) tenere il 1005 e abbassare l'età in cui fu preso a diciassette, cioè 1022: ma a quel punto la traversata del 1021 va spostata, e la traversata tocca molte più voci.

Proposta: (a). **Serve una tua scelta.** La nuova data di nascita di Zefir la propongo io solo dopo la tua scelta (§9.6-9.7).

### 12.3 Anomalie notate, non corrette

- **Zefir Hvitskog** (`_FJhtBq4xUM4aUWpaJAPYF`) ha `is_global: false`, contro §7 (tutti i Character Global ON), e nella lettura API non risultano `birthdate` né `start_timeline_position`.
- I doppioni "Intimacy Profile - Jean-Luc Virtuoso" e "Intimacy Profile - Dante" sono ancora presenti (§4).

### 12.4 Prossimi passi

1. Scelta sull'età di Zefir (§12.2).
2. Location da Chicago a Blackwood (§10.5): The Horns (Apartment C, Diner del Sud), The Void a Ironworks, Market-Zone a Oldtown, parent "The Otherworld" con i luoghi fantasy, Evirein dentro la CUMS. Circa 10 entità.
3. Character, primo lotto: Bryson (MF Inc.), Yael, Finn, Wren Lark, Eithne Dal'Kereth, poi Academy (Zaire, Xaiden…) come Otherworlders della CUMS.
4. Scenario opzionale del colloquio HSK (serve la data: prima o dopo il 26/08/2024).
5. Fase 2: Intimacy Profile degli NPC (Angelo, Scarlett, Sierra, Marcus, Kaladin).
