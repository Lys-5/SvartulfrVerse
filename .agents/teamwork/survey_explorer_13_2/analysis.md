# Full Survey & Design Specification for R2: Runic & Divine Marks References & Visuals

**Agent**: `survey_explorer_13_2`  
**Date**: 2026-10-31  
**Target Milestone**: R2 — Runic & Divine Marks References & Visuals  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\survey_explorer_13_2\`

---

## 1. Executive Summary & Problem Boundary

This investigation provides a comprehensive survey, canonical lore inventory, and visual design specification for **Requirement R2** of the Svartúlfr Verse:
> "Progettare e generare le immagini di reference e i prompt per i marchi runici e divini del branco, salvando i file immagine generati e le specifiche documentali in una cartella dedicata del repository (es. `assets/references/` o `docs/references/`):
> - Tatuaggio Gebo al polso sinistro dei gemelli (inchiostro di ferro freddo)
> - Marchio runico di Máni (mezzaluna argentata con glifi lunari sub-dermici) unicamente sull'anca sinistra di Alyssa (Hvít Mániúlfr)
> - Marchio runico di Sól (sole nero radioso con glifi fiammeggianti sub-dermici) unicamente sull'anca destra di Jasper (Svartr Sólúlfr)
> - Marchi e tatuaggi degli altri membri del branco come Logan, Malachia, Erik, Wulfnic"

### Core Findings:
1. **Divine Marks Invariant**: The sacred celestial marks of the twins are **strictly localized to the hips**:
   - Alyssa: **Left Hip** (Marchio Runico di Máni — silver crescent moon with sub-dermal lunar glyphs).
   - Jasper: **Right Hip** (Marchio Runico di Sól — radiant black sun with sub-dermal flaming glyphs).
   - Legacy drafts describing celestial marks on hands, chest, neck, collarbone, or wings on the back are **categorically prohibited and purged** per `GEMINI.md` §5, `03_outfits_e_coerenza_visiva.md`, and `CHANGELOG.md` lines 24–32.
2. **The Only Shared Tattoo**: The **Gebo rune tattoo** on the **left wrist** is the **sole shared tattoo** between the twins, inscribed during the 5th-day post-partum rite using serpent tooth and cold iron ink (`inchiostro di ferro freddo`).
3. **Cosmic Titles Canon**:
   - **Sólúlfr** (Sun Wolf) belongs **exclusively to Svartr (Jasper)**.
   - For **Hvít (Alyssa)**, the divine title is **Mániúlfr** (Maniulf / White Moon Wolf).
4. **Pack Marks Spectrum**:
   - Logan: Full sleeves on both arms (Norse/Celtic knotwork, hunt tales) + `Eihwaz` + Rune of Fenris protection brand on left wrist.
   - Malachia: Extensive Norse/tribal warrior blackwork across arms and climbing up the neck + `Thurisaz` + Rune of Fenris protection brand on left wrist + duel scars.
   - Erik: Faint ritual hunt scar on left cheekbone + `Tiwaz` / `Hagalaz` + Rune of Fenris on left wrist + clan signet ring.
   - Wulfnic: Ancient 9th-century primeval Viking brands and battle scars spanning 1200 years across colossal torso/arms + `Othala`/`Jera` Fenris blood-oath on wrist + stolen eye of Odin.
5. **Asset Repository Structure**:
   - Recommended specs path: `docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md`
   - Recommended image assets path: `asset/references/` (harmonizing with existing `asset/NEW_IMAGE/` and `asset/PROMPTS_...md`), with a cross-directory symlink/alias or documentation pointer in `assets/references/`.

---

## 2. Canonical Lore & Theological Foundations

### 2.1 The 5th Day Lycanthrope Birth-Rune Ritual (`Lycanthrope Birth-Rune Ritual`)
As documented in `FINAL/Svartulfr_Lorebook_I.json` (Entry `_ryRgj7b33yXNeN14WBfDJ` / line 9135) and `CHANGELOG.md` line 990:

```text
"Il rito della Runa di Nascita (Birth-Rune) e una delle pratiche cerimoniali piu intoccabili della tradizione licantropica. 
Esattamente il quinto giorno dopo la nascita del neonato, il patriarca o l'anziano del branco celebra l'incisione della runa 
dell'antico Futhark che ne dichiara l'essenza spirituale, il temperamento e il vincolo col destino.

Il rituale esige rigorosamente tre elementi arcaici:
- L'Ago Sacro: L'incisione viene effettuata unicamente utilizzando un autentico dente di serpente, simbolo di saggezza velenosa, mutamento e precisione.
- L'Inchiostro del Vincolo: L'inchiostro viene preparato miscelando carbone di legna sacra purificata con polvere finissima di ferro freddo (cold iron). 
  La presenza del cold iron e fondamentale: ancorando l'inchiostro nella carne, sigilla la risonanza magica della runa e funge da barriera 
  indelebile contro interferenze demoniache, corruzioni astrali e incantesimi di possessione mentale.
- La Sede: La runa viene sempre incisa all'interno del polso (tradizionalmente il sinistro, il lato del cuore e della guardia in combattimento), 
  lasciando una caratteristica cicatrice scura cerimoniale."
```

### 2.2 The Prophecy of the Twin Wolves (`LSE: La Profezia dei Lupi Gemelli`)
From `FINAL/Svartulfr_Lorebook_I.json` (lines 9428–9429) and `scripts/apply_hip_marks_and_maniulf.py`:

```text
"Tha er tungl ok sol risa saman i dreyra,
mun old hinna Fyrstu lida undir lok,
ok Vigit mun verda Konungr
eptir eitt hundrad ok fimm tigi vetra."

(Traduzione: "Quando la luna e il sole sorgeranno insieme nel sangue, l'era dei Primi giungera alla fine, e il Bastione diverra Re dopo centocinquanta inverni.")
```

- **Svartr Sólúlfr (Jasper)**: The Black Sun Wolf, solar incarnation of Sköll, bearer of the exclusive title **Sólúlfr**.
- **Hvít Mániúlfr (Alyssa)**: The White Moon Wolf, lunar daughter of Máni and Hati, bearer of the divine title **Mániúlfr**.
- Born simultaneously on April 22, 2005 in the dying blood of their mother Nixara Bloodmoon (3rd White Moon).

---

## 3. Detailed Character Marks Inventory & Invariants

| Character | Divine / Cosmic Mark | Birth Rune & Location | Additional Tattoos & Body Art | Scars, Brands & Relics | Invariant Constraints |
|:---|:---|:---|:---|:---|:---|
| **Alyssa Hvit Douglas Bloodmoon** | **Marchio di Máni**: Silver crescent moon with sub-dermal glowing lunar glyphs **strictly on LEFT HIP**. | **Gebo** (`ᚷ`) on **inner left wrist** (serpent tooth & cold iron ink). | None on upper body. Shared Gebo on left wrist with Jasper. | None. Pierced navel (silver crescent moon charm), ear cartilage hoops, Douglas silver signet ring. | **ZERO marks on hands, chest, neck, collarbone or heart**. No angel wings on back. Title strictly **Mániúlfr**. |
| **Jasper Svartr Douglas Bloodmoon** | **Marchio di Sól**: Radiant Black Sun of Sköll with sub-dermal dark-gold flaming glyphs **strictly on RIGHT HIP**. | **Gebo** (`ᚷ`) on **inner left wrist** (serpent tooth & cold iron ink). | Nordic `Gebo` + `Mannaz` runic patterns along forearms/wrist with subtle glowing cyan accents (technomancy). | Arcane neural socket at base of neck; silver nipple rings; cartilage rings on wolf ears; Douglas signet ring. | **ZERO marks on chest, neck, hands or collarbone** (Moon Aegis purged). Title strictly **Sólúlfr**. |
| **Logan Járn Douglas** | None (Beta lineage). | **Eihwaz** (`ᛇ`) on **inner left wrist** (serpent tooth & cold iron ink). | Full sleeve tattoos on both arms (Norse knotwork, pack stories, Celtic serpents). | Magical protection brand (**Eihwaz + Rune of Fenris**) on left wrist; crisscrossing hunt scars; weathered biker hands. | Sleeves hidden under long jackets/flannel, revealed when pushed up. |
| **Malachia Björn Douglas Bloodmoon** | None (Ascendant Enigma potential). | **Thurisaz** (`ᚦ`) on **inner left wrist** (serpent tooth & cold iron ink). | Extensive Norse/tribal warrior blackwork covering both arms and climbing up the sides of his neck (Bloodmoon tradition). | Sacred protection brand (**Thurisaz + Rune of Fenris**) on left wrist; broken boxer nose; left eyebrow scar; fur scars in shift. | No jewelry/accessories. Hands wrapped only during training/fights. |
| **Erik Ulfr Douglas** | None (Pureblood Prime Alpha). | **Tiwaz** (`ᛏ`) / **Hagalaz** (`ᚺ`) on **inner left wrist** (serpent tooth & cold iron ink). | Discreet wrist protection brand (**Hagalaz + Rune of Fenris**) on left wrist. | Faint ritual cheek scar on left cheekbone (hunt at 16); Douglas silver/obsidian signet ring; gold necklace (Nixara memorial). | Elegant, corporate restraint. Tattoos concealed under bespoke cuffs. |
| **Wulfnic Báleygr Bloodmoon** | **First Fang / Living Saga**: Divine bloodline primeval aura. | **Othala** (`ᛟ`) / **Jera** (`ᛃ`) on **left wrist** (864 AD primeval inscription). | Ancient 9th-century Viking Svartúlfr tattoos carved across shoulders, chest, and arms. | 1,200 years of battle scars across colossal torso; Stolen Eye of Odin; Firstborn tooth pendant; wolf-pelt mantle. | Completely ignores modern clothing; archaic Viking demigod aesthetics. |
| **Noah Loki Douglas Bloodmoon** | None (Delta diplomat). | **Kenaz** (`ᚲ`) on **inner left wrist** (serpent tooth & cold iron ink). | Minimal to none; pristine sun-tanned skin fitting his corporate/diplomatic public profile. | None. Impeccably groomed, designer sunglasses, luxury signet ring. | Zero aggressive warrior ink; clean aristocratic aesthetic. |
| **Edric Douglas** | None (Gamma pup, 13yo). | **Ingwaz** (`ᛜ`) on **inner left wrist** (serpent tooth & cold iron ink). | None. | Awaiting solemn Presentation ceremony at Yule (Dec 21, 2024). | Minor background NPC rating. Zero body art beyond birth rune. |

---

## 4. Visual Reference Design & Generation Architecture

### 4.1 Recommended Directory Layout
Following analysis of the existing workspace structure (`asset/`, `docs/`, `FINAL/`):
- **Documentation & Design Specs**:
  `docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md`
- **Visual Image Assets**:
  `asset/references/` (or mirrored to `assets/references/` for compatibility):
  ```text
  asset/references/
  ├── mark_01_gebo_wrist_twins.png          # Macro isolated close-up of Gebo cold iron wrist tattoo
  ├── mark_02_mani_hip_alyssa.png           # Macro isolated reference of Máni crescent on Alyssa's left hip
  ├── mark_03_sol_hip_jasper.png            # Macro isolated reference of Sól radiant sun on Jasper's right hip
  ├── mark_04_twins_celestial_polarity.png  # Paired visual showing Left Hip (Máni) & Right Hip (Sól) polarity
  ├── mark_05_logan_sleeves_and_eihwaz.png  # Logan's Norse biker sleeve & wrist talisman
  ├── mark_06_malachia_neck_and_thurisaz.png# Malachia's aggressive warrior blackwork & neck markings
  ├── mark_07_erik_ritual_scar_and_tiwaz.png# Erik's cheekbone scar & executive wrist seal
  └── mark_08_wulfnic_primordial_saga.png   # Wulfnic's archaic Viking torso brands & weathered battle scars
  ```

### 4.2 Aesthetic & Technical Invariants for Generation
1. **Art Style**: `MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, ANIME-INSPIRED REALISM, DARK MODERN FANTASY`.
2. **Cold Iron Ink Shader (`Inchiostro di Ferro Freddo`)**:
   - Deep, matte charcoal-black base mixed with ultra-fine metallic dark iron flecks that catch grazing light with a gunmetal sheen.
   - Distinct, slightly raised ceremonial keloid/scar line along the staves representing the serpent's tooth incision.
3. **Sub-Dermal Bioluminescence**:
   - **Máni (Alyssa)**: Pearlescent, moonlight-silver glow (`#E2E8F0` to `#FFFFFF` with iridescent lavender-blue edge), softly diffusing from beneath translucent fair skin.
   - **Sól (Jasper)**: Dark solar flame, glowing molten amber-gold (`#F59E0B` to `#D97706` with subtle dark-core radiation and cyan technomantic circuit traces).
4. **Anatomical Strictness**:
   - Demi-human anatomy: Single pair of lupine ears only, zero human ears (`SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS`).
   - Alyssa: 155 cm, voluptuous hourglass, mark strictly on LEFT HIP.
   - Jasper: 193 cm, athletic gamer/DJ build, mark strictly on RIGHT HIP.
   - Left wrist for Gebo: Volar wrist (inner flexor side), never on outer forearm or back of hand.

---

## 5. Master Prompt Blueprints for R2 Generation

### Blueprint 1: Gebo Rune Tattoo on Left Wrist (Twins Alyssa & Jasper Shared Bond)
```text
[MASTER STYLE PREFIX]
MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, PREMIUM ANATOMICAL REFERENCE SHEET, MACRO CLOSE-UP PHOTOGRAPHY, DARK URBAN FANTASY, CINEMATIC GRAZING LIGHT.

SUBJECT: Macro detailed focus on the inner flexor surface of a slender, graceful werewolf wrist (volar wrist). 
THE SACRED MARK: The Gebo Rune ("ᚷ") tattooed with archaic precision. The linework is executed in dark cold iron ink (deep charcoal-black with a subtle metallic gunmetal sheen and fine iron-particle texture). The edges of the rune staves show a faint, delicate raised ceremonial scar line, healed from an ancient serpent-tooth incision.
MAGIC RESONANCE: A faint, ethereal, dual-toned sub-dermal luminescence gently halos the staves (soft pearlescent moonlight-silver on one side, faint glowing cyan-gold on the other), symbolizing an unbreakable empathic twin bond.
COMPOSITION & DETAILS: Tight macro composition focusing on the wrist crease, smooth skin texture, soft radial pulse point, subtle skin pores, beautiful linework craftsmanship. Clean dark studio background with warm cinematic side rim light catching the cold iron texture.

NEGATIVE PROMPT: deformed hand, extra fingers, malformed fingers, double wrists, colorful anime tattoos, blurry linework, washed out, watercolor splash, messy ink, grimdark gore, infection, open wound, text, watermarks, signature.
```

---

### Blueprint 2: Divine Runic Mark of Máni (Alyssa Hvit — Strictly Left Hip)
```text
[MASTER STYLE PREFIX]
MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, LUXURY VISUAL STORYTELLING, LUMINOUS MOONLIGHT AESTHETIC, HIGHLY DETAILED ANATOMY.

SUBJECT: Close-up anatomical reference focusing on the left hip and waist curve of a young werewolf woman with porcelain, flawless fair skin.
THE SACRED MARK: The Divine Runic Mark of Máni (The White Moon) located STRICTLY ON THE LEFT HIP (iliac crest sweeping down the upper pelvic curve). 
DESIGN DETAILS: An elegant, sacred crescent moon curve facing outward, woven seamlessly with delicate Elder Futhark lunar glyphs and sacred celestial geometry. The mark appears as an iridescent, pearlescent silver-white birthmark etched beneath the epidermis. 
BIOLUMINESCENCE: When awakened, the inner lunar glyphs softly pulsate with liquid silvery-white moonlight radiance, casting a gentle, ethereal glow across the hip and lower abdomen. 
SURROUNDING DETAILS: Soft caramel wolf tail tip visible at the lower edge of the frame, flawless skin texture, gentle anatomical curves, zero marks on hands, chest, neck or collarbone.
LIGHTING: Moody nighttime setting bathed in gentle silver moonlight and warm ambient candle glow.

NEGATIVE PROMPT: mark on right hip, marks on chest, marks on neck, collarbone tattoo, angel wings, human ears, deformed anatomy, harsh shadows, dirty skin, aggressive scars, text, watermark.
```

---

### Blueprint 3: Divine Runic Mark of Sól (Jasper Svartr — Strictly Right Hip)
```text
[MASTER STYLE PREFIX]
MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, DARK CYBER-ARCANE AESTHETIC, UNDERGROUND NEON LIGHTING, HIGHLY DETAILED ANATOMY.

SUBJECT: Close-up anatomical reference focusing on the right hip and lean muscular pelvic crest of a 19-year-old male werewolf (athletic runner/DJ build).
THE SACRED MARK: The Divine Runic Mark of Sól (The Black Sun) located STRICTLY ON THE RIGHT HIP.
DESIGN DETAILS: An intricate radiant Black Sun motif (the solar wheel of Sköll) featuring sharp, geometric solar flares and stylized ancient Norse sun runes (Sowilo variants). The linework is rich dark obsidian black with burnt amber undertones.
BIOLUMINESCENCE: Sub-dermal flaming glyphs ignite with a deep molten-gold and dark solar fire glow from beneath the skin, with microscopic cyan circuit-like leyline conduits tracing outward into the hip muscle.
SURROUNDING DETAILS: Toned obliques, dark caramel-black wolf tail base just visible at the lower back, clean skin texture, silver ring piercing glinting in the ambient neon light.
LIGHTING: Atmospheric dark room illuminated by ultraviolet blacklight and fiery amber screen glow from a DJ terminal.

NEGATIVE PROMPT: mark on left hip, marks on chest, collarbone tattoos, marks on neck, deformed anatomy, human ears, muddy linework, blurry, text, watermark.
```

---

### Blueprint 4: Logan Járn Douglas (Full Sleeve Tattoos & Eihwaz Wrist Brand)
```text
[MASTER STYLE PREFIX]
MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, GRITTY URBAN BIKER SANCTUARY, WARM WORKSHOP LIGHTING.

SUBJECT: Logan Járn Douglas, 49-year-old rugged Werewolf Beta master mechanic. Muscular, dense broad-shouldered build (198cm), rugged square jaw with salt-and-pepper stubble, tousled black hair greying at temples, amber eyes.
BODY ART & SLEEVES: Heavy full-sleeve tattoos covering both muscular arms from deltoids down to wrists. Intricate dark black-and-grey Norse and Celtic knotwork: Jörmungandr scale coils, snarling Fenris wolf heads, mountain pines, and braided runic chains. Faint, silvery hunt scars cut through the weathered ink.
LEFT WRIST BRAND: On the inner left wrist, a distinct sacred protective talisman combining his Birth Rune Eihwaz ("ᛇ", the World Tree) with the binding knot of Fenris, inscribed in dense cold iron ink.
SETTING: Standing in The Verve mechanic garage, sleeves rolled up over massive forearms, holding a vintage steel wrench and shop rag, surrounded by vintage muscle cars, car lifts, and warm amber hanging work lamps. Single pair of dark lupine ears atop head.

NEGATIVE PROMPT: second pair of human ears, clean corporate suit, clean spotless skin, deformed hands, extra fingers, cartoonish tattoos, blurry, watermark.
```

---

### Blueprint 5: Malachia Björn Douglas Bloodmoon (Warrior Neck/Arm Blackwork & Thurisaz Brand)
```text
[MASTER STYLE PREFIX]
MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, DARK COMBAT GRANDEUR, SEVERE GLADIATOR MOOD.

SUBJECT: Malachia Björn Douglas Bloodmoon, 28-year-old colossal Werewolf Dominant Alpha heavyweight gladiator (208cm / 6'10"). Mountainous boxer physique, thick neck, scarred knuckles, stoic severe expression, cold amber predatory eyes, windswept dark hair.
BODY ART: Brutal, heavy Norse-tribal warrior blackwork tattoos covering both massive arms, spreading across broad shoulders, and climbing boldly up the lateral sides of his muscular neck toward the jawline in the ancient Bloodmoon tradition. Spiked runic bands, jagged protection staves, and Fenrisian war sigils.
LEFT WRIST BRAND: On the inner left wrist, a prominent, dark ceremonial keloid brand of his Birth Rune Thurisaz ("ᚦ", the Giant's Thorn) bound with the Rune of Fenris, inked in deep cold iron.
FEATURES: Faded duel scar slicing through left eyebrow, slightly crooked boxer nose broken twice, white athletic hand wraps around large fists. Single pair of black wolf ears atop head.
LIGHTING: Moody underground combat ring lighting, dramatic chiaroscuro rim light highlighting muscle striations and heavy black ink.

NEGATIVE PROMPT: second pair of human ears, thin physique, cheerful smile, delicate tattoos, colorful anime art, deformed anatomy, extra fingers, watermark.
```

---

### Blueprint 6: Erik Ulfr Douglas (Patriarch's Cheekbone Scar & Tiwaz-Hagalaz Wrist Seal)
```text
[MASTER STYLE PREFIX]
MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, HIGH LUXURY PATRIARCH, CALIFORNIAN EXECUTIVE POWER.

SUBJECT: Erik Ulfr Douglas, 55-year-old Werewolf Prime Alpha patriarch and billionaire CEO (213cm / 7'0"). Imposing, disciplined ex-athlete powerhouse physique, jet-black hair with distinguished silver touches at temples, piercing amber eyes flaring molten gold, sharp authoritative jaw.
RITUAL SCAR: A faint, clean ceremonial ritual scar cleanly crossing his left cheekbone, earned during a solitary initiation hunt at age sixteen, lending dangerous edge to his sunny Californian executive smile.
WRIST SEAL: Peeking from beneath the unbuttoned cuff of a bespoke crisp white linen shirt, his left inner wrist reveals a discreet, sacred talisman combining Tiwaz ("ᛏ", Alpha Command) and Hagalaz ("ᚺ") bound with the Rune of Fenris in dense cold iron ink.
ACCESSORIES: Heavy silver-and-obsidian signet ring bearing the Douglas wolf-skull crest on left ring finger; heavy gold chain resting against collarbone. Single pair of dominant dark wolf ears atop head.
SETTING: High-rise penthouse boardroom overlooking Blackwood City coastline at golden hour sunset.

NEGATIVE PROMPT: second pair of human ears, scruffy beard, deformed hands, messy clothing, low budget, blurry, watermark.
```

---

### Blueprint 7: Wulfnic Báleygr Bloodmoon (Primordial Viking Demigod Brands & Scars)
```text
[MASTER STYLE PREFIX]
MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, MYTHOLOGICAL DEMIGOD, ANCIENT NORSE SAGA.

SUBJECT: Wulfnic Báleygr Bloodmoon, 1200-year-old Primordial Werewolf Firstborn Alpha of Alphas (220cm / 7'3", presented age 60). Colossal weathered Viking demigod frame, long silver-white warrior braid, thick silver beard, piercing ice-blue eyes glowing silver-blue with slit pupils.
PRIMEVAL BODY ART: Ancient 9th-century archaic Norse tattoos hand-carved with bone needles across his weathered torso, shoulders, and thick forearms. Archaic Elder Futhark staves, primeval Fenris blood-runes, and Svartúlfr clan longship sigils.
LEFT WRIST BRAND: An ancient sovereign Othala ("ᛟ") and Jera ("ᛃ") blood-oath talisman carved into his wrist over eleven centuries ago.
SCARS & RELICS: Deep legendary battle scars crisscrossing his chest and shoulders from ancient wars; leather cord at his throat bearing a Firstborn tooth; stolen eye of Odin hidden under archaic presence; draped in a heavy wolf-pelt mantle and thick woolen Norse tunic. Single pair of massive silver wolf ears.
SETTING: Ancient timber Longhouse sanctuary inside the Dead Zone, sitting before a roaring stone hearth beneath colossal thousand-year-old yew beams.

NEGATIVE PROMPT: second pair of human ears, modern clothes, technology, clean unscarred skin, youthful face, weak build, deformed hands, text, watermark.
```

---

### Blueprint 8: Paired Celestial Polarity Sheet (Máni Left Hip vs Sól Right Hip)
```text
[MASTER STYLE PREFIX]
MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, PREMIUM CHARACTER DESIGN CONCEPT SHEET, DUAL COMPOSITION, CELESTIAL POLARITY.

COMPOSITION: Split dual anatomical concept sheet showcasing the sacred celestial hip marks of the Douglas-Bloodmoon twins in high-definition contrast side-by-side.
LEFT PANEL (ALYSSA - THE WHITE MOON):
- Focus on the delicate curve of Alyssa's LEFT HIP.
- The Mark of Máni: Iridescent silver crescent moon surrounded by fine sub-dermal lunar glyphs, softly emitting a soothing silvery-white bioluminescent glow across fair porcelain skin.
- Soft caramel-and-black wolf tail brushing past.
RIGHT PANEL (JASPER - THE BLACK SUN):
- Focus on the lean muscular athletic curve of Jasper's RIGHT HIP.
- The Mark of Sól: Dark radiant black sun motif with angular solar flares, ignited from within by sub-dermal molten-gold and dark flame embers, faint cyan technomancy lines tracing the hip bone.
- Dark caramel-black wolf tail brushing past.
LIGHTING & SYMBOLISM: Moonlit silver radiance on the left balancing dark solar golden flame on the right, embodying the ancient prophecy of the Twin Wolves.

NEGATIVE PROMPT: inverted hips (mark on wrong side), marks on chest, marks on neck, collarbone tattoos, angel wings, human ears, deformed anatomy, blurry linework, text, watermark.
```

---

## 6. Synthesis & Execution Guidance

1. **Phase 1: Asset Directory Creation**:
   Ensure `docs/references/` is populated with the definitive reference document, and `asset/references/` (or `assets/references/`) is created to house the generated PNG/JPG files.
2. **Phase 2: Generation Execution**:
   Use the verified Gemini Argon / Imagen 3 blueprints above, enforcing single-ear anatomy and hip-position strictness.
3. **Phase 3: Repository Integration**:
   Catalog the resulting images in `asset/PROMPTS_PERSONAGGI_E_OUTFIT_GEMINI_ARGON.md` or a new standalone companion catalog `asset/PROMPTS_MARCHI_RUNICI_E_DIVINI.md`, updating `CHANGELOG.md` with full traceability.
