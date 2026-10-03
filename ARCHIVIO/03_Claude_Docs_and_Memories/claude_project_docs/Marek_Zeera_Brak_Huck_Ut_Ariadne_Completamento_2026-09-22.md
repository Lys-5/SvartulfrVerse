# Marek, Zeera/Brak/Huck, Ut Berg, Ariadne — Completamento 2026-09-22

Sessione di continuazione dopo compattazione. Lavoro svolto sul World via interfaccia (modifiche) + API di sola lettura (verifica), come da istruzione esplicita di Lys in questa sessione.

## Scoperta di piattaforma: Lexicon duplicate orfane

Durante la modifica di "Intimacy Profile - Zeera" ho scoperto che esistevano **due entry Lexicon con lo stesso nome**:
- `_MfPUdXVGH2yneMzkP8hKh` (creata 14/09, party_conditions correttamente puntata su un `character_id` di Zeera che **non esiste più** nella lista Character del World, e **non compare nella lista dei 251/252/253 Lexicon del World** nonostante sia leggibile via GET diretta per id)
- `_KfC16pAxwjMbE3PD4qYpL` (creata 18/09, stesso giorno di creazione della card Zeera attuale, party_conditions vuoto all'origine, **questa è quella davvero attiva nel World**)

Causa quasi certa: una ricreazione della card Zeera avvenuta il 18/09 (stesso pattern osservato anche su Ariadne Cirillo, vedi sotto) ha generato un nuovo `character_id` senza aggiornare o rimuovere la vecchia entry Lexicon collegata al `character_id` precedente, lasciandola orfana. La nuova entry creata contestualmente aveva party_conditions vuoto (bug di sync, probabilmente dal passaggio locale-Wyldfire-poi-Wyvern di cui parla §17), quindi finché non l'ho corretta oggi **sparava ovunque nel World**, non solo nelle scene con Zeera.

**Non ho toccato l'entry orfana** `_MfPUdXVGH2yneMzkP8hKh`: è irraggiungibile dall'interfaccia (non appare in nessuna ricerca né nella lista Lexicon), quindi non influisce sul gioco. Segnalato qui per traccia, non serve azione a meno che riemerga.

**Lezione operativa per il futuro**: dopo qualunque modifica a una entry Lexicon "Intimacy Profile - X" o simile, verificare via API che il `character_id` nei `party_conditions` corrisponda davvero all'id attuale di X nella lista Character del World, non fidarsi del solo fatto che l'interfaccia mostri "Ariadne Cirillo" o "Zeera" selezionata per nome: un nome può corrispondere comunque all'unico personaggio vivo con quel nome, ma se in futuro ne esistessero due lo stesso problema si ripresenterebbe.

## Zeera, Brak Ironfist, Huck: recupero dati scartati

Su richiesta esplicita di Lys ("Zeera, Huck, Brak Ironfist: crea il lexicon recuperando i dati scartati"), chiarita via AskUserQuestion con risposta **"Solo il kink/anatomia riusabile, non l'arco {{user}}"**. Le tre fonti originali JanitorAI sono state lette per intero dopo login di Lys nel browser.

- **Zeera** (Lexicon `_KfC16pAxwjMbE3PD4qYpL`): aggiunto size kink (compatibilità anatomica Vax come elemento di attrazione) e una storia pregressa di scarsa attenzione al piacere del partner, scritta come difetto riconosciuto e corretto, non come scusa. Fonte esclusa: l'intera cornice di tratta di schiavi legata a `{{user}}`.
- **Vax - Reproduction and Compatibility** (Lexicon specie): **nessuna modifica necessaria**, la entry esistente copre già il meccanismo di doppia anatomia riproduttiva in registro biologico/enciclopedico non esplicito, conforme a §7.
- **Brak Ironfist** (Lexicon `_qy9XxBqQp6cQyWpB9kwyQ`): aggiunto size kink (preferenza per partner più piccoli) e lode verbale intensa durante l'intimità. Fonte esclusa: il matrimonio combinato con `{{user}}`.
- **Huck** (Lexicon `_G9RArLtbUjLTY6UnE1xy8`): aggiunto controllo del consenso costante anche a metà scena ("you good?"), dominante ma mai crudele, molto verbale. Fonte esclusa: la sottotrama di stalking/video, gun/weapon play e la cornice semi-pubblica/di rischio (esclusi per scelta editoriale, tonalmente legati alla parte scartata).

Tutte e tre le entry avevano `party_conditions` mancanti o vuoti prima di questa sessione (non solo Zeera): corretti tutti e tre puntandoli sul `character_id` attuale del rispettivo personaggio.

## Ut Berg: nuova Intimacy Profile

Non esisteva. Creata da zero (Lexicon `_cB7wkXA8WcKnAkAjbV16A`) usando il materiale già pulito e già sincronizzato nel repo (`Ut_Berg_world.json`), stile a blocchi coerente con Erik/Zefir. Unica modifica rispetto alla fonte: **rimossa la clausola "STRICTLY NON-APPLICABLE with `{{user}}`"** dal blocco Hard Limits, perché anche una clausola che vieta esplicitamente `{{user}}` resta comunque un riferimento a `{{user}}` che non ha senso in un World dove `{{user}}` non è una persona fissa (§13). Sostituita con un Hard Yes generico coerente con il resto della scheda. `party_conditions` impostato su `_NYtBzeKNkm3pedHMnYaka` (id attuale di Ut Berg).

## Ariadne Cirillo: estrazione da long_summary

Verificato (§9.5, mai fidarsi di un documento vecchio senza riverificare alla fonte) che la nota nel documento del 14/09 sull'audit generale ("Ariadne già sistemata") si riferiva a un `character_id` precedente (`_hXBqkLzmdXTyk6yYVHM6y`), **anche lei ricreata il 18/09** con un nuovo id (`_q1rYKHndN64QUgjHQazXB`), stesso pattern di Zeera. La sezione `INTIMACY:` completa era quindi ancora presente per intero in `long_summary` sulla card attuale, non solo un residuo.

- Arricchita la entry Lexicon esistente "Intimacy Profile - Ariadne Cirillo" (`_zAWDDbAEyxt1Q9J2aUTWG`), che copriva solo il tratto "dominante, non switcha" (550 caratteri), fondendola con tutto il contenuto rimosso da `long_summary` (registro giocoso, pratiche nominate, gestione del consenso sul veleno, aftercare, "the level voice"): ora 1372 caratteri. `party_conditions` era vuoto, corretto puntandolo su `_q1rYKHndN64QUgjHQazXB`.
- `long_summary` della card: sezione `INTIMACY:` ridotta a una riga sobria che rimanda al Lexicon, stesso pattern già in uso su Venera Dolce: *"A fuller Intimacy Profile is filed separately in the Lexicon rather than spelled out here."*

## Marek | Ukiyo Series → Marek

Import grezzo (`long_summary` vuoto, tutto il materiale ammassato in `summary`, pieno zeppo di `{{user}}`) convertito in scheda JED+ completa.

**Escluso integralmente** (§13 estensione 14/09, arco romantico/sessuale intero costruito su `{{user}}`): la storyline del vicino di casa `{{user}}` di cui si invaghisce, l'intera sottosezione "With `{{user}}`" della personalità, i Dialogue Examples rivolti a `{{user}}`, le Notes di istruzione su come trattare `{{user}}` in scena, e le misure anatomiche esplicite numeriche.

**Riusato**: origine (Autonomous Commercial District, tribù blue oni, fratello di sangue Niran), il club Ironhorn Nomads (fondazione, legame con gli Obsidian Blades, traffico di armi/droga), le relazioni con Niran (Presidente) e Vannak (Road Captain), personalità (Charismatic Devil, possessivo, territoriale, leale ai suoi), abitudini (riordina senza chiedere, non finisce mai un drink, brucia incenso), il segreto delle tradizioni oni nascoste e il gancio narrativo della "fame" che cresce sotto la rabbia (riscritto come arco aperto, non richiude nulla). Base fissata a Ironworks, il distretto industriale di Blackwood City, coerente con la descrizione del World.

Scritto:
- `long_summary` in JED+ completo (blocco attributi + BACKSTORY + CLUB AND CREW + VOICE & BEHAVIOR + THE HUNGER HE WON'T NAME), 3817 caratteri
- `summary` riscritto come PList puro
- `display_description`
- Nickname "Iron Hammer"
- Display Name / First Name ripuliti da "| Ukiyo Series"
- Global Character acceso (era spento)
- Start Position impostata via Era ("Present (Marek's lifetime)", 10073664h, nato 3 marzo 1977, coerente con l'età dichiarata di 47 anni e con il world_age corrente)
- Nuova Intimacy Profile Lexicon (`_nPnMzN11td3x7CUaAQg14`), kink generalizzati (dominanza, forza fisica, marking, dirty talk) senza l'arco `{{user}}` e senza descrizioni anatomiche numeriche, `party_conditions` sul suo id attuale

**Non affrontato, da valutare**: il World ha solo due Environment (`Voidspace`, `California Coast`) e §7 documenta che popolare i Character Pool degli Environment è stato valutato inutile e abbandonato. Ho interpretato "conversione come char dell'environment di Blackwood" come "scheda propriamente calata nell'ambientazione Blackwood" (già fatto: cartella BLACKWOOD, base a Ironworks), non come aggiunta letterale al Character Pool di "California Coast". Se Lys intendeva quest'ultima cosa, va fatta esplicitamente.

**Pipeline non completata per Marek** (rimane per una sessione futura, stesso standard delle altre schede): 5 Outfit contestuali + Default Outfit, 5 Dialogue Examples, Attitudes (almeno Alyssa/Jasper stranger/15, più eventuali su Niran/Vannak se diventano Character), pronomi, RPG Stats (in pausa di default, §8).

## Verifica

Tutte le scritture di questa sessione riverificate via GET API autenticata subito dopo il salvataggio (non solo il toast "successo" dell'interfaccia, che in un caso durante questa sessione si è rivelato non affidabile, vedi sopra). Zero `{{user}}` residuo verificato programmaticamente sulla card di Marek.

## Addendum 2026-09-22 (seconda parte sessione): Entry Type "Memory" + Attached Character

Lys ha segnalato, con screenshot annotato della entry "Intimacy Profile - August Reed", che ogni Lexicon riferita a un singolo personaggio va anche impostata con **Entry Type = "Memory"** e collegata tramite il campo **Attached Character** al personaggio corrispondente — un campo distinto dai `party_conditions`, che finora in questa sessione non avevo toccato (avevo impostato solo i `party_conditions`, lasciando `type` e `attached_world_character_id` non impostati sulle sei entry nuove/modificate).

Confermato via GET su August Reed che questi corrispondono, lato API, ai campi di primo livello `type: "memory"` e `attached_world_character_id: "<char_id>"` sull'oggetto Lexicon (stesso schema già noto da §11, non campi nuovi — semplicemente non li avevo popolati finora su queste sei entry). Su indicazione di Lys ("fallo tramite api dovrebbe essere non pericoloso per una cosa di questo genere") applicato via PUT parziale (solo i due campi, non l'oggetto intero) a tutte e sei le entry toccate in questa sessione:

| Entry | id | Attached Character (id) |
|---|---|---|
| Intimacy Profile - Zeera | `_KfC16pAxwjMbE3PD4qYpL` | Zeera (`_a6KYGdN3BWTgbYEbT4mx8`) |
| Intimacy Profile - Brak Ironfist | `_qy9XxBqQp6cQyWpB9kwyQ` | Brak Ironfist (`_AycV4d9dJRBakCmdH4q4J`) |
| Intimacy Profile - Huck | `_G9RArLtbUjLTY6UnE1xy8` | Harlan "Huck" Beaumont (`_AjMH4N66RxKj2Pr84wqgz`) |
| Intimacy Profile - Ut Berg | `_cB7wkXA8WcKnAkAjbV16A` | Ut Berg (`_NYtBzeKNkm3pedHMnYaka`) |
| Intimacy Profile - Ariadne Cirillo | `_zAWDDbAEyxt1Q9J2aUTWG` | Ariadne Cirillo (`_q1rYKHndN64QUgjHQazXB`) |
| Intimacy Profile - Marek | `_nPnMzN11td3x7CUaAQg14` | Marek (`_kP1gWeyLw9jKbz3Xf73GH`) |

Tutte e sei riverificate con una GET fresca subito dopo il PUT: `type` e `attached_world_character_id` persistiti correttamente su ognuna, `party_conditions` e contenuto invariati (nessuna sovrascrittura collaterale, come atteso da un PUT parziale su campi di primo livello).

**Nota per lo sweep più ampio**: Lys ha formulato la regola in generale ("gli intimacy profile e le lexicon che fanno riferimento ad un unico personaggio"), il che suggerisce che anche altre entry pre-esistenti nel World (es. quelle dell'audit del 14/09, o altre non toccate in questa sessione) potrebbero avere lo stesso buco (`type`/`attached_world_character_id` mancanti pur con `party_conditions` corretti). Non ancora verificato con uno sweep dedicato: da fare in una sessione futura se Lys conferma che la regola vale retroattivamente su tutto il World e non solo sulle entry toccate qui.
