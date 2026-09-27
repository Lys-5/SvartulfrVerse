# Concilio di Blackwood — i quattro Pack Leader mancanti, e la promozione Marino/O'Connor a Pureblood (2026-09-14)

Completati i quattro personaggi di distretto che mancavano dal Concilio, più una revisione di Vito Marino già esistente. Fonte: profili sintetici forniti dall'utente per tutti e dieci i capi di distretto (età apparente, orientamento, personalità, alleanze), usati per scrivere le schede complete via API, verificate con GET diretto (zero `{{user}}`, em-dash, grassetto o asterischi su tutte e cinque le schede toccate).

## Decisione di lore: età apparente vs età reale

Per i Common Bloodline l'età "apparente" indicata dall'utente è il dato fisico, l'età reale è stata scelta da Claude per adattarsi meglio alla personalità del personaggio (non calcolata a rigore dalla formula di invecchiamento lento di `Longevita_Common_Bloodline.md`, che resta comunque coerente nella maggior parte dei casi per pura combinazione). Confermato dall'utente: "intendo l'aspetto fisico, sull'età stabiliamo in base a quella più adatta alla personalità".

## Promozione a Pureblood: Marino e O'Connor

Decisione dell'utente: dato che Blackwood è più antica di Solarton, può permettersi qualche famiglia Pureblood in più oltre ai Douglas. Due famiglie promosse:

- **Vito "Scar" Marino** (Ironworks, già esistente): promosso da semplice Alpha a **Pureblood**. Scheda rivista per dargli un'origine reale: nato Vittorio Marino nel sud Italia nel 1901, emigrato in America negli anni '20 come molte famiglie italiane dell'epoca, arrivato a Blackwood e risalito nella gerarchia dell'Ironworks da zero. Età reale ora 123 anni (nato 14 marzo 1901), non più calcolata a faccia valore come nella build originale. Aggiunto un accenno d'accento italiano che riemerge quando è arrabbiato, e la sua codardia verso i pari o superiori (dettaglio nuovo emerso dal profilo fornito dall'utente, non presente nella build originale). RPG Stats impostate per la prima volta via API (erano `null`): Livello **99** (tetto di piattaforma per i centenari, §8), specie Weres/Shapeshifters. `birthdate`/`start_timeline_position` aggiornati di conseguenza.
- **Marcus "Mark" O'Connor** (Oldtown, nuovo): scritto direttamente come Pureblood. Origine irlandese, immigrato a inizio '800, arrivato a Blackwood mentre Oldtown veniva ancora costruita sopra l'insediamento coloniale di Lord Cornelius Douglas, il che lo rende letteralmente uno dei pochissimi residenti che ricorda davvero la città che Oldtown dice di preservare. Età reale 225 anni (nato 2 settembre 1798). Livello RPG 99.

## Le quattro schede nuove

Tutte con pipeline completa: JED+ in `long_summary`, `summary` compatto, `display_description`, titles/keys/pronomi, cinque outfit contestuali con default, RPG Stats via API (specie + livello, budget punti standard 25+base), cinque Dialogue Examples, Attitudes verso Alyssa e Jasper (tier `stranger`, mai incontrati) più le relazioni rilevanti già note dal profilo fornito dall'utente, Global Character ON.

- **Naomi Black** (`_pPe6prj8qnWaDWpt2Kfnd`), co-Pack Leader di Uptown North insieme a Cass Harrow. Werewolf Beta (non Alpha, per differenziarla dalla rigidità di Cass), età reale 67. Carismatica, ambiziosa, calcolatrice, gestisce finanza e tecnologia del distretto, legame diretto con Angelo Moreno costruito in decenni. Attitude aggiunta anche sul lato di Cass Harrow (che non l'aveva ancora, nonostante la citasse in background) per chiudere il legame in entrambe le direzioni.
- **Darius Vale** (`_YCnHbjcbrLe9AFFXQEqX6`), Pack Leader di Uptown South. Werewolf Alpha, età reale 45. Riservato, leale, determinato, non ha mai cercato il potere che gli è stato affidato. Relazioni cordiali ma non intime con Uptown North.
- **Marcus "Mark" O'Connor** (`_C1LapDdDhfXefNcEJ66D8`), Pack Leader di Oldtown, vedi sopra per l'origine Pureblood. Alleato fidato di Logan Douglas (tier `friend`, intensità 75) e protetto personalmente da Malachia Douglas-Bloodmoon (tier `friend`, intensità 60), entrambe le relazioni aggiunte come Attitudes.
- **Prof.ssa Helena Weiss** (`_181C2DDyEUfRgLREyd4CC`), Pack Leader di Arcadia e Rettore del complesso scolastico del distretto. Werewolf Beta, età reale 59. Trattata esplicitamente come l'eccezione prevista dal canon LSE del Pack Leader non-Alpha (§12 del progetto: "nel 95% dei casi lo è" implica un 5% che non lo è): tiene il seggio per autorità accademica e istituzionale, non per forza territoriale, ed è scritta come una delle voci più neutre e rispettate del Concilio proprio per questo.

## Stato del Concilio

Con questi quattro, tutti i dieci seggi distrettuali del Concilio hanno un personaggio completo su Wyvern: Vito Marino (Ironworks), Bianca Rossi (Paradise East), Dominic Chen (Paradise West), Aurora Night (Bluemoon North), Eclipse Noir (Bluemoon South), Cass Harrow e Naomi Black (Uptown North), Darius Vale (Uptown South), Marcus O'Connor (Oldtown), Isobel Blackwater (Dockside), Helena Weiss (Arcadia).

Restano da fare: Erik Douglas già esiste come personaggio (presidente del Concilio, non serve altro lavoro); Angelo Moreno (rappresentante vampiro) e Federico "Riki" Savini (rappresentante Solitaries) andrebbero verificati se già esistono come schede complete o solo come segnaposto; i sette rappresentanti delle specie minoritarie restano con **Zeera** (demoni) come unico completato, gli altri sei ancora da decidere nei dettagli (fatato, orco, demi-human, strega, naga, non-morto) e il rappresentante umano ancora senza nome.

## Nota per il futuro

Il materiale fornito dall'utente per tutti e dieci i distretti include anche alleanze e rivalità fra i Pack Leader già esistenti non ancora tradotte in Attitudes sulle rispettive schede (es. Bianca Rossi/Dominic Chen alleati commerciali, Bianca Rossi/Angel&Co legami stretti, Bianca Rossi/Eclipse Noir alleanza instabile, Isobel Blackwater/Vito Marino ostilità aperta, già presente su Vito ma da verificare sul lato di Isobel). Non ancora fatto in questa sessione, segnalato come lavoro pulito da riprendere.
