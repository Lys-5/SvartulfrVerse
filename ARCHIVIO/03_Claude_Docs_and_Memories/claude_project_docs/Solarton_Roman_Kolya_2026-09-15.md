# Solarton — Roman Blackwood e Kolya Varenkov (2026-09-15)

Coppia di schede nuove, dominio SUCC (autore esterno, io wuvs soap), inserite nel locale Wyldfire. World a 124 personaggi dopo l'inserimento (122 → 124).

- **Roman Blackwood**, id locale `qOzvwbH1EysIS7o_A-ijS` — demi-umano lupo, 23 anni, studente MBA alla SUCC per obbligo familiare, vera passione per MMA e incontri clandestini.
- **Kolya Varenkov**, id locale `qIQ0NO_7eAUl9oxzYgC5w` — vampiro, 24 anni, dottorando in diritto sovrannaturale alla SUCC, squadra MMA, neurodivergente.
- Intimacy Profile separati per entrambi (`RXpxarW94imqwo_gXpaGR` per Roman, `QdYUm_FPIthxfn62f4OgD` per Kolya).

## Nota sul cognome "Blackwood"

La fonte chiama il personaggio "Roman Blackwood". Blackwood City è il dominio di Lys (famiglia/branco Douglas), ma questo Roman è un personaggio SUCC ambientato a Solarton, senza alcun legame con la famiglia Douglas o con Blackwood City: coincidenza di cognome nella fonte originale, non un aggancio narrativo. Mantenuto come da fonte (nessuna autorizzazione a modificare senza indicazione), ma segnalato qui per evitare che in futuro qualcuno lo scambi per un membro della famiglia Douglas-Blackwood o gli assegni per errore agganci con quel branco.

## Cosa dice la fonte

Due card in inglese del roster SUCC: Roman ha una cotta dichiarata su `{{user}}`, respinta da `{{user}}`, letta dal suo istinto da lupo come "riconoscimento del compagno destinato". Kolya si innamora a prima vista di `{{user}}`, ha come obiettivo dichiarato di corteggiarla e renderla la sua ragazza (legge un libro di consigli per appuntamenti a questo scopo), e ha una sezione Secret imperniata sulla paura di non essere "abbastanza normale" per lei. Entrambe le schede includono sezioni sessuali esplicite con misure anatomiche e kink dettagliati.

## Cosa abbiamo scritto

**Purga standard §13** (non estensione 14/09: nessun contenuto di tratta, sfruttamento o non-consenso, solo archi romantici fissi su `{{user}}`):

- **Roman**: rimossa la cotta per `{{user}}`, il rifiuto subito e il riconoscimento del "compagno destinato". L'istinto da lupo verso un possibile partner resta come tratto generico non risolto ("For all the swagger, Roman has never actually been in a real relationship, and the idea of one terrifies him"), riusabile per futuri agganci narrativi senza puntare a nessun personaggio specifico.
- **Kolya**: rimosso l'obiettivo di corteggiamento verso `{{user}}`, il libro di consigli per appuntamenti, l'innamoramento a prima vista. Il Secret è stato generalizzato in una paura di fondo sul non essere "abbastanza" per un futuro partner qualsiasi, senza destinatario fisso.
- **Blocchi anatomici/kink** spostati integralmente nei rispettivi Intimacy Profile (formato in prosa, senza misure numeriche esplicite), coerente con lo stile Dominic Rogers. Per Kolya, la sua preferenza per il rapporto senza barriera è stata riscritta come vincolata esplicitamente a una relazione stabile ed esclusiva, non come default verso chiunque (la fonte lo motivava con "è {{user}}, non una qualunque", frase incompatibile con un `{{user}}` non fisso in questo World).
- **Misoginia involontaria di Roman**: mantenuta come tratto di personalità leggero (fonte esplicita: "unintentionally misogynistic", mai malevolo), non è contenuto da espellere, è caratterizzazione.

**Attitudes**: oltre alle due obbligatorie Alyssa/Jasper (`stranger`, intensity 15, mai incontrati), aggiunta la relazione reciproca Roman↔Kolya come `best_friend`/intensity 85 su entrambe le schede (compagni di squadra MMA e migliori amici, confermato da entrambe le fonti).

RPG Stats lasciate `NULL` (sistema in pausa, §8). Start Position = birthdate su entrambi (vivi, nessuna End Position). Età reali scelte per calzare con le età dichiarate nella fonte (23 e 24) rispetto al world_age corrente (5 aprile 2024): Roman nato 8 novembre 2000, Kolya nato 22 agosto 1999, date scelte variate come da convenzione §9.6.

## Verifica

`PRAGMA integrity_check` ok, conteggio World 124/124, zero `{{user}}`, zero em-dash, zero grassetto markdown su tutte e quattro le righe (2 character + 2 lexicon entry), Attitudes risolte correttamente per id locale (compresa la coppia reciproca Roman/Kolya), `attached_world_character_id` di entrambi i lexicon entry allineato all'id locale del rispettivo personaggio, nessuna collisione di chiavi con schede esistenti. Scritto sul dispositivo dopo conferma che Wyldfire fosse chiuso, nessun file `-wal`/`-shm` residuo trovato dopo la scrittura.
