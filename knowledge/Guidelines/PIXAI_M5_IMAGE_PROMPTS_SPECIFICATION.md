# PixAI Prompt Specifications: Milestone 5 Secondary Cast Batch

**Date:** 2026-11-16  
**Scope:** Ready-to-run image generation prompt specifications for Kian, Goran, Radek, Eric, and Javier Reyes.  
**Platform:** PixAI (https://pixai.art)  
**Standard Checkpoint & LoRA Configuration:**  
- **Base Checkpoint:** `VXP_XL v2.2 (Hyper)`  
- **LoRA:** `Niji semi realism [Illustrious]` (Weight: `0.75 - 0.85`)  
- **Sampling Steps:** `7 - 8`  
- **Sampler:** `Euler a` or `DPM++ SDE`  
- **CFG Scale:** `1.6 - 1.8`  
- **VAE:** `Pony Enhanced VAE Pastels` or `SharpSpectrumVAEXL`  
- **Aspect Ratio:** `3:4` (Portrait Avatar: 768x1024 or 832x1216)  
- **Anatomical Discipline:** Demi-human species-specific positive framing (single pair of animal ears on head for mammals/avians, zero mixing of species traits, technical exclusion tags confined strictly to negative prompt).

---

## 1. Kian (Team Ukiyo Scout & Hunter)
- **Role & Lorebook:** Index 6, `FINAL/Svartulfr_NPC_Primary.json`, ID `zlW_PSDs-w17mZqXA8WOY`.
- **Species & Archetype:** Orc, agile dungeon scout and hunter.
- **Positive Prompt:**
  ```text
  masterpiece, best quality, ultra-detailed, semi-realistic, painterly realism, anime-inspired realism, premium visual novel art, luxury visual storytelling, niji style, natural anatomy, highly detailed face, expressive eyes, soft facial rendering, healthy vibrant skin tone, emotional realism,

  1boy, solo, male, 24 years old, orc, handsome male orc, lean muscular athletic build, predator grace, raven-black messy top-knot hair, undercut, sharp slate-grey eyes, keen focused gaze, unusually handsome symmetrical facial structure, two small delicate ivory tusks protruding upward from lower lip, polished gold hoop ring piercing through left tusk, clean shaven jawline, black ink spiral tribal tattoos flowing from neck across shoulder blades,

  wearing form-fitting dark tactical leather armor, high-collared scout vest, dark carbon-fiber reinforced bracers, twin curved shadow daggers sheathed on harness, dark combat pants,

  moody dungeon entrance, ancient stone ruins, dim torchlight and blue ethereal ambient glow, dramatic rim lighting, cinematic shadows
  ```
- **Negative Prompt:**
  ```text
  lowres, worst quality, low quality, bad anatomy, bad hands, extra fingers, extra limbs, mutated hands, deformed face, blurry, watermark, signature, text, cropped, child, feminine, bulky ugly monster, exaggerated pig nose, missing tusks, deformed tusks
  ```

---

## 2. Goran (Team Ukiyo Frontline Berserker)
- **Role & Lorebook:** Index 7, `FINAL/Svartulfr_NPC_Primary.json`, ID `w-wcHqVIIvpNhN2kJh_NW`.
- **Species & Archetype:** Orc, frontline berserker and vanguard.
- **Positive Prompt:**
  ```text
  masterpiece, best quality, ultra-detailed, semi-realistic, painterly realism, anime-inspired realism, premium visual novel art, luxury visual storytelling, niji style, natural anatomy, highly detailed face, expressive eyes, soft facial rendering, healthy vibrant skin tone, emotional realism,

  1man, solo, male, 29 years old, orc berserker, colossal massive build, impenetrable brick wall physique, extraordinarily wide barrel chest, thick muscular neck, olive-green weathered skin, messy black hair with faded shaved sides, intense bloodshot hazel eyes ignited with faint predatory orange glow, flattened broken pugilist nose, thick jaw, one jagged broken lower tusk on right, 'HATRED' gothic tattoo across heavy knuckles, beast claw scars across chest,

  wearing distressed heavy leather combat vest, rugged steel-reinforced gauntlets with brass knuckles, heavy combat harness, thick tactical trousers, massive dual-headed steel warhammer resting against shoulder,

  underground monster den, shattered rock floor, dust particles, embers and glowing orange magma light, intense dramatic side lighting, cinematic contrast
  ```
- **Negative Prompt:**
  ```text
  lowres, worst quality, low quality, bad anatomy, bad hands, extra fingers, extra limbs, mutated hands, deformed face, blurry, watermark, signature, text, cropped, child, slim, skinny, symmetrical intact tusks, clean unbroken nose
  ```

---

## 3. Radek (Team Ukiyo Squad Leader & Heavy Tactician)
- **Role & Lorebook:** Index 8, `FINAL/Svartulfr_NPC_Primary.json`, ID `T-11cZKiuLPINjkJwyiQ0`.
- **Species & Archetype:** Orc veteran, tactician and squad leader.
- **Positive Prompt:**
  ```text
  masterpiece, best quality, ultra-detailed, semi-realistic, painterly realism, anime-inspired realism, premium visual novel art, luxury visual storytelling, niji style, natural anatomy, highly detailed face, expressive eyes, soft facial rendering, healthy vibrant skin tone, emotional realism,

  1man, solo, male, 31 years old, orc veteran, squad leader, colossal dense muscle build, weathered deep olive-grey skin, battle-tested presence, jet-black undercut with a thick Viking-style top-braid falling over shoulder, piercing luminous amber-gold eyes, chipped left ivory tusk, sharp vertical scar cutting through right eyebrow, forearm tattoos displaying intricate dungeon topographical maps, stern thoughtful tactical expression,

  wearing high-grade tactical carbon-fiber chest plate over rugged dark combat under-armor, heavy reinforced shoulder pauldrons, leather tactical straps, massive custom steel cleaver-greatsword strapped to back harness,

  tactical command room inside a modern dungeon shelter, holographic tactical map table reflecting cyan and amber light onto armor, cinematic lighting, gritty high-fantasy realism
  ```
- **Negative Prompt:**
  ```text
  lowres, worst quality, low quality, bad anatomy, bad hands, extra fingers, extra limbs, mutated hands, deformed face, blurry, watermark, signature, text, cropped, child, scrawny, clean unmarked skin, wild undisciplined hair
  ```

---

## 4. Eric (SUCC Undergrad & Demihuman Fox Musician)
- **Role & Lorebook:** Index 12, `FINAL/Svartulfr_NPC_Primary.json`, ID `9vQ1lK3sbRRj_I6aIsX4m`.
- **Species & Archetype:** Fox Demihuman (Kitsune subtype), SUCC undergrad student and indie band guitarist.
- **Positive Prompt:**
  ```text
  masterpiece, best quality, ultra-detailed, semi-realistic, painterly realism, anime-inspired realism, premium visual novel art, luxury visual storytelling, niji style, natural anatomy, highly detailed face, expressive eyes, soft facial rendering, healthy vibrant skin tone, emotional realism,

  1boy, solo, male, 20 years old, fox demihuman, kitsune traits, single pair of fluffy russet fox ears atop head, fluffy russet fox tail, slender skinny tall build, pale skin with light freckles dusted across nose and cheeks, messy short dark hair with deep teal-green tinted highlights, expressive warm hazel eyes, silver lip ring piercing on lower lip, silver tongue stud, silver gauges in fox ears, multi-pierced fox ear cartilage, detailed black ink dragon tattoo wrapping along neck and down collarbone,

  wearing oversized distressed white streetwear t-shirt, layered silver chain necklaces, loose dark denim jeans, guitar pick necklace,

  indie band rehearsal garage, vintage amplifiers, neon magenta and turquoise stage wash lighting, casual college student vibe, warm California evening atmosphere
  ```
- **Negative Prompt:**
  ```text
  lowres, worst quality, low quality, bad anatomy, bad hands, extra fingers, extra limbs, mutated hands, deformed face, blurry, watermark, signature, text, cropped, child, human ears, two sets of ears, four ears, dog ears, wolf ears, muscular bodybuilder
  ```

---

## 5. Javier Reyes (SUCC Film Student & Demihuman Owl)
- **Role & Lorebook:** Index 13, `FINAL/Svartulfr_NPC_Primary.json`, ID `_riI9AvE7q6mY5-8jaVaw`.
- **Species & Archetype:** Owl Demihuman (Avian subtype), SUCC undergrad film major.
- **Positive Prompt:**
  ```text
  masterpiece, best quality, ultra-detailed, semi-realistic, painterly realism, anime-inspired realism, premium visual novel art, luxury visual storytelling, niji style, natural anatomy, highly detailed face, expressive eyes, soft facial rendering, healthy vibrant skin tone, emotional realism,

  1boy, solo, male, 20 years old, owl demihuman, avian traits, single pair of soft tufted feathered owl ears atop head, broad athletic build, warm golden-brown Mexican-American skin, wavy long black hair past shoulders, gentle light facial stubble along jaw, kind intelligent dark brown eyes, black-rimmed glasses pushed up on bridge of nose, subtle speckled brown and cream feathers layered along forearms, white wireless earbuds resting in ears, confident warm charming smile,

  wearing vintage blue denim jacket over clean white crewneck t-shirt, dark chinos, leather wristband, modern smartphone in hand,

  sun-drenched university campus courtyard, California palm trees, golden hour sunset backlight, architectural stone arches, warm glowing aesthetic
  ```
- **Negative Prompt:**
  ```text
  lowres, worst quality, low quality, bad anatomy, bad hands, extra fingers, extra limbs, mutated hands, deformed face, blurry, watermark, signature, text, cropped, child, human ears, four ears, full bird head, beak, wings replacing arms, full animal
  ```
