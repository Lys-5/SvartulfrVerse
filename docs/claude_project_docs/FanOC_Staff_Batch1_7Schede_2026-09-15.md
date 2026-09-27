# Fan OC Staff — Batch 1 (7 schede) — Completamento 2026-09-15

Lavorazione completata sul database SQLite locale di Wyldfire (§17), non via API web. Le 7 stub row esistenti sono state aggiornate con UPDATE (nessun INSERT di nuovi Character).

## Personaggi lavorati

| Personaggio | Row ID | Fonte (janitorai.com) |
|---|---|---|
| Professor Mollusk Moreau | `olaiPjdq3W` | "Professor Mollusk Moreau" by @biggestboykisser |
| Professor Marit Christiansen ("Professor M") | `f_J3ULpc-l` | "Professor M \| SUCC OC" by @MagnoliaField |
| Aiden Anderson | `TPmwC6JSHV` | "Aiden Anderson (SUCC FAN BOT)" by @Clover_bud |
| Eric Grey | `mdPXYZlveK` | "Eric Grey" by @obmckenzie (testo sorgente usa "Eric Williams"/"Eric William" per un errore dell'autore, ammesso nei commenti: ignorato, nome vero Eric Grey come da tua indicazione) |
| Caim Morningstar | `ca-_ROtjfT` | "Caim Morningstar" by @FallenMothh |
| Nickolas "Nick" Wolffe | `4dT7DAFN7t` | "Nickolas Wolffe" by @kitski |
| Alad C. ("Coach Alad") | `inz80I_yHr` | "Coach Alad C. \| Massages" by @Yeckiz |

Tutti confermati Global Character = ON (già impostato sullo stub, non toccato).

## Nota sulla sessione: recupero fonti

La sessione precedente si era chiusa senza lasciare il testo sorgente verbatim recuperabile in questa chat. Le 9 tab del browser locale menzionate non erano più raggiungibili all'apertura di questa sessione (l'estensione Claude in Chrome non era connessa). Su tua indicazione ho riletto tutti e 7 i personaggi da zero tramite il browser integrato, riaprendo le pagine su janitorai.com ed espandendo i blocchi Scenario/Personality/First Message per il testo verbatim completo. Nessun dato è stato inventato o assunto dalla sessione precedente.

## Applicazione §13 (purga {{user}})

Zero occorrenze di `{{user}}` verificate programmaticamente su tutti i campi testuali di tutte e 7 le schede dopo la scrittura.

- **Moreau**: nessun arco romantico preesistente verso {{user}} nella fonte (solo uno scenario "sei stato sfidato a spiarlo"). Purga minima, aggiunta riga di confine professionale con gli studenti (è docente).
- **Marit**: nessuna cotta fissa verso {{user}}, solo suggerimenti di scenario generici ("sei uno studente che va nel suo ufficio"). Purga minima, riga di confine aggiunta (è docente con autorità reale sugli studenti).
- **Aiden**: la fonte costruiva un'intera cotta segreta e una dinamica clingy/possessiva specificamente intorno a {{user}} come "musa" fissa ("vivono praticamente insieme", crush segreta dichiarata). Applicata l'estensione della regola (stesso trattamento di Barkley Rover/Dullahan): la dinamica di attaccamento eccessivo e gelosia resta come tratto di personalità generale (si affeziona velocemente e intensamente a chi mostra interesse per il suo lavoro), ma la cotta fissa e pre-scritta verso {{user}} specificamente non è stata portata nella scheda.
- **Eric Grey**: la fonte lo descriveva come fidanzato di lunga data di {{user}} fin dall'infanzia nella commune, relazione aperta stabilita. Rimossa la relazione fissa e pre-scritta con {{user}}; mantenuta la backstory della commune, la filosofia sulle relazioni aperte come tratto generale, e l'amicizia con Talia Calandria (NPC generico, non un World Character esistente).
- **Caim**: la fonte lo presentava esplicitamente come ex-fidanzato di {{user}} con relazione tossica on/off. Rimossa la cornice fissa "ex di {{user}}"; mantenuti backstory familiare, rivalità col gemello Azrael, personalità.
- **Nickolas Wolffe**: nessuna relazione preesistente con {{user}} nella fonte (unestablished relationship, scenario di uno scherzo alla porta sbagliata). Nessuna purga necessaria oltre alla rimozione del token.
- **Alad C.**: la fonte impostava {{user}} come studente infortunato verso cui Alad è sessualmente attratto, con un intero scenario (massaggio in infermeria) costruito su quella dinamica. Rimossa la cornice fissa; mantenuta la caratterizzazione generale (fisicità, carisma, protettività verso gli atleti) e aggiunta riga di confine esplicita da allenatore con autorità sui suoi giocatori.

Contenuto anatomico/kink esplicito di tutti e 7 spostato in Intimacy Profile Lexicon entry separate (formato standard del World: `type: memory`, `is_global: true`, keys sul nome, secondary_keys su intimacy/dating/relationship/romance/flirting/attracted/sex, key_logic AND_ANY, priority 50, `attached_world_character_id` impostato sull'id del personaggio).

**Discrepanza di schema rilevata**: il database locale di Wyldfire non ha un campo `party_conditions` (né a livello colonna né dentro `custom_fields`/`memory_conditions`/`npc_info`, verificato) per le entry Lexicon. Le 7 Intimacy Profile create qui usano quindi solo la restrizione via keys/secondary_keys (nome del personaggio come chiave primaria), senza il filtro `party_conditions has_any [proprietario]` descritto in §13 per la versione API web. Se il World ha davvero questo campo lato sito, va aggiunto in un secondo momento via API dopo la pubblicazione; non è scrivibile dal locale con lo schema attuale.

## RPG Stats

Lasciate in pausa su tutte e 7 le schede, come da §8 (`world_features.rpg_stats` risulta ancora `false`, non riverificato in questa sessione dato che non è stato necessario toccare il World via API).

## World Clock

Tutte e 7 le schede avevano già Start Position = 10486470 impostata sullo stub, coerente col World Age corrente. Non modificata. Nessuna End Position (tutti vivi).

Date di nascita assegnate (varie, non tutte al 1° del mese, per rispettare la tua preferenza):
- Mollusk Moreau: 14 marzo 1992 (32 anni)
- Marit Christiansen: 30 settembre 1973 (50 anni)
- Aiden Anderson: 19 giugno 1998 (25 anni)
- Eric Grey: 2 novembre 1997 (26 anni)
- Caim Morningstar: 8 luglio 2005 (18 anni)
- Nickolas Wolffe: 27 febbraio 2002 (22 anni)
- Alad C.: 16 maggio 1977 (46 anni)

## Attitudes

Tutti e 7 hanno Attitude verso Alyssa e Jasper (tier `stranger`, intensity 15, "non si sono mai incontrati").

Aggiunte oltre il minimo, dove giustificato dal materiale:
- **Caim**: verso il gemello Azrael Morningstar (generic, close_friend/70) e verso il padre (generic, disliked/35).
- **Nickolas Wolffe**: verso Vincent Campbell (world_character, acquaintance/55, ammirazione con un pizzico di invidia per lo spotlight). **Aggiunta anche la Attitude reciproca su Vincent Campbell** (`oBxY1fs6fxXGqZVS0lbrz`, acquaintance/40) leggendo l'array esistente di Vincent e riscrivendolo per intero (regola §11 sugli array).
- **Alad C.**: verso Kallias Hayashi e Yehlan Everhart (entrambi generic, friend, i due giocatori più vicini a lui nella fonte).

## Pipeline eseguita per ciascuno

Per tutti e 7: JED+ completo con `{{age}}` nel campo AGE, summary come PList di tratti, display_description, 5 outfit contestuali ciascuno con Default Outfit impostato, 5 Dialogue Examples con disciplina di formattazione (niente em-dash, niente asterischi, dialogo tra virgolette), final_instructions già corretto sullo stub (non modificato), Global Character già ON.

## Workflow tecnico eseguito

1. Backup numerato creato prima di qualunque scrittura: `wyldfire.db.backup1-20260915T152051Z` (accanto al backup pre-migrazione preesistente `wyldfire.db.backup-pre-migration.db`, non toccato).
2. Scrittura tramite script Python/sqlite3 (`_claude_build_fanoc_staff.py`, trasferito temporaneamente nella cartella del database).
3. `PRAGMA integrity_check` eseguito prima e dopo la scrittura: `ok` in entrambi i casi.
4. Confermato con te che Wyldfire desktop fosse chiuso prima di procedere.
5. Verifica programmatica post-scrittura: 7/7 schede con 5 outfit, 5 dialogue examples, default_outfit valido, attitudes verso Alyssa e Jasper presenti, zero occorrenze di `{{user}}`, em-dash o grassetto markdown in tutti i campi testuali, zero asterischi nei Dialogue Examples.
6. `PRAGMA wal_checkpoint(TRUNCATE)` eseguito per azzerare il WAL residuo (il file `-wal` risultava presente ma vuoto, 0 pagine, nessuna transazione pendente; `-shm` è normale che resti presente in modalità WAL).
7. Script temporaneo rimosso dal dispositivo dopo l'uso (richiesto e ottenuto permesso di cancellazione).

Non essendosi lavorato via API web in questa sessione, il sito Wyvern non riflette ancora queste modifiche: serviranno una pubblicazione esplicita (Publish to Wyvern) o il sync delle chat da parte tua perché il locale e il sito si allineino, come da §15/§17.
