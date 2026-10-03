# Graham Purcell: aggiornamento da fonte primaria, e Arran Parker (nuovo) — 2026-09-14

## Perché è un aggiornamento e non una prima stesura

Graham Purcell era già stato costruito in questa sessione (vedi `LosAngeles_SRF_AlphaSquad_Completamento_2026-09-14.md`) da una fonte secondaria minima incorporata nella scheda di Kaladin Nargathon (poche righe: legame professionale, personalità sommaria). È arrivata oggi la fonte primaria completa e dedicata a Graham, molto più ricca. Per §9.4, il `long_summary`/`summary`/`display_description` sono stati **riscritti** usando il materiale primario; outfit e Dialogue Examples, già generici e senza `{{user}}`, sono stati lasciati intatti perché restano coerenti con la versione aggiornata.

**Nessuna discrepanza sull'età**: 40 anni, confermata sia dalla prima stesura sia dalla fonte primaria arrivata oggi (`birthdate` 10133688 invariato).

## Esclusione di contenuto

Caso standard §13: `{{user}}` nella fonte primaria è l'amante di Graham, con protezione, favoritismi (fa fare a `{{user}}` la sua scartoffia), un obiettivo dichiarato di "morire in battaglia o ritirarsi in Scozia con `{{user}}`", e un contrasto pubblico/privato (lo tratta come un soldato qualunque in pubblico, lo vizia in privato). Rimosso integralmente, non generalizzato con un ruolo: non c'è modo di mantenere "il suo amante" come concetto senza legarlo a un `{{user}}` specifico. L'obiettivo di vita è stato riscritto senza il riferimento a `{{user}}`. Il tratto "tratta il partner da soldato in pubblico, lo vizia in privato" è stato mantenuto in forma generica nell'Intimacy Profile, riusabile con un futuro interesse romantico.

## Arran Parker: nuovo personaggio costruito

Menzionato nella fonte primaria come "amico stretto da quasi vent'anni", Captain S.R.F., volpe demiumana. Costruito come Character a pieno titolo (non solo riferimento nelle Attitudes), nessun contenuto da escludere, la fonte non ne forniva.

## Relazioni aggiornate

Graham → Arran: close_friend, intensity 85 (nuova).
Arran → Graham: close_friend, intensity 85 (nuova, reciproca).
Graham → Miles Airhardt (già esistente, gli riporta direttamente): acquaintance, intensity 55 (nuova).
Miles → Graham: acquaintance, intensity 55 (nuova, reciproca).
Graham → Kaladin Nargathon: close_friend, intensity 70 (dalla stesura precedente, non toccata).
Graham/Arran → Alyssa e Jasper: stranger, intensity 15, come da §16.

## Intimacy Profile

Nuovo (mancava nella prima stesura, non c'era ancora base). Registro prosa: libido alta e dominanza legate alla biologia da orso, si eccita quando è arrabbiato invece di calmarsi, kink per breeding (pur non volendo figli), sesso pubblico/rischioso, differenza di taglia, brat taming, shotgunning, il contrasto pubblico/privato generalizzato. Nessun riferimento a `{{user}}`. Lexicon `_kmtwf7pRLRqnf2f1n37N8`.

## Pipeline

Graham: `long_summary`/`summary`/`display_description` riscritti, outfit e Dialogue Examples esistenti confermati validi e lasciati intatti, Attitudes estese da 3 a 5. Arran: JED+ completo, summary PList, display_description, pronomi, 5 outfit con Default Outfit ("Duty Uniform"), 5 Dialogue Examples, 3 Attitudes, final_instructions standard. Global Character ON per entrambi, RPG Stats non toccate. Arran filato nella cartella Los Angeles (ora 26 personaggi, insieme al resto del cluster Alpha Squad/S.R.F.).

Verificato con GET autenticata fresca dopo la scrittura su entrambe le schede: zero `{{user}}`, zero em-dash, zero grassetto, birthdate/start coincidenti su entrambi, outfit_count 5, speech_examples_count 5, attitudes_count 5 (Graham) e 3 (Arran), is_global true su entrambi.
