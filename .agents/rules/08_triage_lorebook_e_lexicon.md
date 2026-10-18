# Regola 08 — Triage Import Lorebook ed Architettura Lexicon World

## 1. Triage delle Entità da Importare

I personaggi (anche deceduti) non vanno più archiviati come semplici voci di dizionario:
- **Personaggi Stand-Alone Creati (`/mine`):** Vengono collegati direttamente al World tramite il modulo **Linked Characters** (`linked_characters`, visibile in `ws=library&tab=linked-characters`). Questa architettura garantisce che le modifiche apportate alla scheda dell'autore in `/mine` (o nelle sessioni 1-on-1) si riflettano istantaneamente nel World senza duplicazione di dati né disallineamenti.
- **Personaggi Nativi del World:** Rimangono interni all'istanza World (`ws=library&tab=characters`), con la loro Start Position definita dal World Clock.
- **Personaggi Deceduti:** Vanno inseriti come **Character**, configurando sia **Start Position** che **End Position** (modello Nixara; non vanno nel Lexicon).

*Obbligo della Start Position:* La Start Position va impostata **sempre e senza eccezioni** per ogni personaggio nativo o storico, per prevenire la comparsa anacronistica negli scenari storici o futuri.

### Tabella di Triage per l'Importazione

| Tipologia di Entry Sorgente | Destinazione / Azione nel World |
|---|---|
| **Species Details / Intimacy Profile del proprietario** | **Non importare** nella description della card; creare una Lexicon separata tipo `memory` con `party_conditions` (vedi Regola 07). |
| **Personaggio vivo ricorrente in più file** (es. Magnus, Elizabeth, Kaladin) | Creare **una sola volta** come Character con Start Position; linkare e referenziare nelle altre schede senza duplicare. |
| **Personaggio deceduto** (es. Nixara) | Creare come **Character** con Start Position ed End Position. |
| **Luogo già creato come Location** (es. The Verve) | **Non importare** il duplicato proveniente da lorebook esterni. |
| **Attività o concetto astratto** (es. underground fighting ring) | Importare come voce di **Lexicon**. |
| **Luogo fisico non ancora mappato** | Importare come **Location**. |
| **Gruppo di personaggi secondari off-world** | Accorpare in un'**unica entry Lexicon ricca** (es. "The Other Contractors"), da scorporare solo se un membro entra attivamente in scena. |
| **Lore generale di specie** (cultura, biologia, società) | Importare come Lexicon di tipo `lore/concept`, `is_global: true`, panoramica ampia senza dettagli intimi. |
| **Biologia intima / apparato riproduttivo di specie** | Entry Lexicon separata, tipo `memory`, `is_global: false`, keys primarie sul nome della specie + secondarie sull'argomento, tono enciclopedico/scientifico. |

---

## 2. Tassonomia Entry Type del World Lexicon

La tassonomia valida per il World Lexicon di Wyvern (verificata su `wiki.wyvern.chat/en/Features/Worlds/Lexicon`) comprende:
- **Voci di puro testo:** `lore/concept`, `organization/faction`, `memory`, oppure nessun tipo specificato.
- **Voci con pannelli configurativi avanzati:** `item`, `furniture`, `creature`, `move`, `nature`, `ability`.
- *Nota di rettifica:* Il tipo `mob` citato in vecchi appunti non esiste. La lore di specie generale va in `lore/concept`; `creature` va riservato esclusivamente a veri mostri/avversari fisici.

### Regola di Lys (Entry Monopersonaggio)
Ogni entry Lexicon che gravita attorno a un singolo personaggio (Intimacy Profiles, Digital Interactions, dinamiche personali, memorie biografiche):
1. Deve avere **Entry Type = Memory** (`type: "memory"`);
2. Deve essere associata al personaggio tramite il campo **Attached Character** (`attached_world_character_id`).
3. Le memorie che coinvolgono coralmente più personaggi (eventi collettivi, rituali, log di gruppo) restano senza Attached Character.

---

## 3. World Lean Architecture, Placement e Logiche di Attivazione

Per impedire che il prompt inviato all'LLM superi il Context Budget di Wyvern e provochi il troncamento della cronologia di chat:

### Confinamento Roster dei World Characters
- **Superamento del Global Character ON generalizzato:** L'impostazione `is_global: true` a tappeto su tutti i personaggi satura il context window.
- **Regola di Confinamento:** Solo i protagonisti principali (il nucleo ristretto dei 5 Douglas: Malachia, Noah, Jasper, Erik, Alyssa) mantengono `is_global: true`.
- **Tutti gli altri 108 World Characters:** Devono avere tassativamente `is_global: false`.
- **Meccanica di Caricamento:** Gli NPC secondari (docenti CUMS, residenti di Solarton, bande criminali, Firstborn e antenati storici) entrano in contesto unicamente quando il giocatore si trova fisicamente nella loro Location o se vengono aggiunti esplicitamente al Party attivo.

### Triage Rigoroso del Lexicon Globale (`is_global: false` come Default)
- **`is_global: true` Riservato:** È consentito esclusivamente a un nucleo ristretto di concetti cosmologici e biologici universali (~30 voci max: LSE, fisiologia licantropi/vampiri, vulnerabilità argento/aconito, ciclo solare/notturno).
- **Tutte le altre voci (`is_global: false`):** Tutti i 284 NPC minori nel Lexicon, i 51 item di negozio, i 16 contratti di lavoro, le 19 memorie personali, e le entry specifiche di confraternite/negozi devono avere tassativamente `is_global: false`.
- **Significato di `is_global: false`:** Spegne l'entry dalla scansione globale del World. Voci locali e commerciali si caricano unicamente tramite associazione a specifiche Location (`included_lexicon_entries`) o Scenari.
- **Il campo `attached_world_character_id` NON è un trigger di iniezione:** serve per metadati e legami logici, non inietta il testo da solo.

### Strumenti Corretti di Attivazione e Filtraggio
1. **Chiavi Primarie e Secondarie:** Impostare sempre `key_logic: "AND_ANY"` dove le **chiavi primarie** sono identificatori specifici (es. nome del personaggio) e le **chiavi secondarie** parole tematiche (`dating`, `romance`). Evitare termini generici tra le primarie per non far sparare l'entry a sproposito.
2. **`party_conditions`:** È il filtro elettivo per i contenuti personali (es. `has_any [id_personaggio]`), assicurando che l'informazione entri in contesto solo se il soggetto è nel party attuale.

### Soglia di Sicurezza Context Budget
La somma dei metadati statici del World (Istruzioni avanzate + Location + Rotte + RPG State + Voci Lexicon scattate + Personaggi) non deve mai superare i **5.000 token**, garantendo che almeno il 70% della finestra di contesto rimanga sempre riservata alla cronologia di chat e all'input dell'utente.

---

## 4. Architettura dei 6 Lorebook Standalone per Character Scenarios & Igiene Dati

Con la dismissione della modalità World, tutto il patrimonio enciclopedico e demografico di Svartúlfr è riorganizzato nei **6 Lorebook Standalone** sincronizzati live su Wyvern (`ws=library&tab=lorebooks`) e collegati ai Character Scenarios via `lorebook_ids` (793 voci attive totali, 0 disattivate):

1. `_gwwCxCfQ6PQaLEjAQVpJL` — **Svartúlfr - Lorebook I** (221 entries: Ecologia LSE, Rune, Casate, Fazioni e Lore primaria).
2. `_HfG7TeV6MJyj6bxMwxkpt` — **Svartúlfr - Lorebook II** (139 entries: Bacheca Contratti, Economia, Oggetti, DDM Voidspace).
3. `_9zWTGqYJNJ4BCDMj8gfcD` — **Svartúlfr - Lorebook III** (35 entries: Campus SUCC, CUMS, Confraternite, Sport, Underworld).
4. `_EjXxkmPVhpCXg8xABpFkK` — **Svartúlfr - Location** (188 entries: Location strutturate di Blackwood, Solarton, Riserve e Dungeon).
5. `_zwEqgEEzh12X6gHVmMKKC` — **Svartúlfr - NPC Primary** (99 entries: NPC primari, World Dossier del cast fisso, memorie intime e profili personali con Statistiche Finali).
6. `_Uht3Ckz44JBDrPnUHq7LV` — **Svartúlfr - NPC Secondary** (111 entries: NPC secondari e terziari del mondo con Statistiche Finali).

### Regole Vincolanti di Igiene Lorebook:
1. **Zero Keyword Ombrello (`BROAD_KEYS`) sugli NPC:**
   È vietato assegnare tag geografici o tassonomici generici (`solarton`, `succ`, `blackwood`, `losangeles`, `underworld`, `vampire`, `werewolf`, `human`, `demihuman`, `demon`, `college`, `student`, `alpha`, `beta`, `omega`, `pack`) alle schede NPC del Lorebook. Tali keyword causerebbero l'attivazione simultanea di oltre 100 schede, prosciugando l'intero token budget. Le keyword degli NPC devono essere unicamente il nome, cognome, soprannomi e alias univoci del personaggio.
2. **Zero `selective: true` senza `secondary_keys`:**
   In Wyvern, un'entry con `selective: true` (`AND_ANY`) priva di chiavi secondarie può bloccarne l'attivazione. Mantenere sempre `selective: false` salvo quando `secondary_keys` contiene filtri contestuali espliciti.
3. **Divieto di Macro Non Valutabili (`{{age}}`):**
   Nei Lorebook e nelle Character Card non va mai utilizzata la macro `{{age}}` (attiva solo nel World Clock). Riportare sempre l'età anagrafica calcolata e la data di nascita (`AGE: 19 (Born April 5, 2005)`).
4. **Rimozione Stringhe Ridondanti e Leak Locali:**
   La riga di formattazione non va duplicata all'interno delle singole entry dei Lorebook (è demandata ai Prompt Overrides globali). Nessun testo deve contenere percorsi file locali (`.md`, `FINAL/`, ecc.).
5. **Standard Obbligatorio Metadati per Entry NPC (Avatar Parsing & UI Splitting):**
   Ogni entry di tipo `npc` inserita o aggiornata nei Lorebook o nei Lexicon di Wyvern deve includere tassativamente i metadati completi per il parser client:
   - **`avatar`**: URL HTTPS pubblico e valido dell'immagine (Cloudflare imagedelivery o CDN Janitor `https://ella.janitorai.com/bot-avatars/{hash}.webp`).
   - **`custom_avatar_regex`: `true`**: Abilita la regex personalizzata per il riconoscimento del turno dell'NPC.
   - **`avatar_activation_regex`**: Regex multiline che rileva il nome completo, il nome proprio ed eventuali soprannomi/alias ufficiali seguiti da due punti: `(?:^|\n)\s*(?:Nome Completo|Nome|Nickname)\s*:`
   - **`lines_parsed`: `1`**: Numero di paragrafi successivi alla regex da inglobare nella bolla dell'NPC (default: `1`).
   - **`npc_info`**: Oggetto strutturato con i dati anagrafici dell'NPC (`first_name`, `last_name`, `nicknames`, `titles`).
   - **Istruzione di Formattazione Obbligatoria nei Prompt di Scenario/Card**: Ogni Character Scenario e card che impiega NPC di Lorebook deve includere nelle istruzioni la direttiva:
     > "When secondary NPCs or background characters speak or take action, always output their dialogue on a new line prefixed with their exact full name and a colon (e.g., `Santiago Herrera: [dialogue/action]`). Never blend NPC dialogue anonymously into narration."
