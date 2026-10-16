# LOREBOOK KNOWLEDGE GUIDE

**Version:** 1.0
**Date:** 2026-06-08
**Purpose:** Operational guide to lorebook design, creation, and optimization. Companion to LOREBOOK_SPECIFICATION.md and BOT_SEARCH_SPECIFICATION.md — explains lorebook architecture, trigger design, keyword strategy, token optimization, and canon-layer management.

---

## 1. WHAT A LOREBOOK ACTUALLY IS

A lorebook is a **dynamic knowledge injection system.** Think of it as a smart dictionary that only looks up definitions when the conversation makes them relevant.

**How it works:**
1. The user sends a message
2. The platform scans the message (and recent history) for keywords
3. When a keyword matches a lorebook entry, that entry's content is injected into the prompt
4. The AI sees the injected context and uses it to inform its response
5. When the keyword stops appearing, the entry drops out of context

**What this means practically:**
- Lorebook entries are NOT always in context (unlike character card fields)
- Lorebook entries activate and deactivate based on conversation content
- The same lorebook can produce different context injections in different conversations

---

## 2. LOREBOOK ARCHITECTURE

### 2.1 The Three-Layer Model

**Layer 1: Character Card (Permanent Context)**
Always present. Contains the essential character definition.
- Name, appearance, core personality
- Speech patterns, behavioral anchors
- Motivations, key relationships
- Scenario/opening context

**Layer 2: Character Lorebook (Triggered Context)**
Activates when conversation touches on specific topics.
- Extended backstory details
- Per-relationship deep dives
- Personal history milestones
- Psychological deep-dives
- Specific knowledge areas

**Layer 3: World Lorebook (Triggered Context)**
Activates when conversation touches on world elements.
- Setting details, locations
- Institutions, organizations
- Cultural/social rules
- Historical events

### 2.2 Why Three Layers?

**Token economy.** A character card might be 800 tokens. A full lorebook might be 5000 tokens. But only 500-1000 tokens of lorebook are active at any time. This gives you 5000 tokens of depth while only consuming 500-1000 at once.

**Relevance filtering.** The AI only sees lorebook entries that are relevant to the current conversation. This prevents information overload and keeps the context focused.

**Scalability.** You can build massive world lorebooks without worrying about context window limits, because only a fraction activates at any time.

---

## 3. TRIGGER DESIGN

### 3.1 How Triggers Work

From SillyTavern documentation and community testing:

```
User Message: "I walked into the old library where Wulfnic used to study as a boy"

Engine scans for keywords:
  → "library" matches Entry #47 (Location: Douglas Library)
  → "Wulfnic" matches Entry #12 (Character: Wulfnic — Early Life)
  → "study" matches Entry #12 (secondary keyword)
  → "boy" matches Entry #12 (secondary keyword)

Entries #47 and #12 activate.
Sorted by priority. Inserted until token budget exhausted.
```

### 3.2 Trigger Strategies

**Strategy 1: Narrative Keywords**
Use words that naturally arise when the topic comes up.
- Backstory entry: triggers on "remember", "before", "used to", "childhood"
- Relationship entry: triggers on the person's name + emotional context words
- Location entry: triggers on the location name + action words

**Strategy 2: Emotional Triggers**
Entries that activate on emotional states.
- Character's grief response: triggers on "death", "loss", "miss"
- Character's anger response: triggers on "betrayal", "lie", "broken promise"
- Character's joy response: triggers on "success", "achievement", "proud"

**Strategy 3: Event-Chain (Recursive)**
Entries that trigger other entries through cross-references.
- Entry about a city mentions the faction that controls it
- Entry about a faction mentions its leader
- Entry about the leader mentions their family
- One trigger cascades into a web of relevant context

**Strategy 4: Constant + Keyword Hybrid**
- Constant entries (always on) for critical world rules
- Keyword entries for specific details
- This ensures foundational context is always present while specific details activate as needed

### 3.3 Trigger Design Best Practices

1. **Use specific, contextual keywords.** "Douglas Trading House" is better than "trade" or "house" alone.
2. **Include synonyms and variants.** People refer to the same thing different ways. "Wulfnic", "patriarch", "family head" should all trigger the same entry.
3. **Test your keywords.** If entries never fire, broaden. If they fire constantly, narrow.
4. **Use selective mode for conditional entries.** If an entry should only fire when TWO concepts are present (e.g., "mother" AND "death"), use primary + secondary keywords with selective mode.
5. **Avoid common words as standalone keywords.** "Go", "the", "is" will fire constantly. Always pair with context or use whole-word matching.

---

## 4. KEYWORD DESIGN

### 4.1 Keyword Types

| Type | Example | Use When |
|------|---------|---------|
| Proper noun | "Wulfnic", "Douglas" | Character/location names |
| Specific noun | "trading house", "patriarch" | Concepts unique to your world |
| Emotional word | "grief", "anger", "love" | Mood-triggered entries |
| Action word | "study", "travel", "fight" | Activity-triggered entries |
| Temporal word | "childhood", "before", "years ago" | Backstory-triggered entries |
| Relationship word | "father", "rival", "ally" | Relationship-triggered entries |

### 4.2 Keyword Budget Per Entry

**3-5 keywords per entry is the sweet spot.**

- **Too few (1-2):** Entry rarely activates. Misses relevant conversations.
- **Too many (8+):** Entry activates too often. Wastes token budget. Competes with other entries.
- **Just right (3-5):** Entry activates when relevant, stays quiet when not.

### 4.3 Keyword Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Single common word | Fires constantly | Make specific: "Douglas Trading House" |
| Only proper nouns | Misses casual references | Add synonyms |
| Too many keywords | Fires too frequently | Pick 3-5 essential |
| Overlapping with other entries | Competes for budget | Differentiate trigger domains |
| Case sensitivity issues | Misses matches | Use case-insensitive matching |

---

## 5. TOKEN OPTIMIZATION

### 5.1 The Math

```
Total Context Window:     8192 tokens (example)
System prompt:            -200 tokens
Character card:           -800 tokens
Active lorebook entries:  -500 tokens (budget)
─────────────────────────────────
Available for conversation: 6692 tokens
```

Every lorebook entry that activates reduces available conversation space. This is why entry conciseness matters.

### 5.2 Entry Size Guidelines

| Entry Type | Recommended Size | Notes |
|-----------|-----------------|-------|
| Character fact | 30-80 tokens | One key fact, stated concisely |
| Relationship detail | 50-100 tokens | Who + dynamic + key history |
| Location description | 40-80 tokens | Sensory detail + narrative relevance |
| World rule | 30-60 tokens | One rule, explained through example |
| Backstory event | 50-100 tokens | One event + its impact on character |
| Personality deep-dive | 80-150 tokens | How a trait manifests, with examples |

**The SillyTavern documentation recommends ~50 tokens per entry as a general guideline.**

### 5.3 Token Budget Management

Most platforms have a configurable lorebook token budget (SillyTavern default is often 500-1000 tokens). When the budget is full:

- **Constant entries are inserted first** (they always consume budget)
- **Higher priority entries are inserted next** (lower insertion_order number = higher priority)
- **Remaining entries compete for leftover budget**
- **Entries that don't fit are silently dropped**

**This means priority assignment is critical.** Your most important entries should have the highest priority (lowest insertion_order number).

### 5.4 Priority Tiers (From Community Best Practices)

| Priority | Use For | Examples |
|----------|---------|---------|
| 10-20 | Critical context | Main character facts, essential world rules |
| 30-40 | Core lore | Key NPCs, important locations |
| 50 | Standard entries | Most lorebook entries |
| 60-70 | Background flavor | Minor details, atmosphere |
| 80-100 | Rare/obscure | Trivia, deep-cut references |

---

## 6. SOURCE ATTRIBUTION

### 6.1 Why Attribution Matters

Every lorebook entry must trace to a canonical source. This is not optional — it's a governance requirement (R-009).

**Without attribution:**
- You can't verify if the entry is canon-compliant
- You can't update the entry when the source changes
- You can't audit the lorebook against the repository

### 6.2 Attribution Format

Each lorebook entry should include:

```yaml
source_id: "C_Wulfnc"           # Canonical record ID
source_file: "database/characters/C_Wulfnic_Bloodmoon.md"
canon_layer: "active"           # active/historical/cultural
authority: "Character"          # Character/Family/Visual/Experience
last_synced: "2026-06-08T00:00:00Z"
```

### 6.3 Canon Layer Tagging

For SvartúlfrVerse lorebooks, every entry must be tagged with exactly one canon layer:

| Layer | Tag | Handling |
|-------|-----|----------|
| Active | `active` | Always included in runtime lorebooks |
| Historical | `historical` | Included with historical tag; may include period context |
| Cultural | `cultural` | Included with cultural disclaimer; marked as non-factual |
| Deferred | `deferred` | NOT included in runtime lorebooks |
| Candidate | `candidate` | NOT included until promoted |

---

## 7. BEST PRACTICES

### Design
1. **Each entry should be standalone.** The AI must understand it without other entries active.
2. **Entries should ADD information, not repeat the card.** If it's in the card, it doesn't need to be in the lorebook.
3. **Use recursive cross-references** to build world cohesion. Entry A mentions concept B, which triggers Entry B.
4. **Group related entries** in the same lorebook file. Character entries together, world entries together.
5. **Keep entries concise.** Every token competes with every other active entry.

### Keywords
1. **3-5 specific keywords per entry.** Not too few, not too many.
2. **Include synonyms and variants.** People refer to things different ways.
3. **Use selective mode for conditional triggers.** When two concepts must both be present.
4. **Test keywords in conversation.** Verify they fire when expected and stay quiet when not.

### Token Economy
1. **Target 50 tokens per entry** as a general guideline.
2. **Assign priority based on importance.** Critical entries get priority 10-20.
3. **Monitor your token budget.** If entries are being dropped, either reduce entry sizes or increase the budget.
4. **Constant entries consume budget first.** Use sparingly.

### Canon Compliance
1. **Every entry traces to a source.** No unsourced content.
2. **Canon layer tagging is mandatory.** One layer per entry.
3. **Cultural content gets a disclaimer.** "According to family tradition..." or "Legend holds that..."
4. **Deferred/Candidate content is excluded** from runtime lorebooks.

---

## 8. ANTI-PATTERNS

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Lorebook repeats card content | Wastes tokens with no new information | Ensure entries add information not in card |
| Entries too long (200+ tokens) | Consumes budget rapidly | Break into smaller, focused entries |
| Keywords too broad | Entries trigger constantly | Make keywords specific and contextual |
| Keywords too narrow | Entries almost never activate | Include common synonyms |
| No recursive scanning | Entries feel isolated | Use cross-references between entries |
| No priority assignment | Important entries may be dropped | Assign priority based on importance |
| No source attribution | Can't verify canon compliance | Add source_id to every entry |
| Mixing canon layers in one entry | Violates ADR-006 | One layer per entry |
| Circular references | Infinite injection loops | Set recursion limits; avoid A→B→A chains |

---

## 9. OPTIMIZATION GUIDELINES

### For New Lorebooks
1. Start with character core entries (identity, key relationships)
2. Add world context entries (locations, institutions)
3. Add backstory entries (personal history, formative events)
4. Add flavor entries (atmosphere, minor details)
5. Test with real conversations and adjust keywords

### For Existing Lorebooks
1. Audit for entries that never fire → broaden keywords or remove
2. Audit for entries that always fire → narrow keywords or make constant
3. Audit for entries that exceed token budget → split or shorten
4. Audit for canon compliance → verify source attribution
5. Audit for layer correctness → verify canon layer tags

### For SvartúlfrVerse Specifically
1. Use the canon layer taxonomy (active/historical/cultural/deferred/candidate)
2. Tag dynasty relationships in family lorebook entries
3. Use the Visual Fusion Model for visual inheritance entries
4. Separate Douglas and Bloodmoon cultural entries
5. Include provenance metadata in every entry

---

## 📚 Cross-References

- **For comprehensive lorebook best practices, community consensus, and detailed examples:** See [JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md §5 (Lorebook Design)](../Guidelines/JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md)
- **For formal specification:** See [LOREBOOK_SPECIFICATION.md](file:///d:/SvartulfrVerse/core/LOREBOOK_SPECIFICATION.md) and [BOT_SEARCH_SPECIFICATION.md](../Guidelines/BOT_SEARCH_SPECIFICATION.md)
- **For validation of lorebook entries:** See [VALIDATION_KNOWLEDGE_GUIDE.md](../Guidelines/VALIDATION_KNOWLEDGE_GUIDE.md)
- **For implementation patterns:** See [IMPLEMENTATION_PATTERNS.md §1 (Pattern 3: Three-Layer Architecture)](../Guidelines/IMPLEMENTATION_PATTERNS.md)

---

*This guide is derived from LOREBOOK_SPECIFICATION.md, BOT_SEARCH_SPECIFICATION.md, and SillyTavern World Info documentation. For formal specifications, consult the source documents directly.*
