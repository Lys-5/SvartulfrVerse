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
