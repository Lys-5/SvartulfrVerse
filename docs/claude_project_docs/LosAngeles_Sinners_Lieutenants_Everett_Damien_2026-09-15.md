# Sinners: Everett Rottmore, Damien Bishop, i Lieutenants e Alicia Virtuoso (2026-09-15)

Completamento delle sei schede vuote flagged in `Audit_Completezza_Outfit_Shift_2026-09-15.md`, su materiale sorgente fornito esplicitamente dall'utente. World invariato a **134 personaggi** (sono tutti UPDATE su righe stub già esistenti, mai INSERT), **221 entry Lexicon** (+2 Intimacy Profile).

## Everett Rottmore

Fixer soprannaturale losangelino, umano colpito da una maledizione che lo desidrata lentamente, curabile solo consumando carne o fluidi corporei viventi. Fonte con una dinamica "{{user}} acquisito come animaletto personale": non rientra nella soglia grave dell'Estensione 14/09 (nessuna cattività fisica, mutilazione o riproduzione forzata), quindi trattato con la purga standard §13: la meccanica di nutrimento della maledizione è stata riscritta come un bisogno aperto e attualmente irrisolto, senza inventare una relazione sostitutiva per riempire il buco (§13.2, §9.4). La maschera a teschio è scritta come costante esplicita e motivata (§4, stesso trattamento del cappuccio di Dullahan): non si toglie mai, in nessun contesto, e il tocco su viso/testa è un hard limit. Silas, il maggiordomo, resta materiale di supporto in prosa, non una scheda propria (stessa scelta di scope fatta altrove nel World per figure di contorno). Intimacy Profile separato creato (contenuto anatomico/kink presente nella fonte).

## Damien Bishop

Demone detective privato specializzato in casi sovrannaturali. **Rilocato da Manhattan a Los Angeles**: la fonte lo ambientava a Manhattan, ma è confermato presente nel roster Underworld/Modern Fantasy (`Roster_Canon_Underworld_Modern_Fantasy.md`), e quel dominio nel World è Los Angeles, non New York (§10). Corretto come dettaglio geografico minore non tematico, non come deviazione dal personaggio. Nessun contenuto `{{user}}` nella fonte. Sessualità switch/dom con corruption kink spostata in Intimacy Profile separato.

## GLUTTONY - Kevin, ENVY - Siobhan, GREED - Roxie

Costruiti dal materiale sui "Lieutenants" fornito dall'utente più le tracce già scritte nelle schede esistenti di Jean-Luc Virtuoso e Dante, che li citavano già in prosa e nelle rispettive Attitudes (per Roxie e Siobhan) pur avendo le righe corrispondenti ancora vuote. Età tutte tratte dalla fonte: Kevin 22, Roxie 38. Per Siobhan la fonte dà solo "100+"; la cifra esatta (104, nata 1920) è un'invenzione dichiarata sul solo numero preciso, non sull'ordine di grandezza, con data variata rispetto al 1° del mese (§9.6). Nessun contenuto `{{user}}` nella fonte per questi tre. Nessun Intimacy Profile: la fonte non contiene materiale anatomico/kink per loro, solo tratti caratteriali (incel per Kevin, attivismo performativo per Siobhan, ossessione da accumulo per Roxie).

## Alicia Virtuoso

Moglie di Jean-Luc, ex modella, umana indifferente al mondo sovrannaturale/criminale del marito. Età 35 dalla fonte, coerente con il matrimonio "decennale" già scritto sulla scheda di Jean-Luc. **Aspetto informato dall'immagine di riferimento inviata dall'utente**: usata per scrivere l'outfit "At Home" (camicia bianca oversize presumibilmente di Jean-Luc, stivali alti color cammello, divano di pelle nera, carte sparse sul pavimento), coerente col suo ruolo di chi gestisce la tenuta e l'immagine pubblica del marito. Nessun contenuto `{{user}}` né anatomico/kink nella fonte, nessun Intimacy Profile.

## Aggiornamenti incrociati (Attitudes, §16)

- **Jean-Luc Virtuoso**: aggiunte le tre Attitudes mancanti verso Kevin (disliked/35, disgusto malcelato), Siobhan (acknowledged/45, consapevole del suo complotto e lo trova quasi divertente), Roxie (acknowledged/50, "la tratta come un'arma carica"). Array riletto e riscritto per intero (§11, gli array si sostituiscono, non si fanno il merge), ora **11 Attitudes** in totale.
- **Zero**: aggiunta l'Attitude reciproca verso Roxie (rival/55, "fights constantly", citata sulla scheda di Roxie ma assente sul lato di Zero), ora **6 Attitudes**.
- Alicia → Siobhan aggiunta (acknowledged/20, consapevole della sua gelosia e la trova irrilevante), reciproca alla Siobhan → Alicia già scritta (hated/75, gelosia dello status e del matrimonio).
- Roxie ↔ Dante, Siobhan ↔ Dante aggiunte sul lato Roxie/Siobhan, reciproche alle Attitudes già esistenti su Dante verso di loro.
- Kevin ↔ Roxie, Kevin ↔ Siobhan, Roxie ↔ Siobhan aggiunte come relazioni fra Lieutenant dello stesso gruppo, testualmente supportate dalla fonte dove presente (dinamica Kevin/Roxie/Siobhan esplicita nella fonte) o come acquaintance leggero fra colleghi dove la fonte non specifica nulla (Roxie↔Siobhan).

Tutti e sei i personaggi hanno le due Attitudes obbligatorie verso Alyssa Douglas Bloodmoon e Jasper Douglas Bloodmoon (stranger/15, mai incontrati, mondi separati).

## Verifica

Script eseguito in due tempi (un `NameError` su una costante mancante nell'ultimo blocco di cross-reference ha richiesto un secondo script di completamento mirato; le sei schede principali erano già state scritte e committate correttamente al momento dell'errore, verificato che nessuna scrittura fosse duplicata prima di procedere). `PRAGMA integrity_check` ok, conteggio World invariato a 134, conteggio Lexicon a 221 (+2 Intimacy Profile). Zero `{{user}}`, zero em-dash, zero markdown grassetto su tutte le sei schede e sulle due entry Lexicon. Tutte le Attitudes risolvono su id di personaggi effettivamente presenti nel World. Outfit: 5 per scheda, tutti con chiave `avatar`, `default_outfit` valido su tutte e sei. Scritto sul dispositivo dopo conferma che Wyldfire fosse chiuso, nessun file `-wal`/`-shm` residuo trovato dopo la scrittura.
