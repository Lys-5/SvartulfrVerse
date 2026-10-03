# Audit Live: Family, Pack, Blackwood, Council (esclusa Los Angeles) — 2026-09-14

Verifica in tempo reale eseguita su richiesta dell'utente ("lasciando fuori los angeles, cosa rimane da fare per le altre sezioni?"), perché diversi documenti del Project (in particolare `TODO_Consolidado.md`, datato 7 settembre) risultavano superati dal lavoro fatto in questa sessione e in quella precedente.

## Metodo

GET autenticata fresca su `/api/worlds/{world_id}` per `content_folders`, e su `/api/worlds/characters/world/{world_id}` per l'elenco completo (104 personaggi). Controllo campo per campo di ogni scheda nelle cartelle Family (12), Pack (4), Blackwood (9), più i personaggi del Concilio creati in questa sessione.

## Risultato per cartella

**Family (12/12) e Pack (4/4): complete.** Ogni scheda ha long_summary in JED+, summary, display_description, 5+ outfit con Default Outfit impostato, Start Position, Global Character ON. Due falsi allarmi trovati e chiariti durante il controllo:
- Jasper e Noah Douglas Bloodmoon: il mio primo check segnava "non JED+" perché il long_summary comincia con un'intestazione `# [Nome]` prima del blocco `[NAME: ...]`. È JED+ valido, solo con un titolo markdown-H1 davanti (non un asterisco, quindi non viola §3). Nessuna azione necessaria.
- Wulfnic Bloodmoon: il mio primo check segnava "Start Position mancante" perché `start_timeline_position` vale `0`, che in JavaScript è falsy. In realtà `0` è un valore legittimo: coincide con il World Age 0 (21 dicembre 827), coerente con Wulfnic come Divine Blood dell'era fondativa. `birthdate` coincide. Nessuna azione necessaria.

Unico dettaglio minore, non bloccante: sette schede di Family/Pack (Edric, Jasper, Noah, Magnus, Nixara, Wulfnic, Kaladin) hanno **3 Dialogue Examples invece di 5**, sotto lo standard di §14.9. Probabile residuo di una convenzione più vecchia. Segnalato, non corretto: nessuna indicazione dell'utente a farlo ora.

**Blackwood (9/9): completa.** Angelo Moreno, Vito Marino, Bianca Rossi, Aurora Night, Cass Harrow, Eclipse Noir, Federico "Riki" Savini, Isobel Blackwater, Dominic Chen: tutti con long_summary JED+, 5 outfit con Default Outfit, 5 Dialogue Examples, Attitudes, Start Position, Global Character ON, zero `{{user}}`/em-dash/grassetto. Nessuno ha un Intimacy Profile in Lexicon, ma verificato che nessuno ne ha bisogno: le uniche occorrenze di parole come "sexual" nei long_summary sono etichette di orientamento (pansexual, demisexual, heterosexual, bisexual), non contenuto esplicito da spostare.

## Gap reali trovati

**1. Dodici schede non filate in nessuna `content_folder` dei personaggi** (su 104 totali, solo 92 risultano in una cartella):
- Le 8 create in questa sessione: Harrison Black, Abel Vilas, Cassian Aralas, Marlowe Voss, Zeera, Brak Ironfist, Barrow, Harlan "Huck" Beaumont.
- Altre 4, presumibilmente da lavoro di sessioni precedenti mai filate: Helena Weiss, Darius Vale, Naomi Black, Marcus O'Connor.

Non è un problema di merito della scheda (tutte già passate per la pipeline completa), è solo mancata assegnazione a una cartella. Va deciso dove vanno: probabilmente serve una cartella "Council" o "Blackwood" a seconda del personaggio, da confermare con l'utente prima di scrivere (i nomi delle cartelle esistenti sono Family/Pack/Blackwood/Solarton/Los Angeles, nessuna è ovviamente corretta per un Concilio cittadino).

**2. Attitudes reciproche mancanti tra i 7 rappresentanti di minoranza del Concilio.** Solo la coppia Cassian Aralas ↔ Harrison Black si conosce reciprocamente (aggiunta durante la lavorazione di Cassian). Le altre 6 schede (Abel Vilas, Barrow, Brak Ironfist, Harlan Beaumont, Marlowe Voss, Zeera) non hanno alcuna Attitude verso gli altri membri del Concilio, né viceversa. Dato che siedono nello stesso organo, è ragionevole che si conoscano almeno di vista/reputazione. Non fatto finora, resta in coda come lavoro opzionale già segnalato in `Marlowe_Voss_NonMorti_Representative_2026-09-14.md`.

## Voci del TODO_Consolidado.md (7 settembre) verificate come superate

Confermato risolto dal lavoro di questa sessione e della precedente: Vito Marino, Bianca Rossi, Isobel Blackwater, Eclipse Noir, Dominic Chen, Cass Harrow (tutti nella cartella Blackwood, verificati completi sopra). Elizabeth Duskwood, citata nel TODO come scheda vuota, risulta invece completa nella cartella Family. Le cifre aggregate del TODO (88 personaggi totali, 25 schede vuote, ecc.) sono da considerare obsolete: il World ne conta oggi 104.

## Cosa resta aperto, esclusa Los Angeles

- Filing delle 12 schede orfane (punto 1).
- Attitudes reciproche fra i 7 rappresentanti di minoranza (punto 2), opzionale.
- 7 schede Family/Pack con solo 3 Dialogue Examples invece di 5, minore.
- Nessun'altra lacuna strutturale trovata in Family, Pack, Blackwood.

## Aggiornamento 2026-09-14 (stesso giorno): tutti e tre i gap chiusi

Su istruzione esplicita dell'utente ("puntiamo ad avere ZERO gap prima di inserire nuovo materiale"), i tre gap sopra sono stati chiusi in sequenza, ciascuno verificato con una GET autenticata fresca dopo la scrittura:

**1. Filing delle 12 schede orfane.** Tutte spostate nella cartella Blackwood via PUT su `content_folders` (world-level, campo `content_folders` per intero per via della regola di sostituzione totale degli array): Harrison Black, Abel Vilas, Cassian Aralas, Marlowe Voss, Zeera, Brak Ironfist, Barrow, Harlan Beaumont, più le 4 già orfane da prima (Helena Weiss, Darius Vale, Naomi Black, Marcus O'Connor). Scelta di cartella: Blackwood, perché è già la cartella dei Pack Leader/figure cittadine di Blackwood, la stessa categoria di questi 12. Verificato dopo reload: 104/104 personaggi filati, zero orfani.

**2. Attitudes reciproche fra i 7 rappresentanti di minoranza del Concilio + Harrison Black (8 schede totali).** Scritte le 27 coppie mancanti (54 entry singole, 27 su ciascun lato), lasciando invariata l'unica coppia già esistente (Cassian↔Harrison). Tier assegnato caso per caso in base al testo di ogni personaggio: `acquaintance` per la maggioranza (colleghi di Concilio, intensity 40-50), `friend` dove il materiale di scheda già suggeriva un rapporto più caldo (es. Brak↔Barrow, Cassian↔Marlowe), `wary` dove il passato di Zeera (ex mercante di schiavi Vax) crea attrito plausibile con Barrow (rappresentante dei demi-umani, la specie storicamente sfruttata) e con Harrison (un dio che riconosce lo schema dello sfruttatore riformato). Verificato dopo reload: tutte le 28 coppie possibili fra gli 8 personaggi ora reciproche, zero mancanti.

**3. Dialogue Examples portati a 5/5** su Edric Douglas, Jasper Douglas Bloodmoon, Noah Douglas Bloodmoon, Magnus Douglas III, Nixara Bloodmoon, Wulfnic Bloodmoon, Kaladin Nargathon (prima a 3/5). I due nuovi esempi per personaggio sono stati scritti rispettando la voce già stabilita da ciascuna scheda esistente (letta per intero prima di scrivere) e temi non ancora coperti dagli esempi precedenti: per Edric, l'interazione con la sicurezza di Kaladin e la ricerca di vicinanza fisica notturna da Logan; per Jasper, il suo alter ego DJ Frequency smascherato e il compleanno che coincide con la morte della madre; per Noah, il ruolo di scudo PR per Malachia e l'insicurezza di essere "solo un Delta"; per Magnus, la correzione formale del proprio nome e la scelta di isolamento con Elizabeth; per Nixara, l'insofferenza verso i silenzi di Wulfnic e un momento di tenerezza con Erik prima della nascita dei gemelli; per Wulfnic, il disdegno paziente rivolto direttamente a Erik e l'effetto della Dead Zone sulla tecnologia; per Kaladin, il legame silenzioso con Marcus (unico altro sopravvissuto Gamma-7) e un momento più leggero con Edric. Verificato dopo reload: tutti e sette a 5/5, zero em-dash, zero asterischi, zero `{{user}}`.

**Stato dopo questa chiusura:** zero gap noti in Family, Pack, Blackwood e Concilio (esclusa Los Angeles, non ancora auditata in questa sessione).
