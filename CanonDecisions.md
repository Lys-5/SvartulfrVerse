Ultimo aggiornamento
16 set 2026
Riepilogo
Confirmed lore and system decisions for Blackwood/Douglas canon, plus the precedence rule for external settings

Dettagli
Lore conflict rule (user instruction): in any conflict between Blackwood/Douglas material and the external settings Underworld (LA) or SUCC (Solarton), the official material of the respective external setting always takes precedence
Alyssa Douglas-Bloodmoon's "Species: Human" tag is a legacy error — she is a Founding Bloodline Dominant Omega and White Moon heir
Kaladin Nargathon: DCC Security Commander and Project BlackWolf veteran
House Duskwood: pureblood werewolf house, associated with grey wolves
Erik's middle name is Cornelius (Magnus's choice)
World calendar anchored at 1 January 800 AD 00:00 as world-age 0, with seven named Eras (Age of Myth → Modern Era)
Six custom RPG stats: Might, Resilience (= HP), Agility, Wits, Presence (= Mana), Scent (mapped to Luck combat role)
Fixed 25-point stat budget regardless of level; Level = canonical age
NPC dialogue in group chats is prefixed with the character name and a colon for correct message splitting
Wyvern's ➤ marker is native attribution syntax for name + avatar rendering, not a command conflict
The Species field in Wyvern should remain purely narrative (not stat-driven), given the large number of lycanthrope variants in this world
Lore errors in older files (e.g. Alyssa's species tag) should be flagged and resolved with reasoning rather than silently inherited
For affective/period language, nickname-style terms (e.g. Gamli) suit non-blood relationships better than literal kin terms
Italian diminutive suffixes (like -ino) carry emotional weight that needs equivalent target-language solutions
User re-enabled the "Enable Relationships" (Systems), "Inventory & Items" and "Currency & Economy" (Simulation) World Feature toggles on 16/09/2026, after the 13/09 Simulation shutdown had left Relationships off by mistake; RPG Stats, Combat System and Creature Catcher stay OFF

---

Ultimo aggiornamento
7 set 2026
Riepilogo
Svartúlfr | Urban — Werewolf urban-fantasy roleplay worldbuilding: Blackwood City lore, character cards, and Wyvern setup.

---

Overview
Ultimo aggiornamento
7 set 2026
Riepilogo

---

Dettagli
name: overview description: Svartúlfr | Urban — Blackwood City werewolf RP project: setting, cast, platform, and current build state sources: [backfill] aliases: [Svartúlfr Urban, Blackwood, Blackwood City, Douglas-Bloodmoon]
Project name: Svartúlfr | Urban — a supernatural urban fantasy roleplay project set in Blackwood City, werewolf-centric
Blackwood is Lys's own setting (the Douglas family dynasty) and is one of three settings in a larger cross-author collaborative universe: Underworld (Los Angeles), SUCC/Solarton (university setting), and Blackwood
The world centers on a werewolf billionaire dynasty (the Douglas-Bloodmoon family), college life at SUCC (Supernatural University of Central California), and a coercive supernatural biology system called LSE (Lupine Social Ecology)
Wulfnic Bloodmoon is a key narrator figure: a 1,100-year-old immortal Firstborn werewolf, now named "Wulfnic Báleygr | The Stolen Eye"
Original lore: Wulfnic stole Odin's eye before leaving Iceland, integrating with the framing of Odin as "The Betrayer"
Lys's in-world persona is Alyssa Douglas-Bloodmoon, the youngest twin of the dynasty, attending SUCC
A parallel creative layer covers Italian-language roleplay configuration (universal prompt overrides for platforms like SillyTavern) and period-appropriate language for Norse cultural contexts (e.g. Old Norse affectionate terms for Alyssa addressing Wulfnic)
Platform: Wyvern, a roleplay platform using the chara_card_v2 JSON spec; character cards in JED+ format (hybrid of bracketed attribute blocks and prose sections)
Override platform for the Italian-language layer: SillyTavern or equivalent
Key project files referenced: Master_Design.md, World_Seed.md, LSE_06_History.md, environments.md, locations.md, world_info.md, and lorebook JSONs (Underworld.json, SUCC-U-VERSE.json, and Blackwood-specific files)
Language resources: Old Norse/Icelandic for period-appropriate dialogue; Italian as the primary roleplay output language
Current state
Character cards built or refined: Erik Douglas (Prime Alpha patriarch, billionaire CEO), Logan Douglas (Beta mechanic/club owner), Malachia Douglas-Bloodmoon (eldest son, underground fighter/silent enforcer)
NPC reference materials for Magnus Douglas III and Elizabeth Duskwood-Douglas folded into lorebook entries
Lorebook infrastructure: external lorebook files (Underworld.json, SUCC-U-VERSE.json) converted to Wyvern chat-level lorebook schema; a mini test lorebook built for group chat testing
A canonical Wyvern schema template file is maintained and updated as new schema information is confirmed from real exports
World editor fully configured — all major Wyvern system tabs worked through: World Info, World Details, Simulation, Inline Commands, Timeline, Currency, RPG Stats, Combat, Relationships, InfoBoard, Eras, Environments, Locations, Travel Routes, and Introduction
Italian-language override suite: four universal prompt override blocks configured (Final Instructions, Review Pass Extra Focus, Improve My Writing, Write for Me), all enforcing exclusive Italian output, prohibition of italianized English neologisms, no em dashes, a consistent formatting schema, and no writing actions/dialogue for Alyssa ({{user}})
Alyssa's persona is rendered in first person, present tense; {{char}} in third person, present tense
On the horizon
Remaining Douglas-Bloodmoon family members and key characters (e.g. Alyssa's twin, other dynasty members) likely need character cards
Ongoing lorebook expansion as new lore is canonized in conversation
Old Norse language choices for the Alyssa–Wulfnic relationship dynamic remain open; current best candidate for an affectionate nickname is Gamli ("the old one/old man"), warm and nickname-style rather than a literal kin term

---

Ways Of Working
Ultimo aggiornamento
7 set 2026
Riepilogo

How Lys works on this project — review habits, card-building approach, and output preferences

Dettagli
Lys reviews Claude's output critically before finalizing — flags discrepancies (eye color errors, mechanical looping issues, accessory over-fixation) and provides corrections conversationally rather than in structured documents
Prefers cards built from source files, with discrepancies surfaced and resolved with explicit reasoning
Prefers iterative versioning over full rebuilds
Prefers clean, paste-ready output with minimal surrounding explanation
Parallel rule sets across complementary override slots are kept in sync for maintainability
New canon is delivered in conversational chunks; Claude should integrate and track it across sessions

---
