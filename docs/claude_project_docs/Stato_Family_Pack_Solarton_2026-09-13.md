# Stato schede: Family, Pack, Solarton (SUCC) — rilevazione 2026-09-13

Rilevazione live via API, non da documenti d'archivio: i due doc di riferimento precedenti (`Roster_Canon_SUCC_Stato_Schede.md` e parte di `TODO_Consolidato.md`, entrambi del 7 settembre) sono superati su gran parte dei punti e vanno considerati storici, non correnti. Questo documento li sostituisce come fotografia dello stato attuale per queste tre cartelle.

Le tre cartelle esistono nel World come **Content Folders** di tipo Character: **Family** (12 schede), **Pack** (4 schede), **Solarton** (47 schede, è la cartella che di fatto contiene il roster SUCC, non esiste una cartella "SUCC" separata).

---

## Family (12 schede)

Tutte scritte, tutte JED+, nessuna vuota, nessuna con Attitudes a zero, nessuna con outfit a zero, Global Character ON su tutte.

| Personaggio | `long_summary` | Dialogue Ex. | Outfit | Birthdate | RPG Livello |
|---|---|---|---|---|---|
| Edric Douglas | 3925 | 3 | 5 | sì | 12 |
| Jasper Douglas Bloodmoon | 13844 | 3 | 5 | sì | 19 |
| Noah Douglas Bloodmoon | 7921 | 3 | 5 | sì | 25 |
| Elizabeth Duskwood | 7229 | 5 | 5 | sì | 76 |
| Magnus Douglas III | 5177 | 3 | 5 | sì | 85 |
| Erik Douglas | 16064 | 5 | 3 | sì | 55 |
| Logan Douglas | 7252 | 5 | 4 | sì | 49 |
| Malachia Douglas Bloodmoon | 11882 | 5 | 4 | sì | 28 |
| Nixara Bloodmoon | 3241 | 3 | 5 | sì | 30 |
| Wulfnic Bloodmoon | 10076 | 3 | 6 | **no** | **1199** |
| Alyssa Douglas Bloodmoon | 5815 | 3 | 11 | sì | 19 |
| Lord Cornelius Douglas | 4407 | 0 | 5 | sì | **RPG non abilitato** |

**Elizabeth Duskwood è stata sistemata** dopo il 7 settembre: allora era il caso peggiore del World (`long_summary` vuoto, niente birthdate, età scritta a mano, due em-dash). Oggi ha JED+ completo, birthdate, 5 dialoghi, zero em-dash. Non è chiaro da questa rilevazione quando è stata corretta, ma è confermata a posto.

**Da guardare:**
- **Wulfnic senza birthdate**, unico della cartella.
- **Lord Cornelius Douglas: zero Dialogue Examples e RPG Stats mai abilitate.** L'unico dei dodici con questo doppio buco.
- **Jasper e Noah hanno un'intestazione markdown estranea** in cima al `long_summary` (`# [Jasper]`, `# [Nome]`), prima del blocco `[NAME: ...]` vero e proprio. Non è un em-dash o un asterisco fuori posto, ma è comunque markdown dentro un testo del World, cosa che §3 vieta esplicitamente. Segnalato, non corretto.
- **Nessuna delle 12 schede ha Species/Occupation nelle RPG Stats**, eccetto Elizabeth Duskwood (unica con entrambi impostati). Coerente con quanto già noto: questi campi si scrivono solo via API e finora l'attenzione è andata al roster SUCC.
- **Wulfnic (1199), e nella cartella Pack Ut Berg (1201) e Zefir (1019), hanno il Livello RPG impostato all'età reale**, non al tetto convenzionale di 99 che le istruzioni di progetto (§8) prescrivono esplicitamente per chi supera il secolo. Dato che lo stesso paragrafo documenta un bug di piattaforma per cui un Livello sopra ~100 fa fallire in silenzio l'intero blocco RPG, va verificato con un reload sull'interfaccia se questi tre stanno effettivamente salvando o se il blocco RPG risulta silenziosamente vuoto lì, nonostante l'API restituisca il valore.

---

## Pack (4 schede)

| Personaggio | `long_summary` | Dialogue Ex. | Outfit | Birthdate | RPG Livello |
|---|---|---|---|---|---|
| Kaladin Nargathon | 14772 | 3 | 3 | sì | 38 |
| Marcus Thornfield | 10229 | **0** | 3 | sì | 39 |
| Ut Berg | 7252 | **0** | 3 | sì | 1201 |
| Zefir Hvitskog | 9053 | **0** | 3 | sì | 1019 |

Tutte JED+, tutte con birthdate, tutte con Attitudes popolate, Global ON. **Tre delle quattro non hanno un solo Dialogue Example** (solo Kaladin ne ha). Nessuna delle quattro ha Species/Occupation nelle RPG Stats. Stessa osservazione di cui sopra su Ut Berg e Zefir e il tetto di Livello.

---

## Solarton / roster SUCC (47 schede)

**Una entry fantasma**: l'id `_KNFPcrCMR1GB6RqcY9D3d` compare nella cartella Solarton ma il Character dietro **non esiste più** (`GET` risponde 404). È un riferimento orfano lasciato da una cancellazione, non un personaggio mancante da scrivere. Segnalato per pulizia della cartella, non corretto in questa rilevazione (rimuovere un singolo entry_id da un Content Folder via API è un'operazione delicata, da fare con cautela e non come effetto collaterale di un controllo di stato).

**Le due schede davvero vuote**: Allegra Lumsden, Luisa Sanchez Rogers. Uniche due a `long_summary` a zero caratteri su tutta la cartella.

**Il roster "in evidenza" (i 26 nomi del canon SUCC, censiti il 7 settembre) è oggi in ottimo stato.** Tutti i buchi che il documento del 7 settembre segnalava come aperti su questo gruppo sono stati chiusi nelle sessioni successive:
- Fade Greymoor, Mackenzie Sanchez-Rogers, Roland Vickers: allora vuote, oggi scritte (rispettivamente 4033, 6296, 3210 caratteri), tutte con 5 Dialogue Examples e birthdate.
- Santiago Herrera, Chase Anderson, Tomas Matthews, Oskar, Bailey Rogers, Dominic Rogers: tutte completate in questa sessione, tutte con 5 Dialogue Examples.
- Il backlog dei "22 su 26 senza un solo Dialogue Example" segnalato il 7 settembre **è chiuso**: le due sessioni di batch di questa giornata (Finnegan Novak, Casey Williams, Jared Thompson, Tate, poi Ariadne Cirillo, Bailey Rogers, Iordan R. Vess, Jasmin Thompson, Stanley Davies Sr., Hank Thompson, Janice Thompson, Nikolaj Jökull, Stanley Davies Jr., Professor Loewe) hanno colmato l'intero buco.

**Quello che resta aperto sul roster in evidenza è solo la Birthdate**, non più i Dialogue Examples: mancano ancora su Iordan R. Vess, Finnegan Novak, Barkley Rover, Professor Loewe, Eris Davies, Jasmin Thompson, Stanley Davies Sr., Hank Thompson, Oskar, Janice Thompson, Stanley Davies Jr., Jared Thompson, Casey Williams, Tate, Nikolaj Jökull, Dullahan. Sono 16 su 26, quindi la maggioranza del roster in evidenza non può ancora usare la macro `{{age}}` e porta l'età scritta a mano dove compare.

**Il buco reale della cartella Solarton è un secondo strato, distinto dal roster in evidenza**: un gruppo di 17 NPC ancora a livello di abbozzo, tutti con `long_summary` sotto i 2000 caratteri, zero outfit, zero Attitudes e zero Dialogue Examples insieme:

Sierra, Rev, Warg, Scarlett Rose, Brittany Willow, Javier Sinclair, Aris Thorne, Jake Thompson, Talia Grimwood, Kai Mitchell, Coach Mithers, Rue, Adelin Coso, Venera Dolce, Hideo Reid, più le due vuote (Allegra Lumsden, Luisa Sanchez Rogers).

Coerente con quanto già registrato in `TODO_Consolidato.md` come "schede grezze/stub da passare in pipeline", solo che quel documento contava anche personaggi fuori da queste tre cartelle (Blackwood/Los Angeles), quindi i numeri complessivi lì restano più alti.

### Numeri di sintesi, Solarton

- 47 schede totali (46 reali + 1 riferimento fantasma)
- 2 completamente vuote
- 17 sotto i 2000 caratteri, tutte senza outfit/attitudes/dialoghi
- 19 senza Dialogue Examples in totale (le 17 sopra più 2 del roster in evidenza non ancora coperte da questa rilevazione incrociata)
- 20 senza birthdate
- 38 senza Species RPG, 37 senza Occupation RPG
- 18 senza RPG Livello impostato (RPG mai abilitato)
- 1 sola scheda non Global (da identificare quale, non ancora tracciata nominalmente in questa rilevazione)

---

## In sintesi, per priorità

1. **Le due schede vuote** (Allegra Lumsden, Luisa Sanchez Rogers) e la **entry fantasma** nella cartella Solarton sono il buco più visibile.
2. **Il secondo strato di 15 NPC stub** (Sierra, Rev, Warg, Scarlett Rose, Brittany Willow, Javier Sinclair, Aris Thorne, Jake Thompson, Talia Grimwood, Kai Mitchell, Coach Mithers, Rue, Adelin Coso, Venera Dolce, Hideo Reid) è il blocco di lavoro più grande rimasto sul roster SUCC, e replica esattamente il tipo di lavoro appena fatto su Bailey Rogers.
3. **Le 16 birthdate mancanti** sul roster in evidenza sono ormai il gap più diffuso lì, non più i Dialogue Examples.
4. **Lord Cornelius Douglas** (Family) è l'unico della sua cartella senza RPG e senza dialoghi.
5. **Wulfnic, Ut Berg, Zefir**: il Livello RPG segue l'età reale invece del tetto convenzionale di 99, da verificare se il blocco RPG sta davvero salvando sull'interfaccia data la soglia di bug nota.
6. **Jasper e Noah**: intestazione markdown estranea in cima al `long_summary`, da ripulire quando si ritocca la scheda.
