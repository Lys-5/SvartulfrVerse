# LOREBOOK SPECIFICATION

**Status:** CANONICAL  
**Date:** 2026-06-08  
**Authority:** ADR-005, ADR-006, R-009_Lorebook_Rules, R-007_Engine_Rules  
**Version:** 1.0 — Canon Freeze v1

---

## Purpose

This document defines the canonical structure, source attribution format, and canon-layer tagging system for lorebook generation. Lorebooks are **derived artifacts** — they organize and present canonical data for runtime consumption but hold no authoritative status.

**Authority:** All lorebook entries must be traceable to database/ records. Lorebooks must comply with R-009_Lorebook_Rules.

---

## Lorebook Structure

### Top-Level Organization

```
lorebook/
├── lorebook_active_canon.md       — Active Canon entries (runtime facts)
├── lorebook_historical_canon.md    — Historical Canon entries (documented history)
├── lorebook_cultural_canon.md      — Cultural Canon entries (family traditions)
├── lorebook_characters.md         — Character-derived entries
├── lorebook_worlds.md             — World/environment entries
├── lorebook_institutions.md       — Institution entries
├── lorebook_experiences.md        — Experience/scenario entries
└── README.md                      — Lorebook index and usage guide
```

### Entry Format

Every lorebook entry follows this standardized format:

```markdown
---

## [ENTRY_TITLE]

**Canon Layer:** [Active | Historical | Cultural]  
**Source:** [database/file/path.md]  
**Authority:** [Authority Domain]  
**Last Synchronized:** [ISO Date]  
**Entry ID:** [LB-XXX-NNN]

[Entry content — derived from canonical source. No original content.]

### Source Attribution
- **Primary Source:** [file path]
- **Supporting Sources:** [file paths, if any]
- **Canon Version:** 1.0

### Canon Layer Tags
- **[ACTIVE|HISTORICAL|CULTURAL]:** [Classification rationale]

---
```

---

## Canon-Layer Tagging System

### Tag Definitions

| Tag | Label | Color | Usage |
|-----|-------|-------|-------|
| `[ACTIVE]` | Active Canon | 🟢 Green | Runtime-eligible facts. Full governance enforcement. |
| `[HISTORICAL]` | Historical Canon | 🔵 Blue | Documented historical facts. Reference only. |
| `[CULTURAL]` | Cultural Canon | 🟡 Yellow | Family traditions, oral history, myths. Flavor only. |
| `[DEFERRED]` | Deferred Canon | ⚪ Grey | Valid but not active. Not included in runtime lorebooks. |
| `[CANDIDATE]` | Candidate Canon | 🟠 Orange | Proposed material. Not included until approved. |

### Tagging Rules

```
RULE 1: Every lorebook entry MUST have exactly one canon layer tag.
RULE 2: Active Canon entries form the primary lorebook for runtime use.
RULE 3: Historical Canon entries are separated into their own section/file.
RULE 4: Cultural Canon entries are separated and clearly marked as non-factual.
RULE 5: Deferred and Candidate Canon entries are NOT included in runtime lorebooks.
RULE 6: Cultural Canon entries MUST include a disclaimer: "Cultural tradition — not runtime fact."
RULE 7: No entry may be promoted to a higher canon layer without Authority Decision.
```

### Canon Layer Content Rules

#### Active Canon Entries

| Property | Rule |
|----------|------|
| Source | Must reference Active Canon records in database/ |
| Content | Must be verifiable facts from authority records |
| Runtime Use | Full compilation — treated as ground truth |
| Update | Requires Authority Decision to modify |
| Examples | Character identities, family relationships, visual baselines, institutions |

#### Historical Canon Entries

| Property | Rule |
|----------|------|
| Source | Must reference Historical Canon records or ADR-001 |
| Content | Documented historical facts with evidence |
| Runtime Use | Reference only — background context |
| Update | Requires new evidence to modify |
| Examples | Dynasty origins, migration timelines, historical figures |

#### Cultural Canon Entries

| Property | Rule |
|----------|------|
| Source | Must reference ADR-006 Cultural Canon classification |
| Content | Family stories, traditions, myths, legends |
| Runtime Use | Dialogue flavor only — never as factual content |
| Update | Append-only — new traditions may be added with evidence |
| Examples | Svartúlfr (Black Wolf), Fenrir, family sagas |

---

## Source Attribution Format

### Inline Attribution

Every lorebook entry must include inline source attribution:

```markdown
**Source:** database/characters/C_Alyssa_Douglas_Bloodmoon.md → Identity, Psychology  
**Authority:** Character Authority (ADR-003)  
**Canon Layer:** Active
```

### Composite Attribution

When an entry derives from multiple sources:

```markdown
**Primary Source:** database/families/F_Douglas_Bloodmoon.md  
**Supporting Sources:**
- database/families/F_Parent_Child.md
- database/characters/C_Malachia_Douglas_Bloodmoon.md
- database/characters/C_Noah_Douglas_Bloodmoon.md
- database/characters/C_Jasper_Douglas_Bloodmoon.md
- database/characters/C_Alyssa_Douglas_Bloodmoon.md
**Authority:** Family Authority (ADR-002)  
**Canon Layer:** Active
```

### Attribution Metadata Block

Every lorebook file must include a header metadata block:

```markdown
# Lorebook: [Section Name]

**Canon Layer:** [Active | Historical | Cultural]  
**Generated:** [ISO Timestamp]  
**Canon Version:** 1.0  
**Source Repository:** SvartulfrVerse  
**Authority:** [Authority Domain]  
**Compliance:** R-009_Lorebook_Rules v1.0  
**Validation:** validation_engine status [pass/fail]

---

**DISCLAIMER:** This lorebook is a derived artifact. The authoritative source is the SvartulfrVerse repository (database/). This document must not contradict database/ records. If a conflict exists, database/ prevails.
```

---

## Lorebook Content Sections

### Characters Lorebook

**Source:** `database/characters/C_*.md`

| Entry Type | Canon Layer | Fields Extracted |
|------------|-------------|------------------|
| Character Identity | Active | Name, age, dynasty, role |
| Character Personality | Active | Core traits, fears, motivations |
| Character Visual | Active | Hair, eyes, build, height |
| Character Biography | Active | Backstory, key events |
| Character Relationships | Active | Non-familial relationships |
| Character Education | Active | Institution, level, track |
| Character Occupation | Active | Baseline profession |

**Format Example:**

```markdown
---

## Alyssa Douglas-Bloodmoon

**Canon Layer:** [ACTIVE]  
**Source:** database/characters/C_Alyssa_Douglas_Bloodmoon.md  
**Authority:** Character Authority  
**Entry ID:** LB-CHR-012

**Identity:** Alyssa Douglas-Bloodmoon, age 19, Douglas-Bloodmoon dynasty heir, twin.  
**Personality:** Affectionate, naive, trusting, family-oriented, defenseless.  
**Visual:** Caramel-brown hair, mint green eyes, petite hourglass build, 165cm. Fusion-visual with strongest Nixara resemblance.  
**Education:** UCLA Pre-Med, first-year undergraduate, GPA 3.8.  
**Aspiration:** Neuropsychiatry or Biogenetics (aspirational).

### Source Attribution
- **Primary Source:** database/characters/C_Alyssa_Douglas_Bloodmoon.md
- **Visual Authority:** database/worlds/W_Visual_Inheritance.md
- **Canon Version:** 1.0

---
```

### Families Lorebook

**Source:** `database/families/F_*.md`

| Entry Type | Canon Layer | Fields Extracted |
|------------|-------------|------------------|
| Dynasty Structure | Active | Dynasty membership, founding |
| Parent-Child | Active | Biological relationships |
| Marriages | Active | Union records |
| Surname Rules | Active | Naming conventions |
| Historical Lineage | Historical | Pre-contemporary genealogy |

### Worlds Lorebook

**Source:** `database/worlds/W_*.md`

| Entry Type | Canon Layer | Fields Extracted |
|------------|-------------|------------------|
| Setting | Active | Geographic context, timeline |
| Visual Baseline | Active | Dynasty appearance standards |
| Visual Inheritance | Active | Inheritance rules, fusion model |
| Style Guide | Active | Aesthetic guidelines |

### Institutions Lorebook

**Source:** `database/institutions/I_*.md`

| Entry Type | Canon Layer | Fields Extracted |
|------------|-------------|------------------|
| Institution Identity | Active | Name, type, scope |
| Personnel | Active | Key personnel, roles |
| Relationships | Active | Character affiliations |

### Experiences Lorebook

**Source:** `database/experiences/Ex_*.md`

| Entry Type | Canon Layer | Fields Extracted |
|------------|-------------|------------------|
| Scenario | Active | Framing, context |
| Roles | Active | Character assignments |
| Occupation Overrides | Active | Scenario-specific roles |

### Cultural Lorebook

**Source:** ADR-006 Cultural Canon classification

| Entry Type | Canon Layer | Fields Extracted |
|------------|-------------|------------------|
| Family Traditions | Cultural | Oral traditions, stories |
| Myths & Legends | Cultural | Mythological references |
| Cultural Identity | Cultural | Ancestral clan identity |

**Format Example:**

```markdown
---

## Svartúlfr (Black Wolf) — Ancestral Clan Identity

**Canon Layer:** [CULTURAL]  
**Source:** ADR-006_Canon_Layer_Architecture.md — Cultural Canon classification  
**Authority:** ADR-006  
**Entry ID:** LB-CUL-001

**⚠️ CULTURAL CANON — NOT RUNTIME FACT**

The Bloodmoon family preserves the ancestral identity of Svartúlfr (Black Wolf) as part of their Icelandic heritage. This is a **cultural tradition and family story**, not a runtime fact.

The Svartúlfr identity represents:
- Ancestral clan identity from Icelandic Bloodmoon lineage
- Family storytelling tradition passed through generations
- Cultural heritage preserved by Wulfnic Bloodmoon as memory keeper

**This entry must NOT be compiled as:**
- A runtime fact or character ability
- A supernatural element
- A world mechanic

**This entry MAY be used for:**
- Character dialogue (family stories)
- Background flavor (Icelandic heritage)
- Wulfnic's custodial role (memory keeper)

### Source Attribution
- **Primary Source:** ADR-006_Canon_Layer_Architecture.md
- **Canon Version:** 1.0

---
```

---

## Generation Rules

### R-009 Compliance

All lorebook generation must comply with R-009_Lorebook_Rules:

| Rule | Requirement | Enforcement |
|------|-------------|-------------|
| R-009-LRB-001 | Lorebooks are derived artifacts, not authority | Header disclaimer on every file |
| R-009-LRB-002 | Must not contradict canon | validation_engine cross-reference check |
| R-009-LRB-003 | All entries must reference database/ sources | Source attribution mandatory |
| R-009-LRB-004 | Must mark Active/Historical/Cultural | Canon layer tags on every entry |

### Generation Workflow

```
1. Select source domain (characters, families, worlds, etc.)
2. Query En_Core for all records in domain
3. For each record:
   a. Extract relevant fields per section mapping
   b. Classify canon layer (Active/Historical/Cultural)
   c. Generate entry with source attribution
   d. Apply canon layer tag
4. validation_engine: cross-reference all entries against database/
5. IF valid: Write lorebook file with metadata header
6. IF invalid: Reject entries, return error report
7. Update synchronization timestamp
```

### Forbidden Lorebook Operations

| Operation | Rule | Authority |
|-----------|------|-----------|
| Create entries without database/ source | PROHIBITED | R-009-LRB-003 |
| Contradict database/ records | PROHIBITED | R-009-LRB-002 |
| Treat lorebook as authoritative | PROHIBITED | R-009-LRB-001 |
| Omit canon layer tags | PROHIBITED | R-009-LRB-004 |
| Treat Cultural Canon as Active | PROHIBITED | R-009-LRB-004, ADR-006 |
| Include Deferred/Candidate in runtime | PROHIBITED | ADR-006 |
| Add information not in database/ | PROHIBITED | R-009-LRB-002 |

---

## Synchronization Policy

- Lorebooks are regenerated when database/ records change
- Every regeneration includes a new synchronization timestamp
- Version-locked to canon version (currently 1.0)
- Outdated lorebooks must be flagged and regenerated

---

## Authority

**Established by:** Architecture Review & Canon Authority  
**Approved by:** Canon Freeze v1 Governance  
**Depends on:** ADR-005, ADR-006, R-007, R-009  
**Version:** 1.0 — Frozen under Canon Freeze v1
