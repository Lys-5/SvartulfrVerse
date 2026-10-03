# Chiusura dei tre buchi sistemici sul roster SUCC (2026-09-13)

Seguito diretto di `Audit_Completezza_SUCC_2026-09-13.md`. Chiusi i tre gap trovati sulle 29 schede SUCC già considerate complete, lasciando fuori per ora solo Dialogue Examples/Attitudes mancanti su Eris Davies e Attitudes su Jasmin Thompson (lavoro creativo separato, non meccanico).

## 1. Format discipline in `final_instructions` (22 personaggi)

Aggiunta in coda, senza toccare il resto del testo esistente, la riga richiesta da §3:

> "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."

Applicata a: Archer Wolfwood, Ariadne Cirillo, Barkley Rover, Casey Williams, Chase Anderson, Dominic Rogers, Dullahan, Eris Davies, Finnegan Novak, Hank Thompson, Iordan R. Vess, Janice Thompson, Jared Thompson, Jasmin Thompson, Nikolaj Jökull, Oskar, Professor Loewe, Santiago Herrera, Stanley Davies Jr., Stanley Davies Sr., Tate, Tomas Matthews. Ora tutti i 29 personaggi SUCC lavorati hanno la riga.

## 2. Start Position e birthdate (14 personaggi)

Nessuno di questi 14 aveva né `birthdate` né `start_timeline_position`, solo un'età scritta in chiaro nel blocco JED+. Per ciascuno:

- Calcolata una data di nascita compatibile con l'età dichiarata rispetto a oggi nel World (world_age 10486470 = 5 aprile 2024), usando **date variate e non tutte al 1° del mese o al 1° gennaio**, come richiesto da §9.6.
- Scritti `birthdate` e `start_timeline_position` sullo stesso valore in ore (convenzione già osservata su tutte le altre schede SUCC con questi campi popolati: i due coincidono per un personaggio vivo, §6).
- Convertito il campo AGE nel blocco JED+ dal numero in chiaro alla macro `{{age}}` (§2), preservando l'eventuale nota qualitativa (es. Hank Thompson: "{{age}}, and passes for late thirties"; Jasmin Thompson: "{{age}}, and reads as late thirties").

Date di nascita usate: Casey Williams 1997-03-14, Finnegan Novak 2001-11-08, Hank Thompson 1973-06-23, Iordan R. Vess 1996-09-30, Janice Thompson 2003-02-17, Jared Thompson 2001-07-04, Jasmin Thompson 1975-10-12, Nikolaj Jökull 1996-01-29, Professor Loewe 1975-08-03, Stanley Davies Jr. 2002-12-05, Stanley Davies Sr. 1978-03-27, Tate 2001-04-30, Eris Davies 1981-02-22.

**Eccezione: Oskar.** Il suo blocco JED+ dice esplicitamente "Appears early twenties. He does not know and the question does not mean to him what it means to you", una scelta narrativa deliberata (è un RMH, Rapidly Mutating Hivemind, senza un passato tracciabile). Gli ho comunque assegnato `birthdate`/`start_timeline_position` (2001-05-19, coerente con "early twenties") perché il motore ne ha bisogno per posizionarlo correttamente nel World Clock, ma **non ho toccato il testo AGE in prosa**: resta "non lo sa" in scena, il dato numerico è solo meccanico e non contraddice la caratterizzazione.

## 3. `display_description` (15 personaggi)

Scritta una riga (una o due frasi) per ciascuno, basata sul `long_summary` esistente, senza inventare dettagli non presenti in scheda:

Ariadne Cirillo, Casey Williams, Eris Davies, Finnegan Novak, Hank Thompson, Iordan R. Vess, Janice Thompson, Jared Thompson, Jasmin Thompson, Nikolaj Jökull, Oskar, Professor Loewe, Stanley Davies Jr., Stanley Davies Sr., Tate.

## Verifica

Tutte le scritture via PUT parziale, **verificate dopo reload completo della pagina**: format discipline presente su tutti i 22, `start_timeline_position === birthdate` su tutti i 14, `display_description` popolata su tutti i 15, zero em-dash/`{{user}}`/markdown grassetto su tutti i campi toccati (`long_summary`, `display_description`, `final_instructions`).

## Cosa resta aperto

- **Eris Davies**: ancora zero Dialogue Examples e zero Attitudes. Non toccato in questo giro (lavoro creativo, non meccanico).
- **Jasmin Thompson**: ancora zero Attitudes. Stesso discorso.
- I 17 personaggi mai iniziati restano scoperti, come da `Audit_Completezza_SUCC_2026-09-13.md`.
