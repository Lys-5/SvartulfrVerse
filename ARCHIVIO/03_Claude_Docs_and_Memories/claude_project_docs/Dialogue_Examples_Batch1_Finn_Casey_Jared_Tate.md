# Dialogue Examples — Batch 1 di N (Finnegan Novak, Casey Williams, Jared Thompson, Tate)

Primo blocco della lavorazione a batch da 3-4 concordata con l'utente per colmare il backlog di Dialogue Examples mancanti (`speech_examples` vuoto) su ~15 schede del roster SUCC. Nessun altro campo di queste quattro schede necessitava modifiche: `long_summary`, RPG, outfit, attitudes erano già completi da lavorazioni precedenti. Unico gap era `speech_examples = []`.

## Nota tecnica

Il primo tentativo di scrittura era fallito con `TypeError: window.CHECK is not a function`: uno script precedente aveva ridefinito `window.TOK`/`window.RAW`/`window.W` dopo un reload di pagina ma non `window.CHECK`, quindi la validazione pre-scrittura ha lanciato un'eccezione prima di qualunque PUT. Nessuna scrittura era avvenuta. Risolto ripartendo da zero in una nuova sessione browser: refresh token da Firebase, redefinizione completa di `window.CHECK` (scanner em-dash/`{{user}}`/markdown-bold), poi `window.RAW` per le chiamate API.

## Personaggi

### Finnegan Novak (`_pq3nBwweU9aVkRKVRJ2KQ`)
5 Dialogue Examples: greeting, celebrazione post-partita sul ghiaccio, attrito con il capitano Vincent Campbell (subito senza rancore aperto), il tell della coda quando qualcuno che ha scelto in silenzio parla con calore a qualcun altro, e la menzione del nome di Alyssa Douglas Bloodmoon (tutto vero quello che dice, niente di quello che dice è la storia reale).

### Casey Williams (`_KqmaNBhQYBxf7RmWU7W2k`)
5 Dialogue Examples: greeting nel laboratorio fotografico, gentilezza pratica non richiesta, un'opinione "ragionevole" sulla trasparenza nelle relazioni che è in realtà il suo pattern da red flag detto con voce calma, la maschera che scivola per un attimo quando si parla di un ex o partner nuovo, e la battuta sulla nonna Matilda che lascia intuire quanto di quella visione del mondo si sia tenuto.

### Jared Thompson (`_1JhayQC7pzY6TC4qRHTx9`)
Riletto integralmente il `long_summary` prima di scrivere (7519 caratteri) per confermare dettagli: family di nove figli, Beta Rho Omega, coda come tell incontrollabile, il compagno di stanza licantropo (LA FRIENDSHIP HE BROKE, verosimilmente Stan Davies Jr. vista la descrizione), i due trigger che uccidono il sorriso ("dumb" e "animal"), il timore reale sotto la maschera da J-Man (una brutta stagione dalla scadenza della borsa di studio). 5 Dialogue Examples: greeting da J-Man, rottura accidentale di una porta per non calcolare la propria forza, la coda che tradisce lo show-off, la difesa scomposta quando qualcuno nota che il compagno di stanza lo evita, e la reazione piatta (non assente, piatta) quando viene chiamato "animale stupido" in un litigio.

### Tate (`_DYmRyAw642RbzLF4EzPBL`)
Riletto integralmente il `long_summary` (7498 caratteri) prima di scrivere: Subject 36, l'arrangiamento con SUCC counselling, l'amico Elio Warren (altro dog demi-human, ha deciso loro fossero amici e non si è lasciato dissuadere), la paura dei dottori sopra ogni altra cosa, l'abitudine di rosicchiarsi le nocche, la convinzione letterale di essere un mostro. 5 Dialogue Examples: greeting che si offre come "Subject 36" per riflesso, un trigger di paura quando qualcuno nomina un appuntamento dal dottore, un collasso in loop verbale in un ambiente sovraffollato, l'interazione con Elio (segue borbottando ma la coda lo tradisce), e il momento in cui rifiuta una rassicurazione raccontando cosa ha fatto prima che SUCC lo trovasse.

## Verifica

Tutti e quattro verificati dopo reload completo della pagina (non solo status 200 sul PUT): `speech_examples.length === 5` per ciascuno, zero occorrenze di em-dash, zero `{{user}}`, zero grassetto markdown, su tutto il contenuto concatenato.

## Backlog residuo

Dopo questo batch restano da colmare (Dialogue Examples mancanti): Nikolaj Jökull, Iordan R. Vess, Stanley Davies Jr., Bailey Rogers, Janice Thompson, Richard Loewe, Ariadne Cirillo, Hank Thompson, Stanley Davies Sr., Jasmin Thompson — 10 personaggi, non 11: Tate era nella lista dei mancanti riportata a fine sessione precedente ed è stato coperto in questo batch.

Prossimo batch da 3-4 in attesa di conferma dell'utente su questo primo blocco, come da istruzione esplicita ricevuta ("a blocchi da 3-4, mostrami il primo blocco").
