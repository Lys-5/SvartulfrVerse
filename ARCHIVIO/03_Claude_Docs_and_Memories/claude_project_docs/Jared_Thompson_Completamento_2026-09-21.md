# Jared Thompson — Completamento scheda (2026-09-21)

## Dominio

Jared Thompson **non è un personaggio Douglas/Blackwood**: è un personaggio SUCC/Solarton (quarterback dei SUCC Bulls, half-minotaur). Scoperto durante la ricognizione dei prossimi nomi nella coda di priorità ("Jared Thompson" e "Mac"), che si sono rivelati entrambi personaggi del campus SUCC, non membri di pack/famiglia Douglas.

Conclusione operativa: la coda di priorità ereditata dalla sessione precedente ("continua con gli altri npc di pack e family") è in pratica una coda più ampia di "schede corrotte da riparare", non ristretta al sangue Douglas. La pipeline di riparazione (§14) è identica indipendentemente dal dominio, quindi si è proceduto allo stesso modo, segnalando qui la distinzione di dominio per chiarezza. Per §10, il materiale SUCC è governo del proprio dominio: nessuna regola Blackwood-specifica (family look Douglas, ecc.) si applica a Jared.

## Corruzione riscontrata (4° caso confermato dello stesso pattern)

Stesso pattern già visto su Wulfnic, Kaladin: Display Description e Long Description vuote (placeholder di default Wyvern, variante "Margret Alaina Thames"/"DeTamble's Disease"), con l'intero blocco JED+ (long_summary) + la nota format-discipline di final_instructions riversati nel campo Short Description (6966 caratteri = 6757 + 191 + separatore).

**Fix**: i tre campi ripristinati direttamente dal database di riferimento SQLite tramite payload JSON base64 iniettato via JS (bypassando qualunque tentativo di parsing del testo corrotto in pagina). Verificato via lunghezza esatta dei tre campi: Display 151, Long 6757, Short 872 caratteri.

## Altri problemi corretti

- **Nome non diviso**: First Name conteneva "Jared Thompson", Last Name vuoto. Corretto: First Name "Jared", Last Name "Thompson".
- **Nicknames/Titles mancanti**: aggiunti "J-Man" e "Jare" come nickname (chip separati, via pattern digita+click "+"), "Quarterback" come title.
- **Tags e Secondary Keys**: vuoti sia in scheda live che in riferimento, nessuna correzione necessaria. **Primary Keys**: già corrispondenti al riferimento (Jared, Jared Thompson, SUCC Bulls, JT, J-Man), caso raro in cui questo campo dell'import corrotto non era stato danneggiato.
- **Timeline vuota**: Start Position e Birthdate entrambi mancanti sulla scheda live nonostante i valori esistessero nel riferimento (10287000 per entrambi). Corretti impostando Start Position via input diretto e Birthdate tramite JS native setter (bypassando proattivamente il bug ctrl+a noto da Kaladin) — nessun artefatto "zero iniziale" osservato nemmeno prima del reload.
- **Pronomi placeholder-non-valore**: stessa trappola vista su Wulfnic/Kaladin. Risolta con lookup via label esatta + JS native setter per tutti e 5 i sotto-campi (he/him/his/his/himself).
- **Contatore "How many examples to show" errato**: preimpostato a 3 invece di 5 (3° caso confermato dello stesso pattern di corruzione, dopo Wulfnic e Kaladin). Corretto a 5 via `document.activeElement` + native setter.
- **Zero Outfit presenti**: nonostante 7 pronti nel riferimento. Aggiunti tutti e 7 uno alla volta con salvataggio individuale e verifica di persistenza tra un outfit e l'altro (nessuna perdita di dati osservata): Game Day, Campus Default, BRO Party, The Dorm, Home in Solarton, Halloween, Beach.
- **Default Outfit non impostato**: impostato su "Campus Default" (il dropdown, popolato con tutti e 7 i nomi, ha confermato che tutti gli outfit erano davvero persistiti).

## Dialogue Examples (5, con disciplina di formattazione §3)

1. **Greeting** — presentato a qualcuno di nuovo, stretta di mano troppo forte, si presenta come "J-Man".
2. **Forgets his own strength** — applaude qualcuno festeggiando e rompe una porta senza accorgersene.
3. **The tail** — trash-talking pre-partita, la coda che si muove eccitata tradisce quando il colpo dell'avversario va a segno, lui continua a sorridere senza accorgersene.
4. **The roommate** — qualcuno nota che il coinquilino lo evita, lui minimizza troppo in fretta.
5. **Called an animal** — insultato come "animale stupido" durante un litigio, il sorriso non si muove ma cambia argomento subito dopo, senza aver davvero risposto.

## Attitudes (5, secondo §16)

| Target | Tier | Intensity | Motivazione |
|---|---|---|---|
| Hank Thompson (padre) | Close Friend | 70 | Il padre, e lo standard a cui si misura senza mai dirlo. |
| Janice Thompson (sorella) | Close Friend | 68 | La sorella, una delle poche persone che vede oltre la stazza e il rumore. |
| Stanley Davies Jr. (coinquilino) | Acquaintance | 45 | Il coinquilino, che disapprova tutto ciò che fa Jared e comunque gli presta le cose. |
| Alyssa Douglas Bloodmoon | Stranger | 15 | Non si sono mai incontrati (requisito minimo §16, non essendo personaggio Douglas non ha altri agganci con lei). |
| Jasper Douglas Bloodmoon | Stranger | 15 | Non si sono mai incontrati (requisito minimo §16). |

Nessuna correzione di tier `romantic_interest` necessaria: tutti i valori nel riferimento erano già corretti (a differenza del pattern Wulfnic/Noah/Logan).

Nota interpretativa aperta, ora risolta empiricamente: il riferimento SQLite per un personaggio SUCC includeva comunque Alyssa e Jasper come Stranger a intensità 15, quindi il requisito minimo §16 si applica anche a personaggi fuori dal dominio Douglas, e i dati di riferimento lo confermano.

## Global Character

Impostato ON (era OFF sulla scheda live nonostante `is_global: 1` nel riferimento). Salvato e verificato persistente dopo reload.

## Verifica finale (§14.12, dopo reload completo)

- Zero occorrenze di `{{user}}`, em-dash, asterischi singoli, grassetto markdown in tutti i campi testo/textarea della pagina (controllo programmatico via JS).
- Nome diviso correttamente (Jared / Thompson), Nicknames (J-Man, Jare) e Titles (Quarterback) persistenti come chip separati.
- Tags e Secondary Keys vuoti per convenzione di riferimento (nessuna azione richiesta).
- Timeline: Start Position e Birthdate entrambi 10287000, coincidenti, ≤ world_age (10486470).
- Pronomi: tutti e 5 i sotto-campi corretti (he/him/his/his/himself).
- 7 Outfit presenti e persistenti, Default Outfit = Campus Default.
- Dialogue Examples: 5 presenti, contatore "how many to show" = 5.
- Attitudes: 5 presenti (Hank, Janice, Stanley, Alyssa, Jasper) con tier/intensity/reasoning corretti.
- Global Character: ON.

Scheda considerata completa. Nono personaggio completato nel progetto (dopo Erik, Jasper, Alyssa, Malachia, Noah, Logan, Wulfnic, Kaladin).

## Prossimo passo

Procedere con **Mac** (Mackenzie Sanchez-Rogers, personaggio SUCC, tastierista), seguendo la stessa pipeline diagnosi-contro-DB-locale poi fix-sul-sito-live ormai collaudata su nove schede.
