# Audit completezza roster SUCC/Solarton (2026-09-13)

Controllo di tutti i 46 personaggi nella cartella Character "Solarton" (uno in meno dei 47 di prima: rimosso l'id orfano trovato nell'audit di `content_folders`, vedi `Audit_Content_Folders_Completo_2026-09-13.md`). Letti tutti i campi via API e confrontati con i requisiti della pipeline §14.

## 1. Stub grezzi, nessun lavoro di scheda fatto (17)

`long_summary` minimo o assente, zero outfit, zero Dialogue Examples, quasi sempre zero Attitudes. Coincidono esattamente con l'elenco già aperto dei personaggi SUCC da costruire da zero (task #118-120 mai chiusi):

**8 fully custom (mai iniziati):** Sierra, Rev, Scarlett Rose, Brittany Willow, Javier Sinclair, Aris Thorne, Talia Grimwood, Kai Mitchell.

**6 da cross-reference (mai iniziati):** Warg, Jake Thompson, Coach Mithers, Rue, Allegra Lumsden, Luisa Sanchez Rogers.

**3 in attesa di materiale dall'utente:** Adelin Coso, Venera Dolce, Hideo Reid.

Nessuna sorpresa qui, solo conferma che sono ancora tutti scoperti.

## 2. Schede iniziate ma con pipeline incompleta

- **Eris Davies**: ha `long_summary` in JED+ (3982 caratteri), 5 outfit con Default Outfit impostato, RPG Livello 43, ma **zero Dialogue Examples e zero Attitudes**. È il caso già noto (per questo era stata esclusa dal giro Outfit Hybrid/Full Shift). Manca il passo 9 e 10 della pipeline.
- **Jasmin Thompson**: card altrimenti completa (outfit, RPG, speech examples) ma **zero Attitudes**. Non era stata segnalata prima.

## 3. Buchi sistemici trovati sulle schede "già fatte" (29 su 46)

Tre gap ricorrenti, nessuno dei quali salta all'occhio scheda per scheda ma che riguardano un numero consistente di personaggi già considerati completi:

**`display_description` vuoto** (15 personaggi): Finnegan Novak, Hank Thompson, Iordan R. Vess, Janice Thompson, Jared Thompson, Jasmin Thompson, Nikolaj Jökull, Oskar, Professor Loewe, Stanley Davies Jr., Stanley Davies Sr., Tate, Casey Williams, Eris Davies, Ariadne Cirillo. È un campo richiesto dal passo 4 della pipeline (una o due righe su chi è il personaggio), attualmente assente.

**Start Position mancante** (14 personaggi): Casey Williams, Finnegan Novak, Hank Thompson, Iordan R. Vess, Janice Thompson, Jared Thompson, Jasmin Thompson, Nikolaj Jökull, Oskar, Professor Loewe, Stanley Davies Jr., Stanley Davies Sr., Tate, Eris Davies. Il §7 delle istruzioni è esplicito: "va sempre messa, senza eccezioni", proprio per via degli scenari fuori tempo (nave di Wulfnic, scenario 2499). Questi 14 comparirebbero oggi anche in quegli scenari fuori epoca.

**Riga di format discipline assente da `final_instructions`** (22 su 29): il §3 richiede esplicitamente che ogni scheda chiuda `post_history_instructions`/`final_instructions` con la riga "Format discipline: dialogue in quotes, actions and narration in plain text..." così da valere durante la chat vera, non solo negli esempi. **Ce l'hanno solo 7 su 29**: Andrew Campbell, Bailey Rogers, Fade Greymoor, Mackenzie Sanchez-Rogers, Roland Vickers, Vincent Campbell, Viola Carter. Mancano su tutti gli altri 22, inclusi personaggi altrimenti completi come Archer Wolfwood, Dullahan, Dominic Rogers, Chase Anderson, Barkley Rover, Santiago Herrera, Tomas Matthews e tutta la famiglia Thompson/Davies. È il gap più esteso trovato in questo audit, perché non si vede aprendo la scheda a occhio: bisogna guardare dentro `final_instructions`.

## Nota su Species/Occupation

Non incluso fra i gap da correggere ora: l'assegnazione RPG Species/Occupation è sospesa dal 2026-09-13 insieme al resto del passo 8 (vedi `Simulation_World_Features_Disattivate_2026-09-13.md`), quindi non è trattata qui come dato mancante urgente anche se resta vuota su gran parte del roster.

## Riepilogo numerico

- 46 personaggi totali nella cartella Solarton.
- 17 mai iniziati (stub).
- 29 con scheda avviata, di cui:
  - 2 con Dialogue Examples e/o Attitudes mancanti (Eris Davies, Jasmin Thompson).
  - 15 senza `display_description`.
  - 14 senza Start Position.
  - 22 senza la riga di format discipline in `final_instructions`.

Nessuna scrittura è stata fatta in questo passaggio: è solo l'audit. Resta da decidere con l'utente l'ordine in cui chiudere questi buchi.
