# BOT SEARCH KNOWLEDGE GUIDE

**Version:** 1.0
**Date:** 2026-06-08
**Purpose:** Operational guide to bot discovery, indexing, and metadata strategy. Companion to BOT_SEARCH_SPECIFICATION.md — explains how bots are found, categorized, and made discoverable.

---

## 1. WHY BOT SEARCH MATTERS

In the SvartúlfrVerse context, "search" has two meanings:

1. **External search:** How users find your bots on platforms (JanitorAI, SillyTavern, CHUB)
2. **Internal search:** How the engine finds and retrieves canonical data for export

Both require deliberate metadata strategy. A bot that can't be found is a bot that doesn't exist. A bot without proper metadata is a bot that attracts the wrong audience or sets wrong expectations.

---

## 2. METADATA STRATEGY

### 2.1 Tag Architecture

Tags serve as the primary discovery mechanism. SvartúlfrVerse uses a structured tag taxonomy:

**Canon Layer Tags (Required):**
| Tag | Meaning |
|-----|---------|
| `active-canon` | Current timeline, factual content |
| `historical-canon` | Past timeline, factual content |
| `cultural-canon` | Mythological/traditional content, non-factual |

**Dynasty Tags (Required for dynasty members):**
| Tag | Meaning |
|-----|---------|
| `douglas` | Member of the Douglas dynasty |
| `bloodmoon` | Member of the Bloodmoon dynasty |
| `douglas-bloodmoon` | Member of the unified dynasty |

**Character Type Tags:**
| Tag | Usage |
|-----|-------|
| `patriarch` / `matriarch` | Family head |
| `heir` | Designated successor |
| `founder` | Dynasty originator |
| `outsider` | Non-dynasty character |

**Content Tags (for platform search):**
| Tag | Usage |
|-----|-------|
| `male` / `female` / `non-binary` | Gender |
| `adult` | Age classification |
| `contemporary` | Setting period |
| `family-drama` | Content theme |
| `business` | Content theme |
| `slice-of-life` | Content theme |

**Project Tag (Required):**
| Tag | Usage |
|-----|-------|
| `svartulfrverse` | Identifies the bot as part of the SvartúlfrVerse project |

### 2.2 Tagging Best Practices

- **Always include `svartulfrverse`** — This is the project identifier
- **Always include exactly one canon layer tag** — Prevents layer confusion
- **Include dynasty tags for all dynasty members** — Enables family-based discovery
- **Use content tags that accurately reflect the character** — Misleading tags attract wrong users and generate bad experiences
- **Don't over-tag** — 5-8 relevant tags beat 20 vague ones

### 2.3 Tagging Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| No canon layer tag | Users can't gauge content type | Always include one |
| Multiple canon layer tags | Confuses the classification | Exactly one |
| Trending tags unrelated to character | Attracts wrong audience, bad experience | Use accurate tags only |
| Missing `svartulfrverse` tag | Can't identify project bots | Always include |
| Dynasty tag for non-dynasty characters | Misrepresents canon | Only for actual members |

---

## 3. BOT DISCOVERY ON PLATFORMS

### 3.1 JanitorAI Discovery

**Primary discovery mechanisms:**
- **Search bar** — Matches against character name, tags, and description text
- **Tag browsing** — Users filter by tags
- **Featured/Recommended** — Algorithmic promotion based on engagement
- **Creator pages** — All bots from a creator grouped together

**Optimization for JanitorAI:**
- Character name should be searchable (include full name and common aliases)
- Description/bio should include key searchable terms naturally
- Tags should match what users actually search for
- First message quality affects engagement, which affects algorithmic promotion

### 3.2 SillyTavern Discovery

**Primary discovery mechanisms:**
- **CHUB (Character Hub)** — `chub.ai` / `characterhub.org` — The main repository for SillyTavern character cards
- **Direct import** — Users import PNG/JSON files directly
- **Community sharing** — Discord, Reddit, forums

**Optimization for SillyTavern/CHUB:**
- Character card metadata (name, description, tags) is embedded in the PNG
- CHUB uses tags and descriptions for search
- High-quality character cards with proper metadata get more downloads
- The `creator` field should identify the project

### 3.3 CHUB (Character Hub) Strategy

CHUB is the de facto character card repository. Key metadata fields:

| CHUB Field | Purpose | Recommended Value |
|-----------|---------|------------------|
| Name | Character identity | Full canonical name |
| Description | Search and preview | 2-3 sentence summary |
| Tags | Discovery | SvartulfrVerse taxonomy |
| Creator | Attribution | Project identifier |
| Character version | Version tracking | Match canon version |
| Category | Browsing | Match content type |

---

## 4. INDEXING STRATEGY

### 4.1 Internal Indexing (Repository)

Within the SvartúlfrVerse repository, characters are indexed by:

1. **Canonical ID** — `C_[Name]` format (e.g., `C_Wulfnic`)
2. **File path** — `database/characters/C_[Name].md`
3. **Dynasty membership** — Cross-reference in family records
4. **Canon layer** — Active, Historical, or Cultural

### 4.2 External Indexing (Platform)

On external platforms, characters are indexed by:

1. **Name** — Full name + aliases
2. **Tags** — Structured taxonomy
3. **Description** — Searchable text
4. **Creator** — Project attribution

### 4.3 Cross-Platform Consistency

The same character should be discoverable across platforms with consistent metadata:

```
Repository:     C_Wulfnic → database/characters/C_Wulfnic_Bloodmoon.md
JanitorAI:      "Wulfnic Bloodmoon" → tags: [svartulfrverse, douglas-bloodmoon, patriarch, active-canon]
SillyTavern:    "Wulfnic Bloodmoon" → tags: ["SvartulfrVerse", "Douglas-Bloodmoon", "patriarch", "active-canon"]
CHUB:           "Wulfnic Bloodmoon" → tags: ["svartulfrverse", "douglas-bloodmoon", "male", "adult", "contemporary"]
```

---

## 5. CATEGORIZATION

### 5.1 By Canon Layer

| Layer | Content Type | Export Handling |
|-------|-------------|-----------------|
| Active | Current timeline, factual | Full export with all fields |
| Historical | Past timeline, factual | Export with `historical` tag, may include period-specific context |
| Cultural | Mythological, traditional | Export with `cultural` tag + non-factual disclaimer |

### 5.2 By Dynasty

| Dynasty | Characters | Notes |
|---------|-----------|-------|
| Douglas | Erik, Logan, Edric | Material/commerce lineage |
| Bloodmoon | Nixara | Cultural/memory lineage |
| Douglas-Bloodmoon | Wulfnic, Malachia, Noah, Jasper, Alyssa | Unified lineage |
| External | Kaladin, Marcus, Angel | Non-dynasty characters |

### 5.3 By Content Type

| Type | Characters | Theme |
|------|-----------|-------|
| Family drama | All dynasty members | Family dynamics, legacy, conflict |
| Business | Wulfnic, Erik, Alyssa | Trading house, commerce, power |
| Coming-of-age | Alyssa, Noah, Jasper | Young generation finding their place |
| Mentor | Wulfnic, Nixara | Guidance, tradition, wisdom |
| Outsider | Kaladin, Marcus, Angel | External perspectives on the family |

---

## 6. BEST PRACTICES

### Discovery
1. **Use consistent naming** across all platforms
2. **Include the `svartulfrverse` tag** on every export
3. **Write descriptions for humans, not just search engines** — Users read them before deciding to chat
4. **Keep tags accurate and current** — Update when canon changes

### Metadata
1. **Every bot needs a canonical ID** that maps to the repository
2. **Version your bots** — When canon updates, bump the version
3. **Include creation date** — Helps users understand the bot's context
4. **Use the structured tag taxonomy** — Consistency enables discovery

### Searchability
1. **Include key terms in the description** — Name, dynasty, role, setting
2. **Don't keyword-stuff** — Platforms may penalize this; users definitely will
3. **Make the first message count** — It's the first impression; quality affects engagement
4. **Update metadata when canon changes** — Stale metadata misleads users

---

## 7. COMMON MISTAKES

| Mistake | Impact | Fix |
|---------|--------|-----|
| Inconsistent naming across platforms | Users can't find the same character | Use canonical name everywhere |
| Missing svartulfrverse tag | Can't identify project bots | Always include |
| Over-tagging with trending terms | Wrong audience, bad experience | Use accurate tags only |
| No version tracking | Can't tell if bot is current | Include canon version |
| Description doesn't match content | User disappointment, bad reviews | Keep description accurate |
| No dynasty tags | Family-based discovery fails | Tag all dynasty members |

---

## 8. OPTIMIZATION RECOMMENDATIONS

### For JanitorAI
- Use the character bio field for discovery text (it's searchable)
- Include trigger words in tags that users actually search
- Keep the first message engaging — it affects algorithmic promotion
- Use the "Dead Dove" tag appropriately if content has mature themes

### For SillyTavern/CHUB
- Embed both V2 and V3 chunks in PNG exports for compatibility
- Use the `creator` field to identify the project
- Include alternate greetings for variety
- Attach a character_book (embedded lorebook) for rich context

### For Internal Use
- Maintain a character registry (the database/ directory IS the registry)
- Use canonical IDs consistently in all references
- Cross-reference family relationships in the family records, not character files
- Keep the EXPORT_MAPPING_MATRIX updated when new fields are added

---

## 📚 Cross-References

- **For export formatting per platform:** See [BOT_EXPORT_KNOWLEDGE_GUIDE.md](./BOT_EXPORT_KNOWLEDGE_GUIDE.md)
- **For field mapping reference:** See [EXPORT_MAPPING_MATRIX.md](../Lore_Worldbuilding/EXPORT_MAPPING_MATRIX.md)
- **For character card design:** See [JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md §2](./JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md)
- **For engine query routing:** See [ENGINE_KNOWLEDGE_GUIDE.md](../Engine_Logic/ENGINE_KNOWLEDGE_GUIDE.md)

---

*This guide is derived from BOT_SEARCH_SPECIFICATION.md and EXPORT_MAPPING_MATRIX.md. For formal specifications, consult the source documents directly.*
