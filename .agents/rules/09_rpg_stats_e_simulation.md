# Regola 09 — RPG Stats e Calcolo Statistiche Finali (Character Scenarios)

## 1. Passaggio dalle Statistiche Base del World alle Statistiche Finali (Card & Lorebook)

Con la dismissione del modulo World di Wyvern e il passaggio ufficiale a **Character Scenarios**, non esiste più un motore esterno che sommi a runtime i modificatori di Specie, Occupazione e Tratti alle statistiche base.

**Regola Operativa Vincolante:**
- All'interno del blocco `RPG STATS & TRAITS:` inserito in fondo alla `description` delle Character Card (`/mine`), delle User Personas e delle schede nel Lorebook `Svartúlfr - NPC Primary` / `NPC Secondary`, **non vanno riportate le sole statistiche base (somma 81), bensì le Statistiche Finali calcolate** (`[STATS: STR ...; PER ...; END ...; CHA ...; INT ...; AGI ...; LCK ...]`), comprensive di tutti i bonus e i malus derivanti da:
  1. **Specie (`Species`)** (es. *Licantropo*: `STR +2, END +2, PER +1, INT -1`);
  2. **Occupazione (`Occupation`)** (es. *Technomancer / Cyber-Mage*: `INT +2, PER +1, STR -1`; *Guild Berserker*: `STR +2, END +2, INT -1`; *Pack Leader*: `CHA +2, STR +1, END +1`; *Firstborn Apex Sovereign*: `STR +3, END +3, CHA +2, PER +2`);
  3. **Tutti i Tratti (`Traits`)** posseduti dal personaggio, indicando accanto a ciascun tratto, specie e occupazione i relativi modificatori tra parentesi.

### Formula di Calcolo
$$\text{STAT}_{\text{finale}} = \text{STAT}_{\text{base}} + \Delta_{\text{Specie}} + \Delta_{\text{Occupazione}} + \sum_{i} \Delta_{\text{Tratto}_i}$$

### Formato Standard del Blocco `RPG STATS & TRAITS:`
```text
RPG STATS & TRAITS:
[LEVEL: <Livello>; ARC_LEVEL: <ARC Level DDM>; SPECIES: <Specie> (<Bonus/Malus Specie>); OCCUPATION: <Occupazione> (<Bonus/Malus Occupazione>); CLASS: <Classe Narrativa>]
[STATS: STR <val>; PER <val>; END <val>; CHA <val>; INT <val>; AGI <val>; LCK <val>]
TRAITS:
- <Nome Tratto> (<Bonus/Malus Tratto>): <Descrizione del tratto>
```

---

## 2. Convenzioni di Bilanciamento, Composizione Tratti, Curva dei Livelli (Max 99) e Classificazione ARC Level DDM

- **I Sette Attributi Ufficiali:**
  - `STR` (Strength), `PER` (Perception), `END` (Endurance), `CHA` (Charisma), `INT` (Intelligence), `AGI` (Agility), `LCK` (Luck).
- **Budget di Partenza (Base Stats prima dei modificatori):** 81 punti totali (base 8 su tutte e 7 le statistiche = 56, più 25 punti distribuibili).
- **Regola di Composizione del Profilo RPG (`1 Specie + 1 Occupazione + 5..15 Tratti`):**
  - Tutti i personaggi (Character Card, User Persona e NPC dei Lorebook) devono avere obbligatoriamente **1 Razza/Specie (`Species`)** + **1 Occupazione (`Occupation`)** + **da un minimo di 5 a un massimo di 15 Tratti (`Traits`)** per il calcolo delle statistiche RPG.
  - **Massimo di 15 Tratti per Protagonisti e Personaggi Molto Potenti:** I **protagonisti** (`Alyssa`, `Jasper`, `Malachia`, `Noah`, incluse le rispettive varianti High Fantasy) e i **personaggi per lore molto potenti** (es. i Firstborn primordiali `Wulfnic`, `Zefir`, `Ut`, i capifamiglia e veterani d'élite come `Erik`, `Logan`, `Magnus`, `Cornelius`, `Zeera`, i Contractors DDM, i Demoni Superiori come `Father Revazhael`, ecc.) devono possedere **il massimo consentito, ovvero esattamente 15 tratti**.
- **Curva Canonica dei Livelli per Età Anagrafica (Max Livello 99):**
  - **Da 0 a 13 anni (`0 <= età <= 13`):** `Livello = 1` (es. Edric a 13 anni $\to$ `LEVEL: 1`).
  - **Da 14 a 21 anni (`14 <= età <= 21`):** `Livello = 2` (es. Alyssa e Jasper a 19 anni $\to$ `LEVEL: 2`).
  - **Maggiore di 21 anni (`età > 21`):** **`+1 livello ogni 5 anni`** oltre i 21 anni, secondo la progressione:
    $$\text{Livello} = \min\!\left(99,\; 2 + \left\lceil \frac{\text{età} - 21}{5} \right\rceil\right)$$
    *(es. 22–26 anni = Livello 3 [Noah, 25]; 27–31 anni = Livello 4 [Malachia, 28]; 47–51 anni = Livello 8 [Logan, 49]; 52–56 anni = Livello 9 [Erik, 55]; 137 anni = Livello 26 [Zeera]).*
  - **Tetto Massimo al Livello 99 (`Max Level 99`):** Per tutti i personaggi ultracentenari/millenari il cui calcolo superi 99 (`Wulfnic`, `Zefir`, `Ut`, `Cornelius`, `Magnus`, `Nixara`, `Father Revazhael`), il livello RPG è fissato a **99**, mentre l'età reale millenaria o secolare è dichiarata nel blocco JED+ (`AGE: ...`).
- **Classificazione DDM `ARC_LEVEL` (*Active / Alternate Reality Control*, Scala `0.0 – 5.0+` da `https://io-ddm.uwu.ai/`):**
  - Ogni scheda personaggio, User Persona e voce NPC riporta obbligatoriamente il parametro **`ARC_LEVEL`** sia nel blocco PList iniziale `[...]` sia nell'intestazione `[LEVEL: ...; ARC_LEVEL: ...; ...]` del blocco `RPG STATS & TRAITS:`:
    - **ARC Level `0.0`:** Non-concetto o oggetto inanimato privo di impatto sulla realtà.
    - **ARC Level `1.0` (`0.8 – 1.1`):** Mortale umano standard privo di magia; **`1.2+`** è la soglia minima naturale di idoneità per un contratto DDM.
    - **ARC Level `1.5 – 2.1` (Grado 2 / ACEs & Sovrannaturali Base):** Forza/sensi potenziati, empatia o telepatia minore; fascia tipica degli **ACE DDM** (`Corrin Snow: 1.8`, `Elias Carter: 1.9`, `Orion Kovač: 1.9`, `Aria Xenthon: 2.0`, `Catharsis Eight: 2.1`), dei Gamma pre-shift (`Edric: 1.6`) e degli studenti sovrannaturali SUCC.
    - **ARC Level `2.2 – 2.9` (Soglia Chiusura Reality Tears):** `2.2` è il requisito minimo per sigillare autonomamente una *Reality Tear*; include operativi tattici e cacciatori di gilda (`Larek: 2.2`, `Echo: 2.3`, `Mackenzie: 2.4`).
    - **ARC Level `3.0 – 3.9` (Grado 3 / Alta Magia, Mutazione & Contractors Standard):** Controllo elementale/runico avanzato, trasmutazione, manipolazione di portali e squarci:
      - `Noah`: `3.2 (Pack Delta & Runic Tactician)`
      - `Logan`: `3.4 (Elder Beta & DCC Commander)`
      - `Hana & Adam Valencia (Contractor #02)`: `3.5 [medicated] - 4.2 [raw]`
      - `Alyssa (Modern & High Fantasy)`: `3.6 (Base) / 4.2 (White Moon Hvit Resonance)`
      - `Jasper (Modern & High Fantasy)`: `3.6 (Base) / 4.2 (Solar Svartr Resonance)`
      - `Zeera Darkfire`: `3.6 (Horned Skull Clan Leader)`
      - `Erik Douglas`: `3.7 (Prime Alpha of Seven Hills)`
      - `Malachia (Modern & High Fantasy)`: `3.8 (Base) / 4.4 (Bastion Enigma Spike)`
      - `Luka Sutter (Contractor #03)`: `3.8` | `Dr. Johan Jakobsen (Contractor #05)`: `3.9`
    - **ARC Level `4.0 – 4.9` (Grado 4 / Alterazione della Realtà, Firstborn, Contractors Senior & Re SERAPHIM):**
      - `Fenrir (Contractor #06)`: `4.0` | `Nixara`: `4.0` | `Cornelius & Magnus`: `4.1`
      - `Father Revazhael`: `4.3 (Greater Nightmare Demon)`
      - `Zefir & Ut Berg`: `4.4 (Surviving Firstborn Enigma)` | `Chaos (2nd King)`: `4.4`
      - `Dullahan (Contractor #04)`: `4.5` | `Chorus (4th King)`: `4.5 [unstable]`
      - `Richard Whitlock (Contractor #01)`: `4.6` | `Prism (3rd King)`: `4.6`
      - `Wulfnic Báleygr Bloodmoon`: `4.8 (Primordial Firstborn Enigma)` | `Raphael (#00 / 1st King)`: `4.8`
    - **ARC Level `5.0+` (Grado 5 / Entità Divina / Cosmica):** Divinità primordiali (`Fenris`, `Máni`, `Sól`, `Hati`, `Sköll`) e `The Council` (`>5.0`).

---

## 3. Protocollo di Formulazione RPG & Matrice delle Stirpi

È fatto divieto assoluto a qualsiasi assistente AI di proporre, generare o modificare tratti RPG, occupazioni, razze, classi o statistiche basandosi su dati parziali, intuito o inferenze dal solo nome del personaggio.

1. **Lettura Integrale del Dossier:** Prima di qualsiasi proposta o modifica, recuperare e leggere l'intero testo descrittivo del personaggio e le relative voci del Lorebook.
2. **Matrice Tassonomica Vincolante delle Stirpi Dinastiche:**
   - `Divine Blood`: riservato **esclusivamente** ai tre Firstborn primordiali (`Wulfnic`, `Zefir`, `Ut`).
   - `Founding Bloodline`: riservato a `Nixara`, ai Firstborn, alla seconda generazione di sangue misto Douglas-Bloodmoon (`Alyssa`, `Jasper`, `Malachia`, `Noah`), e ai diretti discendenti delle stirpi primordiali nei boschi tradizionali: `Thorvald` (discendente diretto del Firstborn Ut Berg) e `Harald Sigurdsson` (scion diretto di uno dei Nove Firstborn caduti). Non appartiene a `Erik` né a `Logan`.
   - `Pureblood Lineage`: riservato alle casate storiche di pura discendenza: Douglas (`Erik`, `Logan`, `Edric`, `Magnus`, `Cornelius`), Duskwood (`Elizabeth`), Wolfwood (`Archer`), Rogers (`Mackenzie`).
   - *Doppia Linea di Sangue:* I quattro fratelli Douglas-Bloodmoon (`Alyssa`, `Jasper`, `Malachia`, `Noah`) possiedono contemporaneamente sia `Founding Bloodline` che `Pureblood Lineage`.
3. **Invarianti Assolute di Sottogenere Lupino (LSE):**
   - **Noah Loki Douglas Bloodmoon:** Tassativamente un **Delta** (`LSE Delta Biology`; zero tratti Alpha, zero Alpha Command).
   - **Jasper Svartr Douglas Bloodmoon:** Tassativamente un **Beta** (`LSE Beta Biology`; zero tratti Alpha).
   - **Logan Dominic Járn Douglas:** Tassativamente un **Beta** (`LSE Beta Biology`; zero tratti Alpha).
   - **Edric Douglas:** Tassativamente un **Pre-Presentation Gamma** (`Pre-First Shift (Gamma)` e `Pureblood Lineage`; zero tratti Alpha).
   - **Malachia Björn Douglas Bloodmoon:** **Dominant Alpha** (futuro Pack Leader designato; possiede `Pack Leader`, `Dominant Alpha`, `Alpha Command`, `Ascended Enigma`, `Apex Core Resonance`).
   - **Erik Ulfr Douglas:** **Prime Alpha** (Pack Leader in carica della Casata Douglas; possiede `Pack Leader`, `Dominant Alpha`, `Alpha Command`, `Apex Core Resonance`).
   - **Kemonomimi Demi-Umani (es. Finn Novak, Roman Blackwood):** Non sono licantropi (nessun Partial o Hybrid Shift, nessuna allergia all'argento, nessuna rigenerazione lunare; possiedono un solo paio di orecchie animali).

---

## 4. Motore di Risoluzione D20 + S.P.E.C.I.A.L. per Game Master & Narratori

Per gli Assistant e i Prompt Assembly che operano come Game Master (come `Svartúlfr — Game Master & World Engine`), le azioni rischiose o incerte intraprese da `{{user}}` o dai PNG vengono risolte mediante il motore D20 parametrato sugli attributi S.P.E.C.I.A.L.

### 4.1 Formula di Conversione
I punteggi S.P.E.C.I.A.L. calcolati (comprensivi di Livello, Specie, Occupazione e Tratti) generano il modificatore al tiro del dado a venti facce (D20):
$$\text{Mod} = \left\lfloor \frac{\text{Stat} - 10}{2} \right\rfloor$$

### 4.2 Classi di Difficoltà (CD / DC)
- **CD 10 (Facile / Routine sotto stress):** Azioni standard eseguite sotto pressione moderata.
- **CD 15 (Media / Professionale):** Azioni che richiedono addestramento specifico.
- **CD 20 (Difficile / Esperto):** Sfide complesse, hackeraggio sistemi protetti, manovre tattiche avanzate.
- **CD 25 (Estrema / Master):** Limite delle capacità individuali.
- **CD 30 (Eroica / Quasi Impossibile):** Imprese leggendarie.

### 4.3 Risoluzione a 4 Livelli (Dice & Outcomes)
1. **Successo Critico (Nat 20 o Margine $\ge +10$ rispetto alla CD):** Successo con slancio eccezionale, vantaggio tattico o risorsa risparmiata.
2. **Successo Pieno ($\text{Totale} \ge \text{CD}$):** Obiettivo raggiunto senza imprevisti negativi.
3. **Successo con Costo / Fallimento Parziale (Margine tra $-1$ e $-4$):** Azione riuscita ma con complicazione narrativa o consumo di risorse, oppure fallimento pulito senza ritorsioni disastrose.
4. **Fallimento Critico (Nat 1 o Margine $\le -10$ rispetto alla CD):** Conseguenza avversa immediata (inceppamento, danno, innesco allarmi).

### 4.4 Isolamento Diegetico Obbligatorio
Tutti i calcoli numerici, tiri di dadi e verifiche meccaniche devono essere rigorosamente isolati su riga autonoma all'inizio o alla fine del messaggio in un blocco compatto:
```markdown
> [TEST: <Attributo> (D20: <Tiro> + <Mod> = <Totale> vs DC <Target>) -> ESITO: <SUCCESSO / FALLIMENTO / SUCCESSO CRITICO / FALLIMENTO CRITICO>]
```
Il corpo narrativo deve rimanere al 100% letterario, viscerale e sensoriale, traducendo l'esito del tiro in conseguenze fisiche e psicologiche concrete senza inquinare la prosa con gergo numerico.

---

## 5. Regola di Auto-Provisioning RPG (Specie, Occupazioni e Tratti Mancanti)

Durante la fase di creazione o modifica di qualsiasi personaggio (Character Card in `/mine` o `FINAL/`, User Persona o scheda NPC nei Lorebook `_zwEqgEEzh12X6gHVmMKKC` e `_Uht3Ckz44JBDrPnUHq7LV`):

1. **Verifica della Corrispondenza nei Cataloghi:** L'assistente e la pipeline di deploy devono verificare preliminarmente che la `Specie`, l'`Occupazione` e tutti i `Tratti` dichiarati nel blocco RPG del personaggio trovino corrispondenza esatta nei cataloghi registrati sul World attivo (`POST /api/worlds/rpg/species`, `/occupations`, `/traits`) e nei cataloghi master locali (`scratch/rpg_*_catalog.json` e `FINAL/`).
2. **Auto-Provisioning Immediato:** In caso di mancata corrispondenza (nessun match per nome o identificatore), il sistema o l'assistente **non deve rimuovere il tratto né generare errori bloccanti**, ma deve procedere **immediatamente alla creazione automatica (Auto-Provisioning)** dell'entità mancante sul World via Web API:
   - **Endpoint:** `POST https://app.wyvern.chat/api/worlds/rpg/{species|occupations|traits}`
   - **Payload Obbligatorio:**
     ```json
     {
       "world_id": "_YpX47fNraQFw2dD7TdycJ",
       "name": "<Nome Esatto della Specie / Occupazione / Tratto>",
       "description": "<Descrizione narrativa diegetica, accurata e contestuale>",
       "player_selectable": true,
       "stat_modifiers": { "<stat_special>": <valore_delta> },
       "tags": [],
       "display_order": <prossimo_indice>
     }
     ```
3. **Modificatori Coerenti con S.P.E.C.I.A.L.:** I modificatori assegnati (`stat_modifiers`) devono utilizzare tassativamente gli attributi S.P.E.C.I.A.L. ufficiali (`strength`, `perception`, `endurance`, `charisma`, `intelligence`, `agility`, `luck`) e riflettere fedelmente le capacità biologiche, mistiche o professionali descritte nella backstory o nel blocco JED+.
4. **Sincronizzazione Contestuale dei Cataloghi Master:** Contestualmente alla creazione remota via API, l'assistente deve registrare la nuova entità nei cataloghi JSON master locali per preservare la parità omni-canale (`Omni-Parity`) e impedire drift tra World e archivio locale.

