# Audit completezza schede: scoperta problema Long Description vuota (21/09, sessione pomeridiana)

## Contesto

Proseguendo il controllo di completezza schede richiesto ("controllo dei character per quanto riguarda la completezza delle schede e l'inserimento di outfits e dettagli"), è emerso un problema strutturale più grande e più urgente di outfit/dettagli mancanti: su gran parte del roster, il campo **Long Description è vuoto (0 Token)** e l'intera scheda JED+ è incollata nel campo **Short Description**, che dovrebbe invece contenere solo un riassunto condensato (1-2 paragrafi, per la voce Lexicon).

Questo non è quello che dicono le istruzioni di progetto (§2, §14.4): Long Description deve contenere il JED+ completo, Short Description un riassunto compatto separato.

## Metodo

L'anteprima della colonna CONTENT nella lista Characters mostra **solo lo Short Description**, quindi non basta a diagnosticare il problema: uno Short Description che comincia con `[NAME:...]` o `[SPECIES:...]` può essere sia il sintomo (JED+ intera incollata lì, migliaia di token) sia, in alcuni casi, un riassunto condensato legittimo che semplicemente usa la parentesi come stile (es. Jared Thompson, Short Description a 254 Token, del tutto corretto). L'unico modo affidabile è aprire la scheda e leggere il conteggio Token effettivo di entrambi i campi.

Il database locale Wyldfire (SQLite) non è utilizzabile per questa diagnosi: mostra `long_summary` vuoto per tutte le 360 schede, incluse quelle appena verificate come corrette sul sito (es. Erik Douglas, Jared Thompson), quindi è chiaramente disallineato rispetto al sito, che resta la fonte di verità.

## Popolazione del roster (360 personaggi)

- **205 placeholder segnaposto** (`STATUS: placeholder, in attesa di fonte`), creati il 15/09. Corretti così, non vanno toccati senza fonte (§9.4).
- **155 schede con contenuto reale.**

## Campione verificato individualmente sul sito (9 schede)

| Personaggio | Long Desc | Short Desc | Stato | Nota |
|---|---|---|---|---|
| Erik Douglas | popolata (migliaia di token) | condensata | OK | Completamento 20/09 |
| Alyssa Douglas-Bloodmoon | popolata | condensata | OK | Completamento 21/09 |
| Jasper Douglas-Bloodmoon | popolata | condensata | OK | Completamento 20/09 |
| Noah Douglas-Bloodmoon | popolata | condensata | OK | Completamento 21/09 |
| Malachia Douglas-Bloodmoon | popolata | condensata | OK | Completamento 21/09 |
| Logan Douglas | popolata | condensata | OK | Completamento 21/09 |
| Wulfnic Bloodmoon | popolata | condensata | OK | Completamento 21/09 |
| Jared Thompson | 1503 | 254 | OK | Completamento 21/09 |
| Mackenzie Sanchez-Rogers | 1410 | 70 | OK | Completamento 21/09 |
| Abel Vilas | **0** | 1055 | **ROTTO** | Nessun doc di completamento recente |
| Adelin Coso | **0** | 925 | **ROTTO** | Ha un doc `Adelin_Coso_Completamento_2026-09-13.md`, ma è rotto oggi lo stesso |
| Arthur Grey | **0** | 879 | **ROTTO** | Ha un doc `Arthur_Grey_Blackwood_Completamento_2026-09-14.md`, ma è rotto oggi lo stesso |
| Zero | **0** | (intera scheda) | **ROTTO** | Ha un doc `Zero_Wrath_Sinners_Completamento_2026-09-14.md`, ma è rotto oggi lo stesso |

## Conclusione del campione

**L'esistenza di un documento `_Completamento_` nel Project non garantisce che la scheda sia oggi corretta sul sito.** Tre schede con documento di completamento datato 13-14/09 sono risultate rotte (Long Description vuota) quando verificate oggi 21/09. Le uniche schede confermate corrette sono quelle con documento datato **20/09 o 21/09** (il giorno in cui, presumibilmente, è stato individuato e applicato il pattern giusto per la prima volta).

Ipotesi di lavoro, da trattare come tale finché non verificata a tappeto: **tutte le ~146 schede con contenuto reale rimaste, tranne le 9 già confermate corrette, sono probabilmente nello stato rotto** (Long Description vuota, JED+ intera nello Short Description). Il campione (5 schede non recenti su 5, provenienti da date e cluster diversi) è coerente al 100% con questa ipotesi, ma non è una verifica esaustiva.

## Prossimo passo concordato con Lys

Lys ha scelto la verifica sistematica completa: aprire ogni scheda con contenuto reale (una per una, l'anteprima lista non basta) e controllare Long/Short Description, outfit, Dialogue Examples, Attitudes. Lavoro in corso, proseguirà su più sessioni per la scala (~146 schede da controllare individualmente via browser, ~40-70 secondi per operazione di pagina secondo §15).

Split del lavoro pianificato:
1. Verifica individuale di ogni scheda rimasta → elenco definitivo rotto/corretto.
2. Per ogni scheda rotta: il contenuto in Short Description NON va perso, va spostato in Long Description (è già la scheda JED+ scritta bene), e va scritto un nuovo Short Description condensato nello stile dimostrato da Erik/Jared/Mackenzie (riassunto ALWAYS/NEVER/REMEMBER o prosa breve, non la scheda intera).
3. Documentare l'elenco finale e via via i personaggi sistemati.
