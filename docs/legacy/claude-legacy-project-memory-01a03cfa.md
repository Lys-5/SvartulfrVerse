**Purpose & context**

Lys is building *Svartúlfr | Urban*, a supernatural urban fantasy roleplay project set in Blackwood City — a werewolf-centric setting that is part of a larger cross-author collaborative universe combining three distinct settings: Underworld (Los Angeles), SUCC/Solarton (university setting), and Blackwood (Lys's own Douglas family dynasty). The project runs on **Wyvern**, a roleplay platform using the chara_card_v2 JSON spec, with character cards in **JED+ format** (hybrid of bracketed attribute blocks and prose sections).

The world centers on a werewolf billionaire dynasty (the Douglas-Bloodmoon family), college life at SUCC (Supernatural University of Central California), and a coercive supernatural biology system called **LSE (Lupine Social Ecology)**. A key narrator figure is **Wulfnic Bloodmoon** — a 1,100-year-old immortal Firstborn werewolf, now named "Wulfnic Báleygr | The Stolen Eye" (with original lore that Wulfnic stole Odin's eye before leaving Iceland, integrating with the framing of Odin as "The Betrayer"). Lys's in-world persona is **Alyssa Douglas-Bloodmoon**, the youngest twin of the dynasty, attending SUCC.

A parallel creative layer involves Italian-language roleplay configuration (universal prompt overrides for platforms like SillyTavern) and period-appropriate language for Norse cultural contexts (e.g., Old Norse affectionate terms for Alyssa addressing Wulfnic).

**Lore conflict rule (user instruction):** In any conflict between Blackwood/Douglas material and the external settings Underworld (LA) or SUCC (Solarton), the official material of the respective external setting always takes precedence.

---

**Current state**

- **Character cards built or refined:** Erik Douglas (Prime Alpha patriarch, billionaire CEO), Logan Douglas (Beta mechanic/club owner), Malachia Douglas-Bloodmoon (eldest son, underground fighter/silent enforcer). NPC reference materials for Magnus Douglas III and Elizabeth Duskwood-Douglas folded into lorebook entries.
- **Lorebook infrastructure:** External lorebook files (Underworld.json, SUCC-U-VERSE.json) converted to Wyvern chat-level lorebook schema; a mini test lorebook built for group chat testing. A canonical Wyvern schema template file is maintained and updated as new schema information is confirmed from real exports.
- **World editor fully configured:** All major Wyvern system tabs worked through — World Info, World Details, Simulation, Inline Commands, Timeline, Currency, RPG Stats, Combat, Relationships, InfoBoard, Eras, Environments, Locations, Travel Routes, and Introduction.
- **Key confirmed lore decisions:**
  - Alyssa Douglas-Bloodmoon's "Species: Human" tag is a legacy error — she is a Founding Bloodline Dominant Omega and White Moon heir.
  - Kaladin Nargathon: DCC Security Commander and Project BlackWolf veteran.
  - House Duskwood: Pureblood werewolf house, associated with grey wolves.
  - Erik's middle name: Cornelius (Magnus's choice).
  - World calendar anchored at 1 January 800 AD 00:00 as world-age 0, with seven named Eras (Age of Myth → Modern Era).
  - Six custom RPG stats: Might, Resilience (= HP), Agility, Wits, Presence (= Mana), Scent (mapped to Luck combat role); fixed 25-point stat budget regardless of level; Level = canonical age.
  - NPC dialogue in group chats prefixed with character name and colon for correct message splitting.
- **Italian-language override suite:** Four universal prompt override blocks configured (Final Instructions, Review Pass Extra Focus, Improve My Writing, Write for Me), all enforcing exclusive Italian output, prohibition of italianized English neologisms, no em dashes, consistent formatting schema, and no writing actions/dialogue for Alyssa ({{user}}). Alyssa's persona rendered in first person, present tense; {{char}} in third person, present tense.

---

**On the horizon**

- Remaining Douglas-Bloodmoon family members and key characters (e.g., Alyssa's twin, other dynasty members) likely need character cards.
- Ongoing lorebook expansion as new lore is canonized in conversation.
- Old Norse language choices for Alyssa–Wulfnic relationship dynamics (current best candidate for affectionate nickname: **Gamli**, "the old one/old man," warm and nickname-style rather than literal kin term).

---

**Key learnings & principles**

- Wyvern's `➤` marker is native attribution syntax for name + avatar rendering, not a command conflict.
- Species field in Wyvern should remain purely narrative (not stat-driven) given the large number of lycanthrope variants in this world.
- Lore errors in older files (e.g., Alyssa's species tag) should be flagged and resolved with reasoning rather than silently inherited.
- For affective/period language, nickname-style terms (e.g., *Gamli*) suit non-blood relationships better than literal kin terms; Italian diminutive suffixes (like *-ino*) carry emotional weight that needs equivalent target-language solutions.

---

**Approach & patterns**

- Lys reviews Claude's output critically before finalizing — flags discrepancies (eye color errors, mechanical looping issues, accessory over-fixation) and provides corrections conversationally rather than in structured documents.
- Prefers cards built from source files with discrepancies surfaced and resolved with explicit reasoning.
- Iterative versioning over full rebuilds; clean, paste-ready output with minimal surrounding explanation.
- Parallel rule sets across complementary override slots kept in sync for maintainability.
- New canon delivered in conversational chunks; Claude should integrate and track it across sessions.

---

**Tools & resources**

- **Platform:** Wyvern (chara_card_v2 / JED+ format)
- **Roleplay override platform:** SillyTavern or equivalent (for Italian-language universal prompt overrides)
- **Key project files referenced:** `Master_Design.md`, `World_Seed.md`, `LSE_06_History.md`, `environments.md`, `locations.md`, `world_info.md`, lorebook JSONs (Underworld.json, SUCC-U-VERSE.json, and Blackwood-specific files)
- **Language resources:** Old Norse/Icelandic for period-appropriate dialogue; Italian as primary roleplay output language

#### Modifiche alla memoria
- Progetto Svartúlfr/Blackwood-Douglas (character cards Wyvern): se emerge un conflitto di lore tra il materiale Blackwood/Douglas e le ambientazioni esterne Underworld (LA) o SUCC (Solarton), prevale sempre il materiale ufficiale della rispettiva ambientazione specifica.