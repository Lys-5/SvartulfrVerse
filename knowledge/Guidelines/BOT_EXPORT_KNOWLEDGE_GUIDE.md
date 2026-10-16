# BOT EXPORT KNOWLEDGE GUIDE

**Version:** 1.0
**Date:** 2026-06-08
**Purpose:** Operational guide to bot character card exports. Companion to BOT_EXPORT_SPECIFICATION.md — explains export workflows, field mappings, common mistakes, and platform-specific guidance.

---

## 1. WHY BOT EXPORTS ARE COMPLEX

A SvartúlfrVerse character exists as structured canonical data in `database/`. A bot character card exists as a JSON or PNG file that an AI platform can consume. **The export process transforms canonical data into platform-compatible formats while preserving:**

1. **Canon integrity** — Every exported field traces to a database record
2. **Authority compliance** — Data comes from the correct authority layer
3. **Platform compatibility** — Output matches the target platform's schema
4. **Traceability** — Provenance metadata enables audit and debugging

If any of these four requirements is violated, the export is invalid.

---

## 2. THE THREE EXPORT FORMATS

### 2.1 Generic JSON (Canonical)

**Purpose:** The universal interchange format. All other formats derive from this.

**Why it exists:** JanitorAI and SillyTavern have different schemas. The Generic JSON is the superset that contains all fields needed by any platform. Platform adapters transform from Generic JSON to platform-specific format.

**Key Fields:**
```json
{
  "character": {
    "id": "C_Alyssa",              // Canonical identifier
    "canon_layer": "active",         // ADR-006 classification
    "identity": {
      "name": "Alyssa Douglas-Bloodmoon",
      "gender": "Female",
      "age": 19,
      "birth_date": "2005-03-14",
      "nationality": "American",
      "pronouns": "she/her"
    },
    "visual": {
      "hair_color": "Dark brown",
      "eye_color": "Heterochromatic (left: ice-blue, right: amber)",
      "build": "Athletic",
      "height": "5'7\"",
      "visual_classification": "Douglas-dominant"
    },
    "psychology": {
      "core_traits": ["Determined", "Loyal", "Stubborn"],
      "fears": ["Failure", "Letting family down"],
      "motivations": ["Prove herself beyond her family name"]
    },
    "capabilities": {
      "skills": ["Equestrian", "Business management"],
      "education": "UCLA, Business Administration",
      "occupation": "Douglas Trading House junior executive"
    },
    "relationships": {
      "parents": ["C_Malachia", "C_Jasper"],  // IDs only, not names
      "siblings": ["C_Noah"],
      "dynasty": "Douglas-Bloodmoon"
    },
    "biography": {
      "backstory": "Born in Los Angeles...",
      "current_status": "Active in family business"
    }
  },
  "provenance": [
    "database/characters/C_Alyssa_Douglas_Bloodmoon.md",
    "database/families/F_Douglas_Bloodmoon.md",
    "database/worlds/W_Visual_Inheritance.md"
  ]
}
```

### 2.2 JanitorAI Format

**Purpose:** Character cards for the JanitorAI platform.

**Schema:** JSON with JanitorAI-specific field names. Can also be embedded in PNG.

**Key Differences from Generic JSON:**
- `char_name` instead of `character.identity.name`
- `body` instead of composite description
- `first_persona` / `second_persona` for personality
- `personality` field (summary)
- `example_dialogue` for speech patterns
- `greeting` for first message
- `extensions.svartulfrverse` for traceability (custom)

**Required Fields (JanitorAI):**
| Field | Source | Notes |
|-------|--------|-------|
| `char_name` | C_Template → Identity.Name | Required |
| `body` | Composite: visual + personality | Max ~5000 chars |
| `personality` | Psychology.Core Traits | Formatted as prose |
| `scenario` | Default experience context | From Experience Authority |
| `first_mes` | Generated from personality + context | Must not contradict canon |
| `mes_example` | Generated from personality | Must reflect canonical speech |
| `greeting` | Generated from personality | Opening line |
| `tags` | Canon layer + dynasty + ID | Must include `SvartulfrVerse` |
| `extensions.svartulfrverse` | Engine metadata | Traceability data (required) |

### 2.3 SillyTavern Format (Character Card V3)

**Purpose:** Character cards for the SillyTavern platform.

**Schema:** Character Card V3 (`chara_card_v3`) — JSON embedded in PNG tEXt chunk with keyword `ccv3`, or standalone JSON.

**Key Differences from Generic JSON:**
- `data.name` instead of `character.identity.name`
- `data.character_desc` for full description
- `data.system_prompt` for meta-instructions
- `data.post_history_instructions` for hard constraints
- `data.character_book` for embedded lorebook
- `data.alternate_greetings` for multiple opening messages
- `extensions.svartulfrverse` for traceability (custom)

**Required Fields (SillyTavern V3):**
| Field | Source | Notes |
|-------|--------|-------|
| `data.name` | C_Template → Identity.Name | Required |
| `data.description` | Composite: personality + appearance | Full description |
| `data.personality` | Psychology.Core Traits | Summary |
| `data.scenario` | Default experience context | From Experience Authority |
| `data.first_mes` | Generated from personality + context | Opening dialogue |
| `data.mes_example` | Generated from personality | Dialogue examples |
| `data.system_prompt` | Composite: identity + constraints | System-level instructions |
| `data.creator_notes` | History + backstory | For bot context |
| `data.post_history_instructions` | Behavioral constraints | From psychology + rules |
| `data.tags` | Canon layer + dynasty | Tag array |
| `data.extensions.svartulfrverse` | Engine metadata | Traceability data (required) |

---

## 3. EXPORT FLOW — STEP BY STEP

### Step 1: Request
A bot export request specifies:
- **Target character** (canonical ID, e.g., `C_Alyssa`)
- **Target platform** (JanitorAI, SillyTavern, Generic JSON)
- **Scenario context** (optional — which experience to use for scenario/roles)

### Step 2: Data Collection
En_Core collects data from multiple sources:
- **Character record** → identity, personality, psychology, capabilities, biography
- **Family engine** → genealogy, dynasty membership
- **Visual records** → appearance, visual classification
- **Experience engine** → scenario context (if specified)

### Step 3: Validation
All collected data passes through `validation_engine(full)`:
- Cross-reference: Do all references resolve?
- Canon-layer: Is all data from the correct layer?
- Authority: Does each field come from its owning authority?
- Traceability: Does each field have a provenance chain?

### Step 4: Format Transformation
Validated data is transformed to the target platform schema:
- Generic JSON → direct mapping
- JanitorAI → field name mapping + persona formatting
- SillyTavern → V3 schema mapping + system prompt generation

### Step 5: Provenance Attachment
The `extensions.svartulfrverse` block is added:
```json
"extensions": {
  "svartulfrverse": {
    "canon_id": "C_Alyssa",
    "canon_layer": "active",
    "provenance": [
      "database/characters/C_Alyssa.md",
      "database/families/F_Douglas_Bloodmoon.md"
    ],
    "visual_classification": "Douglas-dominant",
    "dynasty": "Douglas-Bloodmoon",
    "validation_status": "PASS",
    "generation_timestamp": "2026-06-08T00:00:00Z",
    "canon_version": "1.0"
  }
}
```

### Step 6: Release
The formatted, validated, provenance-attached character card is released.

---

## 4. FIELD OWNERSHIP — WHO OWNS WHAT

This is the most common source of export errors. Every field has exactly one owning authority:

| Export Field | Owner Authority | Source Path |
|-------------|----------------|-------------|
| Name, age, gender, nationality | Character | database/characters/C_*.md |
| Personality, traits, fears, motivations | Character | database/characters/C_*.md |
| Skills, education, occupation | Character | database/characters/C_*.md |
| Backstory, biography | Character | database/characters/C_*.md |
| Hair, eyes, build, height | Visual | database/worlds/W_Visual_*.md + C_*.md |
| Visual classification | Visual | database/worlds/W_Visual_Inheritance.md |
| Parents, children, siblings, spouse | Family | database/families/F_Parent_Child.md, F_Marriages.md |
| Dynasty membership | Family | database/families/F_Douglas_Bloodmoon.md |
| Surname rules | Family | database/families/F_Surname_Authority.md |
| Scenario context | Experience | database/experiences/Ex_*.md |
| Role assignments | Experience | database/experiences/Ex_*.md |
| Occupation overrides | Experience | database/experiences/Ex_*.md |
| Provenance metadata | Engine | Auto-generated |

**If a field's data comes from the wrong authority, the export fails validation.**

---

## 5. COMMON MISTAKES AND ANTI-PATTERNS

### Anti-Pattern 1: Manual Lore Injection
**What it looks like:** Adding personality traits, backstory details, or speech patterns that don't exist in the database because "it makes the bot better."
**Why it's wrong:** The export is no longer canon-derived. It contains unaudited, untraceable content.
**Fix:** If the database doesn't have it, the export doesn't include it. To add new content, update the database through the proper Authority workflow first.

### Anti-Pattern 2: Authority Cross-Contamination
**What it looks like:** Including genealogy data in the character's personality field, or putting personality traits in the family data.
**Why it's wrong:** Violates authority boundaries. Genealogy belongs to Family Authority. Personality belongs to Character Authority.
**Fix:** Each field comes from its owning authority only. Cross-reference through relationship_engine if needed.

### Anti-Pattern 3: Missing Provenance
**What it looks like:** Exporting a character card without the `extensions.svartulfrverse` block.
**Why it's wrong:** The export becomes untraceable. If a field is wrong, there's no way to find the source.
**Fix:** Provenance is mandatory. Every export includes the full traceability block.

### Anti-Pattern 4: Canon Layer Violation
**What it looks like:** Including Cultural Canon content (e.g., werewolf mythology) in an Active-layer export without marking it as Cultural.
**Why it's wrong:** Cultural content presented as Active fact violates ADR-006.
**Fix:** Tag all content with its canon layer. Cultural content gets a disclaimer or is excluded from Active exports.

### Anti-Pattern 5: Platform Schema Drift
**What it looks like:** Using V2 schema fields in a V3 export, or using deprecated JanitorAI field names.
**Why it's wrong:** The target platform may not recognize the fields, causing silent failures.
**Fix:** Always use the current platform schema. Reference the Character Card Specification (V2/V3) for field definitions.

### Anti-Pattern 6: Over-Description
**What it looks like:** Stuffing every available field from the database into the character card, resulting in a 3000+ token card.
**Why it's wrong:** Consumes context window, reduces conversation memory, and can confuse the model with too many instructions.
**Fix:** Use the token budget guidelines. Card: 500-1300 tokens. Extended details go in the lorebook.

---

## 6. VALIDATION REQUIREMENTS

Every export must pass these validation checks before release:

| Check | What It Verifies | Failure Result |
|-------|-----------------|----------------|
| Entity resolution | All character references exist in database/ | FAIL |
| Relationship consistency | All family claims match Family Authority | FAIL |
| Visual consistency | All visual claims match Visual Authority | FAIL |
| Identity consistency | All identity claims match Character Authority | FAIL |
| Canon-layer classification | All content correctly classified | FAIL |
| Authority ownership | All data from correct authority | FAIL |
| Rejected canon detection | No rejected concepts present | FAIL |
| Traceability | All fields have provenance chain | FAIL |
| Schema compliance | Output matches target platform schema | FAIL |

---

## 7. PRACTICAL EXAMPLES

### Example: Exporting Wulfnic Bloodmoon to JanitorAI

**Step 1: Data Collection**
```
Character record: C_Wulfnic_Bloodmoon.md
  → Name: Wulfnic Bloodmoon
  → Age: 76 (born 1948)
  → Personality: Stern, protective, traditional, pragmatic
  → Occupation: Patriarch of the Douglas-Bloodmoon family

Family engine:
  → Spouse: Nixara Bloodmoon
  → Children: Erik Douglas (adopted/step)
  → Dynasty: Douglas-Bloodmoon

Visual records:
  → Visual classification: Bloodmoon-dominant
  → Hair: Silver-white
  → Eyes: Pale blue
```

**Step 2: Validation** → All checks PASS

**Step 3: Format for JanitorAI**
```json
{
  "char_name": "Wulfnic Bloodmoon",
  "body": "Wulfnic Bloodmoon is the patriarch of the Douglas-Bloodmoon family...",
  "personality": "Stern, protective, traditional, pragmatic. Values family loyalty above all...",
  "scenario": "Present day, Los Angeles. The Douglas-Bloodmoon family estate.",
  "first_mes": "*The study smells of old leather and pipe tobacco. Wulfnic looks up from his desk...*",
  "mes_example": "<START>\n{{user}}: I need to talk to you about something.\n{{char}}: *Sets down his pen and fixes you with a measured look.* Then talk. I'm listening.",
  "tags": ["SvartulfrVerse", "Douglas-Bloodmoon", "patriarch", "male", "active-canon"],
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
}
```

---

## 📚 Cross-References

- **For engine data collection during export:** See [ENGINE_KNOWLEDGE_GUIDE.md](../Engine_Logic/ENGINE_KNOWLEDGE_GUIDE.md)
- **For field mapping reference:** See [EXPORT_MAPPING_MATRIX.md](../Lore_Worldbuilding/EXPORT_MAPPING_MATRIX.md)
- **For bot discovery and metadata:** See [BOT_SEARCH_KNOWLEDGE_GUIDE.md](./BOT_SEARCH_KNOWLEDGE_GUIDE.md)
- **For character card best practices:** See [JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md §§2-4](./JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md)
- **For validation requirements:** See [VALIDATION_KNOWLEDGE_GUIDE.md](./VALIDATION_KNOWLEDGE_GUIDE.md)

---

*This guide is derived from BOT_EXPORT_SPECIFICATION.md and EXPORT_MAPPING_MATRIX.md. For formal field definitions and platform schemas, consult the specifications directly.*
