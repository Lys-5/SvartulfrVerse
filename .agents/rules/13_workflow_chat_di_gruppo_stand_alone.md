# Regola 13 — Standard Operativo Chat di Gruppo Stand-Alone (/mine)

Nelle sessioni di gioco giocate al di fuori del World (Chat di Gruppo stand-alone con 2-6 personaggi di `/mine`):

## 1. Architettura delle Schede in `/mine`
- **JED+ Compatto:** Ogni scheda in `/mine` deve avere un peso calibrato tra **1.000 e 1.500 token** per preservare il context window del gruppo.
- **Disciplina di Formattazione:** Dialoghi tra virgolette inglesi doppie standard (`"..."`), narrazione in testo semplice senza asterischi, asterischi riservati solo ai pensieri, divieto assoluto dell'em-dash (`—`).
- **Anatomia Demi-Umani:** Un solo paio di orecchie (solo orecchie animali).

## 2. Disaccoppiamento dello StoryEngine
- Nella definizione dello StoryEngine (`engine_HCTPXhL8xr89wUY9r9dYU`), l'array `worlds` deve essere impostato su `[]` (`definition.worlds = []`).
- Questo impedisce all'engine di tentare di risolvere, scansionare o richiamare in loop l'intero World esterno durante una chat di gruppo locale, garantendo tempi di risposta immediati e zero token sprecati.

## 3. Gestione Lorebook Reattivo
- Ciascuna scheda ha collegati i 3 Lorebook stand-alone (`Svartúlfr - Lorebook`, `Svartúlfr - NPC Primary`, `Svartúlfr - Location`).
- I Lorebook stand-alone operano in modalità di scansione selettiva: scansionano unicamente gli ultimi messaggi e iniettano solo 0-2 voci se espressamente citate.
- Nessuna voce globale viene forzata a ogni turno: il consumo del Lorebook rimane inferiore a 500-1.000 token per turno.

## 4. Prestazioni Attese
- Il prompt complessivo iniziale prima della cronologia deve rimanere stabilmente tra **4.000 e 6.000 token**.
- La cronologia dei messaggi e l'input del giocatore rimangono integri al 100%, garantendo coerenza narrativa e assenza di troncamenti.
