# Regola 10 — Pipeline Standard delle Card e Configurazione Attitudes

## 1. Pipeline di Lavorazione Sequenziale

Ogni character card deve essere elaborata seguendo rigorosamente questa sequenza ordinata di 13 passaggi. Ogni fase va validata prima di procedere alla successiva.

1. **Raccolta e Audit delle Fonti:** Raccogliere tutte le fonti (lorebook, Q&A autore, entry Lexicon esistenti, legami già scritti in altre schede, documentazione WyvernWiki). Non avviare la scheda se le fonti sono lacunose o parziali; chiedere chiarimenti all'utente prima di ipotizzare dati chiave.
2. **Controllo Duplicati nel World:** Verificare via API (GET filtrata per nome) se il personaggio esiste già nel World come segnaposto vuoto o import grezzo. Popolare l'entità esistente per evitare duplicati orfani.
3. **Epurazione di `{{user}}` e Bonifica:** Applicare i protocolli di bonifica (Regola 07), rimuovendo ogni traccia di `{{user}}`, dinamiche non consensuali o cotte inappropriate.
4. **Redazione Campi Testuali Principali:**
   - `long_summary`: In formato standard JED+ (Regola 01) con macro `{{age}}` nel campo `AGE`.
   - `summary`: Blocco PList puro di soli tratti psicologici/comportamentali.
   - `display_description`: 1-2 frasi incisive su chi è e cosa lo rende memorabile.
   - Nickname, titoli, keys, pronomi.
5. **Configurazione 5 Outfits Contestuali:** Creare esattamente cinque outfit contestuali (Regola 03).
   - *Via API:* Inviare l'array completo in un unico payload PUT.
   - *Da Interfaccia Web:* Inserire e salvare **un singolo outfit per volta** con salvataggio intermedio (l'interfaccia sovrascrive gli elementi se inviati simultaneamente).
6. **Impostazione del Default Outfit:** Assegnare obbligatoriamente il Default Outfit (l'abito ordinario di riposo/routine, non il più appariscente). Senza Default Outfit, l'LLM allucina abiti casuali.
7. **Start Timeline Position:** Calcolata in ore assolute dal World Clock (Regola 04). Inserire la `End Position` solo ed esclusivamente per i personaggi deceduti.
8. **Gestione RPG Stats:** Verificare lo stato del modulo: in pausa di default (Regola 09). Se riattivato, impostare stat, livello (cap a 99 per ultracentenari) e blueprint Species/Occupation via API.
9. **Cinque Dialogue Examples:** Redatti secondo la disciplina di formattazione (Regola 02: virgolette, testo piano, no em-dash, no asterischi). Almeno un esempio deve ritrarre il personaggio nel suo momento di massima vulnerabilità o perdita di controllo.
10. **Configurazione Attitudes:** Compilare secondo le specifiche indicate nella Sezione 2 di questa regola.
11. **Global Character = ON:** Attivare il flag globale per garantire la disponibilità nel World.
12. **Verifica Finale Post-Scrittura:** Eseguire verifica su GET fresca o reload completo: zero `{{user}}`, zero em-dash, zero asterischi di narrazione, zero grassetto `**`, integrità di tutti i campi, Default Outfit selezionato, Intimacy Profile correttamente collegato via Attached Character.
13. **Documentazione nel Project:** Registrare decisioni di scrittura, collegamenti creati, discrepanze rilevate e snapshot dei valori precedenti in caso di scritture API massive.

---

## 2. Disciplina per le Attitudes

Ogni scheda deve possedere una mappa relazionale calibrata secondo criteri precisi:

### Destinatari Obbligatori e Selettivi
- **Alyssa e Jasper (Obbligatori):** Devono essere presenti in ogni scheda, essendo i due protagonisti del roster giocabile. Se il personaggio non li conosce, va comunque inserita la relazione con il tier più basso (`stranger`), motivando che non si sono mai incrociati. Questo impedisce all'LLM di inventare confidenze inesistenti.
- **Relazioni Pertinenti di Background:** Oltre ad Alyssa e Jasper, inserire **esclusivamente** i personaggi esplicitamente citati nel testo di background o legami di comando/branco documentati (es. Pack Leader / membri del Concilio). Se una relazione è dichiarata sulla scheda di A verso B, va inserita reciprocamente anche sulla scheda di B verso A. Vietato inventare legami fittizi solo per riempire la lista.
- **The Player (Persona):** Non va usato per sentimenti verso individui specifici; serve solo per attitudini generali verso qualunque giocatore impersonato (es. diffidenza generica verso qualsiasi estraneo).

### Parametri Tecnici di Compilazione
1. **Target Type:** `World Character` quando il bersaglio è un personaggio con scheda nel World. Il tipo `Generic (text)` si usa solo per fazioni collettive, gruppi o ideologie (es. posizione verso *Humans First*).
2. **Tier API vs Ladder a Schermo:**
   - L'API registra esclusivamente le chiavi di sistema standard: `stranger`, `acquaintance`, `friend`, `close_friend`, `best_friend`, `disliked`, `despised`, `hated`, `enemy`, `rival`, `wary`, `acknowledged`, `romantic_interest`.
   - La ladder personalizzata visibile in interfaccia (Blood Enemy, Enemy, Rival, Distrusted, Wary, Unknown Scent, Acknowledged, Trusted, Pack, Pack-bonded, Beloved) è una pura etichettatura grafica a video. Non crea nuove chiavi API. Nelle scritture API usare le chiavi grezze stabili (es. `stranger` per "mai incontrato").
3. **Intensity (Obbligatoria):** Se lasciata vuota, la piattaforma la imposta di default al valore minimo **1** (non a metà come indicato in alcune guide). Va sempre valorizzata esplicitamente:
   - `15`: Mai incontrati / estranei assoluti.
   - `20 – 25`: Conoscenza superficiale o indiretta.
   - `50`: Rapporto professionale, di routine o neutrale.
   - `85`: Relazione fondamentale, cardine identitario o legame viscerale.
4. **Reasoning:** 1 o 2 frasi concise che spieghino l'origine storica o psicologica dell'atteggiamento.
