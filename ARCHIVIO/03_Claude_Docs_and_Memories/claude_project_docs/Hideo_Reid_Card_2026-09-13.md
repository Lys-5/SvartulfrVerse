# Hideo Reid — Card completata (2026-09-13)

## Stato di partenza
Card esistente su Wyvern come stub minimo (`_1WCQ14AbLVDKXcCAqkaCc`): solo `display_name`, `display_description`/`summary`/`long_summary` placeholder che dicevano esplicitamente "not established", 2 Attitudes verso Alyssa/Jasper a `stranger`. Nessun outfit, nessun Dialogue Example, nessuna Start Position.

## Fonte
Materiale JanitorAI fornito dall'utente (`created by gunko 2026© on janitorai.com`): Hideo Reid, kitsune, professore di Chimica alla SUCC, scritto come sugar daddy di `{{user}}` con un blocco Intimacy esplicito e un first_mes costruito interamente sulla dinamica voto-in-cambio-di-favori.

## Applicazione §13 — caso più severo (staff, non pari)
A differenza di Venera Dolce (studentessa-studentessa), qui il personaggio è **staff con autorità su studenti**: il caso esplicitamente più severo di §13.2, "a maggior ragione quando è staff. Non attenuare: rimuovere."

Rimosso integralmente, non rilocato in una Intimacy Profile separata:
- L'intero arrangement sugar daddy/sugar baby e la sezione Relationships su `{{user}}`.
- Il blocco Intimacy esplicito (turn-ons, genitali, comportamento sessuale).
- Il first_mes originale, costruito sul voto basso di `{{user}}` come leva di ricatto emotivo/economico.

Non è stata creata una entry Lexicon Intimacy Profile per lui: il contenuto intimo della fonte era inscindibile dalla dinamica di potere staff/studente che va eliminata, non preservata altrove (stesso trattamento di Dullahan e Richard Loewe).

Aggiunta, secondo §13.4, una sezione tematica di chiusura **THE LINE** nel `long_summary` più una riga esplicita in coda a `final_instructions`: Hideo non ha eccezioni sulla non-relazione con studenti, qualunque sia la proposta. Il quinto Dialogue Example ("A Student Oversteps") mette in scena esattamente questo, chiudendo la porta invece di lasciarla socchiusa.

## Cosa è stato tenuto (non diretto a `{{user}}`)
Specie (Kitsune), nazionalità, età (56), aspetto fisico completo, backstory (vedovo, moglie Rosie morta di leucemia a 35 anni, carriera accademica, trasferimento alla SUCC), personalità, reputazione da professore rigido su RateMyProfessor, e le AI Guidelines sulla trasformazione in volpe a nove code.

## Discrepanza di fonte segnalata
L'altezza è data sia come "6'4"" sia come "187 cm" nello stesso documento: 6'4" corrisponde a circa 193 cm, non 187. Riportata come trovata nel JED+ (§9), non corretta. **Nota tecnica:** il campo `creator_notes` usato in altre schede del progetto non esiste nello schema Character di questo World (verificato via GET, elenco completo delle chiavi non lo contiene) — la discrepanza e la motivazione della purga restano quindi documentate solo qui nel Project, non nella card stessa.

## Campi scritti
- `long_summary` (JED+: NAME block, BACKSTORY, LIFE AT SUCC, VOICE & BEHAVIOR, THE LINE), `{{age}}` nel campo AGE.
- `summary` (PList), `display_description`.
- 5 outfit + Default Outfit: Lecture Hall, Office Hours (Default), Faculty Formal, Off Campus, Full Kitsune Shift (la forma volpe vera, per coerenza con la convenzione Full Shift già usata per i licantropi).
- 5 Dialogue Examples, nessuno diretto a `{{user}}`: primo giorno di lezione, office hours con studente in difficoltà, colleghi sul suo RateMyProfessor, un momento privato di lutto per Rosie (il suo momento più esposto), e lo studente che tenta un approccio personale respinto senza ambiguità.
- `final_instructions`: disciplina di formato + riga esplicita sulla non-relazione con studenti.
- `birthdate`/`start_timeline_position`: 14 novembre 1967 (ora mondo 9992136), età 56 corretta rispetto a world_age corrente (10486470).
- `pronouns`: he/him.
- Attitudes verso Alyssa/Jasper lasciate invariate (stranger, corrette: nessun altro personaggio del World è citato nella fonte).

## Verifica post-reload
Ricaricata la pagina, ri-autenticato, rifetch della card: `check` (em-dash/{{user}}/{{char}}/bold-markdown) vuoto, 5 outfit con Default impostato, 5 Dialogue Examples, 2 Attitudes, birthdate = start_timeline_position, format-discipline e riga THE LINE presenti in `final_instructions`, `is_global` true.

## Stato "3 in attesa"
Con Hideo Reid completato, restano Venera Dolce (fatta) e **Adelin Coso**, il cui materiale è appena arrivato e verrà lavorato subito dopo.
