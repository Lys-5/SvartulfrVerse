# Asset Visivi & Motore di Prompt: Marchi Divini e Proporzioni di Gruppo
*Svartúlfr Verse — Specifiche Grafiche Ufficiali*

---

## 1. Marchi Canonici & Vincoli Anatomici Rigorosi

### 1.1 Marchio di Máni (Hvítúlfr — Alyssa Douglas)
- **Posizione Tassativa:** Esclusivamente sull'anca sinistra (`left hip / left iliac crest`).
- **Descrizione Visiva:** Mezzaluna argentata finemente cesellata, intagliata nella carne con glifi runici sub-dermici luminescenti che pulsano di una tenue fluorescenza lunare bianco-argentea. Nessuna irradiazione caotica: i glifi seguono la curva dell'osso iliaco sinistro.
- **Divieti Assoluti (Negative Constraints):** Zero marchi sull'anca destra, petto, schiena o viso. Divieto assoluto di doppio paio di orecchie (ha solo le orecchie lupine in testa, zero orecchie umane).
- **Titolo Sacro:** Mániúlfr (Lupo della Luna Bianca).

### 1.2 Marchio di Sól (Sólúlfr — Jasper Douglas)
- **Posizione Tassativa:** Esclusivamente sull'anca destra (`right hip / right iliac crest`).
- **Descrizione Visiva:** Sole nero radioso (`black sun`) cerchiato da rune solari norrene stilizzate a raggi fiammeggianti sub-dermici a riflesso oro scuro e nero ossidiana.
- **Divieti Assoluti (Negative Constraints):** Zero marchi sull'anca sinistra, petto o viso. Zero orecchie umane (solo orecchie lupine).
- **Titolo Sacro:** Sólúlfr (Lupo del Sole Nero).

### 1.3 Marchio Gebo (Alyssa & Jasper Douglas)
- **Posizione Tassativa:** Faccia interna del polso sinistro (`inner left wrist`).
- **Descrizione Visiva:** Tatuaggio geometrico a croce runica Gebo ($\mathcal{X}$) impresso con inchiostro cerimoniale a polvere di ferro freddo (`cold-iron ash ink`). Appare come una cicatrice/inchiostratura scura, opaca e priva di bagliori, fungente da legame gemellare e schermo antimagico.

---

## 2. Griglia Proporzioni & Altezze di Gruppo

| Personaggio | Altezza Canonica | Riferimento Visivo / Allineamento Spaziale |
| :--- | :--- | :--- |
| **Alyssa Douglas** | **193 cm** (6'4") | Demi-umana slanciata, muscolatura tonica da atleta, altezza alla pari con Jasper. |
| **Jasper Douglas** | **193 cm** (6'4") | Demi-umano possente, spalle larghe, linea degli occhi perfettamente identica ad Alyssa. |
| **Noah Blackwood** | **197 cm** (6'5.5") | Supera i gemelli di 4 cm; la linea degli occhi è appena sopra la fronte di Alyssa e Jasper. |
| **Malachia Douglas** | **208 cm** (6'10") | Supera Alyssa di 15 cm e oltre mezzo metro rispetto a una donna media. Il vertice della testa di Alyssa si allinea a metà del suo sterno/pettorale; corporatura da colosso mastodontico. |
| **Erik Douglas** | **213 cm** (7'0") | Imponente patriarca da 7 piedi; sovrasta Noah di 16 cm e Alyssa di 20 cm. |
| **Wulfnic Douglas** | **220 cm** (7'2.5") | Gigante ancestrale, apice visivo del gruppo; la sommità del suo torace è all'altezza del volto dei gemelli. |

---

## 3. Suite di Prompt Master

### 3.1 Midjourney v6

#### Prompt: Marchio di Máni (Alyssa - Dettaglio Anca Sx)
```text
close-up intimate photography of the bare left hip and iliac crest of a tall athletic werewolf woman, clean smooth pale skin, an isolated glowing silver crescent moon rune tattoo etched directly onto the left hip bone, intricate Norse moon glyphs faintly pulsing with sub-dermal lunar white luminescence, completely clean unblemished skin on waist and stomach, cinematic studio lighting, raw texture, hyper-realistic, 8k resolution --ar 4:5 --style raw --v 6.0
```

#### Prompt: Marchio di Sól (Jasper - Dettaglio Anca Dx)
```text
detailed close-up photography of the bare right hip of a massive athletic werewolf man, tanned rugged skin, an isolated black radiant sun rune tattoo inked strictly onto the right iliac crest, jagged stylized solar flame glyphs with sub-dermal dark golden and obsidian aura, zero markings on abdomen and torso, dramatic chiaroscuro side lighting, tactile skin pore detail, 8k resolution --ar 4:5 --style raw --v 6.0
```

#### Prompt: Marchio Gebo (I Gemelli - Polso Sx)
```text
macro detail shot of two hands resting together, showing the inner left wrists of a male and female pair, each bearing an identical crisp minimalist Gebo rune X tattoo inked in matte cold-iron ash black pigment, non-magical grounded texture, subtle faint skin indentations, natural diffuse daylight, hyper-detailed skin grain --ar 16:9 --style raw --v 6.0
```

#### Prompt: Scena di Gruppo & Scala d'Altezza (Alyssa, Jasper, Noah, Malachia)
```text
cinematic full body group shot of four modern fantasy werewolves standing side-by-side on an urban rooftop at sunset, dramatic height difference and vertical scale: on the far left stands a massive 208 cm (6'10") muscular titan male (Malachia), towering over a 193 cm (6'4") athletic female wolf demi-human (Alyssa) who reaches only to his mid-chest level; beside her stands an identical 193 cm tall male twin (Jasper) with exact eye-level parity; beside them stands a 197 cm tall alpha male (Noah) slightly taller than the twins. All demi-humans have single pairs of pointed wolf ears on their heads and zero human ears, realistic body proportions, coastal skyline background, golden hour lighting, 8k --ar 16:9 --style raw --v 6.0
```

---

### 3.2 SDXL / Pony Diffusion (Pony XL)

#### Prompt: Marchio di Máni (Alyssa)
```text
score_9, score_8_up, score_7_up, source_anime, 1girl, alyssa douglas, wolf demi-human, wolf ears, grey eyes, athletic physique, crop top, exposed midriff, bare left hip, (single tattoo:1.3), (left hip tattoo:1.4), (silver crescent moon tattoo:1.3), glowing runes, sub-dermal luminescence, clean stomach, no human ears, high resolution, masterpiece
Negative prompt: score_4, score_3, score_2, score_1, (human ears:1.4), 4 ears, (full body tattoo, chest tattoo, arm tattoo, facial markings, tattoo sleeve:1.4), blurry, deformed
```

#### Prompt: Marchio di Sól (Jasper)
```text
score_9, score_8_up, score_7_up, source_anime, 1boy, jasper douglas, wolf demi-human, wolf ears, amber eyes, muscular broad shoulders, low-rise trousers, bare right hip, (single tattoo:1.3), (right hip tattoo:1.4), (black radiant sun tattoo:1.3), obsidian flame runes, clean chest, no human ears, atmospheric lighting, masterpiece
Negative prompt: score_4, score_3, score_2, score_1, (human ears:1.4), 4 ears, (full body tattoo, left hip tattoo, chest tattoo, arm tattoo:1.4), extra limbs, low quality
```

#### Prompt: Composizione Gruppo (Height Hierarchy con Regional Prompting / BREAK)
```text
score_9, score_8_up, score_7_up, source_anime, group shot, (height difference:1.4), (size difference:1.3), full body, standing side-by-side,
1boy, malachia douglas, (tallest:1.3), 208cm tall, massive muscular frame, wolf ears, dark hair, towering over others
BREAK
1girl, alyssa douglas, 193cm tall, athletic build, head reaching malachia mid-chest level, wolf ears,
BREAK
1boy, jasper douglas, 193cm tall, equal height to alyssa, broad shoulders, wolf ears,
BREAK
1boy, noah blackwood, 197cm tall, slightly taller than twins, wolf ears,
Negative prompt: score_4, score_3, score_2, score_1, (human ears:1.4), 4 ears, equal heights, midget, deformed hands, bad anatomy, cropped heads
```

---

### 3.3 NovelAI V3

#### Prompt: Alyssa & Malachia (Scale Contrast)
```text
{masterpiece}, {best quality}, 1girl, 1boy, alyssa douglas, malachia douglas, wolf ears, {height difference}, {size difference}, head to mid-chest, {tall male}, {athletic female}, standing together, modern fantasy city background, detailed lighting, volumetric shadows
Undesired Content: human ears, 4 ears, equal height, flat color, bad anatomy, multiple tattoos, blurry, lowres
```

#### Regola Speciale per Sierra Cruz (Lamia):
- **Prompt:** `sierra cruz, lamia, (snake tail:1.4), lower body is a 4-meter rainbow iridescent serpentine tail, colorful scales, slithering on ground, rainbow hair, zero legs, no feet`
- **Undesired Content:** `legs, feet, shoes, knees, pants, standing on feet, walking`
