# Character Pool: come funziona il piazzamento dei personaggi

Trovato controllando che Finn potesse comparire al campus. **Risolto:** il piazzamento va fatto a livello di Environment, non di Location.

## Il meccanismo, confermato dalla wiki

Ogni Character ha un toggle **Global Character**:

> "When on, this character is active everywhere in the world. When off, it is scoped to specific locations/environments and only active where it is placed."

Un personaggio non globale e non inserito in nessun pool **non si attiva mai**, né a inizio chat né per keyword.

Dalla pagina wiki [Environments & Locations](https://wiki.wyvern.chat/en/Features/Worlds/Environments-Locations):

| Livello | Testo ufficiale |
|---|---|
| **Environment** → Included Characters Pool | "Which of your world's Characters can appear in this environment. Add characters here with a **participation weight** (higher = more likely to be selected for the active scene)." |
| **Location** → Included Characters Pool | "Characters who can appear at this specific location. **Stacks with the environment's pool, both are merged.**" |
| **Parent Location** | "The parent's description and character pool also load when this location is active." / "Its character pool is merged into the current location's pool." |

Quindi **l'intuizione dell'utente è corretta e confermata**: mettere i personaggi nel pool dell'Environment copre automaticamente tutte le Location al suo interno. Il pool della Location serve solo per aggiungere chi è specifico di quel singolo posto.

**12 Environment invece di 79 Location.**

Nota importante: il pool ha un **participation weight** per personaggio. Mettere 40 personaggi nel pool di SUCC non è un problema, il peso governa chi viene effettivamente selezionato. E comunque:

> "Included Characters Pool is not the same as 'who is in the scene.' It's the pool of who could be in the scene. The actual selection of who appears depends on the user's party state."

C'è anche **Character Capacity Limits** (Minimum / Maximum) sull'Environment, che governa quanti personaggi esistono nell'ambiente quando la simulazione viene inizializzata.

## Stato rilevato

| Personaggio | Global Character |
|---|---|
| Alyssa Douglas Bloodmoon | ON |
| Noah Douglas Bloodmoon | ON |
| Vincent Campbell | OFF |
| Jared Thompson | OFF |
| Finnegan Novak | OFF |

Pool controllati e **tutti vuoti**: Environment `Supernatural University of Central California`; Location `Lunar Quad`, `Gym & Changing Facilities`, `KSA House`.

Non era un problema di Finn: FAMILY e PACK funzionano perché globali, ma tutti gli NPC di campus erano non globali e non piazzati, quindi inerti. Valeva anche per Vincent e Jared.

## Decisione operativa

**L'utente popola i pool a livello di Environment**, per categoria geografica:

- personaggi SUCC/Solarton → Environment `Solarton` e `Supernatural University of Central California`
- personaggi Blackwood → Environment `Blackwood City` (e `Blackwood Forest` dove ha senso)
- personaggi Los Angeles → Environment `Los Angeles`
- **FAMILY e PACK restano su Global Character**, nessun pool necessario

## Nota tecnica: come consultare la wiki

`WebFetch` su `wiki.wyvern.chat` restituisce **403** in modo sistematico (bot detection), e i risultati di `web_search` danno solo snippet.

**Metodo che funziona, indicato dall'utente:** aprire la wiki **in un tab del browser** (`preview_start` / `navigate`) e leggere la pagina con `javascript_tool`. Va sempre fatto così, mai col fetch.
