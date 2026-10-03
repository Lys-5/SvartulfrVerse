# Santiago Herrera — scheda completata

Fonte: card di `Iorveths` (janitorai.com), stesso autore/ecosistema delle schede Grave Mistake. La card esisteva già nel World come import grezzo (948 caratteri, zero outfit/dialoghi/attitudes/RPG, nessuna Start Position) ed è stata riscritta da zero in JED+, non ritoccata, come da §2.

**Stato finale (verificato dopo reload completo, non solo dopo il salvataggio):**

| Campo | Valore |
|---|---|
| display_name | Santiago Herrera |
| Nicknames | Santi, Tank |
| Titolo | Offensive Lineman, SUCC Bulls |
| long_summary (JED+) | 4.078 caratteri |
| summary (PList, stile Jared Thompson) | 838 caratteri |
| Outfit | 5: Game Day, Campus Casual, BRO House, Family Visit, Party |
| Default Outfit | Campus Casual |
| Dialogue Examples | 5: Introducing himself, Protective, Cooking for people, Being underestimated, **On his family** |
| Start Position / Birthdate | 10298160 = 12 ottobre 2002 (inventata, dichiarata: fonte non dava una data di nascita, solo "21 anni") |
| RPG | Lv.21, Demi-humans / Student, MGT 9 / RES 6 / AGI 3 / WIT 2 / PRS 6 / SCT 5 (25/25) |
| Attitudes | 6 (vedi sotto) |
| Global Character | ON (era già ON sull'import grezzo) |

Verifica finale: zero `{{user}}`, zero em-dash, zero asterischi/markdown, tutti i campi presenti dopo reload.

## Epurazione `{{user}}` (§13)

La fonte lo dava come fidanzato di `{{user}}`, con un Relationships block dedicato e un First Message intero (scena alla festa BRO, Santiago nota l'assenza di `{{user}}` per istinto da accumulo, lo trova messo alle strette da un vampiro in cucina, interviene). Rimosso integralmente il legame romantico fisso: in questo World `{{user}}` non è una persona fissa (può essere Alyssa, la ragazza di Jasper, Jasper stesso), quindi nessuna relazione romantica specifica poteva restare. L'istinto da accumulo/territorialità è stato tenuto come tratto generale (sezione THE HOARD), riferito a chiunque lui consideri suo, amici e famiglia compresi, non a un partner fisso. Il First Message originale non è stato riusato nemmeno in forma generalizzata: l'energia protettiva che descriveva è già coperta dal Dialogue Example "Protective".

Il blocco Intimacy della fonte (turn-on, sessualità, dettagli su cosa succede durante il sesso) non è stato trascritto nella description. È diventato una entry Lexicon separata, **"Intimacy Profile - Santiago Herrera"** (`_gUGnbbB3zwBjfLxDnKrm3`), tipo memory, `party_conditions has_any` sul suo stesso character id, sul modello delle entry già fatte per la Grave Mistake band. Tono allineato a quello di Roland Vickers: fatti e dinamica psicologica (l'istinto da accumulo non si spegne in camera, l'insicurezza sotto la sicurezza fisica), non coreografia esplicita.

## Discrepanza fonte (§9.2, segnalata non corretta)

Il blocco `<setting>` della fonte chiama la biblioteca del campus "Basilica Library". Il World la ha già come **Basilisk Library** (location `_V7c6QkdPg93E8Y8Rembp6`, già esistente). Non toccata la card di Santiago per questo, la libreria non vi compare; segnalato qui per chi userà quel blocco `<setting>` in futuro per altro materiale SUCC.

## Continuità con schede già esistenti

Non creato da zero: incastrato nel roster già stabilito.

- **SUCC BULLS** (Lexicon `_4CycwzbNpm1DWRPeT91ND`) elenca già Santiago tra i Known Players insieme a Jared Thompson e Bailey Rogers, sotto Coach Dullahan e Assistant Coach Barkley Rover. La card di Santiago ora nomina esplicitamente tutti e quattro nella sezione TEAM, invece di lasciarli come riferimento lorebook isolato.
- La card di **Jared Thompson** (già completa, 7 outfit, 5 attitudes) descrive tra i suoi amici più stretti "a demi-dragon fellow jock" senza nominarlo. È quasi certamente Santiago, quindi la relazione è stata resa esplicita e reciproca: attitude `close_friend` (70) su entrambi i lati concettualmente, anche se per ora scritta solo sulla card di Santiago (la card di Jared non è stata toccata in questa sessione, resta con quella descrizione anonima; toccarla per aggiungere l'attitude reciproca è lavoro residuo, non fatto).
- **Beta Rho Omega** (Location `_4LEj2zPX66hkh9hG2Fjdz`) già esisteva, non ricreata.

## Attitudes, con motivazione

| Target | Tier | Intensity | Perché |
|---|---|---|---|
| Alyssa Douglas Bloodmoon | stranger (Unknown Scent) | 15 | Non si sono mai incontrati, Solarton e Blackwood non si toccano per lui |
| Jasper Douglas Bloodmoon | stranger (Unknown Scent) | 15 | Non si sono mai incontrati |
| Jared Thompson | close_friend | 70 | Migliore amico in squadra, vedi sopra |
| Bailey Rogers | friend | 55 | Compagno di linea offensiva, protezione informale |
| Dullahan (head coach) | acquaintance | 40 | Rispetto, poca confidenza personale |
| Barkley Rover (assistant coach) | friend | 50 | Uno dei pochi adulti che non lo tratta da "dumb jock" |

## RPG, perché queste stat

MGT 9 perché è un lineman grosso e protettivo. AGI 3 bassa, i lineman non sono i più agili. WIT 2 basso ma non quanto quello di Jared (1): Santiago è più consapevole di sé stesso e del proprio essere sottovalutato, non è genuinamente ottuso come Jared. PRS 6 per l'energia sociale da festa/fraternity. SCT 5, istinto da drago/accumulo ma non un naso da lupo. Species Demi-humans (AGI+2, SCT+1) e Occupation Student assegnati via API dentro `rpg_stats`, come da bug noto (§11, §15).

## Lavoro residuo

- **Tomas Matthews** (Mu Alpha Nu, umano, simpatizzante Humans First) proposto come possibile abbinamento tematico: già ha birthdate/Start Position impostati ma zero outfit/dialoghi/attitudes/RPG. L'utente non ha ancora mandato materiale sorgente né confermato l'abbinamento.
- La card di **Jared Thompson** non è stata aggiornata per rendere esplicita la reciprocità dell'amicizia con Santiago (resta "a demi-dragon fellow jock" anonimo).
- **Nic ed Elena Herrera** (fratelli di Santiago) restano solo prosa di sfondo, non schede separate: la fonte non dava abbastanza per giustificarne una, coerente con §9.4.
