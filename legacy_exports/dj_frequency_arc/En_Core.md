# PUBLIC METADATA

**Title:** SvartúlfrVerse | Engine Core

**Theme:** Midnight

**Description:**

_The invisible operating system of the SvartúlfrVerse._

En_Core routes Worlds, manages runtime state, enforces POV Overrides, compiles Lorebook entries, and injects formatting standards before every response.

It is the authority layer that guarantees architectural consistency across Experiences, Worlds, and Characters.

---

## Responsibilities

### World Routing

Determines the currently active World and controls transitions between realities.

**World Taxonomy:**

Contemporary
└── Urban Fantasy

Fantasy
├── High Fantasy
└── Norse Mythic

Science Fiction
├── Cyber
└── Wasteland

Historical
└── Regency

---

### Runtime State

Maintains global session variables:

- Active world
- Previous world
- Scenario state
- Environmental variables
- Relationship scaffolding

---

### POV Override Firewall

Enforces canonical casting rules.

If a Character is assigned to the POV Slot:

```text
C_Alyssa
C_Logan
C_Wulfnic
```

the Engine prevents duplicate NPC manifestations of that Character.

**Dependency:** ADR_008 (POV Identity Tags)

---

### Lorebook Compilation

Processes:

- Priorities
- Triggers
- Shifts
- Probabilities
- Apply limits

before content reaches the model.

---

### Output Standardization

Injects:

- Header formatting
- HUD formatting
- Diegetic interfaces
- Runtime notices

to maintain consistency across Experiences.

---

### User Settings Parser

Extracts and processes user preferences:

- Language
- NSFW Gate
- Dark Themes
- Prose Style

from character personality, scenario, and chat history.

---

### Narrative Engines

Maintains atmospheric and narrative systems:

- Weather and environmental effects
- Vitals mechanics (heart rate, temperature)
- Travel and fatigue protocols
- Care escalation for distress

---

### Diegetic UI

Applies world-appropriate interface formatting:

- Cyber: Terminal/Network interfaces
- Modern: Encrypted communications
- Pack: Howl-code/pack sense
- Fantasy: Scrolls and wax seals

---

## Message Depth

10

### Reason

The Engine must remain active during the entire session.

Every generated response depends on:

- World routing
- Lorebook compilation
- POV validation
- Formatting rules
- Atmospheric effects

These systems require maximum persistence.

---

## Cover Prompt

A colossal mechanical heart suspended inside an immense cathedral-sized data core, obsidian architecture, glowing amber circuitry, holographic data streams, warm cinematic lighting, deep shadows, luxury sci-fi aesthetic, painterly realism, monumental scale, intricate machinery, dramatic volumetric lighting.

---

## Style Constraints

- Warm cinematic lighting
- Rembrandt lighting
- Deep shadows
- Amber and obsidian palette
- Painterly realism
- Luxury visual storytelling

---

## Negative Prompt

generic anime, pastel palette, flat lighting, oversaturated colors, cartoon, low quality, blurry, watermark, text, logo, bad anatomy, malformed limbs, duplicate body parts, jpeg artifacts

---

## Technical Debt

### DEBT-001: Legacy Runtime Variable Names

Runtime variables use legacy naming:
- mv_active_l1
- mv_prev_l1

Retained for backward compatibility.
Migration deferred until after Los Angeles validation.

### DEBT-002: POV Override Identity Parsing

POV Override currently relies on identity parsing.
ADR_006 (POV Override) is operationally constrained until ADR_008 is implemented.
Implementation unchanged during this pass.

**POV Firewall Limitation:** Current implementation blocks `[Name: Alyssa]` and `Meta_Notes: C_Alyssa` but may not intercept alternative descriptions like "Alyssa Douglas", "Miss Douglas", "The Douglas Heiress". POV Override is conditionally validated pending ADR_008.

### DEBT-003: World-Specific Lore in En_Core

World-specific references exist in En_Core:
- Douglas Estate
- Solarton
- Bloodmoon
- Ambrosia

Documented as temporary debt.
Removal deferred until after Los Angeles validation.

### DEBT-004: World Registry / Runtime Taxonomy Divergence

Documentation uses canonical taxonomy:
- Contemporary, Urban Fantasy, High Fantasy, Norse Mythic, Cyber, Wasteland, Regency

Runtime uses legacy identifiers:
- modern, pack, cyber, fantasy, underworld

WORLD_REGISTRY is documentation-only and does not replace runtime routing.
Migration to canonical runtime identifiers deferred until after Los Angeles validation.

**Critical Mapping:** Urban Fantasy currently maps to "pack" runtime identifiers. This mapping must be preserved during any future taxonomy migration.

### DEBT-005: Lorebook Runtime Schema Divergence

Canonical Schema v1 uses field names:
- uid, category, world, priority, key, keysecondary, related, tags, comment, content, disable, order

Runtime Schema uses field names:
- keywords, scenario, triggers, andAnyTags, andAny, tag, minMessages, personality, layer, probability

**Dual-field migration implemented:**
- All legacy runtime fields preserved unchanged
- Canonical schema fields added alongside legacy fields
- Runtime continues using legacy field names
- compile() function unchanged
- Zero behavioral modifications

Future migration to canonical schema field names deferred until after Los Angeles validation.

---

## Related ADRs

- ADR_001: Knowledge vs Behavior
- ADR_002: Experience Layer
- ADR_003: Runtime Authority
- ADR_004: Player Avatar
- ADR_005: World Taxonomy
- ADR_006: POV Override
- ADR_008: POV Identity Tags
- ADR_009: Character Canonicality

---

## Governance Hierarchy

Runtime
↓
ADR
↓
Workflow
↓
Documentation
↓
Templates
