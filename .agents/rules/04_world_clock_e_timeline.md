# Regola 04 — World Clock e Gestione Timeline

## 1. Coordinate Temporali di Riferimento

Il World Clock di Wyvern per il mondo Svartúlfr è calibrato sui seguenti parametri strutturali:

- **World-age 0 (Epoca):** 21 dicembre 827 d.C., ore 00:00 UTC.
  - Valori letti dall'API del World:
    - `human_start_date: "0827-12-21T00:00:00.000Z"`
    - `calendar.start_year: 827`
    - `start_month_id: "dec"`
    - `start_day_of_month: 21`
- **Anno Corrente del World:** **2024**.
- **World-Age Corrente:** **10486470** (corrispondente esattamente al **5 aprile 2024, ore 06:00 UTC**, riconfermato via API il 14 settembre).
- *Attenzione:* Qualunque riferimento al 2022 reperibile nei documenti legacy o nelle fonti grezze è un residuo obsoleto e va ignorato.

---

## 2. Calcolo Matematico delle Ore Assolute

Il calcolo delle ore assolute si basa sul calendario gregoriano prolettico standard:

$$\text{ore} = (\text{giorni trascorrenti dall'Epoca}) \times 24 + \text{ora del giorno}$$

### Snippet di Verifica in JavaScript (Browser Console o Node)

Per verificare o convertire date e ore senza commettere errori di calcolo:

```javascript
const EP = Date.UTC(827, 11, 21); // 21 Dicembre 827 UTC
const dataDaOre = h => new Date(EP + h * 3600000).toISOString().slice(0, 10);
const oreDaData = iso => (Date.parse(iso) - EP) / 3600000;
```

---

## 3. Controlli di Integrità Temporale (Sanity Checks)

Prima di salvare o validare qualunque scheda:
1. Per ogni personaggio vivente, `birthdate` (ora assoluta di nascita) e `start_timeline_position` (ora di inizio presenza nel mondo) devono **coincidere**.
2. Né `birthdate` né `start_timeline_position` possono essere maggiori di `world_age` corrente (10486470).
3. La `start_timeline_position` va inserita **sempre e senza eccezioni** per ogni personaggio (vedi Regola 08 per i dettagli sugli scenari temporali fuori asse).

---

## 4. Passività Cronologica Assoluta per Game Master e Scenari (Zero Date Reset)

Con l'introduzione dell'**AI Time Tracking** nativo su Wyvern, il reset sistematico della data ongame (es. ritorno persistente al "15 marzo 2024" o a date di apertura scenario) è causato dal tentativo del modello di generare attivamente o forzare intestazioni temporali fisse per imitazione di boilerplate (*Example Memorization*).

### Direttiva Vincolante:
1. **Passività Assoluta:** Il Game Master e i prompt degli Scenari **NON gestiscono né determinano la data del mondo**.
2. **Ereditarietà Passiva:** Il modello deve unicamente leggere e riflettere la data e l'ora ereditate dall'ultimo turno di gioco o fornite nativamente dal runtime di Wyvern.
3. **Divieto Date Boilerplate:** È severamente vietato inserire date fisse cablate (es. 15 marzo 2024) in prompt o risposte.

---

## 5. Standard Scenari a Innesco Timeline (Starts When & Scenario-Guided-Intro)

Per consentire l'inserimento automatico organico degli Scenari nel corso delle sessioni di gioco (secondo la guida ufficiale Wyvern `wiki.wyvern.chat/Features/Worlds/Scenario-Guided-Intro`):

1. **Singola Apertura Obbligatoria (Single Premade Scene):**
   - Ogni Scenario progettato per l'innesco automatico temporale deve contenere tassativamente **una sola scena premade** (`premade_scenes.length === 1`) oppure operare a **sole istruzioni di scena** (`scene_instructions`). È vietato inserire aperture multiple nello stesso scenario: la presenza di più opzioni di apertura blocca l'engine con il warning `opening_choice` ("This scenario has more than one opening, so the event cannot choose one on its own").
2. **Divieto di Insertion Point negli Scenari Automatici:**
   - Il campo `insertion_point` deve essere impostato a `null` (assente). Gli eventi automatici non possono richiedere conferme di reset dell'orologio all'utente: la presenza di un insertion point causa il blocco `time_override` ("This scenario has an Insertion Point. An automatic event cannot ask whether to set the chat clock, so it is skipped").
3. **Parametri di Innesco (`Starts when`):**
   - `repeat`: `"once"` (Auto-trigger once per party) oppure `"cooldown"` con `cooldown_messages: 20`.
   - `priority`: Valore numerico intero (priorità maggiore eseguita per prima).
   - `conditions`: Array di condizioni logiche (con logica `AND` o `OR`):
     - `time_basis: "world_day"` con `world_day_number: <N>` (Giorno 1 = Ora 0 = Lunedì 21 Dicembre 827 CE);
     - Oppure `time_basis: "world_time"` con soglia in ore;
     - Condizioni di party / persona (`party_has_character` o `persona`).

---

## 6. Sincronizzazione Time of Day e Sfondi Dinamici
- L'AI Time Tracking calcola automaticamente la fascia oraria corrente tra `dawn`, `day`, `dusk` e `night`.
- Nelle Location censite nel World, nel Lexicon o nel Lorebook Location (`_EjXxkmPVhpCXg8xABpFkK`), associare per ciascun periodo l'immagine d'atmosfera corretta, consentendo alla piattaforma di sfumare lo sfondo in tempo reale al procedere della timeline.
