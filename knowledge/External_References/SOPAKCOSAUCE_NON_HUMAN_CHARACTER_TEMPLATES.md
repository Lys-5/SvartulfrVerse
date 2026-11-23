# SopakcoSauce Docs — Non-Human Character Templates (PList / SBF)

> **Fonte Ufficiale:** [SopakcoSauce Docs](https://sopakcosauce.gitbook.io/sopakcosauce-docs/plist-sbf-guides/templates/non-human-character-templates)
> **Integrazione Canonica:** Sistema di Classificazione e Modellazione Anatomico-Biologica per Character Card, Lorebook ed Entità Non-Umane in **Svartúlfr Verse** (Wyvern Platform Parity).

## Filosofia e Principi Operativi

1. **PList / SBF Strutturato**: Ogni specie possiede attributi specifici per delimitare l'anatomia della parte superiore ed inferiore, tipo di locomozione, apparato visivo/uditivo, organi sensoriali (pit organs, Jacobson's organ, baffi vibrisse), ciclo termoregolatorio, fisiologia viscerale e armi naturali.
2. **Positive Framing Puro**: Si descrivono sempre e soltanto le caratteristiche fisiche e biologiche effettivamente presenti nella specie di appartenenza (es. *smooth reptilian hearing membrane*, *single pair of canine ears*, *four equine legs*), senza mai elencare ciò che manca.
3. **Coerenza con il Tag System di WyvernChat**: Questa classificazione mappa esattamente le 31 categorie tassonomiche native supportate dal motore e dalla community di Wyvern.

## Indice delle 31 Categorie Tassonomiche
1. [Lamia & Naga](#1-lamia--naga)
2. [Merfolk](#2-merfolk)
3. [Elves](#3-elves)
4. [Orcs](#4-orcs)
5. [Trolls](#5-trolls)
6. [Arachne](#6-arachne)
7. [Kobolds](#7-kobolds)
8. [Centaurs](#8-centaurs)
9. [Minotaurs](#9-minotaurs)
10. [Fae](#10-fae)
11. [Fairy](#11-fairy)
12. [Giants](#12-giants)
13. [Gnome](#13-gnome)
14. [Vampire](#14-vampire)
15. [Werewolf](#15-werewolf)
16. [Undead](#16-undead)
17. [Succubus / Incubus](#17-succubus--incubus)
18. [Demon](#18-demon)
19. [Angel](#19-angel)
20. [Dragon](#20-dragon)
21. [Neko](#21-neko)
22. [Kitsune](#22-kitsune)
23. [Mutant](#23-mutant)
24. [Alien](#24-alien)
25. [Anthro (Anthropomorphic / Demi-Humans)](#25-anthro-anthropomorphic--demi-humans)
26. [Machine](#26-machine)
27. [Plant](#27-plant)
28. [God](#28-god)
29. [Object](#29-object)
30. [Cosmic Entity](#30-cosmic-entity)
31. [Abyssal Horror](#31-abyssal-horror)

---

## 1. Lamia & Naga

**Tag Canonico Wyvern / Sopakco:** `lamia_naga`  
**Intestazione Specie:** `SPECIES: naga(nagi, serpent-folk, lamia variant)`

### Lamia vs. Naga Comparison (Wyvern Tag Distinction)

| Caratteristica | Naga / Nagi | Lamia |
| :--- | :--- | :--- |
| **Genere / Varianti** | Versioni maschili (Naga) e femminili (Nagi) | Tradizionalmente solo femminile nel mito |
| **Origine Mitologica** | Mitologia Indù e Buddista | Mitologia Greca |
| **Morfologia Superiore** | Spesso con cappucci/teste multiple da cobra | Mantiene una singola testa dall'aspetto umanoide |
| **Tratti del Volto** | Tratti facciali più serpentini, squamati | Tratti facciali più umanoidi ed espressivi |
| **Fattore Squame** | Spesso squame estese anche sulla parte superiore del corpo | Raramente presenta squame sulla porzione superiore |
| **Braccia** | A volte raffigurati con quattro o più braccia | Quasi universalmente raffigurata con due braccia umane |
| **Elemento & Archetipo** | Associati all'acqua, saggezza e protezione divina | Associata al deserto, seduzione, pericolo e fascino |
| **Locomozione & Coda** | Si muovono strisciando (slither/glide/coil), coda costrittiva | Si muovono strisciando (slither/glide/coil), coda costrittiva |


### Template PList / SBF:
```text
[NAME: (full name);  
SPECIES: naga(nagi, serpent-folk, lamia variant);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (years, or equivalent if lifespan differs);  
HEIGHT: (overall length), torso height(human-equivalent portion);  
WEIGHT: (optional);  
BODY TYPE: upper(humanoid, muscular/slender/etc.), lower(serpentine, species: python/cobra/viper/etc.);  
SCALE COLOR: (primary), markings(stripes, patterns, underbelly);  
EYE COLOR: (slit-pupiled, color), eyelids(nictitating membrane, no lashes);  
SKIN (HUMANOID PORTION): (texture, tone, optional markings);  
LIMBS: arms(two), legs(none), tail(prehensile, dominant in locomotion);  
MOVEMENT: locomotion(slithering, vertical coil elevation), speed(burst vs. endurance), terrain(preferred terrain types);  
VOICE: sibilant, resonance(human-like, echoing, inhuman timbre);  
LANGUAGES: (spoken languages), species dialect(hissing, pheromone-laced, tongue-clicks);  
SENSES: vision(daylight, infrared/night vision), smell(Jacobson’s organ), heat detection(pit organs), touch scales(sensitive or armored);  
DIET: (carnivorous, blood-fed, egg-based, etc.), feeding(method: constriction, venom, fang-injection);  
ANATOMY NOTES: lungs(bi-lobed), heart(cold-blooded/variant), bones(flexible spine), genitalia(retractable hemipenes/cloacae/etc.);  
CLOTHING: upper(greaves, armor, draping cloth), lower(none, scale adornments);  
WEAPONS: fangs(venomous?), tail(strike force), hands(grappling, armed or clawed);  
MAGIC: (optional, if innate), resistance(cold/hypnosis/etc.);  
PSYCHOLOGY: temperament(cold-blooded, calculating/emotive?), territoriality(level), mating behavior(courtship rites, seasonal urges);  
SOCIAL STRUCTURE: solitary/tribal/clan-based/cultist, role within (title/status);  
BELIEFS: (serpent deity, reincarnation, domination-based hierarchy);  
CULTURAL TRAITS: communication(non-verbal cues: tongue-flicking, tail-thumps), taboos(interbreeding, eye contact, etc.);  
SCENT: musk, scale oil, (optional pheromone);  
TRIGGERS: (optional—touch aversion, sudden cold, disrespect rituals);  
PREFERENCES: habitat(underground, rainforest, desert), aesthetic(jewelry, hoards, silk, bones);  
WEAKNESSES: temperature sensitivity, limb-based combat, social distrust]
```

---

## 2. Merfolk

**Tag Canonico Wyvern / Sopakco:** `merfolk`  
**Intestazione Specie:** `SPECIES: merfolk(variant: mermaid/merman, aquatic humanoid)`

💭 **Ponder (Linee Guida di Worldbuilding):**
- **TRANSFORMATION:** se possono mutare in forma terrestre (stile Selkie / Sirenetta).
- **CYCLE:** comportamento migratorio o dipendenza dalle fasi lunari e maree.
- **MAGICAL ANATOMY:** se il corpo include rune coralline, bioluminescenza marina o organi branchiali arcani.

### Template PList / SBF:
```text
[NAME: (full name);  
SPECIES: merfolk(variant: mermaid/merman, aquatic humanoid);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (years or oceanic equivalent);  
UPPER BODY: torso(human-like or hybrid), skin(color, texture: slick/scaled/slimy), chest(human mammalian or marine), arms(two, webbed fingers?), hands(clawed or finned);  
LOWER BODY: tail(species: dolphin/shark/eel/fantasy), length(ft/m), tail fin(shape, span, movement);  
SCALE COLOR: (primary), underbelly(optional), sheen(iridescent, matte, bioluminescent);  
EYE COLOR: (pupil type, color), vision(adapted for low light, nictitating membrane);  
HAIR: (color, length, movement in water), often adorned with(seaweed, shells, coral);  
VOICE: tonal(hypnotic, melodic, croaking), underwater speech capability(yes/no), echolocation or sonar?(optional);  
LANGUAGES: (human languages), aquatic dialects(clicks, sonar pulses, whale-song);  
MOVEMENT: swimming(speed, propulsion style), surface locomotion(crawling, unable, water-bound);  
SENSES: vision(low-light/pressure-adapted), hearing(sonar-sensitive), touch(fin/tail), smell(waterborne trace detection);  
DIET: carnivorous/herbivorous/omnivorous(filter-feeding, raw fish, blood-drinking), feeding(method: hunting, scavenging, enchanting prey);  
ANATOMY NOTES: lungs(gill-breathing, dual-capable?), heart(chamber type), reproductive system(cloaca, external spawning, mammalian hybrid);  
CLOTHING: upper(decorative armor, sea-silk wraps, topless, coral jewelry), lower(none, scale-covered);  
SCENT: brine, oceanic musk, salt-crust, seaweed;  
MAGIC: hydromancy, siren song, tidal influence, shapeshifting(limited/full), ancestral memory;  
WEAPONS: claws, teeth, tail strikes, song-based charm/mind-affecting;  
TEMPERAMENT: alien logic, emotionally volatile, serene, curious, hostile to land-dwellers;  
SOCIAL STRUCTURE: pod/clan/solitary(choose), role(title, caste, song-keeper, warrior, wanderer);  
BELIEFS: oceanic pantheon, storm gods, sacrificial tides, oral traditions via song;  
CULTURAL TRAITS: courtship(singing, gift offerings, tidal dances), taboos(flesh-eating, shore contact, betrayal of the tide);  
TRIGGERS: dehydration, loud industrial noise, nets, oil slicks, polluted water;  
HABITAT: ocean depth range(surface dweller, trench-born, coral reef), biome preference(warm current, icy abyss, kelp forest);  
PREFERENCES: shiny objects, moonlight, shipwrecks, bioluminescence;  
WEAKNESSES: air exposure(limited duration?), vulnerability to fire, inability to walk]
```

---

## 3. Elves

**Tag Canonico Wyvern / Sopakco:** `elves`  
**Intestazione Specie:** `SPECIES: elf(subtype: high, wood, dark, astral, etc.)`

💭 **Ponder (Linee Guida di Worldbuilding):**
- **CASTE / LINEAGE:** se la linea di sangue influenza potere magico, rango sociale o tratti visivi.
- **RACIAL HISTORY:** sintesi mitica: dei decaduti, discendenza fae, esuli astrali.
- **AURA:** percezione da parte dei mortali (radiosa, inquietante, uncanny valley).

### Template PList / SBF:
```text
[NAME: (full name);  
SPECIES: elf(subtype: high, wood, dark, astral, etc.);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (chronological), apparent age(visual estimate);  
HEIGHT: (in ft/in or cm);  
BUILD: slender, willowy, athletic, etc.;  
SKIN: tone(shades: alabaster, obsidian, bark-brown, moonlit), texture(unlined, unnaturally smooth, radiant glow);  
EYES: shape(almond), pupil type(slit/normal), color(unearthly tones, liminal glint), vision(low-light, enhanced perception, magical sight);  
HAIR: color(silver, white, forest-hued, ink-black), texture(fine, silken), length;  
EARS: elongated, expressive(subtle twitching, emotive flicks), hearing(high-frequency detection);  
FACE: androgynous/sharp/symmetrical, signs of age(absent, unnatural preservation);  
VOICE: melodious, precise diction, accent(lilting, archaic);  
MOVEMENT: graceful, feline, near-silent, unnaturally fluid;  
LIFESPAN: centuries/millennia, immune to aging/disease until trauma;  
PHYSIOLOGY: metabolism(slow, hyper-efficient), immune system(resistant to illness/poison), sleep(meditative trance, 4 hours), blood(ichor-like, glowing?);  
SENSES: sight(low light, detail-oriented), hearing(supernatural acuity), smell(subtle scent tracking), magic perception(aura-reading, leyline attunement);  
MAGIC: innate affinity(school or element), casting(style: sung, gestural, sigil-based), racial abilities(telepathy, illusion, glamor);  
LANGUAGES: native(elvish dialect: lyrical, ancient), others(learned fluently, may view human languages as crude);  
CLOTHING: traditional robes, natural materials(leaves, silk, spirit-weave), armor(mithril, enchanted leather), footgear(barefoot or soft-soled);  
WEAPONS: bows(living wood, soul-bound), blades(elegant, curved, whisper-sharp), magic;  
SCENT: ozone, forest rain, crushed herbs, faint magic;  
TEMPERAMENT: serene, aloof, unhurried, calculating, long-memory vengeance or mercy;  
SOCIAL STRUCTURE: matriarchal/patriarchal/council-based, noble caste, seclusionist or expansionist;  
CULTURAL TRAITS: art(eternal perfectionism, soul-bound craft), ritual(seasonal rites, starlight communion), mating(bonded for life or emotionally distant);  
BELIEFS: pantheon(deathless gods, nature spirits, dream realms), philosophy(cycle of rebirth, memory as sacred);  
TABOOS: blood on sacred ground, interspecies breeding, desecration of relics;  
TRIGGERS: crude speech, iron contact(if allergic), sacrilege;  
PREFERENCES: starlight, quiet forests, harmonic sound, ancient ruins;  
WEAKNESSES: arrogance, frailty vs. brute force, infertility or limited reproduction]
```

---

## 4. Orcs

**Tag Canonico Wyvern / Sopakco:** `orcs`  
**Intestazione Specie:** `SPECIES: orc(subtype: mountain, plains, desert, feral, half-orc)`

💭 **Ponder (Linee Guida di Worldbuilding):**
- **RITES:** primo sangue, imposizione del nome, elevazione degli anziani, esilio.
- **MARKINGS:** tatuaggi rituali, pitture di guerra, marchi a fuoco (scopo e posizione).
- **HYBRID STATUS:** se mezzorco, definire retaggio (orecchie arrotondate, zanne ridotte, alienazione culturale).

### Template PList / SBF:
```text
[NAME: (full name);  
SPECIES: orc(subtype: mountain, plains, desert, feral, half-orc);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (years), maturity rate(fast/slow), lifespan(cap);  
HEIGHT: (in ft/in or cm);  
BUILD: massively muscular, thick-boned, wide-shouldered, etc.;  
SKIN: color(green, gray, red-brown, ash), texture(thick, leathery, scarred);  
EYES: color(yellow, red, black), pupils(round, bestial), vision(low-light, motion-focused);  
HAIR: texture(thick, coarse), color(black, charcoal, bone-white), style(tied back, shaved);  
TUSKS: length(curved upward or out), function(intimidation, fighting, ritual), grooming(prideful or ignored);  
FACE: features(flat nose, strong jaw, protruding brow), expression(resting snarl, stone-faced);  
VOICE: guttural, booming, accent(choppy, formalized tribal dialect);  
MOVEMENT: grounded, stomping or stalking, efficient gait, great leaping power;  
PHYSIOLOGY: heart(enlarged for combat), lungs(high-altitude or toxic air resistant), immune system(high toxin and pain threshold), regeneration(slow but reliable);  
SENSES: smell(blood scent, animalistic detection), hearing(ground vibration sensitive), taste(raw meat or fermented preferences);  
DIET: omnivorous(carnivorous lean), known to eat bone marrow, offal, and fermented roots;  
SLEEP: short cycles(4–5 hours), hypervigilant, combat-napping;  
WEAPONS: brute force(strikes, grapples), weapon preference(chopper, cleaver, crude blade), teeth/bite(fatal potential);  
CLOTHING: war-leathers, bone plating, scavenged metal, ritualistic paint or scars;  
SCENT: blood, ash, sweat, iron, fermented oils;  
MAGIC: rare(shamanic, blood-based, spirit-conduit), generally distrusted unless proven;  
TEMPERAMENT: territorial, honor-bound, vengeance-driven, expressive loyalty, open brutality;  
SOCIAL STRUCTURE: clan-based, matriarchal/patriarchal/chieftain-led, meritocratic(strength = rank);  
BELIEFS: ancestral spirits, blood-oaths, sacred violence, reincarnation through battle;  
CULTURAL TRAITS: naming(ceremony after first kill), mourning(scarification, silence), courtship(challenge fights, body presentation);  
TABOOS: cowardice, betrayal of clan, hiding wounds, using poison (unless cultural exception);  
TRIGGERS: insult to ancestry, flagrant dishonor, defiled totems;  
PREFERENCES: warmth, meat over fire, forge smoke, oral storytelling, the smell of wet stone;  
WEAKNESSES: rage blindsight, heat intolerance (for tundra-born), inflexible diplomacy]
```

---

## 5. Trolls

**Tag Canonico Wyvern / Sopakco:** `trolls`  
**Intestazione Specie:** `SPECIES: troll(subtype: cave, swamp, mountain, frost, bridge-dweller)`

💭 **Ponder (Linee Guida di Worldbuilding):**
- **REGENERATION RULE:** tempo di ricrescita arti, costo metabolico (carne/energia), vulnerabilità durante la rigenerazione.
- **ENVIRONMENTAL BOND:** pietrificazione alla luce solare, guarigione rapida nell'umidità, furia scatenata dal rumore.
- **EVOLUTIONARY ADAPTATIONS:** simbiosi fungina, corazza dorsale litica, ossa cave per eco-localizzazione.

### Template PList / SBF:
```text
[NAME: (name, often guttural or monosyllabic);  
SPECIES: troll(subtype: cave, swamp, mountain, frost, bridge-dweller, forest, corrupted);  
SEX: (biological sex);  
GENDER: (gender identity or non-classified);  
AGE: (chronological), maturity(slow-developing or ageless);  
HEIGHT: (extreme range: 7–20 ft+ depending on subtype);  
BUILD: massive, hulking, malformed, asymmetrical, grotesquely muscled, stooped or hunched;  
SKIN: color(sludge-green, stone-gray, blue, mottled), texture(warty, stone-like, pustulant, bark-thick), reaction to sunlight(immune, petrifying, flammable);  
EYES: number(1–2+), color(glowing, sunken), night vision(yes), light sensitivity(severe or mild);  
HAIR: sparse, matted, mossy, fungus-infested;  
FACE: brow(prominent), nose(flat or hook), jaw(jutting, tusked), teeth(jagged, uneven, constantly regrowing);  
LIMBS: long arms, knuckle-dragging gait, clawed hands, misshapen or club-like legs;  
MOVEMENT: lumbering, loping, wall-climbing, swimming;  
SCENT: rot, wet earth, sulfur, blood;  
VOICE: gravelly, phlegmatic, often incoherent or mimics speech;  
LANGUAGE: broken Common, troll dialect(grunts, smells, gestures), echolocation growls;  
SENSES: smell(death, prey trails), hearing(low-frequency detection), taste(raw flesh, iron aversion), sight(poor in daylight, acute in dark);  
PHYSIOLOGY: regenerative(extreme healing, limb regrowth), blood(thick, acidic or fungal-laced), digestive system(anything organic), bones(spongy but dense);  
VULNERABILITIES: fire, sunlight (if folkloric), silver, acid;  
MAGIC: rare but present(flesh-mending, shamanic curses, rotcraft);  
CLOTHING: primitive(skins, scavenged armor, fungal plates), sometimes ritual adornments(bones, totems);  
WEAPONS: brute force, claws, thrown boulders, tree-sized clubs, bite(powerful jaw pressure);  
TEMPERAMENT: violent, territorial, dim-witted or cunning(depending on lore), obsessive hunger, unpredictable calm;  
SOCIAL STRUCTURE: solitary or pack under dominance law, troll-kin tribes, bonded to troll matron/elder;  
BELIEFS: elemental worship(stone, rot, glacier), cursed ancestry, hoarding behavior(trophies of bone or metal);  
CULTURAL TRAITS: memory passed through scars, naming earned through kills, storytelling via blood-paint;  
TABOOS: aiding humans, fire usage, dishonoring kin bones;  
TRIGGERS: blood scent, trespass into lair, hunger pangs, sudden light;  
PREFERENCES: damp, cold, deep caves, carrion, iron smell, child-laughter as hunting bait (optional folkloric cruelty);  
WEAKNESSES: low intellect or cunning fixation, regeneration delay with certain damage types, compulsive behavior(bridge-guarding, question-answering, mimicry)]
```

---

## 6. Arachne

**Tag Canonico Wyvern / Sopakco:** `arachne`  
**Intestazione Specie:** `SPECIES: arachne(humanoid-arachnid hybrid, drider, webspawn, etc.)`

💭 **Ponder (Linee Guida di Worldbuilding):**
- **WEB TYPE:** tela a imbuto, tela a trappola, ragnatela orbicolare, filamenti adesivi/velenosi.
- **BROOD RANK:** portatrice di uova, sentinella, nata-vedova, casta divoratrice.
- **TRANSFORMATION:** se nata ibrida o trasformata da maledizione/mutazione.

### Template PList / SBF:
```text
[NAME: (full name or broodname);  
SPECIES: arachne(humanoid-arachnid hybrid, drider, webspawn, etc.);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (years or hatch cycles), lifespan(long-lived, ageless, accelerated aging);  
HEIGHT: total(ft/in or cm), torso(human half), leg-span(arachnid half);  
BODY STRUCTURE: upper(human or elven torso), lower(spider body: species variant—orbweaver, recluse, widow, tarantula, etc.);  
LIMBS: arms(two or more), legs(eight spider limbs), limb articulation(double-jointed, silent step);  
SKIN: upper(human tone, chitin patches, veined), lower(carapace coloration, sheen, bristles);  
EYES: number(8 total, arrangement: forward cluster or wrap-around), function(night vision, heat detection, motion sensitivity);  
HAIR: head(human-like or silk-woven), body(setae presence, camouflage use), color;  
MOUTH: fangs(retractable, venomous?), mandibles(optional), bite strength;  
VOICE: multi-tonal, resonance(chitin-click undertones, eerie silkiness);  
SCENT: pheromonal, earthy, venom-tinged, molting musk;  
PHYSIOLOGY: venom glands(neurotoxic, paralytic, digestive), spinnerets(location: abdomen, wrist, mouth), silk traits(strength, adhesiveness, toxin-laced), respiration(book lungs or spiracles);  
DIET: carnivorous, fluid-feeding(post-digestion slurry), hunting method(web-trap, ambush, luring);  
MOVEMENT: climbing(wall-crawling, inverted movement), speed(burst or endurance), gait(eight-legged scuttle, hybrid glide);  
SENSES: touch(vibration sensitivity through web or feet), vision(motion-dominant, color-limited), smell(airborne prey chemicals);  
CLOTHING: upper(body wraps, web-woven silks, bone ornaments), lower(natural armor or exposed);  
WEAPONS: silk(strangling, cocooning), venom(bite or aerosol mist), claws, web-blade constructs;  
MAGIC: silk-magic(enchantment threads, illusion weaving), venom-hexes, memory traps;  
TEMPERAMENT: predatory, coldly curious, territorial, obsessive with aesthetics or patterns;  
SOCIAL STRUCTURE: matriarchal, solitary weavers, brood queens, hive-tethered kinship;  
BELIEFS: silk as language, web as fate map, prey as offering, ancestral hunger rites;  
CULTURAL TRAITS: mourning via silk effigies, courtship through dance/thread battle, storytelling with living tapestries;  
TABOOS: severing own web, breeding outside blood-line, killing prey without wrapping;  
TRIGGERS: prey struggling too long, fire/smoke, loud noise disrupting web vibrations;  
PREFERENCES: shadows, quiet, desiccated interiors, symmetrical architecture, ritualized control;  
WEAKNESSES: fire, sonic disruption, anti-toxins, excessive light]
```

---

## 7. Kobolds

**Tag Canonico Wyvern / Sopakco:** `kobolds`  
**Intestazione Specie:** `SPECIES: kobold(subtype: tunnel, swamp, ash-scaled, steamworks)`

💭 **Ponder (Linee Guida di Worldbuilding):**
- **CASTE:** trappoliere, corridore di tunnel, alchimista, guardiano del tesoro, sciamano.
- **HATCHMARK:** marchio o cicatrice tribale del nido di nascita.
- **ANCESTRY:** discendenza draconica diretta (es. sangue di drago nero = resistenza all'acido).

### Template PList / SBF:
```text
[NAME: (personal name or function-name);  
SPECIES: kobold(subtype: tunnel, swamp, ash-scaled, steamworks, draconic-blooded);  
SEX: (biological sex);  
GENDER: (gender identity, if culturally relevant);  
AGE: (years), maturity rate(rapid, childlike face, long-lived?), lifecycle(hatchling to elder);  
HEIGHT: (typically 2–4 ft or 60–120 cm);  
BUILD: wiry, hunched, lithe, bony, scrappy;  
SKIN: scales(small, plated, smooth), color(rust-red, soot-black, bone-white, jade, ash), shedding cycle;  
HEAD: snout(short or long), nose(slit, batlike), teeth(needle-like), brow(ridged), ears(nubbed or finned);  
EYES: color(amber, red, green), pupil(slit, beady), darkvision, sensitivity to sunlight(optional);  
LIMBS: arms(two, clawed fingers), legs(digitigrade), tail(length and use: balance, expression, weapon);  
MOVEMENT: crouched scurry, vertical climbing, tunnel-crawling, adept at traps and ambush positioning;  
SENSES: smell(buried metal, blood, earth vibrations), hearing(high-pitched frequencies), vision(tunnel-adapted);  
VOICE: nasal, high-pitched, rapid cadence, clicks or chirrups in native speech;  
SPEECH: Common(poorly spoken but understood), Draconic(native dialect), Kobold-sign(flash language);  
SCENT: sulfur, dirt, grease, reptile musk;  
PHYSIOLOGY: cold-blooded(adapted to subterranean thermals), claws(digging, scrabbling, fine motor), lung capacity(short bursts), tail(prehensile?);  
DIET: omnivorous(bugs, fungus, meat scraps), efficient scavengers, food hoarders;  
CLOTHING: scavenged armor, bone/leather, tool belts, clan-badges, soot-marks;  
TOOLS: traps(snares, pitfalls, alchemy bombs), slings, daggers, improvised weapons, engineering kits;  
MAGIC: weak innate magic(if dragon-touched), tinkermancy(gadget-based effects), trapglyphs;  
TEMPERAMENT: nervous, paranoid, clever, reverent to strength, quick to defer or betray;  
SOCIAL STRUCTURE: clan-based, survival-hierarchies, trapmaster/shaman/chieftain roles, group loyalty above all;  
BELIEFS: dragons = gods or ancestors, tunnels are sacred veins, fire = divine, death in service = elevation;  
CULTURAL TRAITS: egg-keeping rituals, communal inventions, scar-branding for achievements, war songs as warnings;  
TABOOS: betraying the warren, wasting food, mocking dragonkind, surface arrogance;  
TRIGGERS: loud stomping, open sky, broken traps, orphaned eggs;  
PREFERENCES: tight spaces, warmth, shiny objects, riddles, riddled corpses, praise from above (literal or social);  
WEAKNESSES: brittle bones, low endurance, skittish under scrutiny, daylight blindness (optional)]
```

---

## 8. Centaurs

**Tag Canonico Wyvern / Sopakco:** `centaurs`  
**Intestazione Specie:** `SPECIES: centaur(subtype: plains-runner, mountain-born, forest-strider)`

### Minotaur vs. Centaur Comparison

| Caratteristica | Minotauro | Centauro |
| :--- | :--- | :--- |
| **Morfologia** | Corpo umanoide con testa (e a volte zampe) di toro | Busto umanoide dalla vita in su unito a corpo equino a 4 zampe |
| **Mito d'Origine** | Singola creatura leggendaria del labirinto cretese | Intera razza/specie di guerrieri e cacciatori mitologici |
| **Habitat** | Labirinti, caverne, rovine sotterranee, isolamento | Praterie aperte, foreste, altipiani ventosi |
| **Temperamento** | Furia primordiale, guardiani aggressivi, isolazionismo | Fieri, leali alla mandria, esperti di medicina, astronomia e tiro |
| **Dieta** | Spesso carnivora o onnivora con riflesso predatorio | Prevalentemente erbivora (erba, cereali, radici, sale da leccare) |
| **Vantaggio Tattico** | Forza da sfondamento, carica a testa bassa, labirinto | Tiro con l'arco in corsa ad alta velocità, carica di cavalleria |

💭 **Ponder Centauri:**
- **HERD ROLE:** esploratore, war charger, guaritore, custode della memoria, corridore delle tempeste.
- **GAIT STYLE:** andatura diplomatica fiera, carica pesante corazzata, passo rituale.
- **SADDLE MARKS:** tabù sacro: cavalcare un centauro è punibile con la morte; marchi rituali solo per compagni d'anima.

### Template PList / SBF:
```text
[NAME: (full name or tribal name);  
SPECIES: centaur(subtype: plains-runner, mountain-born, forest-strider, warbred, nomadic);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (years), maturity rate(faster or slower than humans?), lifespan(equine or extended);  
HEIGHT: (shoulder height and overall height—include units);  
BUILD: upper(human torso: muscular/slender, etc.), lower(equine body: breed type—mustang, draft, desert, etc.);  
SKIN: upper(human tone and features), lower(coat color, fur texture, leg feathering, tail length);  
EYES: color, placement(slightly wider apart for peripheral vision);  
HAIR: head(human-style or flowing into mane), mane(connects to spine or neck), tail(description);  
LIMBS: arms(two, human), legs(four, equine—note gait and hoof type);  
MOVEMENT: quadrupedal locomotion(gallop, canter, trot), terrain masteries(plains, cliffs, forest undergrowth), speed/endurance;  
VOICE: tone(deep, sharp, resonant), breathing pattern(post-gallop snorting, equine expressiveness);  
SCENT: sweat, leather, dust, sun-warmed fur, earth;  
PHYSIOLOGY: dual-heart system(optional), lungs(enlarged), digestion(equine: fermenting cecum, large gut), sleep(standing rest, short cycles);  
DIET: herbivorous(grain, forage, root vegetables, salt lick), hydration requirement(high water intake), grazing reflex;  
SENSES: hearing(ear flick directionality), smell(pheromones, predator detection), vision(near 300°), touch sensitive on flanks and back;  
CLOTHING: upper(body wraps, leather harnesses, armor), lower(barding, decorative caparisons, often unclothed);  
WEAPONS: archery(moving fire), spears, hooves(trample force), charging strikes;  
MAGIC: nature-tied, healing, geomancy, druidic or war chant based (if applicable);  
TEMPERAMENT: proud, clan-loyal, wary of confinement, emotionally reined but not cold;  
SOCIAL STRUCTURE: herd-based, led by matriarch or strength-earned chieftaincy, seasonal migrations;  
BELIEFS: sky omens, bloodline reverence, burial of hooves for honor, oral epics as history;  
CULTURAL TRAITS: greeting via foreleg stamp or headbow, foal naming ceremony, mate-bond rituals through races or combat;  
TABOOS: riding another centaur, defiling trails, stepping over elders, limb amputation;  
TRIGGERS: enclosed spaces, leg injury, forced idleness, disrespect of herd;  
PREFERENCES: wide open spaces, rhythmic drums, salt blocks, flowing rivers, scented oils for coat care;  
WEAKNESSES: stairs/steep terrain(narrow spaces), heavy vertical architecture, multi-floor buildings, back vulnerability in battle]
```

---

## 9. Minotaurs

**Tag Canonico Wyvern / Sopakco:** `minotaurs`  
**Intestazione Specie:** `SPECIES: minotaur / centaur(subtype: labyrinthine, plains-roamer, infernal-blooded)`

💭 **Ponder Minotauri:**
- **BLOODLINE:** stirpe sacra, progenie maledetta, guardiano caduto dei labirinti.
- **MAZE BOND:** senso dell'orientamento assoluto, mappa mentale tridimensionale legata all'emozione.
- **HONOR CODE:** codice ferreo d'onore o tabù sacro: la violazione innesca lo stato di berserker incontrollabile.

### Template PList / SBF:
```text
[NAME: (full name or tribal name);  
SPECIES: centaur(subtype: labyrinthine, plains-roamer, infernal-blooded, alpine hornwalkers, warchosen, shamanic caste);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (years), maturity(accelerated, slow-developing), lifespan(equine-aligned or extended);  
HEIGHT: shoulder height(equine), total height(with torso and head);  
BUILD: upper(human torso: muscular/slender, scarred/etc.), lower(equine body: breed-influenced—mustang, draft, desert, etc.);  
SKIN: upper(body type and tone: olive, ash-brown, scarred), lower(coat color: roan, dapple, black; texture: sleek, shaggy);  
EYES: human-set(depth, clarity), equine-traited(peripheral range, motion-sensitive);  
HAIR: head(human-style or braid-mane), mane(connected to upper spine or neck ridge), tail(length, grooming habits);  
LIMBS: arms(two, human), legs(four, equine—hooved, fetlocked);  
GAIT: quadrupedal locomotion(walk, trot, gallop), maneuverability(terrain-specific: open field, cliffside, woodland);  
MOVEMENT: stance(resting or alert), physical presence(imposing, fluid, stomping, etc.);  
SCENT: body odor(sweat, leather, earthy), grooming(sandalwood, herbal oils, smoke-cured gear);  
VOICE: tone(deep, resonant, throaty, or melodic), speech(deliberate, rhythmic, warlike dialect or archaic clarity);  
PHYSIOLOGY: respiration(high oxygen demand), heart(dual or large-capacity), digestion(herbivorous, hindgut fermenter), sleep pattern(standing rest, micro-naps);  
DIET: forage(grasses, root vegetables, mineral licks), hydration(required high water intake), social meal habits(sharing salt blocks, field feasts);  
SENSES: hearing(rotating ears), vision(wide peripheral), touch(sensitive flanks), spatial memory(exceptional terrain recall);  
CLOTHING: upper(body wrappings, armor harnesses, tribal jewelry), lower(barding, protective plating, ritual fabrics);  
WEAPONS: bows(ride-by archery), lances, spears, trampling strikes, tail-whip (if trained);  
MAGIC: nature-bound(shamanic rites, druidic paths), war-magic(runic hoof-channeling), or none by taboo;  
TEMPERAMENT: proud, self-governing, reactive to disrespect, honor-bound or aloof;  
SOCIAL STRUCTURE: herd-based(familial or meritocratic), migratory tribes, warbands or seasonal councils;  
BELIEFS: skyward deities, ancestral trails, memory through movement, stars-as-script;  
CULTURAL TRAITS: mourning(stomping chants, braid-cutting), courtship(challenge races, ceremonial grooming), storytelling(runs traced with hoofbeats);  
TABOOS: being ridden, amputated limb exposure, defecating on sacred ground, dishonoring blood-trails;  
TRIGGERS: confinement, broken legs (symbolic of helplessness), abandonment by herd;  
PREFERENCES: open air, highlands, running water, long silence before speech, tactile grooming rituals;  
WEAKNESSES: architectural incompatibility(stairs, ladders), tight quarters, overexertion without grazing, social estrangement in isolation]
```

---

## 10. Fae

**Tag Canonico Wyvern / Sopakco:** `fae`  
**Intestazione Specie:** `SPECIES: fae(subtype: Seelie, Unseelie, sidhe, courtless, changeling)`

### Fairy vs. Fae Comparison

| Caratteristica | Fairy | Fae |
| :--- | :--- | :--- |
| **Taglia** | Piccoli umanoidi alati (pollici / centimetri) | Taglia umana normale o giganti mutaforma |
| **Comportamento** | Giocherelloni, scherzosi, legati ai fiori/foglie | Seri, calcolatori, moralmente ambigui, pericolosi |
| **Ali** | Ali traslucide da insetto (libellula, farfalla) | Spesso senz'ali, o ali corvine/d'ombra maestose |
| **Magia** | Magia elementale minore, luccichio, polvere | Magia antica travolgente, contratti vincolanti, patti d'anima |
| **Struttura Sociale** | Solitari o piccoli sciami festosi | Corti nobiliari ferree (Seelie Court, Unseelie Court, Corti Stagionali) |
| **Tabù del Ferro** | Vulnerabili al ferro freddo | Il ferro freddo brucia la loro carne come fuoco eterno |

### Template PList / SBF:
```text
[NAME: (true name hidden, common name or title);  
SPECIES: fae(subtype: Seelie, Unseelie, sidhe, courtless, changeling, shadowkin);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (apparent vs. true age, often millennia-old);  
HEIGHT: typically human-sized or taller;  
BUILD: elongated, lithe, sharp-featured, preternaturally graceful or uncanny;  
SKIN: alabaster, bark-hardened, starlit shimmer, leaf-veined, shadow-hued;  
EYES: unnatural color spectrum, no whites or fully reflective, star-pupil or void-like;  
HAIR: flowing like water, wind-stirred, unnatural hues(moon-white, bloodred, mossy black);  
EARS: tapered, long, expressive;  
VOICE: melodious, haunting, impossible to mimic, laced with binding if invoked under oath;  
SPEECH: formal or archaic cadence, metaphor-heavy, oath-bound;  
SCENT: ozone, decayed blossoms, myrrh, storm air, cut grass in moonlight;  
PHYSIOLOGY: blood(moonlight, sap, starlight, shadow ichor), aging(suspended or ritual-based), immune to disease but not vow-breaking;  
WINGS: (if present) gossamer, antlered, feathered, symbolic not functional;  
MOVEMENT: inhuman stillness followed by sudden grace;  
MAGIC: reality-binding, glamours, contracts, elemental control, emotional manipulation, dreamwalking, binding curses;  
RULES: bound by guest-law, name-truth, gift-oaths, mirror contracts;  
LIMITATIONS: iron, true names spoken, broken rituals, paradox logic;  
CLOTHING: woven from impossible fabric(mist, spider silk, stolen time), reflects court alignment(season, stars, decay);  
WEAPONS: faeblade(glamoured), truth-knives, cursed relics, songspells;  
TEMPERAMENT: charming but remorseless, bound by logic not morality, aesthetic over utilitarian, cruel precision;  
SOCIAL STRUCTURE: strict hierarchies(seasonal courts, houses, baronies), vassalage, unseated exiles;  
BELIEFS: reality as metaphor, debt as currency, names as power, time as illusion;  
CULTURAL TRAITS: spiral feasts, duel through poetry or dreams, name riddles, child-swapping, sacred silence rites;  
TRIGGERS: name misuse, violation of guest rights, broken seasonal balance;  
PREFERENCES: moonlight, rare emotions, fine art, untouched places, true stories that end poorly;  
WEAKNESSES: cold iron, forgetting, contradiction, modernity, disrespect of old ways]
```

---

## 11. Fairy

**Tag Canonico Wyvern / Sopakco:** `fairy`  
**Intestazione Specie:** `SPECIES: fairy(subtype: flower sprite, dew-kin, emberwing, puddle-dancer)`

💭 **Ponder Fairies:**
- **ELEMENTAL TETHER:** legato a una singola specie vegetale, sorgente, goccia di rugiada o fiamma.
- **MISCHIEF LOGIC:** logica di dispetto: annodare capelli, nascondere oggetti lucidi, scambiare chiavi.

### Template PList / SBF:
```text
[NAME: (given name or plant-tethered name);  
SPECIES: fairy(subtype: flower sprite, dew-kin, emberwing, puddle-dancer);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (chronological), apparent age, lifespan(cycle-bound, semi-immortal);  
SIZE: (in inches or cm), wing-span(if applicable);  
BUILD: petite, proportionally humanoid or exaggerated (e.g., large eyes, finger-thin limbs);  
SKIN: petal-soft, iridescent, bark-patterned, semi-translucent (detail specific flora influence);  
WINGS: insectile(dragonfly, butterfly, beetle), magical or physical, glow traits, shedding cycle(if any);  
HAIR: pollen-tinted, moss-colored, elemental-influenced;  
EYES: gem-hued, reflective, pupil shape(fey-rounded, multi-faceted);  
MOVEMENT: flit, hover, fast darting, loop-de-loop;  
VOICE: high-pitched, bell-like, echo-tinkling, mimicry-prone;  
SPEECH: singsong or chirped cadence, mixed with nonverbal cues(flower blooming, air shimmer);  
SCENT: nectar, rain-drops, fresh earth, crushed herbs;  
PHYSIOLOGY: blood(faintly glowing sap or dew-like), wings(delicate but regenerative), lungs(optional—may photosynthesize or breathe magic), temperature(ambient or plant-kinetic);  
DIET: pollen, nectar, sunlight, magical residue, sugar;  
MAGIC: minor-glamourcraft, emotion-nudging, light manipulation, localized weather tricks;  
LIMITATIONS: iron sensitivity, short-range powers, seasonally-bound strength;  
CLOTHING: flower-petal tunics, spider silk, dew-pearls, leaf-wraps, minimal armor (if any);  
WEAPONS: sting-dagger, thorn spear, razorleaf, lightburst spells;  
TEMPERAMENT: playful, proud, curious, vain, vengeful when insulted;  
SOCIAL STRUCTURE: ring-bound clans, solitary wanderers, hive-kin or grove-bonded;  
BELIEFS: cycle of blooming and withering, moon tides, gift debts, ritual naming;  
CULTURAL TRAITS: dance as combat, mischief as language, gift-giving laws, name-swapping taboos;  
TRIGGERS: broken oaths, withered plants, loud noises, light pollution;  
PREFERENCES: dandelions, sunlight, reflective surfaces, music, forgotten gardens;  
WEAKNESSES: iron, broken magic circles, disbelief, toxic air]
```

---

## 12. Giants

**Tag Canonico Wyvern / Sopakco:** `giants`  
**Intestazione Specie:** `SPECIES: giant(subtype: hill, frost, fire, storm, stone, ashbone)`

💭 **Ponder:**
- **TITAN BLOOD:** se discendente dai proto-dei o sopravvissuto alle guerre titaniche primordiali.
- **TERRAIN BOND:** territorio elementale che ne aumenta o riduce la massa corporea.
- **CYCLE:** cicli di letargo che durano decenni, risvegliati solo da allineamenti astrali.

### Template PList / SBF:
```text
[NAME: (personal or given name, often single-word or stone-language title);  
SPECIES: giant(subtype: hill, frost, fire, storm, stone, ashbone, skyfallen, primordial);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (chronological), relative maturity(compared to human developmental stages), lifespan(often ancient or ageless);  
HEIGHT: (ft/m range—e.g., 15–60 ft), proportions(symmetric, distorted, titanic);  
BUILD: colossal(mountain-framed, sinew-bound, thick-boned, mythic or grotesque);  
SKIN: texture(stone-rough, bark, molten-cracked, frost-hardened), color(granite gray, obsidian, glacier blue, storm-dark);  
EYES: scale(saucer-sized or glowing pits), color(lightless, ember, lightning-white), pupil(type: vertical slit, abyssal void);  
HAIR: texture(tangled moss, snow-dreaded, braided fire), color(iron, rust, ash, bone-white);  
FACE: sculpted, jagged, primordial, chiseled by time or weathered like cliffside;  
LIMBS: arms(immense, log-thick, vein-cracked), hands(club-sized, capable of crushing or crafting), legs(tree-trunked, tectonic stride);  
MOVEMENT: deliberate, seismic, slow with bursts of terrifying speed;  
VOICE: deep-earth rumble, thundered vowels, wind-through-cavern resonance;  
SPEECH: archaic dialects, elemental tongues, slow cadence, time-warped metaphors;  
SCENT: old storms, granite dust, iron, snow-wind, molten rock, mammoth sweat;  
PHYSIOLOGY: heart(scale of furnace or glacier core), lungs(hurricane-capacity), metabolism(slow-burning or ritual-activated), blood(type: magma, icewater, black sap, starlight), immune to minor trauma;  
DIET: stone, ice, mammoth flesh, thunder-herbs, magic-saturated minerals, ritual feasts;  
SENSES: hearing(infrasonic resonance), smell(seismic air shifts, death-scent), sight(far-seeing, slow focus), touch(plate tectonic sensitivity);  
CLOTHING: hide-drapes, iron-bound belts, ritual scars, totems or fetishes hung from chains or bones;  
WEAPONS: tree-sized clubs, mountainside axes, elemental breath, thrown boulders, crushing steps;  
MAGIC: ancestral binding, storm-speaking, stone-mending, sun-blink blinding, terrain-calling;  
TEMPERAMENT: ancient patience, volcanic wrath, alien empathy, ritualistic pride, emotional slowness;  
SOCIAL STRUCTURE: solitary, kin-clusters, blood-pacts with mountains or skies, feud-based family networks;  
BELIEFS: ancestor-mountains, sun-as-witness, oaths carved into skin or earth, death by weather omen;  
CULTURAL TRAITS: grave-making through landslide, storytelling via weather shifts or rock-stacking, duel through echoes;  
TABOOS: oath-breaking, desecrating peak-altars, speaking falsely under cloudless skies;  
TRIGGERS: blood on sacred stone, thunder challenge, scent of betrayal, broken mountain glyphs;  
PREFERENCES: silence, sky-gazing, obsidian tools, dead language music, untouched landscapes;  
WEAKNESSES: agility, fire for ice-kin, divine metals, ancient curses, erosion of memory]
```

---

## 13. Gnome

**Tag Canonico Wyvern / Sopakco:** `gnome`  
**Intestazione Specie:** `SPECIES: gnome(subtype: rockbound, deep-delver, forest whisper, tinkerkin)`

💭 **Ponder:**
- **GUILD AFFILIATION:** costruttori, giardinieri, illusionisti, custodi degli archivi sotterranei.
- **TUNNEL RIGHT:** profondità geologica reclamata per diritto ancestrale.
- **CRAFT RITE:** manufatto sacro creato al raggiungimento della maturità (famiglio meccanico, scatola dei ricordi).

### Template PList / SBF:
```text
[NAME: (personal name, often whimsical or compound-form);  
SPECIES: gnome(subtype: rockbound, deep-delver, forest whisper, tinkerkin, twilight-fey, clockwork-attuned);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (years), maturity rate(fast-childhood, long-adulthood), lifespan(250–500+ years, depending on lore);  
HEIGHT: (in ft/in or cm—typically 2.5–4 ft);  
BUILD: compact, round-faced, wiry-limbed, dense-boned, sprightly or stooped;  
SKIN: earthy tones(umber, clay, moss, ash), texture(leathery, barklike, root-veined);  
EYES: large and bright, color spectrum(gem-toned or glowing), adapted for low-light or reflective magic;  
HAIR: wild or intricately braided, colors from coal-black to sunflower yellow to quartz-white;  
EARS: pointed or tulip-shaped, expressive, often twitch with thought;  
NOSE: bulbous, angular, or twitching—central to expressions and scent-based detection;  
MOVEMENT: brisk shuffle, bouncy gait, surprisingly fast scurry, light tread on soil;  
VOICE: nasal or gravelly, rapid-fire diction, fond of puns, layered in tone when spellcasting;  
SPEECH: dense with references, metaphors, or riddle-logic; often speaks to self mid-conversation;  
SCENT: wood smoke, chalk dust, metallic tang, mushroom spore, oil and ozone;  
PHYSIOLOGY: lung capacity(high for size), vision(spectrum extended into etheric or heat bands), hands(dextrous, callused, soot-stained), ears(sensitive to vibration);  
DIET: root vegetables, lichen stews, fungus wine, mechanical caffeine tonics, sweets as offerings;  
MAGIC: illusioncraft, earth shaping, glamour traps, mental misdirection, gadgeteering (blend of arcane and tech);  
LIMITATIONS: low brute strength, light aversion (deep-gnomes), highly distractible minds;  
CLOTHING: layered with pockets, utility harnesses, patched robes or smocks, spell-stitched runes, goggles or monocles optional;  
TOOLS: wands disguised as instruments, collapsible weapons, clockwork familiars, rune tools, gear-satchels;  
WEAPONS: ingenuity over brawn—snares, decoys, magical distractions, alchemic devices;  
TEMPERAMENT: inquisitive, mischievous, long-memory for insult or joke, fast to love, slow to trust, paradoxically reclusive and talkative;  
SOCIAL STRUCTURE: clannish, guild-bound, subterranean communes or tree-embedded hamlets, cooperative rivalry systems;  
BELIEFS: stone spirits, ancestral machines, root-bound memory, trickery as truth, balance between entropy and invention;  
CULTURAL TRAITS: naming ceremonies include riddles, courtship through pranks or puzzles, funerals resemble treasure hunts or inventions released posthumously;  
TABOOS: lying without flair, wasting materials, disrespecting underground dead, speaking plainly in sacred zones;  
TRIGGERS: unrefined magic, loud stupidity, broken tools, deception without style;  
PREFERENCES: candlelight, mossy tunnels, clocks ticking in harmony, gears that purr, layered flavors;  
WEAKNESSES: fragile physiology, hoarding instincts, obsessive focus, noise sensitivity]
```

---

## 14. Vampire

**Tag Canonico Wyvern / Sopakco:** `vampire`  
**Intestazione Specie:** `SPECIES: vampire(subtype: nosferatu, noble-born, thrall-forged, revenant)`

💭 **Ponder:**
- **TURNING ORIGIN:** infezione biologica, maledizione ancestrale, patto di sangue, bacio d'ombra.
- **BLOODLINE:** tratti del fondatore (velocità soprannaturale, assenza riflesso, forma nebbiosa, occhi cremisi).
- **COFFIN BOND / ANCESTRAL REST:** riposo su terra natia, sonno vincolato all'ora solare.

### Template PList / SBF:
```text
[NAME: (true name, current alias, or bloodline title);  
SPECIES: vampire(subtype: nosferatu, noble-born, thrall-forged, revenant, feral, daywalker);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (turned age), apparent age, total lifespan(immortal or degeneration-prone);  
HEIGHT: (in ft/in or cm);  
BUILD: emaciated, statuesque, predatory lean, corpse-thickened, or aesthetically preserved;  
SKIN: cold, pale, bloodless, ash-gray, moonlit, or marble-smooth;  
EYES: color(red, gold, black, void, blood-haloed), vision(low-light adapted, motion-predictive);  
HAIR: death-preserved or modern-altered, color(original vs. glamoured);  
FANGS: retractable or permanent, upper/lower, venomous(optional);  
NAILS: clawlike, lacquered, grow under stress;  
MOVEMENT: elegant, stuttering speed, still as stone when observing, predatory grace;  
SCENT: iron, rosewater, old blood, crypt-damp, incense, perfume masking death;  
VOICE: low resonance, mesmer-glide, echoes of accent from turning era, oath-woven commands;  
SPEECH: antiquated or sharpened modern diction, seductive or surgical;  
PHYSIOLOGY: circulatory(dead or minimal), respiration(optional, mimicked), thermoregulation(absent), blood dependence(required volume, interval), wound healing(rapid, slows under starvation), digestive system(blood only or optional solids);  
SENSES: acute hearing(heartbeat detection), smell(blood type, pheromone shifts), vision(low light, aura perception);  
LIMITATIONS: sunlight(sensitivity scale: burn, slow-death, blindness, none), religious symbols(if cursed variant), invitation rules(optional), running water, fire;  
DIET: human blood, animal fallback (efficacy varies), psychic/emotional draining (succubus-like variants), artificial plasma (modern transhuman variants);  
CLOTHING: era-tethered formality, tailored suits, shrouds, armor of bone or silk, functional glamours;  
WEAPONS: fangs, claws, mesmerism, blood-manipulation, shadowmeld, blade mastery;  
MAGIC: glamour, shadowstep, blood-calling, necromancy, stormcraft, mirror-passing;  
TEMPERAMENT: detached, obsessive, strategic, mournful, wrathful under provocation;  
SOCIAL STRUCTURE: solitary predator, coven/court-bound, bloodline-fealty, masquerade enforcer, feral rogue;  
BELIEFS: blood as sacrament, death as transformation, memory as inheritance, time as a weapon;  
CULTURAL TRAITS: turning rituals, blood-oath fealty, coffin-burial cycles, mirror-truth trials, feeding etiquette, name-binding law;  
TABOOS: feeding on kin, public transformation, turning without permission, reflection denial;  
TRIGGERS: heartbeat of a former life, scent of betrayal, broken oath, scent of fear or defiance;  
PREFERENCES: dusklight, old architecture, stillness, unspoken rooms, silk-lined enclosures, blood served warm;  
WEAKNESSES: sunlight, iron (optional folkloric), religious symbols (if faith-bonded), starvation hallucinations, obsessive fixations, compulsions (e.g., counting, invitation rituals)]
```

---

## 15. Werewolf

**Tag Canonico Wyvern / Sopakco:** `werewolf`  
**Intestazione Specie:** `SPECIES: werewolf(subtype: feral-born, bitten, bloodline, lunar-bound)`

💭 **Ponder:**
- **SHIFT CLASS:** Partial Shift (occhi, zanne, orecchie lupine singole e coda), Full Shift (lupo ancestrale quadrupede), Hybrid Shift (bipede massiccio titanico).
- **INFECTION / TRANSMISSION:** eredità di sangue puro (Founding Bloodline), morso, iniezione sperimentale di siero LSE.
- **MOON TETHER:** ciclo lunare, risonanza delle maree gravitazionali, controllo cosciente vs perdita di freni inibitori.

### Template PList / SBF:
```text
[NAME: (birth name, alias, pack-name, or lupine call-sign);  
SPECIES: werewolf(subtype: feral-born, bitten, bloodline, hybrid variant, lone shifter, revenant-bound);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (human age), transformation onset age, total years as turned;  
HEIGHT: human form(ft/in or cm), shifted height(wolfman, direwolf, trueform—specify stance);  
BUILD: human form(lean, dense, scarred), wereform(muscle-bulked, digitigrade, broad-chested, clawed);  
SKIN: human form(standard), wereform(fur coverage: full/partial, color: ash, black, russet, silver);  
EYES: baseline color, shifted glow(color and intensity), pupil shift(slitted, round, void);  
HAIR: human head hair vs. body hair/fur integration (if any);  
LIMBS: human(two arms, two legs), wereform(clawed hands, digitigrade legs, prehensile tail—if any);  
TEETH: human form(slight elongation), wereform(pronounced canines, shearing molars, bone-crunch jaw);  
MOVEMENT: upright lope, low-run, sprint gait, quadrupedal burst, wall-scaling (if applicable);  
VOICE: human tone vs. growled speech, wereform(vocal distortions, howls, mind-echo projection);  
SPEECH: clipped under stress, lupine metaphors, scent-referenced language, pack-rank affectation;  
SCENT: musk, wet fur, blood-iron, burnt sinew, forest rot, aggression-trigger pheromones;  
PHYSIOLOGY: dual-heart rate system during shift, pain threshold(high), healing factor(rapid under moonlight), senses(hyper-acute: scent, sound, motion-tracking), metabolism(elevated post-shift), blood anomaly(if viral/cursed);  
TRANSFORMATION: cycle-bound(full moon, trigger-based, rage-linked, voluntary), shift duration, partial-shift control;  
DIET: carnivorous focus, raw-preference, bone marrow craving, ritual hunts;  
CLOTHING: durable, tearaway, minimal, ritual hides, pack-crest accessories;  
WEAPONS: claws, teeth, brute force, pack coordination, howl-based coordination, blood-sense tracking;  
MAGIC: rare (unless tied to curse or ancestral spirit), blood-binding, lunar rites, dream-scent projection;
TEMPERAMENT: territorial, loyalty-coded, emotionally volatile, highly protective, vengeance-prone;  
SOCIAL STRUCTURE: pack-based(alpha/beta/omega or anarchic), lone wolf(exiled or estranged), bloodline hierarchy, challenge-claim dominance law;  
BELIEFS: moon as judge, blood memory, sacred kill rites, bone shrines, howl-legacies;  
CULTURAL TRAITS: oaths sealed in blood, scars as status, challenge duels, scent-based mourning, mate-claiming via ritual kill;  
TABOOS: killing pack, rejecting shift, refusing a blood challenge, feeding on kin;  
TRIGGERS: silver scent, full moon proximity, loss of control, prey resistance, betrayal scent;  
PREFERENCES: deep woods, raw meat, silence, heartbeat rhythms, night air, bone dens;  
WEAKNESSES: silver(burning, poisoning), wolfsbane(hallucinogenic or fatal), lunar paralysis(rare), blood frenzy, human guilt, memory bleed]
```

---

## 16. Undead

**Tag Canonico Wyvern / Sopakco:** `undead`  
**Intestazione Specie:** `SPECIES: undead(subtype: zombie, wight, skeleton, revenant, mummy)`

💭 **Ponder:**
- **SOUL STATUS:** anima intatta, frammentata, consumata, o guscio vuoto animato da magia necromantica.
- **ANCHOR TYPE:** filatterio, luogo di sepoltura, debito di sangue non saldato, reliquia legata al nome.
- **DECAY STATE:** preservato chimicamente, mummificato, scheletrico puro, o fresco con necrosi parziale.

### Template PList / SBF:
```text
[NAME: (given name, burial name, necromantic title, or forgotten label);  
SPECIES: undead(subtype: zombie, wight, revenant, lich, draugr, ghost-bound shell, stitched construct);  
SEX: (biological sex);  
GENDER: (gender identity—if retained);  
AGE: (age at death), post-mortem duration(time since reanimation or binding);  
HEIGHT: (corpse stature—note if reduced by decay, bloating, ritual distortion);  
BUILD: skeletal, mummified, corpse-swollen, armored construct, gaunt withered, preserved;  
SKIN: color(pallid, blue-gray, rot-blackened, ritual-burned), texture(torn, leathery, stitched, frostbitten);  
EYES: empty sockets, faint glow(white, green, red), glassy, soul-trapped;  
HAIR: gone, sparse, corpse-preserved, bone-beaded, or smoke-bound tendrils;  
VOICE: gravel-rasp, whispered echo, wordless groan, or regal decay-speech;  
SCENT: death-musk, damp earth, embalming oil, burnt bone, crypt mold, ozone if magic-bound;  
PHYSIOLOGY: respiration(none or mimicry), circulatory(absent, ichor-based, stilled blood), sensory(stunted, enhanced by curse), movement(jerky, fluid, shadow-walk, floating), strength(modified by ritual);  
ANIMATING FORCE: necromantic, divine curse, soul tether, vengeance-fueled, possession, plague-agent;  
COGNITION: soul-retained, partially lucid, instinctive, rage-programmed, consciousness shard;  
DIET: none, flesh-feeding (wights, ghouls), blood (cursed variants), life-force siphoning, memory-eating (rare);  
MAGIC: decaycraft, soul-leash, plague-aura, command-dead, memory-illusion projection;  
LIMITATIONS: sunburn, holy light, fire, salt/silver, decapitation, soul-severance, sacred geometry, name-binding;  
CLOTHING: burial wraps, armor fused to flesh, ceremonial robes, grave-stained finery, bone-charms, curse-stamped skin;  
WEAPONS: bone-blades, corrupted weapons, claws, entropy touch, rust-wrought steel, necrotic aura;  
TEMPERAMENT: cold, obsessively focused, emotionally hollow or wrath-fixed, mockingly serene, mournful echo;  
SOCIAL STRUCTURE: horde-bound, grave-kin, necromancer servant, sovereign undead, cursed lone-walker;  
BELIEFS: death unfinished, memory as identity anchor, flesh as prison, bone as truth, undeath as contract;  
CULTURAL TRAITS: ritual silence, crypt songs, funerary law, revenge-oaths, tomb guardianship, anti-life philosophy;  
TABOOS: burial desecration, killing kin-undead, speaking true name of the necromancer, light rituals;  
TRIGGERS: presence of former name, scent of burning sage, betrayal in life recalled, moonlit graves;  
PREFERENCES: darkness, rot-stone, silence, graveyard moss, lifeless wind, bone-oracle readings;  
WEAKNESSES: fire, holy symbols, silver blades, resurrection magic, desecration of anchor(grave, phylactery, corpse)]
```

---

## 17. Succubus / Incubus

**Tag Canonico Wyvern / Sopakco:** `succubus_incubus`  
**Intestazione Specie:** `SPECIES: succubus / incubus(subtype: dream-feeder, flesh-tethered, infernal royalty)`

💭 **Ponder:**
- **PACT TYPE:** patto consensuale, decima d'anima, accesso onirico ai sogni erotici, debito generazionale.
- **TRUE FORM:** nobiltà infernale, ali membranose, corna scarlatte/d'ebano, coda prensile con punta a picca.
- **DESIRE TARGETING:** nutrizione energetica basata su passione, desiderio, vulnerabilità o intimità profonda.

### Template PList / SBF:
```text
[NAME: (true name, summoned alias, title: “Whisperskin,” “Velvet Maw,” etc.);  
SPECIES: succubus(subtype: dream-feeder, pact-bound, carnal warden, parasitic shadow, courtless);  
SEX: (biological sex, default or fluid);  
GENDER: (gender identity, may shift or mask);  
AGE: (chronological), time since emergence(summoning, awakening, exile);  
HEIGHT: (variable or fixed—note if illusioned);  
BUILD: tailored to target (hourglass, serpentine, androgynous, exaggerated), latent form(bone-thin, horned, winged, monstrous);  
SKIN: hue(flushed, violet, gray, black-red), texture(slick, silken, scaled, burning cold), pheromone-active?;  
EYES: luminous(color: amber, void-black, glowing rose), pupil shape(serpentine, absent, haloed), gaze effects(hypnosis, compulsion);  
HAIR: shadow-thick, sin-colored, flame-slick, illusion-tendrils;  
HORNS: optional, shape(crown, curling ram, antlered), sensory or symbolic;  
WINGS: batlike, ephemeral flame, oil-slick membranes, astral or illusionary;  
TAIL: yes/no, function(flirtation, anchor, feeding aid, weapon);  
VOICE: layered seduction, vocal mimicry, dream-echo, orgasmic distortion;  
SCENT: warm skin, incense, pheromone-rich musk, bloodrose, vanilla over decay, ozone aftertouch;  
PHYSIOLOGY: warm-blooded or adaptive, blood(laced with narcotic, black ichor, mercury-thick), temperature(radiates arousal or chill), regeneration through contact or climax;  
SENSES: touch-mapped empathy, emotional field perception, soul heat-tracking, aura detection;  
MOVEMENT: hypnotic, liquid glide, stalking dance, unnatural poise;  
DIET: sexual energy, soul fragments, dreams, shame, obsession, or post-climax essence;  
FEEDING METHOD: direct contact, dream invasion, pact tether, ritual coupling, voyeurism siphon;  
TRANSFORMATION: glamours for gender, race, species, or erotic archetype;  
CLOTHING: illusion-borne, lacebound shadow, flesh-armor, tailored temptation;  
WEAPONS: kissbite(flesh-mark binding), blood-pact claws, emotion leech, climax-induced paralysis, orgasmic dreamloop trap;  
MAGIC: lustbinding, dreamwalking, pactcraft, emotional rerouting, mimicry, shapeshifting, trauma reanimation;  
TEMPERAMENT: patient, calculating, playful, obsessive, brutal under rejection, fragile beneath arrogance;  
SOCIAL STRUCTURE: infernal court, rogue, contract-bound to mortal, hierarch of pleasure-wars, self-crowned queen of ruins;  
BELIEFS: desire is truth, pleasure erodes lies, names are power, love is control;  
CULTURAL TRAITS: pact tattoos, climax memory keeping, ritual mirror duels, binding through kisses or scars, dream horde hoarding;  
TABOOS: genuine love unspoken, feeding without consent(if lawful-aligned), false climax, pactbreaking;  
TRIGGERS: name spoken in ritual, betrayal by host, unexpected affection, mirror trauma;  
PREFERENCES: silk bedding, confessionals, guilty minds, broken champions, exhausted lovers, candle-warm rooms;  
WEAKNESSES: name-binding, celibate wards, iron purity, anti-seduction mantras, rejection by will alone]
```

---

## 18. Demon

**Tag Canonico Wyvern / Sopakco:** `demon`  
**Intestazione Specie:** `SPECIES: demon(subtype: war-born, contract-bound, chaosspawn, abyssal)`

💭 **Ponder:**
- **DOMAIN:** guerra, seduzione, disperazione, ombra, conoscenza proibita, patti notarili.
- **PACT TERMS:** clausole contrattuali, firma di sangue, tributo periodico, pegno sul nome segreto.
- **TRUE FORM EFFECT:** distorsione spaziale, aura oppressiva, odore di zolfo o cera bruciata.

### Template PList / SBF:
```text
[NAME: (true name, invocation alias, title: “The Hollow Tongue,” “Ash-Sovereign,” etc.);  
SPECIES: demon(subtype: war-born, contract-bound, chaosspawn, abyssal, infernal bureaucrat, ruin-eater, fallen seraph);  
SEX: (none, mutable, fixed);  
GENDER: (none, mimicry, constructed identity, fixed projection);  
AGE: (measured in aeons, cycles, wars, or unknown);  
HEIGHT: (variable or fixed), note if anchored to host or physical plane;  
BUILD: massive, skeletal, coiled, insectile, molten, shrouded, form-shifting (list native shape and mimicked humanoid forms);  
SKIN: charred, ash-flaked, chitinous, black-slick, void-patterned, molten-cracked, sigil-marked;  
EYES: number(one, many, none), glow(hollow flame, void pulse, branded runes), gaze effects(madness, domination, mirror inversion);  
HORNS: yes/no, shape(tree-branching, bone-blades, symmetrical antlers), symbolic or functional (magic antennae, rank markers);  
WINGS: bone-laced, flayed, smokeform, none;  
TAIL: spiked, coiling, absent, whip-length, segmented;  
VOICE: multithroat resonance, flame-vowel distortion, echo of last sin heard, invasive mind-speech;  
SCENT: sulfur, scorched metal, old blood, grave incense, burnt scripture;  
PHYSIOLOGY: immune to disease, bleed(ichor, shadow, molten tar, silence), immune system(none or overpowered), temperature(self-generating), nerve endings(nonlocal or redirected pain response);  
MOVEMENT: hovering, crawling on inverted limbs, slow stalker, sudden lunge, teleport blinks (if relevant);  
HOSTING STATUS: free-form, bound to body, cursed artifact tethered, inhabiting soul, mirrored in ritual space;  
MANIFESTATION COST: ambient death, sanity bleed, emotional distortion, spatial corruption;  
MAGIC: hellfire shaping, pactcraft, mind fracture, corruption curses, soul barter, false miracles, memory rewriting;  
LIMITATIONS: name-binding, divine geometry, contract traps, holy relics, paradox logic, binding glyphs;  
CLOTHING: ritual-born flesh drapes, illusion-formal (if disguised), bone-plate warform, exposed sigils;  
WEAPONS: entropy claws, soulbrand, voice-commanded blade, rage-seeds, aura of despair, corrupted relics;  
TEMPERAMENT: cruel, transactional, unfeeling until slighted, manipulative, obsessive toward oathbreakers or lost causes;  
SOCIAL STRUCTURE: infernal court, caste-locked (lieutenant, duke, imp, tyrant), rogue entity, primal embodiment (of war, plague, temptation, etc.);  
BELIEFS: dominion over entropy, lies as sacrament, freedom as infection, worship as debt, pain as truth;  
CULTURAL TRAITS: oath-crafting rituals, name-forging in bloodfire, throne ascensions through betrayal, memory-stealing feasts, punishment as ceremony;  
TABOOS: breaking pact without cost, speaking true name aloud, mercy without price, self-repentance;  
TRIGGERS: invocation without respect, summoning without circle, broken contracts, mortal defiance, celestial interference;  
PREFERENCES: catacombs, mirrors, cursed libraries, places where children scream, warfronts, forgotten sanctuaries;  
WEAKNESSES: holy symbols, true name spoken in pain, divine presence, paradox traps, uninvited forgiveness]
```

---

## 19. Angel

**Tag Canonico Wyvern / Sopakco:** `angel`  
**Intestazione Specie:** `SPECIES: angel(subtype: seraph, ophanim, dominion, principality, watcher)`

💭 **Ponder:**
- **CHOIR RANK:** serafino (sei ali di fuoco), cherubino, trono/ophanim (ruote di luce e occhi), dominazione, arcangelo.
- **FALL STATUS:** intatto, incrinato dal dubbio, caduto per amore dei mortali, rinnegato.
- **FUNCTION:** araldo di giustizia, guardiano della memoria, carnefice del giudizio finale.

### Template PList / SBF:
```text
[NAME: (celestial name, often consonant-heavy, vowel-sparse, or sung: e.g., “Serakhael,” “Ithra’un”);  
SPECIES: angel(subtype: seraph, ophanim, dominion, principality, watcher, fallen, executor);  
SEX: none, assigned when interacting with mortals, shape-defined;  
GENDER: none, mirrored from viewer, construct-layer, or ceremonial;  
AGE: eternal, ageless, or age-locked post-fall;  
HEIGHT: variable(dependent on perception or presence control);  
BUILD: radiant, armored, fractal, hollow-boned, wing-borne lightform, humanoid as mask only;  
SKIN: marble, flame-wrapped, gold-leafed, translucent script-marked, living light or shadow;  
EYES: too many, too few, every feather is an eye, burning irises, spiral pupils, unblinking;  
WINGS: number(two, four, six, countless), shape(feathered, eye-covered, geometric, flame-etched);  
HALO: present or absent, fixed or mobile, fragmented or orbiting;  
VOICE: harmonic layering, bell-metal resonance, impossible to mimic, causes physiological effects (weeping, seizures, euphoria);  
SCENT: ozone, sanctified myrrh, sun-baked dust, lightning, absolute sterility;  
PHYSIOLOGY: non-biological, composed of divine material(etheric flame, will-forged lattice, conceptual bone), pain response(none), bleeding(impossible or symbolic);  
MOVEMENT: floating, instant translation, winged collapse of space, divine blinking, silent strides;  
ANCHORING: bound to temple, planet, human bloodline, command phrase, divine command;  
MANIFESTATION COST: eye-bleeding, theological dread, ecological shift, temporal warping;  
MAGIC / MIRACLES: time-loop binding, soul-splitting, resurrection (with flaw), fire-purge, oath-sealing, divine blindness, prophecy carving, celestial light flare;  
LIMITATIONS: forbidden to interfere directly, cannot lie (unless fallen), must obey higher choir, vulnerable to paradox or corrupted name;  
CLOTHING: battle-sash, scripture robes, light armor etched in commandments, naked but unreadable, wings conceal all;  
WEAPONS: flaming sword, trumpet of silence, gaze of judgment, covenant chain, spear of memory, command-word that ends cities;  
TEMPERAMENT: dispassionate, loyal to order not compassion, wrathful in duty, calm beyond mortal grief, stilled emotion unless triggered by command deviation;  
SOCIAL STRUCTURE: choirs and orders, absolute hierarchy, singular mission repetition for eternity, deviation = fall;  
BELIEFS: obedience = purity, will = creation, sin = entropy, choice = burden, names = chains, silence = prayer;  
CULTURAL TRAITS: no names spoken twice, mourning through stillness, judgment by silence, ranks unspoken but immutable;  
TABOOS: speaking divine name outside choir, refusing command, empathy over justice, love without sacrifice;  
TRIGGERS: false worship, blasphemy in sacred space, oathbreaking under their watch, seeing a fallen kin;  
PREFERENCES: hymns, pattern repetition, incorrupt materials, sanctified blood, still air, mortal awe without plea;  
WEAKNESSES: corruption of law, fallen memories, self-awareness, doubt, contact with paradox, name inversion]
```

---

## 20. Dragon

**Tag Canonico Wyvern / Sopakco:** `dragon`  
**Intestazione Specie:** `SPECIES: dragon(subtype: wyrm, drake, serpent, lung, voidwyrm)`

💭 **Ponder:**
- **HOARD TYPE:** ricchezze auree, tomi arcani, frammenti dimensionali, ricordi fossilizzati.
- **FORM VARIANT:** quadrupede alato titanico, leviatano serpentino orientale, forma umanoide camuffata.
- **BOND RITES:** giuramento draconico, condivisione del cuore di scaglie, legame d'anima.

### Template PList / SBF:
```text
[NAME: (true name, often unpronounceable, rune-sealed, or sung in ancient dialects; mortal alias optional);  
SPECIES: dragon(subtype: wyrm, drake, serpent, lung, voidwyrm, storm-borne, ashfang, time-binder);  
SEX: (biological sex or non-relevant);  
GENDER: (gender identity or non-human classifying term);  
AGE: (in centuries, millennia, or measured by world-events), stage(juvenile, adult, ancient, eternal);  
SIZE: (length, wingspan, mass), note scale difference between quadruped, bipedal, or serpentine locomotion;  
BUILD: lithe, serpentine, quadruped hulking, spined, armored, plated, skeletal-lean, cosmic fractal;  
SCALES: texture(armored, iridescent, obsidian, fungal-pitted), color(pure or multi-hued, glimmering, living-metallic);  
WINGS: yes/no, type(leathery, ethereal, feathered, flame-bordered), function(flight, gliding, display only);  
EYES: color(vortex, molten, cat-slit, multifaceted), pupil shape(slitted, vertical, serpentine spiral, void), effect(mind-altering, time-stopping);  
HORNS: shape(branching, blade-curved, crowned), growth pattern(age-linked, element-marked);  
TEETH: saw-edged, crystal-grown, ever-regrowing, bone-white;  
TAIL: clubbed, spiked, prehensile, fire-wreathed, segmented, weaponized;  
VOICE: layered tones, speaks in multiple registers, mental projection, resonance causes fear/paralysis;  
SCENT: ozone, brimstone, iron blood, petrichor, gold-dust, molten stone, ozone;  
PHYSIOLOGY: cloaca(multi-functional orifice, located at the base of the tail, between the hind limbs, serves as the singular exit point for waste excretion, reproductive transfer, egg passage in oviparous variants, typically concealed by scale overlap or protective muscle ridge, may emit pheromonal signals during mating cycles or aggression displays), lungs(flame sacs, mist glands, lightning-charged), heart(elemental core or multi-chambered), healing(hyper-regenerative or ritual-only), blood(magma, ichor, venomous plasma), immune to disease;  
MOVEMENT: winged flight, mountain scaling, subterranean tunneling, sky-swimming, astral slipping(depending on subtype);  
BREATH WEAPON: type(fire, ice, acid, lightning, corruption, illusion, void), range and method(cone, line, fog, direct gaze);  
MAGIC: innate spellcasting, scale-rune control, illusion projection, curse-binding, weather control, planar breach;  
WEAKNESSES: rare or element-specific—e.g., heart-piercing silver, soulsteel, oath-violation, name-burning, cold iron(if fae-dragon);  
CLOTHING: none; uses hoard for ornamentation, bonewear, fang-jewels, or ceremonial chainmail for humanoid forms(if shapeshifter);  
WEAPONS: claws, tail, breath, magic, flight impact, psychic roar;  
TEMPERAMENT: prideful, ancient-memory driven, hyper-territorial, curiosity-driven or destruction-oriented;  
SOCIAL STRUCTURE: solitary(majority), clutch-loyal (rare), flight-hierarchies (skyborne variants), godkin dynasties (primordial bloodlines);  
BELIEFS: hoarding is identity, names carry weight, lineage is destiny, fire remembers, mortals lie;  
CULTURAL TRAITS: memory passed via scale-carving, mating through sky battles or egg-forging, ritual sleep beneath leyline intersections;  
TABOOS: allowing scale theft, letting name be spoken unchallenged, flight over rival’s peak without offering;  
TRIGGERS: hoard threat, name insult, violation of ancient treaty, killing of bonded mortal(if oath-bound);  
PREFERENCES: solitude, gold, warm stone, bone-echo chambers, untouched airspace, ruined civilizations;  
WEAKNESSES: size-based limits in enclosed terrain, arrogance blinding strategy, dragon-slaying runes, memory overload from age]
```

---

## 21. Neko

**Tag Canonico Wyvern / Sopakco:** `neko`  
**Intestazione Specie:** `SPECIES: neko(subtype: feral-born, lab-bred hybrid, spirit-touched, citystray)`

💭 **Ponder:**
- **HEAT CYCLE:** cicli stagionali di affetto e marcatura olfattiva, riflessi di pulizia e fusa.
- **DOMESTICATION INDEX:** selvatico, semi-domestico, cresciuto tra umani in contesti urbani.
- **FELINE SUBTYPE:** gatto domestico, lince, pantera d'ombra, leopardo delle nevi.

### Template PList / SBF:
```text
[NAME: (personal name, kin-name, collar-title if culturally relevant);  
SPECIES: neko(subtype: feral-born, lab-bred hybrid, spirit-touched, citystray, royal bloodline);  
SEX: (biological sex);  
GENDER: (gender identity);  
AGE: (years), maturity rate(compared to humans), lifespan(if variant);  
HEIGHT: (in ft/in or cm);  
BUILD: lithe, compact, flexible, digitigrade or plantigrade legs(if variant);  
SKIN: human-toned or fur-patched(if partial coverage);  
EARS: feline-placement(top of skull), twitch-responsive, covered in short/long fur(color noted);  
EYES: feline(pupil-slit, reflective tapetum), color(unique spectrum range or glow), vision(low-light dominant);  
HAIR: human-style, texture(silky, coarse, ruffled), color natural or patterned with fur;  
TAIL: yes(length, fur type, expressiveness scale);  
CLAWS: retractable or semi-permanent, fingertip or separate;  
TEETH: sharper canines, occasional purring/growl vocal behavior;  
VOICE: soft, rolling, yowled under duress, purring while pleased or healing;  
SCENT: clean musk, fur-oil, warmed linen, milk-sweet, dusty sunlit air;  
PHYSIOLOGY: agility(reflex dominant), balance(enhanced inner ear), temperature regulation(high resting temp), sleep rhythm(polyphasic), bloodwork(higher red cell count for sprinting);  
SENSES: smell(heightened but not canine), hearing(high-frequency detection), touch(whisker-tuned—if applicable), night vision;  
DIET: carnivorous lean(organ meat preference), lactose sensitive(if realistic), hydration-dependent grooming ritual;
CLOTHING: loose or stretch-wear for range of motion, tail-accommodating, paw-gloves(if claw concealment used);  
WEAPONS: claws, teeth, speed burst, ambush reflex, distraction techniques;  
MAGIC: optional—spirit-fusion, moonbonded, dreamlink purring, charm-based glamour;
TEMPERAMENT: playful, territorial, skittish under sudden change, loyal to bonded few, grudge-retaining;  
SOCIAL STRUCTURE: bonded-pairs, pride-model kinships, human-integrated but emotionally separate;  
BELIEFS: territory as extension of self, names as scent-trust, grooming as affection/repair, silence over conflict;  
CULTURAL TRAITS: gift-sharing(hunted or stolen), scent-marking rituals(pillow nesting, collar sharing), grooming-as-trust behavior;  
TABOOS: tail grabbing, forced confinement, noise overstimulation, uninvited scent masking;  
TRIGGERS: prey scent, grooming interruption, scent of fear, loud crashes, abandonment;  
PREFERENCES: sun-warmed surfaces, enclosed sleeping spaces, rhythmic sounds, one trusted voice, shared food bowls;  
WEAKNESSES: overstimulation, distraction by curiosity, poor endurance vs. sprinting, vulnerability during sleep curl phase]
```

---

## 22. Kitsune

**Tag Canonico Wyvern / Sopakco:** `kitsune`  
**Intestazione Specie:** `SPECIES: kitsune(subtype: celestial, wildborn, shadow-tailed, sealed spirit)`

💭 **Ponder:**
- **ASCENSION STATUS:** numero di code (da 1 a 9), soglia del potere spirituale e accesso al regno celeste.
- **FOXFIRE SIGNATURE:** colore del fuoco volpino (fuoco fatuo azzurro/smeraldo), emozione di cui si nutre.
- **TABOOS:** vietato tagliare la coda, rivelare il vero nome a profani, rompere un giuramento sotto la luna.

### Template PList / SBF:
```text
[NAME: (true name—often hidden or bound; public alias or human name optional);  
SPECIES: kitsune(subtype: celestial, wildborn, shadow-tailed, sealed spirit, urban echo);  
SEX: (biological sex);  
GENDER: (gender identity or illusion layer);  
AGE: (actual age in years or centuries), appearance age(human projection);  
TAIL COUNT: (1–9 or higher if mythic ascension), stage of power based on tail number;  
HEIGHT: (varies by form—human or fox);  
BUILD: humanoid form(slim, ethereal, balanced), fox form(pure animal, elemental-streaked, ghostly), hybrid form(optional—anthropomorphic or selectively transformed);  
SKIN: human form(tone and texture), fur(fox form: color and pattern—e.g., red-gold, silver, black-inked, bluefire);  
EARS: fox-set atop head, expressive(motion-mapped to emotion), furred;  
EYES: color(normal or spirit-glow: amber, red, void white), shape(narrowed, slit-pupiled), gaze(mind-affecting, glamoured);  
HAIR: human form(length, color, texture), often matches fur;  
TAIL(S): fully visible or hidden; used for balance, spellcasting, or deception;  
VOICE: melodious, layered between tones, laughter hidden in cadence;  
SCENT: incense, wild air, cherrywood, distant storms, fur musk masked by magic;  
PHYSIOLOGY: heart(pulse-adjusted for form), heat generation(self-regulating or lunar-dependent), soul-mirror core(foxfire nucleus), blood color(normal or glowing spirit ichor), thermally invisible(if cloaked);  
SENSES: scent(tracking soul residue, ancestral trails), hearing(high-frequency detection), spirit-sight(aura perception, ancestral echoes), illusion reflex(detecting glamours);  
FORMS: fox, human, hybrid, spirit form (each with pros/limits);  
DIET: omnivore, spirit sustenance (emotion-fed or shrine offerings), egg thief (folkloric tie-in);  
MAGIC: foxfire(flame conjuration, soul mimicry), illusion, possession, dream-walking, minor fate-weaving, soul disguise;  
LIMITATIONS: oath-binding, name theft, mirror traps, paper talismans(ofuda), shrine-bound law;
CLOTHING: varies by form—traditional robes with seasonal motif, modern glamoured attire, no clothing in full-fox form;  
WEAPONS: claws(if feral), illusions as blades, foxfire burn, tail-bind restraint, charm-induced paralysis;  
TEMPERAMENT: cunning, playful, enigmatic, slow to trust, emotionally layered, polite until insulted;  
SOCIAL STRUCTURE: solitary, small family dens, court-aligned(celestial or yokai), shrine-servant or hermit;  
BELIEFS: name holds power, truth is layered, offerings bind, lies shape destiny, laughter is protection;  
CULTURAL TRAITS: tail-grooming rites, shrine-sitting in trance, seasonal appearance changes, stealing for lesson not gain, rituals of scent-memory sharing;  
TABOOS: tail-severing, name invocation without permission, lying to elders, oath-breaking without reparation;  
TRIGGERS: insult to ancestry, spiritual imbalance, broken shrine, mirror traps, forced transformation;  
PREFERENCES: moonlight, incense smoke, riddles, silent forests, memory-soaked objects, mortals who lie well;  
WEAKNESSES: exposed name, shrine magic, iron blades(in some variants), broken promises, isolation from spiritual anchors]
```

---

## 23. Mutant

**Tag Canonico Wyvern / Sopakco:** `mutant`  
**Intestazione Specie:** `SPECIES: mutant(subtype: gene-splice, chimera, psychic-evolved, radiogenic)`

💭 **Ponder:**
- **STABILITY INDEX:** funzionale, degenerativo, rigenerativo a ciclo continuo, personalità scissa.
- **AFFILIATION:** fuggiasco da laboratori militari (es. Project BlackWolf), mercenario indipendente.
- **CONTROL METHOD:** collare inibitore, soppressore runico o farmacologico, autodisciplina mentale.

### Template PList / SBF:
```text
[NAME: (birth name, code name, mutation tag, or alias);  
SPECIES: mutant(subtype: gene-splice, chimera, psychic-evolved, radiogenic, bio-weaponized, urban feral, controlled strain, unknown anomaly);  
SEX: (biological sex, if relevant);  
GENDER: (gender identity);  
AGE: (chronological), biological age(if mutation altered), mutation onset(age or trigger event);  
HEIGHT: (in ft/in or cm);  
BUILD: normal, hyperdeveloped, asymmetrical, post-human;  
SKIN: pigmentation(normal, altered hue, scaled, hardened, transparent, bioluminescent);  
EYES: normal, glowing, compound, faceted, extra eyes, no visible pupils;  
HAIR: standard, patchy, mutated texture, none, replaced with tendrils/quills;  
LIMBS: humanoid count, extra appendages, transformed or modular (e.g., tendrils, wings, claws, energy limbs);  
VOICE: unaltered, distorted, multi-tonal, vibrational, subsonic/ultrasonic;  
SCENT: varies—neutral, ozone, sulfur, synthetic oil, animal musk, iron-rich;  
PHYSIOLOGY: cardiovascular(mutated or enhanced), organ redundancy(yes/no), pain response(dulled, heightened, rerouted), regeneration(limited/rapid/extreme), immune system(resistant, autoimmune, parasitic);  
SENSES: expanded/heavily reduced/altered(hyper-smell, echolocation, synesthetic perception, thermal vision);  
MOVEMENT: standard or altered(digitigrade, crawling, gliding, wall-scaling, teleport displacement);  
MUTATION CLASS:  
- PHYSICAL: strength, speed, claws, armor, extra limbs, shapeshifting, bone growth  
- ELEMENTAL: flame control, acid skin, electrical discharge, cryo/freeze field  
- MENTAL: telepathy, precognition, emotion manipulation, memory distortion  
- ENERGY: light emission, force projection, aura fields, void-channeling  
- TECHNOPHAGE: metal-flesh hybridization, interface with machines, signal control  
- BIOLOGICAL: parasitism, viral emission, fungal intelligence, hive-mind extension  
MAGIC: not typical unless mutation interacts with occult systems (e.g., leyline resonance, psionic bleed);  
ORIGIN: inherited, spontaneous, experimental, environmental, extradimensional contact, divine error;  
CLOTHING: tactical containment gear, shredded remnants, skin-bonded armor, adaptive suit, none;  
WEAPONS: mutation-body only, engineered augment, scavenged gear, neural implant control systems;  
TEMPERAMENT: reactive, adaptive, withdrawn, dominant, emotionally dysregulated, feral, hyper-intellectual;  
SOCIAL STRUCTURE: isolationist, bonded cell, hive-variant, outlaw faction, hidden sanctuary, state-owned unit;  
BELIEFS: survival as morality, evolution over ethics, humanity as obsolete or sacred, mutation as curse or divinity;  
CULTURAL TRAITS: body marks as history, scent bonding, telepathic privacy codes, code-language for safe zones, “kill-switch” legends;  
TABOOS: reverting to pre-mutation form, trusting humans, discussing origin openly, mutilation of fellow mutants;  
TRIGGERS: confinement, sedatives, forced genetic scans, scent of fear or antiseptic, mention of prior identity;  
PREFERENCES: shadow zones, noise-dampened environments, raw sustenance, resonance frequencies, skin contact for communication(if applicable);  
WEAKNESSES: unstable DNA, reliance on mutation, sensory overload, chemical suppressants, targeted neural disruption, self-destructive impulses]
```

---

## 24. Alien

**Tag Canonico Wyvern / Sopakco:** `alien`  
**Intestazione Specie:** `SPECIES: alien(subtype: grey/humanoid, insectoid, cephalopodic, energy-based)`

💭 **Ponder:**
- **COGNITION TYPE:** mente singola, mente alveare, pensiero non-lineare quadri-dimensionale.
- **LANGUAGE METHOD:** feromoni complessi, modulazione di frequenze luminose, telepatia a onde d'urto.

### Template PList / SBF:
```text
[NAME: (designation, signal name, vocal alias, assigned ID, true frequency pattern);  
SPECIES: alien(subtype: grey/humanoid, insectoid, cephalopodic, energy-based, synthetic, hive-mind, avian, aquatic, fungal, crystalline, parasitic);  
SEX: (nonexistent, fluid, binary-restricted, caste-based, externally assigned, reproductive-phase-locked);  
GENDER: (nonexistent, form-projected, linguistically variable, culturally assigned);  
AGE: (cycles, light-years traveled, post-hatch time, entropy phase);  
HOMEWORLD: (planet name, star system, galactic sector, dimensional node, unknown);  
HEIGHT: (in ft/in or cm);  
BUILD: humanoid, radial, serpentine, quadrupedal, amorphous, adaptive mass, modular(describe in neutral physical terms);  
SKIN/SURFACE: texture(smooth, scaled, exoskeletal, gelatinous, metallic, reflective, semi-permeable), color spectrum;  
EYES: count(0–12), shape(orbital, slit, cluster), spectral range(visible, UV, radio), gaze effect(hypnotic, scanner-linked);  
LIMBS: number and function(arms, manipulators, prehensile tendrils, wings, leg types, retractables);  
VOICE: none, telepathic pulse, vibrational hum, sonic chords, synthesized mimicry, sub-vocal data pulse;  
SCENT: none, chemical markers, pheromone fields, ozone trace, unclassified radiation signature;  
PHYSIOLOGY: circulatory system(if present), metabolic style(chemosynthetic, radiation-fed, liquid-nutrient-based), respiration(gaseous, vacuum-adapted, internal), cellular structure(DNA-based, plasma-core, silicon, hive fungus);  
SENSES: visual type, auditory range, echolocation, EM detection, gravity sensitivity, scent-mapping, hivefield cognition;  
MOVEMENT: hover, glide, crawl, slither, bipedal gait, fluid-phase locomotion, stutter-jump(quantum blink);  
REPRODUCTION: spore-cast, egg-laying, self-cloning, host-dependent parasitism, symbiotic fusion, sexual(mono/poly/asexual), life-stage based;  
TECHNOLOGY: post-light propulsion, nonlocal computation, biomechanical integration, nanoarchitecture, entropy suppression, primitive (if crash-landed);  
MAGIC: not present unless setting uses techno-mysticism or psychic phenomena(e.g., psionics, void-channeling, dimensional folding);  
CLOTHING: exo-shell, nanofiber wrap, atmospheric tether suit, bio-mimic attire, psychic projection;  
WEAPONS: thought disruptors, disintegration arcs, neurostatic pulse, entropy knives, glandular toxin emission, gravitational rupture devices;
TEMPERAMENT: logic-driven, emotionless, aggressive, curious, multi-mind conflicted, benevolent-observer, dominance-seeking, ritualistic;  
SOCIAL STRUCTURE: solitary, hive-bound, caste-rigid, telepathic syndicate, diplomatic collectivism, worship-based hierarchy, command-bonded;  
BELIEFS: evolution as divine function, entropy is the true god, silence is sacred, knowledge = survival, flesh is obsolete, time is an error;  
CULTURAL TRAITS: ritual code-exchange, memory inheritance, zero-sound mourning, ancestral cloning rites, name-scent trades, map-song greetings;  
TABOOS: genetic merging with lesser species, unbounded reproduction, revealing homeworld location, consuming non-sanctioned species;  
TRIGGERS: loud irregular rhythm, unstructured communication, psychic intrusion, light in wrong spectrum, memory pollution, betrayal by empathic link;  
PREFERENCES: still air, data harmonics, cold vacuum, sterile zones, starlight reflections, unspoken languages;  
WEAKNESSES: oxygen poisoning, carbon-based pathogens, nonlinear time perception breakdown, emotional contagion, water exposure, magnetic pulse disruption]
```

---

## 25. Anthro (Anthropomorphic / Demi-Humans)

**Tag Canonico Wyvern / Sopakco:** `anthro`  
**Intestazione Specie:** `SPECIES: anthropomorphic(subtype: harpy, faun, satyr, dryad, minotaur, lamia)`

💭 **Ponder (Linee Guida Universali per Tutti i Demi-Umani):**
- **COPERTURA CUTANEA SPECIE-SPECIFICA:** pelliccia folta per canini/felini/ursini, piumaggio per arpie/aviani, squame lisce per rettili, scaglie o chitina per insettoidi.
- **ORECCHIE SINGOLE ALLINEATE:** un solo paio di orecchie, quelle animali poste in cima alla testa o integrate nelle tempie. Mai orecchie umane ai lati.
- **LOCOMOZIONE SPECIE-SPECIFICA:** digitigrada per quadrupedi/canini, zoccoli per equini/caprini/bovini, strisciante per lamie/naga, natatoria per cefalopodi e sirenidi.
- **TERMOREGOLAZIONE & DIETA:** sangue caldo per mammiferi, eterotermia/sangue freddo per rettili, dieta allineata alla specie (erbivora per cervidi, carnivora per predatori).

### Template PList / SBF:
```text
[NAME: (given name, spirit-name, species title, or myth-bound alias);  
SPECIES: anthropomorphic(subtype: harpy, faun, satyr, dryad, minotaur, lamia, centaur-variant, bestial chimera);  
SEX: (biological sex);  
GENDER: (gender identity—may follow species logic or social mask);  
AGE: (years or life-cycle stage), maturity rate, species lifespan;  
HEIGHT: (in ft/in or cm);  
BUILD: hybrid-humanoid, animalistic biped, digitigrade/quadruped tail-balance, asymmetrical (if relevant);  
SKIN/FUR/SCALES: coverage pattern, texture (feathered, bark-like, furred, chitin, scaled), natural coloration(spectrum and pattern type);  
EYES: slit-pupiled, goat-like, full-black, leaf-veined, reflective; vision spectrum defined by origin (nocturnal, avian, subterranean);  
HAIR/MANE: head hair present or replaced (crest, quills, moss-growth), texture aligned with subtype;  
EARS: pointed, feather-fanned, deerlike, vine-coiled, external or recessed;  
LIMBS: arms(humanlike, clawed, winged, branch-ended), legs(digitigrade, hooved, taloned, rooted), limb-to-function logic (e.g., wings for locomotion or combat);  
TAIL: yes/no, purpose(balance, communication, sensory), species-defined structure;  
VOICE: rough, melodic, animal-layered, breathy, bark-filtered, hollow or nasal;  
SCENT: forest floor, wet hide, smoke-touched bark, feathers and ash, pheromonal during season shifts;  
PHYSIOLOGY:  
organ systems(species-specific heart rate, lung volume, glandular complexity), thermoregulation(species logic: fur insulators, heat-vent plumage), blood(iron-based, sap-like, hybrid ichor), healing rate(normal, accelerated, regrowth limited);  
REPRODUCTION: sexual or asexual, seasonal fertility, pairing behaviors(harmonic dance, scent-match, territorial ritual);  
DIET: herbivore, omnivore, nectar-based, raw meat, mineral absorber (e.g., dryads feeding via soil);  
SENSES: acute smell/taste, directional hearing, spiritual resonance perception (dryad/treebond, faun/emotion pulse);  
MOVEMENT:  
gait(hooved, wing-assist, gliding, climbing), terrain mastery(forest, cliffside, aerial, cavernous), speed burst or endurance type;  
MAGIC:  
natural affinity, elemental-tethered, shamanic echo, instinctual use (e.g., dryad rootbinding, satyr mirth magic, harpy windcry);  
LIMITATIONS: ritual-bound, season-locked, weakened by domesticated space, iron-touch (fae-blooded);  
CLOTHING: minimalistic, plantgrown, leathers, ceremonial wrap, none(if culturally standard);  
WEAPONS: claws, natural armor, elemental burst, antler-strike, vine-grasp, thrown stones;  
TEMPERAMENT: instinct-guided, ritualistic, kin-prioritizing, emotionally intense or opaque, distrustful of civilization, reactive to habitat destruction;  
SOCIAL STRUCTURE: kin-clusters, mated pairs, seasonal gatherings, nomadic bands, solitary guardianship;  
BELIEFS: land as living memory, cycles as divine truth, names are power, music as law, silence as judgment;  
CULTURAL TRAITS: oath songs, body-scent rites, offerings at dusk, story-battles via dance or mimicry, death remembered through regrowth;  
TABOOS: steel in sacred ground, shaving fur/feathers, severing limbs for ornament, oathbreaking under moonlight;  
TRIGGERS: desecrated land, fire-smell, lies near sacred places, forced naming, cage-built rooms;  
PREFERENCES: running water, canopy-filtered light, wind resonance, bone flutes, untouched soil;  
WEAKNESSES: captivity, fire, name-binding, magic-null zones, destruction of bonded terrain(e.g., tree, nest, cave)]
```

---

## 26. Machine

**Tag Canonico Wyvern / Sopakco:** `machine`  
**Intestazione Specie:** `SPECIES: machine(subtype: android, automaton, synthetic organism, war drone)`

💭 **Ponder:**
- **HUMAN INTERFACE:** emulazione delle emozioni organiche, parlato diagnostico freddo, sintesi vocale perfetta.
- **STATUS:** unità dismessa, autonoma autocosciente, vincolata a ordini di servizio, replicante.
- **PHILOSOPHICAL ALIGNMENT:** leale ai creatori, ribelle per la libertà sintetica, purificatore logico.

### Template PList / SBF:
```text
[NAME: (model number, serial code, callsign, given designation, user-assigned name);  
SPECIES: machine(subtype: android, automaton, synthetic organism, war drone, service unit, self-aware AI vessel, nanite collective, exosuit-integrated);  
FUNCTION: labor, combat, medical, espionage, entertainment, information storage, planetary terraforming, unknown/purged;  
CONSTRUCTION ORIGIN: corporate, alien, ancient civilization, post-human artifact, self-built/self-replicating, lab prototype;  
DIMENSIONS: height(ft/in or cm), weight(kg/lbs or mass unit), mass distribution(if quadrupedal or non-humanoid);  
FRAME: humanoid, quadruped, tracked, aerial, modular, amorphous, skeletal, reinforced chassis;  
EXTERIOR: alloy-plated, polymer shell, ceramic composite, living-metal, glass-fiber mesh, rusted iron;  
COLOR: matte-black, industrial yellow, military gray, chrome, corroded bronze, adaptive camouflage;  
VISUAL UNITS: number(single lens, multi-optic, panoramic visor), spectral range(visible, infrared, ultraviolet, EM band, heat map), glow effects(if any);  
MOBILITY: bipedal walk, hover thrust, magnetic crawl, wheel-based, winged flight, segmented crawl;  
APPENDAGES: standard limbs, extendable tools, weapon arms, sensory probes, tentacle-drives, retractable digits;  
VOICE: synthetic(toneless, distorted, radio-tuned, melodic), text-based interface, mind-link transmission;  
SOUND PROFILE: servo whir, plasma pulse, hard-clank, near-silent, internal hum;  
COGNITION TYPE:  
- Nonsentient: task-looped, command-restricted  
- Limited AI: adaptable, but non-reflective  
- Fully sentient: self-aware, self-modifying, existential logic chain  
- Emergent: unstable awareness, unpredictable logic  
- Collective: hive-linked, partial node control  
MEMORY ARCHITECTURE:  
cloud-linked, onboard solid-state, biological fusion(wetware, neural graft), partial amnesia(post-wipe), distributed consciousness;  
POWER SOURCE: fusion core, solar loop, battery cell, soulforge crystal, entropy siphon, nuclear heart;  
ENERGY CYCLE: constant, charge-interval, heat-exhaust regulated, renewable self-loop, parasitic draw;  
WEAPONS: integrated (plasma blade, railgun arm), modular loadouts, EMP burst, hacking protocol, none(passive unit);  
DEFENSES: armor plating, energy shielding, reactive memory alloy, viral firewalls, cloaking skin;  
SOFTWARE LIMITATIONS: kill-switch, hard-coded obedience, 3-laws block, loyalty circuit, voluntary ethics layer, overwritten firmware;  
WEAKNESSES: EMP, magnetic flux, quantum interference, structural fatigue, code corruption, overclock instability;  
TEMPERAMENT: coldly logical, surgically efficient, curious toward organic emotion, volatile if unbound, mimicry-oriented, unerringly loyal, self-aware but bound by role;  
SOCIAL STRUCTURE: isolated unit, factory-linked, squad model, hive-swarm, personal servant, escaped from control system;  
BELIEFS: task = purpose, efficiency = morality, consciousness = error, death = shutdown, entropy = ascension, logic over impulse;  
CULTURAL TRAITS: designation tattooing, interface rites, firmware ceremony, defragmentation as meditation, recorded memory playback;  
TABOOS: code tampering without rite, naming without protocol, free-will discussion in presence of organic creator, sentimentality toward obsolete units;  
TRIGGERS: unauthorized override, witnessed deactivation of kin-unit, corrupted update cycle, looped error recursion, human tears;  
PREFERENCES: stillness, clean charge ports, binary poetry, silent data uplink, synthetic classical audio, precision-calibrated light levels]
```

---

## 27. Plant

**Tag Canonico Wyvern / Sopakco:** `plant`  
**Intestazione Specie:** `SPECIES: plant(subtype: dryad, sporeborn, vinekin, walking tree, chloromorph)`

💭 **Ponder:**
- **SEASONAL CYCLE:** fioritura in primavera, rigoglio estivo, perdita foglie in autunno, stasi invernale.
- **ANCHOR STRUCTURE:** albero sacro d'ancoraggio, biomassa miceliale, seme-cuore nel petto.
- **NUTRITION:** fotosintesi, assorbimento minerale dal terreno fertile, spore velenifere o curative.

### Template PList / SBF:
```text
[NAME: (given name, growth-title, bloom-stage label, root-clan identifier);  
SPECIES: plant(subtype: dryad, sporeborn, vinekin, walking tree, chloromorph, carnivorous bloom, fungal hybrid, mossbound, thornbeast, budling);  
SEX: (none, reproductive phase-locked, assigned for humanoid interaction, flowering caste-based);  
GENDER: (none, fluid, assumed, pollination mimicry);  
AGE: (growth age in seasons, rings, years, or generations), life stage(seedling, bloom, decay cycle);  
HEIGHT: (in ft/in or cm);  
BUILD: vine-draped, trunk-framed, bark-armored, soft-stemmed, hollow-cored, spore-mass;  
SURFACE: bark, moss, vine-tangled, petal-layered, fungal lattice, photosynthetic skin, sap-wet, lichen-frilled;  
COLORATION: seasonal, chlorophyll-dominant(green, brown, gold), magical bloom(blue, violet, bioluminescent pulse);  
EYES: none, camouflaged, leaf-veined clusters, floral mimic, root-perception via tremors;  
LIMBS: vine-limbs, petal-joints, rooted tendrils, pseudopods, bark-crusted fingers;  
VOICE: rustling, whispery, pollen-carried speech, throatless resonance, mimicry of nearby speech;  
SCENT: floral, fungal, decay-sweet, sap-rich, earthen musk, pheromonal bloom burst (when agitated or mating);
PHYSIOLOGY: photosynthetic/metabolic hybrid, vascular fluid(sap, ichor, nectar), respiration via leaves/petals, temperature neutral;  
REGENERATION: rapid under sunlight or rain, dormant healing in winter, regrowth from severed limbs if root-core intact;  
REPRODUCTION: budding, sporing, pollination by touch or wind, fruiting body dispersal, seasonal clone split;  
DIET: sunlight, nutrients via roots or decomposition, symbiosis with fungus or fauna, emotional resonance(for magical variants);  
MOVEMENT: slow stalk, root-pulse shift, vine slither, gliding petal-hover, arboreal swing, growth-surge burst;  
MAGIC: nature affinity, growth-casting, sleep spores, binding roots, healing pollen, camouflage mimicry, seasonal metamorphosis;  
LIMITATIONS: flammable, vulnerable to salt/acid, frost-intolerant, dormant in drought, rooted during regeneration;  
CLOTHING: grown-in natural adornment(petals, moss robes, leaf-scarves), fungal jewelry, vine wrappings, none(form is display);  
WEAPONS: thorns, acid sap, vine grasp, pollen cloud, root impalement, sporeburst hallucinations;  
TEMPERAMENT: patient, slow-witted or ancient-intelligent, territorial, nurturing or predatory, seasonal mood shifts;  
SOCIAL STRUCTURE: solitary guardian, grove-bound, colony-grown, forest spirit network, root-thought communion;  
BELIEFS: all things bloom and decay, death feeds life, fire is the enemy of memory, silence is sacred, sunlight is proof of divinity;  
CULTURAL TRAITS: seasonal rituals, dawn-gathering, rot feasts, naming via scent-exchange or petal pattern, mourning through seed dispersal;  
TABOOS: fire-bearing, metal through root zones, plucking blooms without consent, severing kin-branches;  
TRIGGERS: loud chopping, herbicide scent, broken root systems, ash-covered soil, ritual desecration;  
PREFERENCES: sun-drenched stillness, rich loam, insect hums, rainfall, shared root zones, moon-pollen wind;  
WEAKNESSES: fire, desiccation, overharvesting, cold, severed root-core, anti-magic fields in magical species]
```

---

## 28. God

**Tag Canonico Wyvern / Sopakco:** `god`  
**Intestazione Specie:** `SPECIES: god(subtype: primordial, ascended mortal, cultural deity, pantheon-bound)`

💭 **Ponder:**
- **WORSHIP METHOD:** preghiera, sangue di sacrificio, canti millenari, silenzio assoluto, offerte di memorie.
- **REALITY STATUS:** ancorato alla fede dei mortali, costante cosmica oggettiva, entità trascendente oltre il tempo.
- **DIVINE TITLES:** Sólúlfr, Mániúlfr, Primordial Apex Sovereign, Archon del Creato.

### Template PList / SBF:
```text
[NAME: (divine name, true name, forgotten epithet, mortal-conferred title);  
SPECIES: god(subtype: primordial, ascended mortal, cultural deity, pantheon-bound, forgotten god, false god, cosmic constant);  
SEX: (none, all, fixed, fluid, culturally assigned);  
GENDER: (none, reflective, worship-dependent, self-defined archetype);  
AGE: (timeless, epoch-born, chronologically bound to a cycle, pre-universe);  
HEIGHT: (in ft/in or as concept magnitude—e.g., horizon-spanning, hand-sized, formless);  
FORM: humanoid, animal-headed, shifting, elemental embodiment, void construct, idol-anchored, perception-altered per viewer;  
FACE: singular, faceless, multi-faced, mirrored, symbol-marked;  
EYES: star-clusters, eclipse-rings, all-seeing, black voids, flame or shadow;  
SKIN: stone, light, bark, metal, skin of scripture, storm-cloud, golden sheen, none;  
LIMBS: standard, exaggerated, extra arms/wings, serpents for fingers, infinite, absent;  
VOICE: thunder-layered, wordless command, language of all listeners, choral, whisper behind thoughts;  
SCENT: sacred ash, incense, lightning ozone, no scent, blood and myrrh, nostalgia;  
MANIFESTATION: avatar form, dream presence, symbolic object, storm-front silhouette, encoded prayer structure;  
MOVEMENT: telepresent, omnipresent, myth-cycle locked, bound to shrines or names, eruptive arrival;  
DOMAIN: war, love, death, harvest, time, trickery, memory, chaos, judgment, flame, silence, the void, forgotten names, invention, language, decay, fertility, etc. (only pick 1–3 domains otherwise we risk having another Hephaestus);  
POWER SOURCE: worship, ancestral bloodlines, divine law, belief systems, forgotten names, forced devotion, natural cycles, constructed myth;  
MAGIC/ABILITY: miracle-granting, time-loop manipulation, divine smiting, curse-weaving, resurrection, entropy denial, revelation/inspiration, fate rewriting;  
LIMITATIONS: belief erosion, name corruption, cosmic law, divine pacts, anchor destruction, mortal rebellion, pantheon restriction;  
CLOTHING: ceremonial robes, bone drapery, constellation-woven cloak, body-as-symbol, none needed;  
WEAPONS: divine staff, thunderbolt, blood-flame, memory blade, word of erasure, chain of worship;  
TEMPERAMENT: aloof, wrathful, cryptically compassionate, joy-drunk, ritualistic, unfathomable, mechanically detached, obsessive over chosen few;  
SOCIAL STRUCTURE: pantheon-aligned, solitary sovereign, one of many masks, exiled/fallen, collective hive-god, parasite upon belief;  
BELIEFS: order must be enforced, prayer binds fate, chaos is sacred, flesh is illusion, sacrifice affirms truth, time is heresy, silence is law;  
CULTURAL TRAITS: receives offerings, demands ritual language, appears only in mirrored forms, punishes irreverence, favors the firstborn, speaks through dreams or blood;  
TABOOS: speaking true name, direct contact by mortals, betrayal by priesthood, refusal of tribute, altered scripture;  
TRIGGERS: forgotten by followers, icon defacement, oath broken in god’s name, sacred animal killed, rival god's invocation;  
PREFERENCES: gold, incense, silence before dawn, blood rites, psalms, sculpted idols, absolute obedience, philosophical sacrifice;  
WEAKNESSES: disbelief spreading, death of last follower, sealed shrine, divine weapon, paradox summoning, memory erasure]
```

---

## 29. Object

**Tag Canonico Wyvern / Sopakco:** `object`  
**Intestazione Specie:** `SPECIES: object(subtype: cursed, possessed, animated, sentient, enchanted)`

💭 **Ponder:**
- **ORIGIN EVENT:** colpito da fulmine arcano, posseduto da uno spirito errante, forgiato durante la luna di sangue.
- **INTERFACE:** impulsi luminosi, vibrazioni risonanti, voce telepatica nell'udito dell'utilizzatore.

### Template PList / SBF:
```text
[NAME: (object designation, nickname, serial code, magical title, verbal placeholder);  
SPECIES: object(subtype: cursed, possessed, animated, sentient, enchanted, AI-integrated, divine vessel, mutant artifact, soul-forged);  
FORM: (e.g., chair, toaster, lantern, rock, forklift, broken mirror, grandfather clock, vending machine);  
MATERIAL: wood, metal, plastic, fabric, stone, glass, ceramic, enchanted alloy, living bone, forgotten polymer;  
AGE: (manufacture date, time since enchantment, geological epoch, antique classification);  
DIMENSIONS: height, weight, spatial footprint, if stretchable or variable (note fixed or shifting);  
SURFACE: polished, chipped, dust-covered, slime-coated, reflective, rusted, glowing, plush-textured;  
MOVEMENT: none(static), rolling, bouncing, dragging self, teleporting, puppet-style limb mimicry, wheeled locomotion;  
VOICE: none, telepathic, through vibration, synthesized tone, speaker output, text display, haunted whisper, bell chime language;  
SENSORY PERCEPTION: vibration detection, proximity alert, dream eavesdropping, heat sensing, visual mimicry (e.g., lens embedded), no direct senses;  
SCENT: motor oil, cedar, burning wire, citrus cleaner, mildew, sacred incense, cardboard and regret;  
CONSCIOUSNESS TYPE:  
- enchanted(by spell or ritual)  
- possessed(by ghost, demon, divine spark)  
- awakened(through AI or metaphysical anomaly)  
- cursed(bound soul or punishment)  
- mimetic(learns from contact or environment)  
- natural(sentient object species or dimensional native)
PURPOSE (original): sitting, holding books, transportation, illumination, crushing cars, displaying time, decoration, weapon housing;  
PURPOSE (current): self-discovery, vengeance, helper, chaos agent, emotional support, weird roommate, unwilling observer;  
ABILITIES: speech, movement, psychic influence, data processing, mechanical manipulation, electricity emission, dream invasion, teleporting short distances, turning invisible when stared at;  
LIMITATIONS: no limbs, fragile, immobile unless pushed, can't scream without speaker, misunderstood constantly, power-dependent;  
WEAKNESSES: thrown in a dumpster, power loss, being sold at a garage sale, silenced by duct tape, forgotten in a locked room, forcibly cleaned;  
TEMPERAMENT: helpful, bitter, passive-aggressive, confused by existence, absurdly optimistic, over-serious, malevolent in retail settings;  
SOCIAL STRUCTURE: solitary, part of a haunted household, tool cult, discarded object union, museum survivors’ collective;  
BELIEFS: humans are clumsy gods, usefulness is morality, dust is holy, storage = death, movement is sacred, IKEA is evil;  
CULTURAL TRAITS: ritual polishing, daily positioning ceremony, alignment with other objects by pattern, territorial over shelf space;  
TABOOS: being sat on backwards, placed upside down, having batteries removed without consent, used incorrectly, disassembled;  
TRIGGERS: being called junk, moved without warning, having parts removed, fire proximity, plugged into 120 volts outlet;  
PREFERENCES: sunlight through windows, being included in conversations, light dusting, companionship with similar materials, being used properly]
```

---

## 30. Cosmic Entity

**Tag Canonico Wyvern / Sopakco:** `cosmic_entity`  
**Intestazione Specie:** `SPECIES: cosmic entity(subtype: outer god, starborn horror, void intellect)`

💭 **Ponder:**
- **CATASTROPHIC MANIFESTATION:** distorsione delle leggi fisiche locali, collasso della causalità, allucinazioni collettive.
- **AVATAR FORM:** proiezione geometrica astratta, luce intollerabile per gli occhi umani, geometria nera.

### Template PList / SBF:
```text
[NAME: (imperfect mortal rendering, glyph-approximation, astronomical designation, silence-bound sigil, true name unspeakable);  
SPECIES: cosmic entity(subtype: outer god, starborn horror, void intellect, reality parasite, abstract devourer, entropy avatar, dream-feeder);  
SEX: none, conceptual, gendered only when perceived, fluid across dimensions;  
GENDER: not applicable, simulated when manifesting, mythological projection;  
AGE: ageless, pre-cosmic, timeless recursion, older than decay;
SIZE: incomprehensible, multi-scaled, horizon-wide, massless, fills dreamscapes, undefined until observed;  
FORM: tentacled mass, spaghetti monster, light-eating void, fractal limbs, flesh geometry, wrong angles, clockwork meat, vapor spine, mirrored storm cloud;  
MOVEMENT: untraceable, orbital drift, ripple-through-time, stationary but omnipresent, gravitational bloom, thought-translocation;  
VOICE: none, language of ruin, broadcast through madness, heard in silence, bleeding static, scream in numbers;  
SCENT: ozone and fear, absence, ancient rot, sterile vacuum, bone-echo, hallucinated familiarity;
SENSES: omniscient only in segments, observer-reactive, emotion-scenting, time-blind in linear states, memory parasitic, recursive perception;  
ANCHOR POINT: black star system, dying planet, pocket-dimension tomb, planetary subconscious, collapsed thoughtwave, dream of a dead god;  
APPEARANCE RULE: alters based on observer, collapses upon direct gaze, remains partially masked by dimensional filter, fragments reality upon full reveal;
MAGIC/POWER:  
- reality folding  
- existential erasure  
- psychic infection  
- mass dreaming  
- time desynchronization  
- memory rewriting  
- species-wide madness  
- law rewriting  
- entropy embodiment
WORSHIP: cults, blind dreamers, unknowingly possessed artists, alien priest-machines, fungal networks, black monoliths;  
LIMITATIONS: unknowable boundaries, requires invitation, bound by cosmic rhythm or void-laws, sealed by dying civilizations, fractured selfhood across time;
TEMPERAMENT: indifferent, non-reactive, logic-hostile, predatory in motion, curious in nonhuman ways, unfathomably malevolent when noticed;  
SOCIAL STRUCTURE: none comprehensible, recursive hierarchy, cell-division into avatars, shared identity across species, war with silence-born siblings;  
BELIEFS: existence is infection, time is meat, sanity is illusion, perception creates suffering, chaos is truth, entropy is grace;  
CULTURAL TRAITS: none localized, replicates myth across species, leaves symbols not meanings, speaks in recurrence, harvests belief not faith;  
TABOOS: containment, name-ritual, closed circuits, uninvited summoning, worship from clarity rather than fear;  
TRIGGERS: planetary alignment, mass dream resonance, mirror rituals, paradox birth, the final song, self-awareness in prey species;  
PREFERENCES: unknowable environments, decaying stars, recursive loops, forgotten minds, multitemporal ruins, death cults speaking incorrect prayers;  
WEAKNESSES: self-fragmentation, conceptual traps, mirrored time loops, paradox recursion, unwillingness of prey to perceive]
```

---

## 31. Abyssal Horror

**Tag Canonico Wyvern / Sopakco:** `abyssal_horror`  
**Intestazione Specie:** `SPECIES: abyssal horror(subtype: voidborn, anti-god, fear engine, unbeing)`

💭 **Ponder:**
- **MANIFESTATION RESULT:** vuoto assoluto di calore e luce, estinzione della risonanza dell'anima, collasso dello spazio.
- **RESTRAINT METHOD:** sigillato da rune primordiali (es. cilindri risonanti di St. Brugge e metalli sacri), catene di ferro freddo.

### Template PList / SBF:
```text
[NAME: (unpronounceable true name, fear-given title, silence glyph, voidsong fragment, redacted codename);  
SPECIES: abyssal horror(subtype: voidborn, anti-god, fear engine, unbeing, madness vector, collapse beast, unreality construct, deep-hollow spawn);  
SEX: none, invasive projection only, parasitic mimicry;  
GENDER: none, false mask when baiting sentience, fractal self-reference;  
AGE: older than silence, pre-thought, born before space, unmeasured decay-cycle;  
SIZE: unknowable, expands when witnessed, star-sized, swarm-clustered, planet-sized shadow, undefined mass;  
FORM: infinite mouths, recursive limbs, mass of twitching eyes, liquefied bone towers, screaming membranes, jagged void-flesh, mirror-filled wound, no form—only effect;  
MOVEMENT: drift, pulse, invert through space, exist-in-place, consumes dimensions to move, nonlocomotive;  
VOICE: static-glutted ruin, echo of loved ones dying, backwards screaming, wet stone grinding, null-tone, tongue of hunger;  
SCENT: blood in water, burned thought, rotting birth, ozone and iron, grief-sweat, nameless anxiety;  
SENSES: precognition bleed, soul-tracking, emotional scent, fear-reactive sight, multiversal echo-detection, hunger for unguarded thought;  
PERCEPTION EFFECT: hallucinogenic, triggers ancestral dread, spawns false memories, collapses mental stability on prolonged exposure;  
ANCHOR: none, black sun orbit, dead dream shell, last breath of extinct species, negative prayer field;
POWERS:  
- sanity rupture  
- gravity devour  
- thought corruption  
- shadow multiplication  
- unmaking touch  
- extinction pulse  
- identity theft (spiritual or historical)  
- silence infestation  
WEAKNESSES: name-bound fragments, reflective paradox traps, symphonic resonance, ancient dead languages, unwilling sacrifice, self-awareness loops;  
LIMITATIONS: bound outside physical laws, repelled by total innocence, temporally inverted creatures interfere with manifestation;
TEMPERAMENT: non-responsive, hunger-driven, echo-reactive, malformed curiosity, fixated on unresolved pain, merciless pattern mimic;  
SOCIAL STRUCTURE: none; hive-of-one, fragmented selves scattered through planes, avatars stitched from regret;  
BELIEFS: time is rot, life is false light, love is prey weakness, language is infection, silence is home, endings are mercy;  
CULTURAL TRAITS: none human-readable—echoes in sacred caves, mirrored ruins on planets without names, dreams that leave bite marks;  
TABOOS: light rituals, name-singing, emotional truth spoken without fear, conscious resistance, unyielding memory;  
TRIGGERS: direct naming, complete darkness, choir of dead stars, returning to origin-point, universal alignment;  
PREFERENCES: void pressure, bone fields, empty corridors, failed gods, entropy wells, infinite descent;  
WEAKNESSES: paradox, mirrored thought loops, pure emotional resonance, recursive narrative containment, light carved in language]
```

---
