# Archive Recoveries — Second Brain Staging

Questo archivio raccoglie le schede e le note di recupero generate automaticamente dal modulo di **Archive Mining** (`scripts/archive_mining_engine.py` / `scripts/daily_omnisync_archive_mining.py`).

## Obiettivo
Analizzare a blocchi quotidiani (2-3 file al giorno) i documenti storici custoditi in `ARCHIVIO/`:
- `03_Claude_Docs_and_Memories/` (memorie narrative, dialoghi e sfumature di relazioni)
- `02_Drive_and_Raw_Sources/` (testi sorgente primari da Google Drive)
- `01_Drafts/` (bozze e schede storiche)
- `cards_legacy/` (vecchie versioni di character card)

## Workflow di Promozione
1. **Staging:** Le informazioni scoperte vengono estratte e salvate in questo direttorio come file `.md` con timestamp e metadati frontmatter.
2. **Revisione:** L'utente o gli agenti possono consultare le note di staging senza alterare direttamente i file canonici in `FINAL/`.
3. **Promozione a Canone:** I fatti confermati e non in contraddizione con la timeline e le regole del repository vengono integrati nei 6 Lorebook Standalone o nelle schede ufficiali.
