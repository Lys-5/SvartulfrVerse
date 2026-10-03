# Audit SQL e fix dei content (Wyldfire locale) — 16/09/2026

Lavoro svolto sul database locale `wyldfire.db` (world_id `6cfuc64QBr1Flf9nKndFy`), seguendo il workflow §17: backup numerato (`wyldfire.db.backup5-pre-content-fix-...`), scrittura via script Python, verifica `PRAGMA integrity_check` + conteggio righe, conferma che l'app fosse chiusa prima della scrittura, checkpoint del WAL, controllo di file `-wal`/`-shm` residui dopo il sync.

## Risultati dell'audit completo

**Characters (444 totali)**
- 290 sono stub espliciti "in attesa di fonte" (roster Fan OC iofan.uwu.ai), creati il 15/09. Non toccati: da compilare solo quando arriva il materiale, come da §9.4.
- 154 schede "lavorate": tutte complete su outfit, default outfit, speech examples, attitudes, long_summary in JED+, final_instructions con la nota di format discipline. Nessun residuo `{{user}}`, nessun markdown, nessun em-dash nei campi dialogo.
- Tutte le 152 schede lavorate (esclusi Alyssa e Jasper stessi) hanno l'Attitude verso **sia** Alyssa che Jasper Douglas Bloodmoon, come richiesto da §16.
- 400/444 senza avatar (arte, pipeline separata PixAI, non un problema di content testuale).
- Il campo "First Name" risulta vuoto su 303/444 schede: sembra una caratteristica strutturale della piattaforma (il nome vero vive nel campo NAME del blocco JED+), non un difetto di contenuto.

**Lexicon (239 totali)**
- Content mai vuoto. Nessun residuo `{{user}}` o markdown grassetto.
- **Fix applicato:** 9 entry item/vehicle (le "auto/moto/armi" dei personaggi: Zefir's Blade, Ut's Warhammer, Jasper's Porsche, Noah's Sedan, Logan's Harley, Wulfnic's Rolls-Royce, Erik's SUV, Malachia's Motorcycle, Alyssa's Yellow Beetle) avevano `is_global: true` ma **nessuna keys e constant: false**: di fatto non si sarebbero mai attivate in nessuna scena (bug funzionale silenzioso). Aggiunte keys primarie (il nome dell'oggetto) e secondarie (termini come "car", "motorcycle", ecc.) con `key_logic: AND_ANY`.
- Confermato che i tag `<Nome_Entry>` che avvolgono ~60 entry (inclusi tutti gli Intimacy Profile) sono un formato strutturale intenzionale e coerente (stesso pattern usato in `<Villa_Douglas>[LOCATION_ID: ...]` e `<Blackwood_City>[LOCATION_ID: ...]`), non residuo di import grezzo: non toccato.

**Environments (13 totali)** — Tutti con description e context_description ben scritte. Nessun problema.

**Locations (119 totali)** — Trovate 38 schede senza `context_description` (il campo usato "in_chat": senza di esso la Location non inietta nulla in scena nonostante appaia a posto nel browsing) e 7 con `context_description` ricca ma senza `description` (quella mostrata nel browsing/nelle card).

Fix applicati (66 aggiornamenti totali, tutti derivati da materiale già scritto nel World — nessuna invenzione):
- 14 Location con una buona `description` breve già esistente: quel testo è stato copiato/adattato anche in `context_description`, così la Location inietta davvero contenuto in chat (Solarton High School, Sidewinders Bar & Nightclub, Coastal Residential, Parking Lot B, Main Parking Lot, Dragon's Shortcut, Gallery, Sports Fields, Gym & Changing Facilities, Bulls Stadium, Administration, Supernatural Support Center, Additional Student Housing, Fraternity & Sorority Row, The Open Casket).
- 12 Location arricchite combinando la loro `description` con la frase specifica già scritta nell'Environment genitore (Los Angeles, Bakersfield, Ventura/Route 101, Simi Valley), che le nominava esplicitamente: Kern River Canyon, Parco Roulotte di Oildale, The Dusty Coyote Diner, Campi Petroliferi di Kern River, Skid Row, Molo 42, The Neon Mirage, Osservatorio Griffith, Hollywood, Beverly Hills, The Simi Valley Grid, Area di Servizio "The Halfway House".
- 6 Location completamente vuote ma nominate nella lore già scritta di World Info/Environment: DCC Tower, Eidolon Creative, Arcadia School, Blackwood General Hospital, Nightwine Hall, 101 Road. Scritte description + context_description minime derivate da quel materiale.
- 7 Location con `context_description` ricca ma senza `description`: condensata una riga di riepilogo dal testo esistente (The Underground Fighting Ring, Supernatural & Human Alliance, Vampire & Undead Association, Bigfeet Hiking Club, The Pack, Anime Club, Rory's Estate).
- **Pulizia formato:** "Supernatural & Human Alliance" conteneva un import grezzo non lavorato (tag annidati `<SUCC><sha>` e markdown grassetto `**Location:**`/`**Schedule:**`, in violazione di §3). Ripulita la formattazione senza toccare i fatti.

**Restano 5 Location senza alcuna fonte da nessuna parte nel World**, da NON inventare (§9.4): **Ventura Square, Simi Valley Infopoint, Bakersfield Square, Pershing Square, Solarton Square**. Servono indicazioni tue (anche minime) prima di scriverci qualcosa, oppure restano vuote come segnaposto dichiarato.

**Scenarios (3 totali)**
- "First College Day" aveva la Short Description vuota: aggiunta una riga derivata dal proprio setup già esistente (Villa Douglas, Blackwood City, roster personaggi).
- **Da verificare con te:** "First College Day" inizia a world-hour 10489896, superiore al world_age massimo confermato (10486470h = 5 aprile 2024). Non toccato: potrebbe essere intenzionale (inizio anno accademico dopo la fine della storia registrata a oggi) o un refuso da correggere/estendere il World Time Span.

## Cosa NON è stato toccato e perché
- I 290 Character stub: aspettano fonte per esplicita policy del progetto.
- Le 5 Location "Square/Infopoint" senza alcuna fonte.
- I tag strutturali `<Nome>[FIELD: ...]` su Lexicon/Location importanti: sono un formato voluto, non un difetto.
- La discrepanza temporale dello scenario "First College Day": segnalata, non corretta d'ufficio.
- Avatar mancanti (400 Character, molte Location): è un lavoro di pipeline artistica separato (PixAI), non un problema di dati/testo.

## Prossimo passo
Come da tua richiesta, ora si passa alla sistemazione dei Settings World: riattivare "Enable Relationships" (Systems) e provare a riattivare Inventory & Items + Currency & Economy in Simulation.
