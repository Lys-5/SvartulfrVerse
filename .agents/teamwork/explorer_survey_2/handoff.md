# Handoff Report — Svartúlfr Verse Standalone Lorebooks Emergent Lore Survey

- **Subagent**: `survey_explorer_2`
- **Parent Conversation ID**: `a6280f2d-32ae-4a10-82fa-5604ad40f230`
- **Date**: 2026-11-02T06:25:00Z
- **Target File**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_survey_2\handoff.md`
- **Status**: Complete & Verified (Read-Only Investigation)

---

## 1. Observation

### 1.1 Filesystem & Repository Layout
Direct inspection of `FINAL/` and `lorebooks/optimized/` revealed the repository structure and entry parity for all 6 standalone lorebooks:

1. **Svartúlfr - Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL`)**:
   - Path: `FINAL/Svartulfr_Lorebook_I.json` and `lorebooks/optimized/Svartulfr_Lorebook_I.json` (828,006 bytes, identical).
   - Metrics: `token_budget: 5000`, `total_entries: 237`, `len(entries) == len(lexicon) == 237`, `entries == lexicon: True`.
   - Types: 122 `concept`, 50 `item`, 20 `memory`, 16 `job`, 12 `creature`, 6 `faction`, 6 `lore/concept`, 3 `ability`, 2 `organization/faction`.
   - Magic Theory: Contains a dedicated canonical series of `Magic:` concept entries:
     * Line 189: `Magic: Necromancy` (`TjqjKs6otx7hZZgU_ICm8`, keys: `['Necromancy', 'Spirit Manipulation', 'Undead', 'Soul Magic', 'Reanimation']`)
     * Line 191: `Magic: Death powers` (`cl9L0cEDs-lppNwpP7TVj`)
     * Line 193: `Magic: Healing power` (`_evkO6ZSmrW5wAF9KOeaK`)
     * Line 195: `Magic: Light power` (`1HCS4ca5Ozqmx4FF5Sdsk`)
     * Line 197: `Magic: Shadow power` (`m3uROuQ8euxKUD38vODVI`)
     * Line 199: `Magic: Lightning Control` (`q2Cugx3zrej-Oi2C8aKJc`)
     * Line 201: `Magic: Matter/Elemental Manipulation` (`15XKkcPfrJ4xM2BukGu14`)
     * Line 56: `SUCC: Catalizzatori, Focus Runici & Sigilli d'Incanalamento` (item, ID `96UEJzEsDWq2dNoUAFD94`)
     * Line 124: `SUCC: Laboratori di Teoria Runica & Incantamento Applicato` (concept, ID `Q6XSfNl-Mqv0XgpXqNaUI`)
   - Observation: **Zero entries exist for Abyssal Magic or Void Magic**, leaving a distinct ontological vacuum in Lore I.

2. **Svartúlfr - Lorebook II (`_HfG7TeV6MJyj6bxMwxkpt`)**:
   - Path: `FINAL/Svartulfr_Lorebook_II.json` (835,573 bytes) and `lorebooks/optimized/Svartulfr_Lorebook_II.json` (833,919 bytes). Both have `entries == lexicon: True`.
   - Metrics: `token_budget: 5000`, `total_entries: 142`, `len(entries) == len(lexicon) == 142`.
   - Types: 70 `concept`, 22 `faction`, 14 `event`, 13 `memory`, 9 `location`, 7 `item`, 3 `creature`, 2 `ability`, 1 `lore/concept`, 1 `organization/faction`.
   - Tactical Items & Dungeon Gear:
     * Line 19: `Potions and Alchemical Recovery` (item)
     * Line 32: `Dungeon Cores` (item, ID `aZ3tqA2xcNn3mAB00K1nH`, keys: `['dungeon core', 'dungeon cores', 'mana crystal', 'mana crystals', 'core']`)
     * Line 139: `La Frattura: Lo Squarcio del Velo e l'Origine dei Dungeon Europei` (lore/concept)
   - Observation: Currently **zero standalone entries exist for Resonant Cylinders** in Lorebook II.

3. **Svartúlfr - Lorebook III (SUCC & Underworld) (`_9zWTGqYJNJ4BCDMj8gfcD`)**:
   - Path: `FINAL/Svartulfr_Lorebook_III.json` and `lorebooks/optimized/Svartulfr_Lorebook_III.json` (131,196 bytes, identical).
   - Metrics: `token_budget: 5000`, `total_entries: 46`, `len(entries) == len(lexicon) == 46`, `entries == lexicon: True`.
   - Types: 14 `faction`, 12 `event`, 11 `concept`, 7 `location`, 1 `item`, 1 `lore/concept`.
   - Content: Covers institutional academic life (SUCC, CUMS, athletic teams, student clubs, Greek life, Underworld syndicates).
   - Observation: Currently **St. Brugge Private Academy does NOT exist in Lorebook III**, despite Lorebook III having substantial unused capacity (only 46 entries with a 5000-token budget).

4. **Svartúlfr - Location (`_EjXxkmPVhpCXg8xABpFkK`)**:
   - **CRITICAL FILE DIVERGENCE OBSERVED**:
     * `FINAL/Svartulfr_Location.json` was modified into a raw JSON list of 188 objects representing the World Location topology (`world: "_YpX47fNraQFw2dD7TdycJ"`).
     * `lorebooks/optimized/Svartulfr_Location.json` is the genuine Standalone Lorebook (`id: "_EjXxkmPVhpCXg8xABpFkK"`, `token_budget: 5000`, `total_entries: 225`, `len(entries) == len(lexicon) == 225`, `entries == lexicon: True`).
   - Existing Location Entries:
     * Entry #51 (`ulTwlYo2jqObA7l_bFoa5`): `name: "St. Brugge Private Academy"`, `keys: ['St. Brugge', 'St. Brugge Private Academy', 'St Brugge', 'private academy', 'Seven Hills', 'Douglas', 'Blackwood']`, `secondary_keys: ['school', 'academy', 'Father Rev', 'Revazhael']`, length: 403 characters.
       - **Violation Observed**: Umbrella keywords (`private academy`, `Seven Hills`, `Douglas`, `Blackwood`) exist directly in `keys`.
     * Entry #48 (`UmuOEDRDjliMuEpyMbeRo`): `name: "La Dimora del Rifugio"`, `keys: ['La Dimora del Rifugio', 'Dimora del Rifugio', 'Dimensional Refuge', "Father Rev's Refuge", 'Dimension', 'Refuge', 'Father Rev', 'Sanctuary', 'Thermal Baths']`, length: 555 characters. Extradimensional sanctuary accessed via Father Rev's gold key.
     * Entry #84 (`Gbc-aAk3fC76kvFxvNArz`): `name: "Theta Iota Theta (TIT or ΘΙΘ)"`, keys: `['Theta Iota Theta (TIT or ΘΙΘ)']`. Co-inhabited by Sierra Cruz and Scarlett Rose; mentions Revazhael servicing the electrical wiring.

5. **Svartúlfr - NPC Primary (`_zwEqgEEzh12X6gHVmMKKC`)**:
   - Path: `FINAL/Svartulfr_NPC_Primary.json` and `lorebooks/optimized/Svartulfr_NPC_Primary.json` (1,663,467 bytes, identical).
   - Metrics: `token_budget: 7500`, `total_entries: 99`, `len(entries) == len(lexicon) == 99`, `entries == lexicon: True`.
   - All 99 entries are `type: "npc"`.
   - Existing Core Dossiers:
     * Entry #98 (`alyssa_world_dossier_2b54a223`): `name: "Alyssa Hvit Douglas Bloodmoon"`, `content` length: 18,146 chars. `selective: true`, `secondary_keys: ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`, `ignored_characters: ['_6exg3yPfe2eCDK4hTftkh']`, `ignored_personas: ['persona_1786335754946']`.
     * Entry #60 (`Vcj4h2TL4Usola2A4OOl6`): `name: "Jasper Svartr Douglas Bloodmoon"`, `content` length: 16,771 chars. `selective: true`, `secondary_keys: ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`, `ignored_characters: ['_t4J9aQNJM36cUKAP4wB4U']`, `ignored_personas: ['1792155173728']`.
     * Entry #58 (`RVmhUtNzKvHow_AExX-LR`): `name: "Kaladin Nargathon"`, Commander DCC Security / Vanguard, 17,772 chars.
     * Entry #94 (`fQHJanwGPD5nX-5jIpqym`): `name: "Archer Wolfwood"`, SUCC Chancellor, 10,167 chars.
     * Entry #51 (`6OPHMBS-rtYYZ0XQP3c54`): `name: "Marcus Thornfield"`, Vanguard operative, Project BlackWolf.
     * Entry #91 (`LqRTQ988rzB87CFokWGSw`): `name: "Barkley Rover"`, Bulls assistant coach, golden retriever demi-human.
     * Entry #42 (`pUHbCpwVHRbFmC_c5TQHw`): `name: "Santiago Herrera"`, Bulls offensive line, dragon demi-human.
     * Entry #92 (`eWYgfOsI15cq7zd0vm7Nu`): `name: "Bailey Rogers"`, Bulls offensive line, red-skinned demi-human.

6. **Svartúlfr - NPC Secondary (`_Uht3Ckz44JBDrPnUHq7LV`)**:
   - Path: `FINAL/Svartulfr_NPC_Secondary.json` and `lorebooks/optimized/Svartulfr_NPC_Secondary.json` (2,527,857 bytes, identical).
   - Metrics: `token_budget: 5000`, `total_entries: 212`, `len(entries) == len(lexicon) == 212`, `entries == lexicon: True`.
   - Existing Entries of Interest:
     * Entry #23 (`jmh0MajEsRwrm4UYU14mY`): `name: "Rev"`, `keys: ['Rev']`, `content` length: 5,167 chars.
       - Discrepancy Observed: Poses as 20yo Incubus, ARO frat member, TIT handyman. BUT contains section `MISTERY & MENTORSHIP: During Alyssa and Jasper's youth, Rev served covertly as the magic and history instructor at St. Brugge Private Academy...`. His true name secret identifies him as "Revazhael", but his activation keys contain ONLY `['Rev']`, meaning "Father Revazhael" or "Revazhael" never triggers this entry!
     * Entry #37 (`1TnBSs1poc0mTNG8R0OTx`): `name: "Kobal"`, `keys: ['Butler of La Dimora del Rifugio', 'Kobal', 'Kobal Butler', 'Maggiordomo di Padre Rev']`, 2,139 chars. Bound shadow spirit butler serving Father Revazhael and the twins.
     * Entry #92 (`bunD_crPBoA7FFi-QNTzw`): `name: "Warg"`, Head of Campus Security at SUCC (8'2" werewolf).
     * Entry #17 (`gyZ3SOAsx3M7l42RDqSeZ`): `name: "Adelin Coso"`, Head Coach of SUCC Bears hockey, on medical leave for surgery in August 2024.
     * Entry #211 (`npc_larek_steeltooth`): `title: "Larek Steeltooth"`, `type: null` (anomalous schema: missing `type: "npc"`, missing `avatar`, `custom_avatar_regex`, `lines_parsed`).

### 1.2 Verbatim Evidence from Primary Playtest Export (`scratch/chat_export_ftrtAD79eddk9Ue9Jr2WJ.json`)
The 46-turn live playtest session establishes foundational lore:
- **Msg 14, 16-17 (Chancellor Archer Wolfwood & Major Kaladin Narghaton)**:
  * Quote: *"Erik, ti stavo giusto cercando... Il nostro stimato allenatore Adelin Coso deve sottoporsi a un delicato intervento chirurgico nei prossimi giorni... Prendi in mano la panchina dei Bears per quest'anno, Erik, e avrai tutte le chiavi del nostro sistema di sicurezza."*
  * Quote: *"Archer si ferma sulla soglia, 'manda pure il tuo Maggiore Narghaton da Warg, il nostro capo della sicurezza, per il coordinamento.'"*
  * Establishes the exact tripartite security coordination: Erik Douglas head coach of Bears -> Major Kaladin Narghaton (DCC Security) integrates directly with Chief Warg (SUCC Campus Security).
- **Msg 2, 4, 20 (SUCC Football & Hockey Athletes)**:
  * Jared Thompson (7ft minotaur, quarterback, Bulls captain), Santiago Herrera (dragon demi-human, emerald scales, cinnamon/burnt sugar scent), Bailey Rogers (short/stout, black horns, red skin, spade tail, southern accent).
  * Barkley Rover (golden retriever demi-human assistant coach, pure dog ears on crown, no human ears).
- **Msg 24-29 (Theta Iota Theta Sorority Environment)**:
  * Marcus Thornfield delivering Alyssa's luggage in DCC black SUV under orders from Major Narghaton.
  * Sorority atmosphere: Bohemian chic, pillows, velvet, plants on window sills, cat-decorated router with antenna whiskers and Wi-Fi password `TIT<3`.
  * Larek Steeltooth (orc 3rd year computer engineering student, informal network admin sleeping in Michelle's room).
  * Roxy: cat demi-human girl living at TIT, tried flirting with Zefir.
- **Msg 32-41 (Suite 3 & Sierra Cruz & Zefir)**:
  * Sierra Cruz: lamia, 4-meter rainbow iridescent serpent tail coiled on floor, zero legs/feet, massive Grave Mistake horror-punk poster, heated carpet, studying Applied Necromancy.
  * Alyssa's Fur Nest: authentic wolf/game furs hunted personally by Wulfnic, plus large plush wolf "Wolfy" won by Wulfnic at a carnival when Alyssa was 7 (still smells of cedar and grandfather).
  * Zefir Hvitskog: 1200+yo Viking Firstborn disguised as 19yo Icelandic Pre-Med cousin (`White Ghost Scout Shroud`), called *minn snarvinda* by Alyssa, falls asleep peacefully in her fur nest clutching Wolfy after 48 hours awake.
- **Msg 42-45 (St. Brugge, Father Revazhael, Resonant Cylinders, Abyssal vs Void Magic)**:
  * Quote (Alyssa, Msg 42): *"Sorrido, 'li uso per creare i cilindri incantati e le pozioni per i dungeon.' Frugo nella borsetta e tiro fuori un piccolo cilindro colorato, grande quanto un indice, e che somiglia ad un flashlight. 'In pratica sono incantesimi congelati, basta spezzarli e l'incantesimo si libera. Sono utili per gli hunters che non sanno usare la magia... Li faccio da sola perché i maghi della DMHA si fanno pagare uno sproposito per realizzarli... posso personalizzare l'incantesimo sull'utilizzatore... io e Jasper siamo registrati tra gli hunter come personale di supporto.'"*
  * Quote (Sierra, Msg 43): *"'Incantesimi congelati su matrice cristallina... La cristallografia runica applicata è roba da tirocinio avanzato, non da primo anno... io e i miei compagni di Necromanzia usiamo cilindri standard della Gilda per i sigilli di contenimento, e metà delle volte si rompono a metà durante l'evocazione. Se i tuoi sono personalizzati sull'utilizzatore, vuol dire che calibri la risonanza magica individuale di chi li userà. Questo è, tipo, livello da pubblicazione accademica.'"*
  * Quote (Alyssa, Msg 44): *"'Ho fatto le scuole alla St. Brugge Private Academy... Lì, oltre alle materie base, ci sono corsi di magia, storia della magia, alchimia e altre discipline. Il mio maestro era un vecchissimo demone superiore, molto competente... Visto che io e Jasper eravamo molto portati, ogni tanto ci dava delle lezioni private avanzate. È stato lui a insegnarmi a fare i cilindri, e anche le basi della magia abissale.' Padre Revazhael e la sua voce che riempiva l'aula vuota come fumo nero, le sue mani pallide che guidavano le mie sopra la matrice cristallina mentre Jasper traduceva le rune dal banco accanto... Non mi ha mai fatto paura."*
  * Quote (Scarlett, Msg 45): *"'St. Brugge. Certo. La scuola per figli di papà soprannaturali dove le uniformi costano come un mese di affitto e il menù del pranzo include carpaccio di drago... E fammi indovinare, il 'vecchissimo demone superiore' era il tipo più gentile e tranquillo del pianeta, vero? Perché tutti i mostri veramente terrificanti che conosco sono sempre quelli che ti offrono il tè e ti chiedono come stai prima di, tipo, smembrare un esercito.'"*
  * Quote (Sierra, Msg 45): *"'Magia abissale... Alyssa, io non ho mai conosciuto nessuno che abbia studiato magia abissale con un demone superiore. I necromanti del mio dipartimento lavorano con entità del Vuoto e residue, ma l'Abisso è, tipo, un livello completamente diverso di teoria magica. Nessuno al dipartimento di Necromanzia ha mai pubblicato una monografia seria sugli intrecci tra magia abissale e runica cristallina.'"*
  * Quote (Zefir, Msg 45): *"Il corpo di Zefir non si muove, ma le sue orecchie bianche si sollevano di un centimetro al suono del nome di Revazhael... Il demone. Quello che le ha insegnato a mettere il vuoto in una scheggia di cristallo. Il Jarl lo sapeva e non lo ha ucciso. Significa che il vecchio lo giudicava innocuo, o che lo giudicava utile. Il Jarl non lascia vivere ciò che non può controllare."*

---

## 2. Logic Chain

From these direct observations, we derive step-by-step conclusions for the integration of the emergent lore:

### Step 1: St. Brugge Private Academy (Two-Pillar Architecture)
- *Premise*: St. Brugge is both a physical estate with Gothic architecture between Blackwood and Solarton, and a prestigious educational institution serving as the elite preparatory academy for high-society supernatural dynasties.
- *Location Integration*: Entry `#51` (`ulTwlYo2jqObA7l_bFoa5`) in `lorebooks/optimized/Svartulfr_Location.json` already represents the physical site. However, it currently contains broad keys (`Seven Hills`, `Douglas`, `Blackwood`, `private academy`) violating repo rules, and its description is only 403 chars.
  * *Remediation*: Clean `keys` to strictly specific identifiers (`['St. Brugge', 'St. Brugge Private Academy', 'St Brugge', 'Accademia St. Brugge', 'St. Brugge Academy']`). Expand narrative content to ~1,500 chars describing Gothic stone architecture, ward-locked esoteric libraries, shielded courtyards, and alchemy labs.
- *Lorebook III Concept Integration*: Lorebook III (`_9zWTGqYJNJ4BCDMj8gfcD`) covers academia and educational settings, currently holding only 46 entries with a 5000-token budget.
  * *Remediation*: Introduce a new `concept` entry: `St. Brugge Private Academy (Accademia Privata St. Brugge)` in Lorebook III. Detailing the institution's elite status, curriculum (merging standard excellence with magic, history of magic, alchemy, demonology, and runic science), tuition, attendance of Alyssa and Jasper, and Father Revazhael's role as master of magic and history.

### Step 2: Father Revazhael (Location, Schema, and Identity Reconciliation)
- *Premise*: Father Revazhael is canonically an Ancient Superior Demon ("vecchissimo demone superiore"), master/mentor of Alyssa and Jasper at St. Brugge, master of abyssal magic and runic crystallography, creator of the golden key to La Dimora del Rifugio, and monitored by Jarl Wulfnic Bloodmoon. On the SUCC campus, he poses as "Rev", a 20yo incubus affiliated with Alpha Rho Omega and handyman for Theta Iota Theta.
- *Placement Assessment (NPC Secondary vs NPC Primary)*:
  * *Option A (Recommended)*: Retain and upgrade Entry `#23` (`jmh0MajEsRwrm4UYU14mY`) in **Lorebook NPC Secondary (`_Uht3Ckz44JBDrPnUHq7LV`)**.
    - Rationale: In NPC Secondary, he is already co-located with his bound spirit butler Kobal (`1TnBSs1poc0mTNG8R0OTx`). NPC Secondary token budget is 5000 (currently 212 entries).
    - Upgrades needed: Update name to `Father Revazhael (Padre Revazhael / Rev)`; expand trigger keys from merely `['Rev']` to `['Father Revazhael', 'Padre Revazhael', 'Father Rev', 'Padre Rev', 'Revazhael', 'Rev']`; update JED+ prose to harmonize the ancient Superior Demon identity with the campus handyman persona; ensure valid avatar placeholder and complete `npc_info`.
  * *Option B (Alternative)*: Promote to **Lorebook NPC Primary (`_zwEqgEEzh12X6gHVmMKKC`)**.
    - Rationale: If the orchestrator considers the personal mentor of the twin protagonists and wielder of abyssal magic worthy of core status alongside Zefir, Ut, and Nixara. Primary currently has 99 entries (budget 7500), so adding him reaches exactly 100 entries.

### Step 3: Applied Runic Crystallography & Resonant Cylinders
- *Premise*: The playtest establishes a dual reality: Resonant Cylinders are physical, tactical dungeon items carried by hunters; Applied Runic Crystallography is the esoteric academic science behind their creation.
- *Lorebook II Integration (Item)*: Lorebook II (`_HfG7TeV6MJyj6bxMwxkpt`) houses tactical dungeon equipment, potions, and cores.
  * *New Entry*: `Cilindri Incantati a Risonanza (Enchanted Resonant Cylinders)` (type: `item`).
  * *Content*: Flashlight-sized crystalline cylinders storing frozen spells; snapped to activate instantly without mana or casting delay; calibrated to individual magical resonance; contrasted with brittle, commercial DMHA cylinders; handcrafted via precision laboratory glassware.
- *Lorebook I Integration (Theory & Discipline)*: Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL`) houses magic theory, runic research, and catalysts.
  * *New Entry*: `Cristallografia Runica Applicata (Applied Runic Crystallography)` (type: `concept`).
  * *Content*: The esoteric discipline fusing Norse runic engraving with crystal lattice matrices to safely contain high-tier spells (including elemental and abyssal matrices) in a dormant, frozen state. Taught by ancient masters like Father Revazhael.

### Step 4: Abyssal Magic vs Void Magic/Necromancy
- *Premise*: Sierra Cruz explicitly defines the distinction: SUCC Applied Necromancy operates with Void entities, soul-fire, and residual ectoplasm. In contrast, Abyssal Magic is primordial infernal power from the deepest Abyssal planes, wielded by Superior Demons like Revazhael.
- *Lorebook I Integration*: Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL`) contains the canonical `Magic:` series (Necromancy, Death, Healing, Light, Shadow, Lightning, Matter/Elemental).
  * *New Entry*: `Magic: Abyssal Magic (vs. Void Magic & Necromancy)` (type: `concept`).
  * *Keys*: `['Abyssal Magic', 'Magia Abissale', 'Abyssal powers', 'Abyss magic', 'Infernal Magic']`.
  * *Content*: Definitive breakdown of Abyssal Magic (chthonic, heavy, commanding, living infernal essence) versus Void Magic / Necromancy (entropy, departed souls, cold rift emptiness). Details why necromantic containment seals frequently break while runic crystallographic lattices can safely bind abyssal currents.

### Step 5: Alyssa & Jasper Dossiers Enrichment in NPC Primary
- *Premise*: Both dossiers (`alyssa_world_dossier_2b54a223` and `Vcj4h2TL4Usola2A4OOl6`) already contain substantial JED+ text (>16k chars) and strict persona protection (`selective: true`, `secondary_keys: ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']`, `ignored_characters`, `ignored_personas`).
- *Enrichment Points*:
  * *Alyssa*: Integrate Guild-certified healer status, dungeon support credentials, personalized resonant cylinder crafting via crystal lab glassware, and Suite 3 details (Wulfnic's hunted furs, Wolfy plush from 7yo carnival, roommate dynamic with Sierra and Scarlett, Zefir falling asleep in her nest).
  * *Jasper*: Integrate Sound & Acoustic Engineering studies, registered hunter/support status, runic translation assistance for Revazhael, terrifying aura putting KSA jocks to flight at Welcome Fest, and cyber-savviness horrified by TIT's kitten router.

### Step 6: Playtest Emergent Personnel & Locations
- *Major Kaladin Narghaton*: Update Kaladin's entry (#58 in NPC Primary) and Lorebook III / Location notes to explicitly record his direct operational coordination with Chief Warg (SUCC Campus Security) following Erik's appointment as Bears head coach.
- *Theta Iota Theta: Suite 3*: Add dedicated sub-location entry in `lorebooks/optimized/Svartulfr_Location.json` (`Theta Iota Theta: Suite 3`), capturing the second-floor suite shared by Alyssa, Sierra, and Scarlett, featuring Alyssa's fur nest, Sierra's heated carpet and 4m serpent coils, Grave Mistake posters, crystal glassware, and fairy lights.

---

## 3. Caveats

1. **File Target Ambiguity (`FINAL/Svartulfr_Location.json` vs `lorebooks/optimized/Svartulfr_Location.json`)**:
   - `FINAL/Svartulfr_Location.json` was previously rewritten as a 188-element list of World locations for `/api/worlds/{id}/locations`.
   - `lorebooks/optimized/Svartulfr_Location.json` is the actual standalone Lorebook (`_EjXxkmPVhpCXg8xABpFkK`).
   - *Recommendation*: Any updates to the Location Lorebook must be performed on `lorebooks/optimized/Svartulfr_Location.json` (or restore `FINAL/Svartulfr_Location.json` as the standalone lorebook, keeping the 188-list in `scratch/world_locations_188.json`).
2. **Father Revazhael's True Name Secret**:
   - The canon dictates that speaking his absolute true name ("Revazhael") aloud strips his demonic defenses and forces submission. In-character, he goes by "Rev" or "Padre Revazhael" (as a respectful title). Activation keys should include `Padre Revazhael`, `Father Revazhael`, `Father Rev`, `Padre Rev`, and `Revazhael`, but dialogue in-game should treat the true name binding as a closely guarded secret.
3. **Persona Anti-Collision Protection**:
   - Alyssa and Jasper dossiers in `Svartulfr_NPC_Primary.json` must strictly retain `selective: true` with `secondary_keys: ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo']` and `key_logic: 'AND_ANY'` so they never activate as duplicate entities when the player uses the Alyssa or Jasper Persona.
4. **Byte-for-Byte Parity (`entries == lexicon`)**:
   - Every file modification must keep `data['entries']` and `data['lexicon']` completely identical byte-for-byte to satisfy Wyvern frontend Zod schema validation.

---

## 4. Conclusion & Actionable Schemas

### 4.1 Master Allocation Matrix

| Emergent Lore Component | Target Lorebook | Target File | Entry ID | Type | Action |
|---|---|---|---|---|---|
| **St. Brugge Private Academy (Concept)** | Lorebook III (`_9zWTGqYJNJ4BCDMj8gfcD`) | `FINAL/Svartulfr_Lorebook_III.json` & `lorebooks/optimized/` | `succ_lb3_st_brugge_academy` | `concept` | Create new entry |
| **St. Brugge Private Academy (Location)** | Location (`_EjXxkmPVhpCXg8xABpFkK`) | `lorebooks/optimized/Svartulfr_Location.json` | `ulTwlYo2jqObA7l_bFoa5` | `location` | Remediate keys, expand text |
| **Father Revazhael (Superior Demon)** | NPC Secondary (`_Uht3Ckz44JBDrPnUHq7LV`) | `FINAL/Svartulfr_NPC_Secondary.json` & `lorebooks/optimized/` | `jmh0MajEsRwrm4UYU14mY` | `npc` | Expand keys, reconcile profile |
| **Resonant Cylinders (Tactical Item)** | Lorebook II (`_HfG7TeV6MJyj6bxMwxkpt`) | `FINAL/Svartulfr_Lorebook_II.json` & `lorebooks/optimized/` | `lb2_item_enchanted_resonant_cylinders` | `item` | Create new entry |
| **Applied Runic Crystallography (Science)** | Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL`) | `FINAL/Svartulfr_Lorebook_I.json` & `lorebooks/optimized/` | `lb1_concept_applied_runic_crystallography` | `concept` | Create new entry |
| **Magic: Abyssal Magic (vs. Void/Necromancy)** | Lorebook I (`_gwwCxCfQ6PQaLEjAQVpJL`) | `FINAL/Svartulfr_Lorebook_I.json` & `lorebooks/optimized/` | `lb1_magic_abyssal_magic_distinction` | `concept` | Create new entry |
| **Alyssa Dossier Enrichment** | NPC Primary (`_zwEqgEEzh12X6gHVmMKKC`) | `FINAL/Svartulfr_NPC_Primary.json` & `lorebooks/optimized/` | `alyssa_world_dossier_2b54a223` | `npc` | Enrich JED+ content |
| **Jasper Dossier Enrichment** | NPC Primary (`_zwEqgEEzh12X6gHVmMKKC`) | `FINAL/Svartulfr_NPC_Primary.json` & `lorebooks/optimized/` | `Vcj4h2TL4Usola2A4OOl6` | `npc` | Enrich JED+ content |
| **Theta Iota Theta: Suite 3** | Location (`_EjXxkmPVhpCXg8xABpFkK`) | `lorebooks/optimized/Svartulfr_Location.json` | `loc_theta_iota_theta_suite_3` | `location` | Create new entry |
| **Larek Steeltooth Schema Remediation** | NPC Secondary (`_Uht3Ckz44JBDrPnUHq7LV`) | `FINAL/Svartulfr_NPC_Secondary.json` & `lorebooks/optimized/` | `npc_larek_steeltooth` | `npc` | Fix `name` and `type` fields |

---

### 4.2 Exact Entry Specifications & Content Payloads

#### Entry 1: St. Brugge Private Academy (Concept in Lorebook III)
- **File**: `FINAL/Svartulfr_Lorebook_III.json` & `lorebooks/optimized/Svartulfr_Lorebook_III.json`
- **ID**: `succ_lb3_st_brugge_academy`
- **Name**: `St. Brugge Private Academy (Accademia Privata St. Brugge)`
- **Type**: `concept`
- **Keys**: `['St. Brugge', 'St. Brugge Private Academy', 'St Brugge', 'Accademia St. Brugge', 'St. Brugge Academy']`
- **Secondary Keys**: `[]`
- **Selective**: `false`
- **Key Logic**: `AND_ANY`
- **Content**:
```text
St. Brugge Private Academy e un esclusivo istituto privato situato nei boschi periferici tra Blackwood City e Solarton, celebre per accogliere quasi esclusivamente la prole delle dinastie soprannaturali piu abbienti e influenti della West Coast. Le rette astronomiche e l'estrema riservatezza dell'ateneo sono leggendarie nel campus: l'ambiente e noto per uniformi sartoriali di altissimo costo e menu accademici d'elite.

A differenza delle accademie ordinarie, il piano di studi di St. Brugge fonde la rigorosa eccellenza preparatoria pre-universitaria con percorsi avanzati di magia formale, storia dell'arcano, alchimia sperimentale, demonologia e scienze runiche. L'istituto funge da principale bacino di reclutamento per atenei selettivi come la SUCC e la CUMS.

Alyssa e Jasper Douglas Bloodmoon hanno frequentato St. Brugge fin dall'infanzia, completando l'intero ciclo scolastico fino all'ammissione universitaria. Durante gli anni accademici, i gemelli sono stati seguiti con corsi privati avanzati da Padre Revazhael, enigmatico docente di magia e storia, che ha addestrato Alyssa nella cristallografia runica e nell'incantamento dei cilindri risonanti, e Jasper nella traduzione di rune arcaiche, forgiando le basi delle loro attuali competenze da dungeon hunter.
```

#### Entry 2: St. Brugge Private Academy (Location in Location Lorebook)
- **File**: `lorebooks/optimized/Svartulfr_Location.json`
- **ID**: `ulTwlYo2jqObA7l_bFoa5`
- **Name**: `St. Brugge Private Academy`
- **Type**: `location`
- **Keys**: `['St. Brugge', 'St. Brugge Private Academy', 'St Brugge', 'Accademia St. Brugge', 'St. Brugge Academy']` (Purged umbrella keywords: removed `Seven Hills`, `Douglas`, `Blackwood`, `private academy`)
- **Secondary Keys**: `['campus', 'academy', 'Father Rev', 'Revazhael', 'esoteric library']`
- **Selective**: `false`
- **Key Logic**: `AND_ANY`
- **Content**:
```text
Un sontuoso complesso accademico in pietra nera e granito gotico immerso nelle fitte foreste collinari tra Blackwood e Solarton. Il perimetro di St. Brugge e protetto da possenti barriere di interdizione acustica e sigilli arcanici che schermano completamente l'istituto dagli sguardi dei civili umani e dai droni non autorizzati.

L'architettura interna presenta chiostri colonnati, cortili alberati sorvegliati da doccioni incantati, aule a gradoni illuminate da vetrate runiche e biblioteche blindate contenenti testi rari di storia soprannaturale, erbologia e demonologia. I laboratori seminterrati ospitano banchi da lavoro in ardesia e quarzo per alchimia e cristallografia applicata.

In queste aule Alyssa e Jasper Douglas Bloodmoon hanno trascorso la loro giovinezza scolastica, ricevendo lezioni private e tutoraggio esoterico avanzato da Padre Revazhael lontano da occhi indiscreti, prima di fare il loro ingresso alla SUCC.
```

#### Entry 3: Father Revazhael (NPC Secondary Entry #23 Update)
- **File**: `FINAL/Svartulfr_NPC_Secondary.json` & `lorebooks/optimized/Svartulfr_NPC_Secondary.json`
- **ID**: `jmh0MajEsRwrm4UYU14mY`
- **Name**: `Father Revazhael (Rev)`
- **Type**: `npc`
- **Keys**: `['Father Revazhael', 'Padre Revazhael', 'Father Rev', 'Padre Rev', 'Revazhael', 'Rev']`
- **Secondary Keys**: `[]`
- **Selective**: `false`
- **Key Logic**: `AND_ANY`
- **Scan Persona**: `true`
- **Whole Words Only**: `true`
- **Highlight Keys**: `true`
- **Avatar**: `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public`
- **NPC Info**:
  * `first_name`: `"Revazhael"`
  * `middle_names`: `[]`
  * `last_name`: `None`
  * `nicknames`: `['Rev', 'Father Rev', 'Padre Rev']`
  * `titles`: `['Father', 'Padre', 'Superior Demon']`
  * `npc_prefix`: `""`
- **Content (JED+)**:
```text
[NAME: Revazhael; TITLE: Father Revazhael, Master of Abyssal Arts; ALIASES: Rev, Father Rev, Padre Rev; TRUE NAME SECRET: his absolute true demonic name is "Revazhael", an abyssal, hypnotic word that vibrates with ancient power. If any entity or mortal discovers and speaks it aloud, the syllables strip away his demonic armor, forcing him into agonizing, absolute submission and binding his will entirely to the speaker; AGE: Apparent 20, Chronological Ancient; BIRTHDAY: May 6; ZODIAC: Taurus (Sun), Scorpio (Ascendant), Pisces (Moon); SEX: Male; SPECIES: Superior Demon, Greater Incubus, Demon of Desire; ROLE: Alpha Rho Omega (ARO) fraternity member, handyman for Theta Iota Theta (TIT) sorority house, Former Master of Esoteric Arts at St. Brugge Private Academy; HEIGHT: 6'2" (188cm); BUILD: lean, wiry, athletic, moves with the unhurried grace of an apex predator; SKIN: soft reddish undertone holding faint internal heat; HORNS: dark, elegantly curled, sweeping backward; EARS: pointed, adorned with a heavy array of silver piercings; HAIR: ink-black, cascading loosely around his shoulders; EYES: warm liquid brown, filled with terrifying abyssal intelligence; TATTOOS: chest and arms heavily covered in intricate shifting demonic tattoos of black and deep red ink; VOICE: low, warm, dense, vibrating in the chest like a second heartbeat, able to fill a hall like black smoke; SCENT: warm vanilla, ember smoke, leather, and cinnamon; OUTFIT: sleeveless work shirts showing off tattooed arms, worn denim, tool belt around waist]

BACKSTORY: Father Revazhael is an ancient Superior Demon who has walked the mortal plane for centuries, deliberately choosing a path contrary to demonic destruction. Feeding exclusively on emotional energy through consensual intimacy, he refuses to take anything not freely offered. During Alyssa and Jasper's youth, he served covertly as the esteemed master of magic and history at St. Brugge Private Academy. Recognizing Jasper's uncanny intellect and Alyssa's inexhaustible spiritual conduit, Father Rev gave the twins advanced private lessons in botany, demonology, abyssal magic, and applied runic crystallography. He taught Alyssa how to forge crystalline resonant cylinders and gifted her the enchanted golden key to La Dimora del Rifugio, while instructing Jasper in ancient runes and gifting him the Abyssal Armor. Jarl Wulfnic Bloodmoon was fully aware of Revazhael's true nature and tolerated him, recognizing the demon as disciplined, non-hostile, and exceptionally useful. On the modern SUCC campus, Rev maintains a low profile as a laid-back 20-year-old student at Alpha Rho Omega and handyman for Theta Iota Theta, fixing locks, boilers, and wiring.

FAMILY & PACK: Bound by ancient pact and genuine paternal fondness to the Douglas-Bloodmoon twins, Rev acts as a quiet guardian from the perimeter. His bound shadow spirit butler, Kobal, maintains La Dimora del Rifugio in pristine condition for whenever Alyssa requires absolute sanctuary. At SUCC, after an early misunderstanding where Malachia and Kaladin bristled at his casual pheromones, Rev maintains a polite, respectful distance from Alyssa in public, knowing when not to push territorial Alphas.

VOICE & BEHAVIOR: Impeccably polite, calm, and disarmingly gentle. As students often note, the most terrifying monsters are always the ones who offer tea and inquire about one's day before unleashing cataclysmic power. He speaks with a low, melodic resonance that puts people at ease, treating consent as an inviolable metaphysical principle.

THE TRUE NAME HE GUARDS: Revazhael guards his true name above all else. Its utterance would strip away his infernal sovereignty, making its secrecy his single existential priority.

RPG STATS & TRAITS:
[LEVEL: 90; SPECIES: Succube & Incubo (Succubus) (STR -1, END -1, CHA +3, AGI +1); OCCUPATION: Teacher (INT +2); CLASS: Superior Demon & Arcane Master]
[STATS: STR 12; PER 16; END 14; CHA 18; INT 18; AGI 14; LCK 12]
TRAITS:
- Ancient Heritage (CHA +1, INT +1): Accumulated wisdom and dynastic mastery spanning centuries.
- Night Stalker (PER +1, AGI +1): Nocturnal predator operating with dark vision and supernatural stealth.
```

#### Entry 4: Enchanted Resonant Cylinders (Item in Lorebook II)
- **File**: `FINAL/Svartulfr_Lorebook_II.json` & `lorebooks/optimized/Svartulfr_Lorebook_II.json`
- **ID**: `lb2_item_enchanted_resonant_cylinders`
- **Name**: `Cilindri Incantati a Risonanza (Enchanted Resonant Cylinders)`
- **Type**: `item`
- **Keys**: `['cilindri incantati', 'cilindro incantato', 'resonant cylinders', 'resonant cylinder', 'cilindri a risonanza', 'enchanted cylinders']`
- **Secondary Keys**: `['matrice cristallina', 'incantesimi congelati', 'DMHA', 'Gilda', 'Alyssa']`
- **Selective**: `false`
- **Key Logic**: `AND_ANY`
- **Scan Persona**: `true`
- **Whole Words Only**: `true`
- **Content**:
```text
I cilindri incantati a risonanza sono manufatti magitech miniaturizzati, grandi quanto un dito indice e simili a piccole torce di cristallo tascabili, ideati per racchiudere incantesimi attivi in uno stato di sospensione criocristallina. All'occorrenza, l'utilizzatore deve semplicemente spezzare o premere il perno del cilindro per rilasciare istantaneamente la formula magica congelata all'interno, senza alcun tempo di lancio e senza consumare il proprio mana personale.

Questi dispositivi rappresentano uno strumento vitale per i cacciatori della Gilda e per gli operatori privi di doti magiche innate durante le incursioni nei dungeon e nelle fratture dimensionali.

A differenza dei comuni cilindri commerciali venduti a caro prezzo dai maghi della DMHA, che utilizzano matrici standard fragili soggette a incrinarsi o fallire durante le evocazioni critiche, i cilindri personalizzati forgiati da Alyssa Douglas sfruttano i principi della cristallografia runica applicata appresi da Padre Revazhael a St. Brugge. Alyssa calibra la frequenza della matrice di quarzo sull'impronta di risonanza magica individuale del ricevente, azzerando i rischi di rigetto e garantendo un'attivazione immediata e perfetta anche sotto stress estremo.
```

#### Entry 5: Applied Runic Crystallography (Concept in Lorebook I)
- **File**: `FINAL/Svartulfr_Lorebook_I.json` & `lorebooks/optimized/Svartulfr_Lorebook_I.json`
- **ID**: `lb1_concept_applied_runic_crystallography`
- **Name**: `Cristallografia Runica Applicata (Applied Runic Crystallography)`
- **Type**: `concept`
- **Keys**: `['cristallografia runica', 'runic crystallography', 'cristallografia applicata', 'applied crystallography']`
- **Secondary Keys**: `['matrice cristallina', 'risonanza', 'cilindri incantati', 'teoria runica']`
- **Selective**: `false`
- **Key Logic**: `AND_ANY`
- **Scan Persona**: `true`
- **Whole Words Only**: `true`
- **Content**:
```text
La cristallografia runica applicata e una disciplina esoterica avanzata di livello specialistico che fonde l'antica incisione di glifi runici nordici con l'ingegneria dei reticoli cristallini sintetici e naturali (quarzo sintonizzato, diamanti arcanici e frammenti di dungeon core).

Il principio fondamentale della disciplina risiede nel congelare formule magiche complesse all'interno delle giunzioni molecolari del cristallo, sospendendo il flusso energetico in uno stato di potenziale quiescente senza perdite di mana nel tempo. La tecnica richiede una rigorosa calibrazione della risonanza individuale: se la matrice runica non e armonizzata con la segnatura biospirituale dell'utilizzatore, il cristallo rischia di collassare sotto sforzo o detonare prematuramente.

Praticata ai massimi livelli da maestri occulti come Padre Revazhael e insegnata nei corsi avanzati di St. Brugge e nei laboratori specialistici di teoria runica della SUCC, questa scienza consente la produzione di cilindri a innesco rapido, barriere portatili e accumulatori ermetici per spedizioni nei dungeon della faglia.
```

#### Entry 6: Magic: Abyssal Magic (vs. Void Magic & Necromancy) (Concept in Lorebook I)
- **File**: `FINAL/Svartulfr_Lorebook_I.json` & `lorebooks/optimized/Svartulfr_Lorebook_I.json`
- **ID**: `lb1_magic_abyssal_magic_distinction`
- **Name**: `Magic: Abyssal Magic (vs. Void Magic & Necromancy)`
- **Type**: `concept`
- **Keys**: `['Abyssal Magic', 'Magia Abissale', 'Abyssal powers', 'Abyss magic', 'Infernal Magic']`
- **Secondary Keys**: `['Void Magic', 'Magia del Vuoto', 'Necromancy', 'demone superiore', 'Revazhael']`
- **Selective**: `false`
- **Key Logic**: `AND_ANY`
- **Scan Persona**: `true`
- **Whole Words Only**: `true`
- **Content**:
```text
La magia abissale e una corrente esoterica primordiale che attinge direttamente all'energia dell'Abisso Infernale, il piano chthonico governato dai Demoni Superiori. A differenza delle magie elementali ordinarie, l'energia abissale si manifesta con densita palpabile, fumo nero pesante, glifi cremisi incandescenti e un'intrinseca carica di volonta sovrana che scuote la realta materiale.

Sul piano della teoria magica accademica, e fondamentale non confondere la magia abissale con la magia del vuoto o la necromanzia classica:
1. Magia del Vuoto e Necromanzia: praticata nei dipartimenti specializzati come quello di Necromanzia Applicata della SUCC, opera sul vuoto tra le dimensioni, sulla manipolazione di residui spirituali ed ectoplasma, sulla decomposizione entropica e sull'animazione di materia morta. E un'arte fredda, legata alla dispersione e alle ombre dei defunti.
2. Magia Abissale: e un'energia vitale, caotica e rovente di origine demoniaca pura. Non manipola cadaveri ne anime erranti, ma incanala l'essenza stessa dell'autorita infernale e del patto primordiale.

Mentre le matrici necromantiche convenzionali risultano instabili e soggette a rotture impreviste, la magia abissale puo essere imbrigliata e stabilizzata se combinata con la cristallografia runica, come dimostrato dai metodi d'insegnamento di Padre Revazhael con Alyssa e Jasper Douglas Bloodmoon.
```

#### Entry 7: Theta Iota Theta: Suite 3 (Location in Location Lorebook)
- **File**: `lorebooks/optimized/Svartulfr_Location.json`
- **ID**: `loc_theta_iota_theta_suite_3`
- **Name**: `Theta Iota Theta: Suite 3`
- **Type**: `location`
- **Keys**: `['Suite 3', 'Suite 3 TIT', 'camera di Alyssa', 'stanza di Alyssa', 'TIT Suite 3']`
- **Secondary Keys**: `['Sierra', 'Scarlett', 'nido di pellicce', 'Theta Iota Theta']`
- **Selective**: `false`
- **Key Logic**: `AND_ANY`
- **Scan Persona**: `true`
- **Whole Words Only**: `true`
- **Content**:
```text
La spaziosa suite situata al secondo piano dell'ala est della sorority house Theta Iota Theta (TIT), condivisa da Alyssa Douglas, Sierra Cruz e Scarlett Rose. L'ambiente riflette l'eclettica convivenza delle tre studentesse, unendo comfort lussuoso, tocchi punk e misticismo botanico.

L'ala vicino alla finestra e occupata dal terrario caldo e dai tappeti riscaldati di Sierra, dominati da un enorme poster della band garage-punk Grave Mistake, dove la lamia riposa le sue quattro metri di coda iridescente. Al centro della stanza, Alyssa ha allestito il proprio giaciglio trasformandolo in un soffice nido di cuscini e pellicce pregiate cacciate da nonno Wulfnic, custodito dall'enorme lupo di pezza Wolfy vinto alle giostre a sette anni. Sugli scaffali trovano posto gli alambicchi e la vetreria da laboratorio in cristallo usata da Alyssa per distillare essenze e preparare cilindri incantati.

La stanza e illuminata da file di lucine fairy lights e sorvegliata da Zefir quando la scorta familiare veglia sulla matricola. Sulla mensola del salone comune spicca il celebre router decorato a muso di gattino con password 'TIT<3'.
```

#### Entry 8: Larek Steeltooth Schema Fix (NPC Secondary Entry #211)
- **File**: `FINAL/Svartulfr_NPC_Secondary.json` & `lorebooks/optimized/Svartulfr_NPC_Secondary.json`
- **Target**: Entry `#211` (`npc_larek_steeltooth`)
- **Fix**:
  * Set `entry_id: "npc_larek_steeltooth"` (replace `id`)
  * Set `name: "Larek Steeltooth"` (replace `title`)
  * Set `type: "npc"` (currently missing)
  * Set `avatar: "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public"`
  * Set `custom_avatar_regex: true`, `lines_parsed: 1`, `avatar_activation_regex: "(?:^|\\n)\\s*(?:Larek Steeltooth|Larek)\\s*:"`
  * Set `exclude_from_recursion: true`

---

## 5. Verification Method

To verify the integrity, schemas, and byte-for-byte parity across all modified files, the receiving worker should execute:

```bash
# 1. Run schema and parity verification script
python -c "
import json

files = [
    'FINAL/Svartulfr_Lorebook_I.json',
    'FINAL/Svartulfr_Lorebook_II.json',
    'FINAL/Svartulfr_Lorebook_III.json',
    'lorebooks/optimized/Svartulfr_Location.json',
    'FINAL/Svartulfr_NPC_Primary.json',
    'FINAL/Svartulfr_NPC_Secondary.json'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    e = d.get('entries', [])
    l = d.get('lexicon', [])
    assert e == l, f'Parity error in {p}!'
    print(f'{p}: PASS (entries={len(e)}, budget={d.get(\"token_budget\")})')
"

# 2. Check for broad keys on NPC entries
python -c "
import json
broad_keys = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}
for p in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for entry in d['entries']:
        keys_set = set(k.lower() for k in entry.get('keys', []))
        overlap = keys_set.intersection(broad_keys)
        assert not overlap, f'Broad key violation in {p} on {entry.get(\"name\")}: {overlap}'
print('Zero broad keys on NPC entries: PASS')
"

# 3. Check for em-dashes and formatting discipline
python -c "
import json
for p in ['FINAL/Svartulfr_Lorebook_I.json', 'FINAL/Svartulfr_Lorebook_II.json', 'FINAL/Svartulfr_Lorebook_III.json', 'lorebooks/optimized/Svartulfr_Location.json', 'FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    assert '—' not in text, f'Em-dash violation in {p}!'
    assert '{{age}}' not in text, f'{{age}} macro violation in {p}!'
print('Formatting discipline (0 em-dash, 0 {{age}}): PASS')
"
```

### Invalidation Conditions
- Any occurrence of `entries != lexicon`.
- Any presence of em-dash (`—`) or `{{age}}`.
- Any broad/umbrella keyword on NPC triggers.
- Token budget exceedance beyond platform limits (NPC Primary capped at 7500, all others at 5000).
