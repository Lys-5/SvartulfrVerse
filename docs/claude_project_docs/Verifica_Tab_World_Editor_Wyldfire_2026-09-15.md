# Verifica tab-per-tab del World Editor (Wyldfire, locale) — 15/09/2026

Verifica visiva completa di tutte le tab della sidebar del World Editor per il World "Svartúlfr", in ordine, via controllo remoto del PC (app Wyldfire desktop).

## SETTINGS

**World Info** — OK. World Name, Tagline, Description lunga, Rating (Explicit), Avatar e Background impostati.

**Simulation** — OK, coerente con la canon confermata.
- World Features: tutti i toggle di sistema (Inventory & Items, Currency & Economy, RPG Stats, Combat System, Cross-World Ships, Creature Catcher) risultano OFF, coerente con `world_features.rpg_stats: false` confermato via API il 14/09.
- World Time Span: 10486470 = "1197 years, 1 month, 6 hours documented", Recorded History Ends: April 5, 2024 — coerente col world_age riconfermato.
- Calendario: Gregorian Calendar, Epoch CE, Start year 827, Start month December, Start day 21, leap year ogni 4 anni +1 giorno a febbraio — tutto coerente con §6.
- Time of Day: 4 periodi (Dawn, Morning, Afternoon, Evening/Night... in realtà Dawn/Morning/Afternoon/Evening/Night, 5 periodi) tutti con descrizione.
- Campi opzionali vuoti (non segnalati come errore): System Prompt Override, Writing Style & Tone, Final Instructions a livello World, Regex Scripts, descrizioni dei mesi.

**Linked Characters** — Vuoto ("No characters linked yet"). Normale: il World usa solo Character nativi, non personaggi di libreria collegati.

## CONTENT

**All Content** — 818 elementi, vista aggregata di Lexicon/Location/etc. Righe visibili tutte compilate (Name, Keys, Type, Priority, Position).

**Characters** — 444 schede. Molte sono STUB dichiarati ("[STUB, in attesa di fonte. Nessun tratto ancora raccolto.]"), coerente col lavoro di stub in corso (vedi `Stub_FanOC_Creazione_313Schede_2026-09-15.md`). Spot-check su Adrian Locke: Long Description in formato JED+ corretto e completo, ma **campo "First Name" (obbligatorio, con asterisco) vuoto** — probabile caratteristica strutturale della piattaforma dato che il nome vero vive nel campo NAME del blocco JED+ dentro Long Description, non un problema di contenuto. Da tenere presente se in futuro si nota un blocco al salvataggio legato a questo campo.

**Lexicon** — 239 elementi, filtri per tipo (Concept, Event, Item, Job, Memory, Mob, Npc, Other, Vehicle) funzionanti, righe compilate con Keys e Position.

**Environments** — 13 elementi, tutti con descrizione e Position (`in_chat` per la maggior parte, `after_char` per DDM Inc. // Voidspace).

**Locations** — 119 elementi. **Trovate alcune schede vuote o incomplete**:
- "101 Road": nessuna Display Description, nessuna Description interna, nessun avatar/background, nessun Parent Location. Sembra uno stub mai completato.
- "Anime Club": Description interna presente e ben scritta, ma Display Description vuota (quindi non compare nulla nella colonna Content della lista/nelle card di browsing).
- Altre righe con colonna Content vuota nella lista (es. "Arcadia School") probabilmente nello stesso caso di "Anime Club" — non verificate una per una data la scala (119 schede).

**Scenarios** — 3 elementi. "First College Day" ben popolato (8 personaggi in pool, min/max characters, greeting) ma **Short Description vuota**. **Nota di coerenza temporale da verificare**: "When This Begins" = 10489896h, che è **superiore** al world_age massimo confermato (10486470h = 5 aprile 2024). Andrebbe controllato se è intenzionale (es. inizio anno accademico dopo la fine della storia registrata) o un refuso, e se il World Time Span va esteso di conseguenza.

**Import Assets** — Strumento funzionante, non richiede "compilazione".

## VISUAL & NARRATIVE

**Maps** — 2 mappe (Blackwood, California Coast), entrambe **0 pin · 0 route collegate**. Le mappe sono immagini illustrative ricche (distretti, etichette) ma senza dati interattivi collegati alle 119 Location esistenti.

**Eras** — 7 ere, tutte con descrizione e range orari coerenti e consecutivi (Age of Myth → Modern Era), coprono correttamente il world_age attuale.

**Relationship Trees** — **Vuoto**, nessun albero creato.

**Timeline Events** — 465 marker nel periodo T+1197y 31d 6h: 444 Characters, 3 Environments, 4 Locations, 14 Lexicon con posizione temporale. Conferma che la regola "Start Position sempre presente" (§7) è rispettata per i personaggi.

**Gallery** — 58 immagini presenti.

**Pages** — Non disponibile sulla piattaforma ("Soon").

## SYSTEMS

**Travel Routes** — Free Travel OFF, **0 route definite** (quindi `/travel` ricade sulle connessioni mappa, che a loro volta sono 0). Ship Arrivals abilitato ma **0 porti configurati**: feature attiva ma senza dati, di fatto non funzionante.

**Relationships — ⚠️ DISCREPANZA IMPORTANTE.** Il toggle "Enable Relationships" risulta **OFF** ("When off, the relationship panel and its combat/inventory integrations are hidden entirely"). Questo contraddice la canon in memoria secondo cui l'utente ha disattivato l'intero sistema di Simulation **tranne Relationships**. Con questo toggle spento, l'intero sistema di Attitudes/tier (§16 del workflow, presente su ogni scheda personaggio) risulta nascosto lato gioco. Non modificato in attesa di conferma dell'utente: potrebbe essere stato spento di recente/per errore, oppure la nota in memoria è obsoleta.

**InfoBoard** — Ben configurato: toggle attivo, categorie "Family Wanted Level" (progress bar 0-5 + status), "Biology" (Cycle, Scent), "Cover" (Eidolon Cover), "Surveillance" (DCC Coverage), più un Custom Prompt Override dettagliato e coerente con la lore (DCC, Villa Douglas, Dead Zone).

## Riepilogo priorità

1. **Verificare il toggle "Enable Relationships"** (Systems tab) — sembra in contraddizione con la canon salvata.
2. Verificare la coerenza temporale dello scenario "First College Day" (inizio oltre il world_age massimo registrato).
3. Completare o rimuovere gli stub di Location vuoti (es. "101 Road").
4. Valutare se popolare Display Description mancanti su Location con Description già scritta (es. "Anime Club").
5. Valutare se Maps/Travel Routes/Relationship Trees sono feature che si intende usare: al momento sono vuote/non collegate ai dati esistenti.

Non è stata fatta una verifica esaustiva campo-per-campo di tutte le 444 schede Character, 239 Lexicon e 119 Location: per quel livello di dettaglio, il workflow via API/SQLite (§11/§17) resta più efficiente di un controllo manuale via interfaccia.
