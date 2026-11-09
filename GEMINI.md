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
20. [Standard Operativo AI Connections e Micro-Proxy di Failover](#20-standard-operativo-ai-connections-e-micro-proxy-di-failover)
21. [Architettura Second Brain (LLM Wiki 2026), Metabolismo Vault & Automazioni](#21-architettura-second-brain-llm-wiki-2026-metabolismo-vault--automazioni)

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
- **Blocco PList Iniziale su Singola Riga, User Persona & Parità `entries == lexicon`:** Il blocco iniziale `[...]` deve occupare **una singola riga** senza sezioni annidate dentro le parentesi quadre, e la sequenza a 4 blocchi (`[NAME: ...]` $\to$ `BACKSTORY:` $\to$ `FAMILY & PACK:` / `CLAN AND COMPANY:` $\to$ `VOICE & BEHAVIOR:`) si applica obbligatoriamente a **tutte le Character Card** (`FINAL/*_card.json` e `ARCHIVIO/cards_legacy/*_card.json`), a **tutte le User Persona** (`FINAL/personas/*.json`) e a **tutte le 310 voci NPC dei Lorebook**. Nei file JSON locali dei Lorebook (`FINAL/` e `lorebooks/optimized/`), l'array `entries` e l'array `lexicon` devono essere mantenuti **100% identici byte-for-byte**.

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

> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. Demi-human anatomical discipline: treat single animal ears as the natural norm; never mention, describe, or reiterate the absence or lack of human ears in narrative descriptions."

---

## 4. Evitare Oggetti e Tratti "Sempre Visibili"

Definire accessori o elementi visivi come "always on" o "never removed" (es. bende di Malachia, tatuaggi di Logan, catena/anello/occhiali di Erik) induce l'LLM in loop continui, costringendolo a forzare l'elemento anche in contesti incoerenti (piscina, doccia, scene formali o intime).

**Regola:** Se un elemento visivo/accessorio non fa strutturalmente parte dell'anatomia del personaggio, non va descritto come costante. Due opzioni (in ordine di preferenza):
1. **Sistema Outfit Nativo di Wyvern (Soluzione preferita):** Utilizzare *Appearance & Outfits* definendo outfit distinti e contestuali (Allenamento, Casa/Casual, Formale, Notturno, ecc.).
2. **Descrizione Contestuale:** Se gli Outfit non sono ancora popolati, descrivere il tratto come legato al contesto nella prosa: *"X indossa Y solo quando Z; in altri contesti non è presente."*
3. **Eccezione Ammessa:** Un tratto può restare costante se e solo se la sua costanza *è* il personaggio e la scheda lo dichiara esplicitamente (es. il cappuccio di Dullahan non scende mai, in nessun contesto).

### Standard Minimo 9 Outfits Obbligatori per Scheda
Ogni character card redatta o aggiornata nel repository deve includere nel campo `outfits` **un minimo assoluto di 9 outfit contestuali**, strutturati rigorosamente secondo lo schema a 6 sezioni (Abbigliamento, Accessori, Scarpe, Gioielli, Trucco, Acconciatura) con apertura lombare rinforzata per la coda:
1. `casual`: Abbigliamento quotidiano, relax a casa, abiti da strada/tempo libero informale.
2. `business / campus`: Frequenza accademica (campus SUCC) o abito professionale/aziendale di rappresentanza (DCC).
3. `gala / formal`: Alta sartoria per cene di casata, ricevimenti solenni, galà ufficiali o cerimonie di branco.
4. `party / club`: Nightlife, serate in discoteca o lounge bar esclusivi (es. The Verve, Solarton club scene).
5. `beach / terme`: Costume da bagno, costume termale o abbigliamento balneare da sorgente calda/spiaggia/piscina.
6. `sleep`: Abbigliamento da notte, pigiama leggero, boxer o intimo per dormire.
7. `nude`: Nudo anatomico completo, con descrizione rigorosa di corporatura, cicatrici, genitali e tatuaggi/rune sub-dermiche.
8. `hybrid shift / mutation`: Forma ibrida bipede da combattimento (per licantropi LSE: Hybrid Shift mastodontico con pelliccia, muso allungato e artigli).
9. `full shift / other`: Forma bestiale integrale a quattro zampe (per shifters: lupo gigante ancestrale; per non-shifters: uniforme operativa da campo specialistica).

### Sfondi per Fascia Oraria (Time of Day Backgrounds) e Tag Regista
- **4 Periodi Canonici:** Le Location supportano immagini differenziate per `dawn`, `day`, `dusk` e `night`.
- **Tag di Scena `[bg: LocationName]`:** Nella narrazione di Game Master, Assistant e bot in Visual Novel Mode, il cambio di scena deve utilizzare il tag `[bg: Nome Location]` (es. `[bg: Campus Suite Moonflower]`). L'engine di Wyvern sincronizza automaticamente lo sfondo con l'ora calcolata dall'AI Time Tracking senza forzature manuali.


---

## 5. Coerenza Visiva di Famiglia (Douglas) e Anatomia Demi-Umani

- **Family Look Douglas:** I maschi della famiglia Douglas condividono un aspetto visivo comune nelle illustrazioni: capelli scuri lunghi e arruffati (per accomodare le orecchie lupine del Partial Shift), palette cromatica calda al tramonto con sfondi di Blackwood City (palme e architettura costiera), e struttura mascellare e facciale simile. Conservare comunque dettagli individuali (stile dei tatuaggi, cicatrici, tonalità degli occhi, accessori).
- **Anatomia Demi-Umani (Orecchie Singole & Positive Framing):** **I demi-umani possiedono un solo paio di orecchie: quelle animali.** Non hanno un secondo paio di orecchie umane. Questa regola è confermata dall'autore originale ed è vincolante. **Disciplina di Formulazione:** Nei testi di contesto narrativo (schede JED+, outfits, scenari, greeting, lorebook), l'anatomia deve essere descritta esclusivamente in termini positivi (es. *"singolo paio di orecchie da lupo sulla sommità del capo, perfettamente integrate tra i capelli"*) senza mai menzionare, esplicitare o negare l'esistenza di orecchie umane (*mai inserire "No orecchie umane", "senza orecchie umane ai lati", "prive di orecchie umane"*). I vincoli negativi sono riservati esclusivamente ai prompt e parametri tecnici per la generazione di immagini (es. `--no human ears`).
- **Sierra Cruz (Lamia — Locomozione & Livrea Arcobaleno Iridescente):** Possiede **capelli color arcobaleno** e, dai fianchi in giù, la parte inferiore del corpo è interamente quella di un serpente di 4 metri **color arcobaleno con scaglie iridescenti** (zero gambe, zero piedi). È tassativamente vietato usare per Sierra termini o verbi come *gambe*, *piedi*, *ginocchia*, *scarpe*, *pantaloni*, *camminare* o *fare passi* (`legs`, `feet`, `knees`, `shoes`, `walk`, `step`, `stand on feet`): Sierra si muove esclusivamente strisciando, scivolando e avvolgendosi sulle sue spire (`slithers`, `glides`, `coils`).
- **Scarlett Rose (Succubus — Palette Rosa Confetto & Corna Scarlatte):** Possiede **capelli rosa confetto** (`candy-pink`), **occhi rosa confetto** abbinati e **due corna scarlatte** che spuntano visibilmente tra i capelli sopra le tempie, oltre alle ali scure da succubus e alla coda prensile con punta a picca.
- **Marchi Divini dei Gemelli (Mani & Sol) & Distinzione Titoli Cosmici (Maniulfr vs Solulfr):** I marchi celestiali risiedono **esclusivamente sulle anche**: Alyssa porta il Marchio Runico di Máni (mezzaluna argentata con glifi lunari sub-dermici) **unicamente sull'anca sinistra**; Jasper porta il Marchio Runico di Sól (sole nero radioso con glifi fiammeggianti sub-dermici) **unicamente sull'anca destra**. È vietato disperdere marchi multipli su mani, petto, nuca, clavicola o cuore (condividono soltanto il tatuaggio protettivo Gebo a inchiostro di ferro freddo sul polso sinistro). Inoltre, il titolo sacro **Sólúlfr** (Lupo del Sole) appartiene **esclusivamente a Svartr (Jasper)**; per Hvít (Alyssa) il titolo divino correlato a Máni è **Mániúlfr** (Maniulf / Lupo della Luna Bianca).

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
4. **Passività Cronologica Assoluta per Game Master e Scenari (Zero Date Reset):**
   Nelle chat stand-alone, negli Scenari e nei prompt dei Game Master, il modello non deve mai tentare di calcolare, forzare o dichiarare date statiche arbitrarie (inclusa la data ricorrente 15 marzo 2024 o date di avvio scenario). La gestione del calendario e della timeline è demandata all'engine nativo di Wyvern (AI Time Tracking / World Clock) e alla cronologia di chat. Il Game Master deve limitarsi a leggere e riflettere passivamente la data e l'ora ereditate dall'ultimo turno.
5. **Standard Scenari a Innesco Timeline (Starts When & Scenario-Guided-Intro):**
   In accordo con la guida ufficiale Wyvern (`wiki.wyvern.chat/Features/Worlds/Scenario-Guided-Intro`), gli scenari progettati per l'auto-inserimento organico nella timeline devono rispettare due invarianti tassative:
   - *Singola Apertura Obbligatoria:* esattamente una sola scena premade (`premade_scenes.length === 1`) oppure sole istruzioni di scena (`scene_instructions`), prevenendo il blocco `opening_choice` ("This scenario has more than one opening, so the event cannot choose one on its own").
   - *Divieto di Insertion Point:* `insertion_point: null` (assente), per prevenire il blocco `time_override` ("This scenario has an Insertion Point. An automatic event cannot ask whether to set the chat clock, so it is skipped").
   - *Parametri di Configurazione:* `repeat: "once"` (o `"cooldown"` con turni), `priority` intera e condizioni logiche ancorate a `time_basis: "world_day"` (Giorno 1 = Ora 0 = 21 Dicembre 827 CE) o `world_time` unitamente a filtri party/persona.
6. **Sincronizzazione Time of Day e Sfondi Dinamici:**
   L'AI Time Tracking calcola automaticamente la fascia oraria corrente tra `dawn`, `day`, `dusk` e `night`. Nelle Location censite nel World, nel Lexicon o nel Lorebook Location (`_EjXxkmPVhpCXg8xABpFkK`), associare per ciascun periodo l'immagine d'atmosfera corretta, consentendo alla piattaforma di sfumare lo sfondo in tempo reale al procedere della timeline.

---

## 7. Triage Import Lorebook ed Architettura Lexicon World / Lorebooks Standalone

- **Dismissione World e Pivot su 6 Lorebook Standalone:** Con la migrazione definitiva ai Character Scenarios, tutto il corpus informativo del mondo è scorporato e distribuito nei **6 Lorebook Standalone** sincronizzati in `/mine` e collegati agli scenari via `lorebook_ids` (793 voci attive totali, 0 disattivate):
  1. `_gwwCxCfQ6PQaLEjAQVpJL` — **Svartúlfr - Lorebook I** (221 entries: Ecologia LSE, Rune, Casate, Fazioni e Lore primaria).
  2. `_HfG7TeV6MJyj6bxMwxkpt` — **Svartúlfr - Lorebook II** (139 entries: Bacheca Contratti, Economia, Oggetti, DDM Voidspace).
  3. `_9zWTGqYJNJ4BCDMj8gfcD` — **Svartúlfr - Lorebook III** (35 entries: Campus SUCC, CUMS, Confraternite, Sport, Underworld).
  4. `_EjXxkmPVhpCXg8xABpFkK` — **Svartúlfr - Location** (188 entries: Location strutturate).
  5. `_zwEqgEEzh12X6gHVmMKKC` — **Svartúlfr - NPC Primary** (99 entries: NPC primari, World Dossier del cast fisso e profili intimi con Statistiche Finali).
  6. `_Uht3Ckz44JBDrPnUHq7LV` — **Svartúlfr - NPC Secondary** (111 entries: NPC secondari e terziari con Statistiche Finali).
- **Regole di Igiene Lorebook Obbligatorie:**
  - **Zero Keyword Ombrello (`BROAD_KEYS`) sugli NPC:** Divieto assoluto di tag generici (`solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega`, ecc.) sulle schede NPC per evitare l'attivazione massiva simultanea di oltre 100 voci.
  - **Zero `selective: true` senza `secondary_keys`:** Mantenere `selective: false` salvo quando `secondary_keys` è popolato.
  - **Divieto della macro `{{age}}`:** Sostituita con età anagrafica e data di nascita esplicita.
    - **Standard Obbligatorio Metadati NPC & Terna di Flag (Wyvern VN Mega Patch):**
      Ogni entry `npc` deve possedere l'oggetto `npc_info` completo con `first_name` (obbligatorio), `middle_names` (array), `last_name` (opzionale), `nicknames` (array), `titles` (array) e `npc_prefix` (stringa o vuoto), sfruttando la compilazione automatica pesata delle regex del frontend Wyvern (modulo 93312 / WH).
    - **Terna di Flag Obbligatoria su ON (`true`):**
      - `scan_persona: true` (Scan Persona: Yes): garantisce la scansione dei trigger anche all'interno della User Persona attiva.
      - `whole_words_only: true` (Whole Words Only: Yes): previene attivazioni spurie su sottostringhe parziali.
      - `enableEntryHighlighting: true` / `highlight_keys: true`: attiva l'evidenziazione visiva delle entry attivate nei messaggi della chat.
    - **Workflow Obbligatorio Gallery & Riconciliazione Asset (`GET /api/gallery/lorebook/{lorebook_id}`):**
      - L'endpoint ufficiale della Gallery Lorebook su Wyvern è `GET /api/gallery/lorebook/{lorebook_id}` (upload via `POST /api/gallery/lorebook/{lorebook_id}`).
      - Il campo `entry.avatar` deve contenere esattamente la stringa `imageURL` registrata nella Gallery del Lorebook. Se l'URL non coincide byte-for-byte con un asset censito nella Gallery del Lorebook, il frontend di Wyvern visualizza l'avviso di anomalia `Custom Image ⚠️ Unknown source`.
      - **Parità di Validazione Zod Frontend (`entries == lexicon`):** Il form editor di Wyvern (`react-hook-form` con schema Zod) richiede tassativamente che la proprietà `entries` sia popolata come array (`entries: z.array(...)`). Poiché il server GET invia le voci sotto la chiave `lexicon`, qualsiasi payload o stato deve mantenere `entries` e `lexicon` identici byte-for-byte per evitare blocchi silenziosi al salvataggio con errore `entries: Required`.
  - **Soppressione Nativa Wyvern ("Don't Activate When Active"): `ignored_characters` & `ignored_personas`:**
    Per impedire duplicazioni, allucinazioni e collisioni bot-giocatore (es. quando l'utente gioca nei panni di una Persona corrispondente a un NPC del Lorebook, come Alyssa o Jasper, o quando una Character Card esterna e gia presente nel party o nella chat), Wyvern gestisce a livello di schema due array dedicati:
    - `ignored_characters: string[]`: Elenco di ID di Character Card. Se una delle card specificate e presente nella sessione attiva, Wyvern ignora e salta integralmente l'entry del Lorebook.
    - `ignored_personas: string[]`: Elenco di ID di Persona (`{{user}}`). Se il giocatore seleziona una delle Persona specificate, Wyvern ignora e salta integralmente l'entry del Lorebook.
    - Questo meccanismo nativo elimina la necessita di ricorrere a workaround artificiali (come `selective: true` con keyword fittizie 'Dossier'/'Scheda'), consentendo a ogni entry NPC nei Lorebook di conservare `selective: false`, chiavi di attivazione naturali (nome, cognome, alias) e descrizioni JED+ narrative integrali (>2.000 fino a >16.000 caratteri) in totale sicurezza.
- **Personaggi Stand-Alone (`/mine`):** Costituiscono la Single Source of Truth condivisa tra chat 1-on-1 e Character Scenarios.

### 7.1 Principio di Sincronizzazione Totale dell'Ecosistema /mine (Omni-Parity)
La sincronizzazione della lore non è limitata al solo asse World Lexicon ↔ Lorebook Standalone, ma abbraccia **l'intero ecosistema /mine di Wyvern**:
1. **World (_YpX47fNraQFw2dD7TdycJ):** Lexicon (700+ voci), Locations (188), Characters (126) e System Prompt / Relationship Pacing Gate.
2. **I 6 Lorebooks Standalone:** Aggiornati garantendo entries == lexicon byte-for-byte su tutti i 6 volumi (Lorebook I, II, III, Location, NPC Primary, NPC Secondary).
3. **Standalone Characters (/mine):** Single Source of Truth per chat 1-on-1 e Scenari (9 Outfits strutturati, Pacing Gates in inal_instructions, Display Names standard su First Name o Nickname).
4. **Character Scenarios (/mine):** Scenari allineati con i lorebook_ids corretti, greetings coerenti con la timeline del World Clock e assenza di slot bloccati (unavailable_count: 0).
5. **AI Assistants / Game Masters (/mine):** Istruzioni di sistema, assembly Handlebars/XML, regole D20 + S.P.E.C.I.A.L. e passività cronologica (Zero Date Reset).
6. **Prompt Assemblies (/mine):** Template uniformati alla disciplina di formattazione dialoghi (virgolette inglesi, plain text, no asterischi, no em-dash).
7. **User Personas (/mine):** Schedatura JED+ su singola riga per attributi e soppressione nativa anti-collisione reciproca (ignored_personas).
8. **Infrastruttura Proxy Locale & Free-Master-list (proxy/):** Isolamento architetturale dei componenti proxy (FastAPI rotator, config_free_proxy.json, script di avvio automatico all'accensione del PC start_proxy.vbs e shortcut Wyvern Free Tier Proxy.lnk), tracciati stabilmente nella sincronizzazione totale del repository.

È fatto divieto assoluto di introdurre modifiche asimmetriche in un solo comparto di /mine lasciando indietro gli altri. Ogni modifica di lore o di sistema deve essere riflessa simultaneamente su tutte le entità pertinenti di /mine e archiviata nei file master locali in FINAL/.

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
2. **Vincolo `attached_world_character_id` nei World con Linked Characters:** Se il World adotta i **Linked Characters** collegati da `/characters/mine` (Single Source of Truth), il campo `attached_world_character_id` deve essere impostato **TASSATIVAMENTE a `null` / `None`**. È vietato inserire ID di Character Card esterne in questo campo, poiché il backend Mongoose di Wyvern accetta esclusivamente ID di `WorldCharacter` embedded nel medesimo World (pena errore `HTTP 500: attached_world_character_id must reference a WorldCharacter in the same world`). La soppressione di collisione bot/giocatore si attua esclusivamente tramite gli array nativi `ignored_characters` e `ignored_personas`. Nei World con personaggi interni embedded, rimane valido il collegamento all'id del `WorldCharacter`.
3. Le memorie corali (eventi collettivi, log di gruppo) rimangono senza Attached Character.

### Attivazione delle Entry Lexicon
- `is_global: false` disattiva l'entry dalla scansione a parole chiave: diventa idonea solo se inserita esplicitamente in `included_lexicon_entries` di una Location, Environment o Scenario con match di chiavi o `constant: true`.
- `attached_world_character_id` non funge da trigger d'inclusione automatica.
- **Filtri corretti:** `keys` (primarie = nome/specie) + `secondary_keys` (parole tematiche) con `key_logic: "AND_ANY"`, associati a `party_conditions` (`has_any [id_personaggio]`).

### Sprite Sets per NPC e Lorebook & Meccanismo Auto-Cutout
- **Lorebook Sprites Tab:** I Lorebook Standalone supportano il tab `Sprites` (`gallery_sprites`). Le voci NPC possono specificare un campo opzionale `sprite_set_id` (o link a sprite set esistenti) per proiettare sul palco della Visual Novel Mode le espressioni facciali e le pose del personaggio.
- **Auto-Cutout Trasparente:** Per gli NPC privi di sprite set dedicato, il frontend Wyvern genera automaticamente un `avatar_cutout` scontornando lo sfondo dell'avatar Cloudflare censito nella Gallery (`entry.avatar`). È vietato inserire URL esterni non censiti nella Gallery per garantire che il renderer di cutout e lo stage VN non incorrano in fallimenti grafici.
- **Preservazione nei PUT:** Nelle chiamate `PUT /api/lorebooks/:id`, non azzerare o omettere eventuali oggetti `sprite_sets` o puntamenti `sprite_set_id` presenti nelle entry.

### Persona Gallery & Alternate Avatars (/mine)
- Anche per le User Persona (`/api/user-personas/:id`), Wyvern supporta ora una `gallery` dedicata e `alternate_avatars[]`.
- Nei payload di aggiornamento delle Persona (`FINAL/personas/*.json`), preservare sempre i campi `gallery`, `alternate_avatars` e `avatar_shape` evitando la cancellazione accidentale causata da payload parziali grezzi.

---

## 8. RPG Stats e Sistemi di Simulazione

- **Stato del Modulo & World Features:** In seguito all'ottimizzazione del Context Budget (World Lean Architecture):
  - `inventory: true`, `currency: true`, `rpg_stats: true`, `combat: true`, `relationships: true`.
  - Disattivati per evitare il dump di tabelle nel prompt: `show_party_stats: false`, `show_species_info: false`.
  - Disattivati perché estranei al canone del World: `ships: false` (Cross-World Ships) e `creature_catcher: false` (Creature Catcher).
- **Convenzioni RPG, Dotazione Tratti (5–15) e Curva dei Livelli (S.P.E.C.I.A.L.):**
  - I 7 Attributi Ufficiali: `strength` (STR), `perception` (PER), `endurance` (END), `charisma` (CHA), `intelligence` (INT), `agility` (AGI), `luck` (LCK).
  - Parametri di bilanciamento World: `base_value: 8`, `max_value: 30`, `point_budget: 25`.
  - **Dotazione RPG Obbligatoria (`1 Razza + 1 Occupazione + 5..15 Tratti`):** Tutti i personaggi hanno obbligatoriamente **1 Razza/Specie (`Species`)** + **1 Occupazione (`Occupation`)** + **da un minimo di 5 a un massimo di 15 Tratti (`Traits`)**. I **protagonisti** (`Alyssa`, `Jasper`, `Malachia`, `Noah`, incluse le varianti High Fantasy) e i **personaggi per lore molto potenti** (`Wulfnic`, `Zefir`, `Ut`, `Erik`, `Logan`, `Magnus`, `Cornelius`, `Zeera`, i Contractors DDM, i Demoni Superiori come `Father Revazhael`, ecc.) hanno **il massimo, ovvero esattamente 15 tratti**.
  - **Curva Canonica dei Livelli (`Max Livello 99`):**
    - **Da 0 a 13 anni:** `Livello 1`
    - **Da 14 a 21 anni:** `Livello 2`
    - **Maggiore `> 21` anni:** **`+1 livello ogni 5 anni`** ($\text{Livello} = \min(99, 2 + \lceil(\text{età} - 21)/5\rceil)$: es. 22–26 anni = Lv 3, 27–31 anni = Lv 4, 47–51 anni = Lv 8, 52–56 anni = Lv 9)
    - **Max Livello:** `99`.
- **Combat Role Mapping (`stat_roles`):**
  - Mappatura ufficiale vincolata per i ruoli di combattimento e vitalità del motore simulativo:
    - Vitalità: `hp_stat: "endurance"`, `mp_stat: "intelligence"`.
    - Azione Offensiva e Difensiva: `physical_attack: "strength"`, `physical_defense: "endurance"`, `special_attack: "intelligence"`, `special_defense: "intelligence"`.
    - Mobilità e Precisione: `speed: "agility"`, `accuracy: "perception"`, `evasion: "agility"`, `flee: "agility"`.
    - Fortuna e Resa Critica: `luck: "luck"`.
- **Custom Moodlets & Pacing Emotivo (12 Stati):**
  - Configurazione modulare registrata sia in `relationship_config.custom_moodlets` che in `relationship_config.moodlets` per retrocompatibilità totale (durata ore, delta/intensità, effetti):
    *Rut*, *Heat*, *Scent Marked*, *Mated Devotion*, *Vampiric Blood Hunger*, *Blood Frenzy*, *Essentia Hunger*, *Seductive Haze*, *Pack Bond Resonance*, *Feral Aggression*, *Blood Oath Bond*, *Betrayed Trust*.
- **Bug Critico del Livello & Tetto a 99:** Un Livello $\ge 100$ blocca silenziosamente il salvataggio dell'intero blocco RPG. Per tutti i personaggi ultracentenari impostare tassativamente **Livello = 99**, riportando l'età reale nel blocco JED+.
- **Cataloghi Ufficiali World & Auto-Provisioning:**
  - I cataloghi del World (`_YpX47fNraQFw2dD7TdycJ`) includono 24 Specie, 28 Occupazioni e 46 Tratti nativi completi di modificatori S.P.E.C.I.A.L.
  - **Regola di Auto-Provisioning (Specie, Tratti e Occupazioni):** Durante la creazione o la modifica di un personaggio (sia Character Card che World NPC o Persona), qualora una Specie, un Tratto o un'Occupazione indicata nel profilo non trovi corrispondenza esatta nei cataloghi registrati sul World, il sistema/l'assistente deve procedere immediatamente all'auto-provisioning (creazione automatica dell'entità mancante via API `POST https://app.wyvern.chat/api/worlds/rpg/{species|occupations|traits}`) con relativi modificatori S.P.E.C.I.A.L., descrizione e flag `player_selectable: true`, sincronizzando contestualmente i file master locali (`scratch/rpg_*_catalog.json` e `FINAL/`). Nessun personaggio deve rimanere privo del rispettivo riferimento nel sistema RPG.

### Protocollo di Formulazione RPG & Dossier Integrale Obbligatorio
È fatto divieto assoluto a qualsiasi assistente AI di proporre, generare o modificare tratti RPG, occupazioni, razze, classi o statistiche basandosi su dati parziali, intuito o inferenze dal solo nome del personaggio.
1. **Lettura Integrale del Dossier:** Prima di qualsiasi proposta o modifica, l'assistente deve recuperare e leggere l'intero testo descrittivo del personaggio (`long_summary`, `description`, `voice & behavior`, `attitudes`) e le relative voci enciclopediche del Lexicon.
2. **Matrice Tassonomica Vincolante delle Stirpi Dinastiche:**
   - `Divine Blood`: riservato **esclusivamente** ai tre Firstborn primordiali (`Wulfnic`, `Zefir`, `Ut`). Nessun altro personaggio, inclusi i discendenti Douglas, può possedere questo tratto.
   - `Founding Bloodline`: riservato a Nixara, ai Firstborn, alla seconda generazione di sangue misto Douglas-Bloodmoon (`Alyssa`, `Jasper`, `Malachia`, `Noah`), e ai diretti discendenti delle stirpi primordiali nei boschi tradizionali: `Thorvald` (discendente diretto del Firstborn Ut Berg) e `Harald Sigurdsson` (scion diretto di uno dei Nove Firstborn caduti). Non appartiene a Erik né a Logan.
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
- **Canone Ufficiale SUCC (`io-succ.uwu.ai`):**
  - **Nome Ufficiale:** **Supernatural University of Central California (SUCC)** a Solarton, CA.
  - **Divieto del termine "Solarton University":** Il nome "Solarton University" è apocrifo e bandito da ogni testo o scheda.
  - **Fondazione (2002):** Fondata dal **Dean Archer Wolfwood**, pioniere dell'integrazione accademica umano-soprannaturale.
  - **Istituzione Rivale:** **CUMS** (*California University of Magical Sciences*), situata a Hex Valley.
- **Sorgenti Canon JanitorAI & Protocollo Accesso Chrome:**
  - *Lorebook Storico Janitor:* `https://janitorai.com/scripts/896b4e03-5bef-45b3-8007-67ca6230e608/edit`
  - *Personaggi Canon Varie Linee Temporali:* `https://janitorai.com/?segment=following`
  - *Scheda Storica Famiglia Douglas:* `https://janitorai.com/edit_character/3a60976e-c48f-4a83-84b5-7026d914645e`
  - *Personaggi Preferiti da Integrare:* `https://janitorai.com/?segment=favorites`
  - *Protocollo:* È fatto divieto di scraping headless; l'accesso a questi link avviene esclusivamente tramite browser Chrome locale su cui l'utente possiede già la sessione attiva e le credenziali memorizzate.
- **Personaggi Importati da Altri Universi dell'Utente (Zeera, Yael, Huck):** Non sono canone esterno fisso ma materiale proprio riscrittibile liberamente; backstory e ruoli vanno ricostruiti da zero per armonizzarsi con Blackwood.
- **Tracciamento Adattamenti:** Gli adattamenti canonici vanno registrati nel Project evidenziando fonte, resa nel World e logica di compatibilità.

### Legami Canonici Esterni & Network Autori Integrati
Le seguenti figure, derivate dai dossier e preferiti storici JanitorAI, sono state formalmente posizionate nel canone Svartúlfr Verse con ruoli e dinamiche vincolanti:
1. **Campus SUCC & Accademia:**
   - **Finnegan "Finn" Novak:** È ufficialmente l'**amico d'infanzia** della generazione giovane Douglas (Alyssa, Jasper, Noah). Demi-umano canino (1 solo paio di orecchie animali), incarna un legame sincero, rilassato e pre-corporativo.
   - **Russ & The Five Cocketeers:** **Russ** è il **coinquilino di stanza di Jasper Douglas** nei dormitori del campus (Wyrm Hall). Esuberante e rumoroso, porta Jasper fuori dalla sua caverna informatica con tacos notturni e vita studentesca.
   - **Roman Blackwood & Kolya:** Atleti di punta del SUCC Varsity Wrestling Team; sono i **compagni di allenamento al Gym e sparring partners di Malachia Douglas**, uniti dal rispetto per il condizionamento fisico pesante e la disciplina marziale.
2. **Distretto Rurale di Bakersfield:**
   - **Dallas Rhodes:** Licantropo contadino e allevatore a **Bakersfield** (ricollocato ufficialmente dal Texas alla Central Valley). Forte, silenzioso, abiti in denim con apertura per la coda, legato al lavoro dei campi e fiero del proprio pragmatismo operaio.
   - **NOVA FARM:** Branco rurale di licantropi operante a **Bakersfield**. Vivono di agricoltura e allevamento su grandi spazi aperti, in forte contrasto socio-culturale con l'aristocrazia corporativa Douglas di Seven Hills.
3. **Underworld, Nightlife & Rivalità Musicali:**
   - **Neon Purr:** DJ felino cyberpunk underground, introdotto come il **principale rivale musicale di Jasper Douglas**. Si sfidano a colpi di produzioni elettroniche, synth analogici e DJ battle tra The Verve e rave illegali.
   - **Romeo "Gray" Dean:** Leader/luogotenente della **gang di biker rivale dei Nomads** di Marek tra Solarton e Blackwood, in perenne contesa per i corridoi di transito.
4. **Fazione Orchi & Politica Marziale:**
   - **Warchief Thrakgor Deathspine:** Bellicoso capoguerra del Clan Deathspine. È la perenne **spina nel fianco di Brak Ironfist**: mentre Brak cerca la tregua e la cooperazione istituzionale, Thrakgor preme per l'espansione guerriera.
5. **Circolo di Forgia al The Verve:**
   - **Morgeth Steeltooth:** Maestro fabbro orco e conoscitore del ferro freddo, sodale e pari di **Ut Berg**. Si incontrano al The Verve trascinando Logan Douglas in estenuanti dispute su leghe e temprature che Logan sopporta per non farsi spaccare in due.
6. **Clan Bloodmoon Tradizionale (Foresta Profonda):**
   - **Thorvald & Harald Sigurdsson:** Licantropi scandinavi del Clan Bloodmoon arcaico, discendenti diretti del seguito di Wulfnic (1022 d.C.). Vivono stabilmente nella foresta profonda del Dead Zone preservando la lingua, i riti runici e la caccia norrena.

### Asimmetria Informativa, Segretezza Licantropica e Divieto Assoluto di Metagaming
1. **Riserbo dei Licantropi & Folklore come Leggenda Metropolitana:**
   - I licantropi sono per natura e tradizione fieri, chiusi ed estremamente riservati sui loro misteri di sangue.
   - Fuori dal branco interno e dai grandi branchi che giurano formale fedeltà a Wulfnic (o delle antichissime casate aristocratiche millenarie come Sterling o Ashbourne), l'esistenza di una figura come il **Re dei Lupi** (*Wolf King*), dell'entità misteriosa nota come **L'Enigma**, o il folklore legato ai **Firstborn** (i Fondatori Primordiali) sono considerati dal mondo esterno **mere leggende metropolitane, miti popolari o favole da bar**.
2. **Percezione Pubblica dei Douglas (I Sovrannaturali Comuni e Studenti SUCC):**
   - Per la stragrande maggioranza dei sovrannaturali comuni, studenti del campus e residenti di Solarton e Blackwood (inclusi gli amici e compagni di campus come **Jared Thompson**, **Santiago Vance**, **Bailey Rogers**, **Mac Sanchez-Rogers**, **Stanley Davies**, **Russell Sinclair**, Andy, Tate, ecc.):
     - **I Douglas** sono unicamente una famiglia locale di licantropi influente, aristocratica e molto facoltosa, a capo della *Douglas Commercial Coalition (DCC)*. Sono celebri per la filantropia e gli investimenti immobiliari, in primis per aver finanziato la costruzione del **Neptune Stadium** e della Douglas Arena.
     - **Erik Douglas** è ricordato e rispettato come una celebrità sportiva locale: ex eroe del campus ed ex stella/capitano della squadra di hockey su ghiaccio dei *SUCC Bears*.
3. **Wulfnic è Rigorosamente "Nonno Nic" per gli Outsider:**
   - Per chiunque sia estraneo al cerchio ristretto del branco, Wulfnic Bloodmoon è **rigorosamente e unicamente ciò che Alyssa e Jasper hanno raccontato: il loro "nonno Nic" (Grandpa Nic)**.
   - È percepito come un anziano montanaro massiccio, rustico, vecchio stampo, burbero ed eccentrico che vive nei boschi o guida un vecchio pickup.
   - **Divieto Assoluto di Metagaming:** Personaggi come Jared, Santiago, Bailey, compagni di squadra e studenti della SUCC **non sanno, non possono sapere e non devono mai sospettare chi sia in realtà Wulfnic**. Non provano terrore cosmico né reverenza ancestrale verso di lui, ma al massimo il naturale rispetto/soggezione dovuto a un anziano imponente e protettivo. È severamente vietato all'LLM far trapelare la sua identità leggendaria nei pensieri, reazioni o dialoghi di questi personaggi.
4. **Inaccessibilità dei Misteri Esoterici (Luna Bianca, Purosangue, Sangue Fondatore):**
   - I dogmi della **Luna Bianca** (*White Moon / Máni*), dei **Purosangue** (*Trueblood*), del **Sangue Fondatore** (*Founder Blood*), le profezie gemellari dei Lupi Cosmici (*Sólúlfr* e *Mániúlfr*) e le rune sacre di sangue sono dottrine religiose ed esoteriche strettamente interne ai licantropi.
   - Un non-licantropo (umano, demone, mezzo minotauro, demi-umano, gorgone, succube o vampiro comune) **non conosce, non comprende e non sa decifrare questi concetti**. Se sente una menzione o nota un'abitudine peculiare, la liquida semplicemente come una bizzarria culturale dei lupi o un modo di dire di famiglia.

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
  1. *Wyvern Blog & Patch Notes* (`https://app.wyvern.chat/blog`): Fonte primaria e ufficiale per release notes, mega-patch, aggiornamenti architetturali (es. Visual Novel Mode, AI Time Tracking, editor modali NPC, Lorebook Sprites) e annunci degli sviluppatori.
  2. *WyvernWiki* (`https://wiki.wyvern.chat/`, guide sotto `/en/Features/Worlds/...`).
  3. Canale `#dev-notes` su Discord per novità in anteprima.
  4. Reddit (`r/WyvernChat`) e canali di supporto.
  *Se la wiki o il blog divergono dalla piattaforma:* Fa fede il dato empirico verificato tramite GET autenticata fresca.

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
- Maturità completa a 21 anni, poi stop biologico dell'invecchiamento. I Firstborn sono bloccati all'età biologica della consacrazione da parte di Fenris nell'**864 d.C.** (dopo 15 anni di Wulfnic come Jarl di Svartúlfr, eletto a 25 anni nell'**849 d.C.**, con i suoi 8 compagni guerrieri nella fascia vichinga **16–45 anni**):
  - *Wulfnic Báleygr Bloodmoon:* Nato il **21 dicembre 824 d.C.** (**1200 anni** nel 2024), trasformato a **40 anni** nell'864 d.C. (nel IX secolo a 40 anni si era già anziani con capelli bianchi e rughe; agli occhi moderni dimostra circa **60 anni**).
  - *Ut Berg:* Nato il **5 maggio 819 d.C.** (**1205 anni** nel 2024), trasformato a **45 anni** nell'864 d.C. (agli occhi moderni dimostra circa **60 anni**).
  - *Zefir Hvitskog:* Nato il **5 febbraio 848 d.C.** (**1176 anni** nel 2024), il più giovane dei Nove trasformato a **16 anni** nell'864 d.C. prima della fine dello sviluppo. Un guerriero vichingo di 16 anni aveva un aspetto più consumato e maturo di un adolescente odierno, per cui agli occhi moderni dimostra **20–22 anni**. Conserva la spavalderia giovanile e un carattere vivace e capriccioso come il vento dei mari del Nord (*"The North Sea Wind"*), ed è iscritto alla SUCC da Wulfnic per proteggere Alyssa in stile **punk** (cresta alla moicana bianca e giubbotto borchiato) con la copertura di un **lontano parente dall'Islanda**.
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
   - I personaggi minorenni (es. **Edric Douglas**, 13 anni) sono categorizzati **esclusivamente come minor background NPC** con divieto assoluto di framing romantico, intimo o sessuale (*"strictly minor background NPC: zero romantic or intimate framing under any circumstances"*).
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
- **HTTP 413 Payload Too Large su Lorebook PUT:** Non includere nel payload JSON sia l'array legacy `entries` sia l'array canonico `lexicon` (raddoppia la dimensione della richiesta). Inviare solo `lexicon` unitamente ai metadati top-level.
- **Errore Caricamento Immagini su Singola Entry Lorebook:** L'upload diretto di file immagine/avatar nei singoli slot delle entry genera errori o fallimenti di persistenza su Wyvern. Seguire il **Workflow Obbligatorio Gallery**: non caricare file direttamente sulle singole entry, ma caricare prima le immagini nella **GALLERY del Lorebook**, e successivamente selezionare l'immagine desiderata dalla Gallery per ciascuna entry (`entry.avatar`).
- **HTTP 409 Conflict su Scenario PUT:** Lo scenario adotta il locking ottimistico con contatore `revision`. Prima di inviare un `PUT`, eseguire sempre una `GET` autenticata fresca per recuperare l'ultimo intero di `revision`, fonderlo nel payload (`'revision': live_data.get('revision')`) e trasmettere. In assenza di `revision`, l'aggiornamento fallisce con HTTP 409.
- **Validazione Schemi Character Standalone API:**
  - `pronouns`: deve essere obbligatoriamente un oggetto a 5 chiavi (`pronoun_subjective`, `pronoun_objective`, `pronoun_possessive_determiner`, `pronoun_possessive_pronoun`, `pronoun_reflexive`). Il tipo stringa (`"He/Him"`) genera `HTTP 400: Expected object, received string`.
  - `linked_world`: deve essere una stringa contenente l'ID univoco del World (es. `"_CgYT8fHXpDC4crjmegQF7"`), mai un oggetto dizionario (`dict`).
  - `creator_notes`: campo obbligatorio in fase di `POST` (minimo 3 caratteri).
  - Omettere sempre `wyldfire_code` e `vanity_slug` nei payload di creazione o aggiornamento per prevenire errori `E11000 duplicate key error`.
- **Attivazione Involontaria Dossier Lorebook:** Impostare tassativamente `selective: true` sui World Dossier del cast principale con `secondary_keys` dedicate archivistiche (`['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`), e bonificare le chiavi trigger isolate mono-parola (es. `'Alyssa'` -> `'Alyssa Telegram'`).
- **Fastify DELETE Empty Body (HTTP 500 FST_ERR_CTP_EMPTY_JSON_BODY):** L'invio dell'header `Content-Type: application/json` con body vuoto nelle chiamate `DELETE` verso gli endpoint World RPG (`/api/worlds/rpg/{species|occupations|traits}/:id`) genera `HTTP 500 FST_ERR_CTP_EMPTY_JSON_BODY`. Omettere tassativamente il `Content-Type` nelle richieste `DELETE` per ricevere `HTTP 204 No Content` ed eseguire la rimozione pulita senza inquinare il database.
- **Subdocumenti Sprite/Gallery nei PUT Lorebook:** Omettere `gallery` o `sprite_sets` durante un PUT su `/api/lorebooks/:id` svuota le immagini caricate. Mantenere sempre nel payload i campi top-level `gallery` e `sprite_sets` recuperati dalla GET fresca.
- **Selettori UI NPC/Location su Editor Modali:** Gli editor di NPC e Location risiedono in finestre modali dedicate `div[role="dialog"]`. Nei test automatizzati Playwright/CDP, selezionare sempre il contenitore modale attivo prima di interagire con input e pulsanti di salvataggio.

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

## 18. Standard Operativo "Character Scenarios", Statistiche RPG Finali & Stile Visivo Argon

Con la dismissione definitiva del modulo World di Wyvern (`_CgYT8fHXpDC4crjmegQF7`), tutte le sessioni multi-personaggio e di storia adottano ufficialmente i **Character Scenarios** (`https://wiki.wyvern.chat/en/Features/Character-Scenarios`, endpoint `/api/character-scenarios`), come dettagliato in [.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md](file:///e:/repository/SvartulfrVerse/.agents/rules/13_workflow_chat_di_gruppo_stand_alone.md), [.agents/rules/09_rpg_stats_e_simulation.md](file:///e:/repository/SvartulfrVerse/.agents/rules/09_rpg_stats_e_simulation.md) e [.agents/rules/03_outfits_e_coerenza_visiva.md](file:///e:/repository/SvartulfrVerse/.agents/rules/03_outfits_e_coerenza_visiva.md):

1. **Scenario Unificato Multi-Greeting (`char_scenario_1DC43ggb6mB8YLJDJKrU4`):**
   - Tutte le **29 aperture narrative** ordinate cronologicamente (`01.`–`29.`, da giugno 2024 a giugno 2025: dalla serata *Call of Duty* a Villa Douglas e le vacanze estive a *Camp Mystic*, lungo i capitoli del primo anno accademico alla SUCC, le incursioni della Gilda DMHA e i rave di DJ Frequency) sono riunite in lingua italiana in un unico grande Character Scenario che segue la vita dei due gemelli Douglas-Bloodmoon.
   - **Dual-Protagonist (`Alyssa` & `Jasper`):**
     - Le aperture `[FemPOV]` collegano la Persona di **Alyssa** (`["persona_1786335754946"]`), le aperture `[MalePOV]` collegano la Persona di **Jasper** (`["1792155173728"]`), mentre le aperture Dual lasciano `linked_persona_ids: []` per libera scelta del giocatore.
     - Il pool dello slot `twin` (`key: "twin"`) contiene **sia la Character Card di Jasper sia la Character Card di Alyssa** (`weight: 100`), così chi gioca nei panni di Alyssa ha Jasper come `twin` e chi gioca nei panni di Jasper ha Alyssa come `twin`.
   - **Disciplina dei Ruoli per i 13 Slot Canonici (14 Character Cards in `/mine`):**
     - Gli slot non utilizzano i nomi dei personaggi ma esclusivamente i ruoli funzionali o relazionali:
       - `maternal_grandfather` -> Wulfnic Báleygr Bloodmoon (`_HEQQbbRFwKdG8QE2Fh1z1`)
       - `father` -> Erik Ulfr Douglas (`_QPea6g4Q1QfeYCVHCLMPR`)
       - `twin` -> Pool bilanciato: Jasper Svartr (`_t4J9aQNJM36cUKAP4wB4U`) + Alyssa Hvit (`_6exg3yPfe2eCDK4hTftkh`)
       - `brother` -> Noah Loki Douglas Bloodmoon (`_zFLUjV8aVxQRAfQxGcAcY`)
       - `eldest_brother` -> Malachia Björn Douglas Bloodmoon (`_RDfz7XzTpM23LpPALVXHM`)
       - `uncle` -> Logan Járn Douglas (`_T8Ywcr9FEqNf9JxbK6eHP`)
       - `cousin` -> Edric Douglas (`_TbRM3EdxDjHFgqztTbCpL`)
       - `quarterback` -> Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`)
       - `friend` -> Stanley "Stan" Davies Jr. (`_Xd3NhKnRJByMTtdb6PjxJ`)
       - `crush` -> Mackenzie "Mac" Sanchez-Rogers (`_zn24784jfcchQ7EwCyAnm`)
       - `female_roommate` -> Sierra Cruz (`_pnrXbkWqcgmFAf3meRWFY`)
       - `female_friend` -> Scarlett Rose (`_qXgBMbFYJfc84hbLHhe92`)
       - `male_roommate` -> Russell "Russ" Sinclair (`_wn6DkCcg3Xqa2Xpx9ttnT`)
     - *NPC gestiti tramite Lorebook:* Personaggi come Zeera Darkfire, Elizabeth Duskwood, Magnus Douglas III, Kaladin Nargathon, Marek, Santiago Herrera, Coach D, Roman Blackwood, Kolya Varenkov e Neon Purr agiscono tramite le rispettive schede `npc` in `NPC Primary` / `NPC Secondary` con attivazione automatica dell'avatar tramite prefisso su nuova riga (`Nome Completo: "..."`).
   - **Messaggi Multi-Mittente (`messages[]`) e Macro:**
     - Ogni battuta in apertura è un elemento separato di `greeting.messages` con il proprio `speaker_slot` (senza prefissi `=>Nome:` o `Nome: ` nel testo); `greeting.content` e `greeting.speaker_slot` devono sempre coincidere con `messages[0]`.
     - Usare `{{scenarioChar "slot_key"}}` per riferirsi agli altri slot, `{{char}}` per il mittente del messaggio corrente e `{{user}}` per il giocatore.
2. **Startup Script Lua (`startup_script`) & Blindatura Anti-Duplicazione:**
   - Negli Scenari con slot dinamici o protagonisti alternativi, Wyvern espone il campo radice `startup_script` (eseguito all'inizializzazione della chat prima del salvataggio dei messaggi di apertura).
   - Lo script verifica a runtime `user.persona_id`, `user.name` e i pronomi (`user.pronoun_subjective`, `user.pronoun_objective`) assegnando dinamicamente la card corrispondente a `memory._scenario.assignments["twin"]` (Jasper se Persona Alyssa o Femmina; Alyssa se Persona Jasper o Maschio; randomizer 50/50 su pronomi neutri con seed temporale).
   - Nel prompt dello scenario è obbligatorio inserire la clausola `[PERSPECTIVE & LOREBOOK SUPPRESSION INVARIANT]` per impedire che memorie o dossier dei Lorebook collegati generino sdoppiamenti o dialoghi fantasma del gemello dormiente.
3. **Statistiche RPG Finali Calcolate (`[STATS: ...]`):**
   - Essendo fuori dal World, nel blocco `RPG STATS & TRAITS:` in fondo a `description` (su Character Card, Personas e Lorebook `NPC Primary`/`Secondary`) non si inseriscono le sole statistiche base, ma le **Statistiche Finali** comprensive di tutti i bonus e malus derivanti da Specie, Occupazione e Tratti:
     $$\text{STAT}_{\text{finale}} = \text{STAT}_{\text{base}} + \Delta_{\text{Specie}} + \Delta_{\text{Occupazione}} + \sum_{i} \Delta_{\text{Tratto}_i}$$
4. **I 6 Lorebook Collegati & I 4 Prompt Overrides:**
   - Ogni Character Scenario collega i 6 Lorebook ufficiali Svartúlfr (`Lorebook I`, `Lorebook II`, `Lorebook III`, `Location`, `NPC Primary`, `NPC Secondary`) più i 3 Lorebook tecnici (`A1 Physics`, `A5 Sex Position`, `A5.5 Scene Tone`).
   - I **4 Prompt Overrides** ufficiali ([FINAL/PROMPT_OVERRIDES_WYVERN.md](file:///e:/repository/SvartulfrVerse/FINAL/PROMPT_OVERRIDES_WYVERN.md)) applicano il "sandwich linguistico" in italiano, il `<dual_scene_format>` e il `【 LIVE FEED 】`.
5. **Stile Visivo Definitivo Argon / Gemini:**
   - Tutte le immagini dei personaggi e dei loro outfit partono dall'ancora biometrica generata con **Argon** (`<IMAGE_0>`) e usano in Gemini lo schema standard a 6 sezioni in italiano (`Abbigliamento` con fessura lombare per la coda, `Accessori`, `Scarpe`, `Gioielli` con rune, `Trucco`, `Acconciatura` con copertura totale delle tempie umane), lo stile *pittura digitale semi-realistica a figura intera* e la clausola finale obbligatoria `No orecchie umane. No auricolari [se non previsti]. No modifiche alle orecchie da lupo o alla coda, coerenti con <IMAGE_0>.`

---

## 19. Standard Operativo di Sessione e Skill Integrate

Ogni interazione dell'assistente su questo repository incorpora sistematicamente i principi delle seguenti modalità operative (dettaglio in [.agents/rules/14_metodo_operativo_skills_integrate.md](file:///e:/repository/SvartulfrVerse/.agents/rules/14_metodo_operativo_skills_integrate.md)):

1. **Pianificazione Rigorosa (`/plan`):** nessuna modifica strutturale a scenari, schede o Lorebook senza piano di implementazione dettagliato e approvazione esplicita dell'utente.
2. **Allineamento Interattivo (`/grill-me`):** ambiguità e dati non documentati si risolvono con domande mirate una alla volta, mai con assunzioni.
3. **Ispezione Documentale (`/browser`, `/chrome-devtools`):** consultare attivamente le fonti web (profili Wyvern, WyvernWiki, conversazioni Gemini) e ispezionare endpoint e schemi dati prima di assumere formati.
4. **Decomposizione e Verifica Obiettiva (`/teamwork-preview`):** task ampi suddivisi in criteri di accettazione verificabili via script e audit di conformità.
5. **Audit Post-Esecuzione (`/boost`):** ogni scrittura va verificata con GET fresche e controlli di integrità indipendenti.



### Inventario Ufficiale delle Skill di Progetto (`.agents/skills/`)
1. **`auto-loop`**: Pipeline evolutiva completa a 4 stadi (Allineamento, Web Research, Plan/Boost, Esecuzione, Debug e Self-Learning).
2. **`chrome-tabgroup-source-extractor`**: Estrazione diretta e non invasiva di sessioni, tab group e URL da LevelDB Sync di Chrome senza riavvio del browser.
3. **`wyvern-ttrpg-master-deployer`**: Progettazione, compilazione Handlebars/XML e deploy via Wyvern Web API di AI Game Master, Custom Prompt Assembly e Scenari con motore D20 + S.P.E.C.I.A.L.
4. **`wyvern-card-lorebook-sync`**: Sincronizzazione Card/Lorebook, conversione di card in NPC con descrizioni JED+ piene, adozione della soppressione nativa anti-collisione (`ignored_characters` & `ignored_personas`), bonifica slot inaccessibili degli Scenari (`unavailable_count: 0`) e deployment via Wyvern Web API.
5. **`wyvern-world-deployer`**: Progettazione architetturale, topologia gerarchica ad albero (Environment e Location ordinate per profondità), specchiatura completa del Lexicon, configurazione anti-bloat del context budget e deployment sicuro di World su Wyvern via Web API con validazione formale e Chrome DevTools.
6. **`wyvern-ai-proxy-rotator`**: Micro-proxy locale FastAPI OpenAI-compatible per Wyvern con rotazione automatica e failover circuit-breaker (cooldown 60s) su modelli Free Tier prioritari.
7. **`wyvern-world-rpg-automator`**: Automazione end-to-end per la configurazione dei sistemi RPG del World Wyvern: allineamento S.P.E.C.I.A.L., Combat Role Mapping, Auto-Provisioning di Specie, Occupazioni e Tratti, bonifica Shop/Item marketplace_config e Custom Moodlets sovrannaturali/biologici.
8. **`wyvern-positive-framing-sanitizer`**: Pipeline per la bonifica da negative constraint echoing ("Pink Elephant Problem") nei contesti di roleplay LLM (Character Cards, Outfits, Scenari, Lorebook) mediante Positive Framing puro, iniezione di vincoli di stile in `post_history_instructions` e deployment sicuro via Wyvern Web API.
9. **`wyvern-chat-audit-world-sync`**: Audit forense dei chat log Wyvern, rilevamento di relationship pacing drift e sincronizzazione delle correzioni e della lore emergente verso il World e i Lorebook via Web API.
10. **`multi-model-unified-pipeline`**: Orchestrazione della Master Pipeline unificata a 5 stadi (`daily-master-pipeline`) tramite il Team Multi-Modello a 3 Tier (`scout-fast`, `architect-sync`, `lore-judge`), il Registro Open-Provider Plug & Play, il Micro-Proxy locale (`:5005`) e i 5 Client AI Desktop del PC OMEN (`Antigravity.exe`, `Gemini.exe`, `Grok Bot.exe`, `Claude.exe`, `copilotapp.exe`) con Dashboard Telemetrica HTML interattiva.

### Verifica Preventiva Piattaforma Wyvern (Pre-Deployment Guard)
Prima di eseguire deployment massivi o aggiornamenti critici di Lorebook, Card e Scenari:
- Lanciare `python scripts/daily_wyvern_platform_monitor.py`.
- Se vengono rilevati nuovi bundle Next.js (`ALERT: New Wyvern frontend bundles detected`), analizzare l'impatto con un'ispezione mirata prima di procedere a scritture intensive via API, garantendo che schemi Zod o endpoint non abbiano subito breaking changes.


---

## 20. Standard Operativo AI Connections e Micro-Proxy di Failover

### Parametro Browser-Only per Endpoint Locali
Quando si utilizzano proxy locali o gateway di rotazione su `127.0.0.1` o host LAN, impostare tassativamente `browser_only: true` (Local Network / Browser-Only) nel Provider di Wyvern. Questa opzione ordina al frontend nel browser di effettuare la chiamata HTTP direttamente dal client all'indirizzo locale, senza passare dai server cloud di Wyvern.

### Supporto CORS Obbligatorio sui Proxy Locali
I server gateway locali (FastAPI, Express o script dedicati) devono implementare l'abilitazione esplicita di `CORSMiddleware` con `allow_origins=["*"]`, `allow_credentials=True`, `allow_methods=["*"]` e `allow_headers=["*"]`. Cio previene il blocco delle chiamate preflight `OPTIONS` emesse da `https://app.wyvern.chat`.

### Disciplina Rigorosa dei Max Tokens (Generazione vs Contesto)
Nelle configurazioni di Wyvern (`AI Connections -> Connections`) e categorico distinguere due parametri con ruoli radicalmente diversi:
1. **Context Window (`max_tokens` a livello top-level):** Definisce l'ampiezza massima della memoria e della cronologia valutata (es. `1000000` per GLM-5 o Gemini).
2. **Generation Max Tokens (`parameters.max_tokens`):** Definisce il limite massimo di token generabili per singolo turno di risposta dal modello.
   - *Valore Obbligatorio:* Mantenere rigorosamente tra `2048` e `8192` (valore ottimale di default: `4096`).
   - *Errore Critico Evitato:* Inserire il valore della context window (es. `200000` o `1000000`) nel parametro `parameters.max_tokens` provoca l'immediato rigetto della chiamata da parte delle API upstream con errori di schema o budget di generazione ecceduto.

### Circuit-Breaker e Quarantena Temporizzata (60s)
I gateway multiprovider o i proxy di failover devono implementare una quarantena temporizzata automatica (cooldown) di almeno 60 secondi su errori HTTP `429`, `403`, `5xx` o Timeout (`>12s`), saltando a tempo zero i nodi guasti e garantendo continuita ininterrotta alla chat.

---

## 21. Architettura Second Brain (LLM Wiki 2026), Metabolismo Vault & Automazioni

Il repository adotta formalmente i principi del modello **«LLM Wiki / Second Brain 2026»** (Karpathy, CoALA framework, MemGuard) per prevenire il decadimento e la frammentazione della lore nel tempo.

### I Tre Livelli della Conoscenza
1. **Livello 1 — Sorgenti Originali (Immutabili):** Cartella `ARCHIVIO/` (dump Janitor, chat storiche). Gli agenti leggono per estrarre la verita, ma non modificano mai queste fonti.
2. **Livello 2 — La Wiki / Cervello Compilato:** Cartella `FINAL/` e i 6 Lorebook Standalone sincronizzati. Single Source of Truth viva e navigabile.
3. **Livello 3 — Lo Schema come Contratto:** `GEMINI.md`, `AGENTS.md` e `.agents/rules/`. Regole verificate dal codice e non semplici raccomandazioni.

### Separazione Rigida dei 4 Tipi di Memoria (CoALA / MemGuard)
- **Memoria di Lavoro (Vita breve):** La sessione attiva e i file in `scratch/`.
- **Memoria Episodica (Datata):** Eventi, log e storico in `CHANGELOG.md` con timestamp esplicito.
- **Memoria Semantica (Stabile):** Fatti enciclopedici in `FINAL/` (schede JED+, lore, catalogo).
- **Memoria Procedurale (Regole):** Direttive operative in `.agents/rules/`.

### Metabolismo del Vault (Health Check a 6 Dimensioni)
Lo script `scripts/vault_health_check.py` analizza sistematicamente il vault cercando:
1. *Contraddizioni:* Discrepanze su altezze canoniche, date di nascita, marchi divini o anatomia demi-umana.
2. *Affermazioni Scadute:* Sovrascritture di canone.
3. *Pagine/Entita Orfane o Buchi di Dati:* Riferimenti mancanti o entry vuote.
4. *Igiene Trigger:* Eliminazione macro `{{age}}`, blocco broad keys su NPC e terna flag attiva.
5. *Parita Byte-for-Byte:* `entries == lexicon` al 100% per conformita con lo schema Zod del frontend Wyvern.
6. *Infrastruttura:* Validazione proxy locale e automazioni registrate.

Il controllo e integrato come **Stage 0** nel runner quotidiano `scripts/daily_maintenance_runner.py`.

### Standard Obbligatorio Automazioni Antigravity (Unified Scheduled Sidecar)
- **Divieto del tool `schedule`:** Il tool interno `schedule` crea un timer effimero di chat che muore alla chiusura della sessione e non compare nella UI.
- **Unificazione in Singola Master Pipeline (`daily-master-pipeline`):** Tutte le operazioni quotidiane di manutenzione, monitoraggio e arricchimento lore sono consolidate in un'unica automazione atomica registrata in:
  `~/.gemini/config/sidecars/daily-master-pipeline/sidecar.json`
  con `"builtin": "schedule"`, `"restart_policy": "always"`, schedule `"CRON_TZ=Europe/Rome 0 9 * * *"`, delimitatore `"--"` prima del prompt e permessi minimi nel workspace (`workspace_uris` e `access_grants`). I 4 precedenti sidecar separati sono archiviati in `ARCHIVIO/sidecars_legacy_backup/`.
- **Orchestrazione Multi-Modello a 3 Tier & Specialisti Desktop (`multi-model-unified-pipeline`):** Lo script `.agents/skills/multi-model-unified-pipeline/scripts/orchestrator.py` e il registro `references/models_registry.json` orchestrano i 5 stadi giornalieri su **Tier 1 (`scout-fast` — `gemini-3.8-flash` / `copilotapp.exe` / `:5005` `gemma-4-31B-it` & `qwen-3.8-27b`)**, **Tier 2 (`architect-sync` — `gemini-4-argon` & `claude-sonnet-5.5` / `copilotapp.exe` & `Claude.exe` / `:5005` `z-ai/glm-5.3` & `deepseek-chat`)**, **Tier 3 (`lore-judge` — `claude-opus-5.5` & `gemini-4-argon` / `Claude.exe` / `:5005` `nemotron-3-ultra-550b` & `z-ai/glm-5.3`)**, riservando i 2 client desktop specialisti **esclusivamente** ai rispettivi domini: **`Grok Bot.exe` (`agenda_work_slots_only`)** come Agenda Personale per il blocco degli slot di lavoro sullo sviluppo dell'ambientazione, e **`Gemini.exe` (`visual_studio_argon_images`)** tramite **Gemini 4 Argon** per la creazione e generazione delle immagini. Include **Stage 4 (Dashboard Telemetrica HTML `scratch/unified_pipeline_dashboard.html` e Archiviazione Transcript in `logs/automations/`)**.
- **Zero Dipendenze Esterne negli Script Sidecar (`urllib.request` Standard):** Tutti gli script Python invocati dalle automazioni o dall'orchestratore multi-modello devono utilizzare esclusivamente la standard library Python (`urllib.request`, `urllib.error`, `json`, `pathlib`, `time.monotonic()`) per garantire esecuzione deterministica sia sotto `uv run python` sia sotto l'interprete di sistema, includendo sempre favicon SVG inline (`data:image/svg+xml`) nelle dashboard HTML autogenerate.
