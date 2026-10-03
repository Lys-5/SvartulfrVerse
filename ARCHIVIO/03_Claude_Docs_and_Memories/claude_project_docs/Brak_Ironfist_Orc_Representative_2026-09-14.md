# Brak Ironfist — Orc Representative, Blackwood Council (completato 2026-09-14)

Secondo dei sette rappresentanti delle specie minoritarie del Concilio a essere completato (dopo Zeera per i Demoni). Character ID Wyvern: `_zxj6rWxA8e6CNLP3DXrEK`.

## Origine e riscrittura

Brak nasce da una character card fantasy medievale fornita dall'utente (tre varianti della stessa scheda: capo clan orco in un matrimonio combinato con `{{user}}` per portare la pace fra il suo popolo e un regno umano confinante, con arco romantico completo e sezione sessuale esplicita). Come da §13 estesa, tutto l'arco del matrimonio combinato con `{{user}}`, la scena della morte per freccia di `{{user}}`, e i blocchi anatomici/sessuali espliciti **non sono stati portati nella scheda nuova**, esclusi fin dalla lettura del materiale sorgente.

Quello che è stato portato avanti dal materiale originale: aspetto fisico (8ft, pelle verde pallida, cicatrice sulla guancia sinistra, voce come tuono lontano), personalità (protettivo, leale, stratega, testardo, diffidente verso gli estranei, riluttante al cambiamento), voce (frasi brevi, tono diretto), l'archetipo del capo clan che ha ereditato la leadership dal padre dopo conflitti sanguinosi, e alcune battute/mannerism riadattate nei nuovi Dialogue Examples (il "This is dishonor. I will not stand for it", il "Strange. It feels good..." con soggetto cambiato).

## Concept sviluppato in chat con l'utente

- **Riambientazione**: niente più villaggio di montagna medievale (Eldurin Mountains/Grom'kar) né guerra contro un regno umano. Diventa il capo di un'enclave orchesca arrivata a Blackwood una generazione fa, in fuga da conflitti generazionali fra clan orchi rivali (non da una guerra contro gli umani).
- **Professione**: fondatore e CEO di **Ironfist Forge & Structural**, azienda di lavorazione dell'acciaio, opere strutturali e infrastrutture di sicurezza industriale nel distretto di Ironworks. Dà legittimità economica al suo popolo a Blackwood e gli garantisce il seggio al Concilio come datore di lavoro e leader di comunità, non solo come ex-guerriero.
- **Il tema del matrimonio combinato**: rimosso del tutto, non riciclato nemmeno in forma anonima. Sostituito con un matrimonio combinato fra clan orchi (prima del trasferimento a Blackwood) diventato amore vero, e una moglie morta anni fa in un conflitto tribale prima del trasferimento, non per mano di terzi legati a `{{user}}`. Vedovo da allora, non risposato: tratto che il personaggio stesso mette in dubbio (devozione autentica o paura travestita da lealtà), sezione CLAN AND FORGE.
- **Età**: 47 apparente nella fonte, trattata come età reale (nessuna convenzione di longevità per gli Orchi ancora stabilita nel progetto, età umana-simile confermata dall'utente per questo personaggio). Birthdate/start_timeline_position: 10068966 (19 agosto 1976), coincidenti, età 47 al world_age corrente (10486470 = 5 aprile 2024).

## Cosa è stato scritto su Wyvern

Pipeline completa (§14) via API browser-driven, verificata con GET diretto dopo la scrittura (scanner automatico: zero `{{user}}`, zero em-dash, zero grassetto markdown, zero asterischi narrativi).

- `long_summary` in JED+ con sezioni BACKSTORY, CLAN AND FORGE (equivalente di FAMILY & PACK per personaggio senza legame di branco), VOICE AND BEHAVIOR, e la sezione tematica finale "WHAT HE WON'T FORGE AGAIN".
- `summary` in blocco PList compatto.
- `display_description`, `titles` (Orc Representative Blackwood Council; Founder & CEO Ironfist Forge & Structural), `nicknames` (Brak, Ironfist, Mountain's Shield), `keys`, pronomi he/him.
- **Outfit, cinque, contestuali**: Forge Floor (default), Council Session, Home, Formal Occasion, Site Security.
- **RPG Stats: non impostate**, come da pausa del sistema (§8, `world_features.rpg_stats` ancora `false`), pipeline seguita correttamente questa volta.
- **Dialogue Examples, cinque**: primo insediamento al Concilio, un subappaltatore che taglia sui materiali, un apprendista che chiede del vecchio clan, un membro del Concilio che gli contesta il seggio, un momento esposto in solitudine sulla moglie defunta.
- **Attitudes**: Alyssa e Jasper Douglas-Bloodmoon a tier "stranger" (mai incontrati), Erik Douglas a tier "acknowledged" (stesso schema usato per Zeera, rapporto politico principale senza vicinanza personale).
- **Global Character**: ON (`is_global: true`).

## Fix del 14/09: Intimacy Profile aggiunta

Come da nuova regola generale §13.3, è stata creata l'entry Lexicon **"Intimacy Profile - Brak Ironfist"** (id `_eAyLUFVH1wcxfYCK9hjC8`), formato standard (`is_global: true`, `party_conditions` `has_any` su Brak, `keys: ["Brak Ironfist","Brak","Ironfist"]`, `secondary_keys` su intimacy/dating/relationship/ecc., `priority: 50`). Contenuto scritto da zero in registro prosa, non una ricostruzione dell'arco matrimoniale originale verso `{{user}}` (quello resta escluso per intero secondo l'estensione 14/09): copre la sua chiusura emotiva dopo la morte della moglie, l'affetto mostrato attraverso i gesti più che le parole, la dominanza tranquilla e mai spettacolare, il limite invalicabile (essere affrettato oltre la cautela che il lutto gli ha insegnato) e il consenso più profondo (un partner paziente abbastanza da lasciargli credere che fidarsi di nuovo non costerà quanto è costata la perdita di lei). Verificato con GET fresca: zero `{{user}}`, zero em-dash, zero grassetto markdown.

## Note aperte

Nessuna relazione con altri membri del Concilio già scritti (Zeera, Huck, ecc.) inserita: il materiale sorgente e il concept sviluppato non danno base per inventarne (§9.4). Se in futuro emergono agganci narrativi fra Brak e altri rappresentanti, andranno aggiunte le Attitudes reciproche su entrambe le schede secondo §16.

Restano da assegnare quattro seggi del Concilio: Fatati, Umano con capacità magiche, Ibrido/Naga, Non-morto non vampirico.
