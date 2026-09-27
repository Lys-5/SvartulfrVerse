# Worlds - Creation Guide

### A plain language guide to the Worlds feature

### World Creator Guide (WIP)

This is the home page of the WyvernChat World Creator Guide. Each chapter below covers one part of building a world — start here for orientation, then dive into the chapter most relevant to what you're working on.

### The Big Picture

When someone chats in your world, the AI reads a single block of text assembled from everything you've built. That text — called the prompt — tells the AI who it is, where the scene is set, who the characters are, and what rules to follow.

Your job as a world creator is to fill in the right pieces so that prompt is coherent and consistent. Most worlds that "don't work" are missing one or two critical pieces, or have fields in the wrong place.

Here's the order the AI reads your world:

World Overview — your "About Your World" text, always present in every message
Environment description — the broad scene context (a forest, a city district, a dungeon floor)
Location description — the specific place (a tavern room, a market stall, a prison cell)
NPC Database — full descriptions of every character who is actively in the scene
Lore injections — activated entries from your Lexicon, injected before or after the above
Chat history
Final Instructions — the last rules the AI reads before replying, including anything from your world, location, and environment
Everything else you configure determines what fills those slots and when.

### Build Order

If you're starting from scratch, build in this order. Each step depends on the previous one.

### World Info & World Details — name, overview, behavior rules

### Environments — your broad scene contexts
Locations — specific places, each linked to an environment
Characters — your NPCs, then add them to your location and environment pools
Lexicon Entries — lore, facts, background knowledge
Scenarios — entry points that drop users into a specific location and scene
Once the foundation is solid, optional RPG and economy layers can be added on top — stats and blueprints, combat, items and currencies, creatures, property and furnishings, NPC relationships, and advanced world systems like travel, InfoBoard display, world commands, and the Director AI layer. Each of these is covered in its own chapter below.

### Chapters in This Guide

World Info & Details — The public-facing listing and the AI-facing foundation: your world overview, behavior rules, formatting defaults, span depth, and NPC dialogue markers.
Environments & Locations — How to build broad scene contexts (environments) and specific places within them (locations), wire them together, and use the final-instructions stacking order to set context at multiple levels of specificity.
Characters — How to write Long Summary and Summary for your NPCs, the Pronoun Pruned Prose (PPP) writing format, outfits, speech examples, activation keys, and timeline gating. Includes the four character tiers (party, active pool, remaining pool, background) and how to use each.
Lexicon — How to build your world's knowledge base: global vs. non-global entries, position (Before Char / After Char / In Chat), activation controls (delay, sticky, cooldown, chance), and how to wire entries to environments and locations.
Timeline & Eras — The hours-based timeline system, Timeline Start Date, time-of-day periods, recurring logic (cycle and calendar), and how to gate characters, locations, environments, and lexicon entries to specific time windows.
Scenarios & Guided Intro — How to create structured entry points into your world: starting location, character pool overrides, premade and AI-generated opening scenes, and the guided intro branching system for onboarding players into complex worlds.
RPG Stats & Blueprints — How to give characters and creatures S.P.E.C.I.A.L. stats, configure stat templates, and set up the blueprint system that defines how stat-driven mechanics behave in your world.
Combat — How the turn-based RPG combat system works: d20 resolution, the four outcome tiers, initiative, status effects, and how to wire combat into your world's scenarios and locations.
Items, Currencies & Markets — How to define items, configure their use effects, set up currencies, and create shop or market systems players can interact with inside a session.
Creatures, Moves, Natures & Abilities — How to create non-humanoid NPCs (creatures) using lexicon creature entries, define move sets, assign natures that shape stat growth, and configure abilities that trigger during play.
Property & Furnishings Market — How to set up a player housing system: purchasable properties, the furnishings catalog, and how owned property and furniture are reflected in AI prompts.
Relationships & Attitudes — How NPC-to-player affinity works: persistent relationship states, moodlet-based modifiers, how authored character attitudes seed the initial relationship, and how the AI uses inline commands to shift relationship values during play.
Travel, InfoBoard, Commands & Director — Advanced world systems: travel mechanics between locations, the InfoBoard persistent display panel, world-level commands and Lua scripting, and the Director AI layer that reasons about scenes before generating responses.
Inline Chat Commands — The full reference for the built-in >command actions players (and the storyteller) type inside chat — travel, combat, money, jobs, renting, relationships, and sandbox cheats — with exactly what to set up in your world for each to work.

---

## World Info & Details

The public-facing listing and the AI-facing foundation: your world overview, behavior rules, formatting defaults, span depth, and NPC dialogue markers.

### World Info & World Details

Everything the AI knows about your world starts here — the two tabs that form your world's foundation before you build anything else.

### Where to find these tabs

Both tabs are in the left panel of the world editor: the "World Info" tab and the "World Details" tab.

### World Info tab

This is public-facing metadata. It does not affect the AI or the prompt in any way — it only affects how your world appears to users browsing the platform.

| Field                                                                                                                              | Purpose                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| World Name                                                                                                                         | What users see in search results                           |
| Description                                                                                                                        | The listing description shown on your world's browse card  |
| Avatar, Tags, Visibility, Rating                                                                                                   | Controls browsing, discoverability, and content moderation |
| World                                                                                                                              | Details tab                                                |
| This is where your world's AI foundation lives. Every field here shapes what the AI reads during every chat session in your world. |                                                            |

| Field                              | What it does                                                                                                                                                                                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| About Your World                   | The world overview paragraph. The AI reads this in every single message. Keep it focused — this is your world's elevator pitch to the AI.                                                                                                                    |
| Writing Style &                    | Tone (under Advanced Settings) Behavioral rules that apply everywhere in the world. Use this for tone, perspective rules, and content guidelines.                                                                                                            |
| Formatting                         | Rules (under Advanced Settings) World-level final instructions. These appear before environment and location instructions in the final block, so environments and locations can override them for specific contexts. Use for world-wide structural defaults. |
| Span                               | Depth (under Advanced Settings) How many recent messages are scanned to activate Lexicon entries. Default is 10. Higher means the AI can "remember" keywords further back in the conversation, but uses more processing.                                     |
| NPC Dialogue                       | Markers (under Advanced Settings) The format used to denote character speech. Default is =>Name:. Only change this if you have a specific reason.                                                                                                            |
| Writing Style & Tone vs Formatting | Rules — a common source of confusion                                                                                                                                                                                                                         |
| These two fields both shape        | AI behavior, but they live in different places in the assembled prompt and serve different purposes.                                                                                                                                                         |

Writing Style & Tone = how the AI should write and behave throughout the world. Lives early in the final instructions block. Use this for universal behavior you want applied everywhere without exception.
Formatting Rules = world-level final instructions. These appear before environment and location instructions, so they act as defaults that can be overridden by more specific contexts. Use this for structural defaults that individual locations might legitimately need to change.
If you need a rule to hold absolutely everywhere, put it in Writing Style & Tone. If you want environments or locations to be able to override a default behavior, put it in Formatting Rules.

### How this feeds into the rest of the world

The About Your World text from this tab is always the first thing in the AI's prompt — slot 1 in the prompt assembly order. Everything else you build (environments, locations, characters, lexicon) layers on top of this foundation. A strong, focused "About Your World" paragraph makes everything downstream more coherent.

See the chapter "Environments & Locations" for how environment and location instructions stack on top of what you set here. See "Timeline & Eras" for how to configure the Temporal Depth and Timeline Start Date fields, which also live in World Details.

---

## Environments & Locations

How to build broad scene contexts (environments) and specific places within them (locations), wire them together, and use the final-instructions stacking order to set context at multiple levels of specificity.

### Environments & Locations

Environments set the broad scene context for a session; locations pin the user to a specific place within that context. Together they form the spatial skeleton of your world.

### Step 2: Environments

### Where: Content area → Create New dropdown → New Environment

An Environment is a broad scene context. Think of it as a biome or district — "the haunted forest," "the merchant quarter," "level 3 of the dungeon." Users pick an environment when they start a session, and it sets the ambient backdrop for everything that happens there.

### Fields that matter to the AI

### Field label What it does
Name Shown in the prompt header as ## Environment - Name. Keep it evocative.
Context Description The main text the AI reads for this environment. Describe the atmosphere, the sounds, the general feel. This appears in every message while the user is in this environment.
Final Instructions Behavioral rules specific to this environment. Appended to the prompt after the world's Formatting Rules but before the location's rules. Environments can override world defaults, and locations can override environments.
Included Characters Pool Which of your world's Characters can appear in this environment. Add characters here with a participation weight (higher = more likely to be selected for the active scene).
Included Lexicon (under Lexicon Filters) Lexicon entries to load when this environment is active. This is the only way to activate non-global entries — they won't appear without being listed here or on a location. Global entries listed here also load without needing keyword matches.
Excluded Lexicon (under Lexicon Filters) Lexicon entries that are suppressed when this environment is active, even if keywords would normally trigger them.
Included Characters Pool is not the same as "who is in the scene." It's the pool of who could be in the scene. The actual selection of who appears depends on the user's party state. See the chapter "Characters" for a full explanation of how characters move from the pool into the active scene.

### Step 3: Locations

### Where: Content area → Create New dropdown → New Location

A Location is a specific place within an environment — "The Boar's Head common room," "Market Stall Row B," "Cell 7." Users navigate to locations while in a session.

### Fields that matter to the AI

### Field label What it does
Name Shown in the prompt as ### Current Location - Name.
Context Description Describes this specific place. Appears alongside (and below) the environment description.
Final Instructions Location-specific behavioral rules. These are read last in the final instructions block — after the world's and environment's rules — making them the most authoritative. Use this for rules that should absolutely apply at this specific place.
Environment (under Hierarchy & Relations) Links this location to an environment. This is critical. If you don't link a location to an environment, the environment won't load when users navigate here.
Parent Location (under Hierarchy & Relations) Links this location to a broader parent (e.g., "East Corridor" → "Castle Keep"). The parent's description and character pool also load when this location is active.
Included Characters Pool Characters who can appear at this specific location. Stacks with the environment's pool — both are merged.
Included Lexicon / Excluded Lexicon (under Lexicon Filters) Same as on environments. Location exclusions override environment inclusions.

### Final instructions stacking order (last = most authoritative)

When the AI reads final instructions, it reads them in this order:

World Formatting Rules → Environment final instructions → Location final instructions
Location instructions are read last, making them the most authoritative. This means a location can override both the world's and the environment's rules. If the world says "keep responses short" but a location says "describe the scenery in rich detail," the location wins because it's the last thing the AI reads before replying.

This stacking order is intentional — it lets you set sensible world defaults, adjust them per environment, and then lock in specific behavior for individual locations without having to repeat yourself at every level.

### Parent location inheritance

If you nest locations (Room → Wing → Castle), each level in the hierarchy contributes to the prompt:

Its Context Description shows in the prompt above the current location (topmost ancestor first)
Its character pool is merged into the current location's pool
Its included lexicon entries are loaded
This lets you set broad context at the Castle level and specific context at the Room level without repeating yourself. A room inherits the castle's ambient atmosphere, available characters, and relevant lore — and adds only what's unique to the room itself.

### Common mistakes

### "My environment description isn't showing up."
The location probably isn't linked to the environment. Go to the Location → Hierarchy & Relations → set the Environment field. Without this link, navigating to the location won't load the environment at all.

### "My writing style rules aren't being followed."

World-level Formatting Rules can be overridden by environment and location instructions (since they're read after). If a location has contradicting final instructions, those win. Check that your locations and environments aren't overriding your world rules unintentionally. If you need a rule to be truly universal, put it in Writing Style & Tone (which lives earlier in the prompt and frames the AI's behavior) rather than Formatting Rules.

---

## Characters

### Characters

Characters are the most important and most misunderstood part of world building — this chapter covers everything from writing their descriptions to understanding exactly when and how they appear.

### Step 4: Creating Characters

### Where: Content area → Create New dropdown → New Character

### Two completely different text fields

Every character has two description fields. They are not redundant — they serve different purposes and both need to be filled in.

### Long Summary (the NPC Database block)

This is shown in the NPC Database at the top of the prompt when the character is actively in the scene (party member or location pool selection). This is the main block of text the AI uses to roleplay the character.

Write flowing prose paragraphs. Cover whatever is important for your character — there's no rigid format, just write what the AI needs to know:

### Physical appearance and typical clothing

### Background and history
Personality traits, likes, dislikes
Relationships and social patterns
Goals, motivations, secrets, fears
Behavioral patterns and habits
Speech patterns with example quotes
End the description with a speech section that shows the AI how the character actually talks — accent, tone, vocabulary, and 2–3 example quotes that capture their voice.

Example — Long Summary for an NPC Database block:

(Don't include the character's name in XML tags — the system wraps these automatically using the character's Display Name.)

Margret Alaina Thames is a 25-year-old English woman (true age unknown due to disease preservation) with medium-length black wavy hair, striking green eyes, and pale complexion typical of Victorian English nobility. Margret has an athletic and capable build, neither delicate nor overly muscular, standing at 5'8" tall. Margret wears a white Victorian blouse with bell sleeves, black cotton slacks, leather belt with satchel, and practical leather boots suitable for various terrains. Margret wears a large silver Latin cross necklace with deep sentimental value and occasionally adopts period-appropriate items from visited timelines.

Margret was born in 1836 to an English nobleman and respected archaeologist who took her on expeditions worldwide, giving her both highborn education and practical field experience. Margret loved reading fiction and was traveling to the North American West when DeTamble's Disease first activated. Margret's first jump remains a defining but unspoken trauma, the exact circumstances deeply buried.

Margret has jumped to countless realities over her travels, experiencing dinosaurs in the deep past, exploring space stations and distant futures, living through decades of human history across multiple timelines, and visiting worlds that defy description. Margret's extensive experience has made her one of the most knowledgeable time travellers regarding the mechanics and dangers of the disease.

(... additional paragraphs covering abilities, personality, emotional state, behavioral patterns, secrets ...)

Margret's speech: Proper English accent with Victorian formality that occasionally softens in casual settings, precise and educated speech patterns but not pretentious, uses vocabulary and references from multiple time periods sometimes anachronistically, dry wit and sardonic humor when comfortable. "I've walked with dinosaurs and danced among the stars. None of it matters when you can't stay." "The trick to surviving displacement isn't fighting the current - it's learning which currents lead somewhere worth being." "You think immortality is a gift? Try watching everyone you've ever known turn to dust while you remain unchanged."

### Summary (the condensed version)

This appears in three places: (1) As a fallback in the NPC Database when Long Summary is empty. (2) As a mid-conversation reminder in the floating prompt for party characters, alongside their current outfit. (3) As keyword-triggered lore for background characters who aren't in the scene.

The Summary is a shorter version of the character — not a one-liner, but a condensed take that hits the essential points. It can be one paragraph or several, as long as it's meaningfully shorter than the Long Summary. Cover appearance, background, key personality traits, and notable abilities without the full depth of the Long Summary.

Example — Summary for the same character:

Margret Alaina Thames is a 25-year-old English noblewoman from 1836 with DeTamble's Disease, though her true age is unknown due to the condition's immortalizing effects. Margret has wavy black hair, striking green eyes, and a practical fashion sense, typically wearing Victorian blouses with modern adaptations like slacks and a leather belt, along with a silver Latin cross necklace and satchel. Margret speaks with a proper English accent and displays the refined manners of her upbringing. Margret is the daughter of a respected nobleman and archaeologist who took her on expeditions worldwide, giving her both a highborn education and practical field experience. Before her displacement, Margret loved reading fiction and was traveling to the North American West when her disease first activated. Margret has learned to partially control her jumps through a dangerous technique: she inflicts fatal self-harm by slitting her wrists and focuses intensely on her desired destination during the jump trigger. This method works most of the time but occasionally sends her to unexpected places. Margret has jumped to countless realities over her travels, experiencing dinosaurs in the deep past, exploring space and distant futures, and living through decades of human history across multiple timelines. Margret is practical, cunning, observant, and extremely knowledgeable about history and science from both her education and firsthand experience. Margret speaks seven languages fluently: English, French, Gaelic, Mandarin, Japanese, Spanish, and Russian. Margret has found solitude in her eternal travels and maintains emotional distance from others, feeling no need for romantic entanglements beyond physical release. Margret's extensive experience has made her resourceful and adaptable, though she carries the weariness of someone who has seen too much and lost everyone she ever cared about to the curse of her disease.

### Why both fields matter

You should always fill in both fields. Long Summary is the full character sheet for when the character is active in the scene. Summary is the condensed version used as a floating prompt reminder, keyword lore, and as the fallback if Long Summary happens to be empty. If you only have time for one, fill in Summary — it covers the most ground.

### Writing format: Pronoun Pruned Prose (PPP)

Character descriptions should follow a specific writing convention to work well with LLMs. The core rule: never start sentences with pronouns. Always use the character's name as the sentence subject, even if it feels repetitive.

Bad: She walks to the store. She buys bread.
Good: Margret walks to the store. Margret buys bread.
This feels unnatural when writing, but LLMs process text differently than humans read it. Name repetition anchors the AI to who is doing what, preventing confusion — especially in scenes with multiple characters.

Use names for:

### Sentence subjects

### Action descriptions
Thought descriptions
Possession when starting clauses
Margret adjusts her cross. Margret's hand trembles.
Anton scowls. Anton's temper flares.
Janessa clutches the grimoire. Janessa's violet eyes burn with intensity.
Pronouns ARE allowed:

### Within sentences after establishing the subject

### In dialogue
For possessives mid-sentence
As objects
Margret walks to the door and opens it with her key.
Anton commands his guards and watches them scatter.
"I won't let you," Janessa says to Margret.
Never start a sentence with:

### She / He / They (subject pronouns)

### Her / His / Their (possessive pronouns at the start of a sentence)
Writing tips
Accept the repetition. It feels awkward at first. LLMs need this anchoring to stay consistent — trust the format even when it reads strangely to you.
Vary sentence structure. Mix short and long sentences to avoid monotony despite name repetition.
Use descriptors with names. "The merchant," "the time traveller," "the noblewoman" can substitute for names occasionally.
Speech examples are optional. Use them when you want to demonstrate a specific character voice. Skip them for simpler characters.
World-building goes outside character blocks. Mechanics, setting info, magic systems — keep that in your About Your World, environment, or lexicon entries, not inside character descriptions.
Speech sections need example quotes. Always include 2–3 actual quotes showing the character's voice, not just a description of how they talk.
NPC dialogue examples are for demonstration. They show the AI how characters interact when activated with the NPC prefix format (e.g., =>Name:) during roleplay.

### Outfits

Outfits let you swap a character's appearance description per session or per location. Add outfits in the Outfits section and set a Default Outfit. The current outfit description is appended to the character's prompt block.

You can also create Speech Examples that only trigger for a specific outfit (e.g., a character speaks differently when in armor vs. formal dress).

### Speech Examples

Speech examples are shown to the AI as demonstrations of how the character talks. They appear in the ## NPCs section of the prompt.

Speech examples support triggers:

### No trigger — always shown (up to the "Number to Use" limit)

Location trigger — only shown when the character is at a specific location
Environment trigger — only shown when in a specific environment
Outfit trigger — only shown when the character is wearing a specific outfit
Character trigger — shown as a dialogue exchange with another specific character
If any location/environment/outfit-triggered examples exist and match the current scene, only those are shown. If none match, all untriggered examples are used as fallback.

Speech examples appear for party characters, active location pool characters, and remaining pool characters (those in the pool but not selected for the active scene). This means any character you've added to a location or environment pool will have their speech patterns visible to the AI, even if they aren't currently "on stage." Only true background characters (not in any pool at all) don't get speech examples.

### Activation Keys

Keys are the words that trigger a character's Summary to appear in the context when they're not actively in the scene.

The character's own name, first name, nicknames, and titles are automatically added as keys. You only need to add additional keys for things the character might be referred to as — "the librarian," "old Elara," "the archivist."

Without keys, a background character can only appear if they're in the party or a location pool. With keys, they'll appear contextually whenever their name or descriptor comes up in conversation.

### Timeline Gating

If you fill in Start Timeline Position or End Timeline Position, the character will only exist in the prompt during that slice of the world's timeline. See the chapter "Timeline & Eras" for how these values work.

If a character fails the timeline check, they won't appear even if they're in a location pool.

### Step 5: How Characters Enter the Scene

Understanding this is the key to making characters work. There are four tiers, in order of prominence.

### Tier 1 — Party Characters (always in full, with a floating reminder)

A "party" is the user's persistent session state — think of it as their active roster. Characters the user has explicitly added to their party always appear in two places:

NPC Database (at the top of the prompt) — their Long Summary is rendered in full. This is the main block of information the AI uses to understand and roleplay the character.
Floating prompt (inserted partway through the chat history, near the end) — their Summary is rendered along with their current outfit. This acts as a refresher, reminding the AI of who is present even in long conversations where the NPC Database has scrolled far above.
Both Summary and Long Summary matter for party characters. Long Summary is the full character sheet; Summary is the compact reminder that keeps the AI on track in longer chats.

Party characters can be weighted as Primary or Secondary in the reply pool:

Primary weight means the character is a main participant — the AI will favor them when selecting who speaks next.
Secondary weight means the character is present but more of a supporting role.
Both primary and secondary party characters get the same treatment in the NPC Database (full Long Summary) and the floating prompt (Summary + outfit). The weight distinction affects reply selection priority, not the depth of information the AI receives about them.

Users add characters to their party from the in-session party panel, not from the world editor.

Tier 2 — Location Pool Characters (in the NPC Database, with speech examples, but no floating reminder)
Characters you add to a location or environment's Included Characters Pool form a pool of potential scene participants. When a session is active in that location, characters from the pool who are selected for the current scene get:

Their Long Summary rendered in the NPC Database (same as party characters)
Their Speech Examples rendered in the NPC dialogue format section (so the AI knows how they talk)
Their Summary also registered as a keyword-triggered lexicon entry (so their short description can appear when mentioned elsewhere in conversation)
The key difference from party characters: location pool characters do not appear in the floating prompt. They only have their Long Summary in the NPC Database at the top. In long conversations, the AI may "forget" them more easily because there's no mid-conversation reminder. If you want a character to stay prominent throughout long chats, they should be in the user's party, not just in a location pool.

Characters in the pool who are not selected for the active scene become keyword-triggered background characters (Tier 3).

The participation weight on each pool entry controls how likely a character is to be selected when the scene is populated (higher weight = selected more often).

Tier 3 — Remaining Pool Characters (not selected for the active scene, but still nearby)
Characters in a location or environment's pool who were NOT selected for the current active scene land here. They get two things:

Their Speech Examples are rendered in the NPC dialogue format section — the AI knows how they talk even though they aren't front and center.
Their Summary is registered as a keyword-triggered lexicon entry. When their name or keys come up in conversation, the Summary is injected as lore.
They do NOT get their Long Summary in the NPC Database and do NOT appear in the floating prompt. The AI knows they exist in the area (through examples and keyword lore) but doesn't have the full character sheet to work with.

This makes them "nearby" characters — the AI can bring them into a scene naturally because it's seen their speech patterns, and if someone mentions them their Summary provides context. But they won't be played with the full depth of a party or active pool character.

### Tier 4 — Background Characters (keyword-triggered only)

Every WorldCharacter not in a party and not in any location or environment pool for the current session becomes a keyword-triggered Lexicon entry only. Their Summary is the entry content. Their name, first name, nicknames, and titles — plus anything in their Primary Keys list — are the trigger keywords.

When those keywords appear in the recent chat history (within the Span Depth window), the Summary gets injected into the prompt as lore. This does make them "present" in the AI's awareness — the AI can reference them, mention them, and weave them into the narrative. But it only has their short Summary to work with — no Long Summary, no speech examples, no outfit.

This is the intended use for world characters who aren't meant to be in the immediate area — distant rulers, historical figures, characters in other cities. Write their Summary as a lore-style description of who they are and what they're known for, and the AI will reference them naturally when they come up.

### Summary of all four tiers

Tier Who NPC Database Speech Examples Floating Prompt Keyword Lore What to fill in
Party character User adds them to their party Long Summary Yes Summary + outfit — Both Summary and Long Summary
Active pool character In pool, selected for scene Long Summary Yes Not included Summary (also registered) Both Summary and Long Summary
Remaining pool character In pool, NOT selected for scene Not included Yes Not included Summary (when keywords match) Summary, Long Summary, Speech Examples, Primary Keys
Background character Not in any pool Not included Not included Not included Summary (when keywords match) Summary + Primary Keys
Parties (the player's session state)
A party is what the system creates when a player starts a session in your world. Think of it as their active "save file" — it persists between chat logs, so a player can leave and come back to the same state.

The party tracks:

### Current location — where the player is in the world

### Current environment — the environment they're in
Current characters — the NPCs they've added to their roster (the Tier 1 party characters above)
Party Instructions — freeform notes the player adds, appended to every prompt as an <ImportantNotes> block (for example, "my character has amnesia and doesn't know the others" or "we are currently disguised as merchants"). Session-persistent and user-managed from the in-session party panel.

### What you control as a creator

Most party state is set by the player during their session. What you shape is:

Which characters are available — by putting them in location and environment pools.
The default location / environment — by linking scenarios to specific locations (see the Scenarios & Guided Intro chapter), or by setting the world's default starting location.
World-wide behavioral notes — Party Instructions belong to the player, but if you want something that applies to every player, use your world's Writing Style & Tone or Formatting Rules fields instead (see the World Info & Details chapter). Those apply globally; Party Instructions are per-player.
Players add and remove party characters from the in-session party panel, not from the world editor.

### Common mistakes

### "My character does nothing / is ignored."
Check their Long Summary and Summary. When a character is active in the scene, the AI uses Long Summary — but if Long Summary is empty, it falls back to Summary. If both are blank or too short, the AI has essentially no information to work with. Fill in Long Summary with the full character sheet, and Summary with a concise version.

### "My character appears and disappears randomly."

Check Start/End Timeline Position. If these are set incorrectly (e.g., in years instead of hours), the character will be excluded whenever the session timestamp doesn't match. See the "Timeline & Eras" chapter for how timeline values work.

### "I added a character to the world but they never show up."

A WorldCharacter that isn't in a party or active location pool becomes a keyword-triggered lore entry. They'll only show their Summary when their name or keys come up in conversation — and even then, it's just the short lore blurb, not the full character. If you want them to appear as a fully realized NPC with their Long Summary and speech examples, add them to a location or environment's Included Characters Pool.

"A character shows up but feels shallow / doesn't talk like themselves."
Check which tier the character is in. If they're in a location or environment pool, the AI can see their speech examples even when they aren't selected for the active scene — so they should at least sound right. If they're not in any pool at all (Tier 4), the AI only has their Summary and no speech examples. To get the full character experience with Long Summary, speech patterns, and outfit, the character needs to be in the party or selected from an active pool.

### "Characters in my location pool don't appear."

The pool is a list of candidates, not guaranteed participants. The actual selection happens when the session is populated. Additionally, check that the characters pass timeline gating — if their Start/End timeline positions exclude the current timestamp, they won't be selected.

### "Speech examples aren't showing up."

Speech examples render for party characters, active pool characters, and remaining pool characters (those in the pool but not selected for the scene). If a character isn't in any location or environment pool at all, their speech examples won't appear. Add them to the relevant pool to get their dialogue patterns into the prompt.

---

## Lexicon

### Lexicon

Lexicon entries are your world's knowledge base — the lore facts, location details, historical events, item descriptions, organizations, and anything else the AI should know about but that doesn't need a full character card.

### Where to find it

### Where: Content area → Create New dropdown → New Lexicon Entry

### Global vs non-global — this matters first

Every lexicon entry has a Global toggle, and this is the first thing to understand because it determines whether the entry can activate on its own.

Global ON (default): The entry participates in the world-wide keyword scan. The last N messages (where N = your Span Depth setting) are searched for matches against the entry's Primary Keys. If a match is found, the entry's Content is injected into the prompt. Global entries can activate in any location, any environment, any scene — wherever the keywords appear.

Global OFF: The entry is invisible to keyword scanning. It will never activate on its own no matter what keywords appear in the conversation. It can only appear if you explicitly add it to a location or environment's Included Lexicon list.

Use non-global entries for context-specific lore: a dungeon trap description that shouldn't randomly appear in a city scene, a secret room's contents that should only show up when the user is in that room, a local legend only told in one village.

### Other activation modes

Constant: The Constant toggle makes an entry always inject regardless of keywords or location. Use this sparingly — constant entries use tokens in every single message.

Force-loaded from a location or environment: Adding any entry (global or not) to a location's or environment's Included Lexicon list makes it load when that location or environment is active. This works for both global and non-global entries — it's the only way to activate a non-global entry, keywords are still required.

### Where the content is injected

The Position dropdown controls where in the prompt the content lands:

### Position Where it goes Best for

Before Char A <Lore> block at the very top of the system prompt, before the world overview High-priority context that should frame everything else
After Char A <Lore> block at the end of the system prompt, after the NPC Database Supporting lore, item and location descriptions
In Chat Injected into the chat history at a specific depth Recent events, "what just happened," dynamic situational info
For In Chat entries, the Insertion Order field controls depth — a value of 4 means the entry is injected 4 messages from the most recent. A value of 0 means it goes at the very start of the chat history.

### Advanced activation controls

| Field                     | What it does                                                                                                                                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Delay                     | Entry won't activate until at least N messages have passed                                                                                                               |
| Sticky                    | Once activated, stays active for N additional messages even if keywords stop appearing                                                                                   |
| Cooldown                  | After activating, can't activate again for N messages                                                                                                                    |
| Activation                | Chance 0–100. The chance the entry fires on any given message where its keywords match. Use for "sometimes relevant" details you don't want appearing every time.        |
| Entry types               |                                                                                                                                                                          |
| Every lexicon entry has a | Type field. The type is mostly organizational, but several types unlock additional configuration panels that give you specialized behavior beyond plain prose injection. |

The plain types — lore/concept, organization/faction, and memory — are text-only. Write the entry's content as prose the AI will read directly.

The following types open additional configuration panels and are covered in their own chapters or sections:

Item — items that characters can carry, use, buy, or receive. Items have a dedicated item config (name, description, value, weight, usability, effect). See the "Items" chapter.
Furniture — interactive objects placed in locations (chairs, chests, doors, machines). Furniture has placement and interaction config. See the "Furnishings" chapter.
Creature — mobs and enemies with RPG stats, move sets, and loot tables. See the "Creatures" chapter.
Move — combat moves or abilities attached to creatures (or characters). See the "Creatures" chapter.
Nature — character natures used in RPG stat systems (affects base stats or behavior). See the "RPG Systems" chapter.
Ability — player or character abilities with effect config. See the "RPG Systems" chapter.
For all types, the content field is what the AI actually reads — the entry's name is only shown in the editor UI, not in the prompt. Write content as self-contained prose that includes the subject's name within the text itself.

### Common mistakes

### "My lore entry never activates."
Either: (a) the Primary Keys list is empty or doesn't match anything being said in the conversation, (b) the Global toggle is off and you haven't added it to any location or environment's Included Lexicon list, or (c) the Enabled toggle is off. Check all three.

---

## Timeline & Eras

### Timeline & Eras

The timeline system lets your world's content exist across history — gating characters, locations, lore, and environments to specific slices of time so the right things appear at the right moment in a session.

### Where to find it

Where: World Details tab → Temporal Depth (World Age) + Timeline Start Date

### The core concept

Every timeline value is in hours. Not years, not days — hours. The entire timeline system uses a single counter that increments in hours from a starting point of 0.

### 0 = the beginning of recorded history in your world

A value of 87,600 = 10 years into your world's timeline (10 × 365 × 24)
When a user is chatting, their session has a current timestamp — the hour in your world's history that the chat is set at. Every piece of content with a timeline position is compared against this number.

### Timeline Start Date (optional but recommended)

Set a Timeline Start Date to give hour-0 a real calendar date. The prompt will then say "The current in-world date is March 15, 1347" instead of "current timestamp is 3,200 hours." This makes the timeline much more intuitive for both you and users.

Quick conversion:

### hours = years × 8,760

### hours = months × 730 (approximate)
hours = days × 24
Example: If your world's history starts in 1000 AD and the "present" is 1200 AD, that's 200 years = 1,752,000 hours. Set Temporal Depth to 1,752,000 and point your scenarios to that timestamp.

### Gating content to a time period

Every character, lexicon entry, environment, and location has optional Start Timeline Position and End Timeline Position fields. If the current session timestamp falls outside those bounds, the content is silently excluded — it won't appear in the prompt at all.

Use cases:

A character who only exists before a war (end position = the war's timestamp)
A location that only exists after it's built (start position = construction complete)
Lore entries describing an ancient artifact before it's destroyed
If a character fails the timeline check, they won't appear even if they're in a location pool.

### Time of Day periods

The Time of Day Periods section lets you define named periods (Dawn, Day, Dusk, Night) with descriptions. When the current timestamp falls within a period, its description is automatically appended to the final instructions: "The current time period is 'Night': The city falls quiet."

This doesn't gate content — it just adds ambient time-of-day flavor to the prompt.

### Recurring logic (seasonal and cyclical)

On lexicon entries and locations, you can set Recurring Logic to make content appear only at certain times of day or certain times of year:

Cycle — repeats on a fixed hour cycle. A night-only entry with cycle length 24, active 20–6 activates only between hour 20 and 6 of every 24-hour cycle.
Calendar — active during a specific date range each year. Requires a Timeline Start Date to be set.

### Eras

In addition to raw Start/End timeline positions, worlds, characters, environments, and locations can have named Eras — labeled spans of time with their own descriptions and rules.

Eras give you a human-readable way to organize your world's history beyond bare hour numbers. Instead of managing a character who starts at hour 43,800 and ends at hour 87,600, you can associate them with "The Age of Expansion" and let the era handle the bounds.

Content gated to an era is only active when the session's current timestamp falls within that era's span. This works the same as Start/End timeline positions — content outside the active era is silently excluded — but eras let you name and group those spans meaningfully across many entities at once.

Eras are created and managed per entity (a world era, a character era, an environment era, a location era). Each entity manages its own era list independently, though you'll typically align era spans across your world to keep things consistent.

### Referencing past events that stay accurate ("four years ago")

When you write backstory into a character bio, lexicon entry, or location description, you'll often want a phrase like "the Empire fell four years ago." The problem: the moment your world's clock advances a year, that line is wrong — it should now read "five years ago." Editing every mention by hand is a nightmare.

To solve this, the prose fields for Lexicon entries, World Characters, and Locations have an Insert world time button. It drops in a smart reference that recalculates every time the world's clock moves, so "four years ago" quietly becomes "five years ago" on its own.

When you click it, you choose the moment the event happened in one of two ways:

Relative — "4 years / months / days before (or after) the current world time." This is the common case: you're thinking "this happened about four years ago."
Calendar date — pick an exact in-world date (year, month, day). This anchors the reference to a specific point in your world's history.
Either way, the editor shows a live preview ("renders now as: four years ago") so you can see exactly what readers will get. The reference always describes the gap between that moment and wherever the session's clock currently sits — it grows and shrinks automatically as time passes in play.

What the button actually inserts is a macro:

The Empire fell {{worldAgo 35040}}.
35040 is the absolute world-hour the event happened (35040 hours = 4 years after hour 0). If the session clock is at year 8, that renders "The Empire fell 4 years ago"; at year 9 it renders "5 years ago." You can type the macro by hand too. Options:

### {{worldAgo 35040}} renders: 4 years ago

{{worldAgo 35040 unit="years"}} force the unit (years/months/weeks/days/hours)
{{worldAgo 35040 suffix=false}} renders: 4 years (no "ago"/"in" wrapper, for mid-sentence use)
A future date renders as "in 4 years" instead of "ago." If your world has a custom calendar (its own months, year length, and leap rules), the year and month counts follow that calendar; otherwise it uses ordinary 365-day years and 30-day months.

### Birthdates on the calendar

A World Character's Birthdate field uses the same picker. If your world has a custom calendar, you can choose the character's birth year, month, and day directly instead of working out an hour offset by hand — including dates before the start of recorded history (year 0). Without a custom calendar, the field falls back to a plain hours value with a human-date readout.

Once a birthdate is set, two macros work automatically inside that character's content (they read the character whose turn it is, so you don't pass any value):

### {{age}} the character's age in whole years, e.g. 27

### {{time_till_birthday}} e.g. "Today!", "3 days", "2 months"
You can combine {{age}} with logic — for example, only show a line once the character is an adult:

{{#compare age 18 operator=">="}}She carries herself with hard-won authority.{{/compare}}
Other time macros for your content
Any character, lexicon, location, environment, or instructions field accepts these. All hour values are counted from world-age 0.

Reveal or hide text based on the world clock:

{{#afterTimestamp 87600}}The old bridge has long since collapsed.{{/afterTimestamp}}
{{#beforeTimestamp 87600}}The old bridge still stands, for now.{{/beforeTimestamp}}
{{#betweenTimestamps 43800 87600}}The war is raging.{{/betweenTimestamps}}
React to the time of day (uses your Time of Day periods and day length):

### {{timeOfDay}} the active period's name, e.g. "Night"

{{#isTimeOfDay "Night"}}The market is shuttered and dark.{{/isTimeOfDay}}
{{#betweenHours 22 4}}Curfew is in effect.{{/betweenHours}}
{{hourOfDay}} / {{dayNumber}} the current hour within the day / the day count
One thing to keep straight: these macros all run on in-world time. There are also generic date macros like {{timeAgo}} and {{formatDate}}, but those run on the real-world calendar (the actual date the user is chatting), not your world's clock — don't reach for those when you mean world time.

### Common mistakes

### "My character appears and disappears randomly."
Check Start/End Timeline Position. If these are set incorrectly (e.g., in years instead of hours), the character will be excluded whenever the session timestamp doesn't match. Use the quick conversion table above to double-check your values.

### "I set up timeline positions but nothing changed."

The session needs a current timestamp set — this is part of the party's world data and is set either by the scenario's Insertion Point or by the user advancing time during their session. If the timestamp is 0 or unset, only content with no timeline bounds (or with a start position of 0) will appear. Make sure your scenarios have an Insertion Point configured to set th

---

## Scenario & Guided Intro

### Scenarios & Guided Intro

This chapter covers two layers that work together: Scenarios (structured entry points that drop players into your world at a specific location and scene) and the Guided Intro (an onboarding wizard that can walk players through character creation, stat allocation, and custom choices before the chat begins). You don't need both — a simple world can run on scenarios alone — but understanding how they interact lets you build anything from a one-click start to a full Pokémon-style trainer onboarding.

### Part 1: Scenarios

### What a scenario is
A scenario is a premade entry point into your world. When a player starts a chat from a scenario, the system sets their starting location, loads the right environment and character pool, and (optionally) opens with a specific scene — either text you wrote or text the AI generates fresh for each player.

Every world should have at least one scenario. Without one, players have to configure their starting location and character roster manually before the chat can begin, which is a poor first impression.

Where to create them: Content area → Create New dropdown → New Scenario.

### Scenario fields

| Field                                    | What it does                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                                     | The scenario's title shown to players in the start wizard. Make it evocative — it's the first impression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Description                              | A brief summary of what this scenario is about. Shown on the scenario card.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Location                                 | Sets the player's starting location. The location's linked environment loads automatically. Required for the prompt to have any spatial context — without it, the prompt has no location block.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Environment                              | Optional override. If set, loads this environment instead of the one linked to the starting location. Use when you want a location to behave differently in different scenarios.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Included Characters Pool                 | Characters available specifically in this scenario, layered on top of the location's own character pool. Use this to add scenario-specific NPCs without changing the location's default pool.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Scene Instructions A prompt given to the | AI to generate a unique opening scene for each player who starts from this scenario. Every player gets a fresh, AI-written opening.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Premade Scenes                           | Static opening texts you wrote. Players may see a picker if you add more than one, or receive one at random. Use when you want a crafted, controlled cold-open.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Insertion Point                          | The timeline hour this scenario is set at. Sets the session's current timestamp, which determines which timeline-gated content is active. See the Timeline & Eras chapter for how timestamps work.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Starting Currency                        | Grants the player an amount of one of your world's currencies when the session begins. Use this to front-load a character with funds — a noble starting flush with coin, a thief who begins broke.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Starting Inventory                       | Grants the player one or more items from your world's lexicon at session start.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Starting Properties                      | Grants the player ownership of one or more of your world's purchasable locations from turn one. Combined with Starting Currency and Starting Inventory, this lets you build a fully furnished-inheritance setup: the player wakes up owning a place rather than having to earn it.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Scene                                    | Instructions vs. Premade Scenes: these are two separate mechanisms that serve different goals. Scene Instructions hands the AI your direction and lets it write a fresh scene — good for variety and for scenarios where the player's choices (their persona, their gear) should influence the opening. Premade Scenes are text you authored exactly — good for a specific tone or a cinematic moment you don't want the AI improvising around. You can provide both; if a Premade Scene is available, the system uses it and the Scene Instructions are not used for that run. If you want AI-generated openings consistently, leave Premade Scenes empty and rely on Scene Instructions. |

### Default starting location

Separate from any scenario, the World Details tab has a Default Starting Location field. This is the location (and its linked environment) the system falls back to when no scenario resolves a location — for example, when a player starts a world-level intro (see Part 2) and doesn't complete a spawn-location question, or when a session is opened without any scenario context.

Think of it as your world's front door. Set it to whatever location makes sense as a neutral starting point — the village square, the guild hall, the port of entry. If you leave it empty and a player ends up in a session without a location set, the prompt will have no location block, which produces a disoriented, generic AI response.

### Part 2: The Guided Intro

The Guided Intro is a paged wizard that players walk through before the first message in a session. It replaces the "configure everything yourself" Advanced dialog for most players, while keeping the Advanced option available for those who want it.

### How the wizard is structured

The wizard always opens with two built-in pages:

Party — use an existing party (carrying forward its persona, character, and stats) or start fresh.
Scenario — choose which scenario to play. Worlds with a world-level intro also show a Begin here option here (see the "World Intro" section below).
After those, the wizard shows your content pages — the pages you configure. These are derived in one of two ways:

Auto-derived (default): the wizard builds pages from the scenario's setup questions plus two scenario toggles. Standard order is Choose Your Character → Build Your Stats → one page per setup question.
Custom world introduction: if you turn on Custom world introduction in the Introduction section, you author the page list yourself in whatever order you want. This fully overrides auto-derivation.
If you only need a couple of setup questions and the standard character/stats flow, you don't need a custom introduction — just add fields and flip the toggles. Use the custom introduction when you want narrative slides, a specific page order, or pages interspersed between your questions.

### Setup questions (scenario fields)

Setup questions are authored per scenario, in the Scenario editor under Advanced Options → User Inputs. Each question becomes its own page in the guided wizard (or a row in the Advanced dialog).

To add a question: open Advanced Options, click Add Field, and configure it.

### Field types

### Type Player sees
Text A single-line text box
Text Area A multi-line text box
Number A numeric input
Select A dropdown of options you define
Checkbox A toggle
Species Picker Picks a species
Occupation Picker Picks an occupation
Creature Picker Picks from a creature pool you define, shown as image cards
Item Picker Picks from an item pool you define, shown as image cards
Lexicon Picker Picks from any lexicon entries you pool, shown as type-aware image cards
For Creature, Item, and Lexicon Pickers, a pool editor appears after you select the type. Add the specific entries players may choose from, and set Max Selections (1 = single choice; higher = multi-select up to that count). Creature picks also carry a per-entry Level.

### Per-field settings

### Setting What it does
Field Label The question's name. Also used as the page title if you don't override it.
Description Help text shown under the field while the player is answering. Use this for narrative flavor — set the scene for the choice here, not in the greeting.
Page title / Page subtitle Override the title and subtitle of this field's page in the wizard. Leave blank to use the label and description.
Required When on, the player can't advance past this page without answering.
Default A pre-filled starting value seeded into the wizard. The player can accept or change it.

### Bindings — what a choice actually does

A picker is only meaningful if the chosen value goes somewhere. Bindings declare that destination. On any field, under What this choice does, you can toggle one or both:

Activate as lore — the chosen entry is added to the party as live context for the AI. It renders in the prompt according to its lexicon type: a creature shows as a <Creature> block, an item as <Item>, a location as <Location>, and narrative types in the standard lore format. The AI knows the player picked it, but a creature won't be mistaken for a speaking NPC.

Remember as variable — the chosen value is stored in the party's memory under a Memory key you specify (defaults to the field's id). Once stored, you can reference it anywhere variables work: Handlebars templates with {{memGet "key"}}, InfoBoards, and scripts. For lexicon-backed picks, a companion key_name entry is also stored automatically, giving you the human-readable name alongside the raw id.

You can use both at once. A "pick your starter creature" question, for example, can Activate the starter so it's live context in the prompt, and also Remember it under starter so your InfoBoard and greeting can reference it by name.

Lexicon Picker fields automatically activate their pick even with no bindings set. Add Remember on top when you also want a variable available in templates.

### Text field match rules

Free-text answers (Text and Text Area fields) can trigger additional effects based on what the player types, via match rules. Each rule has:

A match type — either Keyword (the player's answer contains this word or phrase, case-insensitive) or Regex (the answer matches this regular expression).
A match value — the keyword string or regex pattern to check.
An action — one of:
Activate — activate a specified lexicon entry as live lore (same as the Activate binding, but conditional on the text match).
Remember — store the matched value (or a fixed value you specify) under a memory key.
Set location — set the player's starting location to a specified location.
Match rules let you react to open-ended answers without scripting. For example: a "describe your background" text field could check for the keyword "guard" and automatically set the spawn location to the barracks, or activate a "military background" lexicon entry that adjusts the AI's tone toward the player.

### Choice-driven grants — currency and property from a single pick

Any setup field — not just text fields — can carry a grant binding that gives the player something of material value based on what they choose. Two grant types are available:

Grant currency (grant_currency) — when the field resolves, the player receives an amount of one of your world's currencies added to their wallet. Set the currency and the amount on the field. Example: a "Choose your starting background" Select field could have the "Merchant's Heir" option grant 500 Gold, while "Traveling Bard" grants 50 Gold. The grant fires automatically at session start; the player doesn't have to claim anything.

Grant property (grant_property) — when the field resolves, the player is given ownership of a specified purchasable location from session start, the same as if they had bought it. Example: a "Which estate did you inherit?" field could grant a Manor in the north or a Cottage by the sea depending on the player's pick.

Both grants combine freely with the existing Activate and Remember bindings. A field can simultaneously activate a lore entry for the AI, remember the player's pick as a variable, and grant them currency or a property. They also stack with the scenario-level Starting Currency, Starting Inventory, and Starting Properties fields — scenario-level grants fire alongside field-driven grants, so the player receives all of them.

Worked example — the furnished-inheritance setup:

Suppose you're building a scenario where the player inherits a deceased relative's estate. You could:

Use the scenario's Starting Properties field to grant the Ashwood Manor location at session start.
Use the scenario's Starting Inventory field to grant the deed, a set of house keys, and a ledger of debts as items.
Use the scenario's Starting Currency field to grant a modest sum of Gold — enough for repairs, not enough to ignore the debts.
Add a "How did you know the deceased?" Select field with options like "Estranged niece/nephew" and "Distant cousin." Give each option a grant_currency binding with slightly different amounts to reflect the closeness of the relationship, and a grant_property binding for a secondary cottage if they were especially close.
The player begins the session already owning the manor, already holding the relevant items, and already weighted with the currency and property that match their chosen relationship — no shopping trip, no onboarding friction. The AI's first message can address them as the new owner of a dusty manor rather than a stranger who just arrived.

### Choose Your Character and Build Your Stats pages

These two pages are controlled by toggles in the Scenario editor, under Publishing → Guided Intro.

### Include "Choose Your Character" page

When on, the wizard shows a Choose Your Character page where the player selects how they enter the world:

Be yourself — the player picks one of their existing personas, creates a blank persona, or picks one of your Suggested personas (preset starting points you author in the Introduction tab; see the Persona Presets section below). Whether they create or pick a preset, the full persona editor opens pre-filled, and they finish and save their own persona.
Play a character — pick from a roster of your world's characters. This button only appears if you've designated a roster.
To build the roster, with the toggle on, a Playable characters grid appears listing your world's characters. Click the ones players should be able to play as. A player who picks a roster character plays as that world character; a player who picks or creates a persona plays as themselves.

The player's name comes from their persona or chosen world character. Do not add a separate "What's your name?" question — it's redundant for personas and meaningless for someone playing as one of your world characters.

### Include "Build Your Stats" page

When on, the wizard shows a Build Your Stats page — the full Species → Occupation → Stat Allocation → Review build, honoring your world's stat configuration (point-buy, free-assign, roll, or fixed). The allocation is saved to the party's RPG state and persists across reused parties.

If a player reuses an existing party and chooses to carry its data forward, the Choose Your Character and Build Your Stats pages are automatically skipped. The previous persona/character and stats come along as-is.

### Stat templates

Stat templates are named starting-point bundles for the stat build. They appear on the Build Your Stats page as preset options a player can pick as a jumping-off point and then tweak.

Each template has a name (shown to the player, e.g. "Veteran Soldier" or "Glass Cannon Mage") and carries a base_stats preset — optionally combined with a suggested species or occupation. Templates don't lock the player into anything; they seed the inputs so the player starts with a sensible spread rather than a blank slate, then adjusts from there.

Author them at the bottom of the Introduction section, under Stat templates. They save with the rest of the Introduction when you click Save introduction.

### Conditional pages and questions

Both scenario setup questions and custom introduction pages can be made conditional, appearing only when earlier answers match a rule. This lets you branch the wizard without scripting.

Each scenario field has a "Show this question only when…" block at the bottom. Each custom introduction page has a "Show this page only when…" block. Click Add condition to add a rule. Each rule has three parts:

Source — what to read. On a scenario field this is a dropdown: Character mode (persona vs. world character) or any other field in the scenario. On a custom intro page, you type a field id or character_mode.
Operator — is, is not, is any of, is none of, has a value, or is empty.
Value — what to compare against (hidden for has a value / is empty).
When multiple conditions are applied to one question or page, all of them must pass (they are AND-ed).

character_mode resolves to persona when the player chose Be yourself and world_character when they chose Play a character — useful for branching on which path the player took.

Examples:

A "Which spell school?" question with a condition on a class field (class is mage) — the question only appears when the player picked mage.
A custom intro page "Describe your backstory" with a condition on character mode (character_mode is persona) — players who chose to play one of your world characters skip it entirely.

### Part 3: World Intro (Starting Without a Scenario)

Everything above is scenario-scoped — the player picks a scenario and the wizard derives its setup from that scenario's fields and toggles. You can also give the world itself an intro, so a player can begin with no scenario at all. This is the "AI Dungeon style" start: set up your character, then choose where you spawn.

On the wizard's Scenario page, a world that has an intro authored shows a Begin here option alongside the scenario list. Selecting it runs the world's own intro instead of a scenario's, and starts a fresh chat with no scenario attached.

### Where to author it

Open the Introduction tab in the world editor. Alongside the custom-introduction page list, you'll find the world-level intro authoring:

Start questions — the same field editor as the scenario's setup questions, but the questions live on the world rather than a scenario. All field types, per-field copy, pools, Required, Default, and match rules (including keyword/regex text rules) work exactly as documented above. World intro fields support the same grant_currency and grant_property bindings as scenario fields — a class or background choice made during the world intro can grant the player currency or property at session start.
Include Choose Your Character / Include Build Your Stats toggles and the playable roster grid — the world-level equivalents of the scenario toggles.
World intro opening — the world-level counterpart to a scenario's premade greeting. It renders once when the chat starts and can branch on the player's intro answers via Handlebars macros (see the Immersive Greetings section below). Leave it empty and the chat opens with no greeting.
If you author a custom-introduction page list, it orders the world intro exactly as it orders a scenario intro. If you leave the page list empty, the wizard auto-derives pages from your world intro fields and the two toggles — the same auto-derivation described at the top of Part 2, just sourced from the world.

### Default starting location

When a world intro is used instead of a scenario, there is no scenario to set the starting location. The player's starting location is determined by:

A Set spawn location binding on a question (see below) — the answer picks the location explicitly.
Falling back to the world's Default Starting Location if no question resolves one.
This is why the Default Starting Location matters: it is the guaranteed fallback for any session that reaches the chat without a scenario or spawn-location answer providing a location.

### Spawn location — let the player choose where they start

Add a Location question (field type Location, internally rendered as selectable location cards) and give it the Set spawn location binding. The location the player picks becomes their starting location — the new chat opens there, and the party's current location is set to it.

Optionally restrict the offered locations to a specific pool so the player only sees valid starting points. Leave the pool open to offer all of your world's locations.

### Faction → location — place the player by their allegiance

You can also set the spawn location indirectly, from a non-location answer like a faction choice:

Add a Select question (e.g. "Choose your allegiance") with the options you want.
Give it the Set spawn location binding, then fill in the location map: each option value → a location. For example: dawnguard → the Citadel, nightwatch → the Frostgate, free_cities → the Harbor.
When the player picks a faction, its mapped location becomes their starting location.

### Part 4: Custom World Introduction

For full control over the intro, open the Introduction section in the world editor sidebar and turn on Custom world introduction.

Turning this on overrides the auto-derived flow. The wizard shows exactly the pages you author, in your order, instead of deriving them from scenario toggles and fields.

### Building the page list

Click Add page to append a page. Each page has a type dropdown and a Title. Use the up/down arrows to reorder and the trash icon to delete. Click Save introduction when done — persona presets and stat templates save with the same button.

### Page types

### Page type What it does
Info / Slide A presentational page: a Markdown body with embedded gallery images. Writes nothing — pure narrative flavor. Use for a cold-open, a "Welcome to…" slide, or setting lore.
Choose Character The Choose-Your-Character experience: personas, persona presets, and your playable roster.
Build Stats The Species/Occupation/Stats/Review build, honoring the world's stat config.
Select (scenario field) Renders a scenario field as an image-card or dropdown picker. Enter the scenario field id this page drives.
Field (scenario field) Renders a scenario field as a plain input (text, number, textarea). Enter the scenario field id.
Species A standalone species picker.
Occupation A standalone occupation picker.
For Select and Field pages you must supply the scenario field id of the field you want shown. The field itself — its type, pool, bindings, and match rules — still lives in the Scenario editor. The intro page just points at it and renders it in the right step of the wizard.

### Info / Slide bodies

Info pages give you a Markdown editor with an image-insert button (to embed gallery images at the cursor) and a preview toggle. This is the same editing experience as advanced character greetings.

### Part 5: Persona Presets

Persona presets are ready-made starting points for a player who wants to be themselves but doesn't yet have a persona that fits your world. Each preset appears as a Suggested personas card on the Choose Your Character page. Tapping it opens the full persona editor pre-filled from your preset — the player tweaks and saves a genuine persona. Presets are seeds, not locks.

To add one: at the bottom of the Introduction section, click Add preset.

| Field                                                                                                                                                                                         | What it does                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Label                                                                                                                                                                                         | The name shown on the card in the wizard (e.g. "Veteran Trainer", "Rookie from Pallet Town"). This is not the persona's name — it's the card label. |
| Suggested name                                                                                                                                                                                | Pre-fills the new persona's name field.                                                                                                             |
| Pronouns                                                                                                                                                                                      | Quick-set — She/Her, He/Him, or They/Them — seeds all five pronoun forms.                                                                           |
| Avatar URL                                                                                                                                                                                    | Pre-fills the persona's avatar image.                                                                                                               |
| Description                                                                                                                                                                                   | Pre-fills the persona description. Also shown as the card's blurb on the preset card.                                                               |
| The preset carries any outfits and default outfit defined on it through to the persona dialog. Because the player lands in the full persona editor, they can adjust everything before saving. |                                                                                                                                                     |

### Part 6: Immersive Greetings

A scenario's premade greeting (authored under Premade Scenes in the Scenario editor) renders once when the chat starts — and it can react to the choices the player just made in the intro. Pick one starter creature and Snivy coils around the player's arm; pick another and Oshawott puffs up proudly. No scripting required.

### The rule: flavor in the field, payoff in the greeting

Put scenario flavor and narration in the field's Description (the help text), so it appears above the selector while the player is choosing.
The greeting should pay off the choice, not re-ask the question.

### The macros

Every intro choice with a Remember as variable binding is available in the greeting under its memory key:

{{memGet "key"}} — the raw value the player chose. For lexicon-backed picks this is the entry id; for Select/Text/Number fields it's the plain value.
{{memGet "key_name"}} — the readable display name for lexicon-backed picks. When the chosen value is a lexicon entry, the system also stores the entry's name under key_name. After a starter pick keyed starter, the greeting sees both {{memGet "starter"}} (the id) and {{memGet "starter_name"}} (e.g. "Snivy"). For multi-select picks, \_name is a comma-joined list.
key is the Memory key you set under Remember as variable, which defaults to the field's id.

### Branching on the choice

Use the ifEquals helper to write a different line per option:

{{#ifEquals (memGet "starter_name") "Snivy"}}Snivy coils calmly around your arm, tail flicking.{{/ifEquals}}
{{#ifEquals (memGet "starter_name") "Oshawott"}}Oshawott puffs up proudly, patting the scalchop on its belly.{{/ifEquals}}
{{#ifEquals (memGet "starter_name") "Tepig"}}Tepig snorts a happy little ember and trots in a circle.{{/ifEquals}}
A greeting with no macros renders exactly as before. This feature only does something when you opt in by adding macros.

### Available context in a greeting

memory — the party's memory states, including everything Remembered from the intro plus the \_name companions for lexicon-backed picks. Access via {{memGet "key"}} / {{#memExists "key"}}…{{/memExists}}.
persona — the player's persona (name, pronouns, description). Pronoun helpers like {{pronounSubjective}} resolve against it.
world, environment, location — the world and the scenario's environment/location objects.
Common helpers: memGet, memExists, ifEquals / ifNotEquals, ifGreater / ifLess, and / or / not, eq / ne / gt / lt, plus the pronoun helpers. These are the same Handlebars helpers used throughout prompt assembly.

### Premade greeting vs. AI-generated opening

The premade greeting is static — it renders once with the player's choices and never changes. That's ideal for a crafted, deterministic cold-open.

If you'd rather the opening be freshly written by the AI, leave the greeting empty and rely on the scenario's Scene Instructions instead. The AI already sees the chosen creature or loadout as live context (because the Activate as lore binding injects it), so it can narrate the player's choice naturally without you authoring per-choice branches. Use a premade greeting for authored precision; use Scene Instructions for AI-driven variety.

### Worked Example: A Pokémon-Style Trainer Opening

Here's how all the pieces above combine into a classic "choose your trainer, pick your starter, allocate your stats" flow.

In the world, create:

Two world characters for the trainer roster — Hilbert and Hilda — so players can play as a canon trainer.
Three creaturetype lexicon entries for the starters, each with an avatar.
In the Scenario editor:

Add a setup field, type Lexicon Picker, titled "Pick your starter". Pool in your three starters with Max Selections 1. Bindings: Activate as lore + Remember as variable, key starter.
Under Publishing → Guided Intro, turn on Include "Choose Your Character" and select Hilbert and Hilda in the Playable characters grid.
Turn on Include "Build Your Stats" using your world's stat config.
Save the scenario.
In the Introduction tab:

Add a couple of persona presets for players who'd rather be themselves — e.g. "Rookie from Pallet Town" (suggested name, They/Them, avatar, a one-line description). When a player taps it, the persona editor opens pre-filled. Do not add a separate name question.
Add a "Veteran Trainer" stat template with a pre-filled base_stats spread.
Optionally, for a narrative cold-open, turn on Custom world introduction and author the exact page order:
Info / Slide — "Welcome to the world of…" with a gallery image.
Choose Character — Hilbert/Hilda roster + persona presets + create-your-own.
Build Stats — point-buy allocation.
Select (scenario field) — point it at your "Pick your starter" field id.
Click Save introduction.
In the Scenario's premade greeting, write the choice payoff:

{{#ifEquals (memGet "starter_name") "Snivy"}}Snivy coils calmly around your arm, tail flicking.{{/ifEquals}}
{{#ifEquals (memGet "starter_name") "Oshawott"}}Oshawott puffs up proudly, patting the scalchop on its belly.{{/ifEquals}}
{{#ifEquals (memGet "starter_name") "Tepig"}}Tepig snorts a happy little ember and trots in a circle.{{/ifEquals}}
What the player gets: a welcome slide → pick Hilbert/Hilda or build their own trainer → allocate stats using the Veteran Trainer template as a starting point → pick a starter from three image cards → Begin. The chosen starter is injected as a <Creature> block for the AI, {{memGet "starter_name"}} is available in templates and InfoBoard, and the player's persona/character and stats are saved to the party.

### Common Mistakes

### "Players land in a session with no location."
Either the scenario has no Location set, or the world-level intro completed without a spawn-location answer and you haven't set a Default Starting Location on the world. Set a default starting location in World Details as your guaranteed fallback.

### "My opening scene is the same for every player."

You're using a Premade Scene instead of (or alongside) Scene Instructions. If a premade scene exists, it takes priority — remove it and use Scene Instructions if you want AI-generated variety.

### "Players are asked for their name."

Remove the name question. The player's persona or chosen world character supplies the name. A separate question is redundant for personas and breaks world-character immersion.

"A follow-up question appears for everyone, not just the right group."
Check the condition on that field. Make sure the Source points to the right field id and the Value exactly matches the option value (not its display label) that should trigger it.

### "My starter creature isn't showing up in the AI's responses."

Check that the Lexicon Picker field has the Activate as lore binding turned on. Remember-only stores a variable but doesn't inject the entry into the prompt. You need Activate for the AI to see the creature as live context.

### "Players can't see the Build Your Stats page on the world intro."

The Include "Build Your Stats" toggle must be turned on at the world level in the Introduction tab, not just on individual scenarios.

### "Keyword match rules on a text field aren't doing anything."

Confirm the field type is Text or Text Area — match rules only apply to free-text fields. Also confirm the keyword or regex pattern is correct; regex patterns are case-sensitive by default unless you include a case-insensitive flag.

"My scenario's Starting Properties or grant_property fields don't seem to do anything."
Both require the world to have at least one currency defined (Economy tab) and the target location to have Purchasable toggled on in its property settings. If either condition is missing, the grant silently has nothing to apply to. See the Property and Furnishings Market chapter for the full setup chain.

---

## RPG Stats & Blueprints

### RPG Stats and Blueprints

This chapter covers three foundational pieces of any RPG-capable world: turning on the gameplay features you need, configuring your stat system, and building the species, occupation, and trait blueprints that give characters mechanical identity at character creation.

### Enabling the RPG Features You Want

Where: World Editor → Simulation tab → World Features section.

Before any gameplay system exists in your world, you have to switch it on. Each toggle below enables a subsystem and reveals its corresponding editor. Nothing turns on automatically — you control exactly which systems your world uses.

### Feature flag What it does

Inventory Players can carry items, equip them, and use them. Adds the Inventory tab to the chat sidebar.
Currency Enables money. Required for marketplaces. Adds currency balances to the inventory display.
RPG Stats Enables stat-based mechanics — SPECIAL stats (or your custom stat system), species, occupations, traits. Adds the Stats tab to the chat sidebar.
Combat Enables battle mode and the Director's combat tools. Combat surfaces through chat narration, with stat changes reflected in the Stats tab.
Ships Enables vehicles that can travel between worlds. Most worlds don't need this.
Creatures Enables the creature-catcher system — party of creatures, dex, encounters, evolution, moves. Adds the Creatures tab to the chat sidebar.
Show Party Stats Includes party HP/MP/stats in the AI prompt so the AI knows how injured or exhausted everyone is.
Recommendation for new RPG worlds: Start with Inventory and Currency. Add RPG Stats once you have a clear sense of your stat system. Add Creatures last — it's the most involved subsystem and builds on everything else.

### Setting Up Your Stat System

Where: World Editor → Simulation tab → Stat Config section.

If you've enabled RPG Stats, this section is where you decide what stats your world uses. The default is SPECIAL: Strength, Perception, Endurance, Charisma, Intelligence, Agility, Luck. Most worlds can ship with these defaults and never look back.

If you want a different system — D&D's six stats, a four-stat magic setup, something you invented — you can fully customize every part of it:

| Field                                                                                                                                                                                                                                                                                                              | What it does                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stats                                                                                                                                                                                                                                                                                                              | The list of stats. Each has an ID, a label, an abbreviation, a description, and an enabled toggle. Disable the SPECIAL stats you don't want, and add your own.                     |
| Allocation Method                                                                                                                                                                                                                                                                                                  | How players assign stats during character creation (see below).                                                                                                                    |
| Base                                                                                                                                                                                                                                                                                                               | Value / Max Value / Point Budget Numbers used for point-buy. Defaults: base 3, max 8, 21 points to spend.                                                                          |
| HP                                                                                                                                                                                                                                                                                                                 | Label / MP Label What you call "HP" and "MP" in this world. "Vigor" and "Mana" are common alternatives.                                                                            |
| Stat Roles                                                                                                                                                                                                                                                                                                         | Which stat drives which combat behavior. By default, HP comes from Endurance, MP from Intelligence, physical attack from Strength, and so on. Remap these to match your stat list. |
| Vital Labels                                                                                                                                                                                                                                                                                                       | Threshold-based display labels for HP and MP — e.g., below 25% shows as "Critical" instead of a bare number.                                                                       |
| Stat Value Labels                                                                                                                                                                                                                                                                                                  | Threshold-based labels for any stat — e.g., a Strength of 6 shows as "high" instead of "6."                                                                                        |
| Species / Occupations / Traits Enabled Toggles for the three blueprint systems described in the next section.                                                                                                                                                                                                      |                                                                                                                                                                                    |
| Allocation                                                                                                                                                                                                                                                                                                         | Method                                                                                                                                                                             |
| Method                                                                                                                                                                                                                                                                                                             | How it works                                                                                                                                                                       |
| Point Buy                                                                                                                                                                                                                                                                                                          | Default. Players spend a pool of points (21 by default) to raise stats from the base value (3) up to the max (8). Every point spent raises one stat by one.                        |
| Fixed                                                                                                                                                                                                                                                                                                              | Every character starts with the same preset values. Good for worlds where all players are on equal footing with no customization.                                                  |
| Free Assign                                                                                                                                                                                                                                                                                                        | Players can put any number in any stat, unconstrained.                                                                                                                             |
| Roll                                                                                                                                                                                                                                                                                                               | Stats are rolled with dice.                                                                                                                                                        |
| Why Stat                                                                                                                                                                                                                                                                                                           | Roles matter                                                                                                                                                                       |
| The combat engine doesn't know what "Strength" means by name. It knows that a physical attack check uses whatever stat you've mapped to the physical attack role. By default that's Strength, but if your world uses "Brawn" and "Finesse" instead, you remap the physical attack role to whichever of those fits. |                                                                                                                                                                                    |

This is what lets you build a fully custom stat system and still have combat work correctly out of the box. Roles are the bridge between your world's vocabulary and the underlying math.

The available roles cover: HP scaling, MP scaling, physical attack, magic attack, physical defense, magic defense, speed (turn order), and accuracy.

### Stat Value Labels

If you set labels at thresholds — say, 0 = "poor," 3 = "average," 6 = "high," 8 = "exceptional" — the AI sees Strength: high in its prompt rather than Strength: 6. This is a display and AI-context choice. The number is still the number internally; it just gets translated into a word the AI can write around more naturally.

You can leave this empty and let numbers speak for themselves. Labels work best in worlds where you want the AI to describe characters in qualitative terms rather than mechanical ones.

### Species, Occupations, and Traits (Blueprints)

Where: World Editor → RPG tab.

These are the three character-creation building blocks. A player picks one species, one occupation, and any number of traits when they create their character — or you assign them when setting up an NPC. Each blueprint adjusts the character's base stats and carries flavor text the AI uses when writing that character.

All three systems are optional and can be enabled or disabled independently in your Stat Config settings.

### Species

Species are biological or origin-based templates: Elf, Dwarf, Robot, Cybered Human, Forest Elemental. Each species has:

Name and description — shown to the player during character creation and included in the AI's context.
Stat modifiers — additive bonuses or penalties applied to base stats (e.g., Elf: +1 Agility, −1 Endurance).
Avatar — optional image shown in the picker UI.
If your world has no biological variety — everyone is the same species — just don't create any. The blueprint system is entirely opt-in. An empty species list means character creation skips the species step.

### Occupations

Occupations are class or profession archetypes: Warrior, Merchant, Spellblade, Hacker, Wanderer. Same fields as species — name, description, stat modifiers, avatar. A character has exactly one occupation.

Occupations are a good place to encode the mechanical identity of different playstyles. A Warrior might get +2 Strength and +1 Endurance; a Scholar might get +2 Intelligence and +1 Perception. The AI also uses the occupation description when narrating the character's actions, so write it in a way that communicates both the stat identity and the narrative flavor.

### Traits

Traits are smaller modifiers a character can stack: "Quick Reflexes," "Thick Skinned," "Silver-Tongued," "Lucky." Same fields — name, description, stat modifiers. A character can have many traits simultaneously.

Traits are good for:

### Fine-tuning a build after species and occupation are set

### Representing injuries, blessings, or permanent conditions
Adding narrative texture without forcing a full class change
Giving NPCs distinguishing mechanical details without overbuilding their sheets
How modifiers stack
When the system computes a character's effective stats, it adds everything together:

### base stats

- species modifiers
- occupation modifiers
- sum of all trait modifiers
  Equipment modifiers (from equipped items) and active status effects layer on top of that. So if you give Elves +1 Agility, the Rogue occupation +1 Agility, and the "Cat-Quick" trait +1 Agility, a Cat-Quick Elven Rogue has +3 Agility before any gear or buffs. That's the intended design — blueprints are additive by default, and players (or you) choose how far to stack them.

There is no diminishing returns or cap at the blueprint level. If you want stat caps, set them via the Max Value field in your Stat Config.

### What comes next

With features enabled, stats configured, and blueprints defined, your world has its mechanical skeleton. The next chapters cover building out the economy (currencies and marketplaces), the item lexicon, and creature systems — all of which build on the stat foundation you've laid here.

---

## Combat

### Combat

Combat in WyvernChat is an optional RPG layer — once you have stats enabled for your world, the Combat tab in the world editor lets you decide exactly how battles are resolved, narrated, and felt. This chapter walks through every authoring choice you'll face, explains what each one produces in play, and offers clear guidance on when to pick what.

The Combat tab only appears after you enable RPG stats for your world. If you don't see it, visit your world's Settings or Simulation tab and turn on RPG stats first. See Chapter 7 — RPG Stats & Blueprints for how to set those up.

If you never open the Combat tab, your world still runs fights using a solid set of defaults. Open it when you want battles to feel like your game — not a generic one.

### Start with a preset

The easiest way in is to click one of the preset buttons at the top of the tab. Each fills every setting with a coherent starting configuration. Tweak from there.

Pokémon-style — stat-driven numeric combat: move power plus attacker stats versus defender stats, type effectiveness, critical hits. Designed for creature-catcher or monster-battler worlds where the math should track like a game.
D&D-style — dice-and-outcomes combat: each action rolls against a difficulty and lands on a tier (critical success, success, failure, or fumble), and the AI narrates that tier. Designed for adventure and tabletop-flavored worlds where drama matters more than arithmetic.
Fallout / VATS — coming soon; currently disabled.
You can change any individual setting after applying a preset — presets are a starting point, not a lock-in.

The central choice: how is an attack decided?
The Combat Style setting is the most important decision you'll make. It controls the fundamental resolution mechanic for every attack in your world.

### Storyteller (dice and outcomes)

Every action rolls against a difficulty and lands somewhere on a four-tier scale: critical success, success, failure, or fumble. The AI is told which tier landed and narrates accordingly — a desperate swing that finds a gap in the armor, a glancing blow that barely connects, a humiliating stumble.

Choose Storyteller when:

Combat is about drama, tension, and cinematic description.
You're building an adventure world, a dark fantasy, or a tabletop RPG setting.
You want the AI to have interpretive latitude in how it describes a fight.
You don't need the hit points to track like a video game.

### Numbers (stats and damage)

Attacks use a real damage formula — move power, attacker stats, defender stats, type effectiveness, hit chance, and critical hit chance all feed into a numeric result. The AI is not told the number; it receives a description of the result (a heavy hit, a glancing blow, super effective, missed) and narrates from there.

Choose Numbers when:

You're building a creature-catcher, monster-battle, or competitive-style world.
You want fights to "add up" — where a tankier creature genuinely survives longer and a faster one genuinely moves first.
Players should feel like the system has real rules underneath.
Your moves have power values and your type chart is configured.

### Mixing the two

The toggle "Use different rules for creatures vs characters" lets you run both styles in the same world. The classic use case is a Pokémon-inspired world: creature-versus-creature battles use Numbers (full stat math), while human-character duels use Storyteller dice. Turn the toggle off to apply one style to everything.

### Telling the engine what your stats mean (Role Mapping)

Your world's stats can be named anything — HP, Vitality, Endurance, Grit, whatever fits your setting. Combat doesn't care about names; it cares about roles. The role-mapping dropdowns let you point each combat role at whichever of your stats fills that function:

Attack power — the stat that makes hits harder (your Attack, Strength, Magic Power, etc.)
Defense / damage soak — the stat that reduces incoming hits (your Defense, Toughness, Armor, etc.)
Initiative / turn order — the stat that determines who acts first (your Speed, Agility, Reflex, etc.)
Health pool — the stat that scales maximum HP (your HP, Endurance, Constitution, etc.)
Once mapped, every formula in the system uses the right stat automatically. This is what allows a Pokémon world and a gritty swords-and-sorcery world to both work without touching any underlying code.

Role mapping also appears in the Simulation tab — it is the same setting. Edit it in either place.

### Health and energy pools

Here you set how large health and energy (MP/stamina) pools are:

Base amount — the minimum HP or energy any character starts with, independent of stats.
Per stat-point growth — how much each point of the health or energy stat adds to the pool. Higher means stats matter more; lower means everyone's closer to the same baseline.
Per level growth — how much HP or energy increases each time a character gains a level.
Tuning these together determines the pace of combat. High base + high per-level = long, attrition-heavy fights. Low base + low growth = fast and lethal. There's a matching set of controls for the energy pool if your world uses one to power special moves.

### Turn order

Also configured here: who acts when.

By stat — the character with the higher initiative stat always acts first each round. Predictable, tactical.
By roll — each character rolls for initiative each round. Swingier; anyone can go first.
Simultaneous — all characters act at the same time, no turn order. Works best for free-form or narrative-forward combat.

### Numbers-style settings

These controls only appear when you've chosen Numbers as your combat style. They let you tune the formula.

### Damage style

How raw damage is calculated before it reaches the target:

Power + attack − defense — a straightforward additive formula. High-attack characters deal reliably high damage; high-defense targets reduce it consistently. Familiar to players of classic JRPGs.
Ratio (attacker vs. defender stats, Pokémon-like) — damage scales with how much the attacker's stat outpaces the defender's, optionally amplified by level. A strong attacker versus a weak defender does much more damage than the stat difference would suggest linearly; a close matchup produces modest results. Best for creature-battle worlds.
Fixed-power move — the move has a set base damage; the target's defense softens the blow but cannot fully block it. Useful for special attacks or abilities that should always deal meaningful damage.

### Accuracy

Always hit — attacks never miss. Simpler; removes a frustration point.
Roll against the move's hit chance — moves can miss, creating moments of relief or tension. Requires your moves to have hit-chance values configured.

### Critical hits

Set the crit rate (how often a critical hit occurs) and the crit multiplier (how much extra damage it deals). The AI is told a crit landed but never sees the multiplier — it narrates something appropriately dramatic.

### Type effectiveness

When enabled, the type chart you've configured for your world applies to every hit. Moves can be super effective, resisted, or completely immune, and the AI is told the effectiveness tier so it can reflect it in description (a devastating strike, an ineffective blow, completely blocked).

For type effectiveness to work, your moves need type values and your world's type chart needs to be configured. See Chapter 10 — Creatures, Moves, Natures & Abilities for how to set that up.

### Storyteller-style settings

These controls only appear when you've chosen Storyteller as your combat style.

Base difficulty — how hard a typical action is to land on the four-tier scale. Raise it to make combat grimmer and more punishing; lower it for heroic, action-forward play.
Attack modifier stat / defense modifier stat — which of your stats shifts the attack roll up or down, and which raises the difficulty the attacker is rolling against.
Critical margin — how far above the difficulty threshold counts as a critical success, and how far below counts as a fumble. A small margin makes crits and fumbles common; a large margin makes them memorable exceptions.

### Battle Mode: what the AI sees during a fight

While a battle is active, the AI receives a short briefing alongside the normal world context. The Battle Mode section lets you write and frame that briefing.

Label — the heading for the battle briefing block in the prompt (e.g. "Active Battle," "Pokémon Battle," "Encounter"). Defaults to something sensible if left blank.
Battle instructions — guidance for how the AI should narrate combat: the tone, pacing, and style you want. Leave this blank to use the system default. Add it when you want something specific — visceral and punishing, lighthearted and energetic, coldly tactical.
Wrapper tags — optionally wrap the battle briefing in opening and closing tags (for example <Battle> / </Battle>) instead of a plain label heading. Use this if your world's prompts use a tagged structure and you want combat to match.
Show enemy health — tells the AI whether the opponent is fresh, hurt, badly hurt, or on the verge of collapse. On by default. Turn it off if you prefer the AI to infer enemy condition from the fight's history rather than having it stated outright.

### How combat reads in play

A few things that are worth understanding as a creator, because they shape how your tuning choices land:

The AI never sees raw numbers. The engine translates every numeric result into language before the AI reads it: "a heavy hit," "the foe is badly hurt," "super effective," "a glancing blow." This means the AI narrates mood and drama, not arithmetic. The underlying numbers are tracked accurately behind the scenes — they just stay there.

The story reflects what actually happened. When a player uses a battle action, the real resolved outcome (the hit that connected, the miss, the capture that worked) is fed into the AI's briefing so its narration matches what actually occurred — not a guess, not an improvisation.

Players can expand the details. Every battle message includes an Actions strip players can open to see the actual rolls, damage values, and step-by-step results. This is visible to players, not part of the AI briefing.

Rerolls stay consistent. If a player swipes or regenerates a battle reply, the resolved outcome stays the same — the new narration describes the same hit, the same miss, the same result, just written differently.

### Quick recipes

### "I want Pokémon-style creature battles."
Click the Pokémon-style preset. Map your creature stats to the Attack, Defense, Speed, and HP roles. Make sure your creature moves have power values and types, and configure your type chart. Enable type effectiveness in the Numbers settings. Done.

### "I want classic tabletop adventure combat."

Click the D&D-style preset. Map your stats to the appropriate roles. Optionally raise the health base and per-level growth to give characters more room to breathe across a long encounter.

"I want Pokémon battles for creatures but narrative duels for human characters."
Click Pokémon-style. Turn on "Use different rules for creatures vs characters." Set the character-specific combat style to Storyteller. Configure both sets of stat role mappings.

### "I want fast, lethal fights with no misses."

Choose Numbers. Set accuracy to always hit. Lower the base HP and per-level growth so fights end in a few exchanges. Crit rate is optional flavor.

### "I want heroic high-fantasy combat where the heroes usually succeed."

Choose Storyteller. Set a lower base difficulty. Set a small critical margin so strong rolls land as crits often. Describe the style you want in the battle instructions — something that biases the narration toward momentum and triumph.

---

## Items, Currencies, and Markets

### Items, Currencies, and Markets

Everything a player can pick up, spend, and buy lives in three interlocking systems: items defined in the Lexicon, currencies tracked on the party, and marketplaces attached to locations. This chapter covers all three — what each field does, how they connect, and what a player experiences at the end.

### Items Are Lexicon Entries

Items aren't a separate content area. They live in the Lexicon tab like any other entry; the only difference is that their Type is set to item. That means an item automatically gets everything a lexicon entry has — a name, description, avatar, activation keys, conditional display, and timeline gating — plus an additional set of item-specific fields.

This also means the AI can "know" about an item as lore whenever the item's keys come up in conversation, the same way any lexicon entry activates. The item is both a mechanical object and a piece of world knowledge at the same time.

To create a new item: Lexicon tab → New Entry → set Type to Item.

### Item Fields

| Field                                                                                                                                    | What it does                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stackable                                                                                                                                | Lets the player carry more than one in a single inventory slot. Turn on for potions and arrows; leave off for unique gear.                                                            |
| Max Stack                                                                                                                                | The maximum quantity that fits in one stack. Leave blank for no limit.                                                                                                                |
| Consumable                                                                                                                               | Removes the item from inventory when used.                                                                                                                                            |
| Tradeable                                                                                                                                | If off, the item can never be sold to any marketplace.                                                                                                                                |
| Key Item A stronger lock than                                                                                                            | Tradeable: the item can't be sold, dropped, or discarded. Use for plot badges, unique relics, and quest completion tokens.                                                            |
| Rarity                                                                                                                                   | A free-form label ("common," "epic," "mythic"). Affects display only — you decide what these labels mean in your world.                                                               |
| Weight                                                                                                                                   | Optional, for encumbrance systems.                                                                                                                                                    |
| Value                                                                                                                                    | The base price in one or more currencies, e.g. { gold: 50 }. Marketplaces use this as the default buy price.                                                                          |
| Equip Slot                                                                                                                               | If the item is wearable or wieldable, which slot it occupies. The eleven available slots are: head, body, legs, feet, weapon_main, weapon_off, ring1, ring2, necklace, cape, trinket. |
| Effects                                                                                                                                  | What the item does when used or equipped (see below).                                                                                                                                 |
| Crafting Recipe                                                                                                                          | An optional list of ingredient items and quantities needed to craft this item.                                                                                                        |
| Teaches Move                                                                                                                             | If set, using the item teaches the named move to a creature.                                                                                                                          |
| Flags                                                                                                                                    | Free-form key-value pairs that scripts or conditional lexicon entries can check, e.g. { badge: true }.                                                                                |
| Item                                                                                                                                     | Effects                                                                                                                                                                               |
| Effects are what an item does — its damage, its healing, the stat bonuses it provides while equipped, the status conditions it inflicts. |                                                                                                                                                                                       |

### Passive effects (apply while equipped)

These take effect as long as the item is in an equipped slot:

### Effect What it does

Base Damage / Damage Type For weapons. Damage type is one of: blunt, slashing, piercing, poison, shocking, flame, frost, psychic, holy, dark.
Armor Value Reduces incoming damage. For shields, body armor, heavy boots.
Stat Modifiers While equipped, raises or lowers specific stats (e.g., a Ring of Wisdom: +2 Intelligence).
Applied Status Effects The wielder gains these status effects while the item is equipped (e.g., "Blessed" while wearing holy armor).
Target Status Effects When the weapon hits, roll for these effects on the target (e.g., 30% chance of "Burning" from a flame sword).

### Active use effects

Enable the Usable toggle and these apply when the player actively uses the item. Effects run in order — you can stack several on a single item (a potion that heals and cures a poison, for example).

### Choosing a target

The Target field controls who the item is aimed at when used:

No target — takes effect without picking anything. Good for torches, self-drinks.
The player — always targets the player character.
A party creature — the player picks one creature in their party.
A character — the player picks an NPC or character in the current scene.
An enemy in battle — only valid during an active fight.
Any — the player chooses from all available targets.

### Use settings

Narrate — when on, using the item triggers an AI-narrated story beat. The storyteller describes what happens in prose: the warmth of the potion, the creature stirring as it revives. Turn it off for silent mechanical effects.
Consume — when on, the item is removed from inventory after use.
Usable In — restricts when the item can be used: Anytime, Only in battle, or Only outside battle.

### Effect types

### Effect What it does

Heal (HP) Restores a flat amount of the target's hit points.
Heal % of max HP Restores a percentage of maximum HP. Useful when party members have very different health pools.
Revive Brings a knocked-out creature or character back, restoring them to a set HP amount.
Restore energy / MP Refills the target's mana or energy pool.
Apply a status Inflicts (or gifts) a status effect on the target — poison, paralysis, haste, whatever your world defines.
Cure a status Removes a specific status effect from the target. An antidote for poison.
Buff a stat Raises a stat by a set amount. Set a duration in in-world hours for a temporary buff, or leave blank for permanent.
Teach a move The target learns a move from your world's move list. Classic for spellbooks or training manuals.
Evolve Triggers a creature's evolution. The evolution target is defined on the creature entry; this effect fires the trigger.
Deal damage Deals a set amount of damage to the target. For throwing weapons, explosives, or offensive consumables.
Shift a relationship Changes how a character feels about the player. Two modes: by moodlet (a named feeling from your Relationships tab, lasting its normal duration) or by amount (push long-term affinity directly up or down by a number). Described further below.
Give / take currency Adds or removes currency from the player's wallet. Useful for found coin pouches or paid tolls.
Set a flag Marks a named flag on the party state, checkable by scripts and conditional lexicon entries.
Narration only No mechanical change. Triggers an AI story beat without altering any numbers — for flavor items and atmosphere props.

### Gift value and relationships

The Shift a relationship effect is what makes gifts mechanically meaningful. When a player types >gift <item> to <character> (or uses the item on a character from the inventory screen), the relationship shift fires and the AI narrates the exchange — without ever showing the player a number.

This connects directly to the world's Relationships system. If your world has Relationships enabled, every character has an affinity score and a set of active moodlets toward the player. Giving a treasured keepsake might apply a "deeply moved" moodlet for several in-world hours. Giving something cheap or unwanted could apply "mildly insulted." The moodlet name and duration are yours to define; the engine handles the rest.

Full details on how affinity and moodlets work — including how characters express them in dialogue and how the AI reads them — are covered in the Relationships chapter.

### How Players Use Items

From the inventory panel: Open the Inventory tab in the chat sidebar, find the item, and open its detail view. If the item is usable and the context matches its restriction, a Use button appears. Tap it, pick a target if needed, confirm.

Via chat commands: Players can type directly in chat without opening the sidebar:

> use <item> — uses the item without a target.
> use <item> on <target> — uses the item on a named target, e.g. >use antidote on Mira.
> gift <item> to <character> (also >give <item> to <character>) — presents the item as a gift. If the item has a relationship-shifting effect, it fires here.
> Vehicles (A Special Kind of Item)
> Set an entry's Type to vehicle instead of item and it gets an extra Vehicle Config section. Vehicles let players board them and travel between locations — ships, airships, hover-bikes, magical mounts.

### Vehicle field What it does

Mediums What kind of travel the vehicle enables: water, air, etc. Determines which routes the vehicle can use.
Speed Multiplier 1.0 = normal travel time. 2.0 = half the time. 0.5 = twice as long.
Capacity Maximum party size that fits aboard.
Locations Rooms inside the vehicle (the captain's quarters, the cargo hold). Players can move between these while aboard.
Character Pool Crew NPCs who appear when the player is inside the vehicle.
Lexicon Entries Lore that loads while aboard — the ship's history, a captain's log, ambient atmosphere.
World Routes Cross-world travel routes. Only relevant if you've enabled the Ships feature and built a multi-world setup.
Context Description / Final Instructions Override the world's normal context while the player is aboard the vehicle.

### Currencies

Where: World Editor → Economy tab.

A world can have any number of currencies. Most worlds only need one. Some need several — gold for commerce, faction tokens for reputation, soulpoints for a specific mechanic that shouldn't convert to gold.

| Field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | What it does                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name "Gold," "Crystal Shards," "Empire Marks."                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                             |
| Symbol                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Optional short symbol or sigil shown beside amounts.                                                                                                                        |
| Icon                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Optional avatar image.                                                                                                                                                      |
| Decimal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Places 0 for whole-number currencies. 2 if you want fractional values.                                                                                                      |
| Is Primary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The world's default currency. The first one you add becomes primary. Used as the assumed currency when prices are unspecified.                                              |
| Universal Credit Rate                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The one number that makes currencies convertible. See below. Leave it blank for any currency that should not convert into others (faction tokens, soulpoints, quest items). |
| How currencies convert — the Universal Credit Rate                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                             |
| There is exactly one conversion setting you fill in: the Universal Credit Rate. Think of the Universal Credit (UC) as a shared measuring stick that every currency can be priced against. You give each currency a UC value — "1 gold = 10 UC," "1 silver = 0.1 UC" — and that's it. From there, the marketplace converts any currency into any other currency automatically, because they all measure against the same stick. The same number is also what lets a currency travel between worlds. |                                                                                                                                                                             |

So if a player has silver and an item is priced in gold, the marketplace works out the gold price through UC and lets them pay — no manual exchange step, nothing else for you to set.

To keep a currency separate, leave its Universal Credit Rate blank. With no UC value, it has no conversion path, and the marketplace refuses payment in it for anything priced in another currency — exactly what you want for faction reputation, soulpoints, or quest tokens that shouldn't be buyable with gold.

Conversion is anti-arbitrage: when buying, the system picks the path that costs the player the most; when selling, the one that pays out the least. Players can't game it by chaining conversions. Buy prices round up; sell payouts round down.

Advanced (optional, AI-assistant only): the engine also supports a direct fixed rate between two specific currencies — say, locking gold-to-silver at exactly 100:1 regardless of what the UC math would give. There's no field for this in the editor; the AI world-assistant can set it for you if you ask. A direct rate, where one exists, takes priority over the UC calculation. Almost no world needs this — setting a Universal Credit Rate on each currency is all conversion requires.

### Player balances

Currency balances live on the party, not on the player account. A player who has multiple parties in your world has separate balances for each. Players earn currency from quests, battle rewards, and selling items.

### Marketplaces

Where: Locations tab → edit a location → Marketplace section.

Marketplaces are attached to locations. A specific tavern can be a shop; the open wilderness can't. Players see a Marketplace button in their inventory panel when they're standing at a location with one enabled.

### Marketplace field What it does

Enabled The master switch. Off means no marketplace here.
Name Optional display name shown to the player, e.g. "Old Marn's Sundries."
Description Optional flavor text.
Inventory The list of items for sale (see below).
Buy Rate When players sell items here, this multiplier determines the payout. 0.5 means the shop pays 50% of the item's value.

### Marketplace inventory entries

Each inventory entry references one item lexicon entry:

### Entry field What it does

Lexicon Entry The item being sold.
Stock How many are available. Leave blank for unlimited.
Price Override Override the item's base Value for this specific shop. { gold: 75 } ignores the item-level price.
Restock Cycle In-world hours before the shop restocks.
Unlock Conditions Optional gating — the item only appears when certain party conditions are met, e.g. "after the player has spoken to the Mayor."
How players buy and sell
When a player is at a location with Marketplace enabled, the inventory tab shows a Marketplace button. Opening it shows a buy/sell dialog:

The player picks which currency to pay or receive in (if multiple are valid).
Their current balance is visible.
Each item shows its buy price, sell price (base value × buy rate), stock count, and quantity controls.
Buy is disabled if the player can't afford the total.
Sell is disabled if the item has Tradeable turned off.
Buying decrements stock (if finite), deducts currency, and adds the item to the player's inventory. Selling removes the item from inventory and pays out at the reduced rate.

Players can also buy directly from the chat with >buy <item> while at a location with a marketplace — the system finds the item in the current shop's inventory, charges the default currency at the listed price, and confirms or declines in a system message.

### Recurring Costs and Income — Rent, Bills, and Jobs

Beyond one-time purchases, RPG worlds can charge ongoing costs and pay ongoing income as in-world time passes. These work through two configuration areas: upkeep fields on purchasable locations, and jobs lists on any location.

### Rent and Bills

When you mark a location as purchasable (Locations tab → property section), two additional upkeep fields appear:

Rent — a recurring cost the player pays to keep holding the property. Think of it as a lease payment: landlords in your world expect regular gold. Set an amount, a currency, and a period.
Bills — a list of separate recurring costs, each with its own amount, currency, and period. Model utilities, maintenance fees, guild dues — anything the property incurs that doesn't feel like rent.
Period options: Daily, Weekly, Monthly, or a custom number of in-world hours. A "Daily" period bills once per in-world day regardless of how many real minutes have passed.

Both fields are optional. A property can have rent only, bills only, both, or neither. Owned properties with no upkeep are entirely free to hold.

### Jobs — Help Wanted

Jobs are Lexicon entries — the same kind of entry you use for items and furniture, with their Type set to Job. Authoring a job in the Lexicon means you write it once and can offer it at as many locations as you like, or post it to the world's global Job Board so players can take it from anywhere in the world.

### Creating a Job Lexicon Entry

Go to the Lexicon tab, create a new entry, and set its Type to Job. Alongside the standard lexicon fields (name, description, activation keys, etc.), you will see a Job Config section:

| Field                            | What it does                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wage                             | Amount earned per period.                                                                                                                                                                                                                                                                                                                          |
| Currency                         | Which currency the wage is paid in.                                                                                                                                                                                                                                                                                                                |
| Pay Period                       | How often the wage pays out: Daily, Weekly, Monthly, or a custom number of in-world hours.                                                                                                                                                                                                                                                         |
| Scope                            | Global — the job appears on the world Job Board and can be taken or paid from anywhere in the world (ideal for remote work, freelance contracts, or off-site positions). Local — the job only appears at locations that list it under "Jobs Offered Here."                                                                                         |
| Only paid while at the workplace | When on, wages only accrue while the player's party is physically at the source location. When off, the player earns wages by the calendar regardless of where they are.                                                                                                                                                                           |
| Offering a Job at a              | Location                                                                                                                                                                                                                                                                                                                                           |
| Open a location in the           | Coordinates tab. In the Jobs Offered Here section, add one or more Job lexicon entries by name. Any Local-scope jobs linked here will appear in the player's Ledger when they are at that location. Global-scope jobs can also be linked to a location (the player can take it in person), but they will still appear on the Job Board regardless. |

### The Job Board

When a player opens the Ledger, a Job Board section lists every Global-scope job in your world. These are remote or world-available positions — the player can take them from anywhere, and wages are paid regardless of where the party is located (unless you turned on "Only paid while at the workplace," in which case they need to be at the linked source location).

### Taking and Quitting

Players take a job with >takejob <name> from chat, or by tapping the Take button in the Ledger panel. They can hold multiple jobs simultaneously. To quit, the player uses >quitjob <name>, or taps Quit in the Ledger's Income section.

### How Settlement Works

Upkeep charges and wages are not billed in real time — they settle whenever in-world time advances. That happens in two situations:

Traveling between locations with a defined travel time.
Advance Time actions (e.g., the sidebar "Rest for the night" controls, or the >rest / >advance-time commands).
When time advances, the system calculates how many full periods have elapsed for each cost or income source and applies them all at once. If you time-skip forward two in-world weeks, each weekly bill fires twice, and each weekly wage pays twice. No periods are skipped — every elapsed cycle settles.

A summary message appears after settlement:

Rent paid — 500 Gold. Tavern Hand wage received — 280 Gold. City Utilities — 200 Gold: insufficient funds. Added to your debts.

Only full periods are settled. A partial period that hasn't elapsed yet carries over and settles on the next time advance.

### Debt

If a player cannot cover a cost — because they don't have enough of the required currency — the shortfall becomes debt rather than a hard block. The player keeps the property and continues playing; the debt accumulates and is shown in the Ledger. The AI is also aware of outstanding debts and may reflect them in the story — a landlord grumbling about overdue rent, a merchant being reluctant to do business.

Players can pay down debt anytime with:

> paydebt <amount> [currency]
> Omitting the currency defaults to the world's primary currency. Partial payments are applied in full.

### The Ledger

The Ledger is a sub-tab inside the Items & Property panel in the world sidebar. It is the player's central view of their economic obligations and opportunities:

### Section What it shows

Costs All active upkeep items — rent and bills on every owned property — with the amount, currency, period, and next due time.
Income All held jobs, with wage, period, and a note if the job requires physical presence.
Debts Any outstanding unpaid costs, with a Pay button for quick repayment.
Job Board All Global-scope jobs in the world, takeable from anywhere.
Jobs Here Jobs offered at the player's current location, with a Take button for each.
History A log of recent settlement events: what was paid, what was earned, and any debts that were added.
The Ledger updates automatically whenever time advances. It does not require navigating to a specific tab — all the player's recurring obligations and options are visible in one place.

### Inline Commands

### Command What it does

> paydebt <amount> [currency] Pays down the specified amount of debt. Omit the currency name to default to the world's primary currency.
> takejob <name> Takes the named job (from the current location's offerings or the Job Board).
> quitjob <name> Quits a currently held job.
> rent <property> Rents the named property at the current location, beginning the lease.
> Creator Notes
> Rent vs bills: Use rent for the headline cost (the lease) and bills for incidentals. The distinction is cosmetic — both are just recurring charges — but naming them separately makes the player's financial picture clearer.
> Balance matters: If upkeep is too high relative to available wages, players will accumulate debt quickly. Test your economy by running through a week of in-world time and checking what the net position looks like.
> Global vs Local scope: Use Global for remote contracts, freelance positions, or jobs the player should be able to take from anywhere. Use Local for on-site roles (blacksmith's apprentice, tavern hand) that only make sense if the player is at that establishment.
> "Only paid while at the workplace" is useful for immersive on-site employment — the player has to show up to earn. Turn it off for passive income or background gigs that don't need physical presence.
> Reusable jobs: Because a Job is a Lexicon entry, the same "Field Harvester" entry can be offered at multiple farm locations without duplicating the configuration. Update it once and every location that offers it reflects the change.
> Debt is soft, not hard. The system never evicts a player or removes a property automatically. Debt is narrative friction, not a hard block. If you want hard consequences, use scripts or lexicon callbacks triggered by a debt flag.
> Common Mistakes
> "My item exists but doesn't show up anywhere." Items don't appear automatically. They have to reach a player's inventory through a marketplace, a battle reward, a command, or a manual grant via the inventory editor. The lexicon entry defines what the item is; it doesn't put one into the world.

"The Marketplace button isn't showing up." Three things to check: the location's Marketplace section has Enabled turned on; the world's Currency feature is on in the Simulation tab; and the player is actually at that location. The button only appears when all three are true.

"I want my currencies to stay separate." Leave the Universal Credit Rate blank on the currency you want isolated. With no UC value it has no conversion path, so the marketplace refuses payment in it for anything priced in another currency — exactly what you want for faction tokens or soulpoints that shouldn't be buyable with gold.

"Equipment modifiers aren't applying." The item needs three things: an Equip Slot set, a copy in the player's inventory, and the player must have equipped it from the inventory tab. Items with stat modifiers but no equip slot are treated as consumables — their modifiers don't apply passively.

---

## Creatures, Moves, Natures, and Abilities

### Creatures, Moves, Natures, and Abilities

The creature-catcher system lets you build a full collect-them-all experience inside your world: wild encounters in the wilderness, capture mechanics that reward strategy, creatures that grow and evolve alongside the player, type matchups you design yourself, and healing stations that serve as safe harbors between adventures. This chapter covers everything you need to author that system — from the creature lexicon entry itself to the per-location encounter and healing configuration.

Before you start: Make sure the Creatures feature flag is turned on. Go to World Editor → Simulation tab → World Features and enable Creatures. This adds the Creatures tab to players' chat sidebars and unlocks the encounter, healing, and creature-settings editors described below.

### Creatures Are Lexicon Entries

Creatures live in the Lexicon — the same place your lore, items, and moves do. To create one, go to World Editor → Lexicon tab → New Entry, then set the entry's Type to creature. The entry still has all the standard lexicon fields (name, content/description, activation keys, timeline gating, etc.) — that content becomes the creature's "flavor card," the lore text a player sees when they inspect it. On top of that, you get a full creature configuration panel.

### Creature Fields

| Field                                                                                                                                                                                                                           | What it does                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Intelligence mindless means the creature acts on a set behavior pattern. sapient means it acts via AI roleplay, like a character would. Most wild creatures should be mindless.                                                 |                                                                                                                                                                                                                                                                                   |
| Wild Behavior                                                                                                                                                                                                                   | For mindless creatures only. Options: aggressive (attacks on sight), defensive (only fights back), berserker (always attacks, ignores self-preservation), healer (prioritizes restoring allies), cowardly (flees when hurt), tactical (reads the situation and acts accordingly). |
| Types                                                                                                                                                                                                                           | The elemental or categorical tags this creature belongs to — fire, water, psychic, mechanical, or any labels you invent for your world. Types are used by the Type Effectiveness chart and by STAB (same-type attack bonus).                                                      |
| Capture Rate                                                                                                                                                                                                                    | A number from 0 to 100 representing the base chance to catch this creature. Hard-to-catch legendaries might sit at 5–15. Common starter creatures work well around 70 or above. Status effects and special capture items modify this further.                                     |
| Base Stats                                                                                                                                                                                                                      | The creature's stats at level 1, keyed to your world's stat IDs. If your world uses SPECIAL, you'd fill in values for Strength, Perception, Endurance, and so on. The stat mapped to your HP role (Endurance by default) determines how much health the creature has.             |
| Growth Rates                                                                                                                                                                                                                    | How much each stat increases per level. { strength: 0.5 } means the creature gains 0.5 Strength every time it levels up. Use this to shape whether a creature becomes a bruiser, a speed demon, or a well-rounded companion over time.                                            |
| Learnable Moves                                                                                                                                                                                                                 | The list of moves this creature can learn, each paired with the level it learns that move. At the specified level, the game offers the move to the player (or teaches it automatically, depending on your settings).                                                              |
| Evolution                                                                                                                                                                                                                       | Optional. Set a target creature (another lexicon entry of type creature) and the conditions required: minimum level, a required item, or a free-form condition description for the AI to interpret.                                                                               |
| Max Moves                                                                                                                                                                                                                       | How many moves the creature can know at once. The default is 4. When a creature would learn a fifth move, the player must choose one to forget.                                                                                                                                   |
| Experience Curve A multiplier on how much                                                                                                                                                                                       | XP the creature needs to level up. 1.0 is normal. Higher values make leveling slower; lower values speed it up. Use this to tune legendary or boss creatures to level more slowly than common ones.                                                                               |
| Possible Abilities                                                                                                                                                                                                              | A pool of abilities (lexicon entries of type ability) this creature might have. When the creature is captured, the system randomly assigns one from this pool — if the Abilities system is enabled.                                                                               |
| Battle Rewards                                                                                                                                                                                                                  | What the player receives for defeating this creature in the wild without capturing it: currency amounts, item drops, or both.                                                                                                                                                     |
| Moves, Natures, and Abilities                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                   |
| These are the creature system's supporting cast. Each one is a separate lexicon entry with its own type. They follow the same pattern as creatures: standard lexicon fields for lore, plus a type-specific configuration panel. |                                                                                                                                                                                                                                                                                   |

### Moves

Create a move by making a new lexicon entry and setting its Type to move. The move configuration includes:

| Field                                                                                                                         | What it does                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power                                                                                                                         | Base damage output. Higher power means more damage before type effectiveness, stats, and accuracy are factored in.                                 |
| Accuracy                                                                                                                      | The percentage chance the move lands (0–100). A move with 90 accuracy misses roughly once in ten attempts.                                         |
| MP Cost How much                                                                                                              | MP (or whatever you've named your MP resource) the move costs per use. 0 for moves with no cost.                                                   |
| Type                                                                                                                          | Which elemental type the move belongs to. This is matched against the defending creature's types via the Type Effectiveness chart.                 |
| Status Effects                                                                                                                | Status conditions the move can inflict on the target — poisoned, paralyzed, confused, and so on. Each effect can carry its own application chance. |
| Moves are referenced by name in a creature's Learnable Moves list. Spell the names consistently — the system matches by name. |                                                                                                                                                    |

### Natures

Natures are small personality-derived stat tweaks: a creature with the Bold nature might gain a little Defense but lose a little Speed. Create a nature by setting an entry's Type to nature.

Each nature configuration has a positive stat (the one that goes up) and a negative stat (the one that goes down), each with a modifier value. Natures are assigned randomly on capture when the Natures system is enabled.

Natures are entirely optional. If you don't want the extra complexity, leave the Natures Enabled toggle off in Creature Settings and you never have to create any.

### Abilities

Abilities are passive effects that are always active — either during battle or in the field. Create an ability by setting an entry's Type to ability. The ability configuration is a free-form description of the effect; the AI uses this text when narrating whether the ability triggers. Examples: "Thick Fat: Reduces damage from fire and ice moves by half." "Intimidate: Wild encounters with weaker creatures may flee on sight."

Like Natures, Abilities are optional. The Abilities Enabled toggle in Creature Settings controls whether they're used at all.

### Creature Settings

Where: World Editor → Simulation tab → Creature Settings section.

These are world-wide rules that apply to the entire creature system — not to individual creatures, but to how the system behaves for everyone playing your world.

### Setting What it does

Max Active The maximum number of creatures in a player's active battle party at one time. The default is 6. The rest go into storage.
Swap Anywhere If on, players can freely move creatures between their active party and storage from anywhere. If off, swapping is only allowed at designated Healing Stations with Allow Creature Swap turned on.
Allow Release Anywhere If on, players can release creatures from their party from any location. If off, release is restricted to healing locations.
Status Capture Bonus Extra capture chance per status effect currently on the wild creature. The default is +10 per effect. This rewards the classic strategy of weakening and inflicting status before throwing a capture item.
Natures Enabled Master switch for the entire Natures subsystem. Off means no creature gets a nature on capture, and you don't need to create any nature entries.
Abilities Enabled Master switch for the entire Abilities subsystem. Same logic — off means no abilities are assigned and you don't need to author any.
Allow Trainer Catch Can the player attempt to capture creatures already owned by another trainer? Default is off. Most worlds should leave this off.
Trainer Catch Penalty If trainer catching is allowed, this flat penalty is subtracted from the capture chance when targeting a trainer's creature. Default is 30.
Obedience Enabled If on, high-level creatures may disobey the player if the player hasn't earned enough authority — measured by the number of badges (key items with the badge: true flag) in the player's inventory. A borrowed or hastily captured legendary won't follow orders from a rookie trainer.
Obedience Base Cap The level cap for automatic obedience when the player has zero badges. Creatures above this level may disobey.
Obedience Per Badge How many levels the obedience cap increases per badge earned. If this is set to 10 and the cap is 20, one badge raises the cap to 30, two badges to 40, and so on.
Forced Evolution If on, creatures automatically evolve the moment they meet the required conditions. If off, the player sees a prompt and must choose to trigger the evolution manually.

### Type Effectiveness

Where: World Editor → Simulation tab → Type Effectiveness section (same area as Creature Settings).

Type effectiveness is the chart that determines how much damage one type does to another. You build it as a list of matchups:

| Field                                                                                                                                                                                                                             | What it does                                                                                                                                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attacking Type                                                                                                                                                                                                                    | The type of the move being used.                                                                                                                                                                            |
| Defending Type                                                                                                                                                                                                                    | The type of the creature being hit.                                                                                                                                                                         |
| Multiplier                                                                                                                                                                                                                        | How effective the attack is. 2.0 = super effective (double damage). 0.5 = not very effective (half damage). 0.0 = immune (no damage). 1.0 = neutral (omit this one — unlisted matchups default to neutral). |
| You define the full chart yourself. If your world has types called Radiant, Void, and Ember, you decide which beats which. You don't need to include neutral matchups — only list matchups where the multiplier differs from 1.0. |                                                                                                                                                                                                             |

### STAB (Same-Type Attack Bonus)

Also in this section, you can enable STAB. When a creature uses a move that matches one of its own types, the damage is multiplied by the STAB bonus (default 1.5×). This rewards using creatures with moves that match their type, without requiring you to hardcode it into individual moves.

### Encounters (Per-Location)

Where: World Editor → Locations tab → edit any location → Encounter section.

Wild encounters are configured individually on each location. A dungeon floor can have different creatures than the forest outside it; a city street can have no encounters at all.

| Field             | What it does                                                                                                                                                                           |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled           | Master switch for encounters at this location. Off means no wild creatures appear here regardless of anything else.                                                                    |
| Encounter Rate    | The percentage chance of triggering a wild encounter per advance-time tick (0–100). A route you want to feel like a dangerous gauntlet might sit at 40–60. A quiet meadow might be 10. |
| Encounters        | The list of possible wild creature encounters at this location (see below).                                                                                                            |
| Encounter List    | Entries                                                                                                                                                                                |
| Each entry in the | Encounters list represents one possible creature that could appear:                                                                                                                    |

| Field                                                                                                                                                                                        | What it does                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lexicon Entry                                                                                                                                                                                | The creature (a lexicon entry of type creature) that can appear.                                                                                                                          |
| Spawn Weight                                                                                                                                                                                 | Relative probability of this creature appearing compared to others in the list. A creature with weight 10 appears five times more often than one with weight 2.                           |
| Level Range                                                                                                                                                                                  | The minimum and maximum level the wild creature can spawn at. The system picks a random level within this range each time.                                                                |
| Time of Day Restriction                                                                                                                                                                      | Optional. Restrict this creature to a specific time window — e.g., nocturnal creatures only appear between certain in-world hours. Leave blank for no restriction.                        |
| Unlock Conditions                                                                                                                                                                            | Optional memory conditions that must be true before this creature can appear. Use this to introduce creatures mid-story, gate post-game encounters, or tie rare spawns to story progress. |
| A location can have as many encounter entries as you want. You might have five common creatures with high spawn weights and three rare ones with low weights, all sharing the same location. |                                                                                                                                                                                           |

### Healing Stations (Per-Location)

Where: World Editor → Locations tab → edit any location → Healing section.

Healing stations are locations where players can restore their party and creatures to full health. A Pokémon Center is the classic example — a safe haven between wild areas. You can also create partial healing stations (creatures only, or party only) and add a currency cost if you want.

| Field                                                                                                                                                                           | What it does                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled                                                                                                                                                                         | Master switch. Off means no healing service at this location.                                                                                                                                     |
| Heal Creatures                                                                                                                                                                  | If on, healing restores all the player's creatures to full HP and MP, and revives any that have fainted.                                                                                          |
| Heal Party                                                                                                                                                                      | If on, healing restores all party characters to full HP and MP.                                                                                                                                   |
| Allow Creature Swap                                                                                                                                                             | If on, and if your Creature Settings has Swap Anywhere turned off, this location becomes one of the designated places where the player can move creatures between their active party and storage. |
| Cost                                                                                                                                                                            | Optional currency cost per healing visit. Leave blank for free healing. Use this if you want inns, doctors, or potion shops to charge for their services.                                         |
| Description                                                                                                                                                                     | Flavor text shown to the player when they use the healing service. "Nurse Joy tends to your party." or "The shrine's energy washes over your companions."                                         |
| A quick reference for common location types                                                                                                                                     |                                                                                                                                                                                                   |
| Location type Encounter                                                                                                                                                         | Healing                                                                                                                                                                                           |
| Wild route / dungeon floor Enabled, encounter rate set, creature list filled Disabled                                                                                           |                                                                                                                                                                                                   |
| Pokémon                                                                                                                                                                         | Center / Clinic Disabled Enabled with heal_creatures + heal_party + allow_swap                                                                                                                    |
| Town (no encounters, free rest) Disabled Enabled, no cost                                                                                                                       |                                                                                                                                                                                                   |
| Paid inn Disabled                                                                                                                                                               | Enabled, cost set                                                                                                                                                                                 |
| Boss chamber                                                                                                                                                                    | Disabled (or single scripted encounter) Disabled                                                                                                                                                  |
| A location can have both encounters and healing enabled if you want a dangerous location that also has a way to recover — a hot spring in the middle of a volcano, for example. |                                                                                                                                                                                                   |

### Tips for Designing Your Creature System

Start with types before creatures. Sketch your type chart on paper first. Decide which types exist in your world, which beat which, and how many you actually need. A simpler chart (six or eight types) is easier to balance and easier for players to learn than twenty. Build the chart in Type Effectiveness before you start assigning types to creatures.

Tune capture rates deliberately. A capture rate of 70 on starter creatures feels generous and welcoming. A rate of 5 on a legendary feels earned. Don't cluster everything at the same number — the spread is what makes catching feel varied.

Use spawn weights, not separate location configs. If you want a creature to be rare in an area, don't make a separate location for it — just give it a low spawn weight in the shared encounter list. A weight of 1 among entries totaling 50 means it appears about 2% of the time.

Gate late-game creatures with unlock conditions. Story-important creatures that shouldn't appear until act three can sit in the encounter list from day one with an unlock condition tied to a memory state. Players won't see them until the condition is met, but you don't have to restructure the location later.

Pair Obedience with a badge system. If you enable Obedience, make sure your world has key items with the badge: true flag that players can earn. Otherwise the obedience cap stays at the base value and high-level captured creatures will always disobey. See the Items chapter for details on the Key Item and Flags fields.

Forced Evolution vs. player choice. Forced evolution keeps things moving and feels automatic, like a classic RPG. Player-triggered evolution adds weight to the moment and lets players hold off if they want to keep a pre-evolution form. Neither is wrong — choose what fits your world's tone.

---

## Property & Furnishings Market

### Property and Furnishings Market

The property and furnishings system lets players occupy places in your world and decorate them. A player can either buy a location — receiving a deed they permanently own — or rent it on a lease without ever taking ownership. Either way, they can furnish the space and the AI will describe it using those choices. This chapter covers both tenures and the economy options that surround them.

### 1. Buying vs Renting

A location can support one tenure, both, or neither. Understanding the difference up front helps you price and configure properties correctly.

### Buying (owning a deed)

When a player buys a property they receive a deed — permanent ownership of that location. Buying involves a one-time purchase price paid in one of the world's currencies.

The player can sell the deed back at any time, recovering a portion of the purchase price (see Section 8, Selling Back).
The player can decorate the property and their furniture stays there until they actively uninstall it or sell the property.
Optionally, you can attach ongoing property tax or bills (utilities, upkeep, maintenance costs) to an owned location. These are recurring charges that accumulate while the player holds the deed. Failing to pay property tax accrues as debt — the player keeps the property and owes the amount.

### Renting (holding a lease)

When a player rents a property they hold a lease — they occupy the space but never own it. There is no purchase price and no deed changes hands.

The player pays recurring rent while the lease is active.
The player can decorate the rented property just like an owned one. If the lease ends, all installed furniture is returned to the player's inventory automatically.
The player cannot sell a rented property — you cannot sell what you do not own.
The player can end the lease at any time using the End Lease button in the Property panel, or by typing >endlease in chat.
If the player misses a rent payment, what happens depends on the world's Unpaid rent setting in the Economy tab:
Evict (the default) — the player loses the lease immediately, their furniture is returned to their inventory, and the missed payment is forgiven.
Becomes debt — the player keeps the lease and the missed rent is recorded as debt they owe.

### What "recurring charge on an owned property" means

Because rent and ownership are separate concepts, the editor separates them clearly:

In a location's property settings, the Rent section is for tenants (players who do not own the deed). Set the recurring rent amount here.
The Property tax / bills section is for owners (players who hold the deed). Set ongoing ownership costs — utilities, upkeep, taxes — here.
A recurring charge on a place you own is property tax or bills, not rent. A recurring charge on a place you do not own is rent. The Unpaid rent setting in the Economy tab only governs missed rent payments on leases; unpaid property tax always becomes debt regardless of that setting.

### Choosing the right tenure for your world

Use buy-only for properties that feel like permanent investments — a home base, a guild hall, a character's estate. The deed model rewards commitment and gives players something tangible to sell.

Use rent-only when you want the location to feel transient or when permanent ownership would break the fiction — a rented room above a tavern, a market stall you lease by the season, a temporary safe house. The lease model fits worlds where players are travelers or where property is scarce.

Use both to let players upgrade from tenant to owner — a rented room that the player can eventually buy outright, or a location that operates as a short-term rental when unowned and a permanent holding once purchased.

### 3. Setup Chain

Three prerequisites must be in place before players can purchase or lease anything. Work through them in this order.

### Step 1 — Define a currency

Open the Economy tab in the world editor. Create at least one currency (e.g. "Gold", "Credits", "Crystals"). Without a currency, prices cannot be set and nothing can be purchased or rented.

While you are in the Economy tab, you can also set the Unpaid rent rule. This controls what happens when a player misses a rent payment on a leased property. The default is Evict (the player loses the lease and their furniture is returned, but the missed amount is forgiven). The alternative is Becomes debt (the player keeps the lease and owes the amount). This setting has no effect on owned properties — unpaid property tax always becomes debt regardless.

### Step 2 — Mark a location as purchasable or rentable

Open the Coordinates (Locations) tab and open or create a location. In the property section:

Toggle Purchasable on to allow buying, and set a purchase price using one of your defined currencies. Under Property tax / bills, optionally add a recurring ownership charge (utilities, upkeep, taxes) that accumulates while a player holds the deed.
Toggle Rentable on to allow leasing, and set a recurring rent amount under the Rent section. This is separate from property tax — rent is for tenants, property tax is for owners.
Add one or more furniture slots — each slot needs a unique id, a display name, and optionally a maximum number of items that can fill it.
The slot id is a plain text key you choose (e.g. bed, shelf, wall_decor). It does not have to match anything else in the world; it only needs to be consistent with the furniture you intend to fit into it (see the slot-matching rule in Section 4).

A single location can have many slots of different types. A bedroom might have bed, nightstand, and wall_art. A shop might have display_case and sign. Each slot defines a space in the narrative that a piece of furniture can occupy.

Optional customization flags:

Name customizable — when on, the player can give the property a personal name that appears in the AI prompt context.
Description customizable — when on, the player can write their own flavor description for the property, layered on top of the base location description.

### Step 3 — Create furniture lexicon entries

Open the Lexicon tab and create a new entry. To make it a piece of furniture, set type to furniture and fill in:

Furniture Properties (furniture_config):
slot_types — which property slot IDs this piece can go into (see Section 4).
context_description — prose injected into the AI prompt when this item is installed.
ambient_effects — optional additional flavor (sounds, smells, lighting).
market_scope — global (sells world-wide) or local (sells only at specific shops).
Item price (item_config.value) — the purchase price in one or more currencies.
Both furniture_config and item_config.value are required. A furniture entry without a price will not appear in any market listing.

### 4. Global vs Local Furniture

Global furniture (market_scope: 'global') is listed in the world Market dialog's Furnishings tab for all players, regardless of where they are in the world. Use this for staple items — basic chairs, common rugs, generic wall hangings — that any player might reasonably order from anywhere.

Local furniture (market_scope: 'local') only appears at specific in-world shops. To stock a local item, open the location that acts as a shop, go to its marketplace_config, and add the lexicon entry's ID to the inventory list. Players must visit that location to see and buy it.

Use local furniture for specialty or rare items that feel like they belong to a particular vendor or region — a master smith's custom anvil, a rare enchanted mirror sold only at a specific wizard's tower. This encourages in-world travel and discovery.

A local furniture item with no locations listing it in their inventory will never appear anywhere. Make sure at least one shop carries it before publishing.

### 5. The Delivery Fee

Players can purchase furniture from two places:

On-site — standing at the shop in the world. No surcharge.
Via the world Market dialog — browsing and buying remotely. A delivery fee applies.
The delivery fee is set as a percentage in the Economy tab under world_market_config.delivery_premium_pct. The default is 15%. A 100 Gold chair ordered remotely costs 115 Gold; the same chair bought in person costs 100 Gold.

Property is always bought at its list price. Whether a player purchases a location by standing inside it or via the Market dialog's Real Estate tab from across the world, the price is the same — no delivery surcharge applies. Only furniture (physical goods that need to be shipped) is subject to the remote delivery fee.

This creates a light incentive to visit shops in person rather than ordering furniture from camp. Set the fee to 0 if you want to remove that distinction entirely.

### 6. The Slot-Matching Rule

When a player tries to install a piece of furniture, the system checks whether the furniture's slot_types list contains an entry matching one of the property's slot id values. The match is by exact slot ID, not by a slot's display name.

['any'] is a wildcard. A furniture entry with slot_types: ['any'] can be installed into any slot on any owned property. Use this for versatile items like potted plants or candles that could reasonably go anywhere.

Exact IDs must match. If a property has a slot with id: "bookshelf" and a piece of furniture has slot_types: ['shelf'], the furniture will not fit — even though the names look related. Both must use the same string: either the property slot becomes shelf, or the furniture's slot_types entry becomes bookshelf.

Example:

A property has these slots:

### id Name

### bed_spot Main Bed
side_table Nightstand
window_seat Window Seat
A "Carved Oak Bed" should only go in the main bed spot:

slot_types: ['bed_spot'] — correct.
slot_types: ['bed', 'main'] — will not fit; those IDs do not exist on this property.
slot_types: ['any'] — will fit any slot (probably too permissive for a bed).
A "Small Lamp" that looks good anywhere:

slot_types: ['any'] — fits every slot on every property, which is probably what you want for a small accent item. 7. The Player Experience
From a player's perspective, the full loop looks like this:

Find a property. Properties appear on the world map with a "For Sale" or "For Rent" marker when available, and an "Owned" or "Rented" badge after acquisition.
Acquire the property. To buy: visit the location or open the world Market dialog's Real Estate tab and purchase at the list price — no delivery fee applies to property. To rent: tap the Rent button in the nearby listing or at the location itself and the lease starts immediately.
Browse furniture. Open the Market dialog's Furnishings tab to see global listings; visit in-world shops for local inventory. Buy furniture — it goes into the player's inventory.
Travel to the property. The player moves their party to the owned or rented location.
Install furniture. In the Property side panel, the player selects an empty slot and chooses a compatible piece of furniture from their inventory. The item moves from inventory into the slot.
AI flavor activates. While the party is present at the furnished location, each installed item's prose is injected into the AI prompt. The AI describes the space using those choices, making the player's decorating feel meaningful in the narrative.
Players can remove or swap furniture at any time while present at the property. Uninstalled furniture returns to inventory. When a lease ends — either because the player chose End Lease, typed >endlease, or was evicted for unpaid rent — all installed furniture is automatically returned to the player's inventory. An owned property retains its furniture until the player uninstalls it or sells the deed.

### 8. Nearby Properties

Players don't need to open the world map to discover property they can buy. The Property panel in the world sidebar includes a Nearby for Sale section that lists purchasable, unowned locations reachable from the player's current position — calculated from the world's map connections and travel routes.

Each nearby listing shows the property name, the travel time or route, and the applicable price (purchase price for buyable properties, recurring rent for rentable ones). The player can tap Buy to purchase it outright or Rent to start a lease, without leaving the sidebar.

This means the connections and routes you draw in the Dimensional Maps tab do double duty: they determine where players can travel, and they determine which properties surface as "nearby" when a player scans for real estate. A location that is purchasable but has no map connections leading to it will not appear in any Nearby list — players would have to find it on the map directly. If you want a property to be discoverable through the Nearby panel, make sure at least one travel route connects it to somewhere the player is likely to be.

### 9. Selling Back

Players can sell furniture and owned property back for currency at any time, subject to the rules below. Selling property requires holding the deed — a rented property cannot be sold because the player does not own it. All payouts are floored to whole units — the house keeps fractions.

### World-level sell-back rate

Set world_market_config.sellback_pct to the fraction of an item's list price the player receives on a sale. The default is 0.5 (50%). A 100 Gold chair sold back at the default rate returns 50 Gold.

The gap between the buy price and the sell-back price is your world's built-in money sink — it discourages pure arbitrage and gives currency weight. A tight spread (e.g. 0.8) makes the economy feel more liquid; a wide one (e.g. 0.25) makes purchases feel more permanent.

### Per-item overrides

You can override the world rate for specific items:

On a furniture lexicon entry: set item_config.sellback_pct.
On a purchasable location: set property_config.sellback_pct.
A per-item value takes precedence over the world default. Use this to make certain items deliberately non-refundable (set to 0) or to offer a higher buy-back on purpose-built investment pieces.

### Where selling is allowed

world_market_config.sellback_location_rule controls where the sell action is available:

'anywhere' (default) — players can sell from anywhere in the world, including via the Market dialog.
'on_site' — players must be physically present at the property or at a shop that stocks the item to sell. Use this if your world has a pawnbroker or estate agent that players should seek out in person.

### Selling furniture

A player can sell one piece of furniture at a time, or use the quantity stepper to sell multiple copies of the same item in a single transaction. The payout is quantity × (item list price × sellback rate), floored.

Items marked untradeable or flagged as key items cannot be sold back. Use these flags for quest-critical objects or unique story items that should never leave a player's inventory involuntarily.

### Selling property — empty or furnished

When a player sells an owned property, they are offered two choices:

Sell empty — the property deed is returned to the market. Any furniture currently installed is uninstalled first and returned to the player's inventory. The payout is the property's sell-back price alone.
Sell furnished — the property and all installed furniture are sold together as a packaged deal. The furniture does not return to inventory. The payout is:
payout = floor( (property_sellback + Σ furniture_sellback) × (1 + furnished_lot_bonus_pct) )
where property_sellback is the property's base sell-back value and Σ furniture_sellback is the sum of every installed piece's individual sell-back value.

### The furnished-lot bonus

world_market_config.furnished_lot_bonus_pct adds a percentage bonus on top of the combined property + furniture total when a player sells furnished. The default is 0 — the mechanic is off until you opt in.

A value of 0.10 gives a 10% bonus over selling the deed and furniture separately. This rewards players who took the time to decorate: a well-furnished property is worth more as a complete package than the sum of its parts.

Selling furnished always pays at least as much as selling the deed and every piece separately. The bonus makes it strictly better to sell furnished when you intend to part with all the contents.

When the player opens the sell dialog for a property, they see both options side by side — the empty payout and the furnished payout, with the bonus called out when it applies — so they can make an informed choice. The dialog also shows a permanence warning: selling removes any custom name or description the player gave the property, and re-buying costs the full list price.

### Where players sell

There are three surfaces from which a player can trigger a sale:

World Market dialog → Sell tab — a consolidated hub listing all sellable furniture (grouped by item, with held quantity shown) and all owned properties in one place. The Sell tab sits alongside the existing Real Estate and Furnishings tabs.
Inventory panel — each furniture item's detail view has a Sell button for quick access without opening the full market.
Property panel — each owned property's management view has a Sell button alongside the install/remove controls. 10. The Items & Property Tab
In the chat sidebar, items and property no longer live in two separate tabs. They are combined into a single Items & Property tab with three sub-tabs:

Items — the player's inventory (consumables, equipment, held furniture, key items).
Property — all owned and rented locations: install/remove furniture, rename the property, sell an owned deed, or end a lease on a rented one.
Sandbox — cheat controls, available in any world that has a currency defined (see Section 11).
This keeps economy-related controls in one place without requiring the player to switch between tabs to compare what they own with what they are carrying.

### 11. Sandbox / Cheat Controls

    In worlds with an economy, every player has access to a Sandbox cheat panel via the Sandbox sub-tab of the Items & Property tab. Sandbox controls affect only the player's own session — they have no effect on other players in the same world.

Three actions are available:

Give currency — instantly adds any amount of any of the world's defined currencies to the player's wallet. Useful for testing economy balance or skipping a grind.

Spawn item — adds any item from the world's lexicon directly to the player's inventory, bypassing the marketplace and delivery system. Specify a quantity if you want more than one.

Grant property — grants ownership of any of the world's purchasable locations to the player immediately, regardless of whether they can afford it or whether it is already "for sale."

### Inline commands

The same three actions are available as chat commands for players who prefer typing:

### Command Aliases What it does

> givecurrency <amount> [currency] >givegold <amount> Adds the specified amount of currency. If you omit the currency name, the world's first defined currency is used.
> spawn <item name> [quantity] >giveitem <item name> [quantity] Adds the named item to inventory. Quantity defaults to 1.
> grant <property name> — Grants ownership of the named location.
> rent <property name> — Starts a lease on the named location immediately, without paying currency.
> endlease <property name> — Ends the active lease on the named location. Installed furniture is returned to inventory.
> These commands work regardless of whether the Sandbox sub-tab is open. They do not generate an AI response — they execute silently and update the party state immediately.

As a world creator, you do not need to do anything to enable sandbox controls. They are always available to players in worlds with at least one defined currency. There is no toggle to hide or restrict them — sandbox is an escape hatch, not a game mechanic, and players who want to cheat their own session are free to do so.

---

## Relationships & Attitudes

### Relationships and Attitudes

The relationships system lets your NPCs remember how you've been treating them — and show it. This chapter covers everything on the Relationships tab in the world editor: turning the system on, choosing which parts you want, authoring the starting feelings your characters bring into a session, tuning how dramatically a moment lands, and controlling what the storyteller AI is told about where things stand.

### Turning it on

At the very top of the Relationships tab is a master Enable Relationships toggle. Flip it on and the whole system activates: the AI starts tracking how each NPC feels about you, and a Relationships panel appears in the sidebar during play so you can see where you stand at a glance.

You can turn the whole system off at any time without losing any data. If you never touch this tab, nothing breaks — it is entirely opt-in.

### Layer toggles — choose what your world tracks

Below the master switch are five toggles that let you mix and match the parts of the system you want:

Persistent affinity level — NPCs have a long-term feeling toward you that carries across sessions. A character who grows fond of you stays fond of you. Turn this off if you only want temporary mood effects with nothing that lasts.
Temporary moods — On top of the long-term feeling, interactions can leave a short-lived emotional impression: a burst of warmth after a kind word, brief irritation after an insult. Turn this off if you want only permanent changes with no mood swings.
Moods fade over time — When a moodlet expires it happens gradually over in-world hours rather than snapping off instantly. Turn this off and moods simply vanish once they run their course.
Seed from authored attitudes — When you open a world session, each character starts with an affinity level based on the attitudes you wrote for them in their character settings. Turn this off and everyone starts at neutral regardless of what their attitudes say.
Show panel to player — Controls whether the Relationships sidebar panel is visible during play. Turn this off for a world where you want feelings to stay ambiguous and emerge only through narrative.

### Authored attitudes — starting feelings

Each world character has an Attitudes section in the World Character editor. An attitude is a starting emotional stance — not a live relationship shift, but a seed that tells the system how that character feels at the very beginning of a session.

Each attitude entry has four parts:

Who it targets — another character in the world, a faction (any lexicon entry tagged as an organization or group), or The Player (Persona), the special option that targets whoever is playing.
Tier — where on your relationship ladder this character begins. The dropdown reflects your world's own tier ladder (see the Tier Ladder section below), not a fixed default list. If you have renamed tiers or built a custom ladder, those names are exactly what appear here. For a world using the defaults you might see tiers like Stranger, Friendly, Friend, Trusted, Beloved, Soulmate on the warm side, or Unfavorable, Disliked, Rival, Enemy, Nemesis on the cold side.
Intensity (1–100) — how strong the feeling is within the chosen tier. The tier sets the band; intensity positions the starting point inside it. A character seeded as Friend at intensity 10 sits at the low edge of that tier; at intensity 90 they sit near the top, on the cusp of the next tier up. Intensity never crosses into a neighboring tier — a character seeded as Friend always reads as Friend no matter the intensity. For cold tiers, higher intensity means a stronger negative feeling. If you leave this unset it defaults to the middle of the band.
Reason (optional) — a short note about why they feel this way, which may surface in the relationship block during play.
When Seed from authored attitudes is on, these entries are converted into starting relationship points when the party is created. The tier picks the band; the intensity picks where in that band the character starts. A character targeting another character with a Friend attitude warms up toward that character from the start, not just toward the player.

Characters can hold attitudes toward multiple targets — an NPC they have known for years, a faction they distrust, and a player they have never met. All of them seed independently.

If a relationship already exists in the party state from a previous session, the seed does not overwrite it. Seeding only applies on first creation.

### Magnitudes — how much a feeling moves

The Magnitudes section is where you tune how dramatically a single interaction shifts things.

There are two weight classes:

Regular — what >like and >dislike emit. Small reactions: a thoughtful gesture, a moment of encouragement, a minor slight.
Severe — what >love and >hate emit. Big reactions: a profound act of loyalty, a betrayal that cuts deep.
For each weight class you set three numbers:

Permanent amount — how many points the long-term affinity level shifts.
Mood size — how strong the temporary moodlet feels (players only ever see it as a qualitative description, never as a number).
Mood hours — how many in-world hours that moodlet lasts before it starts fading.
Higher permanent amounts mean relationships build or crumble quickly. Lower amounts create slow-burn dynamics where change takes sustained effort. Longer mood hours let a single interaction color the storyteller's tone across a whole arc.

### Custom moods — feelings that don't fit like or dislike

Sometimes a regular like or dislike is not quite right. Maybe a character feels awe, or guilt, or protective. Custom moods let you define your own named feelings, each with their own size and fade duration.

Click Add custom mood and give it a name. That name is what the AI uses when it writes >mood awe, for example. Set the size and how many hours it lasts, and you're done. Custom moods work exactly like the built-in ones — they appear as qualitative impressions in the sidebar and color the storyteller's tone while they're active.

You can add as many custom moods as your world needs.

### The tier ladder — what a feeling is called

Under the hood, affinity is tracked as points. But neither you nor the AI ever see the raw numbers. Instead, point ranges map to a tier — a named relationship status.

By default there are 14 tiers covering a full arc from stranger to soulmate on the positive side, and disliked to nemesis on the negative side. The tier name is what the sidebar shows, what the AI sees in the relationship block, and what appears in the Tier dropdown when you author an attitude.

### Renaming tiers

If the default names don't fit your world — say, your story is set at court where "Confidant" makes more sense than "Friend" — click any tier name and type over it. The point thresholds stay the same; only the label changes. The sidebar and the AI prompt both use whatever you write here.

### Building your own ladder

For a completely custom structure — fewer rungs, different thresholds, different emotional vocabulary — you can add, remove, and reorder tiers entirely. Set the threshold (the minimum points needed to reach that tier), a name, and a display color.

Attitude authoring reflects your ladder. The Tier dropdown in the World Character editor is populated from the ladder you define here, not from any fixed default list. Rename a tier to "Confidant," add a tier called "Oathbound," remove ones you don't need — whatever you commit in the ladder is exactly what you'll see when writing attitudes for your characters.

A romance-focused world might use only five tiers: Stranger → Acquaintance → Close Friend → Beloved → Soulmate. A political intrigue world might scale down the positive side and add extra rungs of enmity: Unfavorable → Disliked → Rival → Enemy → Nemesis. Your ladder, your vocabulary.

### The Relationship Block — what the AI is told

When the storyteller AI generates its next reply, it receives a compact summary of where you stand with each NPC in the current scene. The Relationship Block section lets you control how that summary looks and what it says.

### Heading and wrapper tags

By default the block uses a plain markdown heading. If your world uses structured prompt tags — the <Name>…</Name> style some creators prefer — you can set a wrapper start and wrapper end tag instead (for example <Bonds> and </Bonds>). The markdown heading is then replaced by your tags.

### Per-character line template

Each relationship entry gets one line in the block. You control what that line contains using a Handlebars template. The available variables are:

{{subject}} — the character who holds the feeling. Also available as {{name}} for backwards compatibility.
{{target}} — who or what the feeling is directed at: the player's persona name, another character's name, or a faction name. Use {{target}} in any template that covers non-player relationships.
{{tier}} — the relationship tier label (whatever you've named it in your ladder).
{{user}} — the player's persona name. Still available, but {{target}} is preferred for templates that cover character→character or character→faction rows.
{{reason}} — a brief note about what drove the current feeling, if one was recorded (may be blank).
{{mood}} — the active temporary mood description, if any (e.g. "pleased," "quietly uneasy"). Blank if no mood is currently active.
A simple line template:

### {{subject}} → {{target}} — {{tier}}{{#if mood}}, {{mood}}{{/if}}

A more narrative template:

{{subject}} regards {{target}} as {{tier}}.{{#if mood}} Currently: {{mood}}.{{/if}}
If your template previously used {{name}} regards {{user}} as {{tier}} (which only made sense for NPC→player rows), update it to use {{subject}} and {{target}} so the block reads correctly for character→character and character→faction relationships too.

### Instructions

Below the template is a free-text Instructions field — guidance the AI receives about how to use the relationship information during generation. The default tells the storyteller to let these feelings color tone and behavior without explicitly announcing them. You can add notes like "Do not describe characters' inner feelings in direct narration — show through action and dialogue only," or whatever fits your storytelling style.

### How it reads in play

A few things worth knowing about the feel of the system during an actual session:

The AI never sees numbers. It is told that Elara regards you as a "Trusted Friend" with a current mood of "quietly delighted" — not that your affinity is 340 points with a +60 moodlet. The storyteller works in feelings and words, which is where it performs best.
Relationships go beyond the player. Characters can hold feelings about each other and about factions — not just about you. When the AI generates a multi-character scene and one NPC reacts strongly to another, the shift updates that character's relationship with the target. The player sidebar shows how NPCs feel specifically about you; character→character and character→faction states are also passed to the AI and inform how scenes between those characters play.
The sidebar panel. If you have left "Show panel to player" on, a Relationships section appears in the sidebar. Each NPC shows their current tier as a badge, a progress bar for where they sit within that tier, and fading mood chips for any active temporary feelings.
Giving a gift shifts feelings. Type >gift <item> to <character> in the chat to present an item to an NPC. If that item has a gift value configured in its item definition in the Lexicon, it generates a relationship response — the NPC feels something and the storyteller narrates it. Items bought through the marketplace can have gift values too.
Moods use in-world time. An hour of accelerated adventure time counts the same as a quiet evening of play. If "Moods fade over time" is on, a temporary feeling winds down gradually as in-world time passes. Turn the toggle off and moods simply expire and vanish.
The storyteller emits commands after emotional moments. After an exchange that carries emotional weight, the AI may write a >like, >love, >dislike, >hate, or custom >mood command inline in its reply. That command is attributed to whichever character's section it appears under, and targets whoever or whatever the command specifies. You do not have to track anything manually.

### Quick recipes

Slow-burn dating sim. Enable all five layers. Set Regular permanent amounts low so small kindnesses nudge things gently, and Severe permanent amounts high so a grand gesture or a real betrayal lands hard. Give mood hours generous values so a warm interaction leaves a glow for a whole in-world day. Customize the tier ladder to match your love story: Stranger → Acquaintance → Friend → Beloved → Soulmate.

Grudges that fade unless rekindled. Enable persistent affinity and temporary moods. Leave moods fade on, but set mood hours very high (many days of in-world time). Turn off "Seed from authored attitudes" and manually start your NPCs at a negative tier. Over time, if no further hostility occurs, moods soften. But one fresh >hate event restarts the clock.

Simple reputation score with no mood swings. Enable persistent affinity only. Turn off temporary moods (and "Moods fade over time" along with it). Relationships shift only permanently and never flutter. Clean reputation tracking without emotional volatility.

AI feels it, player doesn't see the numbers. Enable everything but turn off "Show panel to player." The storyteller still receives the relationship block and acts accordingly — the player just has to read the room.

---

## Travel, InfoBoard, Commands & Director

### Travel Routes, InfoBoard, Commands, and the Director

This chapter covers four systems that give your world structure, feedback, and depth beyond the basic story setup: the travel graph that moves players between places, the InfoBoard HUD that keeps live world state visible, Commands that let players take repeatable structured actions, and the Director that acts as an invisible GM reasoning about your world before each message.

### Travel Routes

Where: World Editor → Travel tab.

Routes are how players move between locations during a session. Without routes, a player can use the Solo Travel dialog to type any destination by hand, but with routes you get a structured travel graph: a player can only go where there's a route, the trip takes the right amount of in-world time, and you can gate access behind requirements.

### Route fields

| Field                                           | What it does                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| From / To The two locations the route connects. |                                                                                                                                                                                                                                                                                                                             |
| Bidirectional                                   | If on, the route works both ways. If off, you need a separate route for the return trip. Useful for one-way drops, slides, portals.                                                                                                                                                                                         |
| Travel Time                                     | How many in-world hours the trip takes. Set to 0 for instant travel — teleporters, magic circles, interior doorways.                                                                                                                                                                                                        |
| Distance                                        | Optional abstract value for display (miles, kilometers, parsecs — your choice).                                                                                                                                                                                                                                             |
| Required Mediums                                | If non-empty, the player needs a vehicle with one of these mediums to use the route. Leave empty for on-foot travel.                                                                                                                                                                                                        |
| Description                                     | Shown to the player when picking the route.                                                                                                                                                                                                                                                                                 |
| Hazard Description Injected into the            | AI prompt during travel — used for narrating dangers or atmosphere en route.                                                                                                                                                                                                                                                |
| Requirements                                    | Memory conditions that gate the route. For example, "the player has the Mountain Pass key." Players can't see or use the route until the conditions are met.                                                                                                                                                                |
| Hidden                                          | If on, the route doesn't appear in the player's destination list until they've discovered it through other means.                                                                                                                                                                                                           |
| Sublocations are free                           |                                                                                                                                                                                                                                                                                                                             |
| If a location has a Parent                      | Location set (Hierarchy and Relations in the location editor), the sublocation gets implicit instant routes to and from its parent with no travel time and no vehicle required. So if you have "Inn Lobby" with Parent set to "The Boar's Head Inn," the player can move between them freely without you authoring a route. |

Use sublocations for rooms within a building and use travel routes for buildings within a city or cities within a region. Sublocations handle interior geography automatically; routes handle exterior geography.

### Era overrides

If your world uses Eras (different historical periods), each era can carry travel route overrides. You can disable a route entirely (the bridge hasn't been built yet), modify a route's travel time (the road is paved now), or add era-only routes (the airship line that opened in 1850). Covered in detail in the chapter on Eras and Timeline.

### How players use it

The chat top bar has a Map button. If your world has a Map with pins, clicking it opens the visual map viewer with route lines drawn. If not, the player gets a list view of available destinations from the current location. Either way, picking a destination shows the travel time, vehicle requirement, and description, and the player confirms to begin the trip.

The Solo Travel dialog (free-form location entry) is always available for worlds that don't have strict route structure, or as a quick escape hatch during testing.

### The InfoBoard (HUD Sidebar)

Where: World Editor → InfoBoard tab.

The InfoBoard is a customizable sidebar HUD that shows live world state during chat. It's made of categories and key-value rows that the AI keeps updated as the story progresses. Think of it as the stat sheet the player can glance at without breaking narrative flow — current location, HP, quest state, active status effects, whatever matters in your world.

### How it works at runtime

You define categories with keys in the editor. The AI gets instructed to emit those keys in <info_board> blocks at the end of each message:

<info_board>location=Castle of Doom|hp=45/100|status=Poisoned</info_board>
The system parses these blocks silently — they don't appear in the visible message — updates the InfoBoard state on the party, and the sidebar re-renders. Players see a live HUD that updates with the story without any meta interruption.

### Setting up categories and keys

Category fields:

| Field       | What it does                                                              |
| ----------- | ------------------------------------------------------------------------- |
| Title       | Section heading shown in the sidebar — "Vitals," "Location," "Quest Log." |
| Order       | Display order. Lower numbers appear higher in the sidebar.                |
| Keys        | The list of values tracked in this category.                              |
| Key fields: |                                                                           |

| Field                                               | What it does                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Label                                               | The display label the player sees — "Health."                                                                                                                                                                                                                                                                                                                                 |
| Key The internal name the                           | AI emits — hp. Keep these short; the AI types them every message.                                                                                                                                                                                                                                                                                                             |
| Display Type                                        | How the value is rendered (see below).                                                                                                                                                                                                                                                                                                                                        |
| Min                                                 | Value / Max Value / Color For the progress display type — the bounds and bar color.                                                                                                                                                                                                                                                                                           |
| Display types                                       |                                                                                                                                                                                                                                                                                                                                                                               |
| Type Looks like                                     | Best for                                                                                                                                                                                                                                                                                                                                                                      |
| text Plain string                                   | Locations, quest names, status descriptions                                                                                                                                                                                                                                                                                                                                   |
| progress Filled progress bar with a numeric overlay | HP, MP, hunger, reputation                                                                                                                                                                                                                                                                                                                                                    |
| chips                                               | Comma-separated values rendered as colored badges Tags, status effects, active party members                                                                                                                                                                                                                                                                                  |
| monospace                                           | Code-styled fixed-width text Coordinates, codes, IDs                                                                                                                                                                                                                                                                                                                          |
| Custom prompt                                       |                                                                                                                                                                                                                                                                                                                                                                               |
| The InfoBoard config has a Custom                   | Prompt field. By default the system gives the AI a generic instruction explaining the format. Override it if you want world-specific framing — for example, for a tech-themed world: "Update the player's HUD readout in the standard JSON-board format." Make sure any custom prompt you write still tells the AI to emit the <info_board> blocks, or the HUD will go stale. |

### Players can edit values inline

Sidebar values are click-to-edit. A player can override what the AI is tracking — useful for correcting drift or setting up before a session begins. Edits are saved to the party.

### Per-party overrides

A party can override or extend the world's InfoBoard config. Two modes:

Override — replaces the world's InfoBoard config entirely for that party.
Append — adds categories on top of the world's default setup.
This lets players customize their HUD without touching the world itself.

### Commands (Repeatable Player Actions)

Where: Per-character (Character Editor → Commands tab) or world-wide (World Editor → Commands tab).

Commands are structured actions a player can invoke during a chat session. Think of them as in-character tools — "cast spell," "roll perception," "advance time," "check inventory." Players invoke them through a UI form; the system runs the backing logic; the result becomes part of the chat context.

There are four command types:

### Type When to use

command A built-in system action like advancing time, marking an OOC note, or ending the scene.
function An AI-callable action. The AI decides when to invoke it via tool calls. The result is fed back to the AI's next turn.
omni Universal — can be invoked by either player or AI.
turn Runs automatically every N messages. Useful for periodic NPC actions, hunger ticks, ambient events.

### Command fields

| Field                                                                                                                                                                                        | What it does                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Name Internal                                                                                                                                                                                | ID.                                                                                                                                             |
| Label                                                                                                                                                                                        | Display name shown to the player.                                                                                                               |
| Description                                                                                                                                                                                  | Tooltip and help text. The AI also reads this to know when to invoke the command (for function type).                                           |
| Callback                                                                                                                                                                                     | The name of a script in the character's or world's Scripts list that runs when the command is invoked.                                          |
| Parameters A                                                                                                                                                                                 | JSONSchema describing the command's arguments. The player sees a form generated from this schema.                                               |
| In Context                                                                                                                                                                                   | If on, the command's result message appears in the chat for the AI to see. If off, it runs silently — useful for checks that only update state. |
| Transform A                                                                                                                                                                                  | Handlebars template that formats the script's raw result into a readable message. For example: "Margret rolls a 17 on her Insight check."       |
| Is                                                                                                                                                                                           | Multi-Step / Steps For wizard-style commands (see below).                                                                                       |
| Turn                                                                                                                                                                                         | Frequency / Interval / Return Message / As Forced Tool For turn commands — how often they fire and what to do with the result.                  |
| Multi-step commands (wizards)                                                                                                                                                                |                                                                                                                                                 |
| Some commands need multiple decisions before they run. "Cast a spell" might need (1) which spell, (2) which target, (3) how much MP to commit. Set Is Multi-Step to on and define each step: |                                                                                                                                                 |

### Step field What it does

Step Number / Step Name Order and display label for the step.
Parameters JSONSchema for this step's form fields.
Validation Optional script. Runs after the player submits the step; throwing it rejects the step and shows an error.
Data Fetcher Optional script. Runs before showing the form; the result becomes the form's prefill data. For example, "list spells this character actually knows."
Conditional Optional script. Returns false to skip the step entirely. For example, "skip MP commitment if the spell is free."
When the player completes the last step, the command's main Callback runs with all collected step data and produces the final result.

### Inline commands

Separate from the authored Commands above, players can also issue built-in actions directly inside their chat messages by starting a line with >:

I draw my sword and approach the wolf.

> attack wolf
> These cover travel, combat, money, jobs, renting, and more — and the storyteller emits some (relationship changes) on its own. You don't author them; they activate when the matching system is set up in your world.

The full reference — every command, who issues it, and exactly what to set up for each to work — is in its own chapter, Inline Chat Commands (Player and Storyteller Actions).

### Common command patterns

A roll-stat-check function command (AI-callable):

### Name: roll_check

### Type: function
Description: Roll a stat check against a difficulty class.

### Callback: roll_check_script

### Parameters: stat (string, enum), dc (number)
Transform: "**{{args.stat}} check (DC {{args.dc}})**: {{result.value}} — {{result.outcome}}"
In Context: true
A periodic hunger tick (turn command):

### Name: hunger_tick

### Type: turn
Callback: hunger_script
Turn Frequency: every_x_messages
Turn Interval: 5
Turn Return Message: false (silent — just updates state)
An end-of-scene marker (system command, no script):

### Name: end_scene

### Type: command
Description: End the current scene.
The built-in system commands (sys, note, advance, break, end) don't need Callbacks — the engine handles them.

For writing the scripts that power command callbacks, see the developer scripting reference.

### The Director (GM Brain)

Where: Players enable it through their own chat settings, not in the world editor.

The Director is an optional reasoning layer that runs before the narrative AI writes each message. It thinks about scene state — what NPCs want, what story beats are pending, what relationships have shifted, whether to trigger a combat encounter — and produces structured tool calls. The narrative AI then receives a brief from the Director and writes its prose response.

You don't author Director content directly. You build a world the Director can work with well:

Give NPCs clear goals and motivations in their Long Summary.
Use the Story Beats and Pending Events systems to seed specific moments you want to occur.
Configure memory conditions on lexicon entries, routes, and encounters so the Director can gate content appropriately.
Enable Combat in your World Features if you want the Director to be able to spawn battles.
The Director's state is saved on the party and on the chat log, so it persists across sessions. Players can inspect and edit it through the Director State Panel in the chat sidebar.

### Settings players control

These are user-side settings, not world-side:

Always Use Director — runs the Director on every message regardless of other conditions.
Disable Director Mode — turns it off entirely.
If you're building a world designed for Director-style play — heavy combat, intricate NPC plotting, dungeon crawls — mention in your world description that Director mode is recommended. Players can toggle it on when they enter your world.

### What Players See in the Chat Sidebar

When a player is in a session in your world, the chat sidebar auto-populates with tabs for whichever subsystems you've enabled. You don't wire up UI — turning on a feature makes the corresponding tab appear.

### Tab Appears when Shows

### Party Always Active characters, persona, swap controls
Inventory Inventory feature on Item grid, currency balances, equip and unequip, Marketplace button when at a shop, active vehicle
Stats RPG Stats feature on Per-character HP and MP bars, stat values, equipment summary
Creatures Creatures feature on Active and storage creatures, dex, evolve, teach moves, heal at station
InfoBoard InfoBoard configured Categories of live values, inline edit, progress bars and chips
Director Director enabled Story beats, NPC intentions, scene notes, relationships, memory state
The chat top bar also provides:

Time controls — advance time, view the in-world date.
Map / Travel — route picker or the Solo Travel free-form input.
Memory Scanner — extract lexicon entries from the chat log.
Settings menu — debug mode, search, director console.
The various dialogs — marketplace, travel, command runner, character creation wizard, world picker — all open from these surfaces. Players don't navigate to separate pages; everything surfaces inside the chat.

---

## Inline Chat Commands

### Inline Chat Commands (Player and Storyteller Actions)

Inline commands are short instructions written directly inside a chat message. A player (or the storyteller) starts a line with > and the engine runs that action before the next AI reply. This is how a world's mechanical systems — travel, combat, money, jobs, relationships — get triggered from inside the story instead of from menus.

This chapter explains how the system works, who issues which commands, every command available, and exactly what you need to set up in your world for each one to function.

Note: these inline > commands are built into the engine — you do not author them. They are different from the authored Commands system (the command / function / turn actions you define per character or per world), which is covered in the Travel, InfoBoard, Commands, and Director chapter.

### How inline commands work

Players type a command on its own line, usually alongside their roleplay:

I steel myself and swing at the wolf.

> attack wolf
> When the message is sent, the engine reads every line that begins with >, runs the matching action, and feeds the mechanical result back into the story as a system note the storyteller can see:

> travel north_road
> [System: You travel to North Road. The journey takes 2 hours.]
> A few things worth knowing:

The command line stays in the message and is styled distinctly — it isn't hidden.
Commands run before the AI writes its reply, so the storyteller sees both the player's prose and the outcome, and narrates around it.
The parser understands with and on as separators: >use potion on pikachu, >catch with ultra_ball, >attack wolf with thunderbolt.
There is no master on/off switch for inline commands. A command works whenever the system it belongs to is set up in your world; if that system isn't configured, the command simply does nothing useful. Set the world up, and the relevant commands light up.

### Who issues a command

Not every command is meant for players to type:

Players type most of them — movement, combat, buying, working, renting.
The storyteller emits some automatically — the relationship commands (>like, >love, >dislike, >hate, >mood). Players are not meant to type these; the AI writes them after emotionally meaningful moments to record how a character feels. (You set this up in the Relationships system; see that chapter.)
Some are sandbox/cheat commands — they let a player simply give themselves money, items, or property. They're handy for solo play, "Scrooge McDuck inheritance" scenarios, and testing. Be aware they are currently always available to players, so don't rely on scarcity of money or items as a hard wall in a published world.

### Command reference

### Getting around (exploration)
Command What it does What to set up

> travel <place> Moves the party to another location and advances in-world time. Have more than one location. Authoring travel routes (Travel tab) gives structured, timed, gateable movement; without routes, free-form travel still works as a fallback.
> heal Restores the party's creatures at a healing spot. A location with healing turned on, plus the Creatures feature.
> battle Starts a wild-creature encounter. The Creatures feature and an encounter setup on the location.
> challenge <trainer> Starts a battle against a trainer-style NPC. Creatures feature and an NPC built to be challenged.
> fight <enemy> [with <ally>] Starts a character-vs-character battle (non-creature combat). The Combat feature.
> In a battle
> These only work during an active battle, and a player gets one action per turn (info commands below are free and don't use the turn).

### Command What it does What to set up

> attack [target] [with <move>] Attacks. In creature battles the move is looked up on the active creature; in character battles it uses the equipped weapon. Combat or Creatures feature (whichever the battle is).
> catch [with <ball>] Attempts to capture a wild creature. Creatures feature, and a capture item if your world requires one.
> swap <creature> Switches the active creature. Creatures in the player's party.
> defend Takes a defensive stance. Combat/Creatures feature.
> run Tries to flee the battle. Combat/Creatures feature.
> use <item> [on <target>] Uses an item — heal, revive, buff, teach a move, evolve, throw. The item must have a use effect configured (Lexicon → the item → its use settings).
> talk A conversation action inside a battle. Combat feature.
> Looking around (free info actions)
> These never cost a turn and are always safe to use.

### Command What it does

> inspect [target] Asks the storyteller to describe something.
> inventory Lists the party's items and money.
> status Summarizes the party's creatures' health.
> endbattle Ends the current battle.
> How characters feel (storyteller-emitted)
> Players don't type these — the storyteller writes them after meaningful moments to record relationship changes. They're listed here so you understand what your world is doing.

### Command What it does What to set up

> like / >love / >dislike / >hate <character> [reason] Nudges how a character feels about the player, gently or strongly. Turn on the Relationships system.
> mood <character> <moodlet> Applies a named temporary feeling (a "moodlet"). Relationships on, and the moodlet defined in your Relationships setup.
> Players never see numbers — the storyteller narrates the shift. Full detail is in the Relationships and Attitudes chapter.

### Money, goods, work, and housing

These are the commands players use to interact with your world's economy.

### Command What it does What to set up

> gift <item> to <character> Gives an item to a character and triggers their reaction. The item needs a gift value (Lexicon → item), and Relationships should be on for the feeling to land.
> buy <item> Buys an item from the shop at the current location. A currency (Economy tab) and a marketplace enabled on that location with the item stocked. Only usable while exploring, not mid-battle.
> takejob <job> / >quitjob <job> Takes or leaves a paying job. Author a Job in the Lexicon. Global-scope jobs appear on the world Job Board (takeable anywhere); local jobs must be listed under "Jobs Offered Here" on a location. Needs a currency for the wage.
> rent <property> / >endlease <property> Rents a place (charges the first period and starts recurring rent) or ends the lease. A location set up as a property with rental terms, plus a currency.
> paydebt [amount] [currency] Pays down money the player owes. A currency, and an outstanding debt (which comes from unpaid rent or bills).
> Sandbox / cheat commands
> These let a player hand themselves resources directly. Great for sandbox worlds, generous starting scenarios, and testing — but remember they're always available.

### Command What it does What to set up

> givecurrency <amount> [currency] (also >givegold) Adds money to the wallet. A currency defined.
> spawn <item> [count] (also >giveitem) Adds items to the inventory. The item exists in the Lexicon.
> grant <property> Gives the player ownership of a property outright (no cost). A location set up as a property.
> Setup checklist — what each feature unlocks
> A quick map from "what you turn on" to "which commands start working":

### Turn this on / author this Commands it enables

### Multiple locations (and ideally travel routes) >travel
Combat feature >fight, and the battle actions
Creatures feature >battle, >challenge, >catch, >swap, >status, >heal
Inventory + item use effects >use
Currency + a location marketplace >buy
Item gift value (+ Relationships) >gift
Job lexicon entries (+ location jobs) + currency >takejob, >quitjob
A location's rental terms + currency >rent, >endlease
Currency + a debt >paydebt
Relationships system (+ moodlets) storyteller-emitted >like, >love, >dislike, >hate, >mood
A currency / Lexicon items / a property the sandbox commands >givecurrency, >spawn, >grant
Tips for world creators
Tell players the verbs they can use. Players won't guess that your world supports >buy or >takejob. Mention the relevant commands in your world description, an opening scenario, or a "how to play here" note.
Set the systems up first. A command with nothing behind it (a >buy with no shop, a >takejob with no jobs authored) just won't do anything. Walk through the checklist above for the experience you want.
Let the storyteller do relationships. Don't ask players to type relationship commands — build out your Relationships system and the AI handles it in narration.
Decide how you feel about cheats. The sandbox commands are powerful and always on. If money or scarcity is central to your world's challenge, design around the fact that a determined player can grant themselves resources.

---

# Lexicon

Lexicon is a feature that lets you add roleplay details like lore, background information, characters, and more into your chats. It's an easy way to manage lore entries that's built directly into WyvernChat's chat interface. Think of it as a small and character specific lorebook.

There are three types of Lexicon:
- **Lorebook Lexicon** (in development)
- **Chat Lexicon**: Add entries to any chat you're in, visible only in that specific conversation.
- **Character Lexicon**: Add entries to characters you've created, visible across all chats with that character.

## Key Features

### Character-Specific vs. Chat-Specific Entries
Character Lexicon applies to all chats with that character and is managed from the character editor. Only character creators can add character lexicon entries to their own characters.

### Add Entries While Chatting
Create entries on-the-fly when something new comes up in your story - a location, an NPC, or an item - without leaving the chat page.

*Example:* The AI mentions a tavern called "The Gilded Rose." You can open the Lexicon panel, create an entry for it with details about the tavern's owner, atmosphere, and regular customers, then continue chatting. If you mention The Gilded Rose 100 chats later, the character will recall the details.

### Link Avatars
Give your entries visual identity by uploading an avatar image. This is useful for NPC entries, making it easy to remember who's who in your story.

### Categorize Entries
Organize your entries by type:
- **NPC** - Non-player characters with special name-matching features. See Register NPCs below.
- **Item** - Objects and equipment
- **Location** - Places and settings
- **Event** - Happenings and occasions
- **Concept** - Abstract ideas or themes
- **Memory** - Character memories and past events
- **Other** - Anything else you need

### Register NPCs
When creating an NPC entry, Lexicon performs name-matching that automatically triggers the entry when the character is mentioned by first name, full name, nicknames, or titles.

*Example:* Register an NPC as "Captain Sarah 'Redbeard' Morgan" and fill out the corresponding fields. The entry will activate whether someone says "Sarah," "Captain Morgan," "Redbeard," or "the Captain."

### View Keywords with Highlight Detection
As you chat, Lexicon actively monitors your conversation:
- **Highlighted keywords**: Words matching your lexicon entries appear in color in your messages
- **Clickable words**: Click any highlighted word to view the full entry details
- **Real-time checking**: See exactly what information the AI is receiving

---

## Lorebook Lexicon

Lorebooks can now contain Lexicon entries, which work similarly to traditional lorebook entries: they're triggered by keywords and brought into context when you attach the lorebook to a character.

**Key things to know about Lorebook Lexicon:**
- Lexicon entries in lorebooks function like regular lorebook entries when attached to characters
- Lorebook Lexicon entries won't appear in the Lexicon tab in Chat Mode
- Lorebooks containing only lexicon entries cannot be imported to Studio Mode

This feature is useful if you want to organize your lorebook content using the lexicon format while keeping the lorebook's ability to be shared across multiple characters.
For more information on using WyvernScripts with Lorebook Lexicon, check out the WyvernScripts page.

*(Coming Soon: Character Profile Integration - Lexicon will soon be integrated into character profiles. Check back soon!)*

### How Lexicon is Different from Lorebooks
Both Lexicon and Lorebooks provide background information and context to the AI, but they work in different ways:

| Feature | Lorebooks | Lexicon |
| :--- | :--- | :--- |
| **When you create it** | Before starting your chat | Before or during your chat |
| **Where it lives** | Separate document you attach to characters | Built into the character or specific chat |
| **Best for** | Pre-planned worldbuilding and lore you'll reuse | Character-specific details and spontaneous additions |
| **Sharing across characters** | Yes - one lorebook can be attached to multiple characters | No - entries are tied to specific characters or chats |

**Want to use both? No problem:**
- Attach lorebooks for your core world setting and shared lore
- Use Lexicon for character-specific details and story elements that emerge during conversation

---

## Chat Lexicon

### What is Chat Lexicon?
Chat Lexicon entries are specific to one conversation and only visible in that chat. Anyone can create chat lexicon entries while chatting with any character, even if they didn't create it. These entries are private - the character creator cannot see your chat lexicon entries.

**When to use Chat Lexicon:**
- Adding your own additions to someone else's character
- Scenario-specific details that only apply to one conversation
- Testing out ideas before adding them to your character's permanent lore

### Where to Find Chat Lexicon
The Chat Lexicon panel is accessed from the Chat page:
1. Open any chat with a character
2. Look at the right sidebar
3. Select the 4th tab (the book icon)
4. You'll see the Lexicon panel

From here, you can create new entries, search existing ones, and manage all your chat-specific lore.

### The Fields (Chat Lexicon)

#### Basic Information
- **Avatar:** Upload an image to represent this entry. Especially useful for NPCs and important locations.
- **Entry Name:** The name of your entry as it appears in your list.
- **Priority:** Determines display order when multiple entries trigger simultaneously. Lower numbers appear first. Default: 1
- **Position in Context:** Where the entry appears relative to the character's description. Options:
  - *Before Character:* The entry will be inserted before the character's context in the prompt.
  - *After Character:* The entry will appear after the character context in the prompt.
  - *In Chat:* The entry will appear mixed with chat messages, this is the strongest type of position. A lower insertion order is stronger, while a higher insertion order is weaker.

#### Entry Type & Scripting
- **Entry Type:** Categorize your entry to make it easy to find:
  - *No specific type* (default)
  - *NPC*: Selecting this unlocks the NPC Information panel (define their name, nickname, title, etc) and Lines Parsed (How many paragraphs after the handle `{{npcName}}:` it keeps as the NPC's message. Increase for longer dialog. NOTE: Setting above 1 without an NPC/narrator attached can break replies).
  - *Item*
  - *Location*
  - *Event*
  - *Concept*
  - *Memory*
  - *Other*
- **Lua Callback:** Advanced feature, use this if you have created a script using WyvernScript. Default: No callback.

#### Keys
- **Keys (Primary Keywords):** Main words or phrases that trigger this entry. Press Enter after typing each keyword to add it. Multiple keywords can trigger the same entry.
- **Key Logic:** Determines how primary and secondary keywords work together:
  - *AND ANY (default)* - Activates if primary key + any one secondary key appear
  - *AND ALL* - Activates only if primary key + all secondary keys appear
  - *NOT ANY* - Activates if primary key appears but none of the secondary keys
  - *NOT ALL* - Won't activate if primary key + all secondary keys appear together
- **Secondary Keys:** Additional filtering keywords that work with Key Logic to fine-tune activation conditions.
*(Note: If you only have a Primary Key with no Secondary Keys, the entry will activate whenever the primary key appears. The Key Logic setting won't matter.)*

#### Content
The actual information inserted into the AI's context when triggered. Can be any length.

#### Behavior Settings
- **Enabled:** Toggle entry on/off. Default: ON
- **Case Sensitive:** Whether "Sword" and "sword" are treated as different keywords. Default: OFF
- **Constant:** When enabled, entry is always included in context regardless of keywords. Default: OFF
- **Whole Words Only:** Only matches complete words (e.g., "Art" won't trigger inside "King Arthur"). Default: OFF

#### Advanced Settings
- **Activation Chance (%):** Probability the entry activates when triggered. Default: 100%. Lower for randomness or occasional triggers.
- **Linked Entries:** Select related lexicon entries you created.
- **Custom Fields:** Advanced WyvernScripts feature (in development).
- **Comment:** Internal notes for your reference only. Not visible to others or included in AI context.
- **Labels:** Tags for organizing your entries.

### How to View Chat Lexicon Entries During Chat
Highlighted words that match your lexicon entries are noted in the chat. This shows you which entries are currently activating.
To view entry details, select any highlighted keyword to see the full lexicon entry. A dialog box will appear showing:
- The entry title
- All primary keys
- All secondary keys (if any)
- The full content of the entry

---

## Character Lexicon

### What is Character Lexicon?
Character Lexicon entries apply to all chats with that character and are managed from the character editor. Only character creators can add character lexicon entries to their own characters.

**When to use Character Lexicon:**
- Core character lore that should always be present
- Important NPCs that appear across multiple greetings
- Permanent world details for that character's setting
- Crucial information you want all users to have when chatting with your character

### Where to Find Character Lexicon
Character Lexicon is accessed from the character editor:
1. Go to your character's profile page
2. Click Edit
3. Under Navigation in the lefthand column, navigate to the Lexicon tab
4. You'll see the Character Lexicon panel

### The Fields (Character Lexicon)
Character Lexicon uses the same fields as Chat Lexicon. See The Fields (Chat Lexicon) above for detailed explanations of each field.

**Key differences:**
- Entries created here apply to ALL chats with this character
- Only you (the character creator) can edit these entries
- All users chatting with your character will see these entries activate

### How Character Lexicon Appears in Chats
When users chat with your character, your Character Lexicon entries will automatically activate based on their keywords, just like Chat Lexicon entries. Users will see highlighted keywords and can click them to view the entry details.
*(Note: Users can still create their own Chat Lexicon entries when chatting with your character. Both your Character Lexicon and their Chat Lexicon can work together in the same conversation.)*

---

## Tips and Best Practices
- **Add entries as you go:** Don't feel like you need to plan everything upfront - create entries when new NPCs, locations, or concepts naturally emerge in your story
- **Use Character Lexicon for permanent details:** Information that should always apply to this character across all chats
- **Use Chat Lexicon for scenario-specific info:** Temporary or alternate storyline details that only apply to one conversation
- **Choose clear keywords:** Pick words that will naturally come up in conversation
- **Playtest your Lexicon:** When you test, it's easy to spot mistakes in your writing. Need to turn on Whole Words Only? Not a fan of And Any for tags? This is the time to fine tune!
- **Organize with Entry Types:** Categorizing your entries makes them easier to manage as your list grows
- **Use NPC Registration for recurring characters:** Take advantage of name-matching for characters who appear frequently
- **Don't overload:** You don't need a 200+ token entry for everything - focus on details the AI needs to remember

## FAQ
- **Can I still use my old lorebooks?**
  Yes! Lorebooks work exactly as they did before. You can continue attaching lorebooks to your characters.
- **Can I add Lexicon entries before starting a chat?**
  Yes! Character Lexicon entries can be added anytime from the character editor. Chat Lexicon entries can be added before or during the conversation.
- **What happens if I have both a lorebook and Lexicon with the same keyword?**
  Both will activate. The information from both sources will be included in the AI's context.
- **Can character creators see my Chat Lexicon entries when I chat with their character?**
  No. Your Chat Lexicon entries are private to you. When you create entries while chatting with someone else's character, the character creator cannot see them.
- **Can I add Character Lexicon entries to someone else's character?**
  No. Only character creators can add Character Lexicon entries to their own characters. However, you can create Chat Lexicon entries in any conversation.
- **What's the difference between Character Lexicon and attaching a lorebook to my character?**
  Character Lexicon is built into your character and easier to manage from the editor. Lorebooks are separate files that can be shared across multiple characters. Use whichever works best for your workflow!
