# Regole di Progetto — Workflow Character Card Wyvern (Svartúlfr | Blackwood-Douglas)

Questo documento codifica le regole operative ufficiali e vincolanti per la creazione, l'aggiornamento e la gestione delle character card, delle voci di Lexicon e delle entità del World su Wyvern per l'ambientazione **Svartúlfr (Blackwood-Douglas / Modern Fantasy)**. Ogni assistente AI, script o collaboratore operante su questo repository deve attenersi scrupolosamente a queste direttive.

---

## Indice delle Sezioni

1. [Formato di Consegna: Testo, Non JSON](#1-formato-di-consegna-testo-non-json)
2. [JED+ Come Formato Standard delle Schede](#2-jed-come-formato-standard-delle-schede)
3. [Disciplina di Formattazione per Dialoghi ed Esempi](#3-disciplina-di-formattazione-per-dialoghi-ed-esempi)
4. [Evitare Oggetti e Tratti "Sempre Visibili"](#4-evitare-oggetti-e-tratti-sempre-visibili)
5. [Coerenza Visiva di Famiglia (Douglas) e Anatomia Demi-Umani](#5-coerenza-visiva-di-famiglia-douglas-e-anatomia-demi-umani)
6. [World Clock e Parametri Temporali](#6-world-clock-e-parametri-temporali)
7. [Triage Import Lorebook ed Architettura Lexicon World](#7-triage-import-lorebook-ed-architettura-lexicon-world)
8. [RPG Stats e Sistemi di Simulazione](#8-rpg-stats-e-sistemi-di-simulazione)
9. [Gestione Discrepanze nei Documenti Sorgente](#9-gestione-discrepanze-nei-documenti-sorgente)
10. [Precedenza di Lore per Dominio](#10-precedenza-di-lore-per-dominio)
11. [Fonti, Accesso al Web e Lavoro sul World via API](#11-fonti-accesso-al-web-e-lavoro-sul-world-via-api)
12. [Invecchiamento, Longevità e Filone SciFi](#12-invecchiamento-longevità-e-filone-scifi)
13. [Epurazione di `{{user}}` e Gestione Intimacy Profiles](#13-epurazione-di-user-e-gestione-intimacy-profiles)
14. [Pipeline Standard di Sviluppo Card](#14-pipeline-standard-di-sviluppo-card)
15. [Bug e Trappole Note della Piattaforma Wyvern](#15-bug-e-trappole-note-della-piattaforma-wyvern)
16. [Disciplina delle Attitudes](#16-disciplina-delle-attitudes)
17. [Protocollo Operativo per Database Locale SQLite Wyldfire (Sospeso)](#17-protocollo-operativo-per-database-locale-sqlite-wyldfire-sospeso)
18. [Standard Operativo per Chat di Gruppo Stand-Alone (/mine)](#18-standard-operativo-per-chat-di-gruppo-stand-alone-mine)
19. [Standard Operativo di Sessione e Skill Integrate](#19-standard-operativo-di-sessione-e-skill-integrate)

---

## 1. Formato di Consegna: Testo, Non JSON

**Default Assoluto:** Fornire sempre testo pronto da incollare nei campi dell'interfaccia web di Wyvern (`description`, `personality`, `first_mes`, `mes_example`, `system_prompt`, `post_history_instructions`, lorebook/NPC entries, outfit, tagline, shared info, ecc.), **NON file JSON completi**.

Il JSON va generato **esclusivamente** se:
- L'utente lo richiede in modo esplicito; oppure
- Serve come riferimento comparativo per verificare la coerenza incrociata tra più campi complessi (in tal caso, chiedere prima conferma all'utente se preferisce il file JSON o solo un riepilogo testuale).

*Principio dei Backup:* Il file JSON scaricato dall'utente **dopo** il salvataggio su Wyvern costituisce l'archivio storico di sicurezza, non un documento che l'assistente deve mantenere sincronizzato in parallelo.

### Eccezioni Operative
- **Scrittura diretta sul World via API (§11):** Il testo non passa campo per campo nella chat. Si consegna il **riepilogo puntuale** di cosa è stato scritto e dove, corredato da un documento di riepilogo nel Project con i valori precedenti (snapshot).
- **Lavoro locale su SQLite (§17, sospeso dal 22/09):** Vale solo se l'utente lo riattiva esplicitamente. Stessa logica: riepilogo in documento di Project senza dump di testo in chat.

---

## 2. JED+ Come Formato Standard delle Schede

Tutte le character card adottano obbligatoriamente il formato **JED+**:
1. Un blocco di attributi tra parentesi quadre, separati da punto e virgola (stile bracket/PList);
2. Sezioni narrative in prosa per backstory, dinamiche familiari/di gruppo, voce e comportamento;
3. Chiusura con una sezione tematica centrale del personaggio.

### Schema Strutturale JED+

```text
[NAME: ...; SPECIES: ...; AGE: ...; HEIGHT: ...; ... ]

BACKSTORY: ...

FAMILY & PACK: ...

VOICE & BEHAVIOR: ...

[sezione tematica finale, es. CORE TRAGEDY / THE WEIGHT HE CARRIES / THE SECRET HE CARRIES]
```

### Regole Specifiche sui Campi
- **Personaggi senza legame di branco:** Per figure aziendali, indipendenti o civili, la sezione `FAMILY & PACK:` si sostituisce con l'omologo pertinente (es. `CLAN AND COMPANY:` per Zeera), conservando la sequenza a quattro blocchi più chiusura tematica.
- **Campo `personality` (`summary` nella UI di Wyvern):** Va compilato con un blocco compatto di soli tratti tra parentesi quadre (stile PList puro), come riepilogo rapido separato dalla `description` estesa.
- **Import Grezzi:** Una scheda importata grezza col blocco `<nome_personaggio>` incollato tale e quale dalla fonte **NON è una scheda lavorata**. Va riscritta integralmente in JED+, non semplicemente ritoccata.
- **Età e Data di Nascita:** Per garantire piena compatibilità sia nelle chat stand-alone 1-on-1 (dove la timeline del World non è attiva e la macro `{{age}}` non viene valutata) sia all'interno del World, **non usare la macro `{{age}}`**. Indicare sempre nel campo `AGE` del blocco JED+ l'età anagrafica corrente e la data di nascita esplicita con la sintassi: `AGE: <età> (Born <Data>);` (o `BIRTHDAY: <Data>;`). Questo evita che il bot rimanga privo di età calcolata o mostri la macro non espansa quando utilizzato fuori dal World.

---

## 3. Disciplina di Formattazione per Dialoghi ed Esempi

Da applicare tassativamente a `first_mes`, `mes_example`, `alternate_greetings`, Dialogue Examples e a qualunque testo di esempio in-character o narrativo:

- **Divieto dell'Em-Dash:** Mai usare l'em-dash (`—`). Usare virgole (`,`) o punti (`.`).
- **Dialogo tra virgolette:** Parlato racchiuso esclusivamente tra virgolette inglesi doppie standard (`"..."`).
- **Azioni e narrazione in testo semplice:** Movimenti, descrizioni e prosa d'azione in testo semplice, **senza asterischi**.
- **Asterischi riservati ai pensieri interni:** Gli asterischi (`*...*`) sono destinati **esclusivamente** ai pensieri interni del personaggio (uso attualmente non ancora sfruttato, riservato per sviluppi futuri).
- **Lingue straniere:** `"Frase originale"` seguita da `([traduzione])`.
- **Divieto di Markdown nei testi del World:** Niente markdown nei testi del World. L'uso del grassetto con `**` vìola la regola sugli asterischi: il divieto vale anche nelle entry Lexicon e nelle descrizioni di Location ed Environment, non solo nei dialoghi.

### Istruzione Obbligatoria in `post_history_instructions`
Inserire sempre questa riga in coda a `post_history_instructions` (campo `final_instructions` via API):

> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."

---

## 4. Evitare Oggetti e Tratti "Sempre Visibili"

Definire accessori o elementi visivi come "always on" o "never removed" (es. bende di Malachia, tatuaggi di Logan, catena/anello/occhiali di Erik) induce l'LLM in loop continui, costringendolo a forzare l'elemento anche in contesti incoerenti (piscina, doccia, scene formali o intime).

**Regola:** Se un elemento visivo/accessorio non fa strutturalmente parte dell'anatomia del personaggio, non va descritto come costante. Due opzioni (in ordine di preferenza):
1. **Sistema Outfit Nativo di Wyvern (Soluzione preferita):** Utilizzare *Appearance & Outfits* definendo outfit distinti e contestuali (Allenamento, Casa/Casual, Formale, Notturno, ecc.).
2. **Descrizione Contestuale:** Se gli Outfit non sono ancora popolati, descrivere il tratto come legato al contesto nella prosa: *"X indossa Y solo quando Z; in altri contesti non è presente."*
3. **Eccezione Ammessa:** Un tratto può restare costante se e solo se la sua costanza *è* il personaggio e la scheda lo dichiara esplicitamente (es. il cappuccio di Dullahan non scende mai, in nessun contesto).

---

## 5. Coerenza Visiva di Famiglia (Douglas) e Anatomia Demi-Umani

- **Family Look Douglas:** I maschi della famiglia Douglas condividono un aspetto visivo comune nelle illustrazioni: capelli scuri lunghi e arruffati (per accomodare le orecchie lupine del Partial Shift), palette cromatica calda al tramonto con sfondi di Blackwood City (palme e architettura costiera), e struttura mascellare e facciale simile. Conservare comunque dettagli individuali (stile dei tatuaggi, cicatrici, tonalità degli occhi, accessori).
- **Anatomia Demi-Umani (Orecchie Singole):** **I demi-umani possiedono un solo paio di orecchie: quelle animali.** Non hanno un secondo paio di orecchie umane. Questa regola è confermata dall'autore originale e va verificata con estrema attenzione su ogni immagine o descrizione prodotta.

---

## 6. World Clock e Parametri Temporali

- **World-Age 0 (Epoca di Riferimento):** 21 dicembre 827 d.C., ore 00:00 UTC.
  - Parametri API del World:
    - `human_start_date: "0827-12-21T00:00:00.000Z"`
    - `calendar.start_year: 827`
    - `start_month_id: "dec"`
    - `start_day_of_month: 21`
- **Anno Corrente del World:** **2024**.
- **World-Age Attuale:** **10486470** (equivalente al **5 aprile 2024, ore 06:00 UTC**, riconfermato via API il 14 settembre). Ignorare riferimenti legacy al 2022.
- **Formula Ore Assolute (Calendario Gregoriano Prolettico):**
  $$\text{ore} = (\text{giorni trascorrenti dall'Epoca}) \times 24 + \text{ora del giorno}$$

### Snippet di Calcolo e Verifica (JavaScript)

```javascript
const EP = Date.UTC(827, 11, 21); // 21 Dicembre 827 UTC
const dataDaOre = h => new Date(EP + h * 3600000).toISOString().slice(0, 10);
const oreDaData = iso => (Date.parse(iso) - EP) / 3600000;
```

### Controlli di Integrità Temporale
1. Per ogni personaggio vivente, `birthdate` e `start_timeline_position` devono **coincidere**.
2. Nessuna delle due può risultare superiore a `world_age` corrente (10486470).
3. La `start_timeline_position` va impostata **sempre** per ogni personaggio (evita intrusioni anacronistiche negli scenari storici o futuri).

---

## 7. Triage Import Lorebook ed Architettura Lexicon World

- **Personaggi Vivi Nativi:** Entrano come **Character** con **Start Position**.
- **Personaggi Stand-Alone (`/mine`):** Vengono collegati al World tramite **Linked Characters** (`linked_characters`, in `ws=library&tab=linked-characters`), fungendo da Single Source of Truth condivisa tra 1-on-1 e World.
- **Personaggi Deceduti:** Entrano come **Character** con **Start Position** ed **End Position** (modello Nixara; non vanno più nel Lexicon).
- **Confinamento World Characters:** Superamento del Global Character ON generalizzato. Solo i 5 Douglas principali (Malachia, Noah, Jasper, Erik, Alyssa) mantengono **Global Character = ON**. Tutti gli altri 108 World Characters devono avere **Global Character = OFF** (`is_global: false`), caricandosi unicamente se presenti nella Location corrente o nel Party attivo.

### World Lean Architecture & Confinamento Lexicon
Per impedire che il prompt inviato all'LLM superi il Context Budget di Wyvern e provochi il troncamento della cronologia di chat:
- **`is_global: true` Riservato:** Consentito esclusivamente per un nucleo ristretto di concetti cosmologici e biologici universali (~30 voci max: LSE, fisiologia licantropi/vampiri, vulnerabilità argento/aconito, ciclo solare/notturno).
- **Tutte le altre voci (`is_global: false`):** Tutti i 284 NPC minori nel Lexicon, i 51 item di negozio, i 16 contratti di lavoro, le 19 memorie personali, e le entry specifiche di confraternite/negozi devono avere tassativamente `is_global: false`.
- **Soglia di Sicurezza Context Budget:** La somma dei metadati statici del World (Istruzioni avanzate + Location + Rotte + RPG State + Voci Lexicon scattate + Personaggi) non deve mai superare i **5.000 token**, garantendo che almeno il 70% della finestra di contesto rimanga sempre riservata alla cronologia di chat e all'input dell'utente.

### Matrice di Triage

| Tipologia Sorgente | Azione nel World |
|---|---|
| **Species Details / Intimacy Profile** | Non importare nella description; creare Lexicon separata `memory` con `party_conditions` (§13). |
| **Personaggio vivo ricorrente in più file** | Creare una sola volta come Character con Start Position o collegare da Linked Characters. |
| **Personaggio deceduto** | Creare come Character con Start ed End Position. |
| **Luogo già mappato come Location** | Non importare il duplicato. |
| **Attività o concetto astratto** | Importare come voce di **Lexicon**. |
| **Luogo fisico non ancora mappato** | Importare come **Location**. |
| **Gruppo secondario off-world** | Accorpare in un'unica entry Lexicon ricca (es. "The Other Contractors"). |
| **Lore generale di specie** | Lexicon `lore/concept`, `is_global: true`, panoramica ampia senza dettagli intimi. |
| **Riproduzione / anatomia intima di specie** | Lexicon `memory`, `is_global: false`, keys su nome specie + argomento, registro enciclopedico. |

### Tassonomia Ufficiale Entry Type del World Lexicon
- **Testo puro:** `lore/concept`, `organization/faction`, `memory`, oppure nessun tipo.
- **Con pannelli di configurazione:** `item`, `furniture`, `creature`, `move`, `nature`, `ability`.
- *Nota:* Il tipo `mob` non esiste. Usare `lore/concept` per lore di specie, e `creature` per mostri/nemici.

### Regola di Lys per Entry Monopersonaggio
Ogni voce di Lexicon focalizzata su un singolo personaggio (Intimacy Profiles, Digital Interactions, ricordi personali, note comportamentali):
1. **Entry Type = Memory** (`type: "memory"`);
2. Collegata all'id attuale del personaggio tramite **Attached Character** (`attached_world_character_id`).
3. Le memorie corali (eventi collettivi, log di gruppo) rimangono senza Attached Character.

### Attivazione delle Entry Lexicon
- `is_global: false` disattiva l'entry dalla scansione a parole chiave: diventa idonea solo se inserita esplicitamente in `included_lexicon_entries` di una Location, Environment o Scenario con match di chiavi o `constant: true`.
- `attached_world_character_id` non funge da trigger d'inclusione automatica.
- **Filtri corretti:** `keys` (primarie = nome/specie) + `secondary_keys` (parole tematiche) con `key_logic: "AND_ANY"`, associati a `party_conditions` (`has_any [id_personaggio]`).

---

## 8. RPG Stats e Sistemi di Simulazione

- **Stato del Modulo & World Features:** In seguito all'ottimizzazione del Context Budget (World Lean Architecture):
  - `inventory: true`, `currency: true`, `rpg_stats: true`, `combat: true`, `relationships: true`.
  - Disattivati per evitare il dump di tabelle nel prompt: `show_party_stats: false`, `show_species_info: false`.
  - Disattivati perché estranei al canone del World: `ships: false` (Cross-World Ships) e `creature_catcher: false` (Creature Catcher).
- **Convenzioni RPG e Parametri di Bilanciamento:**
  - Budget fisso a **25 punti** (somma finale delle 6 stat uguale a **31** con base 1).
  - Statistiche: `stat_1` (MGT), `stat_2` (RES), `stat_3` (AGI), `stat_4` (WIT), `stat_5` (PRS), `stat_6` (SCT).
  - Livello = Età anagrafica (fino a 99).
- **Bug Critico del Livello & Tetto a 99:** Un Livello $\ge 100$ blocca silenziosamente il salvataggio dell'intero blocco RPG. Per tutti i personaggi ultracentenari impostare tassativamente **Livello = 99**, riportando l'età reale nel blocco JED+.
- **Species e Occupation via API:** I selettori web non salvano Species e Occupation (tornano a None). Vanno scritti via API dentro `rpg_stats` (`rpg_stats.species_id` e `rpg_stats.occupation_id`). Selezionare l'Occupation concettualmente più vicina tra i 18 blueprint disponibili.

### Protocollo di Formulazione RPG & Dossier Integrale Obbligatorio
È fatto divieto assoluto a qualsiasi assistente AI di proporre, generare o modificare tratti RPG, occupazioni, razze, classi o statistiche basandosi su dati parziali, intuito o inferenze dal solo nome del personaggio.
1. **Lettura Integrale del Dossier:** Prima di qualsiasi proposta o modifica, l'assistente deve recuperare e leggere l'intero testo descrittivo del personaggio (`long_summary`, `description`, `voice & behavior`, `attitudes`) e le relative voci enciclopediche del Lexicon.
2. **Matrice Tassonomica Vincolante delle Stirpi Dinastiche:**
   - `Divine Blood`: riservato **esclusivamente** ai tre Firstborn primordiali (`Wulfnic`, `Zefir`, `Ut`). Nessun altro personaggio, inclusi i discendenti Douglas, può possedere questo tratto.
   - `Founding Bloodline`: riservato a Nixara, ai Firstborn e alla seconda generazione di sangue misto Douglas-Bloodmoon (`Alyssa`, `Jasper`, `Malachia`, `Noah`). Non appartiene a Erik né a Logan.
   - `Pureblood Lineage`: riservato alle casate storiche di pura discendenza: Douglas (`Erik`, `Logan`, `Edric`, `Magnus`, `Cornelius`), Duskwood (`Elizabeth`), Wolfwood (`Archer`), Rogers (`Mackenzie`).
   - *Doppia Linea di Sangue:* I quattro gemelli/fratelli Douglas-Bloodmoon (`Alyssa`, `Jasper`, `Malachia`, `Noah`), discendendo sia da linea Douglas che Bloodmoon, possiedono contemporaneamente sia `Founding Bloodline` che `Pureblood Lineage`.
3. **Invarianti Assolute di Sottogenere Lupino (LSE):**
   - **Noah Loki Douglas Bloodmoon:** È tassativamente un **Delta** (Eminenza Grigia, mente diplomatica e finanziaria; zero tratti Alpha, zero Alpha Command).
   - **Jasper Svartr Douglas Bloodmoon:** È tassativamente un **Beta** (braccio destro operativo e tecnologico di Malachia; zero tratti Alpha).
   - **Logan Dominic Járn Douglas:** È tassativamente un **Beta** (braccio destro, mediatore pacificatore di Erik; zero tratti Alpha).
   - **Malachia Björn Douglas Bloodmoon:** È un **Dominant Alpha** (futuro Pack Leader designato; possiede i tratti *Pack Leader*, *Ascended Enigma* ed *Apex Core Resonance*).
   - **Erik Ulfr Douglas:** È un **Prime Alpha** (Pack Leader in carica della Casata Douglas; possiede i tratti *Pack Leader*, *Dominant Alpha*, *Alpha Command*).
   - **Kemonomimi Demi-Umani (es. Finn Novak, Roman Blackwood):** Non sono licantropi (nessun Partial o Hybrid Shift, nessuna allergia all'argento, nessuna frenesia o rigenerazione lunare; possiedono un solo paio di orecchie animali).

---

## 9. Gestione Discrepanze nei Documenti Sorgente

1. **Criterio di Consenso:** In caso di dati contrastanti, scegliere il valore con maggiore consenso tra le fonti; a parità, affidarsi alla fonte gerarchicamente superiore (§11).
2. **Documentazione nel Project:** Registrare la discrepanza esatta in un documento del Project. Nello schema Character di Wyvern **non esiste il campo `creator_notes`**.
3. **Integrità dei Sorgenti:** Non modificare i file originali senza autorizzazione dell'utente.
4. **Divieto di Invenzione:** Non inventare dettagli arbitrari per colmare buchi. Schede redatte a intuito vanno riscritte integralmente all'arrivo delle fonti ufficiali.
5. **Verifica Rigorosa alla Fonte:** Non assumere per assodato un dettaglio citato di seconda mano; verificare sul testo d'origine (evitare casi come "Bulls vs Claws" invece di "CLAMS", o schede duplicate con nuovi id).
6. **Date Inventate Credibili:** Quando è indispensabile creare date non presenti nelle fonti, evitare il ricorso sistematico al 1° gennaio o al primo del mese; scegliere date varie e verosimili.
7. **Scelte Delegate all'Assistente:** Quando l'utente affida una decisione (es. età anagrafica congrua), proporre un valore motivato e attendere conferma prima di scrivere sul World.
8. **Protocollo di Verifica Preventiva alla Fonte e Divieto Assoluto di Inferenza:** È vietato proporre, generare, inserire o aggiornare qualsiasi informazione su personaggi, fazioni, specie, classi RPG, relazioni o lore (razza, anatomia, età, sottogenere LSE, ruoli, poteri) sulla base di deduzioni, intuito, inferenze dal nome o memorie parziali.
   - *Consultazione Primaria Obbligatoria:* prima di ogni proposta o scrittura, reperire e leggere integralmente la scheda sorgente originale (profili Wyvern come Kakihara, schede JanitorAI originali, dossier in `ARCHIVIO/`, Lorebook di riferimento).
   - *Citazione del Dato Letterale:* ogni attributo fondamentale (specie, occupazione/classe, parentela, tratti distintivi) va corroborato citando la fonte specifica verificata.
   - *Divieto di Riempimento a Indovinare:* se un dato manca nella fonte, non va inventato; dichiararne l'assenza e chiedere una decisione canonica all'utente prima di procedere.

---

## 10. Precedenza di Lore per Dominio

| Ambientazione | Autore | Dominio Territoriale / Concettuale |
|---|---|---|
| **Underworld** | Autore esterno | Los Angeles |
| **SUCC / Modern Fantasy** | Autore esterno (*io wuvs soap*) | Solarton, campus SUCC, Hex Valley, CUMS |
| **Blackwood / Douglas** | Lys | Blackwood City, famiglia e branco Douglas |
| **DDM Inc.** | Autore esterno (*io wuvs soap*) | Voidspace (universo separato) |

- **La precedenza si applica per dominio territoriale/concettuale:** In caso di collisione, prevale sempre l'autorità dell'ambientazione a cui appartiene il dominio in questione.
- **Caso Specifico DDM Inc.:** Vale in modo assoluto sul proprio dominio (Contratti, Original Death, ACES, ARC Level, SERAPHIM, realtà lacerate). Non ha invece alcuna autorità sul suolo californiano: gergo e concetti DDM non circolano a Blackwood o Solarton, e l'ARC Level è del tutto sconosciuto. Dullahan opera come Coach D con le regole locali, e come #04 con le regole DDM.
- **Personaggi Importati da Altri Universi dell'Utente (Zeera, Yael, Huck):** Non sono canone esterno fisso ma materiale proprio riscrittibile liberamente; backstory e ruoli vanno ricostruiti da zero per armonizzarsi con Blackwood.
- **Tracciamento Adattamenti:** Gli adattamenti canonici vanno registrati nel Project evidenziando fonte, resa nel World e logica di compatibilità.

---

## 11. Fonti, Accesso al Web e Lavoro sul World via API

- **Sito Wyvern come Fonte di Verità:** `app.wyvern.chat` è l'unica sorgente attiva. Il lavoro avviene direttamente sulla piattaforma web o tramite chiamate API mirate.
- **Divieto di Fetch Diretto:** Nessuna consultazione tramite fetch HTTP grezzo; ogni risorsa web (wiki, Discord) va consultata dal browser locale.
- **Gerarchia Fonti Lore Originale:**
  1. Lorebook ufficiali Discord (*IOVERSE LOREBOOKS*: `SUCC_-_U_-_VERSE.json`, `Dead_Dog_Motel.json`, ecc.).
  2. Risposte dell'autore (*io wuvs soap*) nel canale `ioverse-q-n-a`.
  3. Portale ufficiale SUCC (`io-succ.uwu.ai`).
  4. Wiki Fandom e fonti terze.
- **Gerarchia Fonti Documentali Piattaforma:**
  1. *WyvernWiki* (`https://wiki.wyvern.chat/`, guide sotto `/en/Features/Worlds/...`).
  2. Canale `#dev-notes` su Discord per novità in anteprima.
  3. Reddit (`r/WyvernChat`) e canali di supporto.
  *Se la wiki diverge dalla piattaforma:* Fa fede il dato empirico verificato tramite GET autenticata fresca.

### Riferimenti Ufficiali WyvernWiki per Funzionalità Avanzate e Soluzioni Complesse
Consultare tassativamente queste risorse ufficiali per l'implementazione di logiche complesse, scripting, templating e formattazione:
- **World & Architecture Hub**: [Features/Worlds](https://wiki.wyvern.chat/Features/Worlds)
- **Advanced Lexicon (Categorize Entries & Register NPCs)**: [Advanced/Lexicon](https://wiki.wyvern.chat/en/Advanced/Lexicon)
- **Pronoun Pruned Prose (PPP) Character Guide**: [Guides/PPP-Character-Format](https://wiki.wyvern.chat/en/Guides/PPP-Character-Format) e [Features/Worlds/Characters](https://wiki.wyvern.chat/en/Features/Worlds/Characters)
- **Handlebars nei World**: [Features/Worlds/handlebars](https://wiki.wyvern.chat/en/Features/Worlds/handlebars)
- **Advanced Handlebars**: [Advanced/Handlebars](https://wiki.wyvern.chat/en/Advanced/Handlebars)
- **Lua nei World**: [Features/Worlds/Lua](https://wiki.wyvern.chat/en/Features/Worlds/Lua)
- **Advanced Lua**: [Advanced/Lua](https://wiki.wyvern.chat/en/Advanced/Lua)
- **Story Engine Lua-Handlebars**: [Features/StoryEngine/Lua-Handlebars](https://wiki.wyvern.chat/en/Features/StoryEngine/Lua-Handlebars)
- **Inline Chat Commands**: [Features/Worlds/Inline-Chat-Commands](https://wiki.wyvern.chat/en/Features/Worlds/Inline-Chat-Commands)
- **Boosts & Supporter Shoutouts**: [Features/Worlds/boosts-supporter-shoutouts](https://wiki.wyvern.chat/en/Features/Worlds/boosts-supporter-shoutouts)
- **How to Chat Guide**: [Guides/How-to-Chat](https://wiki.wyvern.chat/en/Guides/How-to-Chat)
- **Prohibited Content Guide (Safety & Content Policy)**: [Policies/Prohibited-Content-Guide](https://wiki.wyvern.chat/en/Policies/Prohibited-Content-Guide)

### Regole per l'Uso Sicuro dell'API
- **Lettura (GET):** Libera e sempre consentita senza autorizzazione preventiva.
- **Modifiche Mirate (PUT / POST):**
  1. Snapshot preventivo dei valori precedenti con GET fresca.
  2. Identificazione unicamente per `id` attivo (mai per nome).
  3. **Body parziale obbligatorio:** Inviare solo i campi modificati (il PUT completo con tutto l'oggetto restituisce 200 ma non salva niente).
  4. **Sostituzione completa degli array:** Gli array non eseguono merge; leggere l'array esistente, aggiornarlo in memoria e ritrasmetterlo completo.
  5. **Verifica GET post-scrittura:** Lo status HTTP 200 non è una prova; rileggere l'entità per validare l'effettiva persistenza.
- **Operazioni in Blocco (> 10 entità):** Presentare il piano all'utente, attendere approvazione, operare a lotti di massimo 25 con memorizzazione dello stato.
- **Cancellazioni (DELETE):** Solo su richiesta esplicita con indicazione puntuale dell'entità. Salvare prima l'intero oggetto nel Project; una chiamata alla volta (mai in loop).

### Protocollo Anti-Data Loss per Lorebook Stand-Alone (/mine)
1. **Divieto Assoluto di Overwrite Massivo:** È fatto divieto tassativo a qualsiasi script o assistente AI di eseguire riscritture complete o sovrascritture di massa dell'array `lexicon` sui Lorebook stand-alone (`/api/lorebooks/:id`).
2. **Integrità dei Lorebook:** I Lorebook stand-alone in `/mine` costituiscono Single Source of Truth storica e manuale. Qualsiasi sincronizzazione o inserimento deve avvenire in modalità "append puntuale" singola voce, con verifica preventiva di schema e mai in sostituzione cieca dell'intero archivio.
3. **Backup Preventivo Obbligatorio:** Prima di qualsiasi operazione di scrittura su entità di libreria, scaricare e persistere una copia integrale JSON su disco locale.
4. **Context Budget Awareness:** Nelle richieste al World, monitorare che la somma dei metadati statici non superi mai i 5.000 token prima della chat history per evitare il troncamento della richiesta da parte del backend di Wyvern.
5. **Preservazione Obbligatoria Metadati Top-Level nei Lorebook:** L'endpoint `PUT /api/lorebooks/:id` non esegue merge parziale: inviare solo `{ lexicon }` cancella i campi top-level (`name`, `description`, `scan_depth`, `token_budget`, `recursive_scanning`, `visibility`, `rating`, `is_private`). In qualsiasi chiamata di aggiornamento è obbligatorio trasmettere sempre l'intero blocco di configurazione del Lorebook insieme all'array `lexicon`.

### Tipizzazione Rigorosa di `priority` e Validazione Schemi Zod
Il backend di Wyvern valida le voci di contesto, lorebook, scenari e lexicon tramite schemi Zod che impongono per il campo `priority` il tipo `z.number()`.
- L'assegnazione di valori stringa (es. `priority: "0"`, `"10"`, `"high"`) scatena un errore HTTP 500 fatale (`Expected number, received string, path: ["priority"]`) che inibisce la ricezione o l'invio di messaggi in chat.
- In ogni script o funzione di creazione/modifica entità, convertire esplicitamente: `priority: Number(val) || 0`.

### Protocollo di Pulizia Post-Diagnostica (Zero-Footprint Testing)
Quando vengono avviate procedure di diagnosi, indagine o test che comportano la creazione programmata di entità temporanee via API (chat log di test come `chat_log_...`, party usa-e-getta o scenari sandbox):
1. **Tracciamento:** Lo script o l'agente deve memorizzare immediatamente in memoria o su scratch gli ID di ogni entità temporanea creata.
2. **Cancellazione Tempestiva:** A diagnosi completata (o in caso di errore), è obbligatorio eseguire la cancellazione sistematica delle entità create (`DELETE /api/new/chat-logs/:id`) per garantire che l'account e la libreria dell'utente rimangano perfettamente puliti e privi di artefatti orfani.

### Note Tecniche API
- Base URL: `https://app.wyvern.chat/api/...`
- Token scaduto (dopo 1 ora): produce 404 su GET e 401 su PUT. Rinfrescarlo leggendo il refresh token in `firebaseLocalStorageDb` (`firebase:authUser:<apikey>:[DEFAULT]`) e richiedendone uno nuovo a `securetoken.googleapis.com`.
- Eseguire gli script sempre nella scheda browser attiva di Wyvern.
- Campi Character: `display_name` per il nome, `long_summary` per la descrizione.
- Campi annidati RPG: `species_id` e `occupation_id` risiedono dentro l'oggetto `rpg_stats`.

---

## 12. Invecchiamento, Longevità e Filone SciFi

### Founding Bloodline e Divine Blood
- **Founding Bloodline:** Malachia, Noah, Jasper, Alyssa.
- **Divine Blood (I Nove Firstborn):** Wulfnic, Ut, Zefir.
- Maturità completa a 21 anni, poi stop biologico dell'invecchiamento. I Firstborn sono bloccati all'età della consacrazione da parte di Fenris:
  - *Wulfnic e Ut:* Aspetto di quarantenni del loro secolo (equivalente moderno: circa 60 anni).
  - *Zefir:* Ha **1019 anni** (nato il 5 febbraio 1005). Consacrato prima della fine dello sviluppo, dimostra 18-19 anni; per il diritto norreno dell'XI secolo era un adulto maggiorenne e guerriero.
- **Filone SciFi:** Varianti future legacy (Malachia "Vanguard Commander", Jasper/Noah/Malachia con impianti cibernetici pesanti e specie *Cyber-Werewolf* nell'anno 2499) sono canoniche per lo scenario futuro.

### Pureblood Houses
- Aspettativa di vita: **200 – 400 anni**. Invecchiamento lento ma non del tutto congelato.
- Possibilità di promozione di famiglie storiche da Common a Pureblood previa approvazione dell'utente (casi confermati: Marino, O'Connor). Comporta Livello RPG 99 e aggiornamento di `SPECIES`, `birthdate` e `start_timeline_position`.

### Common Bloodline
- Aspettativa di vita: **60 – 80 anni** (media umana; logorio rapido e mortalità per conflitto).
- Invecchiamento visivo: sviluppo fino a 25 anni, poi **1 anno di aspetto ogni 5 vissuti** (a 50 anni ne dimostrano 30; a 70 poco più di 34), con tracollo repentino negli ultimi anni di vita. Fertilità in discesa dai 35 anni.
- *Età Apparente vs Reale:* L'età apparente delle fonti va usata nella descrizione fisica; l'età anagrafica va calibrata dall'autore della scheda e confermata con l'utente.

### Canone Visivo
**L'aspetto esteriore non rivela il sangue.** Chi dimostra 30 anni può essere un Common di 50, un Pureblood di 200 o un Firstborn millenario. Nessun personaggio deduce il sangue guardando in faccia un altro: contano odore, portamento ed aura.

---

## 13. Gestione Contenuti, Allineamento Policy Wyvern e Piena Libertà Espressiva (Unchained)

Il World Svartúlfr adotta una politica di **completa libertà espressiva per il genere Adult / Explicit**, rimuovendo qualsiasi autocensura o limitazione artificiale e vincolandosi **esclusivamente ed unicamente alle linee rosse ufficiali stabilite dalla [Wyvern Prohibited Content Guide](https://wiki.wyvern.chat/en/Policies/Prohibited-Content-Guide)**.

### Le Uniche Linee Rosse della Policy Wyvern (Vincoli Tassativi)

1. **Tutela dei Minori (Policy #1 — Tolleranza Zero):**
   - Qualsiasi personaggio coinvolto in romance, attrazione, seduzione, intimità o scene sessuali deve avere età anagrafica formalizzata **18+** (`AGE: {{age}}`).
   - I personaggi minorenni (es. **Edric Douglas**, 12 anni) sono categorizzati **esclusivamente come minor background NPC** con divieto assoluto di framing romantico, intimo o sessuale (*"strictly minor background NPC: zero romantic or intimate framing under any circumstances"*).
   - Divieto assoluto di romance, flirting, grooming o sessualizzazione di minorenni o studenti delle scuole superiori. Elementi di traumi o abusi passati sono ammessi nella lore/backstory solo se il personaggio è attualmente maggiorenne (18+), senza descrizioni grafiche o morbose e senza alcuna glorificazione o feticizzazione.
2. **Divieto Bestialità verso Animali Reali (Policy #2):**
   - È vietata qualsiasi attività sessuale verso animali del mondo reale.
   - **Licantropi, Demi-umani, Furry e Creature Fantasy/Mostruose sono pienamente ammessi** in relazioni romantiche, passionali ed intime purché rispettino l'**Harkness Test** (senzienti, capaci di comunicare tramite linguaggio verbale/articolato e biologicamente adulti per la propria specie).
3. **Divieto Necrofilia e Guro (Policy #3):**
   - Violenza fisica, ferite, combattimento viscerale, sangue, cicatrici e morte sono pienamente ammessi nel roleplay e nelle descrizioni (coerentemente con il rating *Explicit*). È vietata unicamente la feticizzazione o sessualizzazione di cadaveri, membra recise o agonia (guro).
   - Personaggi non-morti senzienti (vampiri, revenant) sono ammessi purché privi di descrizioni grafiche di decomposizione sessualizzata.
4. **Divieto Scat, Fart, Vomit, STD Fetish (Policy #4).**
5. **Divieto Hate Speech verso Gruppi Reali (Policy #5):**
   - Faide, discriminazioni fantastiche e conflitti in-universe (es. branchi vs congreghe, lupi vs vampiri, gerarchie Alpha/Omega, tensioni sociali tra purosangue e mezzosangue) sono **100% ammessi e incoraggiati**. Vietato solo l'odio verso gruppi o individui reali protetti.
6. **Divieto di Prompt di Sistema NSFL (Policy #6):**
   - Non inserire prompt come `"Explicit NSFL content is permitted"`.
7. **Divieto Personalità Pubbliche Reali Viventi (Policy #7).**

---

### Contenuti Sbloccati e Rimozione Limitazioni Autoimposte (Boost al World)

Cadono tutte le precedenti limitazioni prudenziali che frenavano l'intensità e la ricchezza del World:

1. **Sblocco Totale di Romance, Passione, Cotte e Tensione Sessuale:**
   - I personaggi adulti (18+) possono provare attrazione, fascinazione erotica, desiderio, cotte, chimica passionale e seduzione esplicita.
   - La macro `{{user}}` non viene hardcodata nella prosa per preservare la flessibilità sistemica AnyPOV, ma i personaggi **non devono essere sterilizzati o emotivamente asettici**: possiedono una spiccata reattività emotiva, istinti di accoppiamento, vulnerabilità intima e pulsioni fisiche vive.
2. **Sblocco Dinamiche di Potere, Università e Taboo Consenzienti (18+):**
   - Nel contesto SUCC e Blackwood, essendo tutti i personaggi del corpo studentesco e docenti maggiorenni (18+), sono pienamente ammesse dinamiche mature: rivalità seduttive, relazioni professore-studente adulto, coach-atleta adulto, boss-subordinato, contratti di branco e dinamiche di sottomissione/dominanza.
3. **Piena Integrazione della Biologia LSE (Lupine Social Ecology):**
   - Gli istinti biologici dei licantropi (Heat, Rut, Knotting, Baculum, Mating Bond, Scent Marking, Pheromones, Biting, Claiming, Breeding instincts) costituiscono lore primaria del mondo e possono essere integrati direttamente nella `description`, nei tratti e nel comportamento, senza bisogno di essere censurati o nascosti.
4. **Combattimento Viscerale e Linguaggio Senza Filtri:**
   - Libertà di linguaggio realistico, crudo o volgare se coerente con la voce del personaggio. Combattimenti brutali, sfide per la gerarchia di branco, lotte clandestine e missioni letali nei dungeon sono pienamente autorizzati.
5. **Intimacy Profiles & Kink Lore:**
   - Possono essere strutturati come voci Lexicon di tipo `memory` collegate al personaggio (`attached_world_character_id`), oppure inseriti direttamente nei tratti e sfumature comportamentali del personaggio per guidare il roleplay intimo ad alto coinvolgimento narrativo.

---

## 14. Pipeline Standard di Sviluppo Card

Seguire tassativamente la sequenza di 13 passi:

1. **Raccolta Fonti:** Audit completo dei documenti ufficiali e verifica su WyvernWiki.
2. **Controllo Duplicati:** Query GET via API per verificare se il personaggio esiste già nel World.
3. **Epurazione `{{user}}` e Bonifica:** Applicazione rigorosa di §13.
4. **Scrittura Campi Testuali:**
   - `long_summary` in JED+ (§2) con macro `{{age}}`.
   - `summary` come PList puro di tratti.
   - `display_description` incisiva (1-2 righe).
   - Nickname, titoli, keys, pronomi.
5. **Cinque Outfits Contestuali:** Uno alla volta da UI; array completo in unico payload da API (§4).
6. **Default Outfit:** Obbligatorio; scegliere l'abito ordinario di routine.
7. **Start Position:** Ore calcolate dal World Clock (§6). End Position solo se deceduto.
8. **RPG Stats:** In pausa di default (§8). Se attivo: 25 pt, livello (cap 99), Species e Occupation via API.
9. **Cinque Dialogue Examples:** Senza em-dash, senza asterischi, parlato tra virgolette (§3). Almeno un esempio nel momento di massima vulnerabilità.
10. **Attitudes:** Alyssa e Jasper obbligatori, più legami citati nel background (§16).
11. **Global Character = ON:** Attivare il flag globale.
12. **Verifica Finale:** Reload o GET fresca: zero `{{user}}`, zero em-dash, zero asterischi, campi saldi, Intimacy Profile collegato.
13. **Documentazione nel Project:** Registrare le decisioni, collegamenti e discrepanze.

---

## 15. Bug e Trappole Note della Piattaforma Wyvern

- **Save Appeso in UI:** La UI rimane su "Saving...". I dati spesso risultano salvati; ricaricare ed effettuare GET di verifica senza insistere con clic ripetuti.
- **Species e Occupation da UI:** Tornano a `None` dopo il reload; persistono solo se salvati via API nell'oggetto `rpg_stats`.
- **Livello RPG $\ge 100$:** Causa il fallimento silente del salvataggio RPG; impostare tetto a 99.
- **Array Sovrascritti in UI:** Aggiungere outfit uno alla volta con salvataggio intermedio. Via API, trasmettere sempre l'intero array aggiornato.
- **`linked-characters` 500:** Errore interno della piattaforma; ignorare la chiamata senza bloccare le card.
- **PUT con Oggetto Completo:** Risponde 200 ma non aggiorna nulla; usare solo body parziali mirati.
- **Token Scaduto:** Causa 404 su GET e 401 su PUT; rinfrescare il token tramite `securetoken.googleapis.com`.
- **Entry Orfane post-ricreazione card:** Ricreando una card con nuovo ID, le vecchie Lexicon rimangono agganciate al vecchio ID; aggiornare manualmente `attached_world_character_id` e `party_conditions`.
- **Cartelle Collassate UI:** Si espandono cliccando unicamente la chevron iniziale, non il testo. In alternativa, query API.
- **Combobox e Textarea:** Non recepiscono affidabilmente eventi sintetici JavaScript; operare con modifiche mirate via API.
- **Parent Location:** Su nuove Location, il campo Parent si popola solo dopo aver salvato la Location una prima volta.
- **Wipe Metadati Lorebook via PUT:** L'endpoint `PUT /api/lorebooks/:id` non effettua merge parziale. Inviare un body contenente solo `{ lexicon: [...] }` svuota silenziosamente i campi top-level (`name`, `description`, `scan_depth`, `token_budget`, `recursive_scanning`, `visibility`, `rating`, `is_private`). In qualsiasi chiamata è obbligatorio trasmettere sempre l'intero blocco di metadati del Lorebook (`name`, `description`, `scan_depth: 5`, `token_budget: 5000`, `recursive_scanning: true`) assieme al lexicon.
- **Priority come Stringa (Errore Zod 500):** `Expected number, received string, path: ["priority"]` manda in crash il server Wyvern (HTTP 500) bloccando la ricezione o l'invio di messaggi nella chat. Forzare sempre la tipizzazione numerica esplicita: `priority: Number(val) || 0`.
- **Orfani da Testing (Zero-Footprint):** I chat log e i party temporanei creati per test diagnostici restano visibili nella UI utente e inquinano la libreria. Eseguire sempre il teardown sistematico (`DELETE /api/new/chat-logs/:id`) al termine di ogni sessione di test.

---

## 16. Disciplina delle Attitudes

- **Alyssa e Jasper Obbligatori:** Devono figurare su ogni scheda; se mai incontrati, usare tier `stranger` e spiegare che non si sono mai incrociati.
- **Personaggi Citati nel Background:** Inserire solo figure con legami espliciti o relazioni gerarchiche di branco/concilio; garantire reciprocità se citate sulla scheda dell'altro.
- **Target Type:** `World Character` per personaggi del World; `Generic (text)` per fazioni (es. stance verso *Humans First*).
- **Tier API vs Ladder Grafica:** L'API accetta solo le chiavi grezze standard (`stranger`, `acquaintance`, `friend`, `close_friend`, `best_friend`, `disliked`, `despised`, `hated`, `enemy`, `rival`, `wary`, `acknowledged`, `romantic_interest`). La ladder visuale LSE a schermo (Blood Enemy, Beloved, ecc.) è una pura etichettatura grafica e non crea nuove chiavi.
- **Intensity (Obbligatoria):** Non lasciare vuota (salverebbe valore 1):
  - `15`: Mai incontrati.
  - `20 – 25`: Conoscenza vaga.
  - `50`: Rapporto standard / professionale.
  - `85`: Legame viscerale o cardine identitario.
- **Reasoning:** 1-2 frasi sull'origine della dinamica.
- **The Player (Persona):** Vietato per sentimenti verso singoli soggetti.

---

## 17. Protocollo Operativo per Database Locale SQLite Wyldfire (Sospeso)

- **Sospeso dal 22 Settembre:** La sorgente di verità è il sito web Wyvern. L'uso del database locale è disattivato per evitare la generazione di ID duplicati e voci orfane.
- **Ciclo di Sicurezza (In caso di esplicita richiesta di riattivazione):**
  1. Percorso: `C:\Users\<utente>\AppData\Roaming\com.wyvern.wyldfire\wyldfire.db`.
  2. Backup incrementale obbligatorio (`wyldfire.db.backupN-<timestamp>`).
  3. Esecuzione esclusiva via script Python controllati (`sqlite3`).
  4. Verifica con `PRAGMA integrity_check;` e conteggi attesi.
  5. Conferma esplicita di chiusura completa dell'app desktop Wyldfire prima di operare.
  6. Bonifica totale dei file temporanei `-wal` e `-shm`.
  7. Documentazione nel Project e audit via API delle entry Lexicon orfane dopo la pubblicazione su Wyvern.

---

## 18. Standard Operativo per Chat di Gruppo Stand-Alone (/mine)

Nelle sessioni di gioco giocate al di fuori del World (Chat di Gruppo stand-alone con 2-6 personaggi di `/mine`):

1. **Architettura delle Schede in `/mine`:**
   - Ogni scheda in `/mine` deve avere un peso calibrato tra **1.000 e 1.500 token** per preservare il context window del gruppo.
   - Disciplina di formattazione rigorosa: dialoghi tra virgolette inglesi doppie standard (`"..."`), narrazione in testo semplice senza asterischi, asterischi riservati solo ai pensieri, divieto assoluto dell'em-dash (`—`).
   - Anatomia demi-umani: un solo paio di orecchie (solo orecchie animali).
2. **Disaccoppiamento dello StoryEngine:**
   - Nella definizione dello StoryEngine (`engine_HCTPXhL8xr89wUY9r9dYU`), l'array `worlds` deve essere impostato su `[]` (`definition.worlds = []`).
   - Questo impedisce all'engine di tentare di risolvere, scansionare o richiamare in loop l'intero World esterno durante una chat di gruppo locale, garantendo tempi di risposta immediati e zero token sprecati.
3. **Gestione Lorebook Reattivo:**
   - Ciascuna scheda ha collegati i 3 Lorebook stand-alone (`Svartúlfr - Lorebook`, `Svartúlfr - NPC Primary`, `Svartúlfr - Location`).
   - I Lorebook stand-alone operano in modalità di scansione selettiva: scansionano unicamente gli ultimi messaggi e iniettano solo 0-2 voci se espressamente citate. Nessuna voce globale viene forzata a ogni turno: il consumo del Lorebook rimane inferiore a 500-1.000 token per turno.
4. **Prestazioni Attese:**
   - Il prompt complessivo iniziale prima della cronologia deve rimanere stabilmente tra **4.000 e 6.000 token**.
   - La cronologia dei messaggi e l'input del giocatore rimangono integri al 100%, garantendo coerenza narrativa e assenza di troncamenti.

---

## 19. Standard Operativo di Sessione e Skill Integrate

Ogni interazione dell'assistente su questo repository incorpora sistematicamente i principi delle seguenti modalità operative (dettaglio in [.agents/rules/14_metodo_operativo_skills_integrate.md](file:///e:/repository/SvartulfrVerse/.agents/rules/14_metodo_operativo_skills_integrate.md)):

1. **Pianificazione Rigorosa (`/plan`):** nessuna modifica strutturale a World, schede o Lorebook senza piano di implementazione dettagliato e approvazione esplicita dell'utente.
2. **Allineamento Interattivo (`/grill-me`):** ambiguità e dati non documentati si risolvono con domande mirate una alla volta, mai con assunzioni.
3. **Ispezione Documentale (`/browser`, `/chrome-devtools`):** consultare attivamente le fonti web (profili Wyvern, portale SUCC, JanitorAI) e ispezionare endpoint e schemi dati prima di assumere formati.
4. **Decomposizione e Verifica Obiettiva (`/teamwork-preview`):** task ampi suddivisi in criteri di accettazione verificabili via script e audit di conformità.
5. **Audit Post-Esecuzione (`/boost`):** ogni scrittura va verificata con GET fresche e controlli di integrità indipendenti.
