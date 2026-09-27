# Sawyer Shephard & aggancio con Jasper Douglas-Bloodmoon — Completamento 2026-09-14

Nuovo personaggio, nessun placeholder preesistente. Collocazione confermata dall'utente via AskUserQuestion: cartella **Blackwood City**, dato il legame diretto con Jasper.

## Aggancio narrativo con Jasper (indicazione dell'utente)

L'utente ha fornito direttamente il collegamento: a 13 anni Jasper ha violato i server dell'azienda di Sawyer, il CEO gli ha offerto uno stage al compimento dei 16 anni, Jasper ha rifiutato perché non ha interesse a lavorare per altri. Aggiunta una nuova sezione tematica **"THE JOB HE NEVER TOOK"** in coda al `long_summary` di Jasper Douglas-Bloodmoon (append, non riscrittura, per preservare il testo esistente molto esteso), che narra l'episodio dal suo punto di vista. Aggiunta una Attitude reciproca su entrambe le schede: Sawyer → Jasper (acknowledged, 35, lo trova allarmante e delizioso, lo racconta come aneddoto di feste), Jasper → Sawyer (acknowledged, 30, lo trova innocuo e un po' ridicolo, lo tiene a distanza).

## Esclusione di contenuto

Caso standard §13: `{{user}}` nella fonte è la "sugar baby" attuale di Sawyer, tenuta in rotazione 3-6 mesi per evitare legami, viziata ma tenuta a distanza emotiva. Rimosso il riferimento specifico a `{{user}}`, ma il **pattern comportamentale è stato generalizzato e mantenuto**, non richiede di nominare un World character: "tiene abitualmente un/a compagno/a in rotazione" resta un tratto di personalità riusabile con qualunque futuro interesse, esattamente come già fatto per Alistair DeVille e Sully Jones.

## Cosa è stato tenuto

Aspetto fisico completo, il passato da famiglia benestante di licantropi, l'azienda tech finanziata dal padre e diventata un successo dopo il crollo di un concorrente, lo stile di vita da CEO assenteista, i tratti di personalità (rilassato, sicuro di sé, manipolatore, evasivo), l'avversione all'intimità emotiva, l'aneddoto dell'hack di Jasper (ora parte integrante della sua sezione backstory).

## Età

Fonte dava un numero esplicito (42), nessuna discrezione necessaria. Data di nascita scelta per varietà: 20 agosto 1981 (`birthdate`/`start_timeline_position` 10113552, coincidenti).

## Intimacy Profile

Creato in registro prosa: il pattern del "compagno in rotazione" generalizzato, viziare senza investire emotivamente, chiudere i conflitti con regali invece che con un confronto, avversione al preservativo con richiesta di contraccezione alternativa, diventa petulante invece che arrabbiato quando è davvero turbato. Nessun riferimento a `{{user}}`. Lexicon `_8nDqJcKFVU7gddxaRAtzE`.

## Pipeline

JED+ completo, summary PList, display_description, pronomi, 5 outfit con Default Outfit ("Casual Wealth"), 5 Dialogue Examples (incluso uno sull'aneddoto con Jasper), final_instructions con la disciplina di formato standard. Attitudes verso Alyssa (stranger) e Jasper (acknowledged, come sopra); nessuna verso Jasper come "stranger" dato il legame diretto già stabilito. Global Character ON, RPG Stats non toccate. Filato nella cartella Blackwood (ora 25 personaggi).

**Nota tecnica**: il token di autenticazione è scaduto a metà operazione (PUT sul filing di cartella ha risposto 401), rinfrescato e l'operazione ripetuta con successo, coerente con la prassi nota (§11, il token va rinfrescato ogni ora).

Verificato con GET autenticata fresca dopo la scrittura: zero `{{user}}`, zero em-dash, zero grassetto su entrambe le schede, birthdate/start coincidenti su Sawyer, outfit_count 5, speech_examples_count 5, attitudes_count 2 (Sawyer) e 9 (Jasper, da 8), is_global true, reciproca confermata su entrambi i lati.
