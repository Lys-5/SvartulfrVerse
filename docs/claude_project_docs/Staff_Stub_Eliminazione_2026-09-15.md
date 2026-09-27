# Audit Favorites/Following e eliminazione 15 stub Staff senza fonte — 2026-09-15

## 1. Audit favorites tab (verifica personaggi esistenti)

Controllo della tab Favorites di janitorai.com (54 schede su 2 pagine) incrociando i nomi con il database locale del World, per cercare informazioni nuove su personaggi già trasferiti.

**Esito**: la maggior parte dei personaggi canon presenti tra i favorites erano già Character esistenti nel World (Dante, Zero, Jean-Luc Virtuoso, Dullahan, Bailey Rogers, Finnegan Novak, Iordan R. Vess, Romeo "Gray" Dean, Stanley Davies Jr./Sr., Hank Thompson, Jared Thompson, Professor Loewe, Abel Vilas, Emil, Arturo Cardona, Neon Purr, Bram Beaumont/Lennox McKay, Cassian Aralas, Brak Ironfist, Zeera).

Controllo approfondito su **Jared Thompson** (fonte con più varianti disponibili, @veseii "Halloween" e @Iorveths "gloryhole"): espanso il blocco Personality completo del lorebook SUCC-U-VERSE sulla variante @veseii e confrontato riga per riga con la scheda World. Risultato: la scheda è già stata costruita esattamente da questa fonte, tutti i dettagli chiave (rapporto con Stan Davies Jr. e motivo della frattura, famiglia, paure, il tratto della coda) sono già presenti e fedeli. Nessuna informazione mancante di rilievo trovata.

Punto già noto che è tornato visibile: **Brak Ironfist** ha tre bot diversi tra i favorites (base, "alt scenario", "100th Bot Special"). Come già documentato in precedenza, per questo personaggio il contenuto anatomico/kink della fonte era stato scartato del tutto invece che spostato in un Intimacy Profile separato: incoerenza minore nota, non corretta retroattivamente, segnalata di nuovo qui per completezza ma nessuna azione presa.

## 2. Ricerca fonti per i 15 stub "Staff" mancanti

Elenco stub interessati (tutti con `long_summary` vuoto/placeholder, `outfits` e `speech_examples` a `[]`): Professor Tipton, Rania Vega, Adonis Ness, Professor Vulkan, Professor Paul, David Forrester, Nicky Thompson, Lucie Kennedy, Alaina Taylor, Kolvin Loughlin, Mowy "Moss" Movoud, Marcus Jacobs, Veronika Arzan, Eros Cupid, Professor Blackwood.

**Metodo di ricerca, in ordine**:
1. `janitorai.com/search?following=true&search=<nome>` — nessun risultato per nessuno dei 15 nomi.
2. Combinazione ricerca testuale + tag canon (`custom_tags=succ`, `custom_tags=modernfantasy`) — nessun risultato.
3. Su richiesta esplicita, controllo con i tag generici `#urbanfantasy` (459 schede) e `#underworld` (151 schede): confermato che sono tag di community generici, usati da decine di creator scollegati da questo progetto (magical girl bot, mafia/yakuza, mitologia greca, ecc.), non specifici del canon SUCC/Blackwood. Nessun match utile per i 15 nomi.
4. Controllati anche i tag realmente usati dal progetto per l'incrocio Underworld/Modfan (`#thesinners`, `#modfanunderworld`): coprono solo Dr. Arthur Sinclair, Zero, Jean-Luc Virtuoso, Dante (Sinners) e la famiglia Ballantine (Rory, Danny Boone, Harper Aries), tutti già presenti nel World. Nessuno dei 15 nomi mancanti.
5. **Dopo che l'utente ha aggiunto il follow ai collab del multiverso**, ripetuta la ricerca `following=true&search=<nome>` su tutti e 15 i nomi: ancora nessun risultato per nessuno.

**Conclusione**: nessuno dei 15 stub corrisponde a un bot pubblico attualmente reperibile su janitorai.com. Secondo l'utente, alcune fonti sono state cancellate nel tempo dai rispettivi autori.

## 3. Eliminazione dei 15 stub senza fonte

Su indicazione esplicita dell'utente ("se non trovi nulla elimina la scheda"), le 15 schede sono state rimosse dal database locale Wyldfire (§17), non semplicemente lasciate vuote.

**Controllo di sicurezza pre-eliminazione** (programmatico, dentro lo script di scrittura): per ognuno dei 15 id, verificato che `display_name` corrispondesse esattamente al nome atteso, che appartenesse al World corretto (`6cfuc64QBr1Flf9nKndFy`), e che `outfits`/`speech_examples` fossero effettivamente vuoti (nessun contenuto lavorato da perdere). Il controllo è passato su tutti e 15 prima di procedere con la `DELETE`.

| Personaggio eliminato | Row ID |
|---|---|
| Professor Tipton | `nOAKReih10` |
| Rania Vega | `xmzXJI1JQ4` |
| Adonis Ness | `KYBOZCz-Wk` |
| Professor Vulkan | `Dhwbj39E_j` |
| Professor Paul | `IxP79FJSwX` |
| David Forrester | `qmjY3fCET6` |
| Nicky Thompson | `_qFFG-zZ1t` |
| Lucie Kennedy | `TGCFwd5x9T` |
| Alaina Taylor | `HtA2n72fwY` |
| Kolvin Loughlin | `Eaujsif3NX` |
| Mowy "Moss" Movoud | `KBfEhTqp1U` |
| Marcus Jacobs | `EZc9vQ1QW9` |
| Veronika Arzan | `OA_ZOA2H0V` |
| Eros Cupid | `a6L-nMr8vr` |
| Professor Blackwood | `7uoDJYvwLU` |

### Workflow tecnico (§17)

1. Durante il lavoro il database ha smesso temporaneamente di rispondere (`disk I/O error` su ogni apertura, anche in sola lettura), sintomo tipico di un lock tenuto da un altro processo. Sospetto confermato dall'utente: Wyldfire desktop era stata riaperta nel frattempo. Nessuna scrittura tentata finché l'utente non ha confermato la richiusura dell'app; verificato con una query di sola lettura che il database fosse di nuovo accessibile prima di procedere.
2. Backup numerato `wyldfire.db.backup4-20260915T170613Z` (accanto ai backup1-3 di questa sessione e al backup pre-migrazione).
3. Scrittura tramite script Python/sqlite3 (`_claude_delete_15_staff_stubs.py`), con controllo di sicurezza sui 15 id prima della `DELETE` (vedi sopra).
4. `PRAGMA integrity_check` prima e dopo: `ok` in entrambi i casi.
5. Verifica programmatica post-scrittura: tutti e 15 gli id confermati assenti dalla tabella dopo il commit.
6. `PRAGMA wal_checkpoint(TRUNCATE)` eseguito: `(0, 0, 0)`, nessuna transazione pendente. File `-wal` assente dopo il checkpoint, `-shm` presente a 32768 byte (normale in modalità WAL).
7. Script temporaneo rimosso dal dispositivo dopo l'uso.

Come per tutti i batch precedenti di questa sessione, il sito Wyvern non riflette ancora questa modifica: serve una pubblicazione esplicita (*Publish to Wyvern*) o il sync delle chat da parte tua.
