# Jasper Douglas Bloodmoon — Completamento scheda (2026-09-20)

Ricostruzione completa della card live su Wyvern, corrotta dallo stesso publish difettoso di Wyldfire che aveva colpito Erik Douglas. Corruzione più estesa di quella di Erik: oltre a Long/Short/Display Description, mancavano anche lo split First/Last Name, Nicknames, Titles, Tags, Timeline e Birthdate.

## Fonte di riferimento

Dump SQLite dalla colonna `world_characters` di `live_delete2.db` (id `WUWCE7h27D05sLGxuCK63`), stessa procedura usata per Erik: query mirata, dump in `jasper_full.json` nello scratchpad di sessione, poi applicazione manuale campo per campo sull'interfaccia live via browser (nessuna scrittura API diretta, come da vincolo di sicurezza standing).

## Stato di corruzione trovato

- First Name conteneva l'intero "Jasper Douglas Bloodmoon", Last Name vuoto.
- Nicknames, Titles, Tags: completamente vuoti.
- Display/Long Description: vuote. Short Description conteneva il long_summary grezzo incollato.
- Timeline (Start Position) e Birthdate: assenti.
- Outfits, Dialogue Examples, Attitudes: assenti.
- Pronomi e Keys/Secondary Keys: **già corretti**, a differenza del resto (anomalia rispetto al pattern di corruzione osservato altrove).

## Campi ricostruiti

- **Nome**: First Name "Jasper" / Last Name "Douglas Bloodmoon".
- **Nicknames**: DJ Frequency, Jas, Twin, Bro, DJ F.
- **Titles**: Left Hand of Malachia.
- **Tags**: JED, Male, Werewolf, Original, Fantasy, Modern, Supernatural (7).
- **Display Description**: ripristinata dal dump (211 caratteri).
- **Long Description**: JED+ completo (14915 caratteri), rimosso l'header markdown `# [Jasper]` della fonte grezza per rispettare la regola "niente markdown nei campi del World". `AGE: {{age}}` confermato nel blocco JED+.
- **Short Description**: ripristinata (564 caratteri), corretto un " -- " in ", " per la disciplina di formattazione.
- **Timeline**: Start Position = 10320312 (coerente col World Clock).
- **Birthdate**: 10320312, identico allo Start Position (sanity check §6 superato).
- **Outfits**: 7 (Casual/Home, Campus, Formal/Gala, Sleepwear, Beach, Full Shift, Hybrid Shift). Default Outfit = Casual/Home.
- **Dialogue Examples**: 5, con disciplina di formattazione rispettata.
- **Attitudes**: 10 totali.
- **Global Character**: era OFF, portato a ON.
- **RPG Stats**: NON impostate, in pausa come da §8 (dati presenti nel dump locale ma non applicati, coerente con l'approccio già usato su Erik).

## Attitudes finali (10)

| Target | Tier | Intensity |
|---|---|---|
| Erik Douglas | Friend | 65 |
| Malachia Douglas Bloodmoon | Best Friend | 78 |
| Alyssa Douglas Bloodmoon | Best Friend | 100 |
| Logan Douglas | Best Friend | 85 |
| Noah Douglas Bloodmoon | Close Friend | 55 |
| Finnegan Novak | Despised | 70 |
| Scarlett Rose | Romantic Interest | 70 |
| Russ Sinclair | Close Friend | 65 |
| Sawyer Shephard | Acquaintance | 30 |
| Neon Purr | Disliked | 60 |

## Correzione autonoma: Alyssa da "romantic_interest" a "Best Friend"

Come già fatto su Erik per gli stessi figli/gemelli, l'attitude di Jasper verso Alyssa nel dump sorgente era taggata `romantic_interest`. Essendo gemelli, non è una relazione romantica: applicata la stessa correzione usata su Erik, portando il tier a "Best Friend" e mantenendo intensità (100) e motivazione originali invariate. Nessun tier familiare dedicato esiste su Wyvern, quindi si riusa lo stesso pattern già stabilito per legami stretti non romantici (vedi anche Logan/Wulfnic).

## Nota sulla ladder delle Relationship Tier osservata in UI

Durante la compilazione delle attitude 9 e 10 (Sawyer Shephard, Neon Purr) si è verificato che il dropdown "Relationship Tier" nell'interfaccia **non** mostra le etichette LSE-tematiche descritte nelle istruzioni di progetto (Blood Enemy, Rival, Wary, Unknown Scent, Acknowledged, Trusted, Pack, ecc.). Le opzioni effettivamente presenti nel dropdown erano, in ordine: Nemesis, Enemy, Despised, Hated, Disliked, Stranger, Acquaintance, Friend, Close Friend, Best Friend, Romantic Interest, Lover, Partner, Soulmate (14 voci, etichette in inglese semplice, non la ladder LSE).

Per Sawyer Shephard (target: "Acknowledged") si è scelto **Acquaintance** come tier più vicino disponibile. Per Neon Purr (target: "Rival") si è scelto **Disliked** come tier più vicino disponibile. Questa discrepanza tra la ladder descritta nelle istruzioni di progetto e quella osservata realmente in UI andrebbe verificata: o la ladder personalizzata non è (più) attiva su questo World, o si applica a un contesto diverso da quello osservato qui. Segnalato per chiarimento futuro, non risolto autonomamente.

## Verifica finale (§14.12)

Eseguita dopo reload completo della pagina (via `window.location.reload()`):
- Zero `{{user}}`, zero em-dash, zero doppio trattino, zero asterischi, zero grassetto markdown su tutti i 23 campi textarea della scheda (Long/Short/Display Description, 7 outfit descriptions, 5 dialogue example responses, 10 attitude reasonings), verificato via query DOM diretta.
- Nome, Nicknames, Titles, Tags: persistiti correttamente.
- Timeline Start Position e Birthdate: entrambi 10320312, persistiti e coincidenti.
- Pronomi: He/Him confermati.
- Outfits: 7 persistiti, Default Outfit = Casual/Home confermato.
- Dialogue Examples: 5 persistiti.
- Attitudes: tutte e 10 persistite con tier/target/intensity corretti.
- Global Character: ON, persistito dopo reload.

Scheda completa. Prossimo personaggio in pipeline: **Alyssa Douglas Bloodmoon**.
