# Los Angeles — Deadwood Circus (Emlyn, Persephone, Ignis) e Vero Walker (2026-09-15)

Quattro schede nuove, dominio Underworld (Los Angeles), inserite nel locale Wyldfire. World a 128 personaggi dopo l'inserimento (124 → 128). Più una entry Lexicon (`BLOODHOUND PMC`, tipo `other`, id locale `O6M-MniwsKbk86r4R6OcC`).

- **Emlyn Danes**, id locale `BZ5JzyAGk9A8LkE5mFlwI` — arpia, ringmaster e proprietario del Deadwood Circus, in tour attualmente nell'area di Los Angeles.
- **Persephone**, id locale `0cWZvqGMvRNWScB0Cf352` — demone, assistente del circo, in segreto trama per rovesciare Emlyn.
- **Ignis**, id locale `bVJOjn1LW1q0vR0f8If2i` — elementale del fuoco, sputafuoco e ballerino del circo, apertamente diffidente verso Emlyn.
- **Vero Walker**, id locale `aYr_uisqSCdcji7-TSWwf` — licantropo, operativo mercenario per BLOODHOUND PMC.
- Intimacy Profile per Emlyn (`rkEO9dIDrKxCkAffN5bVR`) e Vero (`u1wMQtSFJ0YTgLPjF8ojc`). Persephone e Ignis non ne hanno: la fonte non specifica contenuto sessuale per loro.

## Emlyn Danes: intervento pesante sul materiale sorgente (§13 Estensione 14/09)

La fonte non era una semplice cotta fissa su `{{user}}`. Descriveva **cattività letterale**: Emlyn lega, incollara e "possibilmente storpia (rompe le caviglie)" `{{user}}` se tenta di fuggire; controlla cosa mangia, cosa indossa e con chi parla; lo obbliga a rispondere a indovinelli per guadagnarsi il permesso di lavarsi o dormire; e lo **impregna forzatamente con uova** tramite oviposizione, esplicitamente contro la sua volontà. Segnalato all'utente prima di scrivere qualunque cosa, per l'entità del contenuto (cattività fisica, mutilazione, riproduzione forzata), non una semplice riga isolata.

**Scelta dell'utente: "Villain più esplicito ma sempre consensuale".** Tenuto: ringmaster, arpia, narcisismo, sociopatia, passato da orfano abusato, linguaggio in rima e teatrale, crudeltà verso gli artisti che tentano di andarsene, fama vaga e mai provata di sparizioni (già ambigua nella fonte stessa, lasciata così). Sostituito il nucleo "ossessione per `{{user}}`" con un tratto di personalità generico e non risolto ("The Collector's Instinct": quando qualcosa o qualcuno lo colpisce, l'ammirazione degenera in bisogno di possesso, disponibile per futuri agganci narrativi senza puntare a una vittima specifica già in atto). **Scartati integralmente**: cattività fisica reale, minaccia di mutilazione, controllo totale su una persona nominata, riproduzione forzata, indovinelli come meccanismo di coercizione.

**Intimacy Profile di Emlyn**, per scelta esplicita dell'utente, più esplicito del minimo ma sempre consensuale: dominanza, controllo, collaring, indovinelli come gioco consensuale tra due persone che sanno cosa sono (non più ostacolo reale a bisogni primari), linguaggio elaborato durante l'intimità. L'oviposizione resta come tratto biologico dell'arpia, ma riscritta come atto significativo offerto solo a un partner che lo desidera a sua volta, mai come gravidanza forzata.

## Vero Walker: purga standard §13

Rimosso il legame fisso di "compagno" (mate) con `{{user}}`, inclusa la frase di innamoramento e la rabbia specifica verso l'odore di un altro uomo su `{{user}}`. Il ciclo di calore, l'ossessione per l'accoppiamento/annodamento, il marcaggio olfattivo e la possessività restano come tratti generali del personaggio legati a un futuro compagno non ancora determinato, spostati nell'Intimacy Profile. **Scartato il blocco Setting della fonte** ("Modern Earth 2023, umani e non-umani non possono sposarsi legalmente nella maggior parte dei paesi"): in conflitto con `Supernatural_Civil_Status.md` già canon nel Project (California, dove Vero opera, garantisce piena personalità giuridica ai sovrannaturali). Mantenuti invece BLOODHOUND PMC e la rivalità con LUNAR come elemento organizzativo portabile, documentato in una entry Lexicon separata (`type: other`) dato che non ha una posizione fisica mappata (§7).

## Note minori

- **Età invenzione dichiarata**: la fonte non specifica l'età di Persephone e Ignis. Assegnate età apparenti plausibili (Persephone 29, nata 2 dicembre 1994; Ignis 27, nato 27 luglio 1996), date variate come da convenzione. Da confermare o correggere se in futuro emerge una fonte più precisa.
- **Emlyn**: età reale = età apparente ("early 30s" nella fonte, nessuna indicazione di longevità da arpia in questo dominio), nato 5 settembre 1992.
- **Attitudes**: oltre alle due obbligatorie Alyssa/Jasper (stranger/15) su tutte e quattro le schede, aggiunte le relazioni testualmente supportate dalla fonte: Emlyn↔Persephone (wary/55 su Emlyn, rival/70 su Persephone, dato che lei lo tradirà), Emlyn↔Ignis (wary/55 e wary/60, sfiducia reciproca). Nessuna relazione inventata tra Persephone e Ignis, non supportata dalla fonte.

## Verifica

`PRAGMA integrity_check` ok, conteggio World 128/128, zero `{{user}}`, zero em-dash, zero grassetto markdown su tutte le righe (4 character + 2 Intimacy Profile + 1 Lexicon organizzativo), controllo esplicito di assenza di termini di cattività/coercizione sulla scheda di Emlyn (maim, break their ankles, implant, impregnate, forced, ecc.) superato, Attitudes risolte correttamente per id locale su tutte le schede coinvolte, nessuna collisione di chiavi con schede esistenti. Scritto sul dispositivo dopo conferma che Wyldfire fosse chiuso, nessun file `-wal`/`-shm` residuo trovato dopo la scrittura.
