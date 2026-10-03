# Gerarchia cartelle sorgente (device "omen")

Nota operativa confermata dall'utente il 27/08/2026.

## Cartelle collegate finora
- `D:\SvartulfrVerse` — cartella principale del progetto.
  - `D:\SvartulfrVerse\Wyvern` — **file definitivi**: qui vivono le card/world/lorebook effettivamente usate/da usare su Wyvern (characters/*, lorebooks/*, lexicon/*, ecc.). Qui vanno fatte le modifiche quando si "rende definitivo" qualcosa.
  - `D:\SvartulfrVerse\Drafts` (incl. `Character_Cards_V1`, `Core_Docs` con Master_Design.md e World_Seed.md) — **archivio di consultazione primario**: materiale di riferimento ricco (profili psicologici, relationship map, ecc.) ma NON va corretto/editato per allinearlo al definitivo; si consulta e si sintetizza, non si modifica senza autorizzazione esplicita.
- `D:\SillyTavern` — contiene card/persona/lorebook di una piattaforma precedente (es. Alyssa_Card.json), talvolta più aggiornate del Drafts su SvartulfrVerse. Trattarla come fonte di consultazione anch'essa, da verificare caso per caso contro Wyvern.
- `C:\Users\mande\Documents\Alice\2_PROGETTI\AU`
- `C:\Users\mande\Documents\Alice\3_GDR\3_SISTEMI\Sperimentali\Amarantia`
- `C:\Users\mande\Documents\Alice\3_GDR\3_SISTEMI\Sperimentali\Project Oniroscopio`

Queste ultime tre sono tutte draft e materiale accumulato negli anni per il progetto: **archivio di consultazione secondario**.

## Ordine di ricerca quando serve un'informazione/dettaglio
1. `D:\SvartulfrVerse\Wyvern` (definitivo, se esiste già una card/entry).
2. `D:\SvartulfrVerse\Drafts` (+ `D:\SillyTavern` se pertinente) — archivio di consultazione primario.
3. Solo se non si trova nulla nei punti 1-2: le cartelle secondarie (AU, Amarantia, Project Oniroscopio).

Nessuna di queste cartelle di archivio va corretta/editata per "pulizia" senza autorizzazione esplicita dell'utente (vale la regola 9.3 del workflow: discrepanze si segnalano, non si correggono di iniziativa). Le uniche modifiche dirette ammesse di default sono sui file dentro `Wyvern`, quando si sta effettivamente finalizzando una card.
