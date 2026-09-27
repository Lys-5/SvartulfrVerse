# Regola 12 — Lavoro in Locale su Database SQLite Wyldfire (Sospeso)

## 1. Stato Attuale: Procedura Sospesa dal 22 Settembre

- **Modalità Disattivata di Default:** A partire dal 22/09, il lavoro diretto sul database SQLite locale dell'applicazione desktop Wyldfire non costituisce più il flusso di lavoro predefinito.
- **Motivo della Sospensione:** La sincronizzazione asincrona e la successiva pubblicazione (*Publish to Wyvern*) dal client desktop al sito remoto ha storicamente causato la rigenerazione incontrollata degli ID dei Character, provocando l'orfanezza silenziosa delle entry Lexicon collegate (`party_conditions`, Intimacy Profiles, Attached Character).
- **Fonte di Verità:** Il sito ufficiale `app.wyvern.chat` rimane la sola e unica fonte di verità operativa (vedi Regola 11).

---

## 2. Protocollo di Emergenza (In Caso di Esplicita Riattivazione)

Se e solo se l'utente richiede espressamente di operare sul database locale SQLite di Wyldfire per specifiche elaborazioni massive, attenersi in modo scrupoloso a questo ciclo di sicurezza:

1. **Localizzazione del Database:** Il file SQLite di lavoro risiede sul dispositivo dell'utente al percorso:
   `C:\Users\<utente>\AppData\Roaming\com.wyvern.wyldfire\wyldfire.db`
   Verificare e confermare a inizio sessione `world_id` e `creator_id`.
2. **Backup Incrementale Obbligatorio:** Prima di qualsiasi istruzione `INSERT`, `UPDATE` o `DELETE`, generare una copia numerata e timestampata del file (es. `wyldfire.db.backupN-<timestamp>`). Non toccare mai il database attivo senza backup preventivo verificato.
3. **Automazione via Script Python:** Operare solo tramite script controllati con la libreria nativa `sqlite3`. Vietato inserire o modificare record manualmente tramite interfacce generiche per operazioni in blocco.
4. **Verifica Post-Scrittura:**
   - Eseguire il controllo di integrità: `PRAGMA integrity_check;`.
   - Eseguire query mirate di conteggio e confronto per certificare il numero esatto di righe modificate rispetto al piano.
5. **Chiusura Tassativa di Wyldfire:** Prima di effettuare trasferimenti o scritture sul file, richiedere conferma esplicita che l'applicazione desktop Wyldfire sia completamente chiusa sul sistema host per evitare corruzioni da lock concorrenti.
6. **Bonifica File Temporanei `-wal` e `-shm`:** Assicurarsi che non rimangano file journaling (`wyldfire.db-wal`, `wyldfire.db-shm`) aperti accanto al file database principale al termine della procedura.
7. **Documentazione nel Project:** Registrare dettagliatamente l'intervento nel Project solo a transazione completata, verificata e chiusa.
8. **Audit Post-Pubblicazione:** Una volta che l'utente ha eseguito il comando *Publish to Wyvern*, lanciare tempestivamente una verifica via API delle entry Lexicon per rilevare ed eliminare eventuali orfani generati da ID riassegnati.
