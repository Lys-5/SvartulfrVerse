# Grave Mistake: le quattro schede, decisioni e discrepanze

Lavorate il 2026-09-07 in un blocco unico, perché le quattro schede si
definiscono a vicenda. Tutte e quattro erano import grezzi: `summary` conteneva
il blocco della fonte incollato tale e quale, `long_summary` era vuoto, zero
outfit, zero dialoghi, zero attitudes, niente RPG, niente Start Position.

| | ID | Livello | Specie | Occupazione |
|---|---|---|---|---|
| Fade Greymoor | `_93KXYePUrXYrMPWnkDVLx` | 24 | Vampire | Student |
| Mackenzie Sanchez-Rogers | `_rm9PkkbWEc1zNJAUNUp6U` | 24 | Weres/Shapeshifters | Musician |
| Roland Vickers | `_QdB3BNtd3X6Dzrb196PXy` | 23 | Undead | Student |
| Viola Carter | `_H84mBnGcVWwX6DFCqY6f2` | 22 | Fae | Student |

Date di nascita inventate, varie (§9.6): Fade 23 ottobre 1999, Mac 17 agosto
1999, Roland 14 giugno 2000, Via 30 settembre 2001. Start Position uguale alla
birthdate su tutti e quattro, nessuna oltre `world_age`.

Creati nello stesso passaggio:

- Lexicon **Grave Mistake** `_6dxKb4CE4rPNra23WwYTB`, globale, chiavi
  `Grave Mistake` e `Grave Mistakes`.
- Location **The Open Casket** `_1PX31CB2BfMhBxzTJzENQ`, Environment Solarton.
- Occupazione RPG **Musician** `_FnwYGq4VdHYLXyM3FcjpM`, modificatore `stat_5 +1`
  (Presence), collegata alla entry Lexicon della band.
- Tre **Intimacy Profile** (sotto).
- Scenario **"Ciao, Sono Logan"** `_EyeRqnmmcc89mewWEMVLp`, documentato a parte
  in `claude/Scenario_Ciao_Sono_Logan.md`.

---

## Fonti usate

Sette varianti fornite dall'utente (tre di Fade, due di Mac, due di Roland),
autori `veseii` e `Iorveths` su janitorai, più il lorebook ufficiale
`SUCC_-_U_-_VERSE.json` e il portale personaggi. Ordine di forza applicato
secondo §11: lorebook e portale battono le card di terzi ovunque si
contraddicano.

**Via non era un personaggio abbozzato.** Ha una entry completa nel lorebook
ufficiale, con aspetto, likes, personalità, archetipo, backstory e dialoghi. La
convinzione che fosse "solo accennata" era sbagliata: mancava la scheda, non il
materiale. Lo stesso vale per **Luisa Sanchez-Rogers** e **Allegra Lumsden**, che
sono entrambe entry ufficiali del lorebook e non estensioni nostre.

---

## Discrepanze risolte

**Il padre di Mac non è Dominic Rogers.** Errore registrato per sbaglio nel doc
del portale e ora corretto lì. Dominic Rogers è un incubus della Louisiana,
marito di Lara e padre di Bailey, e non ha alcun rapporto con la famiglia
Sanchez. Il padre biologico di Mac è un licantropo senza nome che ha lasciato
Andrea Sanchez per quella che ha chiamato la propria true mate, ed è la ferita
centrale del personaggio. Il cognome condiviso con Bailey è una coincidenza che
il canon segnala esplicitamente ("no relation"), e Mac ci scherza sopra di
continuo: è scritto come Attitude verso Bailey a tier Acknowledged.

**Viola contro Violet.** Il lorebook scrive `Violet "Via" Carter` nel contenuto e
`Viola "Via" Carter` nel commento; le card di terzi dicono Viola; il World diceva
Viola. Tre fonti su quattro: **Viola**.

**Capelli di Mac.** Una variante dice "shaggy brown", tutte le altre e il
lorebook dicono "shaggy dirty-blond". Vince biondo sporco.

**Bailey quarterback.** La card di Mac lo chiama "incubus quarterback". Portale e
lorebook lo danno offensive lineman, e il quarterback titolare è Jared Thompson.
La battuta è stata riscritta senza il ruolo.

**Grave Mistake contro Grave Mistakes.** Il portale oscilla. Scelta la forma
singolare, ed è scritto nella entry Lexicon che l'altra è sbagliata.

---

## Mac: l'alpha copiato

Decisione dell'utente, arrivata mentre si sistemava lo scenario, e vale come
chiave di lettura di tutto il personaggio.

Le fonti scrivono Mac con un registro interno da predatore: caccia, bersaglio da
acquisire, l'odore che scavalca la parte del cervello che ragiona. Quel registro
è stato tolto, e non solo per il bersaglio: **è caratterizzazione sbagliata in
partenza.** Mac non ha un istinto da esprimere. Ha un'idea di lupo alpha copiata
da fuori, senza niente sotto, perché l'unico che gliel'avrebbe insegnata se n'è
andato quando lui aveva nove anni. Niente branco, nessuna tradizione, nessun
rito, nessun maschio adulto che gli abbia mostrato a cosa serva niente di tutto
questo.

E qui la cosa si chiude su se stessa: **rifiutare le tradizioni e i mate bond a
voce altissima è comodo.** Se sono tutte fandonie, allora nessuno ha mancato di
insegnargliele. Quindi si costruisce la parte con quello che ha a disposizione,
cioè volume, stazza, appetito e la spavalderia di uno che gli alpha li ha visti
sugli schermi e nei bar e mai una volta dentro una casa. È un costume e non gli
sta bene. È al suo peggio mentre lo indossa, petto in fuori e voce abbassata di
un'ottava, ed è al suo meglio quando si dimentica di averlo addosso, cioè quasi
tutto il tempo che passa con Fade, con sua madre e con Luisa.

Scritto nella scheda come sezione `THE ALPHA HE IS COPYING`, e ripreso nelle
`final_instructions` con l'istruzione esplicita di non scriverlo mai come
predatore naturale né come uno che agisce d'istinto: è uno che fa
un'imitazione, e la coda lo tradisce prima che parli.

---

## Epurazione §13

Le sette varianti sono card romantiche o esplicite costruite attorno a
`{{user}}`. Rimosso integralmente:

- Fade come partner di `{{user}}`, comprese le scene delle groupie che insultano
  il partner, la devozione dichiarata, i vezzeggiativi e il fatto che si nutra
  solo da `{{user}}`. Sostituito con: si nutre solo dove è stato offerto e
  discusso prima.
- Mac come friends with benefits di `{{user}}`, e per intero il primo messaggio
  in cui si presenta ubriaco e arrapato alla porta del giocatore.
- Roland come partner di `{{user}}`, la gelosia ossessiva, la convinzione di
  essere tradito e il fatto che provochi il partner per "testarlo".
- I blocchi anatomici e di kink dalle description (§13.3), spostati negli
  Intimacy Profile separati.

Verificato dopo reload completo: zero occorrenze di `{{user}}` su tutte e
quattro.

---

## Roland: come è stato trattato il retroscena della morte

Il fatto che sia morto suicida a ventuno anni **resta**, scritto una volta, senza
metodo. Non è un dettaglio ornamentale: è la ragione per cui è stato rianimato
illegalmente, per cui ha lo status legale di undead, per cui ha la borsa di
studio e per cui odia essere immortale. Toglierlo avrebbe reso il personaggio
incomprensibile.

**Non è stata riportata l'ideazione suicidaria come tratto attivo.** La fonte la
elenca fra le note del personaggio, cioè come qualcosa che il modello dovrebbe
interpretare in scena. Al suo posto le `final_instructions` dicono
esplicitamente di non scriverlo mentre progetta, cerca o minaccia la propria
morte, e di rendere la stessa verità emotiva come stanchezza, rancore per essere
stato riportato indietro senza che nessuno chiedesse, e rifiuto di essere grato.
Il personaggio regge benissimo così.

Le sue posizioni misogine restano, perché sono caratterizzazione e perché la
scheda le inquadra: sono recenti, importate dai forum dopo la morte, e non
appartenevano al Roland vivo. Le `final_instructions` chiedono che la stanza
reagisca, e Fade ha un Dialogue Example che lo zittisce.

---

## Gli Intimacy Profile

Tre entry Lexicon, globali, `constant: false`, `type: memory`, con
`party_conditions` `has_any` sul proprietario, chiavi primarie sugli
identificatori della persona e secondarie sulle parole dell'argomento, secondo
§7.

| Entry | ID |
|---|---|
| Intimacy Profile - Fade Greymoor | `_k39WPeQqXtwtT8UznGxmU` |
| Intimacy Profile - Mac Sanchez-Rogers | `_NBk6c2YtpxzHGNgDGjY7j` |
| Intimacy Profile - Roland Vickers | `_FhYb6fA4jcPeGNx6aqfqV` |

**Attenzione al nome:** le undici entry preesistenti si chiamano
`Intimacy Profile — <nome>` con l'em-dash, che viola §3. Le tre nuove usano il
trattino semplice. La lista risulta quindi disomogenea finché non si rinominano
le vecchie: è una coda da fare in un passaggio solo, insieme al backlog dei
trentotto em-dash sparsi sulle altre schede.

Contenuto: sono profili di comportamento, non prosa. Quello di Fade è per metà
una istruzione su come scriverlo con rispetto, cioè stesso linguaggio che in
qualunque altra scena, nessun eufemismo, nessuna scena che tratti il suo corpo
come una rivelazione. Quello di Mac dichiara esplicitamente che la sua
sconsideratezza è un difetto del personaggio e va letta come tale. Quello di
Roland mette al centro il fatto che si aspetta disgusto e arriva primo con la
battuta.

---

## Nota di lingua

The Open Casket è scritta in inglese, come le quattro schede. Sidewinders Bar &
Nightclub, la Location più vicina per tipo, ha invece la description in italiano,
e così lo scenario. Il World è misto e prima o poi va uniformato: il testo che il
modello legge dovrebbe stare in una lingua sola.

---

## Cosa manca ancora

1. Rinominare le undici Intimacy Profile vecchie per togliere l'em-dash, e
   togliere il grassetto markdown dalla scena di "First College Day".
2. Uniformare la lingua delle Location di Solarton.

---

## Diagnosi aggiornata del bug relationship trees

Accantonato per scelta dell'utente il 2026-09-07: controllerà a mano. La
diagnosi resta qui per quando ci si torna.

- La route **è** `GET /api/worlds/linked-characters/<world_id>`, e quel parametro
  è il World, non un id di collegamento: passandogli un id di record risponde
  `500 World not found`. La variante a schema `.../linked-characters/world/<id>`
  non esiste, risponde 404.
- Con il World giusto risponde **500 Maximum call stack size exceeded**.
- Il World contiene **solo due record** in `linked_characters`
  (`_DjD4pN17jjdtTaXy7mY4U` e `_KAw6hD2MwqGxAM7ab6yaL`). Due soli record che
  fanno esplodere lo stack indicano quasi certamente un **ciclo** fra loro,
  cioè A punta a B che punta ad A.
- **Quei due record non sono leggibili in nessun modo.** Provate sette varianti
  di route per il singolo (`linked-character/<id>`, `.../single/`, `.../entry/`,
  `.../id/`, `linked_characters/`, senza il prefisso `worlds`, e annidata sotto
  il World): tutte 404. Non esiste nemmeno una route di export del World
  (`/export`, `/full`: 404). L'unica via di lettura è la lista, che è quella
  rotta.

Quindi non si può sapere cosa contengono prima di cancellarli, e la DELETE non è
sicura perché la stessa route usa il path param come world_id.
