# User Personas — Prompt `16:9` a Griglia (Avatar Dinamici & Avatar Outfit)

> **Obiettivo:** Generare tutti gli asset visivi delle **10 User Personas** in sole **28 generazioni** (`4` per gli Avatar Dinamici di Default + `24` griglie multi-pannello per tutti gli `80` slot SFW), mantenendo lo **stile di pittura semi-realistica unificato** delle Character Sheet Wave 1, **sfondi tematici dedicati** per ogni pannello e **zero errori anatomici** (singole orecchie lupine per i licantropi, orecchie elfiche per l'elfa, orecchie umane per le forme umane).
>
> **Dove salvare le immagini generate da Gemini Pro:**
> - **Avatar Dinamici (Part 1):** `E:\repository\SvartulfrVerse\scratch\persona_grids\avatars\` (`AV-A1.png`, `AV-A2.png`, `AV-J1.png`, `AV-E1.png`)
> - **Griglie Outfit (Part 2):** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\` (`J-1.png` ... `JHH-2.png`)
>
> **Regole di Generazione su Gemini Pro:**
> 1. Imposta **`16:9` Widescreen** su tutte le tavole multi-pannello (solo `AV-E1` usa **`2:3` Verticale**).
> 2. Allega **esclusivamente la singola reference** indicata per ciascuna scheda (`alyssa_reference.png`, `jasper_reference.png` o `echo_reference.png`).
> 3. Ogni griglia contiene **2, 3 o 4 pannelli verticali affiancati** separati da **barre verticali nette nero pieno (`6px`)**, con pose dinamiche naturali e **sfondo tematico coerente**, **zero testo**, **zero etichette** e **zero sconfinamenti tra pannelli**.
> 4. **Taglio Automatico:** Appena salvi i file in `scratch/persona_grids/`, il comando `python scripts/asset_reference_pipeline.py slice-outfit-grid --mode panels ...` rimuove le barre verticali divisorie al pixel e salva ogni avatar pulito in `assets/<Personaggio>/...`.

---

## PARTE 1 — Dynamic Default Avatars delle 10 Persona (`4` Generazioni Totale)

### `AV-A1` — Alyssa Werewolf Trio: Modern / DDM #07 / Fantasy (`16:9`, 3 Pannelli)
- **Reference da allegare:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\persona_grids\avatars\AV-A1.png`
- **Output del taglio:** `alyssa_modern_avatar.png`, `alyssa_ddm_avatar.png`, `alyssa_fantasy_avatar.png`

```text
3-panel horizontal 16:9 triptych showcasing three dynamic half-body (thigh-up / waist-up) character avatar portraits of the SAME petite 155 cm female werewolf matching the attached character reference sheet strictly 1:1 in face, mint-green doe eyes, soft nose freckles, curvy hourglass DD-cup figure, wavy caramel-chestnut hair, single pair of caramel wolf ears with black tips atop her head (ZERO human ears on sides), caramel-and-black wolf tail, Mannaz wrist rune, and semi-realistic digital painting style with refined clean ink linework. LAYOUT: Three equal vertical illustration panels side-by-side separated cleanly by crisp, thin solid pure-black 6px vertical divider bars. Each panel features a distinct dynamic pose, outfit, and full rich atmospheric background with ZERO text, ZERO labels, ZERO speech bubbles, and ZERO crossover across divider bars. LEFT PANEL (Modern Solarton): Alyssa smiling warmly with lively head tilt, wearing a sunny sunflower-yellow ruffled wrap crop top over light-blue high-waisted denim shorts, delicate sun chain necklace and three tiny platinum cartilage hoops per wolf ear, sunlit Southern California coastal campus plaza background with warm golden sunlight, swaying palm trees, and soft turquoise sky bokeh. CENTER PANEL (DDM Contractor #07): Alyssa in an alert confident tactical stance, wearing a sleek slate-white and charcoal-grey DDM Void-Weave high-collar tactical suit with orange/platinum '#07' shoulder patch, ARC wrist stabilizers, and subtle tactical chest harness, dark atmospheric DDM Voidspace subterranean command corridor background with cool cyan volumetric rim lighting. RIGHT PANEL (Fantasy Silverhaven): Alyssa poised gracefully with hand near hip pouch, wearing a fitted pale-yellow linen cropped tunic with laced corset neckline, brown wyvern-leather herb satchel strap, and gold-leaf hair braids, enchanted Silverhaven twilight stone courtyard background with glowing arcane streetlamps and silver moonlight.
```

---

### `AV-A2` — Alyssa Species Variants: Elf Fantasy / Human Modern / Human Historical (`16:9`, 3 Pannelli)
- **Reference da allegare:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\persona_grids\avatars\AV-A2.png`
- **Output del taglio:** `alyssa_elf_avatar.png`, `alyssa_human_modern_avatar.png`, `alyssa_human_historical_avatar.png`

```text
3-panel horizontal 16:9 triptych showcasing three dynamic half-body (thigh-up) character avatar portraits of Alyssa preserving 1:1 her exact face, mint-green doe eyes, delicate cheek freckles, curvy hourglass DD-cup frame, and long wavy caramel-chestnut hair from the attached sheet, BUT STRICTLY OVERRIDING HER SPECIES TRAITS FOR EACH PANEL in semi-realistic digital painting style. LAYOUT: Three equal vertical panels side-by-side separated cleanly by crisp, thin solid pure-black 6px vertical divider bars; full rich thematic environments, ZERO text, ZERO labels, ZERO crossover between panels. LEFT PANEL (Pureblood Forest Elf Fantasy): Give her LONG POINTED ELVEN EARS protruding cleanly through soft caramel-chestnut waves on the sides of her head (STRICTLY ZERO wolf ears on top of head and ZERO wolf tail); serene luminous expression wearing an ethereal Forest Nymph emerald-leaf and cream botanical corset bodice woven with tiny white moonflowers and living ivy vines around forearms, bathed in sunbeams inside an ancient dappled emerald elven forest glade with soft glowing pollen motes. CENTER PANEL (Modern / Sci-Fi Human): Give her ORDINARY HUMAN EARS naturally tucked behind her locks (STRICTLY ZERO wolf ears, ZERO elf ears, ZERO tail); warm confident modern smile wearing a pastel-yellow ribbed crop top under an open slate-black technical cropped jacket with sun pendant and delicate lobe hoops, set against a twilight futuristic Solarton glass skybridge and soft neon-gold coastal skyline bokeh. RIGHT PANEL (Historical Fantasy Human): Give her ORDINARY HUMAN EARS with small pearl lobe earrings (STRICTLY ZERO wolf ears, ZERO elf ears, ZERO tail); gentle graceful pose wearing a modest tailored sage-green and cream-linen historical bodice laced neatly across the chest with gold-embroidered shawl, set inside a warm candlelit Renaissance stone manor courtyard at dusk.
```

---

### `AV-J1` — Jasper Trio: Werewolf Modern / Human Modern / Human Historical (`16:9`, 3 Pannelli)
- **Reference da allegare:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\persona_grids\avatars\AV-J1.png`
- **Output del taglio:** `jasper_modern_avatar.png`, `jasper_human_modern_avatar.png`, `jasper_human_historical_avatar.png`

```text
3-panel horizontal 16:9 triptych showcasing three dynamic half-body (thigh-up / waist-up) character avatar portraits of Jasper matching the attached character reference sheet strictly 1:1 in lean athletic 193 cm build, sharp handsome jawline with light stubble hint, vivid mint-green eyes, nose freckles, and messy caramel-chestnut wolf-cut hair in semi-realistic digital painting style with crisp clean ink linework. LAYOUT: Three equal vertical panels separated cleanly by crisp, thin solid pure-black 6px vertical divider bars; full atmospheric backgrounds, ZERO text, ZERO labels, ZERO crossover between panels. LEFT PANEL (Werewolf Modern Default): Preserves his SINGLE PAIR OF CARAMEL WOLF EARS WITH BLACK TIPS atop his head (ZERO human ears on sides), wearing a washed faded matte-black oversized streetwear hoodie over dark tee with matte-black and acid-green circumaural wireless headphones resting around his neck, Mannaz left-wrist rune, Douglas platinum signet ring, and sly ironical half-smirk, Blackwood City sunset-and-neon rooftop balcony background with twilight palm silhouettes and cyan glow. CENTER PANEL (Human Modern / Sci-Fi Variant): Give him ORDINARY HUMAN EARS partly framed by wolf-cut locks (STRICTLY ZERO wolf ears and ZERO tail); cool relaxed hacker poise wearing a tailored matte-charcoal technical zip jacket over dark henley and sleek wrist smartwatch, rain-slicked cyberpunk neon glass balcony overlooking glowing city skyscrapers at night. RIGHT PANEL (Human Historical / Fantasy Variant): Give him ORDINARY HUMAN EARS partly covered by tousled brown locks (STRICTLY ZERO wolf ears and ZERO tail); sharp guarded rogue gaze wearing a dark charcoal laced linen tunic under a fitted brown leather scout vest with travel cloak clasped over one shoulder, mist-wrapped lantern-lit gothic medieval cobblestone street background at night.
```

---

### `AV-E1` — Echo AI Drone / Holo-Wave Dynamic Avatar (`2:3`, Ritratto Singolo)
- **Reference da allegare:** `E:\repository\SvartulfrVerse\assets\Echo\echo_reference.png`
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\persona_grids\avatars\AV-E1.png`
- **Output finale:** `E:\repository\SvartulfrVerse\assets\Echo\echo_avatar.png`

```text
Dynamic atmospheric avatar illustration in a 2:3 vertical frame matching the attached Echo reference sheet strictly 1:1 in geometry, proportions, and sleek magitech semi-realistic digital painting style. SUBJECT: A compact 30 cm hexagonal matte-black titanium and cold-iron Aegis counter-intrusion levitation drone hovering smoothly in a slight dramatic 3/4 tilt at center frame, engraved along its beveled edges with glowing emerald-green and electric-cyan Svartulfr runes, centered around a luminous stylized technomantic optical iris projecting floating 3D holographic emerald-cyan oscilloscope audio waveforms and translucent rune telemetry arcs in the air around it. BACKGROUND: Dramatic high-tech Blackwood City twilight balcony overlooking distant twilight skyline skyscrapers, warm sunset violet clouds meeting cool emerald-cyan ambient server-node reflections, shallow depth-of-field bokeh, zero text, zero borders, zero watermarks.
```

---

## PARTE 2 — Outfit Avatars delle 10 Persona (`24` Griglie `16:9` con Sfondo Tematico = `80` Slot SFW)

### Batch 1 — Core Modern Personas (`10` Griglie `16:9`)

#### `J-1` — Jasper Modern Outfits 1–4 (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\J-1.png`
- **Pannelli (`--cols 4 --names casual_home,campus,tactical_guild,abyssal_armor`):**
  1. `Casual / Home` | 2. `Campus` | 3. `Tactical Guild (Spell-Hacker Infiltrator)` | 4. `The Abyssal Armor (Summoned Demonic Steel)`

```text
4-panel horizontal 16:9 character outfit showcase strip featuring ONLY the male werewolf Jasper matching jasper_reference.png strictly 1:1 (193 cm lean athletic frame, messy caramel-chestnut wolf-cut hair, vivid mint-green eyes, SINGLE PAIR OF CARAMEL WOLF EARS WITH BLACK TIPS atop head and ZERO human ears on sides, bushy caramel-and-black wolf tail, Mannaz left wrist rune, platinum Douglas signet ring) in semi-realistic digital painting style. LAYOUT: Four equal vertical full-body / three-quarter dynamic portraits side-by-side separated cleanly by solid pure-black 6px vertical divider bars, ZERO text, ZERO labels, ZERO overlapping across bars. PANEL 1 (Casual / Home): Faded matte-black oversized graphic hoodie over dark tee, black jogger sweatpants with tail opening, black/white canvas high-top sneakers, matte black & acid-green wireless headphones around neck, USB keychain on belt, cozy twilight gaming bedroom background with warm ambient desk monitors. PANEL 2 (Campus): Charcoal crewneck tee with faded tech logo, relaxed smoke-grey tactical cargo pants with tail hole, grey/black suede skate shoes, black cordura messenger bag slung across chest, in-ear wireless buds in wolf ears, sunlit SUCC university glass campus courtyard background. PANEL 3 (Tactical Guild Infiltrator): Sound-dampening dark grey shadow-silk tactical hoodie with kevlar shoulder/forearm plates & wolf-ear hood slits over black compression long-sleeve, black ripstop cargo pants, mid-cut silent combat boots, diagonal magnetic back scabbard holding sleek dark dragon-glass katana, fingerless hacker gloves, modular mana belt, tactical grey face-paint anti-glare cheek streaks, misty neon-lit rooftop infiltration background. PANEL 4 (The Abyssal Armor): Full magically summoned smoke-black demonic steel plate armor with layered angular chestplate, articulated pauldrons, luminous occult-rune vambraces, fluted tassets, shadowy chainmail joints, clawed steel gauntlets, ghostly metallic hood with ear openings shadowing his glowing mint-green eyes, dragon-glass katana scabbard on back and curved black daggers at thighs, dark rift voidstorm cavern background.
```

#### `J-2` — Jasper Modern Outfits 5–8 (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\J-2.png`
- **Pannelli (`--cols 4 --names underground_dj,formal_gala,sleepwear,beach`):**
  1. `Underground DJ / The Verve` | 2. `Formal / Gala` | 3. `Sleepwear` | 4. `Beach`

```text
4-panel horizontal 16:9 character outfit showcase strip featuring ONLY Jasper matching jasper_reference.png strictly 1:1 (193 cm lean athletic frame, caramel-chestnut wolf-cut, mint-green eyes, single pair of caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel wolf tail, Mannaz left wrist rune, Douglas signet ring) in semi-realistic digital painting style separated by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. PANEL 1 (Underground DJ / The Verve): Sleeveless oversized matte-black technical hoodie worn open with UV-reactive glowing cyan geometric accents over deep-V black perforated mesh tank top showing lean chest & small silver nipple barbells, low-slung black tech joggers with platinum hip chain, fingerless DJ leather gloves, cyan LED biometric cuffs, transparent-sole cyber high-top sneakers, two glowing cyan horizontal under-eye UV lines, DJ headphones around neck, neon-lit underground night club DJ booth background. PANEL 2 (Formal / Gala): Sharp two-piece tailored dark charcoal wool suit worn open over unbuttoned crisp white poplin dress shirt (no tie, sleeves pushed slightly up forearms showing platinum Douglas wolf cufflinks), straight dark wool trousers with neat rear tail slot, polished black leather Oxfords, sleek slicked-back hair with stray forehead locks, luxury warm candlelit Villa Douglas grand ballroom background. PANEL 3 (Sleepwear): Oversized faded heather-grey vintage rock concert t-shirt and loose black cotton jersey sleep shorts with wide tail gap, barefoot, tousled sleepy hair and relaxed drooping wolf ears, soft dim moonlit bedroom background. PANEL 4 (Beach): Bare torso showing lean defined swimmer abs, silver nipple barbells, black neck cord with small titanium pendant, mid-thigh black surf boardshorts with acid-green/cyan geometric fade and tail slot, square dark cyan-mirrored sunglasses hooked or worn, rolled dark microfiber towel slung over shoulder, sunny Pacific ocean beach boardwalk background.
```

#### `J-3` — Jasper Modern Outfit 9 & Shifter Forms (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\J-3.png`
- **Pannelli (`--cols 3 --names succ_bears_spectator,hybrid_shift,full_shift`):**
  1. `SUCC Bears Forced Spectator` | 2. `Hybrid Shift (223 cm Biped)` | 3. `Full Shift (Svartr Quadruped Dire Wolf)`

```text
3-panel horizontal 16:9 showcase triptych featuring ONLY Jasper matching jasper_reference.png 1:1 in semi-realistic digital painting style, separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (SUCC Bears Forced Spectator): Full-body bored spectator sitting/standing inside icy SUCC Bears hockey arena stands, wearing heavy oversized matte-black hoodie with deep hood pulled forward hiding lowered caramel wolf ears, thermal black zip-pocket cargo joggers with caramel wolf tail out, heavy winter-insulated black high-top sneakers, and sleek dark-rimmed covert AR smart glasses with faint glowing cyan holographic reflection across lenses over bored mint-green eyes. CENTER PANEL (Hybrid Shift — 223 cm Biped Werewolf): Completely unclothed agile muscular 223 cm biped werewolf predator covered entirely in dense silky warm caramel-chestnut fur with slightly darker dorsal spine and long black-tipped caramel tail (ZERO white moon markings), elongated fierce caramel lupine muzzle with sharp white fangs and blazing bright mint-green predator eyes, thick neck mane, digitigrade wolf hind legs with black paw pads and sharp claws, subtle silvery-gold sub-dermal Mannaz pulse on left forearm, dramatic rocky moonlight cliff background. RIGHT PANEL (Full Shift — Svartr Quadruped Dire Wolf): Full quadruped dynamic running/prowling view of Svartr, an agile rangy giant caramel-chestnut dire wolf with darker dorsal stripe along spine, solid black-tipped tail, thick neck ruff, large swiveling black-edged caramel wolf ears, zero white markings, blazing intelligent mint-green eyes, misty moonlit evergreen pine forest floor background.
```

#### `E-1` — Echo All 4 Visual Modes (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Echo\echo_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\E-1.png`
- **Pannelli (`--cols 4 --names holo_wave,aegis_drone,sunflower_link,cyberspace_avatar`):**

```text
4-panel horizontal 16:9 showcase strip depicting the four operational visual modes of AI companion Echo matching echo_reference.png 1:1 in semi-realistic magitech digital art style, separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO readable UI words, ZERO borders. PANEL 1 (Holo-Wave Interface): Volumetric floating 3D emerald-green and cyan oscilloscope audio wave hovering mid-air above a sleek matte-black earpiece & modern glass backdrop, glowing concentric sound rings pulsing around a stylized geometric emerald technomantic eye emblem. PANEL 2 (Aegis Counter-Intrusion Drone): Compact 30 cm matte-black titanium & cold-iron hexagonal tactical drone levitating smoothly in dramatic 3/4 view with softly glowing emerald Svartulfr rune engravings along beveled edges, projecting active emerald-cyan AR radar scan grids inside a dark underground dungeon/Rift corridor. PANEL 3 (Sunflower Protocol Smart-Display): Sleek frameless translucent emerald-and-gold glass holographic smart-console screen suspended cleanly in space showing stylized glowing geometric sunflower emblem, clean glowing biometric pulse waveforms, and golden security nodes over dark Villa Douglas control desk background. PANEL 4 (Cyberspace Avatar — Emerald Lattice): Full-body sleek androgynous digital humanoid silhouette forged seamlessly from luminous cyan-and-emerald wireframe geometry over deep matte void-black light skin in Deep Cyberspace, glowing geometric nodes along collarbones and fingertips inside a vast glowing neon cyber-lattice void.
```

#### `A-1` — Alyssa Modern Outfits 1–4 (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\A-1.png`
- **Pannelli (`--cols 4 --names white_moon_tactical,solarton_sundress,blackwood_knitwear,pacific_cove_swimwear`):**

```text
4-panel horizontal 16:9 character outfit showcase strip featuring ONLY the petite 155 cm curvy hourglass werewolf Alyssa matching alyssa_reference.png strictly 1:1 (fair glowing skin, soft nose/cheek freckles, mint-green doe eyes, full DD-cup bust, narrow waist, long wavy caramel-chestnut hair, SINGLE PAIR OF CARAMEL WOLF EARS WITH BLACK TIPS atop head and ZERO human ears on sides, bushy black-tipped caramel wolf tail, Mannaz left wrist rune, platinum navel ring) in semi-realistic digital painting style separated by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. PANEL 1 (White Moon Tactical Field Gear): Sleeveless high-neck enchanted tear-resistant white tactical top leaving arms/shoulders bare with front zip & flat mithril buckles, fitted white tactical cargo pants with tail slit, modular white polymer medical belt with potion vials, fingerless white grip gloves, mid-calf white combat boots, high tight ponytail leaving wolf ears erect, mist-filled subterranean dungeon portal background. PANEL 2 (Solarton Sunlit Sundress): Sunny sunflower-yellow ruffled wrap crop top tied neatly under bust showing toned midriff and platinum crescent navel ring, frayed light-blue high-waisted denim shorts with tail hole, white canvas low-top sneakers, straw crossbody bag, amber sunglasses tucked at neckline, long loose hair with tiny boho side braids, sunlit Solarton boardwalk plaza with palms background. PANEL 3 (Blackwood Pine-Mist Knitwear): Cozy oversized ivory cable-knit sweater slipping playfully off one bare shoulder, opaque black thermal leggings with tail opening, chunky sand-colored knit leg warmers, cream fingerless arm warmers, suede caramel winter ankle boots, quartz crystal necklace, half-up hair wooden claw clip, misty Blackwood City pine autumn balcony background. PANEL 4 (Pacific Cove Moonlit Swimwear): Tasteful editorial crisp white two-piece triangle bikini with adjustable neck/side ties, sheer short white muslin pareo sarong knotted asymmetrically at hip, beige rope-handle beach tote bag, oversized tortoiseshell sunglasses resting in hair, barefoot with shell ankle bracelet, twilight glowing Pacific Cove ocean waves background.
```

#### `A-2` — Alyssa Modern Outfits 5–8 (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\A-2.png`
- **Pannelli (`--cols 4 --names moonflower_sleepwear,solarton_festival,succ_campus_anatomy,succ_track_sparring`):**

```text
4-panel horizontal 16:9 character outfit showcase strip featuring ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, wavy caramel-chestnut hair, mint-green doe eyes, single caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel tail, Mannaz left wrist rune) separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. PANEL 1 (Moonflower Dorm Silk Sleepwear): Worn cozy oversized washed-black cotton t-shirt slipping casually off one shoulder down to mid-thigh, soft white ribbed lounge shorts peeking underneath with tail gap, barefoot holding a warm ceramic teacup, messy high bun with champagne silk scrunchie and relaxed sleepy wolf ears, dim warm moonlit university dorm window background. PANEL 2 (Solarton Festival & Autumn Fair): Flowing floor-length white silk Empire-waist ceremonial festival gown richly embroidered in metallic platinum thread along sweetheart neckline and layered sheer georgette slit skirt with tail opening, gossamer silver-fringed white shawl draped over elbows, platinum gladiators, delicate platinum forehead chain with moonstone teardrop resting beneath erect wolf ears, warm lantern-lit Solarton autumn evening plaza background. PANEL 3 (SUCC Campus & Anatomy Lectures): Prestigious Academy Medical Division uniform with tailored crisp white double-breasted blazer piped in emerald green with platinum crest buttons over crisp white collared shirt, forest-green silk thin tie, dark charcoal pleated wool miniskirt with rear tail slot, green medical armband, medical stethoscope around neck, dark brown leather satchel, matte-black lace-up knee boots, straight sleek hair with platinum hairpins, bright modern SUCC university lecture hall background. PANEL 4 (SUCC Track & Pack Sparring Gear): Two-tone sunflower-yellow compressive sports-bra crop top, unzipped navy-blue windbreaker track jacket with yellow reflective piping, high-waisted navy-blue lycra biker shorts with tail eyelet, navy wrist sweatbands, sleek sports wireless earhooks, white/neon-yellow cushioned running sneakers, high bouncy ponytail with braided tip and swept-back wolf ears, sunlit forest track trail background.
```

#### `A-3` — Alyssa Modern Outfits 9–12 (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\A-3.png`
- **Pannelli (`--cols 4 --names seven_hills_spring,douglas_crescent_gown,succ_healer_lab_coat,logans_garage_biker`):**

```text
4-panel horizontal 16:9 character outfit showcase strip featuring ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, wavy caramel-chestnut hair, mint-green doe eyes, single caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel tail, Mannaz wrist rune) separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. PANEL 1 (Seven Hills Botanical Spring Dress): Form-fitting pastel ocean-blue ribbed cotton knit midi dress with sweetheart neckline, short sleeves, thigh side-slit, and rear tail seam, ivory knit cardigan folded lightly over arm, small sand-beige chain shoulder bag, honey-leather flat lace-up sandals, cherry-blossom hairclip next to left wolf ear, blooming Seven Hills sunlit garden greenhouse background. PANEL 2 (Douglas House Crescent Reception Gown): High-class tailored ivory crepe skirt-suit with deep-V single-button blazer worn over light mint-green silk blouse, tailored ivory mini pencil skirt with rear tail slit, glossy ivory patent leather 10cm pointed pumps, pearl choker & pearl wolf-ear drops, rigid ivory envelope clutch, vintage Hollywood glossy side-swept waves, grand sunlit Villa Douglas marble salon background. PANEL 3 (SUCC Healer Clinic & Lab Coat): Crisp spotless white heavy medical lab coat with rolled sleeves worn open over white sleeveless boat-neck jersey top, opaque black three-quarter capri leggings with tail gap, black medical stethoscope over shoulders, clipped photo clinic badge, low black canvas Converse-style sneakers, tidy high ponytail keeping ears clear, clean modern bright clinic office background. PANEL 4 (Logan's Garage & Highway Ride): Glossy heavy black leather biker jacket worn open over strapless sunflower-yellow bandeau tube top leaving shoulders/collarbone bare, quilted-knee black leather riding pants with metal-riveted tail slot, studded black leather choker, fingerless padded motorcycle gloves, matte black helmet with wolf-ear vents tucked under arm, mid-shin buckled black leather biker boots, single thick fishtail braid over back, warm neon-lit custom motorcycle workshop garage background.
```

#### `A-4` — Alyssa Modern Outfits 13–16 (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\A-4.png`
- **Pannelli (`--cols 4 --names villa_douglas_hearth,angelo_moreno_couture,clubbing_night,blackwood_pilates`):**

```text
4-panel horizontal 16:9 character outfit showcase strip featuring ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, wavy caramel-chestnut hair, mint-green doe eyes, single caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel tail, Mannaz wrist rune) separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. PANEL 1 (Villa Douglas Family Hearth Dinner): Floor-length deep ultramarine midnight-blue silk satin mermaid evening gown with softly draped cowl neckline, delicate jeweled micro-straps, bespoke rear tail drape, sheer sequined midnight-blue chiffon stole over elbows, hammered platinum clutch, sapphire-and-white-gold teardrop necklace & matching sapphire wolf-ear drops, soft French low chignon, warm blazing stone fireplace dining hall background. PANEL 2 (Angelo Moreno Couture "Ocean Shadow"): Exclusive haute-couture fluid iridescent gown shifting chromatically from abyssal teal-blue to emerald & amethyst light, sculpted geometric sweetheart corset bodice with invisible straps and flowing asymmetrical draped skirt, ethereal metallic amethyst floor-length silk veil cuffs, chromed geometric gladiator heels, rock-crystal and amethyst hairpins alongside liquid mirror-gloss hair, dramatic runway spotlight dark backdrop. PANEL 3 (Clubbing Night): Long-sleeved sheer black fishnet top layered tastefully over fitted supportive sunflower-yellow bandeau crop top, short light-wash denim pleated miniskirt with rear tail slot, black chain shoulder pouch, black wedge ankle-strap sandals, loose wild wavy hair dotted with tiny mini braids and glowing dark smokey eye makeup, vibrant pulsing purple/cyan dancefloor club lights background. PANEL 4 (Blackwood Studio Pilates & Stretch): Supportive crisp optic-white athletic sports crop bra with sunny yellow contrast trim over high-waisted optic-white full-length compression leggings with yellow-piped tail slot, barefoot holding a rolled yellow yoga mat and white hand towel, messy high bun with yellow scrunchie, glowing sunlit hardwood Pilates studio floor & mirror background.
```

#### `A-5` — Alyssa Modern Outfits 17–20 (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\A-5.png`
- **Pannelli (`--cols 4 --names lace_moonlit_sleepwear,succ_anime_club,succ_starlight_party,succ_bears_spectator`):**

```text
4-panel horizontal 16:9 character outfit showcase strip featuring ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, wavy caramel-chestnut hair, mint-green doe eyes, single caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel tail, Mannaz wrist rune) separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. PANEL 1 (Lace Moonlit Intimate Sleepwear): Graceful romantic ankle-length pure white cotton nightgown with thin straps, modest sweetheart neckline edged cleanly with delicate white eyelet sangallo lace and soft flowing ruffled skirt with rear tail slit, completely barefaced fresh-washed glow, barefoot, long silky loose waves tumbling to hips under soft pale moonlight curtains in a cozy dark bedroom. PANEL 2 (SUCC Anime Club Room 005): Fitted black cotton short-sleeve graphic crop top (featuring stylized dynamic anime dark-haired scarred hero graphic print centered on chest) leaving bare midriff and platinum navel bar visible above a high-waisted navy-and-mustard tartan pleated miniskirt with tail slot, crisp white Converse-style sneakers, small black flap leather crossbody purse, sunlit colorful university Anime Club room background. PANEL 3 (SUCC Starlight Party Dress): Crisp matte-white silk mikado off-shoulder fit-and-flare party dress with sculpted bustier bodice and lively flared mini skirt heavily embroidered in glowing golden sunbeams and ice-blue constellations, pearl-white platinum-chain mini clutch, white/ice-blue 9cm party heels, half-up star-crystal hairpins, warm fairy-lit university campus terrace party night background. PANEL 4 (SUCC Bears Hockey Spectator): Enormous vintage-style deep royal-blue & bright gold-yellow SUCC Bears #01 ice hockey jersey with crisp white stripe trim and bold blue-and-gold winged crest (matching official SUCC blue-and-gold team colors) swallowed down like a comfy mini sports dress on her tiny 155 cm frame with wide sleeves rolled neatly up her wrists over cozy black fleece-lined leggings (tail out), thick royal-blue & gold knit Bears team scarf, white/black insulated sneakers, holding warm paper hot-cocoa cup in noisy ice hockey stadium bleachers background.
```

#### `A-6` — Alyssa Shared Shifter Forms: Hvít Pure Lunar-White Hybrid & Full Shift (`16:9`, 2 Pannelli)
*(Valido identicamente per Alyssa Modern, Alyssa DDM #07 e Alyssa Fantasy!)*
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\A-6.png`
- **Pannelli (`--cols 2 --names maniulfr_hybrid_shift,hvit_full_shift`):**

```text
2-panel horizontal 16:9 creature-form showcase diptych depicting the TWO canonical White Moon wolf shift forms of Alyssa ("Hvít, The White Moon" / "Mániúlfr") matching alyssa_reference.png 1:1 in cohesive semi-realistic digital painting style, separated cleanly by a crisp 6px pure-black vertical center bar, ZERO text, ZERO labels, ZERO overlap. LEFT PANEL (Mániúlfr Biped Hybrid Shift — 185 cm): Unclothed, voluptuously curvy and powerfully maternal 185 cm agile biped werewolf she-wolf embodying the sacred Mother of Wolves and fertility (sculptural feminine hourglass proportions, pronounced wide maternal hips, shapely powerful thighs, narrow waist), completely covered in dense silky PURE LUNAR-WHITE fur (zero caramel patches) with an extra-lush, thick flowing SILVERY-WHITE MANE cascading cleanly from head and neck into a prominent, thick heart-shaped silvery-white fur chest ruff/gorgera that naturally and modestly covers her abundant chest, graceful pure-white lupine snout with dark slate nose, bright LUMINOUS GLOWING LUNAR-WHITE EYES, single pair of tall upright pure-white wolf ears with subtle silver tips atop skull (STRICTLY ZERO human ears on sides of head), lush bushy pure-white wolf tail with silvery sheen, digitigrade hind wolf paws with dark slate pads and sharp PURE-WHITE CLAWS VEINED WITH SILVER, subtle platinum Douglas signet ring on left paw finger and faint pearlescent crescent Mark of Máni glowing subtly through white fur on left hip, cool misty silver moonlit pine clearing background. RIGHT PANEL (Hvít Ancestral Quadruped Dire Wolf — Full Shift): Majestic noble prowling quadruped dire wolf stance with broad protective chest, thick glossy double coat 100% PURE LUNAR-WHITE across entire body, flowing lush SILVERY-WHITE NECK RUFF AND MANE, LUMINOUS GLOWING LUNAR-WHITE EYES, sharp PURE-WHITE CLAWS VEINED WITH SILVER, shimmering silver-pearlescent crescent moon marking on left flank, braided dark leather cord tied neatly around her silvery mane holding her Douglas platinum signet ring, single pair of upright pure-white wolf ears, dense moonlit Blackwood forest edge background.
```

---

### Batch 2 — Alyssa Werewolf Variant Personas (`4` Griglie `16:9`)
*(Nota: le forme Hybrid e Full Shift di `Alyssa DDM #07` e `Alyssa Fantasy` usano già la griglia `A-6` qui sopra.)*

#### `AD-1` — Alyssa DDM Contractor #07 Outfits 1–3 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AD-1.png`
- **Pannelli (`--cols 3 --names ddm_tactical_uniform,ddm_voidspace_lounge,ddm_black_ops_stealth`):**

```text
3-panel horizontal 16:9 character outfit showcase triptych featuring ONLY Alyssa (DDM Contractor #07) matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, wavy caramel-chestnut hair, mint-green doe eyes, single caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel tail, Mannaz wrist rune) separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (DDM Tactical Field Uniform #07): Tear-resistant slate-white & charcoal-grey DDM Void-Weave tactical field suit with high collar, dark reinforced elbow/shoulder guards, bright orange/platinum '#07' shoulder badge, ARC glowing wrist stabilizers, tactical thigh holster, med-pouch, charcoal tactical combat boots, partly tied back chestnut waves, glowing DDM Voidspace portal bay background. CENTER PANEL (DDM Voidspace Lounge Off-Duty): Soft clean ivory-pearl knit lightweight sweater tucked loosely over relaxed dark charcoal DDM lounge cargo pants with rear tail slot, hanging DDM '#07' metal dog-tag, black low flat ankle boots, hair cascading softly around erect wolf ears, warm dimly lit DDM contractor break lounge background. RIGHT PANEL (DDM Black Ops / LAZARUS Stealth): Sleek form-fitting sound-absorbing smoke-grey DDM shadow-silk infiltration suit with lightweight cropped tactical capelet, matte subdued '#07' emblem, subtle glowing cyan ARC tactical eye-visor over left eye, reinforced black tactical gloves, silent stealth boots, practical back braid freeing wolf ears, dark rainy concrete rooftop stealth background.
```

#### `AD-2` — Alyssa DDM Contractor #07 Outfits 4–6 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AD-2.png`
- **Pannelli (`--cols 3 --names ddm_council_formal,ddm_sleep_motel,ddm_casual_safehouse`):**

```text
3-panel horizontal 16:9 character outfit showcase triptych featuring ONLY Alyssa (DDM Contractor #07) matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, wavy caramel-chestnut hair, mint-green doe eyes, single caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel tail, Mannaz wrist rune) separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (DDM Council / Formal Briefing): Crisp tailored charcoal-grey and ivory DDM executive skirt-suit blazer with sharp lapels bearing crisp silver '#07' lapel pin, matching tailored trousers/skirt with neat rear tail opening, DDM badge lanyard, classic low-heel black pumps, poised neat updo framing wolf ears, sleek glass DDM Council war-room background. CENTER PANEL (DDM Sleep — Motel Quarters): Relaxed worn oversized black cotton t-shirt hanging effortlessly over soft dark sleep shorts with rear tail opening, barefoot, '#07' dog-tag necklace, completely barefaced with tousled chestnut hair falling softly around drooping sleepy wolf ears, nostalgic neon-lit motel bedroom window background at night. RIGHT PANEL (DDM Casual / Safehouse Off-Duty): Cozy off-shoulder oversized cream-ivory knit sweater draping gracefully over high-waisted opaque black matte leggings with tail opening, cozy cream cable-knit knee socks, holding a steaming insulated tea mug and rugged DDM medical field notebook, relaxed loose chestnut waves past hips, quiet twilight safe-house kitchen nook background.
```

#### `AF-1` — Alyssa Fantasy Outfits 1–4 (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AF-1.png`
- **Pannelli (`--cols 4 --names silverhaven_field_medic,ocean_shadow_couture,silverhaven_cotton_nightgown,silverhaven_sunshine_foraging`):**

```text
4-panel horizontal 16:9 fantasy character outfit showcase strip featuring ONLY Alyssa (Silverhaven Fantasy Werewolf) matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, wavy caramel-chestnut hair, mint-green doe eyes, single caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel tail, Mannaz wrist rune, platinum navel ring) separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. PANEL 1 (Silverhaven A-Rank Field Medic Rig): Enchanted crisp white high-neck sleeveless dragon-weave dungeon tunic with flat mithril chest buckles, bare muscular toned arms, fitted white cargo expedition trousers with tail grommet, white leather alchemical waist belt stocked with glowing crystal healing potions and steel scalpel, fingerless white grip gloves, white leather laced mid-calf expedition boots, high compact ponytail, ancient mossy Silverhaven dungeon stone archway background. PANEL 2 (Ocean Shadow Couture by Angelo Moreno): Flowing enchanted silk haute-couture gown shifting chromatically from abyssal teal to emerald and liquid amethyst, custom-boned sweetheart bodice with metallic amethyst gossamer silk veil stole, prism teal-crystal clutch, midnight-blue laced gladiator heels, amethyst hairpins, grand enchanted Silverhaven crystal ballroom background. PANEL 3 (Silverhaven Cotton & Lace Nightgown): Breathable ankle-length flowing crisp white cotton and sangallo eyelet-lace nightgown with thin straps, soft romantic ruffled sweetheart neckline and flowing skirt with rear tail slit, completely barefaced and barefoot, cascading natural waves around sleepy wolf ears, candlelit Silverhaven timber inn bedroom background. PANEL 4 (Silverhaven Sunshine Foraging Tunic): Form-fitting pale-yellow cropped linen tunic showing platinum crescent navel ring above soft fawn-brown high-waisted fantasy breeches with tail slit, enchanted dimensional leather hip pouch, woven willow herb basket brimming with glowing wildflowers, tan suede ankle-boots, two small side braids in long waves, sunlit Silverhaven cobble herb market background.
```

#### `AF-2` — Alyssa Fantasy Outfits 5–7 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AF-2.png`
- **Pannelli (`--cols 3 --names royal_arcanum_robes,guild_banquet_honey_gold,mythal_thermal_swimwear`):**

```text
3-panel horizontal 16:9 fantasy character outfit showcase triptych featuring ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, wavy caramel-chestnut hair, mint-green doe eyes, single caramel wolf ears with black tips atop head, ZERO human ears, black-tipped caramel tail, Mannaz wrist rune) separated cleanly by crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (Royal Arcanum Crystallography Robes): Tailored ivory-white and gold-piped Royal Arcanum scholar bodice paired with high-waisted sage-green pleated skirt (tail slit), cross-body alchemical leather bandolier carrying glowing seven-layer quartz cylinders, moon-platinum ink vials, parchment scrolls, clutching a leather botanical grimoire, heeled cream Oxford ankle-boots, half-up braided crown framing wolf ears, sunlit floating crystal library hall background. CENTER PANEL (Guild Banquet Honey-Gold Dress): Enchanted warm honey-gold silk halter skater dress with plunging sweetheart neckline, open back, and tail cutout, sheer cream silk shawl draped loosely over elbows, embroidered velvet potion mini-pouch, burnished platinum heeled sandals, moonstone dangling ear-hoops and platinum moonflower clip, glowing tavern lantern festival courtyard background. RIGHT PANEL (Mythal Thermal Springs Swimwear): Tasteful editorial pale-yellow & pearl-white enchanted silk underwire halter two-piece swimwear paired with translucent gossamer white waist sarong, dainty flat white sandals, single thick over-shoulder braid, happy perked wolf ears, misty steaming turquoise enchanted thermal springs cavern background.
```

---

### Batch 3 — Elf & Human Variant Personas (`10` Griglie `16:9`)

#### `AE-1` — Alyssa Elf Fantasy Outfits 1–3 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AE-1.png`
- **Pannelli (`--cols 3 --names forest_nymph,traveler,elven_court`):**

```text
3-panel horizontal 16:9 fantasy outfit showcase triptych featuring Pureblood Forest Elf Alyssa preserving 1:1 her exact face, mint-green doe eyes, gentle cheek freckles, petite 155 cm DD-cup hourglass silhouette, and long wavy caramel-chestnut hair from alyssa_reference.png, BUT STRICTLY OVERRIDING HER SPECIES TO PUREBLOOD ELF: LONG POINTED ELVEN EARS PROTRUDING CLEANLY ON THE SIDES OF HER HEAD (STRICTLY ZERO WOLF EARS AND ZERO TAIL ON ALL 3 PANELS). Crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (Forest Nymph): Ethereal dress crafted entirely from living twisting green forest vines, overlapping fresh emerald leaves, tiny newly bloomed white moonflowers and yellow buds organically wrapping torso, hips, and forearms, barefoot on lush emerald forest moss, single white moonflower tucked beside her left pointed elven ear, sun-dappled primeval forest sanctuary background. CENTER PANEL (Traveler / Herbalist): Snug cream-and-sunflower-yellow laced linen elven bodice with delicate green botanical embroidery, warm brown travel trousers, soft draped sage-green travel cloak with crescent clasp, suede ankle travel boots, woven wicker basket full of fresh medicinal herbs & flowers, platinum elven ear-cuff on left pointed ear, sunlit woodland dirt road background. RIGHT PANEL (Elven Court): Flowing floor-length emerald-green and ivory silk court gown gilded with fine golden leaf filigree, sculpted sweetheart bodice, sheer bell sleeves, dark forest velvet waist pouch, ivory ribboned soft court slippers, delicate platinum & pearl cuffs hanging down both pointed elven ears, half-up braided crown waves, grand glowing ivory-marble elven palace pavilion background.
```

#### `AE-2` — Alyssa Elf Fantasy Outfits 4–6 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AE-2.png`
- **Pannelli (`--cols 3 --names solstice,sleep,forest_spring`):**

```text
3-panel horizontal 16:9 fantasy outfit showcase triptych featuring Pureblood Forest Elf Alyssa preserving 1:1 her exact face, mint-green doe eyes, cheek freckles, petite 155 cm DD-cup hourglass frame, and long wavy caramel-chestnut hair from alyssa_reference.png, WITH LONG POINTED ELVEN EARS ON SIDES (STRICTLY ZERO WOLF EARS AND ZERO TAIL ON ALL 3 PANELS). Crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (Solstice Festival): Breezy honey-gold lightweight silk dancing gown with sweetheart neckline, ruffled off-shoulder straps, flowing flared skirt, tiny embroidered floral waist satchel, golden flat ankle-lace sandals, woven crown of wild blooms & golden leaves resting above pointed elven ears, warm firefly-lit summer solstice glade festival background. CENTER PANEL (Sleep Nightgown): Pure white ankle-length breathable linen-and-cotton nightgown with thin straps, soft sangallo eyelet-lace ruffled sweetheart neckline, barefoot, barefaced relaxed expression, loose chestnut waves spilling cleanly past both pointed elven ears, soft moonlit wooden treehouse bedroom background. RIGHT PANEL (Forest Spring Swimwear): Tasteful editorial pearl-white lightweight silk two-piece swimwear trimmed neatly in pale sunlight yellow with translucent ivory sheer waist sarong draped loosely on hips, bare feet near natural rock pool edge, single smooth side braid revealing her long pointed elven ears clearly, misty glowing crystal waterfall spring lagoon background.
```

#### `AHM-1` — Alyssa Human Modern/Sci-Fi Outfits 1–3 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AHM-1.png`
- **Pannelli (`--cols 3 --names casual,formal,festa`):**

```text
3-panel horizontal 16:9 modern outfit showcase triptych featuring ORDINARY HUMAN Alyssa preserving 1:1 her exact face, mint-green eyes, freckles, petite 155 cm DD-cup hourglass figure, and long wavy caramel-chestnut hair from alyssa_reference.png, STRICTLY WITH ORDINARY HUMAN EARS AT THE SIDES OF HER HEAD (ZERO WOLF EARS AND ZERO TAIL ON ALL 3 PANELS). Crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (Casual): Fitted ribbed pastel-yellow crop top under a sleek open cropped black-and-white technical jacket, high-waisted matte black slim pants, clean white canvas low-top sneakers, minimalist sand crossbody bag, sleek wrist communicator, small sun pendant & navel ring, sunlit glass sci-fi transit concourse background. CENTER PANEL (Formal): Sharp tailored ivory single-button deep-V skirt-suit over pale mint-green silk blouse with matching high-waisted ivory pencil skirt, glossy ivory pointed heels, rigid ivory envelope clutch, delicate platinum pearl lobe hoops & matching pearl choker, clean side-parted waves, modern glass skyscraper conference gallery background. RIGHT PANEL (Festa): Flared mid-thigh honey-gold satin sweetheart cocktail dress, dainty silver chain clutch, sleek metallic strappy medium-heel sandals, shimmering drop lobe earrings, glowing golden eye shimmer, hair pinned cleanly on one side with crystal clip, glittering rooftop evening terrace party background.
```

#### `AHM-2` — Alyssa Human Modern/Sci-Fi Outfits 4–5 (`16:9`, 2 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AHM-2.png`
- **Pannelli (`--cols 2 --names sleep,beach`):**

```text
2-panel horizontal 16:9 outfit showcase diptych featuring ORDINARY HUMAN Alyssa preserving 1:1 her exact face, mint-green eyes, petite 155 cm DD-cup hourglass figure, and caramel-chestnut hair from alyssa_reference.png, STRICTLY WITH ORDINARY HUMAN EARS (ZERO WOLF EARS AND ZERO TAIL). Crisp 6px pure-black center divider bar, ZERO text, ZERO labels. LEFT PANEL (Sleep): Cozy oversized soft black combed-cotton sleep tee slipping effortlessly off one shoulder to mid-thigh over breathable cotton briefs, barefoot, clean fresh barefaced skin, messy high bun with soft loose nape locks, warm dim twilight apartment/habitat viewport background overlooking distant city lights. RIGHT PANEL (Beach): Tasteful editorial sunflower-yellow microfiber triangle two-piece bikini with short sheer white muslin waist pareo, flat minimalist beach sandals, delicate lobe hoops & platinum navel ring, sunglasses perched smoothly, effortless beachy chestnut waves, bright sunlit ocean resort boardwalk background.
```

#### `AHH-1` — Alyssa Human Historical/Fantasy Outfits 1–3 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AHH-1.png`
- **Pannelli (`--cols 3 --names casual,formal,festa`):**

```text
3-panel horizontal 16:9 historical fantasy outfit showcase triptych featuring ORDINARY HUMAN Alyssa preserving 1:1 her exact face, mint-green eyes, delicate freckles, petite 155 cm DD-cup hourglass silhouette, and caramel-chestnut hair from alyssa_reference.png, STRICTLY WITH ORDINARY HUMAN EARS AT THE SIDES OF HER HEAD (ZERO WOLF EARS AND ZERO TAIL ON ALL 3 PANELS). Crisp 6px pure-black divider bars, ZERO text, ZERO labels. LEFT PANEL (Casual): Fitted cream-and-sunflower-yellow linen laced bodice with dainty floral embroidery over warm chestnut travel skirt/trousers, suede belt with small leather hip pouch, natural tan suede flat ankle boots, two neat side braids tucked back, sunlit medieval cobbled village square background. CENTER PANEL (Formal): Floor-length draped sage-green and ivory silk-velvet historical court gown with structured boned bodice & fluid sleeves, gold-embroidered light silk shawl, velvet waist purse, ivory gold-buckled leather court flats, tiny pearl lobe earrings, half-up braided crown hair, candlelit noble stone great hall background. RIGHT PANEL (Festa): Honey-gold lightweight silk tavern/banquet gown with sweetheart neckline, flowing flared dancing skirt, small embroidered waist bag, laced flat soft leather ankle sandals, delicate floral clip securing lush curls, cheerful lantern-lit autumn harvest festival square background.
```

#### `AHH-2` — Alyssa Human Historical/Fantasy Outfits 4–5 (`16:9`, 2 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\AHH-2.png`
- **Pannelli (`--cols 2 --names sleep,beach`):**

```text
2-panel horizontal 16:9 historical fantasy outfit showcase diptych featuring ORDINARY HUMAN Alyssa preserving 1:1 her face, mint-green eyes, petite 155 cm DD-cup hourglass silhouette, and caramel-chestnut hair from alyssa_reference.png, STRICTLY WITH ORDINARY HUMAN EARS (ZERO WOLF EARS AND ZERO TAIL). Crisp 6px pure-black vertical center bar, ZERO text, ZERO labels. LEFT PANEL (Sleep): Ankle-length breathable pure white cotton historical nightgown with thin straps and delicate sangallo lace-trimmed sweetheart neckline, barefoot, barefaced, cozy loose braid over shoulder, soft lantern/moonlit rustic manor wooden bedroom background. RIGHT PANEL (Beach): Tasteful period pearl-white and pale-yellow linen/silk bathing shift & two-piece halter top with soft hip wrap and flowing white linen towel draped over shoulders, barefoot, neat single braid over shoulder, tranquil sunlit Mediterranean cliffside cove background.
```

#### `JHM-1` — Jasper Human Modern/Sci-Fi Outfits 1–3 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\JHM-1.png`
- **Pannelli (`--cols 3 --names casual,formal,festa`):**

```text
3-panel horizontal 16:9 modern outfit showcase triptych featuring ORDINARY HUMAN Jasper preserving 1:1 his exact face, sharp jawline, light stubble hint, vivid mint/emerald eyes, nose freckles, 193 cm lean athletic frame, and tousled caramel-chestnut wolf-cut hair from jasper_reference.png, STRICTLY WITH ORDINARY HUMAN EARS AT THE SIDES OF HIS HEAD (ZERO WOLF EARS AND ZERO TAIL ON ALL 3 PANELS). Crisp 6px pure-black divider bars, ZERO text, ZERO labels. LEFT PANEL (Casual): Oversized matte dark charcoal cotton hoodie over dark tee, black drawstring joggers, clean white-soled black canvas high-tops, matte-black & acid-green wireless headphones resting around neck, minimalist left-wrist smartwatch, twilight rainy futuristic neon rooftop street background. CENTER PANEL (Formal): Razor-sharp modern matte-black tailored suit with charcoal silk shirt unbuttoned at top two collar buttons, brushed platinum watch, black leather belt, glossy rounded-toe black Oxfords, cleanly styled hair with stray brow locks, sleek modern penthouses/gala lounge skyline background. RIGHT PANEL (Festa): Fitted matte-black leather and technical club jacket over dark charcoal V-neck tee & slim black jeans, thin platinum chain, dark timepiece, thick-soled high-top club sneakers, warm atmospheric neon lounge bar background.
```

#### `JHM-2` — Jasper Human Modern/Sci-Fi Outfits 4–5 (`16:9`, 2 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\JHM-2.png`
- **Pannelli (`--cols 2 --names sleep,beach`):**

```text
2-panel horizontal 16:9 outfit showcase diptych featuring ORDINARY HUMAN Jasper preserving 1:1 his face, sharp jaw, vivid mint/emerald eyes, 193 cm lean athletic swimmer build, and tousled caramel-chestnut hair from jasper_reference.png, STRICTLY WITH ORDINARY HUMAN EARS (ZERO WOLF EARS AND ZERO TAIL). Crisp 6px pure-black center divider bar, ZERO text, ZERO labels. LEFT PANEL (Sleep): Soft slate-grey unbuttoned henley long-sleeve tee paired with comfortable heather-grey cotton jersey sleep pants, barefoot, relaxed tousled bedtime hair, dim moonlit modern apartment bedroom background. RIGHT PANEL (Beach): Lean bare-chested swimmer torso draped lightly with a breezy unbuttoned pure white linen beach shirt over shoulders, matte-black athletic swim trunks, dark sunglasses hooked neatly at collar, barefoot/light sandals, breezy windswept chestnut locks, sunlit Pacific beach pier background.
```

#### `JHH-1` — Jasper Human Historical/Fantasy Outfits 1–3 (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\JHH-1.png`
- **Pannelli (`--cols 3 --names casual,formal,festa`):**

```text
3-panel horizontal 16:9 historical fantasy outfit showcase triptych featuring ORDINARY HUMAN Jasper preserving 1:1 his exact face, sharp jawline, light stubble, mint/emerald eyes, 193 cm lean agile frame, and tousled caramel-chestnut hair from jasper_reference.png, STRICTLY WITH ORDINARY HUMAN EARS AT THE SIDES OF HIS HEAD (ZERO WOLF EARS AND ZERO TAIL ON ALL 3 PANELS). Crisp 6px pure-black divider bars, ZERO text, ZERO labels. LEFT PANEL (Casual): Practical dark charcoal laced linen tunic beneath fitted dark-brown leather scout vest, hooded travel cloak pinned over one shoulder, sturdy dark trousers, tall dark-leather travel boots, worn leather messenger satchel & belt notebook pouch, atmospheric misty medieval forest road background. CENTER PANEL (Formal): Noble obsidian-black and dark forest-green tailored historical doublet jacket with upright collar and subtle silver-thread embroidery over fitted dark court trousers, silver-buckled black belt, polished soft black court ankle boots, platinum signet ring, grand candlelit gothic stone banquet hall background. RIGHT PANEL (Festa): Soft deep-burgundy and charcoal festival silk tunic laced open at collar with sleeves rolled neatly to mid-forearm, comfy dark trousers, hip pouch, dark leather ankle boots, braided leather-and-silver wrist cuff, warm golden lantern-lit medieval tavern courtyard background.
```

#### `JHH-2` — Jasper Human Historical/Fantasy Outfits 4–5 (`16:9`, 2 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\JHH-2.png`
- **Pannelli (`--cols 2 --names sleep,beach`):**

```text
2-panel horizontal 16:9 historical fantasy outfit showcase diptych featuring ORDINARY HUMAN Jasper preserving 1:1 his face, mint/emerald eyes, 193 cm lean agile build, and caramel-chestnut hair from jasper_reference.png, STRICTLY WITH ORDINARY HUMAN EARS (ZERO WOLF EARS AND ZERO TAIL). Crisp 6px pure-black vertical center bar, ZERO text, ZERO labels. LEFT PANEL (Sleep): Loose unlaced cream-white soft linen nightshirt open slightly at chest with comfortable raw natural-cotton trousers, barefoot, deeply relaxed tousled hair, warm moonlit/candlelit wooden manor chamber background. RIGHT PANEL (Beach): Simple dark-linen drawstring swim shorts paired with a light pale linen towel slung casually over one bare tanned shoulder showing lean sculpted torso, barefoot, damp tousled hair, peaceful sunlit ancient stone cove hot-spring background.
```

---

## FIX — Rigenerazione Mirata `10` Pannelli Licantropi (Orecchie Umane Rilevate)

> **Perché servono queste 3 griglie:** su `10` pannelli del Batch 1 (`7` di Alyssa e `3` di Jasper) Gemini Pro ha generato piccole orecchie umane/auricolari/orecchini ai lati delle tempie invece di lasciare esclusivamente le orecchie lupine sulla sommità del capo. Questi `3` prompt blindano le tempie coprendole naturalmente con ciocche di capelli morbide su entrambi i lati e spostano tutti gli orecchini/cerchietti esclusivamente sui bordi delle orecchie da lupo.

#### `FIX-A1` — Alyssa Batch 1 Fix `1/2` (`16:9`, 4 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\FIX-A1.png`
- **Pannelli (`--cols 4 --names succ_track_sparring,douglas_crescent_gown,succ_healer_lab_coat,logans_garage_biker`):**

```text
4-panel horizontal 16:9 character outfit showcase strip featuring ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, mint-green doe eyes, delicate nose freckles, single pair of caramel wolf ears with black tips atop her head, bushy black-tipped caramel wolf tail, Mannaz left wrist rune). CRITICAL ANATOMY OVERRIDE ACROSS ALL 4 PANELS: STRICTLY ZERO HUMAN EARS ON THE SIDES OF HER HEAD — wear rich soft loose caramel face-framing curtain locks flowing cleanly down across BOTH temples and cheeks all the way past the jawline so the sides of her head are 100% smoothly covered by hair, with STRICTLY ZERO earbuds, ZERO ear-cuffs, and ZERO earrings on the human ear area; ALL platinum/pearl hoops and studs belong EXCLUSIVELY on her upright caramel wolf ears atop her skull. Crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. PANEL 1 (SUCC Track & Pack Sparring Gear): Sunflower-yellow compressive sports-bra crop top, unzipped navy-blue windbreaker track jacket with yellow reflective piping, high-waisted navy-blue lycra biker shorts with tail eyelet, navy wrist sweatbands, white/neon-yellow cushioned running sneakers, high bouncy ponytail WITH thick loose soft caramel curtain-bang locks covering both temples smoothly (NO earbuds anywhere), sunlit forest track trail background. PANEL 2 (Douglas House Crescent Reception Gown): Tailored ivory crepe single-button deep-V blazer worn over pale mint-green silk blouse, ivory mini pencil skirt with rear tail slit, glossy ivory 10cm pointed pumps, rigid ivory clutch, pearl choker, vintage Hollywood glossy caramel waves flowing forward cleanly over BOTH temples down past her cheeks with pearl-and-platinum drops hanging EXCLUSIVELY from her upright wolf ears atop her head, grand sunlit Villa Douglas marble salon background. PANEL 3 (SUCC Healer Clinic & Lab Coat): Crisp spotless white medical lab coat with rolled sleeves open over white sleeveless boat-neck top, opaque black three-quarter capri leggings with tail slit, black stethoscope around neck, photo clinic badge, low black canvas Converse sneakers, high ponytail paired with long thick soft caramel side-curtain locks completely covering both temples to jawline, clean bright clinic office background. PANEL 4 (Logan's Garage & Highway Ride): Glossy heavy black leather biker jacket open over strapless sunflower-yellow bandeau tube top, quilted-knee black leather riding pants with tail slot, black leather choker collar, fingerless padded motorcycle gloves, matte black helmet tucked under arm, mid-shin buckled biker boots, thick back fishtail braid WITH generous loose caramel curtain strands covering BOTH temples cleanly (zero side ears), warm neon-lit motorcycle workshop garage background.
```

#### `FIX-A2` — Alyssa Batch 1 Fix `2/2` (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\FIX-A2.png`
- **Pannelli (`--cols 3 --names villa_douglas_hearth,angelo_moreno_couture,blackwood_pilates`):**

```text
3-panel horizontal 16:9 character outfit showcase triptych featuring ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, mint-green doe eyes, soft freckles, single pair of caramel wolf ears with black tips atop her head, bushy black-tipped caramel wolf tail, Mannaz left wrist rune). CRITICAL ANATOMY OVERRIDE ACROSS ALL 3 PANELS: STRICTLY ZERO HUMAN EARS ON THE SIDES OF HER HEAD — style rich thick soft caramel face-framing hair locks cascading smoothly down across BOTH temples and cheeks past the jaw on all 3 panels so the sides of her head remain 100% smoothly covered by hair, with ZERO jewelry anywhere along cheeks/jawline; ALL sapphire, diamond, or crystal earrings belong EXCLUSIVELY dangling from the tips/edges of her upright wolf ears atop her head. Crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (Villa Douglas Family Hearth Dinner): Floor-length deep ultramarine midnight-blue silk satin mermaid gown with draped cowl neckline, delicate jeweled micro-straps, rear tail drape, sheer sequined midnight-blue chiffon stole over elbows, hammered platinum clutch, sapphire-and-white-gold teardrop necklace, soft low French chignon WITH rich billowing curved caramel side locks completely draping over BOTH temples while sapphire-and-diamond drops dangle EXCLUSIVELY from her upright wolf ears, blazing stone fireplace dining hall background. CENTER PANEL (Angelo Moreno Couture "Ocean Shadow"): Exclusive haute-couture fluid iridescent gown shifting chromatically from abyssal teal-blue to emerald & amethyst light, geometric sweetheart corset bodice, ethereal metallic amethyst floor-length silk veil cuffs, chromed gladiator heels, glossy liquid caramel waves sweeping forward cleanly over BOTH temples on both sides with crystal/amethyst hairpins beside wolf ears wearing titanium ear-cuffs atop her head, dramatic dark runway spotlight backdrop. RIGHT PANEL (Blackwood Studio Pilates & Stretch): Supportive crisp optic-white athletic sports crop bra with sunny yellow contrast trim over high-waisted optic-white full-length compression leggings with yellow-piped tail slot, barefoot holding rolled yellow yoga mat and white towel, high messy bun with yellow scrunchie AND thick soft caramel face-framing curtain locks covering BOTH temples seamlessly down to chin, bright sunlit hardwood Pilates studio & mirror background.
```

#### `FIX-J1` — Jasper Batch 1 Fix (`16:9`, 3 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\FIX-J1.png`
- **Pannelli (`--cols 3 --names campus,formal_gala,sleepwear`):**

```text
3-panel horizontal 16:9 character outfit showcase triptych featuring ONLY the male werewolf Jasper matching jasper_reference.png strictly 1:1 (193 cm lean athletic frame, sharp jawline, vivid mint-green eyes, nose freckles, SINGLE PAIR OF CARAMEL WOLF EARS WITH BLACK TIPS atop his head, bushy black-tipped caramel wolf tail, Mannaz left wrist rune, platinum Douglas signet ring). CRITICAL ANATOMY OVERRIDE ACROSS ALL 3 PANELS: STRICTLY ZERO HUMAN EARS ON THE SIDES OF HIS HEAD — keep thick layered shaggy caramel-chestnut wolf-cut locks sweeping full and dense over BOTH temples down to mid-neck/jawline covering the sides of his head 100%, with STRICTLY ZERO earbuds, ZERO earhooks, and NO hand near head pushing hair behind an ear. Crisp 6px pure-black vertical divider bars, ZERO text, ZERO labels. LEFT PANEL (Campus): Charcoal crewneck tee with faded tech logo, relaxed smoke-grey tactical cargo pants with tail hole, grey/black suede skate shoes, black cordura messenger bag slung across chest, left-wrist smartwatch, extra-thick shaggy caramel wolf-cut side locks covering BOTH temples 100% smoothly (NO earbuds in side temples, zero human ears), sunlit modern SUCC glass campus courtyard background. CENTER PANEL (Formal / Gala): Sharp two-piece tailored dark charcoal wool suit worn open over unbuttoned crisp white poplin dress shirt (no tie, platinum Douglas cufflinks), straight dark wool trousers with rear tail slot, polished black leather Oxfords, full swept-back top hair KEEPING thick natural wolf-cut side layers smoothly covering BOTH temples (STRICTLY zero slicked-back temples exposing human ears; platinum hoops ONLY on left upright wolf ear), warm candlelit Villa Douglas grand ballroom background. RIGHT PANEL (Sleepwear): Oversized faded heather-grey vintage rock concert t-shirt and loose black cotton jersey sleep shorts with tail gap, barefoot, BOTH HANDS RELAXED DOWN AT HIS SIDES / IN SLEEP POCKETS (do NOT touch head), sleepy relaxed shaggy wolf-cut hair completely covering BOTH temples smoothly with softened wolf ears atop head, soft dim moonlit bedroom background.
```

#### `FIX-J2` — Jasper Shared Shifter Forms: Svartr Obsidian Black Sun Hybrid & Full Shift (`16:9`, 2 Pannelli)
*(Valido identicamente per Jasper Modern, Jasper DDM #08 e Jasper Fantasy!)*
- **Reference:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\FIX-J2.png`
- **Pannelli (`--cols 2 --names hybrid_shift,full_shift`):**

```text
2-panel horizontal 16:9 creature-form showcase diptych depicting the TWO canonical Black Sun wolf shift forms of Jasper ("Svartr, The Black Sun Wolf" / "Sólúlfr") matching jasper_reference.png 1:1 in lean agile athletic proportions and cohesive semi-realistic digital painting style, separated cleanly by a crisp 6px pure-black vertical center bar, ZERO text, ZERO labels, ZERO overlap. LEFT PANEL (Svartr Biped Hybrid Shift — 223 cm): Unclothed lean, powerfully athletic fast-twitch 223 cm biped werewolf predator completely covered in dense silky OBSIDIAN JET-BLACK FUR across his entire body (ZERO white markings anywhere), lush midnight-black mane with subtle warm solar-obsidian rim sheen running from nape down spine, elongated fierce obsidian-black lupine muzzle with stark white fangs and BLAZING MOLTEN-GOLD PREDATOR EYES, single pair of tall upright obsidian-black wolf ears atop skull (STRICTLY ZERO human ears on sides of head), long bushy jet-black wolf tail, digitigrade hind wolf paws with black pads and sharp OBSIDIAN-BLACK CLAWS VEINED WITH GOLD, subtle glowing golden solar-runic Mannaz pulse gleaming faintly through black fur on left forearm, dramatic rocky twilight cliff with dark solar-eclipse sky background. RIGHT PANEL (Svartr Black Sun Quadruped Dire Wolf — Full Shift): Dynamic prowling quadruped giant dire wolf stance, sleek rangy muscular build covered 100% in glossy OBSIDIAN JET-BLACK FUR with a thick midnight-black neck mane catching subtle warm golden-solar rim highlights, BLAZING MOLTEN-GOLD EYES, sharp OBSIDIAN-BLACK CLAWS VEINED WITH GOLD, stark white fangs, entirely devoid of white coat markings, single pair of tall upright black wolf ears, misty dark volcanic pine forest ridge under a dramatic eclipsed sun and moon twilight sky background.
```

#### `FIX-A3` — Alyssa Batch 2 Earring/Ear Audit Fix (`16:9`, 2 Pannelli)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\FIX-A3.png`
- **Pannelli (`--cols 2 --names douglas_crescent_gown,guild_banquet_honey_gold`):**
  *(Nota: `douglas_crescent_gown` va in `assets/Alyssa/outfits/` per Alyssa Modern; `guild_banquet_honey_gold` va in `assets/Alyssa/outfits_fantasy/` per Alyssa Fantasy.)*

```text
2-panel horizontal 16:9 character outfit showcase diptych featuring ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, mint-green doe eyes, delicate freckles, single pair of caramel wolf ears with black tips atop her head, bushy black-tipped caramel wolf tail, Mannaz left wrist rune). CRITICAL ANATOMY OVERRIDE ON BOTH PANELS: STRICTLY ZERO HUMAN EARS AND STRICTLY ZERO EARRINGS, PEARL DROPS, OR DANGLING JEWELRY ANYWHERE ALONG THE SIDES OF HER FACE, TEMPLES, CHEEKS, OR JAWLINE — style thick rich wavy caramel hair cascading smoothly forward over BOTH temples down past her jawline so the sides of her head remain 100% covered; tiny pearl/platinum/moonflower hair clips belong EXCLUSIVELY on her upright wolf ears atop her skull (NO dangling side-head jewelry). Crisp 6px pure-black center vertical divider bar, ZERO text, ZERO labels. LEFT PANEL (Douglas House Crescent Reception Gown — Modern): Tailored ivory crepe deep-V single-button blazer worn open over pale mint-green silk blouse, ivory mini pencil skirt with rear tail slit, glossy ivory 10cm pointed pumps, rigid ivory clutch, pearl necklace choker on neck ONLY (NO side-head earrings), rich voluminous Hollywood caramel waves covering BOTH temples smoothly down to collarbone, grand sunlit Villa Douglas marble salon background. RIGHT PANEL (Guild Banquet Honey-Gold Dress — Silverhaven Fantasy): Enchanted warm honey-gold silk halter skater dress with sweetheart neckline and tail cutout, sheer cream silk shawl draped loosely over elbows, embroidered velvet potion mini-pouch, burnished platinum heeled sandals, dainty white moonflower hairpin tucked beside her upright wolf ear atop skull (STRICTLY ZERO hanging earrings near cheeks or temples), glowing medieval tavern lantern festival courtyard background.
```

#### `FIX-A4` — Alyssa `villa_douglas_hearth` Fix Singolo (`2:3`, Zero Orecchini / Zero Pendenti)
- **Reference:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png`
- **Salva:** `E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\FIX-A4.png`
- **Output finale:** `E:\repository\SvartulfrVerse\assets\Alyssa\outfits\villa_douglas_hearth.png`

```text
Full-body 2:3 vertical character illustration of ONLY Alyssa matching alyssa_reference.png strictly 1:1 (155 cm petite curvy DD-cup hourglass frame, mint-green doe eyes, soft freckles, single pair of caramel wolf ears with black tips atop her head, bushy black-tipped caramel wolf tail, Mannaz left wrist rune) in semi-realistic digital painting style. CRITICAL ANATOMY OVERRIDE: STRICTLY ZERO HUMAN EARS ON THE SIDES OF HER HEAD, AND WEAR ABSOLUTELY ZERO EARRINGS OR DANGLING JEWELRY ANYWHERE (NOT on cheeks, NOT on jawline, NOT on wolf ears) — her rich thick billowing caramel-chestnut waves cascade smoothly forward over BOTH temples all the way down below her shoulders so the sides of her head remain 100% smoothly covered by hair, with ONLY a sapphire-and-white-gold teardrop necklace resting on her collarbone. OUTFIT (Villa Douglas Family Hearth Dinner): Floor-length deep ultramarine midnight-blue silk satin mermaid evening gown with draped cowl neckline, delicate jeweled micro-straps, bespoke rear tail drape letting her caramel wolf tail fall behind her, sheer sequined midnight-blue chiffon stole draped loosely over elbows, hammered platinum evening clutch held in hands, soft low French chignon at back with rich wavy side-curtain locks over both temples, set inside a grand warm blazing stone fireplace Villa Douglas dining hall background with candlelight bokeh, zero text, zero borders.
```

---

## Nota Operativa: Slot Esclusi (9 Nude / Anatomical) & Comandi Rapidi di Taglio

- **Slot `Nude / Anatomical` esclusi dai prompt Gemini Pro (`9` in totale):**
  1. `Alyssa Modern` — `Nudo Anatomico Mániúlfr (White Moon)` *(ha già un vecchio asset CDN)*
  2. `Alyssa DDM #07` — `Nudo Anatomico (#07 Alyssa DDM)` *(ha già un vecchio asset CDN)*
  3. `Alyssa Fantasy` — `Nudo Anatomico Mániúlfr (Silverhaven)` *(ha già un vecchio asset CDN)*
  4. `Alyssa Elf Fantasy` — `Nude` *(senza immagine)*
  5. `Alyssa Human Modern/Sci-Fi` — `Nude` *(senza immagine)*
  6. `Alyssa Human Historical/Fantasy` — `Nude` *(senza immagine)*
  7. `Jasper Modern` — `Nude` *(senza immagine)*
  8. `Jasper Human Modern/Sci-Fi` — `Nude` *(senza immagine)*
  9. `Jasper Human Historical/Fantasy` — `Nude` *(senza immagine)*
- Questi `9` slot non vengono inclusi per evitare blocchi di policy su Gemini Pro; i vecchi asset di Alyssa restano invariati finché non deciderai se sostituirli con generatori locali o tenerli come fallback.

### Esempio Rapido di Taglio Automatico (`slice-outfit-grid --mode panels`)
Una volta salvati i file in `scratch/persona_grids/`, il taglio automatico rimuove ogni barra verticale divisoria al pixel:

```powershell
# Esempio Avatar Dinamici Alyssa Trio (AV-A1)
python E:\repository\SvartulfrVerse\scripts\asset_reference_pipeline.py slice-outfit-grid `
  --src E:\repository\SvartulfrVerse\scratch\persona_grids\avatars\AV-A1.png `
  --cols 3 --names alyssa_modern_avatar,alyssa_ddm_avatar,alyssa_fantasy_avatar `
  --out-dir E:\repository\SvartulfrVerse\assets\Alyssa\avatars

# Esempio Griglia Outfit Jasper (J-1)
python E:\repository\SvartulfrVerse\scripts\asset_reference_pipeline.py slice-outfit-grid `
  --src E:\repository\SvartulfrVerse\scratch\persona_grids\outfits\J-1.png `
  --cols 4 --names casual_home,campus,tactical_guild,abyssal_armor `
  --out-dir E:\repository\SvartulfrVerse\assets\Jasper\outfits
```
