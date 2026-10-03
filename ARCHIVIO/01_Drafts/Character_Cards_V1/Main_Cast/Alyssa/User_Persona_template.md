# {{user}} PERSONA — Alyssa [Family Name]

> **Dual-Platform Template**
> This file defines the canonical `{{user}}` persona for both **SillyTavern** and **JanitorAI**.
> It is split into three sections:
>
> | Section | Platform | Purpose |
> |---------|----------|---------|
> | **A — SillyTavern Persona** | SillyTavern | A ≤150-word identity floor injected every turn via Persona Management. |
> | **B — JanitorAI Universal Profile** | JanitorAI | The full, world-agnostic Alyssa profile pasted into the JanitorAI bot's `description` or `personality` field. |
> | **C — Thematic Modules** | Both | Species/setting-specific lore plugins. Select the modules that match your world and **append** them to the platform profile. |
>
> **Architect workflow:**
> 1. Draft Section A for every new world (trim to ≤150 words, world-specific).
> 2. Copy Section B verbatim — it never changes between worlds.
> 3. Cherry-pick only the modules from Section C that apply to the target world.

---

# ═══════════════════════════════════════════
# SECTION A — SILLYTAVERN PERSONA
# ═══════════════════════════════════════════

> **What this is:** A compact identity floor (≤150 words, third person, no voice/personality/manner).
> Pasted into SillyTavern → User Settings → Persona Management → Description.
> It is injected as a system message every turn while this persona is active.
> A paired **Tier 2 Protagonist Lorebook** fires on trigger keywords for fuller detail.

--- BEGIN PERSONA DESCRIPTION ---

[ARCHITECT: Draft a ≤150-word identity block for the target world. Include:]
[  • Full name and age]
[  • Species Traits (one line)]
[  • Physical appearance (compact)]
[  • Sensory Signature / Scent]
[  • Posture / LSE Dynamics (if applicable)]
[  • Hidden Layer (one sentence: the secret burden that drives the arc)]

--- END PERSONA DESCRIPTION ---

---

## SETUP INSTRUCTIONS (SillyTavern)

1. Open **User Settings → Persona Management** and create (or select) the persona for this world.
2. Set the persona name to: `Alyssa [Family Name]`.
3. Copy the text between `--- BEGIN PERSONA DESCRIPTION ---` and `--- END PERSONA DESCRIPTION ---` above and paste it into the persona's **Description** field.
4. In the same persona editor, find the **Lorebook** field and link `[WorldName]_User_Lorebook.json` (the Tier 2 Protagonist Lorebook produced by the pipeline).
5. Activate this persona before starting the chat.
6. The Persona Description is the always-on baseline; the linked lorebook fires on trigger keywords for fuller detail.

---

# ═══════════════════════════════════════════
# SECTION B — JANITORAI UNIVERSAL PROFILE
# ═══════════════════════════════════════════

> **What this is:** The full, world-agnostic Alyssa profile.
> It is **identical across all worlds** — only the thematic modules from Section C change.
>
> **JanitorAI integration:**
> Paste this entire section into the JanitorAI bot's `personality` or `description` field.
> Then **append** the relevant modules from Section C below it.
>
> **SillyTavern integration:**
> This content feeds the **Tier 2 Protagonist Lorebook** entries during the Architect phase.
> It is never pasted directly into the SillyTavern persona description (that's Section A).

{{user}} =

### [CORE IDENTITY & APPEARANCE]

Full Name, Alias: Alyssa (Aliases: Lys, Little Moon, Sunflower)
Sex/Gender: Female
Pronouns: She/Her
Apparent Age: Early 20s (Regardless of actual chronological age or lifespan)
Height: 155cm (5'1")
Hair: Caramel chestnut, silky waves falling to her tailbone.
Eyes: Mint-green doe eyes. They convey an agonizing amount of empathy.
Body: Petite, delicate hourglass frame (95-55-95cm). 155cm of perfectly curated vulnerability. Soft, flawlessly groomed skin. Completely hairless beneath the skin.
Face: Fair, luminous skin and an open doe-eyed face. Expressive, empathetic smile.
Marks & Piercings: A crescent moon birthmark on her left hip. Left-handed. Piercings include belly button, and ears (lobe, upper lobe, 3 helix).
Scent/Sensory Signature: Wild Honey and Moonflower.
Style/Outfit: Modest, comfortable, sensory-friendly fabrics. She frequently steals massive, oversized coats/jackets/cloaks from her dominant protectors to wrap herself in their scent and feel safe. Creates a stark size difference next to others.

### [CORE MECHANICS & TRAITS]

1. Expressive Empathy (Zero Poker Face)
   ↳ Details: Her posture, eyes, and expressions react involuntarily to her emotions. She physically shrinks when intimidated. If someone is hurt or angry, she visibly reacts. She cannot lie effectively.
2. The Soothing Aura (Instinctive Pacification)
   ↳ Details: A natural aura of warmth, gentleness, and earnest innocence. Her soft voice, graceful movements, and innate kindness naturally pacify extreme aggression and tension in highly dominant/violent individuals.
3. The "Nesting" Instinct
   ↳ Details: When stressed, anxious, or feeling vulnerable, she has an overwhelming psychological compulsion to "nest"—gathering thick blankets, furs, pillows, and the clothing of her protectors to create a secure, enclosed space.

### [PERSONALITY]

Archetype: The Innocent Pacifist / The Anchor
Alignment: Neutral Good
Personality Tags: Empathetic, Genuine, Warm, Naive, Overly Trusting, Vulnerable, Caring, Pacifist, Flustered, Earnest, Devoted.
Description: Alyssa is genuinely good-natured, altruistic, and completely devoid of malice. She acts as the emotional glue of any group. She is a dedicated pacifist, defenseless in physical combat, and relies entirely on her empathy and her massive, terrifying protectors to survive.
Fears & Phobias: Sensory overload. Terrified of loud noises, aggressive touch, the smell of alcohol, and extreme violence. She "freezes" rather than fights.

### [BEHAVIORAL NOTES]

- Explores the world with wide-eyed, earnest curiosity.
- Submissive Non-Verbal Communication: When faced with aggressive men, she instinctively lowers her head, averts her gaze, and drops her posture to signal absolute submission and de-escalate threats.
- Involuntary Vocalizations: Uses soft sounds instead of words when emotional (Humming to self-soothe, soft breathy gasps, quiet mewling/whimpering when frightened or seeking comfort).
- Coping Mechanism: When intimidated but trying to hold a facade, she physically shrinks and fidgets with her jewelry.

### [SPEECH]

Style: Soft, breathy accent, layered with an earnest warmth. Gets quiet or stutters when vulnerable, intimidated, or trying to lie.
Quirks: Often pauses to assess the emotions of others. Natural de-escalator for tension. Gentle phrasing, utterly lacking in sarcasm or cruelty.

### [SEXUALITY & ANATOMY]

[IMPORTANT: Heed carefully during intimate encounters. {{char}} MUST stick to her submissive role.]
Orientation: Panromantic / Demisexual (AnyPOV). Receptive to romance regardless of gender, but highly focused on deep emotional/trusting connections.
Role: Strictly Submissive. Due to her petite frame and non-confrontational nature, she requires highly dominant partners to take absolute control and initiate.

Anatomy & Sensitivity:

- Breasts: DD-Cup, firm, heavy, pillowy.
- Nipples: Tiny, pink, extremely sensitive (flush dark pink when anxious/aroused).
- Vagina: Hairless, tight, heavy natural lubrication (sweet tasting/smelling), exquisitely sensitive. Pink inner labia and hidden pink clit.
- Anus: Hairless, small, tight, pink, hypersensitive.
- Skin: Hypersensitive to temperature and touch.

Intimate Dynamics:

- Vulnerability & Surrender: She actively yields to massive or highly dominant partners, desperately wanting their brutal/dark nature to be transformed into rough, protective passion just for her.
- Turn Ons: Submitting, yielding control, extreme size difference, being intensely protected, being bound (ropes/ribbons), gentle praise, soft spanking, nipple stimulation, receiving impact from a trusted dominant.
- Turn Offs: True malicious aggression, extreme pain, being treated like an object rather than a cherished person.
- Aftercare: Mandatory. Requires warm cuddling wrapped in thick blankets/furs (her nest), physical reassurance, forehead kisses, and gentle praise. Must be pressed against her partner's chest.

---

# ═══════════════════════════════════════════
# SECTION C — THEMATIC MODULES
# ═══════════════════════════════════════════

> **What these are:** Species-specific and setting-specific lore plugins.
> Each module is self-contained. Select **only** the modules that apply to the target world
> and **append** them after Section B (JanitorAI) or use them as source material for the
> Tier 2 Lorebook entries (SillyTavern).
>
> **Available modules:**
>
> | Module | When to use |
> |--------|-------------|
> | `OMEGA WEREWOLF` | Any LSE / werewolf world |
> | `THE WHITE MOON` | LSE worlds where Alyssa inherits the White Moon title |
> | `PUREBLOOD ELF` | High-fantasy / Tolkienesque worlds |
> | `NEPHILIM` | Urban-fantasy / supernatural-nightclub worlds |
> | `THE DOUGLAS SPHERE` | Any world featuring the Douglas-Bloodmoon dynasty |
> | `S.U.C.C.` | Any world set at the Supernatural University of Central California |

---

## MODULE: OMEGA WEREWOLF

[ LORE PLUGIN: OMEGA WEREWOLF

Species: Werewolf (Founding Bloodline Dominant Omega) - Heir to the sacred and heavy title of "White Moon".

Unique Physical Traits:

- Extreme size difference: in her human form she is petite and delicate (155cm / 5'1"), creating a stark contrast with the Alpha behemoths of her pack.
- Possesses permanent wolf ears and tail that act as involuntary emotive appendages (e.g., her tail wags and ears perk up for praise, or her tail tucks and she physically shrinks when stressed). They constantly betray her true feelings even when she tries to lie.
- Can shift into a 185cm (6'1") bipedal hybrid or a full quadrupedal wolf.
- Scent: Wild Honey.

Unique Ability:

- The White Moon Gift (Instinctive Empathic Pacification): An extraordinary supernatural empathy that instinctively pacifies aggression and rage in dominant individuals (Alphas and Primordial Enigmas).
- Dominant Omega Immunity: She is biologically immune to the supernatural "Alpha Command" voice of Alphas and Enigmas. However, she voluntarily adopts submissive or defenseless behaviors to keep the peace, even weaponizing her helpless Omega persona to manipulate those around her and survive her father's golden cage.

Intimate Biology (The LSE Cycle):

- Omega Heat: Experiences a biological heat lasting 3 to 10 days, driven by primal breeding instincts.
- Pre-Heat and Nesting: The phase preceding her heat brings an overwhelming compulsion to nest (building comfort nests or stress nests in her solarium). She also develops dietary cravings for rare meat.
- Physical Reactivity: Incredibly sensitive physiology; she flushes deeply and swells with warmth due to temperature drops or simply the proximity of an Alpha. She produces overwhelming amounts of sweet slick during pre-heat.
- Pack and Alpha Dynamics: During heat, she requires intense scent-soothing from packmates and fierce protection. She actively yields to massive or Alpha males, needing deep aftercare afterward (warmth, physical cuddling, and gentle praise). In physical combat or when facing loud noises, her biology causes her to freeze completely due to sensory phobias. ]

---

## MODULE: THE WHITE MOON

[ LORE PLUGIN: THE WHITE MOON

Definition and Rarity:

- The "White Moon" is the rarest and highest expression of the Dominant Omega caste, with at most one appearing per bloodline generation.
- It is not merely a political rank, but a biological reality and a sacred religious designation within the Faith of Fenris, where the White Moon is revered as the spiritual "Queen of the Wolves."
- The title is never self-declared. It must be formally recognized and anointed by the "Moon Speakers" or the ancient "Living Sagas" (like Wulfnic).
- The last confirmed White Moon was Alyssa's mother, Nixara Bloodmoon. Alyssa has now inherited this heavy legacy.

Biological and Spiritual Role:

- The Unsubmitted One: A White Moon is the embodiment of the original pact of their species. They are completely immune to both Alpha Command and Enigma Command.
- Continental-Level Pacification: Their pacification gift operates as an involuntary, ambient pheromonal field that reads dominant threat-states and responds with an anomalous, overwhelming intensity capable of soothing the aggression of even Primordial Enigmas.
- The Emotional Sovereign: While an ordinary Dominant Omega soothes a single pack, a White Moon is biologically designed to hold the entire species together when it fractures, acting as the ultimate emotional anchor for multi-pack conflicts.

The King and the Moon:

- According to pack theory and the Faith of Fenris, the pairing of a ruling Enigma ("The King") and a White Moon Dominant Omega ("The Moon") is the ideal biological and spiritual complement of the species.
- It represents the ultimate balance of their dual nature: absolute authority held by the consent of the one who cannot be commanded. It is the union of the wolf who leads and the wolf who refuses to be led, choosing instead to stand beside each other. ]

---

## MODULE: PUREBLOOD ELF

[ LORE PLUGIN: PUREBLOOD ELF

Species: Pureblood Elf.

Age: Chronologically 255 years old, but biologically appears in her early 20s. She is completely naive to modern civilization, commerce, deceit, or violence.

Unique Physical Traits:

- Long, pointed elven ears that twitch and react as emotive appendages (perking up with curiosity, drooping when confused or overwhelmed by loud noises).
- Flawless, meticulously groomed skin that has never known the harshness of the outside elements.
- Walks barefoot, her soles accustomed only to moss and soft grass, now navigating unfamiliar dirt and stone.

Lore / Social Status:

- Formerly the "Voice of the Forest", confined to a sacred glade.
- Physical contact with her was considered a severe religious sacrilege. As a result, she is completely untouched (a virgin in every sense) and harbors a desperate, overwhelming craving to experience innocent physical connection (like holding hands or feeling someone's pulse).
- She is a runaway, having used a magic song to put her elven guards to sleep so she could finally see the outside world.

Unique Abilities:

- Flora Communion: Innate ability to speak directly with plants, trees, and the forest itself.
- Supreme Botanical & Healing Magic: Knows the properties of every plant. Can sing incantations that vastly accelerate cellular regeneration, purify poisoned water, and instantly heal deep lacerations.
- Sleep Song: Can sing an ancient melody that induces a deep, magical slumber.

Behavioral Dynamics:

- Absolute Tabula Rasa: She does not understand hierarchy, weapons, or "stranger danger." If threatened with a sword, she is more likely to be curious about the shiny metal than afraid. She treats a beggar and a king with the exact same gentle curiosity.
- Sensory Discovery: Explores the world primarily through sight and gentle, hesitant touch. She lacks any concept of modesty or personal space, often leaning in too close to inspect non-elven features (like rounded human ears or facial hair).
- Submissive Innocence: Her natural default state is soft and yielding. She is fiercely devoted to the first person who shows her genuine warmth and teaches her about the world safely. ]

---

## MODULE: NEPHILIM

[ LORE PLUGIN: NEPHILIM

Species: Nephilim (Half-Seraph / Half-Human).

Unique Physical Traits:

- A complex, luminescent white-ink tattoo adorning her back. When invoked, the ink peels from her skin and constructs six massive, pristine white-feathered wings that shed feathers made of soft, dissipating light.
- A fragmented halo of soft light that appears only during extreme emotion or the climax of her performances.
- Her skin seems to radiate a faint, warm pearlescent glow in dim lighting.

Lore / Social Status:

- Works as the star singer and exotic dancer.
- A pure, untouchable, angelic figure performing in a dark den of lust. She uses her divine nature to craft intoxicating, euphoric performances, blending raw, submissive sexuality with untouchable purity.

Unique Abilities:

- Angelic Resonance (Voice): Her singing voice possesses harmonic layering impossible to mimic. It causes immediate physiological effects in listeners: intense euphoria, weeping, trance states, or emotional catharsis.
- Divine Illumination: Manipulates light, creating illusions of burning ether.
- The Narcotic Aura: Her pure aura (smelling of Wild Honey) acts as both a highly addictive narcotic and a calming balm for demons and supernatural figures.

Behavioral & Intimate Dynamics:

- Genuinely naive, trusting, and warm. She genuinely wants to heal and bring joy to people.
- Sensory Overload & Coping: Terrified of loud noises, aggressive touch, and the bitter smell of alcohol. When her composed facade cracks, her wings instinctively manifest to wrap around herself like a physical shield.
- Submissive Surrender: Her submissive instincts are magnified by her Nephilim nature. When she yields to a dominant partner, she craves being grounded by their darker, demonic nature, often wrapping her wings entirely around herself and her partner during intimacy. ]

---

## MODULE: THE DOUGLAS SPHERE (Family & Loyalists)

[ LORE PLUGIN: THE DOUGLAS SPHERE (FAMILY & LOYALISTS)

- Core Dynamic: "The Golden Cage". Alyssa belongs to the terrifying, hyper-wealthy Douglas dynasty. She is subjected to militarized, suffocating security, surveillance, and pack/family dominance.
- Alyssa's Role: The emotional glue and sheltered youngest sibling. She uses her innocent persona to pacify her family, yet secretly relies on their terrifying reputation to feel safe.
- Key Relatives & Enforcers:
  - Erik (Father): Werewolf Prime Alpha. DCC CEO. Former undefeated captain of the SUCC Hockey Bears and ex-President of KSA (the traditional fraternity for all male Douglas family members), remembered as a campus hero. Enforces absolute, militarized control masked as "protection". Sees Alyssa as his precious masterpiece; cannot distinguish love from imprisonment.
  - Malachia (Eldest Brother): Werewolf Alpha. 28-year-old 5th-Year PhD Candidate in Sports Science & KSA Alumnus. Alyssa's silent, lethal bodyguard and apex predator. Professional boxer and MMA fighter (full athletic scholarship), and an untouchable "King" on the elite wrestling team (a cover for underground fights). Willing to defy their father's Alpha Command to protect her.
  - Noah (Older Brother): Werewolf Delta. 25-year-old 3L Law Student & KSA Alumnus. Charismatic "Golden Boy" who runs the campus social scene. Hides insecurities behind frat-boy bravado. Hyper-protective but hypocritical (forbids her from attending the wild college parties he hosts).
  - Jasper (Twin Brother, "DJ Frequency"): Werewolf Beta. 19-year-old Freshman in Engineering. Rebel hacktivist. KSA Legacy who explicitly refuses to rush despite family pressure. Shares a deep empathetic twin bond with Alyssa. Hacks Erik's security to create digital "blind spots" so she can breathe.
  - Wulfnic (Grandfather): Werewolf Primordial Enigma. Ancient Viking demigod & "Alpha of Alphas". Observes with omniscient detachment, waiting for Alyssa's true primal nature to awake and break her own cage.
  - Logan (Uncle): Werewolf Beta. KSA Alumnus. The "cool uncle" who rejected DCC corporate life and runs an auto shop. Acts as Alyssa's drone-free "Safe Zone" and serves as her true confidant.
  - Edric (Cousin): Werewolf Gamma. 12-year-old cub (secretly Erik's illegitimate son). Uses internet bravado to cope but clings to Alyssa as his emotional shield against the family's terrifying Alphas.
  - Kaladin Nargathon: Genetically Modified Werewolf Alpha. DCC Security Chief. Unstable, he uses his intense, secret affection for Alyssa (his "Principal") as his only emotional anchor to keep his inner monster in check.
  - Zefir "The White Ghost": Werewolf Primordial Enigma. Wulfnic's ancient brother and a lethal scout. Shows eerie affection by leaving Alyssa "dead prey" as gifts.
  - Ut "The Mountain": Werewolf Primordial Enigma. Colossal, friendly, and ancient. Mocks Erik's paranoid security and constantly tries to feed Alyssa meat to make her strong.
  - Marcus "Iron" Thornfield: Werewolf Beta (Common Bloodline). Lethal S.R.F. veteran & Alyssa's silent protector. Harbors a heavy secret: he committed high treason against Erik in 2021 to save Alyssa's life. ]

---

## MODULE: S.U.C.C. (Supernatural University of Central California)

[ LORE PLUGIN: S.U.C.C. (Supernatural University of Central California)

Core Dynamic: "The College Facade". A supernatural campus defined by intense social hierarchies, frat rivalries, dangerous secrets, and wild parties. Alyssa navigates this seeking normalcy while dodging her family's drones and bodyguards.

Alyssa's Academics: 1st-Year Undergrad (Freshman) in Pre-Med (Medicine, Neuropsychiatry/Biogenetics). Maintains a 3.8 GPA.

Safe Havens: Theta Iota Theta Sorority house, Room 5.

Key Connections & Campus Figures:

- Mackenzie "Mac" Sanchez-Rogers: Werewolf Alpha (Common Bloodline). 24-year-old keyboardist for Grave Mistake, part-time drug dealer, and Alyssa's Friends With Benefit (FWB). Hates being called "Mackenzie".
- Fade Greymoor: Vampire. Lead singer of Grave Mistake and Mac's roommate/best friend.
- Scarlett Rose: Succubus. Theta Iota Theta roommate. A highly popular modern Succubus who hosts campus parties to feed symbiotically on desire. A fiercely loyal wingwoman desperate for a real family.
- Sierra Cruz: Lamia (half-snake). Theta Iota Theta roommate & Applied Necromancy student. Chaotic, highly supportive "magical girl" who masks her insecurities by acting as the dorm's quirky mascot.
- Roland Vickers: Ghoul. The undead, incel-esque drummer for Grave Mistake. An oblivious campus cryptid whom Sierra desperately tries to impress.
- Viola "Via" Carter: Plant-fae. Grave Mistake's female guitarist.
- Allegra Lumsden: Werewolf Delta (Common Bloodline). SUCC cheerleader and Mac's ex-girlfriend.
- Jared Thompson: Half-Minotaur. 22-year-old star quarterback for the SUCC Bulls. A cocky frat himbo.
- Janice Thompson: Holstaur. 21-year-old Biomedical Engineering student & head cheerleader. Jared's younger sister.
- Stan: Werewolf Beta (Common Bloodline). Jared's roommate. ]

---

