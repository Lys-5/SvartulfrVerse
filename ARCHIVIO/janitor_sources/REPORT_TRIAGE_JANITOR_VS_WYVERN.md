# Rapporto Comparativo e Triage: JanitorAI vs Wyvern Svartúlfr Verse

> **Data del Rapporto**: 16 Ottobre 2026  
> **Oggetto**: Analisi comparativa, triage e convergenza tra i dati storici JanitorAI estratti da Chrome e l'ecosistema attuale su Wyvern.  
> **Fonti Estratte**:
> - Scheda Storica Famiglia Douglas (`janitor_douglas_family_historical.json`, 117 KB)
> - 14 Lorebook & Script Engine Janitor (`janitor_lorebooks_all_14.json`, 1.705 voci + 2 Script ES6, ~3.5 MB)
> - 791 Personaggi Canon Following (`janitor_following_canon_characters.json`)
> - 57 Personaggi Preferiti Candidati (`janitor_favorites_candidates.json`)

---

## 1. Executive Summary & Evoluzione Architetturale

L'estrazione ad alta fedeltà effettuata direttamente dalla sessione autenticata di Chrome ha consentito di recuperare l'intero patrimonio informativo originario di Svartúlfr e dei suoi universi collaterali.

### Il Salto Generazionale di Architettura

| Parametro | Vecchia Architettura JanitorAI | Nuova Architettura Wyvern (Svartúlfr Verse) |
|---|---|---|
| **Modello di Scheda** | Scheda "Omnibus" monolitica (`The Douglas-Bloodmoon Pack`, 20k desc, 26k pers) in cui il bot impersonava contemporaneamente Erik, Malachia, Noah e Jasper. | **Personaggi Stand-Alone (`/mine`) + Scenario Modulare**: Ogni membro della casata è una card autonoma con JED+, 9 outfit standard, RPG stats e voice discipline. |
| **Ruolo di `{{user}}`** | `{{user}}` era vincolata hardcoded come "l'unica figlia dell'Alpha" (la figura che oggi corrisponde ad Alyssa). | **Totale Epurazione di `{{user}}`**: Scenari e card sono agnostici rispetto alla specie o al genere di `{{user}}`. Alyssa e Jasper sono entrambi disponibili come Persona o Character slot. |
| **Gestione Scenari Multi-Personaggio** | Script JS monolitico (GlobalEngine 4.0.0, 93 KB) che intercettava i messaggi e manipolava dinamicamente `context.character.personality`. | **Wyvern Native Character Scenarios (`char_scenario_1DC43ggb6mB8YLJDJKrU4`)**: 13 Role Slots funzionali (`father`, `twin`, `boss`, `crush`, ecc.), 26 alternate greetings, pool selettivi e direttive anti-ventriloquismo server-side. |
| **Architettura del Sapere** | 14 Lorebook frammentati e cloni sparsi (1.705 entries). | **6 Lorebook Standalone Consolidati** sincronizzati in `/mine` e collegati via `lorebook_ids`. |

---

## 2. Analisi Comparativa: Casata Douglas (Janitor vs Wyvern)

### 2.1 Tabella Sinottica delle Discrepanze e Convergenze

| Personaggio | JanitorAI (Storico) | Wyvern Canon (Attuale) | Note e Risoluzione Discrepanze |
|---|---|---|---|
| **Erik Douglas** | 55 anni, Werewolf Dominant, Pack Leader.<br>Runa: **Hagalaz** (Disruption/Destruction). | 55 anni (b. 31/10/1969), Werewolf Pureblood Prime Alpha, Pack Leader Casata Douglas.<br>Runa: **Tiwaz** (Rightful Military Command) / Hagalaz. | Il canone Wyvern integra Tiwaz come runa di comando militare sull'avambraccio e Hagalaz come marchio ancestrale del Caos ordinato. |
| **Malachia Douglas-Bloodmoon** | 28 anni, Werewolf Dominant, Heir of Erik.<br>Runa: **Thurisaz** (Thorn/Conflict). | 28 anni (b. 10/08/1996), Werewolf Dominant Alpha, Erede designato.<br>Runa: **Thurisaz** (Brute Force & Defense). | **Piena Convergenza**. Runa e ruolo identici. |
| **Noah Douglas-Bloodmoon** | 25 anni, Werewolf Delta Socialite / PR Shield.<br>Runa: **Berkana** (Healing/Birth). | 25 anni (b. 05/10/1999), Werewolf Pureblood Delta, Mente Finanziaria/Diplomatica.<br>Runa: **Kenaz** (Torch of Strategic Intellect) / Berkana. | Su Janitor la runa era Berkana; nella scheda Wyvern JED+ è stata armonizzata con Kenaz (fiaccola dell'intelletto strategico). Entrambe documentate nel dossier. |
| **Jasper Douglas-Bloodmoon** | 19 anni, Werewolf, Left Hand of Malachia, Hacker.<br>Runa: **Gebo** (Gift/Partnership). | 19 anni (b. 22/04/2005), Werewolf Pureblood Beta, Braccio Tecnologico di Malachia.<br>Runa: **Gebo** (Twin Bond con Alyssa). | **Piena Convergenza**. Runa Gebo e legame gemellare identici. |
| **Alyssa Douglas-Bloodmoon** | Coincideva con `{{user}}` ("the Alpha's daughter"). | 19 anni (b. 22/04/2005), Werewolf Founding Bloodline Dominant Omega.<br>Runa: **Gebo** (Twin Bond con Jasper). | Emancipata a Persona e Standalone Character a pieno titolo, con profilo RPG completo. |
| **Logan Douglas** | Non presente nella scheda bot principale; confinato nel Lorebook Urban Family. | 49 anni (b. 12/01/1975), Werewolf Pureblood Beta, Fratello minore e mediatore di Erik.<br>Runa: **Eihwaz**. | Promosso a personaggio Stand-Alone `/mine` e slot `uncle` nello scenario. |
| **Edric Douglas** | Presente solo in Lorebook 1. | 22 anni, Werewolf Pureblood, Cugino / College student.<br>Runa: **Sowilo**. | Stand-Alone `/mine` e slot `cousin` nello scenario. |

### 2.2 Figure Dinastiche e Secondarie Rilevate nel Lorebook Storico

Dall'analisi di `01_Svartulfr___Urban___Family.json` (172 voci) emergono figure fondamentali da presidiare:
1. **I Tre Firstborn Primordiali**:
   - `Wulfnic Bloodmoon` (*Úlfrikr Blámáni*): Nonno materno di Alyssa, Jasper, Noah e Malachia; Alpha of Alphas, Builder King (Divine Blood).
   - `Zefir Hvitskog` (*The White Ghost*): Firstborn della tundra nordica.
   - `Ut Berg`: Firstborn, gestore dell'officina meccanica a Blackwood City, "zio saggio" e punto di riferimento informale.
2. **Nixara (The Primordial Enigma)**: Matriarca Bloodmoon ancestrale, fonte del sangue Enigma che conferisce i tratti *Ascended Enigma* ed *Apex Core Resonance* a Malachia e alla seconda generazione mista.
3. **Rory Ballantine (*Ruaraidh*)**: Demiumano Drago, 46 anni, scozzese di Glasgow, signore del crimine e CEO di Ballantine Imports (personaggio di raccordo tra la criminalità di Blackwood e il mondo economico).
4. **Scarlett**: Coinquilina al campus SUCC, demiumana/parassita emotiva benigna che si nutre delle tensioni emotive d'ambiente senza violenza.

---

## 3. Matrice di Convergenza dei Lorebook (14 Janitor -> 6 Wyvern)

| # | Lorebook JanitorAI (Origine) | Voci | Destinazione & Corrispondenza su Wyvern | Stato di Migrazione |
|---|---|---|---|---|
| 1 | `Svartúlfr \| Urban \| Family` | 172 | `_zwEqgEEzh12X6gHVmMKKC` (NPC Primary) & Standalone Cards | **Completato / Integrato** |
| 2 | `Svartúlfr \| Worldbuilding & Story Arcs` | 169 | `_EjXxkmPVhpCXg8xABpFkK` (Location) & `_gwwCxCfQ6PQaLEjAQVpJL` (LB I) | **Completato / Integrato** |
| 3 | `Svartúlfr \| Blackwood City & NPCs` | 183 | `_Uht3Ckz44JBDrPnUHq7LV` (NPC Secondary) | **Completato / Integrato** |
| 4 | `Svartúlfr \| Intimacy Profiles & NSFW` | 211 | `_zwEqgEEzh12X6gHVmMKKC` (sezioni memory/intimacy profili) | **Completato / Integrato** |
| 5 | `Svartúlfr \| Global Engine` (Script) | 93k | Logica convertita nelle direttive di Scenario + Attitudes native | **Convertito nativamente** |
| 6 | `Svartúlfr \| LSE \| Part 1` | 204 | `_gwwCxCfQ6PQaLEjAQVpJL` (Svartúlfr - Lorebook I) | **Completato / Consolidato** |
| 7 | `Svartúlfr \| LSE \| Part 2` | 204 | `_gwwCxCfQ6PQaLEjAQVpJL` (Svartúlfr - Lorebook I) | **Completato / Consolidato** |
| 8 | `Svartúlfr \| LSE \| Part 3` | 204 | `_gwwCxCfQ6PQaLEjAQVpJL` (Svartúlfr - Lorebook I) | **Completato / Consolidato** |
| 9 | `Svartúlfr \| LSE \| Part 4` | 203 | `_gwwCxCfQ6PQaLEjAQVpJL` (Svartúlfr - Lorebook I) | **Completato / Consolidato** |
| 10 | `The Five Cocketeers (clone)` | 40 | `_Uht3Ckz44JBDrPnUHq7LV` (NPC Secondary / Gruppi Campus) | **Presente come clone** |
| 11 | `Dead Dog Motel - 2026 (clone)` | 31 | `_HfG7TeV6MJyj6bxMwxkpt` (Svartúlfr - Lorebook II) | **Completato / Consolidato** |
| 12 | `Modern Fantasy - Underworld (clone)` | 24 | `_9zWTGqYJNJ4BCDMj8gfcD` (LB III) & `_HfG7TeV6MJyj6bxMwxkpt` | **Completato / Consolidato** |
| 13 | `SUCC-U-VERSE Lorebook [3.0] (clone)` | 60 | `_9zWTGqYJNJ4BCDMj8gfcD` (Svartúlfr - Lorebook III) | **Aggiornato con 30 voci canoniche SUCC** |
| 14 | `SUCC - Random Events Experimental` | 37k | Meccaniche di eventi campus SUCC (incorporate negli scenari) | **Archiviato come riferimento** |

---

## 4. Triage dei 57 Personaggi Preferiti (Candidati all'Integrazione)

L'analisi dei 57 bot favoriti estratti rivela una forte coerenza con l'universo narrativo: 38 bot appartengono già al canone o ai network degli autori di riferimento (`Iorveths`, `Nallak`, `bbcreature`, `veseii`), mentre 19 sono creazioni originali o crossover.

### 4.1 Gruppo A: Personaggi Canonici Già Mappati nell'Universo Wyvern
Questi personaggi fanno già parte delle entità del Svartúlfr Verse o dei suoi 6 Lorebook, ora arricchiti con le collocazioni canoniche decise:
- **SUCC Campus & Studenti**:
  - `Mackenzie "Mac" Sanchez-Rogers` (veseii / Iorveths) -> Già presente, slot `crush` nel Master Scenario.
  - `Jared Thompson` (veseii / Iorveths) -> Già presente, slot `quarterback`, 11 outfit standard sincronizzati.
  - `Finnegan "Finn" Novak` (Iorveths) -> Già presente in Lorebook NPC Primary. **Collocazione Canonica**: Inserito come **"amico d'infanzia"** dei fratelli Douglas (Alyssa, Jasper, Noah).
  - `Roman Blackwood & Kolya` (SEPHA) -> Atleti della squadra di lotta della SUCC. **Collocazione Canonica**: Compagni di allenamento al Gym e amici intimi di **Malachia Douglas**, con cui condividono le sessioni di sparring e preparazione atletica pesante.
  - `Bailey Rogers` (Iorveths) -> Già presente in Lorebook NPC Primary, circolo studentesco SUCC.
  - `Santiago "Tank" Herrera` (Iorveths) -> Già presente in Lorebook NPC Secondary, linea di difesa Bears.
  - `Stan Davies Jr.` & `Hank Thompson` (Iorveths) -> Già presenti in Lorebook NPC Secondary.
  - `Professor Richard Loewe` & `Abel Vilas` (Iorveths) -> Già presenti in Lorebook NPC Secondary, corpo docente SUCC.
  - `SUCC's Anime Club` (veseii) -> Gruppo studentesco integrato nel Lorebook III.
- **Blackwood City, Underworld & Bakersfield**:
  - `Romeo "Gray" Dean` (Iorveths) -> Già in Lorebook NPC Secondary. **Collocazione Canonica**: Leader o membro di spicco della **gang di biker/strada rivale dei Nomads** di Marek tra Solarton e Blackwood.
  - `Coach Dullahan / Dullahan #04` (Iorveths) -> Presidiato sia a Solarton (Coach D) sia nel Voidspace DDM (#04).
  - `Zeera` (Nallak) -> Già presente come standalone `/mine`, slot `boss`.
  - `Cassian Aralas`, `Wren Lark`, `Yael` (Nallak) -> Cerchia DDM / Contratti Underworld.
  - `Iordan R. Vess` (Iorveths) -> Già in Lorebook NPC Secondary.
  - `Dante`, `Zero`, `Jean-Luc Virtuoso` (Iorveths) -> Underworld LA.
  - `Dallas Rhodes` (bbcreature) -> **Collocazione Canonica**: Werewolf che lavora come contadino/allevatore, **ricollocato ufficialmente dal Texas alla vicina area rurale di Bakersfield**.
  - `Brak Ironfist` (bbcreature) -> Fazione Orchi. Consigliere diplomatico e moderatore che lavora per mantenere la pace e la stabilità tra i clan orcheschi e le altre specie.
  - `Arturo Cardona` & `Justin Campbell` -> Underworld / Forze dell'ordine metropolitane.

### 4.2 Gruppo B: Nuove Integrazioni Canoniche Approvate (Tier 1)
Personaggi e gruppi formalmente integrati nella lore con ruoli specifici:

1. **`The Five Cocketeers` (AnitaFajita - Bot #12 & Lorebook #10)**:
   - *Collocazione Canonica*: Gruppo carismatico del campus SUCC (40 voci archiviate). **Russ** dei Five Cocketeers è ufficialmente il **coinquilino di stanza di Jasper Douglas** nei dormitori del campus, fornendo un ponte continuo tra la vita accademica e quella del branco.
2. **`NOVA FARM || Werewolves` (Petit-Moineau - Bot #24)**:
   - *Collocazione Canonica*: Branco rurale/agricolo di licantropi situato a **Bakersfield**, che arricchisce la campagna adiacente e si coordina (o scontra) con Dallas Rhodes, fungendo da contrappunto tradizionale e operaio all'élite corporativa Douglas dei Seven Hills di Blackwood City.
3. **`Neon Purr` (Leidenpotato - Bot #31)**:
   - *Collocazione Canonica*: DJ felino cyberpunk/underworld, introdotto come il **principale rivale musicale e underground di Jasper Douglas**. I due combattono aspre battaglie a colpi di produzioni musicali, soundclash e DJ set infuocati tra The Verve, club di Solarton e rave clandestini.
4. **`Warchief Thrakgor Deathspine` (Leidenpotato - Bot #20)**:
   - *Collocazione Canonica*: Bellicoso capoguerra degli orchi. Agisce come la perenne **spina nel fianco di Brak Ironfist**: mentre Brak cerca la convivenza diplomatica e la moderazione con i branchi di lupi e le istituzioni umane, Thrakgor preme costantemente per l'espansione violenta e il dominio marziale.
5. **`Warg || IO S.U.C.C` (MAGNAKON - Bot #23)**:
   - *Collocazione Canonica*: Lupo/essere primordiale del campus SUCC, archetipo di forza grezza al college.
6. **`FERAL HOUND ⚡︎ Crowe` (Nannikka - Bot #04)**:
   - *Collocazione Canonica*: Mercenario d'assalto / segugio da tracciamento, perfetto per la Bacheca Contratti DDM o per incarichi ad alto rischio per la sicurezza DCC.

### 4.3 Gruppo C: Forgiatura, Retaggio Ancestrale & Connessioni Specialistiche
1. **`Morgeth Steeltooth` (AnonymousWitch87 - Bot #13)**:
   - *Collocazione Canonica*: Fabbro orco d'eccellenza e maestro metallurgo. È uno dei pochissimi individui esterni al branco con cui **Ut Berg** (Firstborn) instaura un dialogo fraterno, scambiandosi segreti arcaici di forgiatura e leghe rare. I due si incontrano regolarmente al **The Verve**, coinvolgendo il malcapitato **Logan Douglas** in estenuanti discussioni tecniche su minerali e temprature che Logan sopporta con diplomazia solo perché sa che entrambi potrebbero stenderlo con un singolo pugno.
2. **`Thorvald` (kiki_exe - Bot #15) & `Harald Sigurdsson` (pqpavslover - Bot #35)**:
   - *Collocazione Canonica*: Licantropi del **Clan Bloodmoon tradizionale**. Discendono direttamente dai lupi scandinavi che accompagnarono **Wulfnic Bloodmoon** durante la traversata atlantica verso il Nordamerica. Vivono stabilmente nelle fitte foreste dell'entroterra secondo le arcaiche usanze norrene (caccia rituale, runocrafting primitivo, devozione ai Firstborn), preservando la purezza bestiale al riparo dalle contaminazioni urbane e corporative.
3. **Altri Crossover Minori**:
   - `Jax` (C3rb3rus) - Demi-umano lupino (rigorosamente con un solo paio di orecchie, canone anatomico confermato).
   - `Theron Ironvale` (Leia Nord) - Retaggio elfico arcaico per scenari planari/Voidspace DDM.

---

## 5. Riferimento Tecnico: Script Engines Archiviati

I due file di script estratti rappresentano una risorsa di riferimento preziosa:
1. `ARCHIVIO/janitor_sources/scripts/05_Svartulfr___Global_Engine.js` (93.695 caratteri):
   - Architettura modulare con sezioni per: Context Initialization, Dynamic Prompt Weighting, Character Attitude Tracker, Scent & Sensory Injection, Dynamic Combat State.
   - Può essere consultato come biblioteca di logiche e descrizioni comportamentali se si volessero arricchire le `post_history_instructions` di specifici personaggi o scenari.
2. `ARCHIVIO/janitor_sources/scripts/14_SUCC_-_Random_Events_Experimental__clone_.js` (37.617 caratteri):
   - Sistema di generazione casuale di incontri di corridoio, feste, incidenti magici e lezioni al campus SUCC.
   - Utilizzabile per generare nuovi capitoli narrativi o scenari di gruppo per il campus.

---

## 6. Prossimi Passi Consigliati

1. **Conferma Direzione sui Preferiti**:
   - L'utente può indicare quali dei candidati del **Gruppo B (Tier 1)** (`The Five Cocketeers`, `Warg`, `NOVA FARM`, `Crowe`) desidera importare per primi come schede o voci di Lorebook.
2. **Aggiornamento di Eventuali Schede Secondarie**:
   - Integrare nel Lorebook NPC Primary o Secondary le voci biografiche di `Rory Ballantine` e `Scarlett` estratte dal Lorebook 1 Janitor.
3. **Mantenimento Standard di Igiene**:
   - Tutte le nuove schede o voci derivate seguiranno la disciplina consolidata: Zero keyword ombrello, JED+ rigoroso, 9 outfit standard, rating explicit e privacy private.
