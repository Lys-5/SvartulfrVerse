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
