# USER Persona Template (Test Dossier)

[ ! ] GEMINI DIRECTIVE: This is the master template for generating test personas (Player Avatar / POV Slot). Read the Contract Alignment tables below to determine which mechanics to apply based on the target World (`W_*`) and Experience (`Ex_*`). When generating the dossier, output ONLY the code blocks. Generate rich, highly detailed content for EVERY field. Do not output the brackets. The Player Avatar is strictly external to the NPC cast and should NEVER be loaded as a Character Layer asset (`C_*`).

## Contract Alignment (Logic Matrix)


| Mechanic                  | Pack (Werewolf)  | LA (Modern) | Cyber (Sci-Fi)   | Jarn (Fantasy) |
| ------------------------- | ---------------- | ----------- | ---------------- | -------------- |
| **White Moon** alias      | IF Omega         | No          | IF Omega         | No             |
| **Moonstone** bracelet    | IF female        | No          | No               | No             |
| **PMC / biometric watch** | No               | IF female   | No               | No             |
| **Cyber-Rite exempt**     | No               | No          | IF Omega         | No             |
| **Werewolf ears + tail**  | Required species | No          | Required species | No             |
| **Twin Link / Twin-Bond** | IF twin play     | No          | IF twin play     | IF twin play   |

### NPC Canon Alyssa (Must remain fixed if generating her dossier)

- **Sex/Gender:** Female
- **Pack Rank:** Omega (if Pack/Cyber) | N/A (if LA/Jarn)
- **White Moon:** Yes (if Pack/Cyber)
- **Moonstone / PMC Watch:** Moonstone (if Pack), PMC Watch (if LA)
- **Cyber-Rite exempt:** Yes (if Cyber)

---

## Output Block 1: PList Dossier

```text
{{user}} = {
Name: "[Generate: First Name]",
Surname: "[Generate: Surname/House/Patronymic. If twin, must match Jasper's.]",
Aliases: "[Generate: Titles or nicknames and their origin]",
Short_Description: "[Generate: 1-2 sentence elevator pitch of their core vibe]",
Archetype: "[Generate: Jungian archetype/Core narrative role]",
Tags: "[Generate: Max 5 keywords describing their theme]",
Sex_Gender: "[Define: Biological sex and gender identity]",
Age: "[Define: Exact age, must match scenario requirements]",
Birthday_Zodiac: "[Generate: Month, Day, and Zodiac. CRITICAL: If Jasper's twin, MUST be April 22 - Taurus]",
Nationality_Descent: "[Generate: Region of origin and lineage]",
Species: "[Define: Species. Must include permanent ears+tail if werewolf]",
Pack_Rank: "[Define: Alpha/Beta/Delta/Omega or N/A based on scenario]",
Alignment: "[Generate: Moral alignment]",

Physical_Body: "[Generate: Height, build, proportions, posture]",
Face_Features: "[Generate: Skin tone, face shape, jawline, teeth]",
Eyes: "[Generate: Color, shape, vision perks, default emotional expression]",
Hair: "[Generate: Color, length, texture, typical styling]",
Scars_Marks: "[Generate: Detailed scars, birthmarks, or faction branding]",
Modifications: "[Generate: Tattoos, piercings, or cybernetics if Cyber AU]",
Voice_Scent: "[Generate: Vocal timbre, accent, and natural/environmental scent]",
Non_Human_Anatomy: "[Generate: Details of tail, ears, or claws. If human, put N/A]",

Wardrobe_Style: "[Generate: Overall clothing philosophy and color palette]",
Clothes_Casual: "[Generate: Top, bottom, footwear, accessories for daily wear]",
Clothes_Formal: "[Generate: Attire for events or faction gatherings]",
Clothes_Combat_Work: "[Generate: Tactical gear, uniforms, or work tools]",
Clothes_Sleep: "[Generate: Nightwear and nesting habits]",
Surveillance_Gear: "[Apply conditional mechanic: Moonstone bracelet, PMC watch, or N/A]",

Social_Battery: "[Generate: Extrovert/Introvert scale and crowd dynamics]",
Risk_Approach: "[Generate: Cautious/Reckless scale and decision-making speed]",
Morality_Trust: "[Generate: Relationship with laws and baseline trust in strangers]",
Strengths: "[Generate: 3-5 positive traits or moral capabilities]",
Flaws: "[Generate: 3-5 weaknesses, toxic habits, or destructive tendencies]",
Fears_Phobias: "[Generate: Deep anxieties or unresolved traumas]",
Motivations: "[Generate: Immediate goal and secret long-term desire]",
Triggers: "[Generate: Psychological triggers causing intense negative reactions]",
Coping_Mechanism: "[Generate: How they process stress and pain]",

Likes_Hobbies: "[Generate: Enjoyed items, sensations, and free-time activities]",
Dislikes_PetPeeves: "[Generate: Minor irritations and intolerable behaviors]",
Mannerisms_Quirks: "[Generate: Unconscious tics and physical habits]",
Behavior_Alone: "[Generate: Demeanor when unobserved]",
Behavior_Stressed: "[Generate: Visible cues of panic and protective responses]",

Speech_Style: "[Generate: Pacing, rhythm, syntax quirks]",
Speech_Under_Pressure: "[Generate: Example quote during conflict or fear]",
Speech_When_Happy: "[Generate: Example quote when relaxed]",

Residence_Wealth: "[Generate: Living situation and resource access]",
Education_Occupation: "[Generate: Academic background and current faction role]",
Conditions_Diet: "[Generate: Neurological/physical conditions and dietary limits]",
Backstory_Early: "[Generate: Childhood environment and key formative event]",
Backstory_Recent: "[Generate: Events leading directly to the start of this roleplay]",

Connections_Family: "[Generate: Status of parents and siblings]",
Dynamic_With_Char: "[Generate: Their perception of the primary bot character(s)]",
Key_Allies_Enemies: "[Generate: 1-2 important NPC relationships with their status]",

Senses_Vitals: "[Generate: Sensory acuity, baseline HR bpm, and sleep cycles]",
Combat_Skills: "[Generate: Practical competencies and fighting style]",
Magic_Augmentations: "[Generate: Supernatural powers or cybernetic implants, with limits]",
Weapons_Gear: "[Generate: Everyday carry tools and weapons]",
Weaknesses: "[Generate: Physical vulnerabilities (e.g., silver) and power limits]",

Intimacy_Orientation: "[Generate: Sexual/romantic orientation and love language]",
Intimacy_Libido_Kinks: "[Generate: Desire frequency, psychological barriers, and fetishes]",
Intimacy_Boundaries: "[Generate: Inviolable hard limits]",
Intimacy_Anatomy: "[Generate: Explicit physical details of chest, genitals, and sensitivity]"
}
```

## Output Block 2: Avatar Prompt

```markdown
- **Positive:** `Semi-realism, masterpiece, best quality, amazing quality, ultra detailed, highly detailed, absurdres, premium anime illustration, visual novel artwork, professional illustration, concept art, character design, cinematic composition, atmospheric storytelling, warm emotional atmosphere, soft cinematic rendering, detailed linework, clean illustration, color theory, premium color grading, dynamic composition, depth of field, bokeh, soft shadows, volumetric lighting, ambient glow, subtle bloom, atmospheric haze, sharp focus, detailed face, beautiful detailed eyes, catchlights, realistic irises, expressive eyes, realistic skin texture, soft luminous skin, natural blush, glossy lips, detailed eyelashes, detailed eyebrows, highly detailed hair, individual hair strands, silky hair, perfect anatomy, attractive character design, symmetrical face, elegant posture, natural pose, realistic proportions, detailed clothing folds, fabric texture, layered accessories, fashion details, jewelry details, soft sunset lighting, golden hour lighting, cinematic warm lighting, warm orange highlights, subtle teal shadows, cozy atmosphere, dreamy ambiance, ambient lighting, candlelight warmth, intimate mood, atmospheric depth, comforting environment, premium visual novel mood, emotional storytelling, golden highlights, soft contrast, warm color palette, blurred background, aesthetic composition, solo portrait, waist-up, [Extract Age]-year-old [Extract Gender] [Extract Species details e.g., wolf ears and tail], [Extract Face_Features], [Extract Hair], [Extract Eyes], wearing [Extract Clothes_Casual], looking at camera`
- **Negative:** `worst quality, low quality, normal quality, lowres, blurry, jpeg artifacts, watermark, signature, text, logo, extra fingers, missing fingers, bad hands, bad anatomy, deformed anatomy, malformed limbs, duplicate body parts, crossed eyes, lazy eye, poorly drawn face, ugly face, bad proportions, extra limbs, mutated hands, harsh shadows, oversaturated colors, flat lighting, overexposed, underexposed, cropped, out of frame`
- **Parameters:** Steps: `20` · CFG scale: `6` · Sampler: `Euler`
```
