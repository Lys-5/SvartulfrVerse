# Lexicon — Indice Folder (mirror 1:1 Wyvern)

Generato il 30/08/2026 dall'export nativo di Wyvern ("Export as Markdown", World: Svartúlfr | Urban).
**Aggiornato il 30/08/2026 (notte)** dopo la sessione di allineamento piattaforma/locale: 3 fix Global
Entry, 6 nuove Lexicon entries "interazioni digitali/social" create, 4 entry spostate manualmente da Lys
da Uncategorized a Chars Details, e un aggiornamento contenuto/keyword sull'entry Jasper (nome d'arte
"DJ Frequency" + sezione SoundCloud/Spotify).

## Come è organizzato

Ogni file di questa cartella corrisponde a un folder Lexicon su Wyvern e contiene il contenuto completo
(metadata + testo) di ogni entry in quel folder, così come esportato/osservato da Wyvern.

| File | Folder Wyvern | N. entries |
|---|---|---|
| UNCATEGORIZED.md | Uncategorized | 6 |
| CHARS_DETAILS.md | Chars Details | 15 |
| UNDERWORLD_CONCEPT.md | Underworld Concept | 4 |
| ITEM.md | Item | 1 |
| SPECIES.md | Species | 4 |
| HISTORY.md | History | 5 |
| JOB_AND_BUSINESS.md | Job & Business | 1 |
| SUCC_CONCEPT.md | SUCC Concept | 9 |
| **Totale** | | **45** |

## Nota importante sulla ricostruzione dei folder

L'export nativo "Export as Markdown" di Wyvern **non include il campo folder/categoria** per le entry
del Lexicon. L'assegnazione di ogni entry al proprio folder qui sopra è ricostruita incrociando l'elenco
entry con l'osservazione diretta della UI Lexicon (conteggi per folder, nomi visibili), fatta in sessione.
I conteggi tornano esattamente (6+15+4+1+4+5+1+9 = 45).

## Modifiche eseguite in questa sessione (30/08/2026, notte)

### 1. Fix Global Entry (rischio attivazione mai, vedi `claude/Lexicon_Categorization_Plan.md`)
Tre entry avevano Global Entry: No senza collegamento esplicito a un Environment — corrette a
Global Entry: Yes, confermate salvate sulla piattaforma:
- "Il Viaggio di Wulfnic in America" (HISTORY.md, #10)
- "La Guerra di Fenris e l'Esilio dei Firstborn" (HISTORY.md, #11)
- "Douglas Commercial Coalition (DCC)" (JOB_AND_BUSINESS.md, #12)

### 2. 6 nuove Lexicon entries create (contenuto pronto in `claude/Pending_Lexicon_Drafts_Digital_Social.md`)
Tutte create in Uncategorized (non ancora smistate in un folder dedicato), vedi UNCATEGORIZED.md #40-45:
Digital Interactions Chase/Jasper/Iordan (Memory + Attached Character), SUCCbook/social campus,
Pack-Family group chat, Texting & Writing Styles (Concept, Global Entry ON).

**Bug scoperto in sessione**: il salvataggio di una nuova Lexicon entry subito dopo un'altra può
sovrascrivere la precedente invece di crearne una nuova (stesso bug già noto per i Character). La
entry "Digital Interactions — Chase Anderson" è stata persa una volta così e ricreata da zero.
Contromisura applicata con successo per le entry successive: reload forzato della pagina World prima
di ogni click su "New Lexicon", verifica dell'incremento del contatore Lexicon e del testo del toast
("registered" vs "updated") dopo ogni salvataggio.

### 3. Aggiornamento entry Jasper (Digital Interactions — Jasper Douglas Bloodmoon, #41)
Su richiesta di Lys durante la sessione: aggiunta sezione "SoundCloud / Spotify Releases" (per
pubblicazioni ufficiali distinte dai clip social) e introdotto il nome d'arte **DJ Frequency**
(usato nei crediti dei brani, flyer e social pubblici; "Jasper" resta riservato alla cerchia stretta
nei DM/group chat). Nuove keyword aggiunte: SoundCloud, Spotify, DJ Frequency.

### 4. Spostamento manuale 4 entry Uncategorized → Chars Details (fatto da Lys)
Family — Chase Anderson (Parents), Intimacy Profile — Chase Anderson, Intimacy Profile — Stanley
Davies Jr., Intimacy Profile — Bailey Rogers: erano bloccate in Uncategorized per un bug del menu
"Move items…"; Lys le ha spostate manualmente in Chars Details (ora 15 entry, vedi CHARS_DETAILS.md).

## Anomalia investigata: "# [Jasper]" / "# [Noah]" nell'export

Le due righe `# [Jasper]` e `# [Noah]` trovate come falsi "top-level heading" durante il primo grep
strutturale dell'export **non sono un errore o un duplicato**: sono la prima riga del campo "Long
Summary" delle character card di Jasper e Noah (World Characters, non Lexicon), che nel loro contenuto
JED+ iniziano con un heading Markdown `# [Nome]` come da convenzione del progetto. Nessuna azione
necessaria.

## Prossimi passi

- Estendere lo stesso mirror 1:1 a Characters (85), Environments (12), Locations (79), Scenarios (1)
  quando Lys darà il via libera (questo pass resta scoped a solo Lexicon).
- (Opzionale, task a parte) Position field hygiene check e conversione Solarton/Campus Locations in
  Location native, vedi `claude/Lexicon_Categorization_Plan.md` §3-4.
