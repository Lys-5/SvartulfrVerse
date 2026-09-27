# Attitudes: fase 2 e normalizzazione in inglese

Fase 2 il 2026-09-03, normalizzazione linguistica il 2026-09-04.
Scritte via API autenticata, con round-trip verificato.

## Stato finale, verificato dopo reload completo

| | |
|---|---|
| Schede totali | 86 |
| Schede con Attitudes | **36** (tutte quelle lavorate) |
| Attitudes totali | **152** |
| Schede senza Alyssa o Jasper | **0** |
| Collegamenti rotti | **0** |
| Righe verso The Player (Persona) | **0** |
| Intensità lasciate a 1 | **0** |
| Motivazioni in italiano | **0** |
| Em-dash o `{{user}}` nelle motivazioni | **0** |

Regola §16 applicata: Alyssa e Jasper su ognuna, più i soli personaggi
effettivamente citati nel background.

## Le righe che valgono qualcosa

**Zefir → Kaladin, Wary.** Zefir ha guardato il lupo di Kaladin per cinque anni
e ha notato l'unica eccezione al suo camminare avanti e indietro: vicino ad
Alyssa si zittisce. Non l'ha detto a Wulfnic, non l'ha detto a Ut, non l'ha
detto a Kaladin. Non ha ancora deciso se quello che sta guardando sia una
misericordia, e finché non decide tiene la distanza di uno che ha già scelto da
che parte stare.

**Ut → Kaladin, Wary.** Stessa percezione, vocabolario diverso: puzza di
sbagliato e Ut non ha le parole per collegarla a un laboratorio, quindi archivia
sotto inaffidabile.

**Marcus → Kaladin, Pack-bonded 90.** Il ragazzo che ha deciso di crescere.
Marcus → Alyssa e Jasper è **Unknown Scent 15**: non li ha mai incontrati, sono
nomi attaccati alla famiglia che Kaladin è pagato per tenere viva.

**Rev → Alyssa, Acknowledged 40.** Le ha fatto il filo il giorno del suo arrivo
al campus, come lo fa a tutti, feromoni compresi, e ha rischiato di essere fatto
a pezzi. Non ha rifatto quell'errore. **Rev → Malachia, Wary 60**, perché la
lezione l'ha capita benissimo.

**Finn → Alyssa, Wary 55.** Quattro secondi all'ultimo anno di liceo. Lui ha
perso le parole esatte, lei no. **Finn → Jasper, Acknowledged 35**: non sa
ancora che Jasper era lì e ha sentito tutto.

**Hank Thompson → Jasper, Wary 40 / → Alyssa, Trusted 65.** Lo stesso anno in
cui leggeva le assenze di Jasper a Erik davanti a un registro, aveva la sorella
nelle stesse ore, terza fila, appunti perfetti. Hank guida a casa e resta un po'
in macchina nel proprio vialetto prima di entrare.

**Oskar → Andrew, Pack 75 / → Stan Jr., Pack 80.** L'Anime Club del venerdì è
l'unica stanza del campus dove funziona: nessuno gli ha chiesto di togliersi il
cappuccio e nessuno ha cambiato sedia.

**Vincent → Andrew, Pack 60.** Non è crudele con lui, è distratto in pubblico,
che è una risposta a sua volta.

## Chi non conosce nessuno

Tate, Nikolaj, Ariadne e Iordan hanno solo Alyssa e Jasper a Unknown Scent 15.
È corretto: le loro schede non citano nessun altro personaggio del World, e
inventare rapporti sarebbe una violazione di §9.4. Sono anche i candidati
naturali per i prossimi agganci narrativi.

## Normalizzazione in inglese (04/09/2026)

**33 motivazioni erano in italiano, non dodici come stimato inizialmente.**
Riscritte tutte in inglese, non tradotte meccanicamente ma riformulate in modo
che leggano come il resto della scheda.

| Scheda | Righe riscritte |
|---|---|
| Erik Douglas | 10 |
| Logan Douglas | 8 |
| Malachia Douglas Bloodmoon | 7 |
| Noah, Elizabeth, Magnus | 2 ciascuno |
| Wulfnic, Nixara, Kaladin, Edric | 1 ciascuno |

**Motivo:** il Relationship Block entra nel prompt insieme alla description, che
è in inglese. Un blocco misto costringe il modello a cambiare lingua a metà
contesto, ed è esattamente il tipo di attrito che peggiora la resa.

**Convenzione da qui in avanti: tutto il contenuto delle schede è in inglese**,
motivazioni delle Attitudes comprese. L'italiano resta la lingua della
conversazione e della documentazione di progetto, non del contenuto del World.
Fa eccezione quanto deciso per gli Scenari, che avranno **due greeting, uno in
italiano e uno in inglese**.

## Verifica di non danneggiamento

Confronto campo per campo di tutte le 86 schede prima e dopo l'intera
lavorazione: **zero differenze** su description, summary, display description,
final instructions, outfit, Dialogue Examples e blocco RPG. Le uniche modifiche
sono nelle Attitudes.

## Trappola nuova e importante: UI e API non vanno mescolate sulla stessa scheda

**Andrew Campbell è tornato indietro da solo.** Aveva 5 Attitudes scritte via
API e verificate; più tardi, dopo che la sua scheda era stata riaperta
nell'interfaccia per ispezionare il dropdown dei tier, è ricomparso lo stato
vecchio: 3 Attitudes e l'intensità di Noah a 55, cioè **esattamente il
contenuto del form rimasto in pagina da un tentativo di salvataggio precedente
che sembrava non essere andato a buon fine**.

Quindi: un salvataggio dell'interfaccia che sembra non aver fatto niente può
partire in ritardo e sovrascrivere ciò che è stato scritto via API nel
frattempo, riportando indietro la scheda.

**Regola operativa:** su una scheda, in una sessione, o si lavora
dall'interfaccia o si lavora via API. Se serve aprirla nell'interfaccia dopo
una scrittura via API, **ricaricare prima la pagina** e non riusare un form
rimasto aperto. E la verifica finale va sempre fatta rileggendo dal server.

## Nota tecnica: il token va ricatturato a ogni ricarica

Dopo un reload della pagina il Bearer token non è più in memoria e un `fetch`
scritto a mano torna **200 con lista vuota**, che è esattamente il falso allarme
descritto in §11. Si ricattura agganciando `window.fetch` e lasciando che sia
l'app a fare una richiesta (click su Characters e poi sul pulsante Refresh),
leggendo l'header `Authorization` dalla sua chiamata.
