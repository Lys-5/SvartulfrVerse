# Audit di ripristino dati — 2026-09-21

Su richiesta di Lys ("evitiamo le folder e concentriamoci sul ripristinare tutti i dati"), controllo sistematico di ogni sezione del World nell'ordine indicato. Confronto fatto contro i conteggi/valori più recenti già verificati e documentati nel Project (non contro l'API, solo UI/JS in pagina, per il vincolo di sicurezza sulle scritture dirette).

## Esito riassuntivo

**Trovata perdita di dati reale e concreta in almeno 3 punti**, non riconducibile a un problema di questa sessione (la traccia mostra che il calo era già presente il 20/09, prima di oggi):

1. **Environments: 13 → 2.** Il 13/9 l'audit dava 13 Environments (118/118... anzi 13/13 classificati in folder). Oggi ne esistono solo **California Coast** e **Voidspace** (quest'ultimo creato oggi). Mancano almeno: Blackwood Forest, Bloodmoon Pack Territory, Blackwood City, Hex Valley, Solarton, SUCC Campus, Zone di Transito e Confine, CUMS (promosso a Environment). Il documento `Scenari_Arco_2024_9Schede_Completamento_2026-09-20.md`, scritto il 20/9 **prima** di questa sessione, nota già "il World ha solo 2 opzioni Environment: None e California Coast" — quindi la perdita è avvenuta **fra il 13/9 e il 20/9**, non oggi.
2. **Travel Routes: azzerate.** `World_Modifiche_Da_Applicare.md` documenta la creazione di rotte traghetto con tre scali (Dockside, Hex Valley, Bay Area). La pagina Travel oggi mostra: "No travel routes defined here yet." Free Travel è OFF, quindi queste rotte sono davvero necessarie per il gameplay e mancano.
3. **Relationships — Tier ladder personalizzata persa.** Il progetto aveva una ladder a tema LSE (Blood Enemy, Enemy, Rival, Distrusted, Wary, Unknown Scent, Acknowledged, Trusted, Pack, Pack-bonded, Beloved — §16 delle istruzioni). La pagina Relationships oggi mostra la ladder **di default della piattaforma**: Nemesis, Enemy, Despised, Hated, Disliked, Stranger, Acquaintance, Friend, Close Friend, Best Friend, Romantic Interest, Lover, Partner, Soulmate. Le soglie/colori sono anch'essi ai default (`#888888` su tutte le righe, nessun colore personalizzato).

## Anomalia da chiarire con Lys (non necessariamente perdita)

4. **World Features (tab Simulation): Inventory & Items e Currency & Economy sono ON**, insieme a Party Stats in Prompt. Per `Simulation_World_Features_Disattivate_2026-09-13.md` la decisione esplicita dell'utente era di spegnere tutto tranne Relationships. RPG Stats, Combat, Cross-World Ships, Creature Catcher risultano correttamente OFF. Non è chiaro se Lys li abbia riaccesi volutamente in una sessione successiva (non documentato) o se sia un altro sintomo dello stesso evento di perdita/reset.
5. **World Time Span: 1197 anni, 1 mese, 1 giorno, 6 ore**, contro **1249 anni, 2 mesi, 1 giorno, 6 ore** verificato il 13/9 (Task #5 di `Import_Plan_AllContent.md`). Differenza di circa 52 anni. Da capire se questo campo (durata totale documentata, non il puntatore "adesso" del World Clock) sia stato toccato da qualche intervento successivo o sia un altro segnale dello stesso reset.

## Sezioni verificate SENZA segni di perdita

- **Scenarios (9/9):** tutti e 9 gli scenari dell'arco 2024 presenti, titoli combacianti con `Scenari_Arco_2024_9Schede_Completamento_2026-09-20.md`.
- **Locations (134):** conteggio in crescita coerente rispetto al 13/9 (118), nessun segno di calo. Non verificabile nel dettaglio campo-per-campo in questo giro (troppi item), ma la traiettoria è quella attesa.
- **Lexicon (251):** conteggio in crescita coerente (240 il 16/9, 251 oggi).
- **Characters (360):** conteggio coerente con la storia di sessioni ad alto volume (stub batch da centinaia di schede il 15/9).
- **Eras (7 World Eras):** intatte, stessi confini orari già migrati e verificati (`World_Clock_Eras_E_Start_Positions.md`).
- **World Info:** World Name "Svartulfr", Description 3231 caratteri, identico byte-per-byte alla lunghezza già verificata il 13/9. Nessun segno di reset.
- **Economy:** valuta "US Dollar" ($) presente e configurata.
- **Maps (2):** Regionale + Blackwood, coerente con quanto documentato.
- **Scripts, Commands, InfoBoard, Introduction, Trees:** tutti vuoti/non configurati, ma **nessuna prova nei documenti del Project che fossero mai stati popolati** — probabile stato invariato, non una perdita.

## Cosa NON è stato ancora verificato in dettaglio

Per il volume (134 Location, 251 Lexicon, 360 Characters), non è stata fatta una verifica campo-per-campo di ogni singola scheda: solo un controllo di traiettoria sui conteggi totali. Se Lys ha il sospetto che la perdita abbia toccato anche contenuti dentro Character/Location/Lexicon specifici (non solo Environments/Travel/Relationships), serve indicarmi quali, perché un controllo esaustivo di 745 item singoli non è fattibile in un solo giro.

## Ipotesi sulla causa

Il fatto che il calo Environments fosse già presente il 20/9 (prima di questa sessione, e prima ancora del lavoro sulle folder di ieri) esclude che sia stato causato da me oggi o ieri. Possibili cause, nessuna verificabile senza accesso API: un rollback della piattaforma, un salvataggio parziale che ha sovrascritto un blocco di dati del World (coerente con il bug "PUT con oggetto completo risponde 200 e non scrive niente" già noto, se qualcosa ha effettivamente sovrascritto invece di limitarsi a non scrivere), o un intervento manuale non documentato. Non ho elementi per stabilire quale.

## Proposta

1. **Priorità di ripristino secondo me**: Relationships tier ladder (dati di configurazione, rapida da riscrivere: 11 label/soglie/colori) e Travel Routes (3 rotte traghetto, rapida). Gli Environments richiedono di riscrivere il contenuto narrativo di 7-8 voci (Blackwood Forest, Bloodmoon Pack Territory, Blackwood City, Hex Valley, Solarton, SUCC Campus, Zone di Transito e Confine, CUMS) — il testo sorgente esiste ancora in `Wyvern/environments.md` e nei documenti del Project (`World_Modifiche_Da_Applicare.md` per gli arricchimenti CUMS/SUCC/Bloodmoon), quindi è recuperabile senza inventare nulla.
2. Prima di iniziare a scrivere, vuoi che proceda con tutti e tre (Environments, Travel Routes, Relationships ladder), o preferisci un ordine diverso? E per il punto 4 (World Features Inventory/Currency/Party Stats ON), li rimetto OFF per allinearmi alla decisione del 13/9, o li lasci come sono ora nel dubbio che tu li abbia riattivati volutamente?
