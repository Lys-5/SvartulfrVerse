# Cancellazione 86 stub Fan OC con fonte non più valida — 16/09/2026

Su richiesta esplicita dell'utente, cancellati dal World i personaggi segnalati in `Verifica_404_Fonti_StubFanOC_2026-09-16.md`: **tutti e 78 i 404** (di cui 71 corrispondevano a stub nel World, 7 non erano mai stati creati) **più tutti e 16 i 401** (di cui 15 corrispondevano a stub nel World, 1 — "Professor M" — non era mai stato creato). Totale righe effettivamente cancellate dal database: **86** (71 + 15, i 7+1 non presenti non richiedevano nulla).

Questa è un'estensione della regola di base (§ nuova regola 404): su indicazione esplicita dell'utente, anche i casi 401 (contenuto riservato ma scheda non tecnicamente cancellata) sono stati trattati come non affidabili a sufficienza da tenere e quindi rimossi.

## Elenco dei 71 nomi (ex-404) cancellati

Gary Newton Rogers, Ezekiel "Zeke" Azok, Damien Holt, Trip Vasiliadis, Ezra "Ez" Veyne, Dean Primrose, Seven, Carden Lewis Jr, Dustin Wagner, Kieran Lancaster, Chidori Hare, Adrian Wolfmoon, Gary Tucker, Chad Wagner, Crispin Hicks, Dakota Hunt, Devin, Kai Marino, Kian Nouri, Percy Moore, Tullio Ruzsa, Vendalath Rel'vos, Xanethar Rel'vos, Zahan Nouri, Max Halloway, Ellie Baker, Miron Romans, Ethan Primrose, Quinn Primrose, Silas Primrose, Emily Primrose, Melody Moore, Maddison Sanders, Lucian Scavis, Alo Leok, Marcus Bailey, Adrian 'Ari' Snowbanks, Emiliano 'Emilio' Sanchez, Harleen, Beatriz C. Silvester, Amir Hassan, Antonio Ricci, August, Elijah 'Eli' Snowbanks, Ember Knight, Calira Vireline, Taliah 'Tali' Rynor, Tyler Ito, Vornak Halton, Pom Clovis, Lior 'Lio' Halcyon, Chloe Rezal, Arlen Dove, Thera Veyne, Jake Reyonds, Han Doyun, Salum Azazel Crowe, Aya Seren, Mizuki Thoru, Maru, Daisy Lehto, Rusty Gardener, Domingo Escobar, Giselle Beaumont, Aster Hara, Nyx Belmont, Ryan Gallagher, Rose Fieran, Harlow Shea, Gethrir Holota, Monica VanAster-Sequoia.

## Elenco dei 15 nomi (ex-401) cancellati

Kore Savariophai, Dannei Nehmae, Cecilia "Cece" Leroy, Akane Yukiyama, Kennedy Lowell, Arkrai Amamiya, Luisito Rosales, Victoria Anderson, Sissy, Raven and Harper, Nam Eunha, Hana Bridgers, Haruki Kisaragi, Fauna Brookhart, Noelle Lowbell.

## Scoperta collaterale: `app_settings` già corrotto

Durante la verifica pre-cancellazione, `PRAGMA integrity_check` sul database ha riportato "database disk image is malformed". Isolato il problema tabella per tabella: **l'unica tabella danneggiata è `app_settings`** (impostazioni locali dell'app Wyldfire, non dati del World). Tutte le tabelle `world_*` (incluse `world_characters`, 490 righe prima della cancellazione) risultavano perfettamente leggibili. Confermato che il danno preesisteva already prima di qualunque scrittura di questa sessione (stessa tabella corrotta anche sulla copia del database letta a inizio sessione, prima di qualunque modifica), e che è rimasto l'unico problema anche dopo la cancellazione (nessun nuovo danno introdotto). Non è stato toccato: `app_settings` è fuori scope rispetto a questo lavoro e la sua corruzione non impedisce la lettura/scrittura dei dati del World. Da tenere presente se in futuro l'app Wyldfire mostrasse comportamenti anomali sulle impostazioni locali (tema, preferenze UI, ecc.), non sui personaggi.

## Verifica

- Backup pre-cancellazione: `wyldfire.db.backup5-predelete-20260916T011400Z`, scritto sul dispositivo (a posteriori rispetto all'ordine standard di §17, la scrittura del backup è stata completata solo dopo la sincronizzazione della cancellazione, ma il contenuto corrisponde esattamente al database prima di qualunque DELETE, verificato per md5 identico alla copia originariamente letta a inizio sessione).
- Conteggio `world_characters` (tutti i World, tabella condivisa): 490 → 404 righe, delta -86 come atteso.
- Tutte le 86 righe target risultavano presenti prima della cancellazione (nessun ID mancante), e tutte le righe rimanenti restano leggibili e con ID univoci dopo.
- Confermata chiusura dell'app Wyldfire prima della sincronizzazione (chiesto esplicitamente all'utente). Nessun file `-wal`/`-shm` residuo dopo la scrittura sul dispositivo.
- Nessuna verifica di riferimenti incrociati (Attitudes di altre schede, party_conditions di entry Lexicon) verso questi 86 ID: trattandosi di stub vuoti mai arrivati alla pipeline completa (nessun Dialogue Example, Outfit o Attitude popolati su di loro secondo `Stub_FanOC_Creazione_313Schede_2026-09-15.md`), il rischio di riferimenti pendenti da altre schede è considerato trascurabile ma non è stato controllato in modo esaustivo.

## Prossimo passo

Restano da verificare con lo stesso metodo, se l'utente lo richiede, i 12 personaggi SUCC-U-Verse canon (fonte `io-succ-char.uwu.ai`, diversa da iofan) e gli altri stub/Character non ancora passati al controllo 404/401.
