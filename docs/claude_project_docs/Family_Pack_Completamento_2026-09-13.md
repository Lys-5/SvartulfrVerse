# Family e Pack — completamento dati mancanti (2026-09-13)

Seguito diretto di `Stato_Family_Pack_Solarton_2026-09-13.md`, su istruzione esplicita dell'utente.

## Wulfnic Bloodmoon — nessuna scrittura necessaria

L'utente ha chiesto di impostare la data di nascita al 21 dicembre 827 d.C. Verificato che **Wulfnic aveva già `birthdate: 0` e `start_timeline_position: 0`**, cioè esattamente quel giorno (0 = epoca del World). Il mio controllo di stato precedente lo segnalava come "senza birthdate" per un bug nel mio script di analisi: `!c.birthdate` tratta lo 0 come falsy in JavaScript, quindi un personaggio nato esattamente all'epoca del World risultava un falso positivo. Corretto qui, nessuna azione necessaria sulla scheda.

## Lord Cornelius Douglas (`_bK4LXdgq89yLJDFea9FqE`... verificare id esatto in scheda)

**Dialogue Examples**: 5, scritti in voce da nobile inglese del XVII secolo, governatore coloniale. Il `long_summary` di Cornelius dichiara esplicitamente che il suo modo di fare personale non è documentato ("what is known comes from the institutions he left behind"): i cinque esempi restano quindi su un registro archetipico coerente con quanto la scheda stessa attesta (metodico, autoritario, a proprio agio nelle strutture di potere umane), senza inventare dettagli personali non supportati dal testo. Temi coperti: ricevere un supplicante da governatore, fondare la Douglas Commercial Company davanti agli investitori, il peso privato di essere il secondogenito con un fratello destinato al ducato, l'annuncio formale del nome del primogenito Magnus III, l'autorità metodica e fredda verso un subordinato inadempiente.

**RPG Stats**: abilitate da zero (prima non lo erano, unico caso nella cartella Family con questo doppio buco). Specie: Weres/Shapeshifters (Pureblood werewolf). Occupation: Patriarch (corrisponde al titolo già scritto in scheda, "Patriarch of House Douglas"). Livello: **99**, non l'età reale (225 anni alla morte), per la convenzione di progetto sui centenari e per il bug di piattaforma confermato che fa fallire in silenzio il blocco RPG oltre Livello ~100. Punti distribuiti sul budget di 25 (totale 31): MGT 5, RES 5, AGI 3, WIT 7, PRS 8, SCT 3, pesati su un personaggio-mente più che su un guerriero puro (fondatore di una compagnia commerciale, governatore, capo di casata).

## Pack (4 schede)

**Marcus Thornfield, Ut Berg, Zefir Hvitskog**: 5 Dialogue Examples ciascuno, scritti dal `long_summary` già esistente (letto integralmente prima di scrivere).
- Marcus: l'umorismo secco come muro, lo scatto in modalità operativa con gli occhi che diventano rossi, la lettura istintiva di una stanza, la protezione silenziosa verso Kaladin, la deviazione elegante quando qualcuno chiede di Project Blackwolf.
- Ut Berg: l'accoglienza fisica e rumorosa di un nuovo membro, la paura di fallire nel proteggere Wulfnic detta con voce semplice, il tabù di rifiutare un drink, il disagio istintivo e inarticolato verso "quelli che puzzano sbagliato" incontrati al funerale di Nixara, l'accoglienza a Kaladin.
- Zefir: risposte deliberatamente brevissime e taglienti, coerenti con la sua voce già scritta in scheda ("extremely brief, single sharp sentences"). Il silenzio come risposta a un complimento, la preda lasciata come lettera d'amore muta, il calo di temperatura nella stanza quando è irritato, la correzione silenziosa di chi lo scambia per un ragazzino vista la sua età apparente.

**Kaladin Nargathon**: lasciato a 3 Dialogue Examples, non toccato. Non era fra le lacune segnalate (aveva già dialoghi, solo non il numero standard di 5), e l'utente ha chiesto di completare i dati mancanti, non di normalizzare quelli parziali. Da valutare in futuro se portarlo a 5 come gli altri tre.

**Species/Occupation per tutti e 4** (mancavano su tutta la cartella):
- Kaladin Nargathon: Weres/Shapeshifters, Security Commander (corrisponde al suo titolo in scheda, "Commander, DCC Security Division").
- Marcus Thornfield: Weres/Shapeshifters, Bodyguard (ruolo subordinato di sicurezza sul campo, "Field Lead" sotto Kaladin).
- Ut Berg: Primordial, Divine Guardian (Firstborn a Sangue Divino, Right Hand di Wulfnic).
- Zefir Hvitskog: Primordial, Divine Guardian (stesso ragionamento, Left Hand di Wulfnic).

## Verifica

Tutto verificato dopo reload completo: Dialogue Examples e RPG Stats persistiti su Cornelius, Marcus, Ut Berg, Zefir; Species/Occupation persistiti su tutti e 4 i membri del Pack; zero em-dash, zero `{{user}}`, zero grassetto su tutto il contenuto scritto in questo passaggio.

## Non toccato

Il Livello RPG anomalo di Ut Berg (1201) e Zefir (1019), già segnalato nella rilevazione di stato, non è stato modificato in questo passaggio: l'utente non l'ha richiesto esplicitamente, e la correzione (portarli a 99 come da convenzione) comporterebbe probabilmente una ridistribuzione dei punti stat, quindi va decisa a parte.
