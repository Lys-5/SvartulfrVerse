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
[LEVEL: <Livello>; SPECIES: <Specie> (<Bonus/Malus Specie>); OCCUPATION: <Occupazione> (<Bonus/Malus Occupazione>); CLASS: <Classe Narrativa>]
[STATS: STR <val>; PER <val>; END <val>; CHA <val>; INT <val>; AGI <val>; LCK <val>]
TRAITS:
- <Nome Tratto> (<Bonus/Malus Tratto>): <Descrizione del tratto>
```

---

## 2. Convenzioni di Bilanciamento e Tetto al Livello 99

- **I Sette Attributi Ufficiali:**
  - `STR` (Strength), `PER` (Perception), `END` (Endurance), `CHA` (Charisma), `INT` (Intelligence), `AGI` (Agility), `LCK` (Luck).
- **Budget di Partenza (Base Stats prima dei modificatori):** 81 punti totali (base 8 su tutte e 7 le statistiche = 56, più 25 punti distribuibili).
- **Tetto al Livello 99 per Personaggi Ultracentenari:** Per tutti i personaggi che superano il secolo di vita (`Wulfnic`, `Zefir`, `Ut`, `Cornelius`, `Magnus`, `Nixara`), il livello RPG rimane fissato a **99**, mentre l'età reale millenaria o secolare è dichiarata nel blocco JED+ (`AGE: ...`).

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
