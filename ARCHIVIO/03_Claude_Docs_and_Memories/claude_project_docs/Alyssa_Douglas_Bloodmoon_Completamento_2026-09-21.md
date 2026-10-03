# Alyssa Douglas Bloodmoon — Completamento Scheda (2026-09-21)

Terza scheda della famiglia core ricostruita dopo Erik e Jasper, seguendo la stessa pipeline (§14) e la stessa causa di corruzione: import grezzo dalla pubblicazione difettosa dell'app locale Wyldfire, con Long Description vuota e dati compressi nella Short Description, nessun Outfit, nessuna Birthdate, nessun Dialogue Example, nessuna Attitude.

## Pattern di corruzione trovato

Identico a Jasper: mancavano First/Last Name split, Nicknames, Titles, Tags, Timeline, Birthdate, Outfits, Dialogue Examples, Attitudes, Global Character (OFF), Writing Style/final_instructions. **Pronouns e Keys/Secondary Keys erano già corretti** nella riga sorgente, quindi non toccati.

## Campi ricostruiti

- **Nome**: Display "Alyssa Douglas Bloodmoon", First "Alyssa", Last "Douglas Bloodmoon", Middle Name "Hvit".
- **Nicknames**: Lys, Little Moon, Sunflower.
- **Titles**: The White Moon, Mother of Wolves.
- **Tags**: 14, selezionate dal modal (nessun problema di ricerca stavolta, a differenza di Jasper con gli hyphen).
- **Long Description (JED+)**: ripulita dagli artefatti di citazione (`[span_N](start_span)[span_N](end_span)`) via regex Python prima dell'incollaggio, 5214 caratteri finali. Blocco completo NAME/ALIASES/AGE con `{{age}}`/SEX/SPECIES/SECONDARY_SEX/HOUSE/PACK/PACK_ROLE/SOCIAL_STATUS/STUDIES/SCENT/HUMAN_APPEARANCE/HYBRID_FORM/FULL_SHIFT/UNIQUE_TRAITS/CLOTHING/VEHICLE, poi PERSONALITY/TEMPERAMENT/SPEECH, DYNAMIC_WITH_FAMILY (Erik, Malachia, Noah, Jasper, Edric, Wulfnic), ROLE_AND_DUTIES/ABILITIES/RELIGION/QUIRKS/DISLIKES_AND_TRIGGERS, chiusura SEXUALITY_AND_MATING + BLOODLINE_CLOCK.
- **Short Description**: blocco ALWAYS/NEVER/REMEMBER (1105 caratteri).
- **Display Description**: 123 caratteri.
- **Timeline**: Start Position e Birthdate entrambi a `10320312` (coincidenti, verificati contro `world_age` corrente).
- **Outfits**: tutti gli 11 dalla fonte, aggiunti in batch da 3+3+3+2 via tecnica JS sull'ultimo elemento vuoto per placeholder, nessuna perdita di dati tra i batch. Default Outfit impostato su "Confort / Nesting".
- **Dialogue Examples**: 5, disciplina di formattazione rispettata (niente em-dash, niente asterischi in narrazione, dialogo tra virgolette). Ultimo esempio aggiunto in questa sessione: "A rare unguarded moment with Malachia".
- **Attitudes**: 4, tutte Target Type = World Character, corrette dall'errata tag sorgente `romantic_interest`:

  | Target | Tier | Intensity | Motivazione sintetica |
  |---|---|---|---|
  | Erik Douglas (padre) | Best Friend | 95 | La "Golden Cage" di protezione, capita e perdonata, amore profondo |
  | Malachia Douglas Bloodmoon (fratello) | Best Friend | 90 | Protettore letale che lei sa ammorbidire, fiducia totale nella sua sicurezza fisica |
  | Jasper Douglas Bloodmoon (gemello) | Best Friend | 100 | Legame gemellare dalla nascita, nati il giorno della morte della madre |
  | Edric (cugino) | Friend | 90 | Protezione affettuosa verso il cugino più giovane, cotta innocente mai resa esplicita |

  **Nota sulla ladder**: confermato di nuovo (terza scheda consecutiva) che il dropdown Relationship Tier mostra le 14 etichette in inglese semplice (Nemesis, Enemy, Despised, Hated, Disliked, Stranger, Acquaintance, Friend, Close Friend, Best Friend, Romantic Interest, ...) e non la ladder LSE del documento di progetto. Stessa sostituzione già usata su Erik e Jasper.
- **Writing Style & Tone (final_instructions)**: applicato il testo della fonte (1319 caratteri), che include già in coda la frase di disciplina di formattazione richiesta da §3, quindi nessuna aggiunta manuale necessaria.
- **Global Character**: impostato ON (era OFF).

## Bug incontrato e corretto: scambio Long/Short Description

Durante l'impostazione via JS di tre textarea per indice DOM assunto (`areas[2]`=Display, `areas[3]`=Short, `areas[4]`=Long), lo screenshot ha rivelato che l'ordine reale era invertito: il campo "Long Description" (indice 3) aveva ricevuto il testo breve ALWAYS/NEVER, e "Short Description" (indice 4) il blocco JED+ lungo. Corretto con uno snippet JS di scambio, poi verificato con reload completo e lettura di `textarea.value.length` per confermare la persistenza corretta (area 2=123 Display, area 3=5214 Long/JED+, area 4=1105 Short/ALWAYS-NEVER).

**Lezione per le prossime schede**: non fidarsi dell'ordine DOM assunto per campi testuali multipli con placeholder generici. Verificare sempre via screenshot o controllo di `placeholder`/etichetta visibile immediatamente dopo la scrittura JS multi-campo e prima del salvataggio.

## Discrepanza aperta: Content Rating

Il campo `rating` della riga sorgente è `"explicit"` (coerente con le descrizioni di alcuni outfit, incluso un outfit "Nude"). Il **Content Rating sulla card live è rimasto "General"**, non modificato in questa sessione: non esiste un'indicazione esplicita dell'utente su come trattare questo campo per le schede della famiglia core, e cambiarlo unilateralmente sposterebbe la visibilità/filtri della card. Segnalato qui come promemoria, da decidere con l'utente se e quando toccare Content Rating su Alyssa (e sulle altre schede con outfit simili).

## Verifica finale (§14.12)

Dopo reload completo della pagina:
- Zero occorrenze di `{{user}}`, em-dash, doppio trattino, grassetto markdown in tutti i textarea visibili (description, outfit, dialogue examples, attitude reasoning).
- Nome/Nicknames/Titles/Tags/Keys/Secondary Keys tutti confermati.
- Timeline Start Position e Birthdate = 10320312, coincidenti.
- Pronomi She/Her confermati.
- 11 Outfit + Default Outfit "Confort / Nesting" confermati.
- 5 Dialogue Examples confermati (label, context, response tutti intatti).
- 4 Attitudes confermate con target/tier/intensity/reasoning corretti.
- Global Character = ON confermato.
- Writing Style & Tone (final_instructions) confermato, 264 token.
- RPG Stats non toccate (sistema in pausa, §8).

## Prossimi passi

Procedere con **Malachia Douglas Bloodmoon**, seguendo lo stesso ordine di priorità approvato (Malachia, Noah, Logan, Wulfnic, Kaladin, poi Jared Thompson e Mac).
