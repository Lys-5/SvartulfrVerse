# Bailey Rogers — Scheda completata

Costruita dal materiale sorgente fornito dall'utente (Scenario SUCC/CUMS, blocco Personality raw `<bailey_rogers>`, First Message). La scheda era ferma da una sessione precedente allo stato di import grezzo (`long_summary` ancora nel blocco `<bailey_rogers>` originale), con 5 Dialogue Examples già aggiunti in un batch precedente basati su quello stesso testo grezzo, e RPG Stats/Outfit/Default Outfit/due Attitudes (Alyssa, Jasper) e una terza (Jared Thompson) già presenti da lavorazione ancora precedente. Questo passaggio ha completato la pipeline standard.

**Confermato dall'utente**: Dominic Rogers (lavorato in questa sessione) è il padre di Bailey. Collegamento aggiunto come Attitude.

## Campi riscritti

- **`long_summary`**: riscritto integralmente in JED+ (blocco attributi + BACKSTORY + FAMILY & PACK + VOICE & BEHAVIOR + sezione tematica finale "THE HUNGER HE WON'T TAKE" sul suo rifiuto di nutrirsi senza consenso esplicito, il tratto che lo definisce più di ogni altro). Include: corpo tozzo e basso per essere un incubo, corna e coda, l'accento southern, il rapporto col padre Dominic (dalle chiamate dopo le partite), la madre Lara morta quando aveva 14 anni e il peluche Lucibaa, i compagni di squadra Jared Thompson e Santiago "Tank" Herrera, Coach Dullahan, lo split psicologico tra sicurezza fisica/accademica e insicurezza romantica.
- **`summary`**: riscritto come blocco PList compatto di soli tratti.
- **`display_description`**: aggiunta, prima era vuota.
- **`final_instructions`** (post_history_instructions): aggiunta la riga di disciplina di formattazione standard, prima era vuota.
- **`birthdate` e `start_timeline_position`**: mancavano del tutto (campo assente dall'oggetto, non solo vuoto). Calcolati dal World Clock: 8 ottobre 2002 (10298064 ore dall'epoca), scelto per fargli avere 21 anni all'world_age corrente (5 aprile 2024) con una data varia, non il solito 1° gennaio.
- **`rpg_stats.species_id`**: `_WFa39xaHxVhrmy1a9AbgT` (Demons, categoria che copre gli incubi in questo World).
- **`rpg_stats.occupation_id`**: `_gAdjMK383yRrYBHLLE9Qf` (Student).
- **Attitudes**: da 3 a 6. Aggiunte: Dominic Rogers (padre, `wary`, intensity 70, rapporto teso ma con l'affetto residuo che lo spinge ancora a cercare la sua approvazione), Santiago Herrera (compagno di squadra, `friend`, intensity 45), Coach Dullahan (`acknowledged`, intensity 40, intimidatorio ma un buon motivatore nonostante sembri non capire il football). Le tre preesistenti (Alyssa, Jasper entrambe `stranger`, Jared Thompson `friend`) lasciate intatte.

## `{{user}}` purgato

La fonte grezza conteneva una riga "Towards {{user}}: 'You're always really cool to talk to… I mean it.'" Non generalizzata: rimossa integralmente in fase di riscrittura, perché generica e non necessaria al personaggio (già coperto dai tratti "secret romantic" e "touch-starved" scritti in forma neutra). Verificato dopo reload: zero occorrenze di `{{user}}` su tutti i campi.

## Non toccato in questo passaggio

- **Dialogue Examples**: i 5 già scritti in un batch precedente restano validi, letti dallo stesso identico testo sorgente grezzo appena riscritto in JED+. Nessuna contraddizione rilevata, non riscritti.
- **Outfit e Default Outfit**: già presenti (Game Day, Campus, Home Clothes, Frat Party, Formal) da lavorazione precedente, non toccati.
- **First Message fornito dall'utente** (la scena dello spogliatoio con la chiamata del padre): non esiste un campo `first_mes` esposto su questa risorsa Character in questo World via API (verificato elencando le chiavi dell'oggetto). Il materiale è stato comunque usato come fonte per BACKSTORY/VOICE & BEHAVIOR (la vergogna del corpo, la tensione col padre, "la buzz" cioè l'impulso che resiste). Se il campo First Message esiste altrove nell'interfaccia (per esempio legato a uno Scenario separato), va gestito manualmente dall'interfaccia o segnalato per una scrittura successiva.

## Scoperta collaterale: vocabolario reale dei Tier delle Attitudes

Le istruzioni di progetto (§16) elencano una ladder aspirazionale (Blood Enemy, Enemy, Rival, Distrusted, Wary, Unknown Scent, Acknowledged, Trusted, Pack, Pack-bonded, Beloved) che **non corrisponde ai valori realmente salvati nell'API**. Ho enumerato tutti i valori `tier` effettivamente in uso su tutte le schede del World e il set reale è:

`acknowledged, acquaintance, best_friend, close_friend, despised, disliked, enemy, friend, hated, rival, romantic_interest, stranger, wary`

Tredici valori, snake_case, concettualmente sovrapponibili alla ladder documentata ma con etichette diverse (niente "Blood Enemy" o "Pack-bonded", ma "hated", "despised", "best_friend", "romantic_interest"). Non ho corretto le istruzioni di progetto né toccato le attitudes di altre schede: segnalo qui la scoperta perché **§16 vieta esplicitamente di alterare la ladder senza rifare tutte le attitudes**, e prima di qualunque intervento sistemico su questo va deciso con l'utente se aggiornare la documentazione (probabile) o se la ladder testuale del progetto è solo una descrizione approssimativa a uso interno mai stata la fonte di verità dei valori salvati.

## Verifica

Verificato dopo reload completo: `long_summary` 4544 caratteri in JED+, `summary` 763 caratteri PList, `display_description` e `final_instructions` popolati, `birthdate`/`start_timeline_position` = 10298064, `species_id`/`occupation_id` impostati, 6 attitudes, 5 speech_examples, zero em-dash/`{{user}}`/grassetto su tutti i campi controllati, Global Character ON, Default Outfit impostato.
