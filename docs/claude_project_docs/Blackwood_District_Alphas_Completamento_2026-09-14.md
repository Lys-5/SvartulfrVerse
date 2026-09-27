# Completamento cartella Blackwood (9 District Alpha) — 2026-09-14

Audit e completamento pipeline dei 9 personaggi della cartella "Blackwood" del World, i District Alpha che governano i quartieri di Blackwood City. Stato di partenza (verificato via GET diretto): tutti e 9 avevano `long_summary` in JED+ già scritto e completo, ma **zero** outfit, **zero** speech example, **zero** attitudes, **zero** final_instructions, e display_description vuota. Un divario sistemico non ancora toccato in nessuna sessione precedente.

## Scoperta: lingua mista nei long_summary

Solo **Angelo Moreno** aveva long_summary e summary interamente in inglese, già di buona qualità (nessuna riscrittura necessaria oltre alla pipeline meccanica).

Gli altri **8** (Vito Marino, Bianca Rossi, Aurora Night, Cass Harrow, Eclipse Noir, Federico "Riki" Savini, Isobel Blackwater, Dominic Chen) avevano il blocco attributi in inglese ma i paragrafi di prosa (BACKSTORY, VOICE & BEHAVIOR, RAPPORTI CON BLACKWOOD) scritti in **italiano**, e il campo `summary` in formato raw non lavorato: o attributi in italiano tra parentesi quadre (Vito), o lo stile JanitorAI `{{char}}: attributo(valore), ...` (gli altri 6/7). Trattati come import grezzi non lavorati per §2, riscritti integralmente in inglese preservando ogni fatto della fonte, senza inventare nulla di nuovo. Il tag `{{char}}` trovato in questi summary non è lo stesso problema di `{{user}}` (§13): è solo artefatto del formato di import raw, risolto sostituendo l'intero summary con un blocco JED+ compatto in prosa, non con una sostituzione mirata del tag.

## Lavoro svolto su ciascuno (stesso set di campi per tutti e 9)

Per ognuno: `summary` riscritto in inglese (JED+ compatto, bracket + prosa breve) dove necessario, `display_description` (1-2 righe), 5 `outfits` contestuali con `default_outfit` impostato (il quinto per ciascuno è sempre una "Full Wolf Shift", coerente con la specie Werewolf comune a tutti tranne Angelo, vampiro, che ha invece "Feeding" come quinto), 5 `speech_examples` con disciplina di formattazione (dialogo tra virgolette, niente em-dash, niente asterischi salvo pensieri interni, mai usati qui), `final_instructions` con la riga standard di disciplina di formato, e `attitudes`.

## Attitudes assegnate

Tutti e 9 hanno Alyssa e Jasper a `stranger` (bassa intensità, nessun contatto stabilito: sono figure della malavita/politica dei distretti di Blackwood City, non del campus di Solarton). Aggiunte inoltre le relazioni esplicitamente citate nel testo di ciascuno:

- **Angelo Moreno** → Wulfnic (`rival`, 55): rivalità secolare tra vampiro e Divine Blood, esplicitamente descritta nel testo come "fastidio quasi affettuoso".
- **Vito Marino** → Erik Douglas (`disliked`, 35): tensione con la polizia corporativa della DCC.
- **Bianca Rossi** → Angelo Moreno (`friend`, 65): alleanza di reciproco interesse che protegge Paradise East.
- **Cass Harrow** → Angelo Moreno (`acquaintance`, 40) ed Erik Douglas (`acquaintance`, 35): rapporti pragmatici e diplomatici.
- **Aurora Night** → Erik Douglas (`acquaintance`, 30): scambio di informazioni per autonomia.
- **Federico "Riki" Savini** → Malachia Douglas (`close_friend`, 70): decenni di rispetto reciproco e consulenza politica onesta, esplicitamente descritti nel testo come il rapporto più significativo del personaggio.
- **Eclipse Noir, Isobel Blackwater, Dominic Chen**: nessun altro personaggio del World citato esplicitamente nel loro testo con un rapporto abbastanza definito da giustificare un'Attitude oltre Alyssa/Jasper (Naomi Black, co-reggente citata nel testo di Cass Harrow, **non esiste come Character nel World**: menzionata solo in prosa, nessuna Attitude creata per lei, per non inventare un target che non c'è).

Tier tecnici usati (valori enum confermati validi via API in questa sessione, non le etichette del documento di progetto §16): `stranger`, `acquaintance`, `friend`, `close_friend`, `disliked`, `rival`.

## Verifica

Rieseguito GET su tutti e 9 dopo un reload completo della pagina (nuovo token). Per ciascuno confermato: 5 outfit con default impostato, 5 speech example, final_instructions presente, birthdate === start_timeline_position (nessuno di questi era stato toccato, erano già coerenti), long_summary in inglese puro (nessun carattere accentato italiano residuo), e `window.CHECK()` pulito su tutti (zero em-dash, zero `{{user}}`, zero grassetto markdown).

## Stato

Cartella **Blackwood completamente chiusa**: 9/9 personaggi con pipeline completa. Prossimo passo: cartella **Los Angeles** (21 personaggi), non ancora auditata in questa sessione.
