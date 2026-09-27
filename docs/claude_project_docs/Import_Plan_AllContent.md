# Piano di Import Completo — D:\SvartulfrVerse → Wyvern World

Aggiornato 30/08/2026.

## Obiettivi (da Lys)
1. Inserire nel World Wyvern TUTTI i contenuti in `D:\SvartulfrVerse\Wyvern`
2. Ottimizzare/ordinare tutti i content nelle folder corrette
3. Arricchire i dati importati usando `D:\SvartulfrVerse\Drafts`
4. (Futuro) Aggiungere altre informazioni che Lys fornirà dopo i primi due obiettivi

## Nota chiusa — "Marcus Thornfield"
RISOLTO. Card rinominata sulla piattaforma: "Marcus Reyes" → "Marcus Iron Thornfield" (nome canonico da `Drafts/Character_Cards_V1/NPCs/Marcus_Iron_Thornfield`), corretto sia in `long_summary` che in `summary`. Nessuna nuova card creata (contatore Characters invariato durante la modifica).

## Bug piattaforma scoperto — race condition su "New Location"/"New Lexicon"

Il pulsante "New X" seguito da compilazione via JS e Save può, in modo intermittente (~1 volta ogni 5-6 creazioni), sovrascrivere silenziosamente la voce creata immediatamente prima invece di crearne una nuova (net-zero sul counter). Contromisura adottata: dopo ogni Save, attendere 7-9s, poi navigare alla lista e verificare che (a) il contatore sia incrementato di 1 e (b) sia la nuova voce sia quella precedente siano presenti via ricerca testuale. Usando invece "New [tipo] here" dal menu contestuale della folder (vedi sotto), il bug del net-zero non si è più manifestato — ma è emerso un problema diverso e più subdolo (vedi nota su Bianca Rossi nel Task #7): a volte la card viene creata correttamente (nessuna sovrascrittura, contatore totale Characters incrementato) ma sembra non finire nella folder scelta, bensì in UNCATEGORIZED, senza alcun errore visibile al momento della creazione.

**Aggiornamento importante (fine Task #7 / Task #3)**: questo "misfile" in UNCATEGORIZED è stato osservato ripetutamente durante il Task #7 (Cass Harrow, Eclipse Noir, e più avanti un'intera batch di 5-6 personaggi contemporaneamente, incluso Aris Thorne) MA in ogni caso verificato con un refresh/nuova navigazione della pagina, il personaggio risultava correttamente presente nella folder di destinazione originaria (BLACKWOOD o SOLARTON), con UNCATEGORIZED che mostrava di volta in volta un set diverso e mutevole di nomi. Conclusione più probabile ora: **non è un vero misfile ma un artefatto di cache/sync lato client** nella vista folder-raggruppata della lista Characters, che si risolve da solo dopo un refresh. Non è più consigliato tentare fix reattivi (es. "Move to folder") su questi casi: verificare semplicemente con un refresh prima di considerare un personaggio davvero mal posizionato. Confermato di nuovo nel Task #3: Ut Berg e Zefir Hvitskog creati con lo stesso pattern senza alcun problema di posizionamento (entrambi in FAMILY).

## Scoperta importante — creazione diretta dentro una folder (risolve parte del Task #6, ma non sempre affidabile)

Ogni riga folder (Character/Location/Lexicon/ecc.) nelle liste per-tipo (es. `?tab=characters`) ha, accanto al pulsante "Move items…", una piccola icona "⋮" (ellipsis-vertical, separata dal testo "Move items…" e posizionata subito alla sua sinistra) che apre un menu con: **New [tipo] here**, New subfolder, Rename, Delete. Usare "New [tipo] here" crea il record nella folder giusta nella maggior parte dei casi (funzionato per Warg e Vito Marino, verificato via incremento del contatore di folder), e nel Task #7 e nel Task #3 questo pattern è stato riusato con successo per tutti i nuovi Character (15 NPC + Ut Berg + Zefir Hvitskog), restando lo standard consigliato per ogni futura creazione di Character.

**Nota tecnica**: questo bottone "⋮" è un trigger Radix (`aria-haspopup="menu"`) e va cliccato con una sequenza completa di eventi sintetici (pointerdown/mousedown/pointerup/mouseup/click dispatchati via JS al centro reale del suo `getBoundingClientRect()`), non con un semplice click reale a coordinate — un click a coordinate rischia di colpire il bottone "Move items…" adiacente invece (che apre una lista di riordino/spostamento degli item esistenti, non il menu di creazione). Sulla pagina "All Content" overview, invece, lo stesso menu compare cliccando l'icona "⋮" che appare a destra della riga quando selezionata (lì un click reale a coordinate funziona), MA in quel contesto il menu a volte mostra solo New subfolder/Rename/Delete senza "New [tipo] here" — se questo accade, usare la pagina per-tipo (`?tab=characters`, `?tab=locations`, ecc.) invece.

**Nota tecnica aggiuntiva (Task #3)**: nel modal "Select Tags", cliccare i chip per posizione fissa a schermo è fragile (le colonne si riflowano in base ai risultati filtrati) — un click "alla cieca" può selezionare il tag sbagliato (successo con "Machine" invece di "Werewolf" durante la creazione di Ut Berg, poi corretto). **Metodo affidabile**: usare sempre il campo "Search tags..." del modal per filtrare a un singolo risultato prima di cliccare, verificando poi il conteggio `(N/25)` via JS.

**Nota tecnica aggiuntiva (arricchimento mappa campus)**: ogni Location ha DUE campi testo distinti, facilmente confondibili: `description` (= "Display Description" nell'UI, il breve blurb mostrato in lista/browsing) e `context_description` (= campo "Description" più in basso nell'UI, etichettato "Describe this location's atmosphere, setting, and key features. The AI will use this during gameplay." — quello effettivamente usato dall'IA durante il roleplay). Per tutte le 29 Location SUCC create nel Task #1, il campo `context_description` era rimasto vuoto (0 token): l'arricchimento da mappa campus è stato scritto lì. Metodo: `Array.from(document.querySelectorAll('textarea'))[1]` è sempre `context_description` nell'editor Location (index 0 = `description`, index 2 = un campo tecnico irrilevante con valore "x"), impostato via native setter + `dispatchEvent(new Event('input'))` come per gli altri campi.

Questo non risolve lo spostamento dei 61 elementi UNCATEGORIZED già esistenti da prima del Task #7 (51 Location + 10 Lexicon) — per quelli Lys farà lo spostamento manualmente più tardi.

## Stato import Locations (Task #1 del piano) — ✅ COMPLETATO

Tutte le **45 Location [L] mancanti** identificate da `gerarchia_location.txt` sono state create e verificate presenti sulla piattaforma (Locations totali: 37 → 81).

- ✅ SUCC Campus (29): Archer Wolfwood Hall, Basilica Library, Griffin Clocktower, Med/Bioengineering Labs, Science Quarter, Arts Building, Unicorn Hall, Nocturnal Hall, Building A, Building B, Building C, Wyrm Dormitories, Fraternity & Sorority Row, TIT House (parent: Fraternity & Sorority Row), KSA House (parent: Fraternity & Sorority Row), Additional Student Housing, Administration, Supernatural Support Center (SSC), Storage & Supplies, St. Neptune Stadium, Bulls Stadium, Main Pool, Gym & Changing Facilities, Sports Fields, Helsing Chapel, Gallery, Dragon's Shortcut, Main Parking Lot, Parking Lot B
- ✅ Solarton (4): Coastal Residential, Bricklane Mall, Sidewinders Bar & Nightclub, Solarton High School
- ✅ Travel/Transito (2): Area di Servizio "The Halfway House" (env: Ventura/Route 101), The Simi Valley Grid (env: Simi Valley)
- ✅ Los Angeles (6): Beverly Hills, Hollywood, Osservatorio Griffith, The Neon Mirage, Molo 42, Skid Row
- ✅ Bakersfield (4): Campi Petroliferi di Kern River, The Dusty Coyote Diner, Parco Roulotte di Oildale, Kern River Canyon

## Task #2 — Environments — ✅ COMPLETATO

Creato l'Environment mancante "Zone di Transito e Confine" (da `Wyvern/environments.md`). Totale Environments: 11 → 12, confermato presente via ricerca. Nota storica invariata: CUMS è stato promosso a Environment/COMPLEX sulla piattaforma live nonostante `gerarchia_location.txt` lo trattasse come Location — deviazione nota da sessioni precedenti, non toccata.

## Task #3 — ✅ COMPLETATO — Verifica dei 9 personaggi Main Cast

Perimetro confermato leggendo `Drafts/Character_Cards_V1/Main_Cast/` (10 cartelle) incrociato con `claude/Alyssa_Status_Note.md`: Alyssa è esclusa perché resta la persona di {{user}} nel primo scenario, non un NPC (la sua card standalone è pianificata per un secondo momento, come da nota dedicata). I 9 Main Cast effettivi sono quindi: Edric, Erik, Jasper, Logan, Malachia, Noah, Ut, Wulfnic, Zefir.

**Già completi e verificati sulla piattaforma (nessuna modifica necessaria)** — confrontati campo per campo (birthdate, tag, Long/Short Description, pronomi, outfit) contro i file locali `Card_*.md`/`.json`:
- ✅ **Edric Douglas** (FAMILY) — birthdate 25 febbraio 2012 (12 anni), tag Werewolf/Male/Original/Fantasy/Supernatural/Modern (6), Long Description 754 token già in formato JED+ completo coerente col locale, RPG Lv.12, outfit "Casual/Home", Home Location Villa Douglas, Global Character ON. Nessuna azione: già presente da una sessione precedente.
- ✅ **Erik Douglas** (FAMILY) — birthdate 31 ottobre 1969, tag Male/Werewolf/Alpha/CEO/Fatherly (5), Long Description 9201 caratteri **più ricca del file locale** (include il Caccia-bond con Nixara, l'Anointing di Wulfnic, dettagli su Kaladin/Magnus/Elizabeth non presenti nella card locale) — evidentemente arricchita in una sessione precedente non documentata in questo file.
- ✅ **Jasper Douglas-Bloodmoon** (FAMILY) — birthdate 22 aprile 2005, tag JED/Male/Werewolf/Original/Fantasy/Modern/Supernatural (7), Long Description 4104 caratteri, 5 outfit definiti. **Discrepanza PENIS risolta**: il file locale `Card_Jasper.md` riportava 7in, la card piattaforma 10in. Lys ha confermato che 10in è la misura corretta, aggiornata a seguito di uno sviluppo narrativo "LSE biology" (post-presentazione). Il file locale resta disallineato ma non è stato corretto senza autorizzazione (nessuna richiesta esplicita di farlo finora); la card piattaforma (10in) è quella canonica.
- ✅ **Logan Douglas** (FAMILY) — birthdate 12 gennaio 1975, tag Male/Werewolf/Beta/Mechanic (4), Long Description 7154 caratteri, 4 outfit.
- ✅ **Malachia Douglas-Bloodmoon** (FAMILY) — birthdate 10 agosto 1996, tag Male/Werewolf/Alpha/Bodyguard (4), Long Description 7095 caratteri, 4 outfit.
- ✅ **Noah Douglas-Bloodmoon** (FAMILY) — birthdate 5 ottobre 1999, tag JED/Male/Werewolf/Original/Fantasy/Modern/Supernatural (7), Long Description 4376 caratteri, 5 outfit.
- ✅ **Wulfnic Bloodmoon (Báleygr)** (FAMILY) — birthdate 1 gennaio 825 CE (1199 anni), tag JED/Male/Werewolf/Original/Fantasy/Historical/Supernatural/Mythology (8), Long Description 4516 caratteri, 6 outfit. Conferma che la versione piattaforma è già allineata al canon aggiornato (1199 anni/Báleygr) e più avanti del file locale statico (che riporta ancora 1197 anni/823 AD) — nessuna azione necessaria, il file locale resta la fonte da aggiornare in futuro se richiesto, non la piattaforma. **Aggiornamento post-Task #3**: aggiunto il nickname "Nic" tra i Nicknames/Aliases (oltre a The Omniscient Jarl, The Builder King, Báleygr), su richiesta diretta di Lys.

**Creati da zero in questo Task (non esistevano ancora sulla piattaforma)**:
- ✅ **Ut Berg ("Ut The Mountain")** — folder FAMILY. Primordial Enigma/Firstborn, 1201 anni, shield-brother di Wulfnic e Zefir, "blunt instrument" del trio ("The Jarl points, the Ghost tracks, I smash"). Title "Ut The Mountain, Primordial Firstborn", nickname "Út Fjallit". Tag JED/Male/Werewolf/Original/Fantasy/Historical/Supernatural/Mythology (8, stesso set di Wulfnic). Long Description JED+ completa (backstory, family & pack, voice & behavior, sezione tematica "The Weight of the Mountain") + Short Description, 4 Activation Keywords primari (Ut, Ut Berg, The Mountain, Firstborn) + 2 secondari (The Den, shield-brother). Pronomi he/him/his/his/himself. Birthdate 5 maggio 823 CE. Content Rating Explicit, Global Character ON, nessuna Home Location (coerente con Wulfnic, che non ne ha). Nessun outfit definito (come molti degli NPC del Task #7). Verificato: Characters 83→84.
- ✅ **Zefir Hvitskog ("The White Ghost")** — folder FAMILY. Primordial Enigma/Firstborn, 1019 anni (aspetto ~20enne), scout/assassino silenzioso del trio ("Ut makes the noise. I make the corpses. The Jarl makes the history."). Title "The White Ghost, Primordial Firstborn", nickname "Zefir inn hvíti skuggi". Stessi 8 tag di Ut/Wulfnic. Long Description JED+ completa + Short Description, 3 Activation Keywords primari (Zefir, White Ghost, Firstborn) + 2 secondari (The Den, shield-brother). Pronomi he/him/his/his/himself. Birthdate 5 febbraio 1005 CE. Content Rating Explicit, Global Character ON, nessuna Home Location. Nessun outfit definito. Verificato: Characters 84→85.

Contatore Characters finale: 83 → 85 (2 nuove card create in questo Task).

**Non ancora fatto per Ut e Zefir (bassa priorità, come per molti NPC del Task #7)**: nessun outfit/Appearance definito; post_history_instructions con la regola di formattazione discorso non applicata (item pendente trasversale a tutte le card, vedi sotto).

## Task #4 — Lexicon (parziale) — ✅ 3/4 COMPLETATO, 1 scartata per regola anti-duplicato

Controllati tutti i 13 file `Wyvern/lexicon/*.md`: solo 4 contenevano voci sostanziali (Concept, Event, Location, Memory — gli altri 9 sono stub vuoti). Verificate le 28 voci Lexicon già presenti sulla piattaforma (5 folder + 7 UNCATEGORIZED): nessuna delle 4 voci locali esisteva già. Create le seguenti 3, tutte in UNCATEGORIZED (create prima della scoperta di "New location here", quindi non sono nella folder giusta — Lys le sposterà manualmente insieme al resto):

- ✅ **Douglas Commercial Coalition (DCC)** — Entry Type: Concept, Global Entry: OFF (fonte: "Constant: No"), 8 keyword (DCC, Douglas Commercial Coalition, Douglas Commercial Company, Kaladin, Security Division, PMC, BlackWolf, DCC Security). Nota: Kaladin ha già una Character card propria (Security_Chief); questa voce Concept resta scoped alla storia istituzionale DCC/Security Division, non duplica il personaggio.
- ✅ **La Guerra di Fenris e l'Esilio dei Firstborn** — Entry Type: Event, Global Entry: OFF, 11 keyword.
- ✅ **Il Viaggio di Wulfnic in America** — Entry Type: Memory, Global Entry: OFF, 11 keyword.

**Scartata deliberatamente**: la voce Lexicon locale "Yarrow River" (Location, `Wyvern/lexicon/Location.md`) NON è stata importata perché un oggetto Location completo con lo stesso nome esiste già nella folder BLACKWOOD LOCATION — per la Regola #7 del progetto ("luogo già creato manualmente come Location → non importare la versione lorebook equivalente, è un doppione") si tratta di un duplicato. Il dettaglio etimologico interessante che conteneva (vera etimologia norrena "Ýrá" = fiume del tasso, vs. la credenza moderna errata legata alla pianta yarrow) è stato comunque preservato: inserito come riferimento nella nuova voce "Il Viaggio di Wulfnic in America" così l'informazione non va persa.

Contatore Lexicon: 28 → 31.

## Task #5 — World Info settings — spot-check OK, nessuna azione necessaria

Verificati i campi principali della tab World Info/Simulation contro `Wyvern/world_info.md` (righe 1-112):
- **World Age / Timeline**: piattaforma mostra "1249 years, 2 months, 1 day, 6 hours documented", Start Jan 1 800, Recorded History Ends March 3 2049 — coerente con il file locale (World Age 10950000 ore = stesso valore).
- **Description**: il campo "description" in World Info (3231 caratteri) è più lungo/aggiornato rispetto alla "Context Description" nel file locale statico — sembra già stato arricchito in una sessione precedente. Non sovrascritto per non perdere lavoro già fatto; nessuna discrepanza preoccupante rilevata nel confronto a campione.
- **About Your World** (Simulation tab, 705 token) presente e popolato.
- **Enabled Features**: Inventory, Currency, RPG Stats, Combat risultano attivi coerentemente col file locale (`inventory, currency, rpg_stats, show_party_stats, combat`).
- Non ho verificato in dettaglio Currencies/Calendar/Travel Routes voce per voce (verifica di superficie soltanto, dato che erano già presenti e sembravano correttamente popolati) — se serve un controllo puntuale, segnalarlo a Lys o in una sessione futura dedicata.

## Task #6 — Riorganizzazione folder: gestione mista (automazione + manuale)

Create con successo le 2 folder mancanti: **BAKERSFIELD LOCATION** e **TRAVEL LOCATION** (ora esistono, vuote).

**Bloccante "Move items…"**: il pulsante non produce ALCUN effetto osservabile quando cliccato per il bulk-move degli item UNCATEGORIZED — testato con click diretto (coordinate reali), `.click()` via JS, sequenza completa di eventi trusted-like, ctrl+click, right-click. Nessun dialog/menu/checkbox compare mai nel DOM per il bulk-move con più item. Per un singolo item, invece, si apre un dialog "Move to folder" funzionante nell'interfaccia ma inaffidabile nel salvataggio reale (vedi sopra, caso Bianca Rossi: 3 tentativi falliti). **Deciso con Lys**: lo spostamento dei 61 elementi UNCATEGORIZED preesistenti (51 Location + 10 Lexicon) lo farà lei manualmente più tardi — non è più un blocco per il piano.

**Risolto per le nuove creazioni Character**: il menu contestuale "..." (icona ellipsis-vertical) sull'header folder → "New [tipo] here" crea direttamente nella folder corretta; l'apparente finire in UNCATEGORIZED nella vista subito dopo il Save si è rivelato, nei casi verificati con refresh durante il Task #7 e il Task #3, un artefatto di sync temporaneo e non un vero errore di posizionamento (vedi nota nella sezione bug sopra).

**Elementi UNCATEGORIZED preesistenti in attesa di smistamento manuale da parte di Lys**:
- Locations (51): SUCC LOCATION ×29, SOLARTON LOCATION ×4, LOS ANGELES LOCATION ×6, BAKERSFIELD LOCATION ×4, TRAVEL LOCATION ×2 (lista nomi completa nella sezione Task #1 sopra)
- Lexicon (10): Archer Wolfwood Hall (voce di test, probabile doppione — vedi Pulizie sotto), Douglas Commercial Coalition (DCC), La Guerra di Fenris e l'Esilio dei Firstborn, Il Viaggio di Wulfnic in America, Intimacy Profile ×3 (Erik/Logan/Malachia), Species_Details ×3 (Erik/Logan/Malachia)

Nota tecnica: il conteggio Locations (81) risultava 1 in meno rispetto alla somma aritmetica attesa (66 baseline + 16 create = 82); tutti i 16 nomi sono stati individualmente ri-verificati presenti e distinti via ricerca, quindi non risulta perdita dati — probabile imprecisione nel conteggio baseline riportato nel riepilogo di sessione precedente, non un problema attuale.

## Pulizia da fare (bassa priorità, non bloccante)
- Voce Lexicon "Archer Wolfwood Hall" (UNCATEGORIZED, creata durante un test di import JSON precedente) probabilmente duplica il pieno oggetto Location "Archer Wolfwood Hall" già esistente — valutare eliminazione con autorizzazione di Lys.
- Duplicati in BLACKWOOD LOCATION: "Ironworks" e "Bloodmoon Longhouse" risultano entrambi presenti due volte — da deduplicare.

**Chiuso (confermato da Lys, nessuna azione)**: i 4 membri S.R.F. e la DCC Tower restano correttamente in LOS ANGELES (la base SRF e la torre DCC si trovano fisicamente a Los Angeles) — non era un errore di sorting, rimosso dalla lista pulizie.

**Chiuso (confermato da Lys)**: discrepanza PENIS Jasper risolta, 10in è la misura canonica (vedi Task #3) — rimosso dalla lista pulizie.

## Arricchimento da mappa campus — ✅ COMPLETATO (prima passata, dall'immagine fornita da Lys)

Lys ha fornito un'immagine "S.U.C.C. Main Campus" con dettagli interni per le location SUCC già create. Tutte e 15 le location interessate sono state arricchite scrivendo il dettaglio interno nel campo `context_description` ("Description" nell'UI — il campo usato dall'IA a runtime, distinto dal breve "Display Description"; vedi nota tecnica sopra), lasciando il breve `description`/Display Description invariato dove già adeguato:

- ✅ **Basilica Library** — piani multipli (mondano al piano terra, archivio magico protetto ai piani superiori), study rooms insonorizzate, Trophy Room, portico d'ingresso come rifugio informale.
- ✅ **Griffin Clocktower** — Lecture Theatres di Giurisprudenza e Ingegneria ai piani superiori, uffici docenti, club informale nel seminterrato per studenti notturni.
- ✅ **Med/Bioengineering Labs** — aule teoriche, laboratori di ricerca su biologia umana/soprannaturale, spazi per esami pratici, finanziamento DCC.
- ✅ **Science Quarter** — dipartimenti di fisica/chimica/ingegneria, reparti di Specimen Containment ad accesso controllato.
- ✅ **Arts Building** — dipartimento Belle Arti + Arti Performative, Auditorium per saggi/spettacoli/proiezioni.
- ✅ **Unicorn Hall** — Greenhouse (serra) per botanica applicata e come spazio di sosta per studenti grandi/alati.
- ✅ **Nocturnal Hall** — lezioni notturne per vampiri/ombre di notte, riconversione informale a club/salotto studentesco di giorno.
- ✅ **Building A** — aule generiche + lecture theatres più capienti, corsi introduttivi, prevalentemente umani.
- ✅ **Building B** — piccole aule per corsi con pochi iscritti, uffici docenti, area studio comune al piano terra.
- ✅ **Wyrm Dormitories** — (Display Description già completa da sessione precedente con Ala Nord/Ovest/Est/Sud, palestra, parcheggio, sale sole/luna) — aggiunta nota atmosferica sui due ritmi giorno/notte paralleli del complesso.
- ✅ **St. Neptune Stadium** — (Display Description già completa con ice rink/piscina/sauna) — aggiunta nota su squadre Bears/Kelpies e condivisione impianto termico.
- ✅ **Main Pool** — (Display Description già completa con acqua dolce) — aggiunta nota su uso sociale pomeridiano e prendisole.
- ✅ **Helsing Chapel** — (Display Description già completa multi-confessionale) — aggiunta nota su gestione calendario/prenotazioni tramite Student Association Building.
- ✅ **Student Association Building** — card completamente vuota (sia Display Description che Description): scritte entrambe da zero — supporto Supernatural+Human, ambulatorio di Primo Soccorso, sede amministrativa associazioni/club.
- ✅ **Archer Wolfwood Hall** — (Display Description già completa magic-proofed) — aggiunta nota su uso per assemblee/presentazioni a tutto il campus oltre alle lezioni frontali.

Metodo verificato e ripetuto in modo affidabile per tutte e 15: ricerca location via campo "Search" della lista Locations (JS native setter + dispatchEvent), click sul risultato, lettura dei due textarea (`description` index 0, `context_description` index 1) via JS per capire cosa mancava, scrittura del testo mancante via native setter + dispatchEvent, Save, verifica del conteggio token nel campo aggiornato prima di passare alla location successiva.

## Arricchimento da mappa campus — seconda passata (fonti esterne ufficiali) — ✅ COMPLETATA

Su richiesta di Lys, usate come fonti aggiuntive: `https://io-succ.uwu.ai` (sito ufficiale del fandom SUCC-U-VERSE), `https://ioverse.fandom.com/wiki/Supernatural_University_of_Central_California` (fetch diretto bloccato con 403 — bypassato con web_search, che ha restituito solo snippet superficiali senza nuove informazioni sostanziali rispetto a io-succ.uwu.ai), e il Lorebook `Wyvern/lorebooks/SUCC-U-VERSE.json` + `Wyvern/gerarchia_location.txt` (già sincronizzati nel progetto). Da queste fonti sono emersi nomi propri e dettagli d'uso non ancora presenti nelle card, integrati nel campo `context_description` delle location coinvolte:

- ✅ **Basilica Library** — aggiunta la Meeting Room 005 nel seminterrato come sede fissa dell'Anime Club (venerdì ore 18, aperto a studenti umani e soprannaturali), e la presenza di sale climatizzate più calde del normale per studenti/personale a sangue freddo in inverno.
- ✅ **Griffin Clocktower** — il club informale nel seminterrato ha ora un nome canonico, **The Pendulum** (da `gerarchia_location.txt`); aggiunta anche la nota che la torre, fungendo da principale struttura per le lezioni, chiude periodicamente per manutenzione con le classi temporaneamente ricollocate a Building C.
- ✅ **Unicorn Hall** — la Greenhouse ha ora un nome canonico, **La Serra Xenobotanica** (da `gerarchia_location.txt`); aggiunta anche la nota che l'edificio è sede fissa del BigFeet Hiking Club (escursioni, campeggi, gita settimanale estiva).
- ✅ **Science Quarter** — il reparto di Specimen Containment ha ora un nome canonico, **Vault 4**, alta sicurezza (da `gerarchia_location.txt`).
- ✅ **Helsing Chapel** — aggiunta la Vampire & Undead Association come club residente (riunioni domenica/lunedì ore 23, processo di ammissione rigoroso).
- ✅ **Student Association Building** — aggiunta la Supernatural & Human Alliance come club residente (riunioni mensili, uno dei club più grandi e attivi del campus).
- ✅ **Nocturnal Hall** — aggiunta The Pack (società were/canide ufficiale del SUCC) come club residente, riunioni il martedì 19-21, a rotazione stagionale con il Lunar Quad.
- ✅ **Lunar Quad** (location preesistente, non tra le 15 originarie ma aggiornata per coerenza) — aggiunta la nota sulla rotazione stagionale delle riunioni di The Pack con Nocturnal Hall.
- ✅ **Building C** (location preesistente, non tra le 15 originarie ma aggiornata per coerenza) — aggiunta la funzione di aula di riserva durante le chiusure per manutenzione della Griffin Clocktower.

**Altri dati raccolti dalle fonti esterne, non ancora usati ma disponibili per arricchimenti futuri** (demografia, accademici, sport, C.U.M.S.): SUCC ha ~8.000 studenti (80/20 supra/umani secondo Drafts, ma io-succ.uwu.ai riporta una ripartizione di specie più dettagliata: Weres/Shapeshifters 25.8%, Demi-umani 24%, Umani 13.3%, Vampiri 7.5%, Demoni 5%, Fae 4.9%, Ibridi 4.7%, Non-morti 4%, Umani con capacità magiche 4%, Altro <1%); offre ~75 major tra cui Alchimia, Divinazione Applicata, Studi Astrali, Criptozoologia, Magia Ambientale, Licantropologia, Necromanzia, Pozioni, Relazioni Umano/Soprannaturale, Studi Vampirici; squadre sportive Bulls (football), Bears (hockey), Kelpies (nuoto/tuffi), Phantoms (basket, "storia di sfortuna terribile"), oltre a cheerleading e altri sport minori. **C.U.M.S.** (California University of Magical Sciences): fondata nel 1910 a Hex Valley, 20 minuti da Solarton, solo studenti soprannaturali, ~42% almeno parzialmente vampiro, orario "crepuscolare" (luce diurna vera che dura solo ~6 ore d'estate, quasi assente d'inverno grazie a wards magiche), dormitori Artemis (femminile) e Apollo (maschile), Magick Research Labs, Nightwine Hall (location Lexicon già esistente sulla piattaforma), squadre CLAMS (football) e BEAVERS (hockey).

## Task #7 — ✅ COMPLETATO — Import 15 NPC da `Drafts/Character_Cards_V1/NPCs/`

Cross-check con `Review_Pending_Status.md` completato: dei 19 NPC target, 3 esistevano già (Angelo Moreno, Rev, Scarlett Rose), 1 necessitava solo correzione nome (Marcus Iron Thornfield, fatto), 15 sono stati creati da zero. Tutti e 15 sono ora sulla piattaforma, con description JED+, tag Identity/Species/General, pronomi e birthdate impostati:

- ✅ **Warg** — folder SOLARTON. Head of Campus Security, S.U.C.C. Backstory con hook narrativo sul padre mercenario/Gamma-7/Project Blackwolf. Pronomi he/him. Tag Male/Werewolf/Original/Supernatural/Modern. Birthdate 14 giugno 1989.
- ✅ **Vito Marino "Scar"** — folder BLACKWOOD. District Alpha, Ironworks Syndicate. Pronomi he/him. Tag Male/Werewolf/Original/Supernatural/Modern. Birthdate 22 marzo 1974.
- ✅ **Bianca "Bia" Rossi** — folder BLACKWOOD (dopo iniziale flicker in UNCATEGORIZED, confermata correttamente posizionata a refresh). Fashion Negotiator, District Alpha di Paradise East, alleata di Angelo Moreno. Pronomi she/her. Tag Female/Werewolf/Original/Supernatural/Modern. Birthdate 8 luglio 1989.
  - **Discrepanza fonte rilevata** (da segnalare, non risolta nei file sorgente): `Bianca_Rossi.json`, character_book entry #2, descrive una "Bianca Rossi" come socialita "venomous, glacial" di Los Angeles nemica dei Douglas, insieme ad altri nomi (Mark O'Connor, Isobel Blackwater, Antaneone) che non corrispondono alla Bianca Rossi principale. Sembra un blocco di lore mescolato per errore da un'altra fonte/autore. Usata la caratterizzazione principale (entry #1 + description/personality/first_mes, tutte concordi); il blocco #2 non è stato importato.
- ✅ **Aurora Night** — folder BLACKWOOD. District Alpha.
- ✅ **Cass Harrow** — folder BLACKWOOD. District Alpha. Pronomi she/her (Reflexive "herself"). Tag Female/Werewolf/Original/Supernatural/Modern. Birthdate 15 aprile 1979.
- ✅ **Dominic Chen** — folder BLACKWOOD. District Alpha, Paradise West. 38enne, bisessuale, fornitore di lusso. Altezza 6'0"/183cm. Pronomi he/him. Tag Male/Werewolf/Original/Supernatural/Modern. Birthdate 9 settembre 1986.
- ✅ **Eclipse Noir** — folder BLACKWOOD. District Alpha, Bluemoon South. 24enne genderfluid, estetica punk, liaison della resistenza "The Verve". Pronomi they/them (primo caso non-binario gestito). Tag Genderfluid/Werewolf/Original/Supernatural/Modern. Birthdate 21 giugno 2000.
- ✅ **Isobel Blackwater** — folder BLACKWOOD. District Alpha, Dockside. 55enne, eterosessuale, organizzatrice di contrabbando. Pronomi she/her. Tag Female/Werewolf/Original/Supernatural/Modern. Birthdate 10 novembre 1969.
- ✅ **Federico "Riki" Savini** — folder BLACKWOOD. Nickname "Riki". Rappresentante dei Lupi Solitari (~24.250 lupi solitari), confidente di Malachia Douglas. 65enne. Pronomi he/him. Tag Male/Werewolf/Original/Supernatural/Modern. Birthdate 3 ottobre 1959.
- ✅ **Archer Wolfwood** — folder SOLARTON. Rettore (Chancellor), S.U.C.C. 60enne, Alpha. Pronomi he/him. Tag Male/Werewolf/Original/Supernatural/Modern. Birthdate 14 maggio 1964.
- ✅ **Brittany Willow** — folder SOLARTON. Studentessa SUCC, TIT Sorority, super-fan di Malachia Douglas. 20enne umana. Pronomi she/her. Tag Female/Human/Original/Modern (senza Supernatural, essendo umana). Birthdate 2 agosto 2004.
- ✅ **Jake Thompson** — folder SOLARTON. Lavoratore SUCC, Half-Minotaur. 24enne, ex-compagno di classe di Alyssa/Jasper. Pronomi he/him. Tag Male/Minotaur/Original/Supernatural/Modern. Birthdate 18 luglio 2000.
- ✅ **Javier Sinclair** — folder SOLARTON. Studente SUCC, Demihuman Tiger, origine giamaicana, tatuatore part-time al Claw&Steel, coinquilino di Jasper nei Wyrm Dormitories (Stanza 72). Personalità inferita (il file sorgente aveva solo placeholder generico). 19enne. Pronomi he/him. Tag Male/Demihuman/Original/Supernatural/Modern. Birthdate 25 febbraio 2005.
- ✅ **Talia Grimwood** — folder SOLARTON. Studentessa di bioetica vampirica, confidente di Alyssa. Card costruita estrapolando da uno stub minimale (`note.md`), non un JSON completo. 22enne (apparente). Pronomi she/her. Tag Female/Vampire/Original/Supernatural/Modern. Birthdate 17 ottobre 2002.
- ✅ **Aris Thorne** — folder SOLARTON. Professore severo di Pre-Medicina alla SUCC, completamente ignaro del mondo soprannaturale e della vera identità/famiglia di Alyssa. Card costruita estrapolando da uno stub minimale (`note.md`). 52enne umano. Pronomi he/him. Tag Male/Human/Original/Modern/Educational (Educational al posto di Supernatural, essendo umano e ignaro). Birthdate 15 marzo 1972.

Contatore Characters finale: 68 → 83 (15 nuove card create in questo Task, verificato).

## Prossimi passi immediati
1. ✅ ~~Completare le 45 Location [L] mancanti~~ — FATTO
2. ✅ ~~Environments: creare "Zone di Transito e Confine"~~ — FATTO
3. Spostamento batch nelle folder corrette (61 item UNCATEGORIZED preesistenti) — Lys lo fa manualmente più tardi
4. ✅ ~~Task #4: import 3/4 voci Lexicon sostanziali~~ — FATTO (Yarrow River scartata come doppione, vedi sopra)
5. ✅ ~~Task #5: spot-check World Info settings~~ — FATTO, nessuna discrepanza bloccante
6. ✅ ~~Task #7: import 15 NPC~~ — FATTO, tutti e 15 creati e verificati (vedi sopra)
7. ✅ ~~Task #3: verifica Main Cast (9 personaggi)~~ — FATTO, 7 già completi/verificati (Edric, Erik, Jasper, Logan, Malachia, Noah, Wulfnic), 2 creati da zero (Ut Berg, Zefir Hvitskog); più tardi aggiunto nickname "Nic" a Wulfnic su richiesta di Lys; discrepanza PENIS Jasper risolta (10in canonico, confermato da Lys)
8. ✅ ~~Arricchimento mappa campus SUCC, prima passata (15 location, immagine)~~ — FATTO
9. ✅ ~~Arricchimento mappa campus SUCC, seconda passata (fonti esterne ufficiali: io-succ.uwu.ai, lorebook SUCC-U-VERSE, gerarchia_location.txt)~~ — FATTO, vedi sezione dedicata sopra
10. → **Prossimo**: nessun task specifico assegnato al momento. In attesa di direzione da Lys: possibili candidati sono l'Obiettivo #3 completo (arricchimento generale da `Drafts/`), l'Obiettivo #4 (nuove info che Lys fornirà), oppure le pulizie a bassa priorità elencate sopra (deduplicazione Ironworks/Bloodmoon Longhouse, voce Lexicon Archer Wolfwood Hall doppione), oppure sfruttare i dati demografici/accademici/sportivi extra raccolti da io-succ.uwu.ai per ulteriori arricchimenti (es. World Info, Lexicon su C.U.M.S., major accademiche).

Task tracking dettagliato nella task list della sessione (TaskCreate #1-16, invariati salvo #3/#7/arricchimento mappa campus ora completi).
