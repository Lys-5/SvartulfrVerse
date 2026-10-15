# Regola 09 — RPG Stats e Sistemi di Simulazione

- **Stato del Mondo & Configurazione Features:** In seguito all'ottimizzazione del Context Budget (World Lean Architecture):
  - `inventory: true`
  - `currency: true`
  - `rpg_stats: true`
  - `combat: true`
  - `show_party_stats: false` (Disattivato: evita l'iniezione automatica di pesanti tabelle ASCII numeriche nel prompt a ogni turno)
  - `show_species_info: false` (Disattivato: evita l'inclusione di manuali descrittivi di specie nel prompt)
  - `relationships: true`
  - `ships: false` (Disattivato: cross-world ships non pertinenti al canone)
  - `creature_catcher: false` (Disattivato: meccanica capture/evolve disattivata)
- **Conseguenza Operativa:** Con il modulo attivo ma con i display testuali del prompt disattivati, le schede native e i sistemi di calcolo/simulazione rispettano i parametri di budget e blueprint, mentre la UI dei pannelli e lo StoryEngine continuano ad accedere regolarmente ai valori senza intasare la cronologia dei messaggi.

---

## 2. Convenzioni di Progetto (In Caso di Riattivazione)

Qualora l'utente richieda esplicitamente di configurare o riattivare il modulo RPG, attenersi rigidamente a questi parametri:

- **Budget Punti Statistiche:** Fisso a **25 punti** spendibili (indipendentemente dal Livello del personaggio). Considerando la base di partenza di 1 punto su ciascuna delle sei caratteristiche, la somma algebrica finale deve dare esattamente **31**.
- **I Sei Attributi Base:**
  - `stat_1`: Might (MGT)
  - `stat_2`: Resilience (RES)
  - `stat_3`: Agility (AGI)
  - `stat_4`: Wits (WIT)
  - `stat_5`: Presence (PRS)
  - `stat_6`: Scent (SCT)
- **Livello RPG:** Regola generale: **Livello = Età Anagrafica**, salvo la soglia critica descritta di seguito.

---

## 3. Bug Critico della Piattaforma e Tetto al Livello 99

- **Bug Accertato:** L'inserimento di un Livello elevato (accertato con Livello 300; il limite critico risiede tra 100 e 299) **fa fallire silenziosamente il salvataggio dell'intero blocco RPG**. L'interfaccia resta bloccata su "Saving..." e al successivo reload i dati RPG risultano azzerati e disabilitati.
- **Convenzione Salvavita per Personaggi Longevi:** Per tutti i personaggi che superano il secolo di vita (es. Zefir, Ut, Wulfnic, Cornelius, Archer, Magnus, Dullahan, e Pureblood come Vito Marino e Marcus O'Connor), impostare tassativamente **Livello = 99**. L'età reale ultracentenaria rimane indicata nel blocco JED+.

---

## 4. Species e Occupation: Gestione Esclusiva via API

- **Bug dell'Interfaccia Web:** I selettori a tendina per Species e Occupation nella UI non inviano i dati correttamente: al salvataggio tornano a `None`.
- **Scrittura Corretta via API:** Species e Occupation fanno parte integrante dell'oggetto `rpg_stats` (`rpg_stats.species_id` e `rpg_stats.occupation_id`). Vanno salvati tassativamente tramite chiamata API mirata (vedi Regola 11).
- **Assegnazione Realistica:** Poiché la lista delle Occupation predefinite (blueprint) è limitata (Bartender, Bodyguard, CEO, DJ, Divine Guardian, General Laborer, Line Cook, Living Saga, Master Blacksmith, Matriarch, Mechanic, Musician, Patriarch, Security Commander, Server, Stage Technician, Student, Teacher), selezionare il ruolo concettualmente più vicino senza forzature anacronistiche.

---

## 5. Protocollo di Formulazione RPG & Dossier Integrale Obbligatorio

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
