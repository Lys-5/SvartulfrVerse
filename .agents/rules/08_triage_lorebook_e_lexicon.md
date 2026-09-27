# Regola 08 — Triage Import Lorebook ed Architettura Lexicon World

## 1. Triage delle Entità da Importare

I personaggi (anche deceduti) non vanno più archiviati come semplici voci di dizionario:
- **Personaggi Vivi:** Vanno importati come **Character**, impostando **Start Position** (calcolata dal World Clock).
- **Personaggi Deceduti:** Vanno importati come **Character**, configurando sia **Start Position** che **End Position** (modello Nixara).

*Obbligo della Start Position:* La Start Position va impostata **sempre e senza eccezioni** per ogni personaggio, anche contemporaneo, per prevenire la comparsa anacronistica negli scenari storici o futuri (es. la nave vichinga di Wulfnic, lo scenario pirata di Cornelius o l'anno 2499). La `End Position` per i personaggi vivi sarà inserita solo quando lo scenario futuristico 2499 verrà finalizzato.

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

## 3. Placement e Logiche di Attivazione

### Character Placement
Tutti i Character devono essere impostati con **Global Character = ON**. L'assegnazione selettiva ai singoli Character Pool di Location o Environment è sconsigliata: appesantisce il sistema senza benefici concreti.

### Meccanica di Attivazione delle Entry Lexicon
- **Significato di `is_global: false`:** Non confina l'entry, ma la **spegne completamente** dalla scansione automatica a parole chiave del World. Rimarrà attiva solo se inserita esplicitamente in `included_lexicon_entries` di una specifica Location, Environment o Scenario, e necessiterà comunque di un match di chiave o di `constant: true`.
- **Il campo `attached_world_character_id` NON è un trigger di iniezione:** serve per metadati e legami logici, non inietta il testo da solo.
- **Strumenti Corretti di Attivazione e Filtraggio:**
  1. **Chiavi Primarie e Secondarie:** Impostare sempre `key_logic: "AND_ANY"` dove le **chiavi primarie** sono identificatori specifici (es. nome del personaggio) e le **chiavi secondarie** parole tematiche (`dating`, `romance`). Evitare termini generici tra le primarie per non far sparare l'entry a sproposito.
  2. **`party_conditions`:** È il filtro elettivo per i contenuti personali (es. `has_any [id_personaggio]`), assicurando che l'informazione entri in contesto solo se il soggetto è nel party attuale.
- *Nota di diagnostica:* La macro `{{lexiconEntryNames}}` visualizza solo le entry candidate all'inclusione nella scena, non quelle che hanno effettivamente matchato le keyword.
