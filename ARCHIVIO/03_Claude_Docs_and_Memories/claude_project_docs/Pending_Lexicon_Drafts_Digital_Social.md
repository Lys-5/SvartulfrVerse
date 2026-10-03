STATO: TUTTE LE 6 ENTRY CREATE SU WYVERN — 30/08/2026 (notte)

Tutte le entry documentate in questo file sono state create con successo sulla piattaforma Wyvern live
(World: Svartúlfr | Urban) durante la sessione del 30/08/2026 notte, insieme ai 3 fix Global Entry
pendenti (Wulfnic viaggio, Guerra di Fenris, DCC — vedi `claude/Lexicon_Categorization_Plan.md`).
Il mirror locale `D:\SvartulfrVerse\Wyvern\lexicon\by_folder\` è stato aggiornato di conseguenza
(vedi 00_INDEX.md e UNCATEGORIZED.md in quella cartella).

## Checklist di creazione — TUTTE COMPLETATE

- [x] Entry 1 (Chase) — Memory + Attached Character: Chase Anderson. Nota: la prima creazione è stata
      accidentalmente sovrascritta da un bug (salvataggio "New Lexicon" immediatamente successivo che
      sovrascrive invece di creare), poi ricreata con successo dopo reload forzato della pagina.
- [x] Entry 2 (Jasper) — Memory + Attached Character: Jasper Douglas Bloodmoon. **Aggiornata una seconda
      volta in sessione** su richiesta di Lys: aggiunta sezione "SoundCloud / Spotify Releases" e
      introdotto il nome d'arte **DJ Frequency** (usato nei crediti brani/flyer/social pubblici,
      "Jasper" riservato alla cerchia stretta). Nuove keyword: SoundCloud, Spotify, DJ Frequency.
- [x] Entry 3 (Iordan) — Memory + Attached Character: Iordan R. Vess
- [x] Entry 4 (SUCCbook/social) — Concept, Global Entry ON
- [x] Entry 5 (Pack-Family) — Concept, Global Entry ON
- [x] Entry 6 (Texting Styles) — Concept, Global Entry ON

## Bug confermato in questa sessione: overwrite su "New Lexicon"

Salvare una nuova entry Lexicon subito dopo aver salvato la precedente può **sovrascrivere** quella
precedente invece di crearne una nuova (stesso bug già noto per la creazione di Character). Sintomo:
il toast dice "Data index entry updated successfully" invece di "...registered successfully", e il
contatore Lexicon nella sidebar non incrementa. Contromisura che ha funzionato in modo affidabile per
tutte le entry successive: reload forzato (`force: true`) della pagina World prima di ogni click su
"New Lexicon", e verifica dell'incremento del contatore + testo del toast dopo ogni salvataggio.

## Tecnica di selezione Entry Type / Attached Character confermata in sessione

Per i combobox Radix (Entry Type, Attached Character) nel form "New Lexicon": aprire il combobox,
premere ripetutamente la lettera iniziale dell'opzione desiderata (typeahead da tastiera) per ciclare
le opzioni, verificare via screenshot quale opzione è evidenziata, poi cliccare le coordinate esatte
di quell'opzione nello screenshot (NON un ref-based click, che in questo flusso ha selezionato più
volte l'opzione sbagliata). Premere "Enter" per confermare NON ha funzionato in modo affidabile in
questo flusso specifico.

Tutte le 6 entry sono ora vive su Wyvern, contenuto verificato via `get_page_text` dopo ogni salvataggio.
