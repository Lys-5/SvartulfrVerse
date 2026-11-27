# Emotion Sprites — Prompt `16:9` Multi-Posa su Sfondo Bianco Puro (`1696x2528` RGBA)

> **Obiettivo:** Generare le pose emotive compatibili con il **Bulk Upload Sprites** di Wyvern, allineate al centimetro sullo stesso canvas `1696x2528` RGBA trasparente (`FLOOR_Y=2500`, `PX_PER_CM=9.75`) degli sprite `neutral.png` già completati.
>
> **Matrice Ufficiale delle `28` Emozioni di Wyvern (GoEmotions, alfabetico):**
> `admiration`, `amusement`, `anger`, `annoyance`, `approval`, `caring`, `confusion`, `curiosity`, `desire`, `disappointment`, `disapproval`, `disgust`, `embarrassment`, `excitement`, `fear`, `gratitude`, `grief`, `joy`, `love`, `nervousness`, **`neutral`** *(già fatta!)*, `optimism`, `pride`, `realization`, `relief`, `remorse`, `sadness`, `surprise`.
> *(Opzionale: `Extra sprites` custom richiamabili con sintassi `[Nome: posa]`, es. `[Jasper: wave]`.)*
>
> **Regole TASSATIVE per Gemini Pro (`16:9` Widescreen):**
> 1. **Sfondo Bianco Puro Piatto (`#FFFFFF`):** NESSUN pavimento, NESSUNA ombra a terra, NESSUNA barra divisoria verticale nera, NESSUN testo o etichetta. Solo `4` (o `3`) figure intere **dalla testa ai piedi** ben distanziate tra loro da ampio spazio bianco vuoto.
> 2. **Reference da Allegare:** Allega **SEMPRE DUE immagini** per mantenere al 100% volto, outfit di default, colori e proporzioni:
>    - **Alyssa:** [alyssa_reference.png](file:///E:/repository/SvartulfrVerse/assets/Alyssa/alyssa_reference.png) + [alyssa_neutral.png](file:///E:/repository/SvartulfrVerse/assets/Alyssa/alyssa_neutral.png)
>    - **Jasper:** [jasper_reference.png](file:///E:/repository/SvartulfrVerse/assets/Jasper/jasper_reference.png) + [jasper_neutral.png](file:///E:/repository/SvartulfrVerse/assets/Jasper/jasper_neutral.png)
> 3. **Dove salvare i fogli generati:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\` e `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\`.
> 4. **Taglio & Calibrazione Automatica (`--mode sprite`):** Converte lo sfondo bianco in trasparenza RGBA, scala esattamente a **`155 cm` (Alyssa)** / **`193 cm` (Jasper)** su canvas `1696x2528` e salva ogni file come `<emozione>.png` minuscolo pronto per il Bulk Upload!
> 5. **Piano Modulare in 2 Livelli:** Puoi fermarti al **Batch Core (`3` griglie = `12` emozioni principali + `neutral` = `13`)** per personaggio oppure completare tutte le **`7` griglie (`28/28` emozioni totali)** con il **Batch Extended (`4` griglie restanti)**.

---

## PARTE 1 — ALYSSA HVIT DOUGLAS BLOODMOON (`155 cm`, Default SUCC Crop Top + Denim Shorts)
- **Reference da allegare SEMPRE:** `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_reference.png` + `E:\repository\SvartulfrVerse\assets\Alyssa\alyssa_neutral.png`
- **Salva le griglie in:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\`
- **Copia base già pronta:** `assets/Alyssa/alyssa_neutral.png` → `assets/Alyssa/sprites/default/neutral.png`

### Batch Core Alyssa (`EM-A1` .. `EM-A3` = `12` Emozioni Principali)

#### `EM-A1` — Warm & Positive Core (`joy`, `love`, `amusement`, `caring`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\EM-A1.png`
- **Comando taglio (`--height-cm 155 --names joy,love,amusement,caring`):**

```text
4-figure horizontal 16:9 Visual Novel character expression sprite sheet depicting ONLY the petite 155 cm curvy hourglass werewolf Alyssa matching BOTH attached images strictly 1:1 in face, wavy caramel-chestnut hair, mint-green doe eyes, nose freckles, SINGLE PAIR OF CARAMEL WOLF EARS WITH BLACK TIPS atop head (with rich loose caramel curtain locks completely covering BOTH temples smoothly — STRICTLY ZERO human ears), bushy black-tipped caramel wolf tail, Mannaz wrist rune, platinum navel ring, and exact default outfit (sunflower-yellow ruffled wrap crop top, light-blue denim shorts with tail hole, white low-top canvas sneakers) in unified semi-realistic digital painting style. CRITICAL LAYOUT: 4 complete head-to-toe full-body standing figures arranged side-by-side evenly spaced apart by wide blank margins on a PURE SOLID FLAT PURE-WHITE BACKGROUND (#FFFFFF) — STRICTLY ZERO floor shadows, ZERO ground gradients, ZERO divider bars, ZERO text, ZERO labels, and NO touching between figures. 1 (JOY): Radiant bright open smile, sparkling eyes, relaxed open arms slightly lifted in cheerful energy, perked upright wolf ears, lifted wagging tail. 2 (LOVE): Soft dreamy blushing cheeks, tender adoring eyes, hands clasped warmly near chest heart, softened happy wolf ears angled outward. 3 (AMUSEMENT): Playful light giggle with hand gently near smiling lips, tilted head, twinkling teasing eyes, one wolf ear perked curiously. 4 (CARING): Compassionate warm gentle gaze leaning slightly forward, one comforting palm extended softly, tender reassuring smile.
```

#### `EM-A2` — Reactive & Shy Core (`curiosity`, `embarrassment`, `surprise`, `confusion`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\EM-A2.png`
- **Comando taglio (`--height-cm 155 --names curiosity,embarrassment,surprise,confusion`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Alyssa matching BOTH attached images strictly 1:1 (155 cm curvy frame, caramel-chestnut waves covering BOTH temples smoothly with ZERO human ears, single top black-tipped caramel wolf ears, bushy tail, yellow ruffled wrap crop top, blue denim shorts, white sneakers). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, generous blank space between all 4 head-to-toe figures, ZERO shadows, ZERO divider lines, ZERO text. 1 (CURIOSITY): Sweet head tilt, bright wide intrigued eyes, light index finger lightly resting near chin, one wolf ear perked sharp and one slightly angled. 2 (EMBARRASSMENT): Strong pink blush across cheeks and nose bridge, shy flustered smile glancing slightly sideways while tucking hair/fidgeting with fingers in front of waist, wolf ears flattened/drooped cutely outward, tail curled around leg. 3 (SURPRISE): Wide startled mint-green eyes, tiny rounded 'o' mouth, hands raised lightly chest-high in sudden surprise, wolf ears snapped tall upright, fluffed surprised tail. 4 (CONFUSION): Furrowed puzzled brows, small bewildered frown, gentle head tilt with one palm turned up slightly questioning, asymmetrical puzzled wolf ears.
```

#### `EM-A3` — Tense & Sad Core (`nervousness`, `anger`, `annoyance`, `sadness`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\EM-A3.png`
- **Comando taglio (`--height-cm 155 --names nervousness,anger,annoyance,sadness`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Alyssa matching BOTH attached images strictly 1:1 (155 cm curvy frame, caramel-chestnut waves covering BOTH temples smoothly with ZERO human ears, single top black-tipped caramel wolf ears, bushy tail, yellow ruffled wrap crop top, blue denim shorts, white sneakers). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide empty gaps between all 4 head-to-toe figures, ZERO floor shadows, ZERO divider lines, ZERO text. 1 (NERVOUSNESS): Anxious tight smile, slightly hunched shoulders, fingers touching her left-wrist Mannaz rune nervously, slightly lowered tense wolf ears, tail tucked close behind knees. 2 (ANGER): Fierce protective White Moon glare, brows knitted tightly, mouth set firmly showing tiny wolf canine hint, clenched fists at sides, wolf ears pinned flat back defensively. 3 (ANNOYANCE): Exasperated deadpan pouting stare, arms crossed stubbornly under bust, slight side-eye, half-drooped annoyed wolf ears. 4 (SADNESS): Soft sorrowful downcast watery eyes, trembling gentle frown, hands held loosely low in front of body, deeply drooped sad wolf ears and low drooping tail.
```

---

### Batch Extended Alyssa (`EM-A4` .. `EM-A7` = `15` Emozioni Restanti per `28/28`)

#### `EM-A4` — Affectionate & Expressive (`admiration`, `approval`, `desire`, `excitement`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\EM-A4.png`
- **Comando taglio (`--height-cm 155 --names admiration,approval,desire,excitement`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Alyssa matching BOTH attached images strictly 1:1 (155 cm curvy frame, caramel waves covering BOTH temples smoothly with ZERO human ears, single top caramel wolf ears, bushy tail, yellow wrap crop top, blue denim shorts, white sneakers). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide empty gaps between 4 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (ADMIRATION): Awestruck starry wide eyes and soft parted impressed smile, hands held lightly near cheeks/collarbone, tall alert wolf ears. 2 (APPROVAL): Encouraging sunny smile with gentle nod-tilt and warm affirmative thumbs-up/open gesture, confident happy posture. 3 (DESIRE): Deeply flushed cheeks, heavy-lidded longing misty mint-green gaze and soft parted lips, one hand resting delicately on bare collarbone/sun pendant, subtly softened wolf ears. 4 (EXCITEMENT): Overjoyed bright grin, energetic bounce pose on tiptoes with clenched cheerful hands near shoulders, high wagging tail and fully perked wolf ears.
```

#### `EM-A5` — Gentle Positive (`gratitude`, `optimism`, `pride`, `relief`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\EM-A5.png`
- **Comando taglio (`--height-cm 155 --names gratitude,optimism,pride,relief`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Alyssa matching BOTH attached images strictly 1:1 (155 cm curvy frame, caramel waves covering BOTH temples smoothly with ZERO human ears, single top caramel wolf ears, bushy tail, yellow wrap crop top, blue denim shorts, white sneakers). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide empty gaps between 4 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (GRATITUDE): Heartfelt sincere thankful smile with softened eyes and both hands pressed warmly over heart. 2 (OPTIMISM): Bright hopeful radiant expression looking gently upward-forward, relaxed confident stance with one hand resting lightly on hip. 3 (PRIDE): Cute triumphant chest-puffed confident smile, both hands resting cheerfully on hips, tall proud wolf ears and high fluffy tail. 4 (RELIEF): Soft exhaling smile, relaxed drooping shoulders, one hand placed gently over chest as tension melts, gently relaxed wolf ears.
```

#### `EM-A6` — Cognitive & Heavy (`realization`, `fear`, `disappointment`, `disapproval`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\EM-A6.png`
- **Comando taglio (`--height-cm 155 --names realization,fear,disappointment,disapproval`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Alyssa matching BOTH attached images strictly 1:1 (155 cm curvy frame, caramel waves covering BOTH temples smoothly with ZERO human ears, single top caramel wolf ears, bushy tail, yellow wrap crop top, blue denim shorts, white sneakers). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide empty gaps between 4 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (REALIZATION): Sudden enlightened widening of eyes, raised finger snapping/tapping near cheek in an 'aha!' spark, alert tall wolf ears. 2 (FEAR): Trembling frightened wide eyes, pale worried expression, arms wrapped protectively around waist stepping slightly back, wolf ears pressed flat down, tucked tail. 3 (DISAPPOINTMENT): Quiet letdown sigh, lowered eyelids and soft downturned mouth, slumped arms holding each other lightly, drooped ears. 4 (DISAPPROVAL): Firm stern disappointed gaze, brows drawn together, shaking head gently with hands on hips, stiff upright posture.
```

#### `EM-A7` — Deep Negative Trio (`disgust`, `grief`, `remorse` · `3` Colonne)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\EM-A7.png`
- **Comando taglio (`--height-cm 155 --names disgust,grief,remorse`):**

```text
3-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Alyssa matching BOTH attached images strictly 1:1 (155 cm curvy frame, caramel waves covering BOTH temples smoothly with ZERO human ears, single top caramel wolf ears, bushy tail, yellow wrap crop top, blue denim shorts, white sneakers). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, generous blank margins between all 3 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (DISGUST): Wrinkled nose, recoiling leaning slightly back in clear distaste, raised open palm warding away politely yet firmly, flattened wolf ears. 2 (GRIEF): Deeply heartbroken tear-filled expression, one hand lifted trembling toward chest/mouth in profound sorrow, deeply slumped wolf ears and limp tail. 3 (REMORSE): Guilt-stricken apologetic downward gaze, brows pinched regretfully, hands clasped tightly apologizing in front of abdomen, lowered apologetic wolf ears.
```

---

## PARTE 2 — JASPER SVARTR DOUGLAS BLOODMOON (`193 cm`, Default Faded Black Hoodie + Neck Headphones)
- **Reference da allegare SEMPRE:** `E:\repository\SvartulfrVerse\assets\Jasper\jasper_reference.png` + `E:\repository\SvartulfrVerse\assets\Jasper\jasper_neutral.png`
- **Salva le griglie in:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\`
- **Copia base già pronta:** `assets/Jasper/jasper_neutral.png` → `assets/Jasper/sprites/default/neutral.png`

### Batch Core Jasper (`EM-J1` .. `EM-J3` = `12` Emozioni Principali)

#### `EM-J1` — Warm & Sly Core (`joy`, `love`, `amusement`, `caring`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\EM-J1.png`
- **Comando taglio (`--height-cm 193 --names joy,love,amusement,caring`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY the male werewolf Jasper matching BOTH attached images strictly 1:1 in lean athletic 193 cm build, sharp jawline with light stubble, vivid mint-green eyes, nose freckles, thick shaggy caramel-chestnut wolf-cut locks sweeping densely over BOTH temples down to jawline covering sides 100% (STRICTLY ZERO human ears on sides of head), SINGLE PAIR OF CARAMEL WOLF EARS WITH BLACK TIPS atop skull, bushy black-tipped caramel wolf tail, Mannaz left wrist rune, platinum Douglas signet ring, and exact default outfit (washed faded black oversized streetwear hoodie over dark tee, black joggers with tail hole, black/white canvas high-tops, black & acid-green wireless headphones resting around neck). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide empty gaps between all 4 head-to-toe figures, ZERO floor shadows, ZERO divider lines, ZERO text. 1 (JOY): Rare genuine warm relaxed smile softening his eyes, one hand slipped comfortably in hoodie pocket, perked relaxed wolf ears. 2 (LOVE): Soft unguarded affectionate gaze with subtle faint flush across freckles, tender gentle half-smile reserved only for Alyssa/bond, softened drooped wolf ears, curling tail tip. 3 (AMUSEMENT): Classic cocky lopsided smirk with raised brow and teasing spark in mint-green eyes, crossing arms loosely or adjusting headphone band with two fingers. 4 (CARING): Protective steady watchful expression leaning subtly forward, gentle reassuring nod and warm quiet eye contact, attentive upright wolf ears.
```

#### `EM-J2` — Reactive & Sharp Core (`curiosity`, `embarrassment`, `surprise`, `confusion`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\EM-J2.png`
- **Comando taglio (`--height-cm 193 --names curiosity,embarrassment,surprise,confusion`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Jasper matching BOTH attached images strictly 1:1 (193 cm lean frame, thick shaggy caramel wolf-cut covering BOTH temples 100% with ZERO human ears, single top caramel wolf ears with black tips, tail, faded black hoodie, neck headphones, black joggers, high-tops). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide gaps between 4 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (CURIOSITY): Sharp analytical squint, head angled slightly, rubbing chin/jaw thoughtfully, one wolf ear swiveled sharply forward. 2 (EMBARRASSMENT): Caught off-guard blushing faintly on ears & cheekbones, looking sideways while rubbing back of neck awkwardly with one hand (NOT touching temples), wolf ears flattened flat sideways in mortification. 3 (SURPRISE): Wide sharp startled mint-green eyes, brows shot up, shifting weight slightly back with hands out of pockets ready to react, tall perked wolf ears. 4 (CONFUSION): Raised puzzled eyebrow, skeptical squinted gaze, slight head tilt holding one hand out lightly palm-up, uneven asymmetrical wolf ears.
```

#### `EM-J3` — Defiant & Heavy Core (`nervousness`, `anger`, `annoyance`, `sadness`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\EM-J3.png`
- **Comando taglio (`--height-cm 193 --names nervousness,anger,annoyance,sadness`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Jasper matching BOTH attached images strictly 1:1 (193 cm lean frame, thick shaggy caramel wolf-cut covering BOTH temples 100% with ZERO human ears, single top caramel wolf ears with black tips, tail, faded black hoodie, neck headphones, black joggers, high-tops). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide gaps between 4 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (NERVOUSNESS): Restless guarded tension, eyes darting sideward, left thumb rolling platinum coin across knuckles over left wrist Mannaz rune, tense low wolf ears. 2 (ANGER): Lethal predatory Svartr scowl, mint-green eyes blazing fiercely with subtle molten-gold rim sparks, bared sharp white canine teeth, tense ready combat crouch/fists clenched, wolf ears pinned flat back against skull. 3 (ANNOYANCE): Classic bored sardonic glare, heavy eyelids, pinching bridge of nose between thumb and forefinger with deep unimpressed frown. 4 (SADNESS): Quiet guarded grief/sorrow, looking down at floor in silence, shoulders slightly drawn in, hands shoved deep in hoodie pockets, deeply lowered wolf ears and still tail.
```

---

### Batch Extended Jasper (`EM-J4` .. `EM-J7` = `15` Emozioni Restanti per `28/28`)

#### `EM-J4` — Confident & Intense (`admiration`, `approval`, `desire`, `excitement`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\EM-J4.png`
- **Comando taglio (`--height-cm 193 --names admiration,approval,desire,excitement`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Jasper matching BOTH attached images strictly 1:1 (193 cm lean frame, thick shaggy caramel wolf-cut covering BOTH temples 100% with ZERO human ears, single top caramel wolf ears, tail, faded black hoodie, neck headphones, black joggers, high-tops). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide gaps between 4 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (ADMIRATION): Quietly impressed smirk, brows raised genuinely nodding slightly, relaxed appreciative posture. 2 (APPROVAL): Cool casual approving half-grin, confident slight salute/two-finger nod with hand out of pocket. 3 (DESIRE): Intense unblinking dark-lidded hungry mint-green stare catching faint molten-gold sparks, slight parted smirk showing sharp canine hint, tense kinetic posture leaning subtly forward. 4 (EXCITEMENT): Wicked hyped-up rogue grin, eyes bright like before a live DJ set or heist, snapping/clenching one hand eagerly, high alert wolf ears.
```

#### `EM-J5` — Cool & Grounded (`gratitude`, `optimism`, `pride`, `relief`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\EM-J5.png`
- **Comando taglio (`--height-cm 193 --names gratitude,optimism,pride,relief`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Jasper matching BOTH attached images strictly 1:1 (193 cm lean frame, thick shaggy caramel wolf-cut covering BOTH temples 100% with ZERO human ears, single top caramel wolf ears, tail, faded black hoodie, neck headphones, black joggers, high-tops). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide gaps between 4 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (GRATITUDE): Sincere quiet nod with softened warm eyes and slight thankful smirk, resting one hand briefly over collar/chest. 2 (OPTIMISM): Calm forward-looking sly confident grin, relaxed slouched stance with hands casually in pockets. 3 (PRIDE): Supremely smug self-satisfied hacker grin, chest slightly raised, arms folded victoriously across chest, high upright wolf ears. 4 (RELIEF): Letting out a long quiet breath, eyes briefly half-shut, shoulders dropping visibly from tension, one hand resting relaxed at side of headphone cup.
```

#### `EM-J6` — Alert & Hard (`realization`, `fear`, `disappointment`, `disapproval`)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\EM-J6.png`
- **Comando taglio (`--height-cm 193 --names realization,fear,disappointment,disapproval`):**

```text
4-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Jasper matching BOTH attached images strictly 1:1 (193 cm lean frame, thick shaggy caramel wolf-cut covering BOTH temples 100% with ZERO human ears, single top caramel wolf ears, tail, faded black hoodie, neck headphones, black joggers, high-tops). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide gaps between 4 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (REALIZATION): Sudden sharp widening of eyes cracking a dark cipher, finger pointed lightly upward/snapping, wolf ears snapped erect. 2 (FEAR): Pale wide-eyed shock (imagining Alyssa in mortal danger), tense stepped-back defensive stance, clenched hands ready to shift, flattened defensive ears. 3 (DISAPPOINTMENT): Cold cynical letdown frown, looking away skeptically with arms crossed tightly, lowered ears. 4 (DISAPPROVAL): Ice-cold skeptical glare shaking head lightly, sharp flat mouth, unyielding defensive stance.
```

#### `EM-J7` — Dark Trio (`disgust`, `grief`, `remorse` · `3` Colonne)
- **Salva come:** `E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\EM-J7.png`
- **Comando taglio (`--height-cm 193 --names disgust,grief,remorse`):**

```text
3-figure horizontal 16:9 Visual Novel full-body expression sprite sheet depicting ONLY Jasper matching BOTH attached images strictly 1:1 (193 cm lean frame, thick shaggy caramel wolf-cut covering BOTH temples 100% with ZERO human ears, single top caramel wolf ears, tail, faded black hoodie, neck headphones, black joggers, high-tops). PURE SOLID FLAT #FFFFFF WHITE BACKGROUND ONLY, wide gaps between all 3 head-to-toe figures, ZERO shadows, ZERO bars, ZERO text. 1 (DISGUST): Curled upper lip sneer in sharp repulsion, leaning head back slightly with disgusted narrowed eyes, flattened ears. 2 (GRIEF): Hollow shattered quiet stare, jaw clenched hard against pain, head bowed slightly with fists knotted tight inside pockets, ears dropped completely flat. 3 (REMORSE): Quiet heavy guilt-ridden sideways glance, brows furrowed regretfully, one hand gripping back of neck awkwardly while looking down, lowered apologetic wolf ears.
```

---

## Comandi Rapidi di Taglio & Calibrazione Automatica (`1696x2528` RGBA)

Appena salvi i fogli in `scratch\emotion_grids\`, lanciamo lo slicing pixel-perfetto su griglia altezze condivisa:

```powershell
# Esempio Alyssa Core 1 (EM-A1 -> 155 cm RGBA trasparente)
python E:\repository\SvartulfrVerse\scripts\asset_reference_pipeline.py slice-outfit-grid `
  --mode sprite --height-cm 155 `
  --src E:\repository\SvartulfrVerse\scratch\emotion_grids\Alyssa\EM-A1.png `
  --cols 4 --names joy,love,amusement,caring `
  --out-dir E:\repository\SvartulfrVerse\assets\Alyssa\sprites\default

# Esempio Jasper Core 1 (EM-J1 -> 193 cm RGBA trasparente)
python E:\repository\SvartulfrVerse\scripts\asset_reference_pipeline.py slice-outfit-grid `
  --mode sprite --height-cm 193 `
  --src E:\repository\SvartulfrVerse\scratch\emotion_grids\Jasper\EM-J1.png `
  --cols 4 --names joy,love,amusement,caring `
  --out-dir E:\repository\SvartulfrVerse\assets\Jasper\sprites\default
```
