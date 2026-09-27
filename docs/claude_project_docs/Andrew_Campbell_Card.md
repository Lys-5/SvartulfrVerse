# Andrew "Andy" Campbell — scheda completata

Data: 2026-09-03. Verificata dopo reload completo, dati riletti dal server.

## Stato finale

| Campo | Valore |
|---|---|
| `long_summary` | 9.822 caratteri, JED+ |
| `summary` | blocco PList di soli tratti, 546 car. |
| `display_description` | 259 car. |
| `final_instructions` | 1.185 car., con la disciplina di formattazione §3 in coda |
| Outfit | 5: The Bear Suit, Frat House Default, Studio Three In The Morning, Campbell Formal, The Beach T-Shirt On |
| Dialogue Examples | 5 |
| Attitudes | 5: Vincent, Noah, Finn, Alyssa, Jasper |
| Nickname | Andy, andybear, StupidAndy |
| Titoli | Bears Mascot |
| Keys | Andy, andrew, campbell, mascot, andybear, anime club |
| Start Position | 10538088 (7 marzo 2002, giovedì) |
| Birthdate | 7 marzo 2002, offset `-191280` |
| RPG | Lv.22, MGT 3 / RES 5 / AGI 6 / WIT 8 / PRS 2 / SCT 7 |
| Global Character | ON |
| `{{user}}` / em-dash / asterischi | 0 / 0 / 0 |

Sezioni del `long_summary`: BACKSTORY, FAMILY, VINCENT, AT SUCC, THE FIRST LINE,
THE ART, BLOOD, THE ONLINE LIFE, VOICE & BEHAVIOR, THE VERDICT HE HAS ALREADY
REACHED.

## Fonti

Sette varianti fornite dall'utente (janitorai, creator veseii): festa in
confraternita, e-dating su Discord, appuntamento alla pista di pattinaggio,
presentazione ai genitori a Montreal, spiaggia, incontro alla convention con
una streamer, e la card di gruppo dell'**Anime Club** (Stan, Andy, Oskar).

## Decisioni prese con l'utente

**Data di nascita: invenzione dichiarata.** Le fonti danno solo "22 anni".
Scelti i **Pesci**, 7 marzo 2002: escapismo, arte, empatia, autocommiserazione,
romanticismo senza sbocco, tendenza a dissolversi invece di reagire. Bonus di
coerenza interna: i Pesci sono governati da **Nettuno**, e Andy passa le sue ore
al **St. Neptune Stadium**.

**Filone romantico: storia online generica.** Tutte le varianti fanno di
`{{user}}` la cotta o il partner di Andy. Rimosso ogni destinatario, tenuto il
vissuto nella sezione THE ONLINE LIFE: relazioni nate interamente su Discord,
foto scattate solo da angoli alti, messaggi cancellati la mattina dopo, e ogni
storia finita esattamente al punto in cui si parlava di vedersi di persona.

**Blocco Intimacy non trascritto** (§13.3).

**Famiglia Campbell.** Elice (19, capo della VUA), Maria e Leonard sono scritti
nella sezione FAMILY ma non hanno card: in lista NPC.

## Anime Club: correzione

**Errore mio, corretto.** In prima stesura avevo scritto che Andy tiene la sedia
a **Tate**. Falso: il club è **Stan, Andrew e Oskar**. Il World era già corretto
(l'outfit `Anime Club` e i riferimenti ad Andrew stanno sulla scheda di
**Oskar**), quindi l'unica card sbagliata era quella di Andy.

**Canon dalla card di gruppo:** l'Anime Club si riunisce il **venerdì sera** ed
**è Andrew a condurlo**. Ordine del giorno, shounen e shoujo del mese,
materiale pubblicitario, accoglienza dei nuovi. **È l'unica ora della settimana
in cui è lui il responsabile di qualcosa, e non l'ha mai raccontata così.**

## THE FIRST LINE

Andy è la mascotte della squadra che suo fratello capitana (Vincent centro,
Noah ala sinistra, Finn ala destra).

- **Noah**: gli è sempre gentile, e Andy ha archiviato quella gentilezza come
  pietà. **Stanno portando la stessa ferita**, uno come il Campbell minore e uno
  come "solo un Delta", e nessuno dei due lo sa.
- **Finn**: Vincent gli smonta i voti davanti a tutto lo spogliatoio. Andy è in
  quella stanza ogni volta e non ha mai detto niente. È l'unica cosa per cui si
  sente in colpa davvero invece che solo in ansia.

## Materiale emerso dalle fonti

- **CUMS**: corpo studentesco in maggioranza vampirica. Coerente con l'attrito
  Bears/Beavers.
- I **Clams** come squadra avversaria dei Bears, oltre ai CUMS Beavers.
- La convention **SOUPCON**, datata 2025 nella fonte, da spostare o ignorare.

**Correzione:** avevo scritto qui che **Hex Valley** era una "candidata naturale
a Location". Sbagliato, **è già un Environment**, insieme a CUMS, Solarton,
SUCC, Blackwood City, Blackwood Forest, Bloodmoon Pack Territory, Los Angeles,
Bakersfield, Simi Valley, Ventura/Route 101, Zone di Transito e Confine e
DDM Inc. // Voidspace. Prima di proporre di creare un luogo, controllare la
lista degli Environment.

## Discrepanze fra le varianti

| Dettaglio | Discrepanza | Risolto come |
|---|---|---|
| Residenza | Confraternita in cinque varianti, villa dei genitori a Montreal in una | Confraternita, Montreal come contesto stagionale |
| Frat | "Only got into his frat because Vincent pulled strings" assente in una variante | Tenuto, è nella maggioranza delle fonti |
| Ghiaccio | Bravo pattinatore in tre varianti, cade rovinosamente in un'altra | Non è un conflitto: cade **dentro** il costume, che non fa vedere niente |
| Sangue | "gets lightheaded", la vecchia entry lorebook diceva "faints" | Tenuto "lightheaded", consenso delle fonti |

## Osservazioni di piattaforma raccolte qui

**Condition/Control, misurati sulla stessa scheda:**

| Stato | Condition | Control |
|---|---|---|
| Lv.1, tutte le stat a 1 | 56 | 46 |
| Lv.22, tutte le stat a 1 | 77 | 67 |
| Lv.22, stat 3/5/6/8/2/7 | 77 | **52** |

**Condition dipende solo dal Livello**, +1 per livello da 56. **Control parte da
46, cresce di +1 per livello, ma viene ridotto dalla distribuzione delle stat.**
La vecchia formula con basi 67 e 30 è da scartare.

**Attitudes.** Quattro parti: tipo di bersaglio, bersaglio, livello e
motivazione. Con World Character il server salva `target_id` e lascia `target`
vuoto, che è normale. La mappa completa etichetta → chiave è in
`Attitudes_Audit_2026-09-03.md`: attenzione a **Wary**, che sembra "diffidente"
e salva `disliked`.

**Il click su coordinate non è affidabile.** Lo strumento dichiara un frame
800x538 mentre il click via `ref` usa le coordinate CSS della pagina, e le due
cose non coincidono. **Workaround:** dare all'elemento un `aria-label` sintetico
da JavaScript, cercarlo con `find`, cliccarlo per `ref`. Indispensabile per le
chevron delle cartelle e per le opzioni delle combobox.

**Un click sul Save che non registra non dà errore.** Qui tre outfit e cinque
dialoghi erano andati persi per questo. Verificare entro due secondi che il
pulsante sia passato a "Saving...".

**Birthdate.** Toggle, poi anno, mese (combobox) e giorno. Sul server è un
**offset negativo in ore rispetto al 1 gennaio 2024**, il "now" del World. Per
Andy `-191280`.

## Note residue

- `number_of_examples_to_use` è a 3 di default: con cinque esempi ne girano tre.
- Species e Occupation lasciati a None. Nota: **si possono impostare e
  persistono** (Logan ce le ha), ma solo scrivendole via API come `species_id` e
  `occupation_id`; dall'interfaccia il salvataggio fallisce in silenzio.
