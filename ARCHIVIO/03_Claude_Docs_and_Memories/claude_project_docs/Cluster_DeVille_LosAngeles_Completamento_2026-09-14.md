# Cluster DeVille (Los Angeles) — Completamento 2026-09-14

Nessun contenuto da escludere: la fonte non conteneva `{{user}}` in nessuna forma, in nessuno dei quattro personaggi. La sezione Intimacy di Alistair era generica (power play, dominanza, avversione al pain play/marking), coerente con dinamiche fra adulti consenzienti, nessun elemento problematico.

## Stato di partenza

Alistair DeVille (`_3WpnXkC14Hgecd3peACWz`) e Cato (`_JGfYMWPpB1THmfXfMFPtE`) esistevano già come placeholder grezzi (solo `summary` popolato col testo sorgente non lavorato, zero `long_summary`, zero outfit, zero dialogue examples, zero attitudes). Riscritti da zero in JED+ invece di essere ritoccati, come da §2. Charles "Charlie" DeVille e Amelia DeVille non esistevano: creati come Character nuovi via POST.

## Perché sono stati costruiti anche Charles e Amelia

Non erano nel cluster originariamente elencato in `LosAngeles_SRF_AlphaSquad_Completamento_2026-09-14.md` (che menzionava solo Alistair e Cato), ma entrambi hanno caratterizzazione propria sufficiente nella fonte (figlio viziato che evita di dimostrare il proprio valore; ex moglie classista in guerra perenne col marito per soldi e manufatti) per meritare una scheda completa invece di restare solo un riferimento nelle Attitudes di Alistair.

## Relazioni (tutte reciproche, nessuna scrittura pendente)

Alistair → Charles: disliked, 55 (delusione professionale, nessun rispetto).
Alistair → Amelia: hated, 75 (divorzio mai davvero chiuso).
Alistair → Cato: close_friend, 70 (unica eccezione al suo disprezzo specista, guadagnata con anni di lealtà).
Charles → Alistair: wary, 50 (paura di non essere all'altezza, mai messa davvero alla prova).
Charles → Amelia: friend, 55 (affetto genuino, stanchezza per il ruolo di tramite).
Charles → Cato: acquaintance, 30 (conosciuto da sempre, mai davvero avvicinato).
Amelia → Alistair: hated, 75 (la guerra post-divorzio, mai finita).
Amelia → Charles: friend, 55 (affetto genuino, uso strumentale verso il padre).
Amelia → Cato: despised, 60 (disprezzo classista/specista aperto).
Cato → Alistair: close_friend, 70 (lealtà professionale assoluta, mai davvero messa in discussione).
Cato → Amelia: disliked, 40 (disprezzo trattenuto, professionale).
Cato → Charles: acquaintance, 30.
Tutti e quattro: Alyssa e Jasper, stranger, intensity 15, come da §16.

## Età

Tutte esplicite in fonte, nessuna discrezione necessaria. Date di nascita scelte per varietà: Alistair 11 ottobre 1960 (età 63), Amelia 3 ottobre 1970 (età 53), Cato 23 novembre 1991 (età 32, corretta, vedi Aggiornamento 14/09), Charles 14 luglio 2000 (età 23). Tutte con `birthdate`/`start_timeline_position` coincidenti.

## Intimacy Profile

Solo per Alistair al momento della prima stesura, registro prosa: selettività estrema nei partner, distacco emotivo anche con gli amanti, desiderio di controllo e devozione, power play, dinamiche con "brat", attrazione per tratti non umani mai ammessa apertamente (in aperta contraddizione con le sue posizioni speciiste dichiarate, tenuta come tratto psicologico interessante), dominante e controllato anche nell'intimità, avversione al pain play e ai segni permanenti perché vede i partner come "tesori" da non danneggiare. Lexicon `_GFReQdDUbUMPdd7LMRrWE`. Vedi Aggiornamento 14/09 sotto per l'Intimacy Profile di Cato, aggiunto in seguito. Nessun Intimacy Profile per Charles/Amelia, la fonte non ne forniva base.

## Pipeline

Tutti e quattro: JED+ completo, summary PList, display_description, pronomi, 5 outfit ciascuno con Default Outfit, 5 Dialogue Examples ciascuno, 5 Attitudes ciascuno, final_instructions con la disciplina di formato standard. Global Character ON per tutti, RPG Stats non toccate. Charles e Amelia filati nella cartella Los Angeles (ora 24 personaggi, da 22); Alistair e Cato erano già presenti in quella cartella.

Verificato con GET autenticata fresca dopo la scrittura su tutte e quattro le schede: zero `{{user}}`, zero em-dash, zero grassetto, birthdate/start coincidenti su tutte, outfit_count 5, speech_examples_count 5, attitudes_count 5, is_global true su tutte.

---

## Aggiornamento 14/09: Cato riscritto da zero, fonte completa arrivata dopo la prima stesura

La prima versione di Cato (sopra) era stata costruita da una descrizione secondaria minima, incorporata nella fonte di Alistair DeVille (poche righe: aspetto generico, "storia poco nota prima dell'assunzione, mai chiesta"). È arrivata successivamente la fonte primaria completa e dedicata a Cato, molto più ricca e in parte diversa. Per §9.4 ("una scheda scritta a intuito prima che arrivino le fonti va riscritta da zero quando arrivono, non ritoccata"), la scheda è stata **riscritta integralmente**, non ritoccata.

**Discrepanza trovata e risolta:** età. Prima versione: 34 (invenzione, nessuna fonte lo specificava a quel punto). Fonte primaria arrivata dopo: 32, esplicito. Corretta usando il valore della fonte primaria, come da gerarchia §11. Data di nascita ricalcolata: 23 novembre 1991 (`birthdate`/`start_timeline_position` 10203456), sostituendo la precedente (30 gennaio 1990).

**Backstory sostituita per intero:** la versione inventata ("poco si sa del suo passato, Alistair non ha mai chiesto, storia di servizio leale nel tempo") è stata scartata e sostituita con quella reale della fonte primaria: nato da una femmina alligatore demiumana tenuta in cattività da un giro di traffico di animali esotici, madre morta quando era piccolo, padre mai conosciuto, addestrato come enforcer/mercenario da giovane per la forza fisica fuori norma, tour con PMC in zone di guerra (probabile PTSD mai riconosciuto), assunto da Alistair dopo avergli salvato la vita a un'asta durante l'attacco di un'idra fuggita dal contenimento. Analfabeta, in autoapprendimento privato.

**Aspetto fisico arricchito e corretto:** altezza/peso esatti (6'7", 280 lbs, contro un generico "alto e muscoloso" prima), naso romano pronunciato, arcata sopraccigliare marcata, cicatrice vistosa sulla gola, scaglie che fungono da armatura leggera contro lame e proiettili di piccolo calibro.

**Intimacy Profile aggiunto** (mancava nella prima stesura, la fonte precedente non ne forniva base): registro prosa, evita l'intimità emotiva, usa occasionalmente professionisti pagati, turn-on per forza/aggressività, coda toccata, morsi, dirty talk, corpi morbidi, sesso in acqua, turn-off per pianto/supplica/bisogno d'affetto, dominante e primordiale nell'atto (graffi, morsi, immobilizzazione con la coda usata anche per la penetrazione), aftercare scarso (a volte si limita a leccare i graffi lasciati). Nessun contenuto problematico, nessun riferimento a `{{user}}`. Lexicon `_KHR33NmNG7azGdbAThTxp`.

**Outfit e Dialogue Examples riscritti** per riflettere i dettagli concreti della fonte primaria (basking al sole, sigari, arsenal, il suo passato taciuto). Attitudes esistenti (verso Alistair, Amelia, Charles, Alyssa, Jasper) non toccate, restano valide con la nuova versione del personaggio.

Verificato con GET fresca dopo la riscrittura: zero `{{user}}`, zero em-dash, zero grassetto, birthdate/start coincidenti a 10203456, outfit_count 5, speech_examples_count 5, attitudes_count 5 (invariate), is_global true.
