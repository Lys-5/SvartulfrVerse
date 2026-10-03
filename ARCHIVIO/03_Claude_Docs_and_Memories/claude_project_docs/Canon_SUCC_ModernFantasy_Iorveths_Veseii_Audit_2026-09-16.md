# Audit canon SUCC/Modern Fantasy — Iorveths e veseii (16/09/2026)

## Richiesta

L'utente ha chiesto di importare **tutti** i personaggi canon SUCC-U-Verse e Modern Fantasy, individuandoli su Janitor AI cercando nei tag `#SUCC` e `#modernfantasy`, **solo** fra quelli creati da **@Iorveths** e **@veseii** (i due autori "canonizzati", confermati come coppia di scrittori strettamente legata dalla stessa bio di Iorveths: "we're literal roommates best friends irl... ves' account is used for alternate scenarios, but i write most of them").

## Metodo

Confermato dall'utente come "il metodo migliore": query scoped per creatore + tag, equivalenti alla ricerca `#tag` nella barra di ricerca interna del profilo autore.

- Endpoint usato: `GET /hampter/characters?page=N&custom_tags[]=<TAG>&user_id[]=<creator-uuid>&sort=latest&mode=all&count_mode=bounded`
- UUID Iorveths: `ae3b8516-54d5-4469-8557-6dcf808128d0`
- UUID veseii: `fa479f59-71a0-4296-a24d-6e8ca1c3d6fa` (trovato tramite i link `a[href*="profiles"]` nella pagina profilo di Iorveths)
- Query eseguite: 4 combinazioni (Iorveths×SUCC, Iorveths×modernfantasy, veseii×SUCC, veseii×modernfantasy), paginando fino a esaurimento risultati.

## Risultati grezzi

| Query | Risultati |
|---|---|
| Iorveths × SUCC | 28 |
| Iorveths × modernfantasy | 41 |
| veseii × SUCC | 43 |
| veseii × modernfantasy | 35 |
| **Totale voci grezze** | **147** |

Molte voci sono carte duplicate dello stesso personaggio (versioni/scenari alternativi dello stesso "canon", conseguenza diretta del fatto che l'account veseii ospita "alternate scenarios" secondo la bio di Iorveths), o carte di gruppo/crossover (es. "Vincent Campbell VS Jared Thompson", "Miles, Rafael and Kade | Alpha Squad", "Rhett and Jayce", "Jared and Stan", "Hank Thompson & Stanley Sr.", "Casey Williams and Nikolaj Jökull") che accoppiano personaggi già individualmente censiti, senza introdurne di nuovi.

**Dopo deduplica per nome normalizzato: 78 nomi unici.** Di questi, confrontati manualmente (con normalizzazione estesa: nickname fra virgolette, "Jr"/"Jr.", prefissi "Professor"/"Dr.") contro i 404 personaggi attualmente nel World (`world_characters` sul database Wyldfire locale, versione post-purga 404/401 del 16/09), **77 su 78 risultano già presenti** nel World, sia pure quasi sempre sotto un nome leggermente diverso da quello Janitor (es. Janitor "Professor Richard Loewe" = World "Professor Loewe"; Janitor "Chase \"Goldie\" Anderson" = World "Chase Anderson"; Janitor "Stan Davies Jr" = World "Stanley Davies Jr."; Janitor "Finnegan \"Finn\" Novak" = World "Finnegan Novak"; Janitor "Mackenzie \"Mac\" Sanchez-Rogers" = World "Mackenzie Sanchez-Rogers"; Janitor "Dr Arthur Sinclair" = World "Dr. Arthur Sinclair"; Janitor "Andrew \"Andy\" Campbell" = World "Andrew Campbell"; Janitor "Santiago \"Tank\" Herrera" = World "Santiago Herrera").

## L'unico personaggio genuinamente nuovo: Angui

**Non trovato nel World in nessuna forma.** Card Janitor (creator_name riportato: Iorveths, trovata via query veseii — probabilmente per via della condivisione fra i due account descritta nella bio), tag Male / OC / Monster / AnyPOV, `is_nsfw: true`. Il campo `personality`/`scenario`/`first_message`/`example_dialogs` della card Janitor sono vuoti (contenuto riservato, stesso pattern del gruppo 401 già trattato, ma qui la card risponde 200: probabilmente il dettaglio narrativo scenico non è pubblico, non che la card sia privata).

**Fonte primaria (tier 1, lorebook ufficiale) recuperata da `io-modernfantasy.uwu.ai/#angui`:**

> Species: Swamp creature, a humanoid with eel-like traits. Related to the hydra.
> Nationality: Greek
> Age: ??? (testo dice "effectively immortal and over 100 years old")
> Height: 6'11", 210 cm
> Likes: Fish, insects, water, night time, music
> Dislikes: Loud noises, crowds, humans
>
> Originally born in Mykonos, Angui was captured and illegally smuggled into the US, destined to be tested on by a pharmaceutical company due to his natural healing abilities. However, a scientist took pity on him and allowed Angui to escape. Since then, Angui has inhabited a swamp in Maryland and local legend has built up around him, causing locals to believe Angui is a swamp monster of enormous proportions. He is hostile to all humans who enter his territory, but is more lenient with other supernatural creatures. Angui is strictly carnivorous and prefers to eat fish. He doesn't trust humans as he thinks they will hurt him or use him for experiments. Angui is intelligent, but knows very little of the modern world.
>
> Saliva has healing properties. Effectively immortal and over 100 years old. Mostly eats fish and insects.
> **Credit sulla pagina lorebook: "BY OREO"** (non Iorveths/veseii direttamente — verosimilmente uno dei collaboratori il cui materiale viene pubblicato tramite l'account veseii, coerente con "ves' account is used for alternate scenarios, but i write most of them").

## Perché non ho ancora costruito la scheda

Prima di scrivere JED+ per Angui ci sono almeno tre decisioni che secondo le regole del progetto (§9.7) vanno proposte e confermate, non assunte:

1. **Geografia**: il lore originale lo colloca in una palude nel Maryland, non in California. Va deciso se Blackwood/il World lo rilocalizza (es. una palude vicino a Blackwood City) o se resta un personaggio fuori mappa, importato solo come Lexicon/riferimento senza Start Position attiva a Blackwood.
2. **Specie/longevità**: non è un licantropo Common/Pureblood/Founding, è una creatura acquatica greca "legata all'hydra", effettivamente immortale. Non rientra in nessuna delle categorie di specie già codificate nel progetto (§12): va scritto come categoria a parte, oppure segnalato come "fuori tassonomia" nel campo SPECIES.
3. **Età**: la fonte dice esplicitamente "???" più "over 100 anni", quindi rientra nel caso "quando l'utente lascia scelta a discrezione" upon build — andrebbe proposto un numero preciso (o lasciato `{{age}}`/indeterminato) prima di scriverlo sul World.

## Il caso "SUCC's Anime Club"

Trovato con lo stesso metodo (veseii × SUCC), **non è un personaggio singolo** ma una carta di scenario/gruppo: introduce tre personaggi non nominati singolarmente ("an awkward vampire with a blood intolerance, a stoner werewolf gamer who draws furry porn to pay rent and an eldritch being part of an infectious hivemind"). Non essendo nominati, non è possibile trattarli come Character individuali senza inventare identità (vietato da §9.4). Proposta: lasciarlo fuori dall'import, a meno che l'utente non riconosca questi tre come personaggi già esistenti sotto altro nome.

## Esito pratico

Il roster canon SUCC/Modern Fantasy di Iorveths e veseii, per come è raggiungibile tramite i tag `#SUCC` e `#modernfantasy` sui loro due account Janitor, **risulta già quasi interamente coperto** dal lavoro di stub/import delle sessioni precedenti (14-15/09). Resta un solo personaggio genuinamente da importare, Angui, più il caso dubbio del club senza nomi.
