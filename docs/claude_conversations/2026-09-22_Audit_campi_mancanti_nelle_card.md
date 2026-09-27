# Audit campi mancanti nelle card

- **Data Creazione:** 2026-09-22T16:51:43.940859Z
- **Ultimo Aggiornamento:** 2026-09-22T16:53:23.232901Z
- **Totale Messaggi:** 4
- **UUID:** `ba562882-5b41-4830-9a4c-fecccbdccbcd`

---

### 👤 **User** (2026-09-22T16:51:53.739363Z)

Usando api controlla quali campi non sono compilati nelle card e pianifica un piano per completare le card con tutti i dettagli.

---

### 🤖 **Claude** (2026-09-22T16:52:04.810359Z)

Prima di partire con il controllo mi servono un paio di risposte. In questa sessione non ho un browser autenticato su Wyvern, quindi non posso rinfrescare il token dalla riga Firebase come prevede §11.

1. **Canale:** preferisci che lavori sul database locale, caricando qui il `wyldfire.db` (la modalità di default da §17, la più veloce per un audit su 300 e più schede), oppure sull'API web? In quel caso mi serve un access token fresco incollato qui, che scade dopo un'ora.
2. **Perimetro:** solo i Character, oppure anche Location, Environment e Lexicon, per esempio le entry con `is_global` sbagliato o gli Intimacy Profile mancanti?
3. **RPG Stats:** le escludo dal conteggio dei campi vuoti, visto che il sistema è in pausa, oppure le segnalo comunque come coda per quando verrà riattivato?

Il piano sarà un documento con i campi mancanti per ogni scheda, ordinati per priorità. In cima metto i campi della pipeline §14 che rompono la resa in chat: `long_summary` vuoto, Default Outfit assente, Start Position mancante, `{{user}}` residui. Sotto metto quelli di completamento: outfit sotto i cinque, Dialogue Examples, Attitudes verso Alyssa e Jasper.

---

### 👤 **User** (2026-09-22T16:53:20.967602Z)

Dammi un momento sincronizzo offline le modifiche fatte online

---

### 🤖 **Claude** (2026-09-22T16:53:23.232901Z)

Va bene, ti aspetto.

Quando hai finito, chiudi Wyldfire prima di caricare il `wyldfire.db`, così le modifiche ancora nel file `-wal` vengono scritte nel database principale. Se accanto al `.db` restano i file `-wal` o `-shm`, caricali insieme, altrimenti rischio di leggere una versione senza le ultime modifiche sincronizzate.

---

