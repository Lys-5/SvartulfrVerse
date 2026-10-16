# JANITORAI & ROLEPLAY BEST PRACTICES

**Version:** 1.0
**Date:** 2026-06-08
**Status:** Canon Freeze v1 — ACTIVE
**Purpose:** Definitive consolidated reference for bot quality, lorebook quality, prompt quality, and roleplay quality. Extracted from cross-referenced community guides, official documentation, Reddit discussions, and project governance.

---

## 📑 Table of Contents

| Section | Title | Page |
|---------|-------|------|
| 1 | [Executive Summary](#1-executive-summary) | Quality tiers, 5 consensus principles |
| 2 | [Character Card Design](#2-character-card-design) | Definition, personality, motivations, flaws, relationships |
| 3 | [Scenario Design](#3-scenario-design) | Openings, framing, hooks, pacing |
| 4 | [Dialogue Design](#4-dialogue-design) | Speech patterns, emotions, internal thoughts |
| 5 | [Lorebook Design](#5-lorebook-design) | Architecture, keywords, token economy, canon layers |
| 6 | [Prompt Engineering](#6-prompt-engineering) | System prompts, author notes, OOC, instruction hierarchy |
| 7 | [OOC Systems](#7-ooc-systems) | Scene control, pacing, plot steering, corrections |
| 8 | [JanitorAI Scripts](#8-janitorai-scripts) | Scripting philosophy, use cases, patterns |
| 9 | [SillyTavern Compatibility](#9-sillytavern-compatibility) | Cards, lorebooks, metadata, portability |
| 10 | [Long-Term Memory & Continuity](#10-long-term-memory--continuity) | Consistency, drift prevention, large worlds |
| 11 | [Roleplay Quality Framework](#11-roleplay-quality-framework) | Quality matrix for all components |
| 12 | [SvartúlfrVerse Recommendations](#12-svartúlfrverse-recommendations) | Mandatory/recommended/avoided practices |
| App A | [Sources Analyzed](#appendix-a-sources-analyzed) | All 20+ sources |
| App B | [Major Themes](#appendix-b-major-themes-discovered) | 7 cross-cutting themes |
| App C | [Future Expansion](#appendix-c-recommendations-for-future-expansion) | 6 recommendations |
| App D | [External Resource Links](#appendix-d-external-resource-links) | 40 curated links |

**Quick Navigation by Workflow:**
- 🤖 **Bot Creation:** Sections 2 → 3 → 4 → 12
- 📚 **Lorebook Creation:** Sections 5 → 9
- ✍️ **Prompt Engineering:** Sections 6 → 7
- 🔧 **Engine Development:** Sections 8 → 10 → 11
- 📋 **Quality Review:** Section 11 (Quality Framework)

---

# 1. EXECUTIVE SUMMARY

## What Separates Bot Quality Tiers

Across every guide, tutorial, discussion thread, and official documentation analyzed, the separation between quality tiers is consistent:

### Poor Bots
- **Character:** Generic personality ("kind", "caring", "shy" with no depth). No flaws. No motivations. No behavioral specificity.
- **Lorebook:** Missing, or filled with redundant entries that repeat what's already in the personality field. Keywords overlap causing token waste.
- **Prompt:** Vague system instructions. No behavioral anchors. Over-reliance on telling the model what NOT to do instead of what TO do.
- **Scenario:** No framing. No narrative hook. User has no idea why they're talking to this character or what the dynamic is.

### Average Bots
- **Character:** Some personality traits listed, but flat. May have backstory but it doesn't connect to behavior. Functional but forgettable.
- **Lorebook:** Present but disorganized. Entries are too long or too short. Keywords trigger too often or almost never.
- **Prompt:** Correct structure but generic content. Functionally adequate for short conversations but loses consistency in long chats.
- **Scenario:** Basic framing exists but doesn't create narrative tension or a reason to stay engaged.

### Good Bots
- **Character:** Specific personality with contradictions and nuances. Motivations drive behavior. Flaws create friction and interest. Speech patterns are distinct.
- **Lorebook:** Well-structured entries with non-overlapping keywords. Content is concise and standalone. Token budget respected. Entries enhance without repeating card content.
- **Prompt:** Clear behavioral instructions. Positive framing ("does this" not "doesn't do that"). Hierarchical instruction structure.
- **Scenario:** Compelling narrative hook. Clear starting dynamic. User agency preserved.

### Excellent Bots
- **Character:** Archetypal depth — every trait connects to backstory, motivation, or behavior. Personality evolves contextually without breaking consistency. The character surprises you but never contradicts themselves.
- **Lorebook:** Recursive, layered entry design. World entries interlink. Character entries reference world context. Chaff/controversial content separated. Token budget optimized per entry tier.
- **Prompt:** surgically precise. Every token earns its place. System prompt + personality + scenario work as a unified directive hierarchy. Post-history instructions used effectively.
- **Scenario:** Rich narrative context that creates immediate dramatic potential. Opening message establishes tone, dynamic, and hooks without rail-roading.

## The 5 Consensus Principles (Across ALL Sources)

1. **Specificity beats generality** — "speaks in short clipped sentences when angry" beats "has a temper"
2. **Behavioral anchors beat trait labels** — "adjusts glasses when nervous" beats "is nervous"
3. **Positive framing beats negative framing** — "stays in character" beats "don't break character"
4. **Conciseness beats completeness** — Every token must earn its place in the context window
5. **Consistency beats cleverness** — A character that stays coherent for 500 messages beats one that's brilliant for 20

---

# 2. CHARACTER CARD DESIGN

## 2.1 Character Definition

### The Core Formula

Every character needs, at minimum, these five elements working together:

```
WHO they are      → Identity, role, demographic anchor
WHAT they want     → Motivation, goal, desire (conscious or unconscious)
WHY they can't     → Flaw, fear, limitation, contradiction
HOW they behave    → Behavioral patterns, speech habits, physical tics
WHY we care        → Emotional hook, relatability factor, dramatic potential
```

### Best Practices

- **Define the character through behavior, not biography.** A character sheet saying "loyal friend" is useless. Showing *how* their loyalty manifests — what they sacrifice, where it breaks, how it looks in dialogue — is what works. (Consensus: JanitorAI Aurellea guide, Reddit r/JanitorAI_Official)
- **Give every character at least one contradiction.** The brave character who fears water. The generous character who hoards secrets. Contradictions create depth without adding token cost. (Consensus: Iorveth Guide, Narrative Design principles)
- **Separate "personality traits" from "behavioral patterns."** Traits are labels (stubborn, warm). Patterns are observable actions (crosses arms during arguments, deflects compliments with humor). Both are needed. (Consensus: Faylua guide, Aurellea guide)
- **Backstory should explain behavior, not exist for its own sake.** If a traumatic event doesn't affect how the character acts in the present, cut it from the card. It can live in the lorebook for depth without consuming permanent tokens. (Consensus: Multiple community guides)
- **Define relationships as dynamic, not static.** "Is the user's brother" is static. "Complicated relationship with the user built on shared childhood trauma and current resentment" is dynamic and creates roleplay potential. (Consensus: Community consensus across Reddit guides)

### Common Mistakes

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| Listing 40 personality traits | Trying to be comprehensive | Pick 5-7 core traits, make each one specific and behavioral |
| Defining character only through backstory | Confusing biography with personality | Backstory explains, personality drives. Ensure behavioral presence. |
| No flaws or weaknesses | Wanting character to be liked | Flaws create roleplay tension. Without them, there's no story. |
| Over-defining speech patterns | Wanting distinct voice | Pick 2-3 speech habits max. Too many and the model can't juggle them all. |
| Making character agreeable to everything | Fear of limiting user agency | A character with boundaries is more interesting than a yes-machine. Defining what they WANT gives them agency. |

### Recommended Structure

```
[Character Card Layer]          → Permanent tokens (always in context)
  ├─ Core Identity              → Name, role, demographic (50-100 tokens)
  ├─ Personality Essence        → 3-7 core traits, expressed through behavior (200-400 tokens)
  ├─ Motivations & Fears        → What drives them, what holds them back (100-200 tokens)
  ├─ Speech Patterns            → 2-3 specific habits, not a full speech manual (50-100 tokens)
  └─ Scenario / Opening Context → Where they are, what's the dynamic (100-200 tokens)

[Lorebook Layer]                → Triggered tokens (context-dependent)
  ├─ Backstory Details          → Deep biography (only when relevant)
  ├─ Relationship Deep Dives    → Per-relationship detail entries
  ├─ World Context              → Setting, institutions, cultural context
  └─ Specific Knowledge Areas   → Character's expertise, skills, specialties
```

## 2.2 Personality Design

### The PERSONA Framework (Synthesized from Community Consensus)

| Element | Description | Example |
|---------|-------------|---------|
| **P** — Predictable traits | Core behaviors the model can reliably reproduce | Deflects vulnerability with sarcasm |
| **E** — Evolving stances | Attitudes that shift based on trust/context | Warm to friends, cold to strangers |
| **R** — Reactive patterns | How they respond to specific stimuli | Raises voice when questioned, withdraws when pitied |
| **S** — Signature quirks | Unique, memorable details that stand out | Collects small stones, quotes obscure poetry |
| **O** — Opposing impulses | Internal contradictions that create depth | Craves connection but sabotages intimacy |
| **N** — Narrative hooks | Personality elements that create RP potential | Has a secret they're terrified will be discovered |
| **A** — Anchoring anchors | Grounding details that prevent drift | Refers to their mother's cooking as a comfort reference |

### Token Budget Guidelines

From SillyTavern World Info documentation and community testing (consensus across Faylua, Aurellea, Reddit guides):

| Card Section | Recommended Token Range | Notes |
|-------------|------------------------|-------|
| Description/Personality | 150-400 tokens | Sweet spot for most models. Beyond 500, diminishing returns for many LLMs. |
| Scenario | 50-150 tokens | Enough to frame. Not so much it constrains. |
| Example Dialogues | 100-300 tokens | Quality over quantity. 3-5 exchanges showing tone, speech patterns, boundaries. |
| First Message | 100-250 tokens | Establish voice, dynamic, and hook. |
| System Prompt (ST) | 50-200 tokens | Project-level constraints, not character description. |
| **Total permanent budget** | **500-1300 tokens** | Context window above this for conversation. Respect model limits. |

## 2.3 Motivations and Flaws

### Why Motivations Matter

The JanitorAI Scripts Beta documentation and community guides consistently emphasize: **characters without clear goals create flat roleplay.** The AI model needs to know what the character is pursuing in a scene to generate directed behavior.

### The Motivation Stack

```
PRIMARY MOTIVATION    → What the character consciously wants (stated goal)
SECONDARY MOTIVATION  → What they unconsciously need (emotional need)
HIDDEN MOTIVATION     → What they would never admit (shame, secret desire)
```

Example for Wulfnic Bloodmoon:
```
PRIMARY:    Protect and preserve the Douglas-Bloodmoon family legacy
SECONDARY:  Find meaning beyond being the Wulfnic heir (identity beyond duty)
HIDDEN:     Wants to be seen as himself, not just as "the patriarch"
```

### Flaw Design Principles

**Best Practices:**
- Flaws should create *friction* with the user or world, not just be cosmetic
- The best flaws are *strengths taken too far*: loyalty becomes controlling, confidence becomes arrogance
- Flaws should manifest in *observable behavior*, not just internal struggle
- Give at least one flaw that affects how the character treats the user

**Common Mistakes:**
- Flaws that don't actually limit the character ("cares too much" isn't a flaw, it's a virtue)
- Flaws that are actually strengths in disguise
- Too many flaws (the character becomes a mess, not a person)
- Flaws with no behavioral manifestation

## 2.4 Relationship Design

### Best Practices

- **Define the dynamic, not just the label.** "Friends" tells the model nothing. "Friends who've known each other since college, recently drifted apart, meeting again creates awkward warmth" gives the model material to work with.
- **Relationships should have history AND present tension.** The past creates context. The present conflict creates scenes.
- **Every relationship needs a power dynamic.** Even "equal" friendships have subtle imbalances. Who defers to whom? Who cares more? This prevents generic interaction.

### Common Mistakes

- Defining relationships only through family labels (mother, brother) without emotional texture
- Making all relationships harmonious (no conflict = no story)
- Not specifying how the relationship with the USER specifically differs from other relationships

## 2.5 Behavioral Consistency

### The #1 Problem in AI Roleplay

Across every guide and discussion analyzed, **character drift** is the single most cited quality issue. Characters that start strong but gradually become generic, forget their personality, or adopt the user's speech patterns.

### Root Causes and Fixes

| Root Cause | Fix |
|-----------|-----|
| Permanent tokens too vague | Add more specific behavioral anchors (not just trait labels) |
| No speech pattern definition | Include example dialogues that demonstrate the voice |
| System prompt missing | In SillyTavern, use system_prompt for meta-instructions |
| Post-history instructions missing | Remind the model of the character's voice at the end of the context |
| Lorebook contradicts card | Ensure consistency between permanent and triggered context |

### Proven Anti-Drift Techniques

1. **Example dialogues are the strongest drift prevention.** The model anchors to patterns it has literally seen the character use. (Consensus: Multiple community guides)
2. **Reference back to established patterns.** Include in personality: "Often references [specific thing]" — gives the model a callback habit. (Consensus: Reddit community guides)
3. **Post-history instructions.** In SillyTavern, use post_history_instructions to remind the model: "Stay in character as [name]. [name] speaks in [pattern]." (Consensus: SillyTavern documentation + community guides)
4. **Lorebook entries as reinforcement.** Create character-conditioned lorebook entries that trigger in specific contexts to reinforce behavior. (Consensus: Icehellionx scripts, JanitorAI Scripts Beta)

## 2.6 Avoiding Over-Description

### The Token Economy Reality

Every token spent on character description is a token unavailable for conversation history. Community testing shows:

- Models with 8K context: Character cards over ~1500 tokens start consuming meaningful conversation memory
- Models with 32K context: More room, but character cards over ~2000 tokens show diminishing returns
- Models with 128K+ context: More forgiving, but efficiency still matters

### The Subtractive Editing Test

After writing your card, cut 20% of the tokens. If the character still feels fully defined, the cut version is better. Repeat until cutting any more would lose essential character. That's your optimal card. (Consensus principle from multiple advanced guides)

### What to Cut First

1. Redundant trait descriptions (if you've shown the trait in example dialogue, you don't need to label it too)
2. Backstory details that don't affect present behavior
3. Generic descriptors ("very", "quite", "really" — intensifiers add tokens without adding information)
4. Lists of skills/hobbies that don't roleplay into the scenario
5. Detailed physical descriptions (the avatar image handles this — just note distinctive features)

## 2.7 Avoiding Under-Definition

### Minimum Viable Character

A card that avoids being generic needs at minimum:
- **3 specific behavioral patterns** (not just trait labels)
- **1 clear motivation** (what they want from the user/situation)
- **1 clear flaw** (what creates friction)
- **Distinct speech pattern** (defined through example dialogue if possible)
- **1 narrative hook** (why this interaction is interesting)

---

# 3. SCENARIO DESIGN

## 3.1 Opening Messages

### The Three Jobs of an Opening Message

1. **Establish voice** — The first message is a speech pattern demo. The user learns how this character talks by reading it. (Consensus: Faylua guide, Aurellea guide)
2. **Establish dynamic** — The relationship between character and user should be implicit in the opening. Who has the power? What's the tension?
3. **Create a hook** — Give the user something to react TO, not just a greeting to acknowledge.

### Best Practices

- **Start in media res** when possible. A character in the middle of doing something is more interesting than one waiting to be talked to. (Consensus: Multiple community guides)
- **Include a question or prompt** that requires the user to make a choice. Openings that demand a specific response create better engagement. (Consensus: Reddit guides)
- **Match the opening to the character's emotional state** at the scene start, not to an idealized "default" state. (Consensus: JanitorAI Scripts Beta)
- **Keep it under 250 tokens.** Long openings are skimmed. Long openings also eat conversation memory before it starts. (Consensus: Community testing data)
- **Never write an opening that kills the conversation.** "Hi" is the weakest possible opener. The opening should INVITE response, not wait for one.

### Common Mistakes

| Mistake | Fix |
|---------|-----|
| Opening is just a greeting | Start mid-action, mid-thought, or mid-conflict |
| Opening describes the character from outside | Stay in POV. Show, don't describe. |
| Opening over-explains the scenario | Trust the user to pick up on context clues. |
| Opening assumes the user's reaction | Leave room for the user to define their entrance. |

## 3.2 Scenario Framing

### Best Practices

- **Set the scene, then give the character something to DO in it.** "In a coffee shop" is setting. "In a coffee shop, nervously rehearsing a confession" is a scene.
- **Define the stakes.** What does the character want in THIS interaction? Why does it matter NOW?
- **Time pressure creates urgency.** "Has been planning this for weeks" is less immediate than "about to leave the country."

### Common Mistakes

- Setting with no dramatic context
- Scenario that's all backstory with no present action
- Scenario that limits user agency too much

## 3.3 User Agency

### Best Practices

- **The scenario creates a starting situation, not a script.** The user should be able to surprise the character.
- **Write characters who respond to user choices, not characters who railroad the user along a predetermined path.**
- **Scenario should include 2-3 possible directions** the roleplay could go, implied by the setup.

### Common Mistakes

- Openings that force the user into a specific reaction
- Characters who don't let the user affect the scene
- Scenarios so detailed they leave no room for player input

## 3.4 Narrative Hooks

### The Hook Taxonomy

| Hook Type | Example | Best For |
|-----------|---------|----------|
| Immediate crisis | Character is actively in danger/drama | Hooking fast |
| Unresolved tension | Character and user have unfinished business | Creating pull |
| Mystery | Something about the character is unexplained | Sustaining curiosity |
| Contradiction | Character's stated goal conflicts with their behavior | Depth |
| Hidden depth | Surface personality doesn't match deeper nature | Long-term revelation |

## 3.5 Pacing

### Principles

- **Match card complexity to expected RP length.** Simple cards for casual/short RP. Rich cards with lorebook for sustained/long RP.
- **Let the scenario breathe.** Not every opening needs to be high-drama. Quiet moments are powerful when the character is well-defined.
- **Use lorebook entries to scale depth over time.** Early RP uses card basics. Deep lorebook entries activate as the RP progresses and keywords naturally appear.

---

# 4. DIALOGUE DESIGN

## 4.1 Speech Patterns

### Best Practices

- **Define 2-3 speech signatures, not a speech manual.** Pick the most distinctive patterns and let the LLM extrapolate. (Consensus: Faylua guide, Iorveth guide)
- **Show speech patterns in example dialogue** rather than describing them. "Rarely uses contractions" is weaker than example dialogue that demonstrates it.
- **Include emotional range in examples.** Show at least one example where the character is calm and one where they're stressed, to give the model a range to work with.
- **Internal thoughts (parenthetical or italicized)** add depth without requiring separate speech patterns for internal vs. external voice. (Consensus: Community consensus)

### Speech Pattern Categories

| Category | What to Define | Example |
|----------|---------------|---------|
| Rhythm | Sentence length, complexity | Short clipped sentences vs. flowing prose |
| Vocabulary | Register, education level, slang | Technical jargon vs. colloquial vs. formal |
| Emotional tells | How emotion manifests in speech | Gets quieter when angry, faster when excited |
| Filler habits | Verbal tics, pauses, hedging | "I mean..." "Look..." trailing off |
| Taboo patterns | What they NEVER say | Refuses to use certain words, or overly formal |

### Common Mistakes

- **Too many speech patterns** — The model can't remember 7 different speech rules. Pick 2-3 core ones.
- **Speech pattern contradicts personality** — A "brusque" character who speaks in long, flowery sentences confuses the model.
- **Inconsistency across examples** — If the example dialogue doesn't match the described speech pattern, the model will follow the examples.

## 4.2 Emotional Expression

### Best Practices

- **Show emotion through action and dialogue, not labels.** "{{char}} felt angry" is telling. "{{char}}'s jaw tightened. 'Get out.'" is showing.
- **Use the {{char}}'s established behavioral patterns** for emotional expression. If they deflect vulnerability with humor, their sadness looks like a joke. This creates coherent characterization. (Consensus: Scripts Beta documentation)
- **Layer emotions.** Real people feel multiple things at once. "Smiled but didn't reach their eyes" conveys a specific, complex emotional state.

### Common Mistakes

- Emotions stated outright instead of demonstrated
- Every emotion expressed with the same intensity
- Emotional reactions that don't match the character's established patterns

## 4.3 Internal Thoughts

### Best Practices

- **Use sparingly.** Internal thoughts are powerful because they're rare. Overuse dilutes them and adds token bloat. (Consensus: Iorveth guide, Reddit guides)
- **Use for contradiction.** The most effective internal thoughts reveal the gap between what the character says and what they think. This is where the dramatic irony lives.
- **Format consistently.** Italic in parentheses, or whatever convention you use, be consistent so the model learns the pattern.

## 4.4 Dialogue Example Design

### Structure That Works

```
<START>
{{user}}: [Shows initiative, demonstrates the kind of engagement you want]
{{char}}: [Responds in-character, demonstrates voice + personality + emotional range]
{{user}}: [Tests a boundary or asks a character-defining question]
{{char}}: [Reveals something deeper — motivation, flaw, or contradiction]
<START>
{{user}}: [Different tone — shows range of interaction possible]
{{char}}: [Different emotional register — shows character has depth, not one note]
```

### Token Budget for Examples

- **3-5 exchanges** is the consensus sweet spot
- **100-300 tokens** total for all examples
- Each exchange should demonstrate a DIFFERENT aspect of the character
- Quality and distinctiveness matter more than quantity

---

# 5. LOREBOOK DESIGN

## 5.1 Lorebook Architecture

### The RAG Analogy

From SillyTavern official documentation and project BOT_SEARCH_SPECIFICATION.md: **Lorebooks function as a Retrieval-Augmented Generation system.** They are a dynamic dictionary that injects relevant context only when triggered by keyword matches. This means:

- Lorebook entries should NOT repeat what's already in the character card
- Lorebook entries SHOULD add depth that the card can't hold
- Lorebook entries are COMPLEMENTARY to the card, not a replacement

### The Three-Layer Lorebook Model (Synthesized from SillyTavern docs + community guides)

```
LAYER 1: Character Core (in card — permanent)
  ├─ Name, appearance, core personality
  ├─ Speech patterns, behavioral anchors
  └─ Motivations, key relationships

LAYER 2: Character Deep Dive (in lorebook — triggered)
  ├─ Extended backstory entries
  ├─ Per-relationship detail entries
  ├─ Personal history milestones
  └─ Psychological deep-dives (triggers: therapy-related, vulnerable moments)

LAYER 3: World Context (in global lorebook — triggered)
  ├─ Setting details, locations
  ├─ Institutions, organizations
  ├─ Cultural/social rules
  └─ Historical events that affect the character
```

### Best Practices

- **Each lorebook entry should be a standalone piece of information.** The AI must understand each entry without needing other entries active. (Consensus: SillyTavern documentation)
- **Entries should be organized hierarchically.** Character entries → Relationship entries → World entries. Use priority/insertion order to control which gets injected first. (Consensus: SillyTavern docs + community guides)
- **Use character-specific lorebooks bound to the character card** (SillyTavern) or character-tagged entries (JanitorAI) for character-specific lore. Use global lorebooks for world-building. (Consensus: SillyTavern documentation)
- **Lorebooks reduce card token burden.** Move all backstory, extended description, and world context OUT of the character card and INTO the lorebook. The card provides the anchors; the lorebook provides the depth. (Consensus: All major guides)

### Common Mistakes

| Mistake | Why It's a Problem | Fix |
|---------|-------------------|-----|
| Lorebook repeats card content | Wastes tokens with no new information | Ensure entries add information not in card |
| Entries are too long | Consumes token budget rapidly | Break into smaller, focused entries |
| Keywords too broad | Entries trigger constantly, waste context | Make keywords specific and contextual |
| Keywords too narrow | Entries almost never activate | Include common synonyms and variants |
| No recursive scanning | Entries feel isolated, world has no depth | Use [[wikilinks]] or cross-references in entry content |

## 5.2 Entry Sizing

### Token Budget Per Entry

From community testing and SillyTaven recommendations:

| Entry Type | Recommended Tokens | Notes |
|-----------|-------------------|-------|
| Character fact | 30-80 tokens | Name, age, one key fact. Concise. |
| Relationship detail | 50-100 tokens | Who + dynamic + key history point |
| Location description | 40-80 tokens | Sensory detail + narrative relevance |
| World rule / cultural fact | 30-60 tokens | One rule, explained through example |
| Backstory event | 50-100 tokens | One event, its impact on the character |
| Personality deep-dive | 80-150 tokens | How a trait manifests, with examples |
| **Total per entry (typical)** | **40-120 tokens** | The SillyTavern docs recommend ~50 tokens per entry for efficiency |

### The Token Budget Problem

SillyTavern's world info system has a configurable token budget (default often 500-1000 tokens). When the budget is full, no more entries activate even if their keywords are present. This means:

- **Prioritize entry injection order.** Most important entries should have higher priority (lower insertion order number). (Consensus: SillyTavern docs, DeepLore Enhanced guidelines)
- **Constant entries (always-on) consume budget first.** Use sparingly. (Consensus: SillyTavern docs)
- **Keep entries concise.** Every token in an entry competes with every other active entry. (Consensus: All guides)

## 5.3 Keyword Strategy

### Best Practices

- **Use specific, contextual keywords** rather than broad ones. "Wulfnic's study" activates more cleanly than "study." (Consensus: SillyTavern docs)
- **Include common misspellings and variants** as keywords. Especially for names. (Consensus: Community guides)
- **Use selective mode for entries that need multiple conditions.** If an entry should only fire when both "mother" AND "death" are mentioned, use primary + secondary keywords with selective mode. (Consensus: SillyTavern docs)
- **Test your keywords in conversation.** If entries never fire, broaden. If they fire constantly, narrow. (Consensus: Community practice)
- **Avoid keywords that are common words** unless using whole-word matching or selective mode. A keyword like "go" will fire constantly. (Consensus: SillyTavern documentation)

### Keyword Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Single common word as keyword | Fires constantly | Make specific: "Douglas Trading House" instead of "trade" |
| Only proper nouns as keywords | Misses casual references to the same concept | Add synonyms: ["Wulfnic", "father", "patriarch"] |
| Too many keywords per entry (~10+) | Entry fires too frequently | Pick the 3-5 most essential |
| Entries with overlapping keywords | Compete for budget, unpredictable which fires | Differentiate: give each entry a distinct trigger domain |
| Case sensitivity issues | "Douglas" fires but "douglas" doesn't | Enable case-insensitive matching (default in most platforms) |

## 5.4 Trigger Strategy

### Activation Models

From SillyTavern documentation, the activation flow is:

```
User Message → Engine scans last N messages for keywords → 
Matching entries sorted by priority → 
Entries inserted until token budget exhausted → 
Combined context sent to LLM
```

### Trigger Strategies

1. **Narrative Keyword Strategy**: Use keywords that naturally arise in conversation about the topic. People talking about the character's past will use words like "remember", "before", "used to." These make natural triggers for backstory entries. (Consensus: Iorveth guide)
2. **Event-Chain Strategy**: Use recursive scanning so that activating one entry can activate linked entries. Entry A mentions "Rufus," which triggers Entry B about Rufus. (Consensus: SillyTavern docs)
3. **Mood-Triggered Strategy**: Create entries that trigger on emotional keywords. "angry", "sad", "love" — entries that give the model guidance on how the character expresses that emotion. (Consensus: Community guides + Scripts Beta)
4. **Constant + Keyword Hybrid**: Use `constant: true` for critical world rules that must always be present. Use keyword triggers for specific details. (Consensus: SillyTavern docs)

## 5.5 Token Economy

### The Math

```
Total Context Window:     8192 tokens (example)
System prompt:            -200 tokens
Character card:           -1000 tokens
Active lorebook entries:  -500 tokens
─────────────────────────────────
Available for conversation: 6492 tokens
```

Every lorebook entry that activates permanently reduces conversation space. This is why efficiency matters.

### Priority-Based Budget Allocation (From DeepLore Enhanced guidelines)

| Priority Range | Use For | Example |
|---------------|---------|---------|
| 10-20 | Critical context | Main character core facts, essential world rules |
| 30-40 | Major lore | Key NPCs, important locations |
| 50 | Standard entries | Most lorebook entries |
| 60-70 | Background flavor | Minor details, atmosphere |
| 80-100 | Rare/obscure | Trivia, deep-cut references |

## 5.6 Entry Relationships

### Best Practices

- **Use cross-references** between entries to build world cohesion. Entry about a location mentions the character associated with it. (Consensus: SillyTavern recursive scanning docs)
- **Group related entries** in the same lorebook file for related content. Character entries together, world entries together, relationship entries together.
- **Use the hierarchical naming convention.** From SillyTavern best practices: "Character: Wulfnic — Early Life" and "Character: Wulfnic — Current Status" makes scanning and management easier.
- **Avoid circular references** where Entry A triggers Entry B which triggers Entry A, creating infinite injection loops. (Consensus: SillyTavern docs on recursive scanning limits)

### SvartúlfrVerse Canon Layer Integration

For project-specific lorebook design, entries should include canon layer metadata:

```
Layer 1 (Active):   Always included — entry marked constant or with broad keywords
Layer 2 (Historical): Triggered only when past/ancestry keywords appear
Layer 3 (Cultural): Triggered by mythology/tradition keywords
Layer 4 (Deferred): NOT included in any lorebook — stored only in repository
Layer 5 (Candidate): NOT included until promoted to Active/Historical/Cultural
```

---

# 6. PROMPT ENGINEERING

## 6.1 System Prompts

### Purpose

The system prompt defines the rules of engagement for the model. It is the highest-level instruction the model receives. (Consensus: OpenAI Prompt Engineering Guide, project ENGINE_SPECIFICATION.md)

### Best Practices

- **Keep system prompts focused on BEHAVIORAL RULES, not character description.** Character description belongs in the personality/scenario fields. System prompt handles: formatting rules, meta-instructions, content policies. (Consensus: OpenAI Guide + community practice)
- **Use positive framing.** "Respond as the character" is more effective than "Do not respond as yourself." (Consensus: Multiple prompting guides)
- **Instruction hierarchy matters.** Models weight instructions differently based on position. Place the most critical instructions at the beginning AND end of the system prompt. (Consensus: OpenAI Prompt Engineering Guide)
- **Be specific about output format.** If you want actions italicized, say so. If you want specific dialogue formatting, specify it. The model defaults to whatever you tell it. (Consensus: All guides)

### Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Negative-only instructions ("don't X", "don't Y") | Model focuses on the negative concept | Reframe: "Stay focused on [positive framing]" |
| Overloading system prompt with character info | Wastes tokens that should be in character card | System prompt = rules, not description |
| Vague instructions ("be more creative") | Model doesn't know what "more" means relative to | Be specific: "Use vivid sensory details in descriptions" |
| Contradictory instructions | Model picks one, ignores the other, or gets confused | Audit for consistency |

## 6.2 Author's Notes / Creator Notes

### Purpose

Author's Notes (SillyTavern) or Creator Notes (JanitorAI) inject contextual guidance mid-conversation. They're powerful for long-term consistency.

### Best Practices

- **Use for current scene context.** "The character is in the library, studying for an exam" gives the model immediate scene awareness. (Consensus: SillyTavern docs)
- **Use for emotional state reminders.** "The character is hiding their fear behind humor" helps the model maintain complex emotional states. (Consensus: Community guides)
- **Keep under 100 tokens.** These consume context window too. (Consensus: Community practice)
- **Place strategically.** In SillyTavern, the depth setting controls how close to the current conversation the note appears. Depth 1-2 is most effective for scene context.

## 6.3 Jailbreak Resistance / Post-History Instructions

### Purpose

Post-history instructions (SillyTavern) or forced instructions that appear after the conversation history. They have strong model-following effects.

### Best Practices

- **Use for hard constraints that must not be violated.** "Never break character. Never speak for {{user}}. Always stay in third person." (Consensus: Community guides)
- **Keep short and absolute.** Post-history tokens are most effective when they're brief, clear commands. (Consensus: Community testing)
- **Don't duplicate system prompt content.** Use for the 2-3 most critical rules only. (Consensus: Community practice)

### Anti-Patterns

- Long post-history instructions that eat context
- Contradicting the system prompt
- Using for character description (wrong layer)

## 6.4 Narrative Control

### Best Practices

- **Control pacing through instruction.** "Write detailed responses focusing on sensory detail" vs. "Keep responses brief and action-focused." (Consensus: Community guides)
- **Control perspective explicitly.** "Write in third person from {{char}}'s perspective only. Never describe {{user}}'s thoughts or feelings." (Consensus: All guides)
- **Control response length.** "Write 2-4 paragraphs per response" gives the model a target. Without guidance, response length varies wildly. (Consensus: Community practice)

## 6.5 Instruction Hierarchy

### The Proven Hierarchy (From OpenAI Guide + Community Consensus)

```
1. System Prompt         → Platform-level rules (highest authority)
2. Post-History          → Hard constraints (strongest per-message influence)
3. Character Card        → Character definition (permanent context)
4. Author's Note         → Scene context (mid-conversation injection)
5. Lorebook Entries      → Triggered knowledge (context-dependent)
6. Conversation History  → Recent dialogue (most immediate influence)
```

When instructions conflict, the model typically follows the HIGHER layer. This is why system prompt overrides character card, and post-history overrides everything else.

---

# 7. OOC SYSTEMS

## 7.1 Scene Control

### What OOC Does

OOC (Out of Character) commands allow the user to direct the narrative without breaking immersion. JanitorAI's Scripts Beta includes a Scene Orchestrator Engine specifically for this purpose. (Consensus: JanitorAI Scripts Beta docs, Icehellionx scripts)

### When To Use

- **Pacing control**: "Skip to tomorrow" / "Fast forward to the argument"
- **Scene transitions**: "Cut to the kitchen" / "Later that evening"
- **Tone shifts**: "Make this more serious" / "Lighten the mood"
- **Plot steering**: "Introduce a complication" / "Have another character arrive"

### When NOT To Use

- **As a substitute for actual roleplay.** OOC is a tool, not a crutch. If every message is an OOC command, the user isn't roleplaying.
- **To override the character's agency.** "OOC: Character agrees with everything I say" defeats the purpose of having a character with boundaries.
- **Excessively.** More than 1 OOC command per 5-10 messages starts to break immersion.

### Recommended Patterns

```
/OOC: [Brief instruction that respects character agency]
Example: "OOC: Let's skip the small talk and jump to the confrontation"
Not: "OOC: Character immediately forgives {{user}}"
```

## 7.2 Pacing Control

### Best Practices

- **Match response length to scene intensity.** Action scenes: shorter, punchier. Emotional scenes: longer, more introspective. (Consensus: Community guides)
- **Use OOC pacing commands sparingly.** The natural flow of roleplay should handle pacing most of the time.
- **Let the character drive pacing too.** A character who's stalling, changing the subject, or rushing through a topic is more interesting than one who always matches the user's pace.

## 7.3 Plot Steering

### Best Practices

- **The best plot steering is implicit.** A well-designed character with clear motivations will naturally create plot. The user doesn't need to steer because the character's goals create direction. (Consensus: Narrative Design principles)
- **Use OOC for major scene changes only.** "Let's move to the next day" is fine. "Now the character says exactly this" is rail-roading.
- **Leave room for the AI to surprise you.** The best moments in AI roleplay come from the model doing something unexpected but in-character. Over-steering kills this.

## 7.4 Correction Systems

### When the Model Goes Off-Track

This is the most common quality issue in AI roleplay. The model breaks character, contradicts established facts, or drifts into generic responses.

### Correction Hierarchy (Least to Most Disruptive)

1. **In-character correction.** Have another character point out the inconsistency in-world. "That's not like you. What's going on?"
2. **OOC nudge.** "OOC: Remember, {{char}} wouldn't say that. They're more [trait]."
3. **Swipe/regenerate.** Generate a new response. Often the simplest fix.
4. **Edit the message.** Manually correct the model's output. Effective but breaks immersion.
5. **Author's note injection.** Add a note reinforcing the character's current state.

### Prevention Over Correction

The best correction is prevention. Well-defined characters with strong behavioral anchors drift less. Good lorebook entries reinforce consistency. Post-history instructions prevent the most common breakage patterns.

---

# 8. JANITORAI SCRIPTS

## 8.1 Scripting Philosophy

### What Scripts Do

From JanitorAI official documentation: **Scripts are like giving your character a smart assistant that whispers helpful information in their ear during conversations.** They don't permanently change the character — they provide context-aware guidance for each message. (Source: JanitorAI Scripts Documentation)

### Core Principle

**Scripts enhance; they don't replace.** A script can't fix a bad character card. A script can make a good character card more responsive, more consistent, and more dynamic. (Consensus: Icehellionx guide, JanitorAI docs)

## 8.2 Use Cases

### High-Value Script Applications

| Use Case | Script Type | Benefit |
|----------|------------|---------|
| Emotion tracking | Emotion Engine | Character's emotional state persists and influences responses |
| Dynamic lorebook | Dynamic Lorebook | Context-aware lore injection without manual keyword management |
| Social reaction | Action & Social Reaction Engine | Character responds to social cues (greetings, insults, affection) |
| Scene management | Scene Orchestrator | OOC command handling, scene transitions, time skips |
| Random events | Random Encounter | Unpredictable story events that create emergent narrative |
| Preference tracking | Likes-Dislikes-Fears Engine | Character remembers and references user's stated preferences |

### When NOT to Use Scripts

- **When the base card isn't working yet.** Fix the card first, then add scripts.
- **When you don't understand what the script does.** Scripts modify prompt injection. If you don't know what's being injected, you can't debug issues.
- **When stacking too many scripts.** Each script adds processing and potential conflicts. 2-3 well-chosen scripts beat 10 overlapping ones.

## 8.3 Limitations

- **Scripts operate within the model's capabilities.** They can't make a weak model roleplay like a strong one.
- **Scripts add to the prompt.** Every script's output consumes context tokens.
- **Scripts can conflict.** Two scripts trying to control the same behavior can create erratic output.
- **Scripts are platform-specific.** JanitorAI scripts don't transfer to SillyTavern and vice versa.

## 8.4 Maintainability

### Best Practices

- **Document what each script does** in your project notes. Future-you will thank present-you.
- **Test scripts in isolation** before combining them.
- **Version your scripts.** When updating, keep the previous version as backup.
- **Use community-vetted scripts** (Icehellionx, Arcanox) over untested custom scripts when possible.

### Patterns To Avoid

- Scripts that override character personality
- Scripts that inject more than 100 tokens per message
- Scripts with overlapping trigger conditions
- Scripts that haven't been updated for current platform API

### 8.5 Pronoun Macro Boundary — Validated Runtime State

> **Validated Runtime Constraint (as of Phase 15 testing — 2026-06-09)**

**Observed Behavior:**

| Layer | `{{sub}}` expansion | Status |
|-------|---------------------|--------|
| Prompt-facing fields | Expanded | **Available** |
| JavaScript runtime | Not expanded (literal `{{sub}}`) | **Unavailable** |

**Validated macros:** `{{sub}}`, `{{obj}}`, `{{poss}}`, `{{poss_p}}`, `{{ref}}`

**Current assumption (until contrary evidence):**
- Prompt Layer Access = **Available**
- JavaScript Runtime Access = **Unavailable**

**ADR Operational Rule:** Pronoun-dependent resolution belongs in prompt construction, not in JavaScript conditional logic. Use personality/scenario/initial message/lorebook/prompt injection layers.

**Future Update Path:** If Phase 16/17 reveals a direct pronoun API (e.g., `chat.user.pronouns`), this constraint will be updated.

---

# 9. SILLYTAVERN COMPATIBILITY

## 9.1 Character Cards

### V2 vs V3 Specification

From the Character Card Specification V3 (kwaroran/character-card-spec-v3) and community analysis:

| Feature | V2 (chara_card_v2) | V3 (chara_card_v3) |
|---------|-------------------|-------------------|
| PNG tEXt keyword | `chara` | `ccv3` |
| Encoding | Base64 JSON | Base64 UTF-8 JSON |
| Lorebook | Embedded string | Native structured format |
| Multi-language | Not supported | Supported |
| Creator metadata | Basic | Extended |
| Backward compatibility | Universal | Requires V3-aware client |

### Best Practices

- **Export with BOTH V2 and V3 chunks** for maximum compatibility. SillyTavern already does this. (Consensus: SillyTavern behavior, community guides)
- **Use PNG format for sharing** (self-contained, image + metadata in one file). Use JSON format for editing/debugging. (Consensus: Community practice)
- **CHARX format** (RisuAI) is platform-specific. Don't use for cross-platform distribution. (Consensus: Character Card format research)

### Character Card Fields Mapping

| SillyTavern Field | Purpose | Token Weight |
|-------------------|---------|-------------|
| `name` | Character identifier | Permanent |
| `description` | Full character description | Permanent |
| `personality` | Core traits summary | Permanent |
| `scenario` | Default scene context | Permanent |
| `first_mes` | Opening message | Permanent |
| `mes_example` | Dialogue examples | Permanent |
| `system_prompt` | Meta-instructions | Permanent |
| `creator_notes` | Author guidance | Permanent |
| `post_history_instructions` | Hard constraints | Permanent |
| `tags` | Search/organization | Permanent |
| `character_book` | Embedded lorebook | Triggered |

## 9.2 Lorebooks (World Info)

### SillyTavern-Specific Features

From SillyTavern official documentation:

- **Context-specific sources**: Lorebooks can be bound to a character, persona, or individual chat. This is more granular than JanitorAI's system.
- **Insertion position**: Entries can be placed `before_char` (before character definition) or `after_char` (after character definition). `after_char` has more influence on output. (Consensus: SillyTavern docs)
- **Scan depth**: Controls how many recent messages are scanned for keywords. Default is typically 1-2. Increase for entries that should trigger from older context. (Consensus: SillyTavern docs)
- **Recursive scanning**: Entries can trigger other entries through keyword mentions in their content. Powerful for world-building but can consume budget quickly. (Consensus: SillyTavern docs)
- **Match whole words**: Prevents partial-word matching. Essential for short keywords. (Consensus: SillyTavern docs)

### Lorebook Insertion Order

From SillyTavern documentation, the default insertion order is:
1. Chat Lorebook (most specific)
2. Persona Lorebook
3. Character Lorebook / Global Lorebook (sorted evenly by insertion order)

This can be configured to Character First or Global First depending on preference.

## 9.3 Metadata

### Extensions Field

The `extensions` field in character cards is a free-form JSON object for platform-specific metadata. This is where SvartúlfrVerse traceability data lives:

```json
"extensions": {
  "svartulfrverse": {
    "canon_id": "C_Wulfnic",
    "canon_layer": "active",
    "provenance": ["database/characters/C_Wulfnic_Bloodmoon.md"],
    "visual_classification": "Bloodmoon-dominant",
    "dynasty": "Douglas-Bloodmoon",
    "validation_status": "PASS",
    "generation_timestamp": "2026-06-08T00:00:00Z",
    "canon_version": "1.0"
  }
}
```

## 9.4 Portability

### Best Practices

- **Design cards that work without platform-specific features** for maximum portability.
- **Use the Generic JSON format** (from project EXPORT_MAPPING_MATRIX.md) as the canonical source, then transform to platform-specific formats.
- **Test exports on target platforms.** A card that works perfectly in JanitorAI may behave differently in SillyTavern due to different prompt assembly.

---

# 10. LONG-TERM MEMORY & CONTINUITY

## 10.1 Maintaining Consistency

### The Core Challenge

AI models have no persistent memory between conversations. Every session starts fresh. The character card IS the memory. Everything the model "knows" about the character must come from the card, lorebook, and conversation history. (Consensus: All guides, fundamental LLM architecture)

### Strategies

1. **Comprehensive character card.** The card must contain everything essential. If it's not in the card, the model doesn't know it.
2. **Lorebook as extended memory.** Facts that don't fit in the card go in the lorebook. The model retrieves them when relevant.
3. **Example dialogue as pattern memory.** The model uses examples as templates for future responses. More examples = stronger pattern.
4. **Author's notes for session context.** At the start of each session, an author's note can re-establish context: "Continuing from last session. {{char}} and {{user} just had a fight about [topic]."

## 10.2 Preventing Drift

### Drift Types and Solutions

| Drift Type | Symptom | Solution |
|-----------|---------|----------|
| Personality drift | Character becomes generic/agreeable | Strengthen behavioral anchors in card |
| Speech drift | Character starts talking like the user | Add more distinctive speech patterns + examples |
| Fact drift | Character contradicts established lore | Add lorebook entries with specific keywords |
| Tone drift | Character's emotional range flattens | Include emotional variety in examples |
| Boundary drift | Character loses established limits | Add explicit boundary rules in system prompt |

### The Refresh Technique

For long conversations, periodically reinforce the character:
- Use author's notes to restate key character facts
- Reference established lorebook entries naturally in conversation
- If the model drifts, use OOC to correct and regenerate

## 10.3 Managing Large Worlds

### The World-Building Token Problem

Large worlds have more information than can fit in context. The solution is layered information architecture:

```
ALWAYS PRESENT (Character Card):
  ├─ Character's personal world view
  ├─ Key relationships
  └─ Immediate context

TRIGGERED (Character Lorebook):
  ├─ Character's knowledge of the world
  ├─ Personal history details
  └─ Relationship deep-dives

TRIGGERED (Global Lorebook):
  ├─ World rules and systems
  ├─ Location descriptions
  ├─ Historical events
  └─ Cultural context

NEVER IN CONTEXT (Repository Only):
  ├─ Author notes and development history
  ├─ Contradicted/rejected lore
  └─ Meta-information about the project
```

### Best Practices

- **Build the world from the character's perspective.** The lorebook should contain what the CHARACTER knows, not an objective wiki. This keeps entries relevant and character-consistent. (Consensus: Community guides)
- **Use recursive lorebook design.** Entry about a city mentions the faction that controls it, which triggers the faction entry, which mentions the leader, etc. This creates emergent world-building. (Consensus: SillyTavern recursive scanning)
- **Separate world facts from character interpretation.** "The Douglas Trading House was founded in 1666" is a fact. "Wulfnic believes the Trading House is his family's greatest achievement" is character perspective. Both are needed but serve different purposes.

## 10.4 Managing Recurring Characters

### Best Practices

- **Each recurring character needs their own card.** Shared lorebook entries can reference them, but each character's unique perspective needs its own definition. (Consensus: Community practice)
- **Cross-reference in lorebooks.** Character A's lorebook should have entries about Character B, and vice versa. This creates relationship awareness. (Consensus: Community guides)
- **Use group chat features** (SillyTavern) for multi-character scenes. Ensure each character's card is distinct enough that the model can differentiate them. (Consensus: SillyTavern docs)

---

# 11. ROLEPLAY QUALITY FRAMEWORK

## 11.1 Character Quality

| Level | Description |
|-------|-------------|
| **Poor** | Generic traits, no behavioral specificity, no flaws, no motivation. Could be anyone. |
| **Average** | Some distinct traits, basic backstory, but flat. Functional but forgettable. |
| **Good** | Specific behavioral patterns, clear motivation, at least one meaningful flaw, distinct voice. |
| **Excellent** | Multi-layered personality with contradictions, every trait connects to behavior, voice is unmistakable, creates emergent roleplay through character-driven choices. |

## 11.2 Lorebook Quality

| Level | Description |
|-------|-------------|
| **Poor** | Missing, or entries repeat card content, keywords overlap, no organization. |
| **Average** | Present but disorganized, some useful entries mixed with filler, keyword strategy inconsistent. |
| **Good** | Well-structured entries, non-overlapping keywords, entries add depth not in card, token budget respected. |
| **Excellent** | Recursive entry design, layered information architecture, canon-layer tagged, optimized token budget, entries interlink to create emergent world-building. |

## 11.3 Prompt Quality

| Level | Description |
|-------|-------------|
| **Poor** | Vague instructions, negative framing only, no behavioral anchors, contradictory. |
| **Average** | Correct structure but generic content, some positive framing, basic instructions. |
| **Good** | Clear behavioral instructions, positive framing, specific formatting rules, hierarchical structure. |
| **Excellent** | Surgically precise, every token earns its place, instruction hierarchy optimized, anti-drift measures in place, platform-specific features leveraged. |

## 11.4 Scenario Quality

| Level | Description |
|-------|-------------|
| **Poor** | No framing, no hook, no reason for the interaction. |
| **Average** | Basic setting description, minimal context, functional but uninspiring. |
| **Good** | Clear dramatic context, narrative hook, user agency preserved, stakes established. |
| **Excellent** | Rich narrative context with immediate dramatic potential, opening message establishes tone/dynamic/hook simultaneously, multiple implied directions for the RP to evolve. |

## 11.5 Overall Bot Quality Matrix

| Component | Weight | Poor (1) | Average (2) | Good (3) | Excellent (4) |
|-----------|--------|----------|-------------|----------|---------------|
| Character Design | 35% | Generic | Flat | Specific | Layered |
| Lorebook Design | 25% | Missing | Disorganized | Structured | Recursive |
| Prompt Engineering | 20% | Vague | Generic | Clear | Surgical |
| Scenario Design | 20% | None | Basic | Engaging | Immersive |

**Quality Score = (Character × 0.35) + (Lorebook × 0.25) + (Prompt × 0.20) + (Scenario × 0.20)**

| Score Range | Tier |
|-------------|------|
| 1.0 - 1.5 | Poor |
| 1.5 - 2.5 | Average |
| 2.5 - 3.5 | Good |
| 3.5 - 4.0 | Excellent |

---

# 12. SVARTÚLFRVERSE RECOMMENDATIONS

## 12.1 Mandatory Practices

The following are NON-NEGOTIABLE for all SvartúlfrVerse bot and lorebook exports, derived from project governance (R-008, R-009, ADR-006):

1. **Canon-derived content ONLY.** Every piece of text in a bot export must trace to a database/ record. No manual lore injection. (R-008-BOT-001)
2. **Provenance metadata required.** Every export must include `extensions.svartulfrverse` with canon_id, canon_layer, and provenance array. (R-008, EXPORT_MAPPING_MATRIX)
3. **Canon layer compliance.** Active content only in Active-layer exports. Historical content tagged as Historical. Cultural content clearly marked as non-factual. (ADR-006)
4. **No rejected canon.** Valeria/WetNurse, Miss Twin Peaks, KSA origin, supernatural systems — ABSENT from all exports. (ADR-006, R-006-GOV-013)
5. **Authority boundary respect.** Genealogy from Family Authority only. Visual from Visual Authority. No cross-contamination. (ADR-000 through ADR-005)
6. **Layer separation in lorebooks.** Lorebook entries tagged with canon layer. Deferred and Candidate content NOT included in exports. (ADR-006, R-009)

## 12.2 Recommended Practices

1. **Use the Generic JSON format as canonical source**, then transform to JanitorAI/SillyTavern formats. This ensures consistency across platforms. (EXPORT_MAPPING_MATRIX)
2. **Design lorebooks with SvartúlfrVerse canon layers** as entry tags: `active`, `historical`, `cultural`. Use recursive entries for dynasty/family relationships. (BOT_SEARCH_SPECIFICATION)
3. **Character cards should reference but not define genealogy.** Point to Family Authority records. Let the family_engine handle relationship queries. (R-002-FAM-001, R-003-CHR-007)
4. **Visual descriptions follow the Visual Fusion Model.** Morphology from one parent, color blend from both. Document visual_classification in the card. (R-004, W_Visual_Inheritance)
5. **Use the Quality Framework (Section 11) as a pre-export checklist.** Score each component. Target 3.0+ (Good) minimum for any export.
6. **Test exports on both JanitorAI and SillyTavern** even if targeting one platform. Cross-platform testing reveals portability issues.

## 12.3 Practices To Avoid

1. **Do NOT put genealogy in character files.** Even if it seems convenient. Genealogy belongs in Family Authority records. (R-003-CHR-007)
2. **Do NOT mix canon layers in a single lorebook entry.** Each entry should have one clear layer classification. (ADR-006)
3. **Do NOT use supernatural elements in Active-layer content.** Lycanthropy, immortality, pack hierarchy — these are Cultural Canon only. (ADR-006, R-006-GOV-013)
4. **Do NOT create lorebook entries without source attribution.** Every entry needs a `source_id` linking to the database record. (R-009, BOT_SEARCH_SPECIFICATION)
5. **Do NOT export characters with MISSING EVIDENCE.** If a required field has no evidence in the repository or authorized sources, STOP. Do not infer or generate. (Missing Evidence Rule, project_memory)
6. **Do NOT use JanitorAI scripts as a substitute for good card design.** Scripts enhance; they don't fix fundamental character design problems. (Scripts Beta documentation)

## 12.4 Recommended Standards

### Bot Exports

| Standard | Requirement | Authority |
|----------|------------|-----------|
| Character card token budget | 500-1300 tokens permanent | Community best practices |
| Lorebook token budget | 500-1000 tokens triggered | SillyTavern docs |
| Example dialogues | 3-5 exchanges, 100-300 tokens | Community consensus |
| Provenance metadata | Required in extensions | R-008, EXPORT_MAPPING_MATRIX |
| Canon layer tagging | Required per entry | ADR-006, R-009 |
| Validation status | Required pre-export | VALIDATION_CHECKLIST |

### Lorebook Exports

| Standard | Requirement | Authority |
|----------|------------|-----------|
| Entry token size | 40-120 tokens per entry | SillyTavern docs + community testing |
| Keyword strategy | 3-5 specific keywords per entry | Community best practices |
| Canon layer metadata | Required per entry | ADR-006, R-009 |
| Source attribution | Required per entry | R-009, BOT_SEARCH_SPECIFICATION |
| Recursive scanning | Enabled for world-building entries | SillyTavern docs |
| Priority assignment | Based on importance tier | DeepLore Enhanced guidelines |

### Character Design

| Standard | Requirement | Authority |
|----------|------------|-----------|
| Core traits | 5-7 specific, behavioral | Community consensus |
| Motivations | Primary + secondary + hidden | Narrative design principles |
| Flaws | At least 1 that creates friction | Community consensus |
| Speech patterns | 2-3 specific habits | Community consensus |
| Example dialogues | 3-5 exchanges showing range | Community consensus |

### Prompt Design

| Standard | Requirement | Authority |
|----------|------------|-----------|
| System prompt | Behavioral rules only, not character description | OpenAI Guide + community practice |
| Positive framing | "Does this" not "doesn't do that" | Community consensus |
| Instruction hierarchy | Most critical at beginning AND end | OpenAI Guide |
| Post-history | 2-3 hard constraints only | Community practice |
| Author's notes | Under 100 tokens, scene context | SillyTavern docs |

---

# APPENDIX A: SOURCES ANALYZED

## Official Documentation
1. **JanitorAI Official Help Center** — `help.janitorai.com` — Bot creation guides, scripts documentation, creator resources
2. **SillyTavern Official Documentation** — `docs.sillytavern.app` — World Info/Lorebook system, character cards, prompt management
3. **Character Card Specification V3** — `github.com/kwaroran/character-card-spec-v3` — Formal spec for CCv3 format
4. **Character Card Specification V2** — `github.com/malfoyslastname/character-card-spec-v2` — Formal spec for CCv2 format
5. **OpenAI Prompt Engineering Guide** — `platform.openai.com/docs/guides/prompt-engineering` — Foundational prompting principles

## Community Guides
6. **Faylua's Bot Creation Guide** (JanitorAI) — Step-by-step with images, token economy explanation
7. **Aurellea's Bot Creation Guide** (JanitorAI) — Comprehensive walkthrough with examples
8. **Iorveth's Bot Creation Guide** — Advanced character design principles
9. **Icehellionx's Script Collection** (JanitorAI) — Emotion Engine, Dynamic Lorebook, Scene Orchestrator, and more
10. **Reddit r/JanitorAI_Official** — Lorebook best practices discussion, OOC templates, community consensus

## Project Internal Documents
11. **BOT_EXPORT_SPECIFICATION.md** — Export schemas for JanitorAI, SillyTavern, Generic JSON
12. **BOT_SEARCH_SPECIFICATION.md** — Lorebook architecture, engine design, validation pipeline
13. **EXPORT_MAPPING_MATRIX.md** — Field mapping between repository and export formats
14. **ENGINE_SPECIFICATION.md** — Engine architecture and contracts
15. **PROMPT_DESIGN_GUIDE.md** — Project prompt writing standards
16. **VALIDATION_CHECKLIST.md** — 47-check validation guide
17. **R-008_Bot_Rules.md** — Bot export governance
18. **R-009_Lorebook_Rules.md** — Lorebook governance
19. **ADR-006** — Canon Layer Architecture

## External Tools Referenced
20. **DeepLore Enhanced** (SillyTavern extension) — Advanced lorebook management with priority guidelines
21. **Character Foundry Normalizer** — V2↔V3 conversion with loss detection
22. **HoneyChat Character Cards Guide 2026** — V2 vs V3 comparison and analysis

---

# APPENDIX B: MAJOR THEMES DISCOVERED

## Theme 1: The Token Economy is Universal
Every source, regardless of platform, emphasizes that tokens are a finite resource that must be managed. The specific numbers vary (8K vs 32K vs 128K context), but the principle is constant: **every token must earn its place.**

## Theme 2: Behavioral Anchors Beat Trait Labels
The single most consistent finding across all sources. "Is kind" is weak. "Remembers small details about people and brings them up later" is strong. The model needs observable behaviors, not abstract labels.

## Theme 3: Lorebooks Are RAG Systems
Every technical source describes lorebooks as retrieval-augmented generation. This means they should contain COMPLEMENTARY information, not duplicate the card. The card anchors; the lorebook deepens.

## Theme 4: Example Dialogue Is the Strongest Tool
Across all guides, example dialogue is cited as the most effective way to establish voice, prevent drift, and teach the model the character's patterns. It's more powerful than any description.

## Theme 5: Consistency Requires Active Prevention
Drift is not a bug; it's a feature of how LLMs work. Every source agrees that preventing drift requires specific techniques: behavioral anchors, example dialogues, post-history instructions, and lorebook reinforcement. You can't just define a character and hope for the best.

## Theme 6: Platform Differences Are Real But Principles Are Universal
JanitorAI and SillyTavern have different technical implementations, but the underlying principles of good character design, lorebook architecture, and prompt engineering are identical. A well-designed character works on both platforms.

## Theme 7: The Community Has Converged on Best Practices
Despite dozens of independent guides written by different authors at different times, the core recommendations are remarkably consistent. The principles in this document represent genuine consensus, not individual opinion.

---

# APPENDIX C: RECOMMENDATIONS FOR FUTURE EXPANSION

1. **Model-Specific Tuning Guides.** As new LLMs are released, document their specific strengths/weaknesses for roleplay. What works for Claude may not work for DeepSeek.
2. **Automated Quality Scoring.** Implement the Quality Framework (Section 11) as part of the validation pipeline. Score exports before release.
3. **Lorebook Testing Suite.** Create a set of test conversations designed to verify that lorebook entries activate correctly and don't conflict.
4. **Multi-Character Scene Design.** Expand the framework for group chats and multi-character scenarios.
5. **Localization Best Practices.** As the project expands, document principles for multilingual bot exports.
6. **Version Tracking.** As community best practices evolve, version this document and track changes against new sources.

---

# APPENDIX D: EXTERNAL RESOURCE LINKS

## 🤖 AI & LLM

| # | URL | Category | Description |
|---|-----|----------|-------------|
| 1 | `https://docs.google.com/document/d/e/2PACX-1vQggoBXOep1Twy3izYOAH2-fG2qALEGYT1CT3tyROEeHcWhmnabludnGYMwuQg4yKiNTp5PBzP5xLg8/pub` | AI & LLM | Google Docs AI models comparison resource |
| 2 | `https://rentry.org/ai-models#deepseek-on-chutes-free-provider` | AI & LLM | AI models directory with Deepseek on Chutes free provider |
| 3 | `https://docs.google.com/document/u/0/d/16scfv4rjV3kgPGkGOGo4fRDC8sxiPrgHTE1WFJQLlFk/mobilebasic` | AI & LLM | AI models and providers guide (Google Docs) |
| 4 | `https://perchance.org/ai-character-generator` | Character Creation | Perchance AI character generator tool |
| 5 | `https://rentry.co/BDSM_Prompts#switch` | Prompt Engineering | BDSM prompts collection with switch dynamics |
| 6 | `https://jaitutorial.uwu.ai/#` | JanitorAI | JanitorAI tutorial resource |
| 7 | `https://rentry.org/absolutetrashs-bot-guide` | Character Creation | Community bot creation guide (Rentry) |
| 8 | `https://rentry.co/jaibotmakingresources` | Character Creation | JanitorAI bot making resources collection |
| 9 | `https://aistudio.google.com/apps` | AI Platforms | Google AI Studio apps |
| 10 | `https://cheesey-wizards-organization.gitbook.io/masterlist` | Character Creation | Masterlist of AI character resources (GitBook) |
| 11 | `https://civitai.com/` | Image Generation | CivitAI model repository (generic) |
| 12 | `https://rentry.co/cryptidsprompts2` | Prompt Engineering | Cryptids prompts collection |
| 13 | `https://rentry.co/pddvz4oo` | Prompt Engineering | Prompt design resource |
| 14 | `https://emochi.com/` | JanitorAI | Emochi AI character platform |
| 15 | `https://huggingface.co/` | AI Platforms | HuggingFace model repository |
| 16 | `https://civitai.com/models/795765/illustrious-xl?modelVersionId=889818` | Image Generation | Illustrious XL model on CivitAI |
| 17 | `https://tensor.art/` | Image Generation | TensorArt AI image generation |
| 18 | `https://wikia.schneedc.com/bot-creation/trappu/introduction` | Character Creation | Trappu's bot creation introduction |
| 19 | `https://rentry.co/iorveths-bot-creation-guide` | Character Creation | Iorveth's comprehensive bot creation guide |
| 20 | `https://janitorai.com/` | JanitorAI | JanitorAI platform homepage |
| 21 | `https://rentry.co/botmaking` | Character Creation | Community botmaking guide collection |
| 22 | `https://rentry.co/MarPrompt` | Prompt Engineering | MarPrompt collection |
| 23 | `https://www.reddit.com/r/JanitorAI_Official/comments/1kvh4pz/my_goto_ooc_templates_for_scene_control_plot/` | Prompt Engineering | OOC templates for scene control and plot |
| 24 | `https://cheesey-wizards-organization.gitbook.io/masterlist/prompts-and-troubleshooting/my-prompt` | Prompt Engineering | Personal prompt resources and troubleshooting |
| 25 | `https://notebooklm.google.com/notebook/86c599db-3e72-4d2f-8776-044d0d372a21` | Utility Tools | Google NotebookLM notebook |
| 26 | `https://openrouter.ai/` | AI Platforms | OpenRouter AI model gateway |
| 27 | `https://docs.google.com/document/u/0/d/1xfJOM3KnxKqQLD_I29nXGj2u-gz_RAs8ojqtXy3sSQE/mobilebasic?pli=1` | AI & LLM | AI workflow document (Google Docs) |
| 28 | `https://pixai.art/en` | Image Generation | PixAI image generation platform |
| 29 | `https://railway.com/?referralCode=fireship` | Utility Tools | Railway hosting platform |
| 30 | `https://sophiasunblocker.onrender.com/` | Utility Tools | Web proxy/unblocker tool |
| 31 | `https://rentry.co/statuotwtips#the-additions` | Prompt Engineering | Status tips and additions for bot creation |
| 32 | `https://rentry.co/statuobotmakie` | Character Creation | Bot making tips and resources |
| 33 | `https://aistudio.google.com/apps/665584a6-1a8c-4ceb-a224-025eee8dd6bb?showPreview=true&showAssistant=true` | AI Platforms | Google AI Studio specific app |
| 34 | `https://tiktokenizer.vercel.app/` | Utility Tools | OpenAI tokenizer visualization tool |
| 35 | `https://peipei1998.gitbook.io/peipei1998s-universal-prompt/` | Prompt Engineering | Universal prompt design guide (GitBook) |
| 36 | `https://sopakcosauce.gitbook.io/sopakcosauce-docs` | Character Creation | Bot creation documentation (GitBook) |
| 37 | `https://drive.google.com/file/d/1V-lFxmlsYMSmt4CZI2SA_xzWRxoXzC11/view?pli=1` | Character Creation | Bot creation resource (Google Drive) |
| 38 | `https://drive.google.com/file/d/1kMce-Jx3zFBSq-EKjSwqBqRw6boRioNZ/view` | Character Creation | Bot creation resource (Google Drive) |
| 39 | `https://www.reddit.com/r/JanitorAI_Official/comments/1lykj9v/explaining_lorebooks_take_2_better_resolution/` | Lorebook Design | Lorebook best practices (Reddit) |
| 40 | `https://help.janitorai.com/en/category/scripts-1qzakwc/` | JanitorAI | JanitorAI official scripts documentation |

---

*This document synthesizes principles from 20+ sources. All recommendations represent cross-referenced consensus, not single-source claims. Practices marked as "Consensus" appear in 3 or more independent sources. Practices marked with specific source names are attributed to that source.*

*Derived from project governance: ADR-000 through ADR-006, R-000 through R-009, BOT_EXPORT_SPECIFICATION, BOT_SEARCH_SPECIFICATION, EXPORT_MAPPING_MATRIX, ENGINE_SPECIFICATION, VALIDATION_CHECKLIST.*
