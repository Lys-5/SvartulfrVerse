# Completamento cluster S.R.F. Alpha Squad (Los Angeles) — 2026-09-14

Quattro dei 21 personaggi della cartella "Los Angeles" appartenevano a un cluster narrativo già scritto a un livello molto alto dall'autore precedente: **Miles Airhardt** (Lieutenant, Alpha 1-1), **Rafael Callaway** (Sergeant, Alpha 1-2), **Kade Leavis** (Private, Alpha 1-3), tre licantropi della Supernatural Reserve Forces che formano la squadra "Alpha", più **Graham Purcell** (Major S.R.F., ex commilitone di Kaladin Nargathon, collegamento diretto con Villa Douglas).

## Stato di partenza

`long_summary` e `summary` erano già completi, in inglese, di ottima qualità narrativa, e **già conformi a §13**: il testo si riferisce sempre a "the handler" o "whoever is holding this post" invece di nominare un personaggio specifico del World, esattamente il pattern richiesto per evitare di legare `{{user}}` a un\'unica identità. Nessuna riscrittura di contenuto necessaria.

Mancavano solo i passi meccanici della pipeline: `display_description`, `final_instructions`, `speech_examples` (0 su tutti e 4), un quinto outfit per Rafael e Kade (ne avevano 4), tutti e 5 gli outfit per Graham Purcell (ne aveva 0), e le `attitudes` mancanti per Rafael/Kade/Graham (Miles le aveva già tutte e 4: Rafael e Kade come `close_friend`, Alyssa e Jasper come `stranger`).

## Errore commesso e corretto: PUT su array parziale

Nel completare Rafael, il primo tentativo ha inviato `outfits: [nuovo outfit]` pensando che il PUT parziale si applicasse anche dentro l'array. **Non è così: un array è un campo di primo livello e viene sostituito per intero**, non fuso elemento per elemento. Questo ha cancellato i 4 outfit esistenti di Rafael, lasciandone solo 1. Individuato subito con un GET di verifica e corretto rimandando l'array completo (i 4 originali più il nuovo). Per Kade è stato fatto correttamente al primo tentativo, includendo sempre l'array intero. **Nota per il futuro**: ogni PUT che tocca un campo array (outfits, speech_examples, attitudes) deve sempre contenere l'intero array desiderato, mai solo la parte nuova.

## Attitudes assegnate

- Rafael → Miles (`close_friend`, 75), Kade (`close_friend`, 70), Alyssa/Jasper (`stranger`, 15).
- Kade → Miles (`disliked`, 20, odio specifico legato al sospetto di Miles sull'incidente che gli ha aperto il posto in squadra), Rafael (`close_friend`, 65), Alyssa/Jasper (`stranger`, 15).
- Graham Purcell → Kaladin Nargathon (`close_friend`, 70, ex commilitone S.R.F.), Alyssa/Jasper (`stranger`, 15, il suo mondo è la S.R.F., non Blackwood o Solarton).
- Miles: già presenti (Rafael/Kade `close_friend`, Alyssa/Jasper `stranger`), non toccate.

## Outfit aggiunti

Rafael: quinto outfit "After" (post demolizione, la sua versione della calma dopo l'azione). Kade: quinto outfit "Reprimanded" (in punizione, faccia vuota). Graham: tutti e 5 da zero (Duty Uniform, Field Deployment, Off Duty, Meeting Kaladin, Full Berserker Shift).

## Verifica

GET diretto su tutti e 4 dopo reload completo: 5 outfit con default impostato, 5 speech example, final_instructions presente, display_description presente, attitudes coerenti, `CHECK()` pulito (zero em-dash, zero `{{user}}`, zero grassetto).

## Stato

4 dei 21 personaggi Los Angeles completati. Restano da lavorare: gli altri 17, per cui l'audit precedente (`Audit_Los_Angeles_2026-09-14.md`) ha già mappato il contenuto sorgente grezzo (import JanitorAI mai lavorato). Prossimo blocco naturale: il cluster DeVille/Ballantine (Alistair DeVille, Cato, Rory Ballantine, Sully Jones, Danny Boone, Harper Aries), poi il sindacato rivale "The Sinners" (Jean-Luc Virtuoso, Alicia Virtuoso, Arthur, Kevin, Zero, Siobhan, Roxie, Dante), poi gli indipendenti (Everett Rottmore, Damien Bishop, Vasile Ionescu).
