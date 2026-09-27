# Gruppo cross-reference: Warg, Jake Thompson, Coach Mithers, Rue, Allegra Lumsden, Luisa Sanchez-Rogers (2026-09-13)

Su richiesta esplicita dell'utente ("questo gruppo vanno generati in base alle info che abbiamo a disposizione prese dalle altre schede"), nessun materiale sorgente nuovo: tutto ricostruito da quello che il World conteneva già, incrociando le schede di personaggi collegati.

## Scoperta preliminare
Tutti e sei esistevano già nel World, ma in stati molto diversi tra loro. Non erano stub vuoti come temuto:

| Personaggio | Stato di partenza | Lavoro fatto |
|---|---|---|
| **Coach Mithers** | `long_summary`/`summary`/`display_description` già scritti, buoni, 3 Attitudes esistenti (incluso un `rival` verso Adelin Coso, tier confermato valido lato API oltre a quelli già documentati) | Solo pipeline mancante: 5 outfit, 5 Dialogue Examples, `final_instructions` |
| **Rue** | Idem, narrativa già scritta e purgata, 2 Attitudes (Alyssa/Jasper stranger) | Pipeline mancante: 5 outfit, 5 Dialogue Examples, `final_instructions`, più 1 Attitude aggiunta verso Adelin Coso (padre, `best_friend` 85, cablata solo ora perché la scheda del padre non collegava ancora questo verso) |
| **Jake Thompson** | `long_summary` scritto ma in italiano, `summary` in un formato raw non-PList (`attributo(valore)`, tipico di un import non lavorato) | Riscritto integralmente in inglese, JED+ standard, mantenendo tutti i fatti della fonte originale (Semi-Minotauro, fratello maggiore di Jared e Janice Thompson, amico di liceo di Alyssa e Jasper). Aggiunta pipeline completa |
| **Warg** | `long_summary` già ricco e ben strutturato (intestazioni JED+ in inglese) ma corpo del testo in italiano | Tradotto integralmente in inglese preservando ogni dettaglio (Progetto Blackwolf, piastrine del padre, rapporto con Archer Wolfwood, tregua con Kaladin/Marcus). Aggiunta pipeline completa |
| **Allegra Lumsden** | Solo `summary` in formato raw semi-strutturato (JanitorAI-style), nessun `long_summary` | Scritta da zero in JED+, incrociando l'Attitude già esistente su Mac Sanchez-Rogers (lei lo ha lasciato per lo status sociale, se ne pente e lo nega) |
| **Luisa Sanchez-Rogers** | Solo `summary` raw, nessun `long_summary`, nessuna Start Position | Scritta da zero in JED+, materiale ricco incrociato dalla scheda di Mac (madre Andrea Sanchez, fratelli Mario e James, transizione a sedici anni con supporto familiare misto, la reazione di Mac). Aggiunta anche `birthdate`/`start_timeline_position`, unico dei sei a non averla |

## Incroci usati (§9/§16)
- **Mac Sanchez-Rogers** (`_rm9PkkbWEc1zNJAUNUp6U`) è stato letto per intero: la sua card conteneva già Attitudes verso Luisa (`best_friend`, 80) e verso Allegra (`disliked`, 60, "l'ha lasciato quando ha smesso di essergli utile"). Le nuove schede di Luisa e Allegra riflettono questi rapporti dal loro lato, con la stessa sostanza ma un tono coerente con ciascun personaggio (Luisa non ha dubbi sull'affetto, Allegra lo nega attivamente).
- **Jared, Janice, Hank e Jasmin Thompson** (tutti completati in una sessione precedente) sono stati usati per verificare l'età relativa di Jake come fratello maggiore: Jared nato 4 luglio 2001 (~22-23 anni), Jake aveva già una Start Position esistente che corrisponde al 18 luglio 2000 (~23-24 anni), quindi coerente senza bisogno di ricalcolarla.
- **Archer Wolfwood, Kaladin Nargathon, Marcus Thornfield**: tutti già presenti come Character; usati per dare a Warg Attitudes concrete invece di lasciare vaghi i riferimenti del suo `long_summary` a "il suo superiore" e "la DCC Security".
- **Adelin Coso**: usato per la nuova Attitude di Rue verso il padre.

## Date/Start Position: nessuna invenzione necessaria salvo un caso
Verificate le Start Position già esistenti su cinque dei sei prima di scrivere qualunque cosa, per non sovrascriverle per errore:
- Mithers: 4 agosto 1985 (combacia con `BIRTHDAY: August 4` già nel suo `long_summary`).
- Rue: 3 settembre 2000 (combacia con `BIRTHDAY: September 3`).
- Jake: 18 luglio 2000, età ~23-24, coerente col ruolo di fratello maggiore di Jared.
- Warg: 14 giugno 1989, età ~35, combacia con l'età dichiarata nella fonte.
- Allegra: 15 gennaio 2003, età ~21, combacia con l'età dichiarata nella fonte.
- **Luisa**: nessuna Start Position esistente. Inventata secondo §9.6 (data varia, non 1° del mese): 11 novembre 1996, età 27 come da fonte.

## Verifica post-reload
Ricaricata la pagina, ri-autenticato, rifetch di tutti e sei: zero occorrenze di em-dash/`{{user}}`/`{{char}}`/markdown grassetto su tutti i campi, 5 outfit con Default impostato su ciascuno, 5 Dialogue Examples ciascuno, `final_instructions` con la disciplina di formato presente ovunque, `is_global` true, birthdate = start_timeline_position su tutti e sei.

## Nota di qualità emersa
Jake Thompson e Warg sono i primi due casi trovati in questa sessione di card con `long_summary` scritto in italiano mentre il resto del World (90+ schede) è in inglese. Probabile residuo di una lavorazione precedente alla convenzione di lingua inglese per il corpo dei testi del World. Tradotti entrambi in questo passaggio; vale la pena, se emergono altri casi simili durante lavorazioni future, controllare la lingua del `long_summary` come parte della verifica pipeline, non solo la sua presenza.
