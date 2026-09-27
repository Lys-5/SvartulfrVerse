# Mackenzie "Mac" Sanchez-Rogers — Completamento scheda (2026-09-21)

Decimo personaggio completato in questa sessione di ricostruzione, dopo Erik, Jasper, Alyssa, Malachia, Noah, Logan, Wulfnic, Kaladin, Jared Thompson. Character id: `OmG2HT5Sqcf6LIyTQFTgs`. World: Svartúlfr | The Douglas-Bloodmoon Pack (`_CgYT8fHXpDC4crjmegQF7`).

## Corruzione riscontrata

Quinta occorrenza confermata del pattern di corruzione da bad publish Wyldfire: campi Display/Long/Short Description scambiati o riempiti con testo grezzo/placeholder sbagliato (nel caso di Mac, contenuto di un personaggio Victorian-era estraneo, "Margret Alaina Thames"). **Variante inedita rispetto ai casi precedenti:** lo Short Description (`summary`) era già corretto e nel formato PList atteso, a differenza di Long e Display che erano corrotti. Riscritto tutto in JED+ secondo §2, mantenendo lo Short esistente dove già valido.

## Dominio

Confermato dominio SUCC/Solarton (band Grave Mistake, campus), non Douglas/Blackwood, per la precedenza di dominio di §10. Le Attitudes verso Alyssa e Jasper Douglas Bloodmoon sono state impostate a "Stranger" con motivazione esplicita di non essersi mai incontrati, come da §16.

## Decisioni di scrittura

- **Pronomi**: il campo `pronouns` di riferimento era vuoto. Usato "GENDER: Male, he/him" dichiarato nel suo stesso `long_summary` per impostare il Pronoun Set su He/Him (tutte e cinque le forme). Nessuna invenzione: dato dichiarato dalla fonte stessa.
- **Timeline**: Start Position e Birthdate impostati entrambi a `10270512`, coerenti tra loro e ≤ world_age (10486470), come richiesto da §6/§7.
- **Dialogue Examples**: portati a 5 (count confermato).
- **Outfit**: tutti e 7 presenti e contestuali (The Van, Behind the Keys, Working, The Den, Oakland, Full Shift, Hybrid Shift), Default Outfit = "The Van". Full Shift e Hybrid Shift coprono le due forme di licantropo (quadrupede e ibrida bipede) secondo §4/§5.
- **RPG Stats**: non toccate, lasciate disabilitate. `world_features.rpg_stats` resta `false` a livello World, per §8.
- **Global Character**: impostato ON.

## Attitudes / Relationships (10 totali)

| Target | Tipo | Tier | Intensity | Note |
|---|---|---|---|---|
| Fade Greymoor | World Character | Best Friend | 85 | Co-fondatori di Grave Mistake dal primo anno |
| Viola Carter | World Character | Friend | ~50 | Rivalità amichevole, rispetto reciproco come musicisti |
| Roland Vickers | World Character | Disliked | 50 | Non lo sopporta e glielo dice in faccia |
| Allegra Lumsden | World Character | Disliked | 50 | (vedi dettaglio scheda) |
| Luisa Sanchez Rogers | World Character | Best Friend | 85 | Relazione sentimentale storica, liceo/college |
| Bailey Rogers | World Character | Acquaintance | 20-25 | Sorella maggiore, la proteggerebbe sopra ogni cosa |
| Alyssa Douglas Bloodmoon | World Character | Stranger | 15 | Mai incontrati (dominio Douglas/Blackwood, §10/§16) |
| Jasper Douglas Bloodmoon | World Character | Stranger | 15 | Mai incontrati |
| (Generic, es. spacciatori/rivali) | Generic (text) | Despised | alta | Considera l'intera faccenda una menzogna |
| (Generic, es. contesto Oakland) | Generic (text) | Disliked | media | Cresciuto senza niente a Oakland, gli hanno detto che non valeva nulla |

Tutte e 10 verificate persistenti dopo un **reload completo genuino** della pagina (non solo stato in-sessione): lunghezze dei campi Reasoning identiche prima/dopo reload (312, 247, 221, 237, 229, 192, 103, 20, 249, 189 caratteri).

## Bug di piattaforma nuovo scoperto in questa sessione

**Il valore di una `<textarea>` impostato via JS (setter nativo + evento `input`), se lasciato come ultimo campo modificato prima di cliccare Save, si azzera dopo il salvataggio.** Osservato in modo ricorrente (~9 volte su 10 Attitudes) sul campo Reasoning dell'ultima Attitude aggiunta in ogni ciclo. Causa probabile: lo stato React del campo appena impostato via JS non viene "flushato"/commitato prima che l'handler di Save legga lo stato del form.

**Fix verificato e ripetibile**: dopo aver impostato il valore della textarea via JS, cliccare (via JS) su un elemento neutro non-input nelle vicinanze (in questo caso l'header "Attitude Configuration" più recente) per forzare un blur/commit, **poi** cliccare Save. Confermato funzionante alla ripetizione ogni singola volta, e ora anche confermato attraverso un reload completo della pagina (non solo una verifica in-sessione che poteva essere ingannevole).

**Raccomandazione**: aggiungere questo bug alla tabella di §15 del progetto, dato che è un trap genuinamente nuovo non ancora documentato lì, e applicare preventivamente il pattern "click su elemento neutro prima di Save" per qualunque campo testarea sia l'ultimo modificato in un ciclo di editing futuro.

## Verifica finale §14.12 (post-reload)

Eseguita dopo navigazione reale (non solo stato in-memoria) a `https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7` e riapertura della scheda dai risultati di ricerca "Mackenzie":

- Zero `{{user}}`, zero em-dash, zero asterischi, zero grassetto markdown (controllati su tutti i campi input/textarea della pagina).
- Nome: Display "Mackenzie Sanchez-Rogers", First "Mackenzie", Last "Sanchez-Rogers".
- Nickname "Mac" presente come chip.
- Title "Keyboardist, Grave Mistake" presente come chip.
- Pronomi: Pronoun Set "He/Him", tutte le forme (he/him/his/his/himself) popolate correttamente.
- Timeline: Birthdate e Start Position entrambi 10270512.
- Outfit: tutti e 7 presenti con lunghezze descrizione coerenti (205, 195, 186, 171, 194, 429, 376). Default Outfit = "The Van".
- Dialogue Examples: 5.
- Attitudes: tutte e 10 presenti con Target/Tier/Reasoning intatti (dettaglio sopra).
- Global Character: ON (`aria-checked="true"`).
- RPG Stats: non abilitate (invariato, per §8).

Scheda considerata chiusa e conforme alla pipeline §14.
