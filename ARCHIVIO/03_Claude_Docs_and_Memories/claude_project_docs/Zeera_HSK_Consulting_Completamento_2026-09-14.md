# Zeera — CEO di HSK Consulting, Rappresentante dei Demoni al Concilio (completato 2026-09-14)

Prima scheda costruita per il Concilio di Blackwood, primo dei sette rappresentanti delle specie minoritarie a essere completato. Character ID Wyvern: `_3DBJU9NCyKjEb84bfW6qn`.

## Origine e riscrittura

Zeera nasce da una character card di una variante fantasy del mondo (mercante di schiavi Vax, clan del sud), fornita dall'utente. Come da §13, tutta la componente di tratta di schiavi per sesso, il rapporto non consensuale con `{{user}}`, e i blocchi anatomici/sessuali espliciti **non sono stati portati nella scheda nuova**: non sono stati nemmeno trascritti per "ripulirli poi", sono stati esclusi fin dalla lettura del materiale sorgente.

Quello che è stato portato avanti dal materiale originale: aspetto fisico, personalità (dark humor, irriverente, freddamente sarcastico, spietato, dominante, duro), voce (fredda, baritonale, subdola), il concetto di specie Vax come demoni longevi (fino a 180 anni) organizzati in clan.

## Concept sviluppato in chat con l'utente

- **Riconversione professionale**: da mercante di schiavi a CEO di **HSK Consulting** (le iniziali giocano sul nome originale del clan, Horned Skull, senza dichiararlo apertamente), un'agenzia che presta personale a pagamento ad aziende di Blackwood. La DCC è uno dei clienti, non l'unico: questo gli dà indipendenza politica reale al Concilio.
- **Ascesa al potere**: parallelismo esplicito con l'arco narrativo futuro di Malachia. Zeera ha preso la guida del clan sconfiggendo il padre, ormai anziano, in un duello rituale della tradizione guerriera Vax. Il padre è sopravvissuto ed è ora consigliere sullo sfondo, un contrappeso emotivo sotto il cinismo del personaggio.
- **Tradizioni Vax modernizzate**: le pratiche guerriere del clan sono diventate una disciplina marziale quasi meditativa che Zeera pratica quotidianamente; i banchetti rituali sono diventati feste private, un misto di networking spietato e eccesso.
- **Specie Vax riscritta come razza in declino demografico**: i Vax rischiano l'estinzione perché la compatibilità riproduttiva fra partner è rara. Il vecchio metodo (rapire partner compatibili) è stato abolito fra i Vax rossi, sostituito dal corteggiamento, che per una cultura costruita sulla forza è un terreno molto più scomodo. La libido alta della specie resta come tratto ma è ricontestualizzata come pressione personale che Zeera non sa gestire con la stessa efficacia con cui gestisce il business, il suo punto debole esposto nell'ultimo speech example.
- **Seconda etnia Vax scoperta nel frattempo**: i Vax blu del nord (climi freddi, cultura del fated mate monogamo) sono stati registrati come lore di specie generale, non come personaggio, vedi sotto.

## Cosa è stato scritto su Wyvern

Pipeline completa (§14) eseguita via API browser-driven, verificata con GET diretto dopo ogni scrittura (nessun reload UI necessario, la GET autenticata è prova equivalente):

- `long_summary` in JED+ con sezioni BACKSTORY, CLAN AND COMPANY, VOICE AND BEHAVIOR, e la sezione tematica finale "WHAT HE CANNOT ACQUIRE" sulla pressione riproduttiva della specie.
- `summary` in blocco PList compatto.
- `display_description`, `titles` (Demon Representative Blackwood Council; CEO HSK Consulting), `keys`, pronomi he/him.
- **Outfit, cinque, contestuali**: HSK Boardroom (default), Discipline Practice, Private Gathering, Council Session, Off the Clock.
- **Start/Birth Position**: calcolata dal World Clock per un'età di 34 anni al world_age corrente (10486470 = 5 aprile 2024). Birthdate/start_timeline_position: 10188414 (5 aprile 1990), coincidenti come da convenzione per personaggi vivi.
- **RPG Stats**: abilitate via API dentro `rpg_stats` (§11/§15, non salvabili dall'interfaccia). Livello 34. Specie: Demons. Occupazione: CEO. Distribuzione punti (convenzione stat_1..stat_6 = MGT/RES/AGI/WIT/PRS/SCT, dedotta per analogia con altre schede del World che usano questo schema): MGT 8, RES 4, AGI 6, WIT 4, PRS 7, SCT 2, totale 31 come da convenzione del progetto.
- **Dialogue Examples, cinque**: un placement HSK andato storto, un dirigente DCC che spinge per l'esclusiva, qualcuno che gli chiede del padre, una seduta tesa del Concilio, e un momento esposto in solitudine sulla pressione riproduttiva della specie.
- **Attitudes**: Alyssa e Jasper Douglas-Bloodmoon a tier "stranger" (mai incontrati, nessun motivo di contatto), Erik Douglas a tier "acknowledged" (rapporto politico principale di Zeera a Blackwood, indipendenza deliberata da DCC).
- **Global Character**: ON (`is_global: true`).

### Nota sui tier delle Attitudes (chiarita dall'utente)

Il campo grezzo `tier` (`stranger`, `wary`, `acknowledged`, `rival`, `enemy`, `disliked`, `despised`, `hated`, `acquaintance`, `friend`, `close_friend`, `best_friend`, `romantic_interest`) è la chiave stabile salvata dall'API. La scala personalizzata del progetto (Blood Enemy, Enemy, Rival, Distrusted, Wary, Unknown Scent, Acknowledged, Trusted, Pack, Pack-bonded, Beloved) **è già attiva sul World**, ma agisce solo come rietichettatura in interfaccia: non sostituisce le chiavi grezze, le rinomina in visualizzazione. Quindi il tier `stranger` scritto per Alyssa e Jasper è corretto e stabile, comparirà nell'interfaccia con l'etichetta personalizzata corrispondente (verosimilmente "Unknown Scent" per quella posizione), e non serve nessuna rimappatura futura delle Attitudes già scritte. Nota precedente corretta.

## Verifica

GET diretto sulla scheda completa dopo tutte le scritture: zero occorrenze di `{{user}}`, em-dash, grassetto markdown o asterischi in qualunque campo. Cinque outfit con default valido, cinque dialogue examples, tre attitudes, RPG abilitate con specie e occupazione impostate, Global Character ON, birthdate e start_timeline_position coincidenti.

## Lore di specie scritta separatamente (Lexicon)

Due nuove entry Lexicon sul World, non legate a un singolo personaggio:

- **"Vax"** (tipo `mob`, `is_global: true`, id `_Wjptqk7qzxfYxzLAzxe68`): panoramica generale della specie, le due etnie (rossi del sud, ex mercanti di schiavi ora in gran parte riconvertiti al commercio legale; blu del nord, adattati al freddo, cultura del fated mate), il declino demografico condiviso, l'esilio marcato dalla rottura rituale di un corno.
- **"Vax - Reproduction and Compatibility"** (tipo `memory`, `is_global: false`, keys primarie `Vax` + secondarie su accoppiamento/fertilità/anatomia, id `_kBQh8xx2HMm1qjf6hAaBA`): meccanica riproduttiva in registro biologico/enciclopedico, non narrativo, spiega perché la compatibilità rara e la libido alta della specie siano la causa sia della crudeltà storica dei Vax rossi sia del declino demografico attuale.

Il materiale sulla seconda etnia (Yael, Vax blu del nord) è stato usato solo come fonte per arricchire la razza in generale, su richiesta esplicita dell'utente, e non è stato importato come personaggio.

## Fix del 14/09: Intimacy Profile aggiunta

Come da nuova regola generale §13.3 (Intimacy Profile per qualunque personaggio, invece di scartare il contenuto anatomico/kink consensuale), è stata creata l'entry Lexicon **"Intimacy Profile - Zeera"** (id `_MfPUdXVGH2yneMzkP8hKh`), formato standard (`is_global: true`, `party_conditions` `has_any` su Zeera, `keys: ["Zeera"]`, `secondary_keys` su intimacy/dating/relationship/ecc., `priority: 50`). Contenuto scritto da zero in registro prosa, **non** una ricostruzione del materiale originale escluso (quello resta escluso per intero secondo l'estensione 14/09, essendo legato a tratta e non consenso): copre la pressione biologica Vax sul drive sessuale, la dominanza naturale di Zeera, il suo bisogno di controllo anche in intimità, il limite invalicabile (essere trattato come una transazione) e il consenso più profondo (un partner che lo vuole per sé, non per l'azienda). Verificato con GET fresca: zero `{{user}}`, zero em-dash, zero grassetto markdown.

## Stato

Zeera è il primo dei sette rappresentanti delle specie minoritarie del Concilio a essere completato. Restano aperti: fatato (elfo o driade, da decidere), strega/stregone (da decidere), naga (da decidere), non-morto (spettro o ghoul, da decidere). Completati nel frattempo: Orco (Brak Ironfist), Umano (Huck Beaumont), Demi-human (Barrow).
