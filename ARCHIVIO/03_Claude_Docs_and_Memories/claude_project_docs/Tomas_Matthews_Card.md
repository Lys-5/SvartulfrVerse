# Tomas Matthews — scheda completata

Fonte: card di `Iorveths` (janitorai.com). A differenza di Santiago, questa card **non era un import grezzo**: `long_summary`, `summary`, `titles` e `keys` erano già scritti in JED+ da una sessione precedente, con `{{user}}` e il contenuto sotto già esclusi. Questa sessione ha completato la pipeline (§14) dove mancava: outfit, Start Position (già presente), RPG, Dialogue Examples, Attitudes, e ha aggiunto `display_description` e `nicknames`, prima vuoti. Un secondo passaggio, su richiesta esplicita dell'utente, ha poi reintegrato una versione riscritta del materiale sulla condivisione non consensuale (vedi sotto).

**Stato finale (verificato dopo reload completo):**

| Campo | Valore |
|---|---|
| display_name | Tomas Matthews |
| Nicknames | Tee, Tommy |
| Titolo | Sports Science Student, Mu Alpha Nu Fraternity (già presente) |
| long_summary (JED+) | 3.450 caratteri |
| Outfit | 5: The Gym, Frat House, Tailgate, Home in Texas, Class |
| Default Outfit | Frat House |
| Dialogue Examples | 5: Meeting someone new, Losing to a supernatural player, Calling home, Being called out, **What his mother calls him** |
| Start Position / Birthdate | 10302288 = 2 aprile 2003 (già presente, non toccata) |
| RPG | Lv.21, Human / Student, MGT 8 / RES 7 / AGI 5 / WIT 3 / PRS 6 / SCT 2 (25/25) |
| Attitudes | 5 (vedi sotto) |
| Global Character | ON (era già ON) |

Verifica finale: zero `{{user}}`, zero em-dash, zero asterischi/markdown.

## Decisione editoriale sul materiale sorgente, e come è stata rivista

Questa fonte era diversa dai casi normali di "cotta rivolta a `{{user}}`". La card sorgente costruiva l'intero personaggio attorno a una scommessa con l'amico Rhodes Adams (200$ per "datare un freak" senza rompere il personaggio), con registrazioni intime fatte di nascosto e mostrate ai fratelli della confraternita senza consenso, oltre a un blocco Intimacy esplicito con linguaggio degradante.

**Primo passaggio (mio, non richiesto dall'utente):** ho scelto di non portare nel World nessuna parte di questo materiale, in nessuna forma, giudicandolo un meccanismo di coercizione sessuale specificamente centrato sulla vittimizzazione di chiunque giocasse `{{user}}`, non genericizzabile come una normale cotta.

**Secondo passaggio, su indicazione esplicita dell'utente:** l'utente ha chiesto di reintegrare l'ideologia Human First e la tendenza aggressiva in modo più marcato, e di inserire la condivisione di contenuti intimi non come scena con una vittima specifica, ma come **attività goliardica generalizzata della confraternita**, cioè una chat di gruppo dove i fratelli si scambiano foto e video di partner passati come vanteria. In questa forma la richiesta risolve esattamente il problema del primo passaggio: nessuna vittima nominata, nessun legame con `{{user}}`, nessuna scena esplicita o coreografia di un atto, e soprattutto **nessun comportamento scriptato**. La scheda dice che Tomas partecipa alla chat e ci ha messo cose sue in passato, ma dice esplicitamente che se lo rifarebbe, e a chi, "non è deciso in anticipo", lasciando la scelta al momento del gioco piuttosto che imporla come evento fisso. Ho scritto la sezione (THE GROUP CHAT, in coda al long_summary) legando esplicitamente questo comportamento alla stessa radice ideologica del suo specismo, "i soprannaturali non hanno diritto all'equità, i partner non hanno diritto alla privacy, vengono dallo stesso posto", così la scelta di scrittura regge tematicamente e non resta un dettaglio isolato.

In più, su richiesta, la sezione VOICE & BEHAVIOR ora dice esplicitamente che la sua aggressività non è solo posa: ha tirato pugni veri per insulti percepiti e partite perse, e la confraternita lo ha coperto più volte.

**Cosa resta fuori anche in questa versione:** nessuna descrizione di contenuto esplicito o di un atto specifico, nessun nome di vittima, nessuna scena. Il confine tenuto è: caratterizzazione e contesto sociale sì, coreografia esplicita di un atto di coercizione no.

**Non creato** un personaggio separato per Rhodes Adams (il migliore amico), citato solo nel testo se necessario in futuro: non è ancora giustificato costruire una scheda per lui, coerente con §9.4.

## Attitudes, con motivazione

| Target | Tipo | Tier | Intensity | Perché |
|---|---|---|---|---|
| Alyssa Douglas Bloodmoon | World Character | stranger (Unknown Scent) | 15 | Non si sono mai incontrati |
| Jasper Douglas Bloodmoon | World Character | stranger (Unknown Scent) | 15 | Non si sono mai incontrati |
| Il padre e il giro Humans First | Generic | close_friend | 75 | L'approvazione che insegue ancora a distanza |
| Studenti soprannaturali e i SUCC Bulls | Generic | despised | 55 | Ha bisogno che il loro successo sia un imbroglio, l'alternativa è che siano semplicemente più bravi |
| I fratelli di Mu Alpha Nu | Generic | close_friend | 60 | Il suo in-group, dove nessuna delle sue idee viene mai messa alla prova |

## RPG, perché queste stat

MGT 8 e AGI 5 perché era davvero un atleta forte al liceo, non un millantatore puro. RES 7, fisico resistente. WIT 3, non stupido, solo trincerato e ostile alla lettura, leggermente sopra il livello "himbo" di Jared o Barkley perché la scheda lo scrive come uno che capisce esattamente cosa sta facendo quando sceglie di non guardarsi allo specchio. PRS 6 per il carisma da confraternita. SCT 2, il più basso: è umano, non ha nulla dell'asse Scent che conta per i soprannaturali, ed è tematicamente coerente con la sua intera insicurezza. Species Human e Occupation Student assegnati via API dentro `rpg_stats`.
