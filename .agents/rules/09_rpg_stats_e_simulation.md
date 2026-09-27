# Regola 09 — RPG Stats e Sistemi di Simulazione

## 1. Stato Attuale: Sistema in Pausa

- **Stato del Mondo:** Il flag `world_features.rpg_stats` è impostato su `false` a livello globale del World (l'intero modulo Simulation, tranne *Relationships/Attitudes*, è disattivato dall'utente in seguito a test empirici approfonditi).
- **Conseguenza Operativa Standard:** Il passaggio relativo alle RPG Stats è **in pausa di default su ogni nuova character card**. Non abilitare le statistiche, non distribuire punti, né forzare Livello/Specie/Occupazione su nuove schede a meno di esplicita richiesta per quella specifica sessione.
- *Preservazione Dati Esistenti:* Se una card ha già le RPG Stats valorizzate, i dati possono essere conservati: resteranno latenti e inattivi nel gioco finché il modulo rimarrà disattivato a livello World, pronti per un eventuale ripristino.

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
