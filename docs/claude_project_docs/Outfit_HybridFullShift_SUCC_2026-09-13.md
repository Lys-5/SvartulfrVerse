# Outfit Hybrid Shift / Full Shift, roster SUCC/Solarton (2026-09-13)

Seguito diretto del lavoro su Family (`Outfit_HybridFullShift_Family_2026-09-13.md`) e Pack (`Outfit_HybridFullShift_Pack_2026-09-13.md`). Su indicazione esplicita dell'utente, Blackwood e Los Angeles restano fermi per ora; qui si tratta solo il roster SUCC/Solarton, e solo i personaggi già lavorati in pipeline, non l'intera cartella da 47.

## Perimetro

Scansionata l'intera cartella Solarton (47 `entry_ids`). Identificati 7 licantropi via match su `SPECIES:` nel `long_summary`. Di questi:

- **6 eleggibili** (scheda già completa in pipeline): Mackenzie "Mac" Sanchez-Rogers, Iordan R. Vess, Stanley Davies Sr., Stanley Davies Jr., Chase Anderson, Archer Wolfwood.
- **1 escluso**: Eris Davies, scheda con `dialogueCount: 0`, giudicata non ancora completata in pipeline.

Altri 4 personaggi della cartella (Allegra Lumsden, Luisa Sanchez Rogers, Venera Dolce, Hideo Reid) sono stub grezzi senza campo `SPECIES:`, coerenti con i task ancora aperti di costruzione SUCC da zero: correttamente esclusi da questo giro, non toccati.

## Domanda sul modello di trasformazione, e risposta dell'utente

Prima di scrivere, notato che Stanley Davies Sr. e Jr. (Common Bloodline) avevano già in scheda un outfit "The Full Moon" che descrive una trasformazione involontaria mensile direttamente in lupo pieno, senza menzionare una forma Hybrid intermedia: possibile modello diverso da quello a tre stadi usato per i Douglas. Invece di assumere, ho posto la domanda esplicita all'utente con tre opzioni. **L'utente ha scelto "Stesso sistema Hybrid+Full dei Douglas"**: stessa struttura a due outfit per tutti, applicata uniformemente.

Questa scelta è stata poi confermata come corretta anche sul piano del canon interno consultando `LSE_01_Species.md` (vedi sezione sotto): il documento afferma esplicitamente che ogni licantropo possiede tre stadi morfologici distinti (Partial/Hybrid/Full) "indipendentemente da rango, religione o cultura", quindi anche i Common Bloodline SUCC hanno canonicamente accesso alla Hybrid Shift.

## Testi scritti

- **Mackenzie Sanchez-Rogers**: manto biondo scuro shaggy coerente coi capelli, occhi ambra. Full Shift e Hybrid Shift sviluppati dal tono "easy, unbothered" già stabilito in scheda.
- **Iordan Vess**: manto pallido e spesso, occhi rosso stanco, corporatura tozza non atletica coerente con la sua caratterizzazione da sedentario/online.
- **Chase Anderson**: manto color golden retriever (da cui il soprannome Goldie), atletico, coerente col personaggio da streamer.
- **Archer Wolfwood**: manto scuro striato d'argento coerente coi capelli, occhi ambra penetranti, forma riservata a questioni che l'ufficio del Chancellor non risolve a parole.
- **Stanley Davies Sr.**: outfit preesistente "The Full Moon" **rinominato** in "Full Shift" (testo originale intatto, non riscritto: nessuna duplicazione), più nuovo outfit "Hybrid Shift" aggiunto (pelo grigio coerente, zoppia umana che scompare anche qui).
- **Stanley Davies Jr.**: stessa procedura, "The Full Moon" rinominato in "Full Shift" (testo originale intatto), nuovo "Hybrid Shift" aggiunto (pelo scuro con marcature brindle, dogtags del padre che restano anche in forma trasformata).

Scritto via PUT parziale su `outfits`, verificato con reload completo: outfit count corretto per tutti e 6, zero em-dash/`{{user}}`/markdown grassetto.

## Rifinitura con LSE_01_Species.md

Su indicazione dell'utente ("usa i dati in LSE - Biology & Physiology per gestire meglio i tratti"), riletta la sezione "Morphology & Shift Classes" del documento. Punti rilevanti verificati contro i testi già scritti:

- Hybrid Shift = forma bipede, "Species True Form": i testi già usavano "This is his bipedal hybrid form" per tutti e 6, coerente senza bisogno di modifiche.
- Full Shift = forma quadrupede, non più potente della Hybrid ma specializzata (nota di design esplicita: evitare il tropo "Full Wolf = Super Saiyan"): i testi già usavano "This is his complete quadrupedal wolf form" per tutti, e nessuno conteneva un linguaggio di superiorità rispetto alla Hybrid, quindi nessuna correzione necessaria su questo punto.
- Full Shift è "larger than a natural wolf, size varies by individual and blood classification": questo dettaglio mancava nei quattro testi di nuova scrittura (Mackenzie, Iordan, Chase, Archer). Aggiunta una clausola esplicita in ciascuno ("already larger than an ordinary wolf the way every werewolf's full shift runs" e varianti), senza toccare nient'altro del testo.
- Stanley Sr. e Jr.: il loro Full Shift è testo preesistente conservato intatto per decisione already presa (non duplicare, non riscrivere un outfit già scritto dall'utente/fonte). Non modificato in questa rifinitura: già diceva "a large black wolf", coerente a sufficienza senza forzare una riscrittura di un testo che non è farina di questa lavorazione.

Le 4 correzioni scritte via PUT parziale (solo il campo `description` della entry Full Shift, resto dell'array intatto) e riverificate dopo reload completo: outfit count invariato, testo aggiornato confermato, zero em-dash/`{{user}}`/markdown grassetto.

## Bilancio

6 personaggi SUCC/Solarton completati su questo fronte (Mackenzie, Iordan, Chase, Archer, Stanley Sr., Stanley Jr.). Eris Davies resta esclusa fino a completamento della sua scheda. I 4 stub grezzi restano in attesa della build SUCC da zero (task aperti separatamente).

## Stato complessivo Family + Pack + SUCC (parziale)

21 personaggi trattati in totale sul fronte Hybrid/Full Shift: 11 Family (9 diretti + Edric con gate temporale + Nixara), 4 Pack, 6 SUCC. Blackwood (8) e Los Angeles (3) restano fermi in attesa, come da scope concordato con l'utente.
