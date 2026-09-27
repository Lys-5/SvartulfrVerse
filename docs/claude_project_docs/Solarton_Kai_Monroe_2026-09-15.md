# Solarton — Kai Monroe (2026-09-15)

Scheda nuova, inserita nel locale Wyldfire (`world_characters`, id locale `UMU4s2bE7_VLTebcVONpq`) più il suo Intimacy Profile in `world_lexicon_entries` (id locale `JBmDyfc5QAPZhEpO0ZgO4`). World a 122 personaggi dopo l'inserimento (121 → 122).

## Cosa dice la fonte

Card `<kai_monroe>` in inglese: demone incubo, tatuatore, bagnino volontario, residente a Santa Monica in convivenza romantica con `{{user}}`, con famiglia che "adora" `{{user}}`, un tatuaggio a forma di cuore dedicato esplicitamente a `{{user}}`, sezioni Intimacy/Speech/Notes complete.

## Cosa abbiamo scritto

- **Dominio**: Santa Monica non è un luogo di questo World; adattato a **Solarton**, dove il personaggio è stato inserito come da lista NPC ufficiali fornita dall'utente.
- **`{{user}}` purgato secondo lo standard §13** (non l'estensione 14/09, qui non c'era contenuto di tratta/non-consenso, solo un arco romantico fisso): rimossa la convivenza romantica con `{{user}}`, rimossa la riga sulla famiglia che "adora" il partner. Il tatuaggio a cuore, che nella fonte era dedicato a `{{user}}`, è stato **riassegnato a sua madre** invece di essere tagliato del tutto: resta un dettaglio fisico riutilizzabile della scheda.
- **Blocchi anatomici/kink** spostati integralmente nell'Intimacy Profile Lexicon separato (`type: memory`, `is_global: true`, `party_conditions` su Kai stesso, formato in prosa continua senza misure numeriche esplicite), coerente con la §13 punto 3 generale.
- **Attitudes**: solo le due obbligatorie (Alyssa Douglas Bloodmoon, Jasper Douglas Bloodmoon), entrambe `stranger`/intensity 15, "mai incontrati": Kai Monroe non ha ancora agganci narrativi con nessun altro personaggio del World.
- **Key collision evitata**: il World ha già "Kai Mitchell" con `keys: ["Kai Mitchell","Kai","Mitchell"]` e `key_logic: AND_ANY`, quindi la chiave nuda "Kai" da sola attiva già quella scheda. Kai Monroe è stato registrato con `keys: ["Kai Monroe","Monroe","Row"]`, **senza** la chiave nuda "Kai", per evitare che le due card sparino insieme su una menzione generica.
- RPG Stats lasciate `NULL` (sistema in pausa, §8), `species_id`/`occupation_id` non toccati.
- Start Position = birthdate (10245480, nato 1996-10-08, 27 anni), nessuna End Position (vivo).

## Verifica

`PRAGMA integrity_check` ok, conteggio World 122/122, zero `{{user}}`, zero em-dash, zero grassetto markdown su entrambe le righe (character + lexicon entry), Attitudes risolte correttamente per id locale contro Alyssa e Jasper, `attached_world_character_id` del lexicon entry allineato all'id locale di Kai. Scritto sul dispositivo dopo conferma che Wyldfire fosse chiuso, nessun file `-wal`/`-shm` residuo trovato dopo la scrittura.
