# Attitudes: audit, correzioni e mappa dei tier

Data: 2026-09-03. Dati letti dal server via API autenticata, non dall'interfaccia.
**Fase 1 (le 13 schede che avevano già Attitudes) eseguita e verificata.**

## Mappa etichetta → chiave salvata (verificata, definitiva)

Letta dai props React delle opzioni del dropdown, non dedotta. **Le chiavi
interne non corrispondono ai nomi delle etichette**, ed è la causa di ogni
falso allarme di questo audit.

| Etichetta nell'interfaccia | Soglia | Chiave salvata |
|---|---|---|
| Blood Enemy | -100 | `nemesis` |
| Enemy | -70 | `enemy` |
| **Rival** | -45 | **`despised`** |
| **Distrusted** | -25 | **`hated`** |
| Wary | -10 | `disliked` |
| **Unknown Scent** | 0 | **`stranger`** |
| Acknowledged | 15 | `acquaintance` |
| Trusted | 35 | `friend` |
| Pack | 55 | `close_friend` |
| Pack-bonded | 75 | `best_friend` |
| **Beloved** | 92 | **`romantic_interest`** |

**Falsi allarmi chiusi.** L'AI riceve l'etichetta, non la chiave (wiki: *"The
tier name is what the sidebar shows, what the AI sees in the relationship
block"*). Quindi Erik verso i figli legge **Beloved**, non `romantic_interest`,
e non c'era niente da correggere. Allo stesso modo `despised` e `hated` non
erano chiavi orfane: sono semplicemente **Rival** e **Distrusted**.

**Da ricordare:** la corrispondenza è posizionale sulla ladder. Aggiungere,
togliere o riordinare un gradino rimappa il significato di tutte le attitudes
già salvate.

## Correzioni applicate alle 13 schede

| Problema | Stato |
|---|---|
| 5 Attitudes verso **The Player (Persona)** (Erik, Logan, Malachia, Noah, Wulfnic), tutte con motivazioni scritte su Alyssa ma applicate a chiunque giochi, incluso chi gioca Jasper | **Convertite in World Character → Alyssa.** Zero righe persona rimaste |
| 11 bersagli scritti come **Generic (text)** col nome di un personaggio esistente | **Collegati come World Character.** Restano generic solo i 4 bersagli che non sono personaggi: il branco di Seven Hills, l'underground fighting circuit, la Court of the Night, le Rival Pureblood Houses, la cultura aziendale DCC |
| **Collegamento rotto** su Erik verso `_1CWpEG1JfdD3qfbz8pz8t` | Il testo dice *"il laicismo di Magnus"*: riassegnato a **Magnus Douglas III** |
| Attitude di **Noah verso la persona senza motivazione**, guscio vuoto a Beloved | Riscritta come Noah → Alyssa: la sorella che bandisce dalle feste su cui regna e che chiama protezione senza riuscire a dire la parola |
| Alyssa e Jasper mancanti su varie schede | Aggiunte ovunque mancassero |

**Correzione a una mia affermazione precedente:** avevo scritto che l'intensità
era a 1 su tutte le schede. Falso. Le schede di famiglia arrivate con l'import
hanno intensità reali e sensate (78, 90, 95, 100). **A 1 finiscono solo le
attitudes autorate ora dall'interfaccia lasciando il campo vuoto**, come era
successo alle tre di Andrew, poi portate a 85/50/50.

## Copertura Alyssa e Jasper dopo la fase 1

Tutte e 13 le schede hanno ora entrambi, tranne i due diretti interessati che
hanno l'altro. Nessun collegamento rotto, nessuna riga persona.

| Scheda | Attitudes |
|---|---|
| Erik Douglas | 10 |
| Logan Douglas | 8 |
| Malachia Douglas Bloodmoon | 7 |
| Andrew Campbell, Edric, Noah, Elizabeth, Magnus | 5 |
| Wulfnic, Nixara, Kaladin, Alyssa | 4 |
| Jasper | 3 |

## Verifica di non danneggiamento

Confronto campo per campo di tutte le 86 schede prima e dopo la fase 1:
**zero differenze** su `long_summary`, `summary`, `display_description`,
`final_instructions`, numero di outfit, numero di Dialogue Examples e blocco
RPG. Le uniche modifiche sono nelle Attitudes.

Nota: **Elizabeth Duskwood ha `long_summary` vuoto** e vive solo di `summary`
(577 caratteri) e cinque outfit. Non è un danno di questa sessione, era già
così: è una scheda di famiglia mai riscritta in JED+, da mettere in lista.

## Fase 2, ancora da fare

Le 23 schede lavorate senza nessuna Attitude:

Dullahan, Marcus Thornfield, Finnegan Novak, Casey Williams, Jared Thompson,
Hank Thompson, Tate, Oskar, Professor Loewe, Nikolaj Jökull, Iordan R. Vess,
Ariadne Cirillo, Stanley Davies Jr., Vincent Campbell, Barkley Rover, Zefir
Hvitskog, Ut Berg, Lord Cornelius Douglas, Bailey Rogers, Miles Airhardt, Rev,
Janice Thompson, Stanley Davies Sr.

Quelle dove il rapporto **è** il personaggio e vanno scritte bene: Marcus verso
Kaladin, Zefir e Ut verso Wulfnic, Oskar verso Andrew e Stan, Finn verso Alyssa
e Jasper e Vincent, Barkley verso Dullahan, Vincent verso Andrew e Finn.

Le altre 50 schede grezze restano fuori: verranno riscritte da zero e le
Attitudes si mettono in quel momento, secondo §16.
