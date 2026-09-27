# Kaladin Nargathon — Completamento scheda (2026-09-21)

Ottavo personaggio della priorità core family/pack completato in questa sessione (dopo Erik, Jasper, Alyssa, Malachia, Noah, Logan, Wulfnic). Ricostruito interamente sul sito Wyvern via browser automation (mai via app Wyldfire locale), a partire dai dati puliti della SQLite di riferimento (`live_delete2.db`, id `e8vYwNcluNcGPRNMIN8SL`).

## Stato di partenza (corrotto)

Stesso pattern di corruzione già osservato su Wulfnic, confermato ora come ricorrente su almeno 2 schede consecutive:

- **Display Description e Long Description vuote**, che mostravano il placeholder di default di Wyvern (l'esempio "Margret Alaina Thames").
- **L'intero blocco JED+ `long_summary`, con in coda la nota "Format discipline..." (final_instructions) erroneamente appesa**, scaricato per intero nel campo Short Description (15731 caratteri, terminante con una parentesi quadra spuria "...instead.]").
- Nome non splittato, zero Nickname/Titoli/Tag, zero Outfit, Timeline non impostata, Pronomi solo apparenti (placeholder grigio, non valori reali), contatore Dialogue Examples pre-impostato a 3 invece di 5, zero Attitudes.
- **Un campo non era stato corrotto**: le `secondary_keys` sulla scheda live corrispondevano già esattamente al riferimento (Commander, Nargathon, Villa Douglas, PMC, Major, S.R.F., Gamma-7, Marcus). Caso isolato di un campo dell'import grezzo rimasto intatto.

## Fix applicati

**Description fields**: invece di provare a fare il parsing del testo corrotto (inaffidabile per la parentesi quadra spuria finale, a differenza di Wulfnic dove il troncamento a "Format discipline" aveva funzionato), i tre campi puliti (display_description 301 caratteri, long_summary 14772 caratteri, summary/short 1435 caratteri) sono stati scritti direttamente via un payload JSON codificato in base64 ed eseguito con `javascript_tool`, bypassando qualunque tentativo di split del testo corrotto. Confermato via lunghezze di ritorno esatte e successiva ispezione visiva.

**Nome**: splittato in First Name "Kaladin" / Last Name "Nargathon".

**Nickname (4) e Titoli (2)**: scoperto un bug nuovo, il tasto Invio dopo aver digitato un valore nel campo Nicknames/Aliases o Titles **non crea un chip separato ma concatena il testo successivamente digitato in un'unica stringa non ancora confermata** (es. "CommanderKalSixLycan"). Fix: digitare un valore, poi cliccare il pulsante dedicato "+" accanto al campo per confermarlo come chip individuale. Applicato con successo a tutti e 4 i nickname (Commander, Kal, Six, Lycan) e i 2 titoli (Commander DCC Security Division; Major U.S. Army Ret.).

**Tag (7)**: Male, Werewolf, Military, bodyguard, Original, Supernatural, Modern, via il modale di selezione tag standard.

**Timeline**: Start Position e Birthdate entrambi a **10158624** (dal riferimento, non ricalcolati). Bug scoperto: dopo aver attivato lo switch Birthdate (che pre-riempie "0"), un click + ctrl+a + digitazione **non sostituiva lo zero pre-esistente ma lo prependeva**, producendo "010158624" invece di "10158624". Fix: bypassare click+tastiera e impostare il valore direttamente via JS (setter nativo `HTMLInputElement.prototype.value` + evento `input` dispatchato). La visualizzazione sullo schermo continuava a mostrare l'artefatto "0" iniziale in due screenshot successivi anche dopo la conferma via JS che il valore DOM reale era corretto; **risolto dopo un reload completo della pagina**, che ha confermato "10158624" senza zero iniziale. Era quindi un artefatto di rendering dello stepper widget, non un problema di dato reale, come sospettato. Start Position e Birthdate coincidono e sono entrambi ≤ world_age (10486470), coerente con §6.

**Pronomi**: stessa trappola già vista su Wulfnic, i campi apparivano visivamente popolati (testo placeholder grigio "they/them/their/theirs/themselves" sotto un Pronoun Set "Custom") ma erano vuoti. Confermato via query JS che nessun input conteneva un valore reale. Fix: individuare i 5 campi tramite il testo esatto della label precedente e impostare i valori (he/him/his/his/himself) via setter nativo + evento input. Pronoun Set ora corretto a "He/Him", tutti e 5 i sotto-campi confermati dopo reload.

**"How many examples to show"**: pre-impostato a 3 sulla scheda live nonostante 5 esempi pronti nel riferimento, stesso pattern di corruzione già visto su Wulfnic. Corretto a 5 via JS sull'elemento attivo.

**Outfit (5)**: zero presenti sulla scheda live. Aggiunti uno alla volta con salvataggio individuale dopo ciascuno, verificando via screenshot la persistenza dei precedenti prima di procedere al successivo (nessuna perdita di dati osservata):
1. Duty / Tactical (Default)
2. Off-Duty / Casual
3. Formal / Family Event
4. Full Shift
5. Hybrid Shift

Default Outfit impostato su "Duty / Tactical (Default)", corrispondente al riferimento.

**Dialogue Examples (5)**, aggiunti uno alla volta con salvataggio individuale:
1. "Command voice, zero hesitation"
2. "What Blackwolf cost him"
3. "Loyalty to Erik, not blind obedience"
4. "The only one who understands"
5. "Off duty, with Edric"

Tutti verificati privi di em-dash, `{{user}}` e grassetto markdown.

**Attitudes (4)**, tutte già a tier `friend` nel riferimento, **nessuna correzione romantic_interest→altro necessaria** (a differenza di Wulfnic, Noah, Logan dove questa correzione era stata applicata):
- Erik Douglas — Friend, intensità 90
- Malachia Douglas Bloodmoon — Friend, intensità 78
- Alyssa Douglas Bloodmoon — Friend, intensità 82
- Jasper Douglas Bloodmoon — Friend, intensità 75

Alyssa e Jasper, i due personaggi giocabili richiesti da §16, sono entrambi coperti. Selezione del Target Character sempre tramite la tecnica di dispatch JS su `[role="option"]` (mai `computer.type`), per evitare la ripetizione del bug "Nixara" osservato su Wulfnic.

**Global Character**: ON, confermato dopo reload.

## Verifica finale (§14.12, dopo reload completo della pagina)

- Zero `{{user}}`, zero em-dash, zero grassetto markdown in tutti i campi ispezionati (scroll completo di Display/Long/Short Description, Backstory, Family & Pack, Voice & Behavior, sezione tematica finale).
- Nome splittato, 4 Nickname, 2 Titoli, 7 Tag tutti confermati.
- Keys primarie (4: Kaladin, security, BlackWolf, DCC Security) e secondarie (8, incluso il campo che non era mai stato corrotto) confermate.
- Start Position e Birthdate = 10158624, coincidenti, **Birthdate visualizzato correttamente senza artefatto "0" iniziale dopo il reload** (risolve il dubbio aperto lasciato a fine sessione precedente).
- Pronomi He/Him, tutti e 5 i sotto-campi corretti.
- 5 Outfit presenti, Default Outfit impostato su Duty/Tactical.
- 5 Dialogue Examples, contatore "how many to show" = 5.
- 4 Attitudes con Alyssa e Jasper coperti, nessuna correzione di tier necessaria.
- Global Character = ON.
- RPG Stats: sezione lasciata collassata/non toccata, coerente con §8 (`world_features.rpg_stats` resta `false`).

## Note di continuità per le prossime schede

- Il pattern di corruzione descrizioni (Display/Long vuote, JED+ più nota format-discipline scaricati in Short) è ora confermato **2 volte su 2** sulle ultime schede toccate (Wulfnic, Kaladin). Da aspettarsi anche su Jared Thompson e Mac.
- Bug nuovo da tenere a mente per ogni scheda futura: **Invio nei campi Nickname/Titoli concatena invece di creare chip separati** — usare sempre il pulsante "+" dedicato.
- Bug nuovo: **ctrl+a non seleziona il valore pre-riempito "0" del campo Birthdate** dopo aver attivato lo switch — bypassare con impostazione diretta del valore via JS.
- Il rendering visivo del campo Birthdate può mostrare uno zero iniziale spurio anche quando il valore DOM è corretto; si risolve con un reload completo, non serve altro intervento.

## Prossimi passi

Priorità core family: **Jared Thompson**, poi **Mac**, seguendo lo stesso workflow diagnosi-contro-DB-locale poi fix-sito-live ormai collaudato su otto personaggi.
