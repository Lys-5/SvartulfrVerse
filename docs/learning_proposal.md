# Proposta di Apprendimento & Consolidamento Regole (/learn)

**Data Sessione:** 2026-11-16  
**Task:** Refinement Carte Contractor DDM (#01-#06, #08), Scenari Ragnarok, Lorebook & Parità Live Wyvern  
**Stato:** In attesa di approvazione dell'utente tramite `/learn`  
**Autore / Ruolo:** Teamwork Implementer / Specialist  

---

## 1. Sintesi Esecutiva dei Nuovi Pattern Appresi

Durante la sessione di bonifica e deployment delle 8 Character Card Contractor (#01 Richard Whitlock, #02H Hana Valencia, #02A Adam Valencia, #03 Luka Sutter, #04 Dullahan, #05 Johan Jakobsen, #06 Fenrir, #08 Jasper), dei 2 Scenari Ragnarok (`char_scenario_TX9UdgBjXktn4Rd3Wc8r1`, `char_scenario_96kHDTPXYBLjw3fmEdFXr`) e del Lorebook DDM (`_6Bw2jCF3aeMX6gnJnGzgR`), sono emersi 3 pattern tecnici fondamentali che risolvono problemi critici di generazione e allineamento di piattaforma su Wyvern:

1. **Human Anatomical Discipline (Pure Positive Framing per Personaggi Umani / Mortali):**
   - *Problema:* L'inserimento nei prompt di sistema (`post_history_instructions`, `description`, `personality`, scenari e lorebook) di clausole negative o iper-dichiarative sulla natura umana dei personaggi (es. `"100% human anatomy"`, `"ordinary human ears and facial features"`, `"NONE of them have animal ears"`, `"interamente umana"`) innesca il *Pink Elephant Problem*. Nei Large Language Models (LLM basati su matrici di self-attention), tali token semantici vengono costantemente eccitati, spingendo il modello a reiterare e descrivere ridondantemente le "orecchie umane" o la "corporatura umana" anche durante normali dialoghi e azioni di combattimento.
   - *Soluzione:* Eliminare ogni negazione anatomica nei campi di contesto. I tratti umani ordinari costituiscono la norma implicita e non vanno dichiarati né difesi negativamente. Le forme animali o i tratti sovrannaturali vanno definiti unicamente come abilità o trasformazioni attive (`ANIMAL_SHIFT: [Species] (full beast shift);`). In `post_history_instructions` si inserisce la clausola comportamentale positiva:
     `Demi-human anatomical discipline: treat species-specific animal traits as the natural norm; never mention, describe, or reiterate the presence, absence, or type of human ears or human anatomy in narrative descriptions.`
   - *Correzione Specifica per Dullahan:* Rimozione delle descrizioni spurie delle orecchie da Irish Wolfhound nel corpo umanoide/base presente nel primo messaggio e nei saluti di scenario (`first_mes`, `scene-ddm-ragnarok-arrival`, `scene-ddm-fantasy-ragnarok-arrival`), ripristinando la figura incappucciata senza volto e priva di padiglioni auricolari animali in forma base.

2. **Standardizzazione In-Chat Name (`chat_name`):**
   - *Problema:* Quando una Character Card su Wyvern possiede un titolo di catalogo complesso (es. `Richard Whitlock (Contractor #01)` o `Luka Sutter (Contractor #03)`), se il campo `chat_name` non è configurato o contiene il cognome/titolo, l'interfaccia di chat di Wyvern (balloon, indicatori di turno, split degli avatar) visualizza l'intera stringa prolissa o il cognome, rompendo la leggibilità del roleplay.
   - *Soluzione:* Il campo `chat_name` nelle Character Card deve essere valorizzato **rigorosamente con il solo nome proprio** (`Firstname`, es. `'Richard'`, `'Hana'`, `'Adam'`, `'Luka'`, `'Dullahan'`, `'Johan'`, `'Fenrir'`, `'Jasper'`), separando l'identificatore compatto a schermo dal nome di catalogo esteso memorizzato in `name`.

3. **Formattazione Dialoghi Secondari ed ACE su Scenari e Carte (`Firstname:`):**
   - *Problema:* Il motore client di Wyvern analizza i messaggi riga per riga (`lines_parsed: 1`) applicando espressioni regolari per identificare gli interlocutori secondari e attivare i rispettivi avatar dedicati (avatar splitting). Istruzioni generiche che richiedevano di anteporre il "nome completo esatto" (`exact full name and a colon`, es. `Mira Solis: [dialogue/action]`) provocavano il fallimento del matching regex quando l'avatar dell'NPC nel Lorebook o nello scenario era ancorato al solo nome proprio (`first_name: "Mira"`).
   - *Soluzione:* Standardizzare la formula in `post_history_instructions` e nei testi degli scenari richiedendo tassativamente il formato `'Firstname:'` su nuova riga (es. `Bartholomew: [dialogue/action], Luka: [dialogue/action]`).

---

## 2. Regola 1 — Human Anatomical Discipline & Anti-Echoing Positive Framing

### 2.1 Analisi Tecnica della Causa Primaria (Transformer Self-Attention)
Nei modelli transformer, ogni token nel prompt proietta vettori di Query, Key e Value. Inserire token correlati a `human ears`, `orecchie umane`, `100% human` nei campi di istruzione post-storica e nelle schede JED+ aumenta la probabilità a priori (logits) di generare parole semanticamente affini (`ears`, `orecchie`, `human`, `udito`, `umano`). Il modello non processa la negazione logica booleana ("non descrivere orecchie umane"), ma rileva una forte attenzione contestuale sul concetto di anatomia auricolare umana e cerca contesti per esplicitarla narrativamente.

### 2.2 Tabella di Trasformazione (Negative $\to$ Positive Framing)

| Contesto / Campo | Formulazione Negativa Deprecata ❌ | Formulazione Positiva Standard ✅ |
| :--- | :--- | :--- |
| `description` (JED+ Line 1) | `BASE_APPEARANCE: 100% human humanoid anatomy (ordinary human ears, human eyes, and human features; animal traits appear only when fully transformed into Animal Form);` | *(Rimosso integralmente)*. La fisionomia è definita positivamente dai tratti somatici (capelli, occhi, corporatura, cicatrici) e l'animale è dichiarato come `ANIMAL_FORM: [Specie] ([Nome Scientifico], full beast shift);`. |
| `personality` (PList) | `BASE_HUMANOID_FORM: 100% ordinary human anatomy (human ears, human features; Animal Form only when fully shifted);` | *(Rimosso)*. Mantenere solo i tratti temperamentali e, per Dullahan o mutanti: `BASE_FORM: Headless mist-hooded figure;`. |
| `post_history_instructions` (Contractor Cards) | `Base humanoid appearance discipline: Contractors #01 through #06 have ordinary 100% human anatomy in humanoid form (human ears and human facial features...). Only Contractors #07 and #08 are born Werewolves...` | `Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. When secondary NPCs or ACEs speak or take action, always output their dialogue on a new line prefixed with 'Firstname:' (e.g., Bartholomew: [dialogue/action], Luka: [dialogue/action]) to trigger avatar headers in chat. Demi-human anatomical discipline: treat species-specific animal traits as the natural norm; never mention, describe, or reiterate the presence, absence, or type of human ears or human anatomy in narrative descriptions.` |
| Scenari (`scenario`) | `Anatomy Note: Contractors #01 through #06 are 100% human in base humanoid form (ordinary human ears and facial features; animal traits manifest only in full Animal Form). Only #07 Alyssa and #08 Jasper are born Werewolves with wolf ears and tails.` | *(Rimosso il paragrafo Anatomy Note)*. Integrata la disciplina di formato e anatomica unificata in coda alle istruzioni di scena. |
| Scenari (`greetings`) & Dullahan `first_mes` | `...mentre le sue orecchie da Irish Wolfhound guizzano svogliate dietro la nuca.` / `...while his Irish Wolfhound ears flick lazily.` | `...mentre il cappuccio scuro ricade immobile sulle sue spalle massicce.` / `...while standing impassive in the silence of the lounge.` |
| Lorebook (`ddm_lb_contractors_rules`) | `Base Appearance Rule: Contractors #01-#06 are 100% human in appearance in their base humanoid form; NONE of them have animal ears or tails (they only take on animal traits when transforming into their Contract Animal Form)...` | `Base Appearance Rule: Contractors #01-#06 maintain their mortal humanoid appearance in standard form, manifesting animal traits solely during a complete transformation into their Contract Animal Form. Only #07 Alyssa and #08 Jasper, as born Werewolves of the LSE Founding Bloodline, possess natural wolf ears and tails in humanoid form.` |

---

## 3. Regola 2 — Standardizzazione In-Chat Name (`chat_name`)

### 3.1 Mapping Architetturale Wyvern
Nella piattaforma Wyvern, l'identità del personaggio è divisa su tre livelli:
1. `name` (String): Il nome di catalogo univoco visualizzato nella dashboard `/characters/mine` e negli elenchi amministrativi (es. `Richard Whitlock (Contractor #01)`).
2. `display_name` (String, opzionale): Etichetta secondaria del profilo pubblico.
3. `chat_name` (String): Il nome visualizzato a runtime durante la chat all'interno dei balloon di messaggio, nella barra dei partecipanti e per il matching degli avatar.

### 3.2 Matrice di Allineamento dei Contractor Cards

| Card ID | Catalog `name` | Target `chat_name` | Stato API Wyvern | Stato Locale FINAL/ |
| :--- | :--- | :--- | :--- | :--- |
| `_2xh1VhxVjHx1Rje3fg7Bg` | `Richard Whitlock (Contractor #01)` | `'Richard'` | HTTP 200 (Verificato) | `FINAL/Richard_Whitlock_card.json` |
| `_DBd8Rx9pzaPtxeG8232V6` | `Hana Valencia (Contractor #02H)` | `'Hana'` | HTTP 200 (Verificato) | `FINAL/Hana_Valencia_card.json` |
| `_DEDnMNcgX8xDEpGmYqdrM` | `Adam Valencia (Contractor #02A)` | `'Adam'` | HTTP 200 (Verificato) | `FINAL/Adam_Valencia_card.json` |
| `_axCwFrFLmaUn6XE7hbQt2` | `Luka Sutter (Contractor #03)` | `'Luka'` | HTTP 200 (Verificato) | `FINAL/Luka_Sutter_card.json` |
| `_GADYjkenq7CW4RhU2wqbh` | `Dullahan (Contractor #04)` | `'Dullahan'` | HTTP 200 (Verificato) | `FINAL/Dullahan_card.json` |
| `_cPHFyL1FbeQWzX1QMptpW` | `Johan Jakobsen (Contractor #05)` | `'Johan'` | HTTP 200 (Verificato) | `FINAL/Johan_Jakobsen_card.json` |
| `_1zWxyEmwxKq1DhMxj3pXw` | `Fenrir (Contractor #06)` | `'Fenrir'` | HTTP 200 (Verificato) | `FINAL/Fenrir_card.json` |
| `_waQyWtVYDbJkhrH9ADYbn` | `Jasper` | `'Jasper'` | HTTP 200 (Verificato) | `FINAL/Jasper_Contractor_card.json` |

---

## 4. Regola 3 — Formattazione Dialoghi NPC / ACE (`Firstname:`)

### 4.1 Meccanismo di Avatar Splitting del Runtime Wyvern
Il client web di Wyvern decompone la risposta del modello turno per turno. Se rileva che una nuova riga inizia con `Nome:` corrispondente a un NPC o a un personaggio presente nel party o nel Lorebook con `custom_avatar_regex: true`, il client:
1. Divide il blocco di testo in un balloon separato;
2. Assegna l'avatar portrait dedicato dell'interlocutore secondario;
3. Mostra l'header di chat personalizzato con il nome dell'NPC.

Se l'istruzione forza `exact full name and a colon` (es. `Mira Solis:` o `Captain Luka Sutter:`), mentre l'entry del Lorebook ha `npc_info.first_name = "Mira"` e l'avatar regex cerca `(?:^|\n)\s*(?:Mira|Firstname)\s*:`, il matching fallisce o crea frammenti non formattati.

### 4.2 Requisito Obbligatorio di Prompt
In tutte le Character Card e negli Scenari multi-character, la clausola di prefisso secondario deve recitare invariabilmente:
```text
When secondary NPCs or ACEs speak or take action, always output their dialogue on a new line prefixed with 'Firstname:' (e.g., Bartholomew: [dialogue/action], Luka: [dialogue/action]) to trigger avatar headers in chat.
```

---

## 5. Dettaglio delle Modifiche Proposte al Repository (Diff / Patch)

### 5.1 Proposta di Modifica a `GEMINI.md`

```diff
--- a/GEMINI.md
+++ b/GEMINI.md
@@ -105,6 +105,12 @@
 - **Blocco PList Iniziale su Singola Riga, User Persona & Parità `entries == lexicon`:** Il blocco iniziale `[...]` deve occupare **una singola riga** senza sezioni annidate dentro le parentesi quadre, e la sequenza a 4 blocchi (`[NAME: ...]` $\to$ `BACKSTORY:` $\to$ `FAMILY & PACK:` / `CLAN AND COMPANY:` $\to$ `VOICE & BEHAVIOR:`) si applica obbligatoriamente a **tutte le Character Card** (`FINAL/*_card.json` e `ARCHIVIO/cards_legacy/*_card.json`), a **tutte le User Persona** (`FINAL/personas/*.json`) e a **tutte le 310 voci NPC dei Lorebook**. Nei file JSON locali dei Lorebook (`FINAL/` e `lorebooks/optimized/`), l'array `entries` e l'array `lexicon` devono essere mantenuti **100% identici byte-for-byte**.
+- **Politica In-Chat Name (`chat_name`):** Per tutte le character card, il campo `chat_name` deve essere valorizzato rigorosamente con il solo nome proprio (`Firstname`, es. `Richard`, `Hana`, `Luka`, `Dullahan`), separando l'identificatore compatto visualizzato nei balloon e nelle liste di chat dal nome di catalogo esteso memorizzato in `name` (es. `Luka Sutter (Contractor #03)`).
 
 ---
 
@@ -124,7 +130,7 @@
 Inserire sempre questa riga in coda a `post_history_instructions` (campo `final_instructions` via API):
 
-> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. Demi-human anatomical discipline: treat species-specific animal traits (e.g. single animal ears for mammals, smooth reptilian hearing and scales for lamias) as the natural norm; never mix species traits (never give wolf ears to lamias or reptiles); never mention, describe, or reiterate the absence or lack of human ears in narrative descriptions."
+> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. When secondary NPCs or ACEs speak or take action, always output their dialogue on a new line prefixed with 'Firstname:' (e.g., Bartholomew: [dialogue/action], Luka: [dialogue/action]) to trigger avatar headers in chat. Demi-human anatomical discipline: treat species-specific animal traits (e.g. single animal ears for mammals, smooth reptilian hearing and scales for lamias) as the natural norm; never mix species traits (never give wolf ears to lamias or reptiles); never mention, describe, or reiterate the presence, absence, or type of human ears or human anatomy in narrative descriptions."
 
 ---
 
@@ -155,6 +161,12 @@
 - **Anatomia Demi-Umani & Tassonomia Specie-Specifica (Positive Framing):** **I demi-umani ereditano esclusivamente i tratti anatomici, sensoriali e fisiologici della loro specifica specie animale di appartenenza:**
+  - **Personaggi Umani Ordinari e Mortal Shifters in Forma Base:** È tassativamente vietato inserire formule come `"100% human"`, `"ordinary human ears"`, `"interamente umana"` o `"no animal ears or tail"` nella descrizione o nella personality. La base umana è la norma implicita del personaggio mortale; i tratti bestiali si specificano unicamente come trasfigurazione attiva (`ANIMAL_FORM: ... full beast shift`).
   - **Demi-Umani Mammiferi (Lupini, Canini, Felini, Bovini, Ursini, Roditori):** Possiedono un solo paio di orecchie, quelle animali della loro specie (lupine/canine erette, feline a punta, bovine orizzontali con morbida peluria, orse arrotondate), e la rispettiva coda. Mai descrivere orecchie umane ai lati.
```

### 5.2 Proposta di Modifica a `.agents/rules/01_formato_consegna_e_jed.md`

```diff
--- a/.agents/rules/01_formato_consegna_e_jed.md
+++ b/.agents/rules/01_formato_consegna_e_jed.md
@@ -56,6 +56,8 @@
 - **Blocco PList Iniziale su Singola Riga, User Persona & Parità `entries == lexicon`:** Il blocco iniziale `[...]` deve occupare **una singola riga** senza sezioni annidate dentro le parentesi quadre, e la sequenza a 4 blocchi (`[NAME: ...]` $\to$ `BACKSTORY:` $\to$ `FAMILY & PACK:` / `CLAN AND COMPANY:` $\to$ `VOICE & BEHAVIOR:`) si applica obbligatoriamente a **tutte le Character Card** (`FINAL/*_card.json` e `ARCHIVIO/cards_legacy/*_card.json`), a **tutte le User Persona** (`FINAL/personas/*.json`) e a **tutte le 310 voci NPC dei Lorebook**. Nei file JSON locali dei Lorebook (`FINAL/` e `lorebooks/optimized/`), l'array `entries` e l'array `lexicon` devono essere mantenuti **100% identici byte-for-byte**.
+- **Standardizzazione In-Chat Name (`chat_name`):** Tutte le Character Card devono avere il campo `chat_name` configurato con il solo nome proprio (`Firstname`, es. `Richard`, `Hana`, `Luka`, `Dullahan`). Il nome di catalogo esteso (es. `Richard Whitlock (Contractor #01)`) rimane confinato nel campo `name`.
```

### 5.3 Proposta di Modifica a `.agents/rules/02_disciplina_formattazione_dialoghi.md`

```diff
--- a/.agents/rules/02_disciplina_formattazione_dialoghi.md
+++ b/.agents/rules/02_disciplina_formattazione_dialoghi.md
@@ -10,6 +10,7 @@
 6. **Divieto di Markdown nei testi del World:** Niente markdown dentro i testi del World. L'uso del grassetto con `**` viola espressamente la regola sugli asterischi. Questo divieto si applica tassativamente anche alle entry Lexicon e alle description di Location ed Environment, non solo ai dialoghi dei personaggi.
+7. **Prefisso Dialoghi Secondari / ACE su Nuova Riga (`Firstname:`):** Nei contesti multi-character e negli scenari corali, i dialoghi e le azioni dei personaggi secondari devono iniziare su una nuova riga con il prefisso `'Firstname:'` (es. `Bartholomew: [dialogue/action]`) per attivare lo splitting automatico dei balloon e degli avatar nel client Wyvern.
 
 ---
 
@@ -18,1 +19,1 @@
-> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. Demi-human anatomical discipline: treat species-specific animal traits (e.g. single animal ears for mammals, smooth reptilian hearing and scales for lamias) as the natural norm; never mix species traits (never give wolf ears to lamias or reptiles); never mention, describe, or reiterate the absence or lack of human ears in narrative descriptions."
+> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. When secondary NPCs or ACEs speak or take action, always output their dialogue on a new line prefixed with 'Firstname:' (e.g., Bartholomew: [dialogue/action], Luka: [dialogue/action]) to trigger avatar headers in chat. Demi-human anatomical discipline: treat species-specific animal traits (e.g. single animal ears for mammals, smooth reptilian hearing and scales for lamias) as the natural norm; never mix species traits (never give wolf ears to lamias or reptiles); never mention, describe, or reiterate the presence, absence, or type of human ears or human anatomy in narrative descriptions."
```

### 5.4 Proposta di Modifica a `.agents/rules/03_outfits_e_coerenza_visiva.md`

```diff
--- a/.agents/rules/03_outfits_e_coerenza_visiva.md
+++ b/.agents/rules/03_outfits_e_coerenza_visiva.md
@@ -36,6 +36,7 @@
 - **Pure Positive Framing nei Testi Narrativi:** È tassativamente vietato inserire frasi negative di diniego anatomico (*"no human ears"*, *"senza orecchie umane"*, *"prive di orecchie ai lati"*) all'interno di schede JED+, lorebook, greeting, outfits o scenari. L'anatomia va descritta unicamente in termini positivi (*"singolo paio di orecchie da lupo tra i capelli"*, *"fessure uditive rettiliane squamate lungo le tempie"*). La clausola negativa `No orecchie umane` è riservata esclusivamente ai prompt tecnici di generazione visiva Imagen.
+- **Positive Framing per Personaggi a Base Umana:** Per personaggi umani o mortali shifters, non descrivere mai l'assenza di tratti animali né affermare negativamente che hanno orecchie umane. I tratti umani si esprimono naturalmente attraverso la fisionomia ordinaria, evitando formule come `100% human` o `ordinary human ears`.
```

### 5.5 Proposta di Modifica a `.agents/rules/10_pipeline_standard_e_attitudes.md`

```diff
--- a/.agents/rules/10_pipeline_standard_e_attitudes.md
+++ b/.agents/rules/10_pipeline_standard_e_attitudes.md
@@ -16,6 +16,7 @@
    - `summary`: Blocco PList puro di soli tratti psicologici/comportamentali.
    - `display_description`: 1-2 frasi incisive su chi è e cosa lo rende memorabile.
    - Nickname, titoli, keys, pronomi.
+   - **In-Chat Name (`chat_name`):** Tassativamente impostato sul solo nome proprio (`Firstname`).
    - **Invariante Privacy & Rating:** Tassativamente `visibility: "private"` e `rating: "explicit"`.
```

### 5.6 Proposta di Modifica a `.agents/rules/11_wyvern_api_sicurezza_e_bug.md`

```diff
--- a/.agents/rules/11_wyvern_api_sicurezza_e_bug.md
+++ b/.agents/rules/11_wyvern_api_sicurezza_e_bug.md
@@ -49,6 +49,7 @@
    - **Trappola Safe Payload:** Inviare unicamente i campi modificabili definiti in `EDITABLE_FIELDS` (`name`, `display_name`, `avatar`, `description`, `personality`, `mes_example`, `first_mes`, `scenario`, `post_history_instructions`, `pre_history_instructions`, `visual_description`, `creator_notes`, `model_url`, `soundcloud_url`, `character_note`, `tagline`, `backgroundURL`, `tags`, `community_tags`, `rating`, `chat_name`, `pronouns`, `outfits`, `default_outfit`, `shared_info`, `alternate_greetings`, `secretFields`, `secrets`, `fields`, `commands`, `metadata`).
    - L'inclusione di campi di sola lettura gestiti dal backend (`entity_statistics`, `creator`, `created_at`, `updated_at`, `_id`) provoca `HTTP 400 Bad Request`.
+   - **Aggiornamento Scenari e Greetings (Trappola dell'Array Messages):** Nei Character Scenarios, il testo del saluto non risiede solo in `greeting.content`, ma è duplicato all'interno dell'array `greeting.messages[0].content`. Qualsiasi bonifica del testo di saluto deve aggiornare obbligatoriamente entrambi i campi prima del PUT, rispettando l'invariante `greeting.content == greeting.messages[0].content`.
```

### 5.7 Proposta di Modifica a `.agents/skills/wyvern-positive-framing-sanitizer/SKILL.md`

```diff
--- a/.agents/skills/wyvern-positive-framing-sanitizer/SKILL.md
+++ b/.agents/skills/wyvern-positive-framing-sanitizer/SKILL.md
@@ -50,6 +50,15 @@
 Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead. Demi-human anatomical discipline: treat single animal ears as the natural norm; never mention, describe, or reiterate the absence or lack of human ears in narrative descriptions.
 ```
 
+### 2.3 Estensione Human Anatomical Discipline per Personaggi a Base Umana
+Per personaggi mortali, umani o shifters con forma base umanoide ordinaria (es. Contractor DDM #01-#06):
+1. **Divieto di Negazioni Iper-Dichiarative:** Vietato inserire `BASE_APPEARANCE: 100% human humanoid anatomy...` o `BASE_HUMANOID_FORM: 100% ordinary human anatomy...`.
+2. **Positive Behavioral Constraint:** Inserire in `post_history_instructions` la clausola integrata:
+```text
+Demi-human anatomical discipline: treat species-specific animal traits as the natural norm; never mention, describe, or reiterate the presence, absence, or type of human ears or human anatomy in narrative descriptions.
+```
```

---

## 6. Chiarimenti e Domande per l'Utente

Prima di consolidare definitivamente queste patch nei file di regole tramite `/learn`, si sottopongono all'utente i seguenti 3 punti di chiarimento:

1. **Uniformazione Globale di `chat_name` oltre i Contractor:**
   - Si raccomanda di estendere formalmente la regola `chat_name == Firstname` anche alle altre Character Card del repository (es. Seventeen Hills, Campus SUCC), lasciando eventuali titoli e cognomi confinati in `name` e `display_name`. Si desidera applicarla sistematicamente a tutti i futuri rilasci di character card?
2. **Standard Prefisso Scenari Corali (`Firstname:` vs `Nickname:`):**
   - Per NPC con soprannomi ampiamente utilizzati (es. `Coach D` per Dullahan, `Cap` per Richard, `DJ Frequency` per Jasper), si conferma che negli Scenari e nelle istruzioni di avatar splitting il prefisso prioritario debba essere sempre il primo nome anagrafico (`Firstname:`, es. `Dullahan:`, `Richard:`, `Jasper:`) per garantire coincidenza perfetta 1:1 con `chat_name` e `npc_info.first_name`?
3. **Scansione e Bonifica Retroattiva dei Vecchi Chat Logs:**
   - La bonifica eseguita su card, scenari e lorebook previene al 100% la ricomparsa di "orecchie umane" o orecchie di wolfhound nei nuovi turni di chat. Si desidera che un task futuro esegua la bonifica retroattiva via API anche sui messaggi storici pregressi archiviati nei vecchi log di chat (`chat-logs/message/:id`)?
