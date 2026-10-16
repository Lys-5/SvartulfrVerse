# ADR-004: Visual Authority Layer — Appearance and Inheritance Architecture

**Status:** ACCEPTED  
**Date:** 2026-06-07  
**Title:** Visual Authority Layer Definition and Inheritance Ownership Model

## Context

ADR-000 established the runtime baseline. ADR-001 formalized dynastic origins. ADR-002 defined Family Authority as sole custodian of genealogy. ADR-003 defined Character Authority as sole custodian of identity.

Visual appearance represents a distinct authority domain that must be formally defined. Visual inheritance patterns (how children inherit appearance from parents) are NOT genealogy—they are a separate visual authority that must remain independent from Family Authority while still referencing genealogical relationships.

## Decision

We establish the Visual Authority Layer as the sole canonical source for all appearance, aesthetic, and visual inheritance data within SvartulfrVerse.

### Scope

- **Only Human** (no supernatural visual elements)
- **Contemporary** (2020s-2030s timeline)
- **Los Angeles Dynasty** (geographic and familial focus)

### Visual Authority Layer Definition

**Visual Authority Layer is the sole owner and canonical custodian of:**

1. **Appearance Baseline** — Physical characteristics (hair, eyes, build, skin)
2. **Aesthetic Profile** — Style, fashion, visual vibe
3. **Visual Inheritance Rules** — How appearance passes from parent to child
4. **Coloration Authority** — Eye color, hair color, skin tone inheritance
5. **Resemblance Rules** — Which parent a child resembles

**Visual Authority Layer constraints:**

- **Visual-Only Custodian** — Owns appearance, not genealogy or identity
- **Independent from Genealogy** — Visual inheritance ≠ genealogical inheritance
- **Reference-Based** — May reference Family Authority for parent-child relationships
- **Authority-Driven** — Decisions governed by explicit ADR, not by archive inference

---

## Visual Baseline Definitions

### Douglas Visual Baseline

**Canonical Douglas Appearance:**

| Attribute | Value |
|-----------|-------|
| Hair Color | Black (streaked with silver/grey with age) |
| Eye Color | Amber |
| Build | Massive, muscular, imposing |
| Skin | Weathered, mature |
| Aesthetic | Corporate monarch, power suits, luxury executive |

**Reference Character:** Erik Douglas

**Visual DNA Anchor:**
```
Erik Douglas:
  Always:
    - Black hair streaked with silver/grey, slicked back
    - Amber eyes, cold and unyielding
    - 205cm, massive muscular build, weathered skin
    - Corporate monarch aesthetic, bespoke power suits
  Never:
    - Long white hair
    - Ancient king aesthetic
    - Nordic patriarch styling or fur robes
    - T-shirts or casual wear
  Football Exception:
    - During UCLA football games only: authorized to wear the old UCLA team captain's football jersey
    - This is the sole exception to the "no casual wear" restriction
    - Jersey must be the authentic UCLA captain's jersey from his playing years
```

### Bloodmoon Visual Baseline

**Canonical Bloodmoon Appearance:**

| Attribute | Value |
|-----------|-------|
| Hair Color | Blonde |
| Eye Color | Blue |
| Build | Lean, strong, refined |
| Skin | Fair complexion |
| Aesthetic | Ancestral nobility, old-world aristocratic |

**Reference Character:** Wulfnic Bloodmoon

**Visual DNA Anchor:**
```
Wulfnic Bloodmoon:
  Always:
    - Blonde hair (youth) → Silver-white (old age)
    - Blue eyes, steady and knowing
    - 205cm, former warrior physique, broad shoulders
    - Powerfully built despite age
    - Ancestral nobility aesthetic, old-world authority
  Never:
    - CEO aesthetic
    - Executive skyscrapers or corporate boardrooms
    - Modern streetwear or tactical gear
    - Medieval/viking cosplay appearance
```

**Note:** Recovered canon establishes Bloodmoon visual DNA as blonde hair and blue eyes. Wulfnic's hair transitioned to silver-white with age. Previous documentation referenced silver-white as baseline, which has been reconciled.

---

## Visual Fusion Model

### Definition

The Visual Fusion Model defines how children of the Douglas-Bloodmoon union inherit visual characteristics. This model is **visual authority only** and does not affect genealogical authority.

### Core Principle

**Visual inheritance ≠ Genealogical inheritance**

- Genealogy defines WHO is parent to WHOM
- Visual inheritance defines WHAT characteristics pass from parent to child
- These are separate authority domains

### Visual DNA Baselines

| Dynasty | Hair Color | Eye Color | Build |
|---------|------------|-----------|-------|
| Douglas | Black | Amber | Massive, muscular |
| Bloodmoon | Blonde | Blue | Lean, refined |

---

## Character-Specific Visual Inheritance

### Malachia Douglas-Bloodmoon

**Visual Inheritance:** Strongest Douglas coloration expression

| Attribute | Expression | Source |
|-----------|------------|--------|
| Hair | Black | Douglas-visual-dominant |
| Eyes | Amber | Douglas-visual-dominant |
| Build | Tank-like, scarred | Douglas-visual-dominant |
| Aesthetic | Tactical utilitarian | Character-specific |

**Classification:** Douglas-visual-dominant

---

### Noah Douglas-Bloodmoon

**Visual Inheritance:** Strongest Bloodmoon coloration expression

| Attribute | Expression | Source |
|-----------|------------|--------|
| Hair | Blonde | Bloodmoon-visual-dominant |
| Eyes | Blue | Bloodmoon-visual-dominant |
| Build | Lithe elegant swimmer | Bloodmoon-refined |
| Aesthetic | Bespoke elegance | Character-specific |

**Classification:** Bloodmoon-visual-dominant

---

### Alyssa Douglas-Bloodmoon

**Visual Inheritance:** Fusion result with strongest Nixara resemblance

| Attribute | Expression | Source |
|-----------|------------|--------|
| Hair | Caramel-brown | Fusion blend |
| Eyes | Mint green | Fusion blend |
| Build | Petite hourglass | Nixara-derived |
| Facial Structure | Nixara resemblance | Maternal |
| Body Proportions | Nixara archetype | Maternal |
| Aesthetic | Ethereal lunar beauty | Character-specific |

**Classification:** Fusion-visual with maternal-resemblance

**Alyssa/Nixara Resemblance Rule:**
- Alyssa exhibits strongest facial and body resemblance to Nixara Bloodmoon
- This is a **visual inheritance pattern** that does not affect genealogy
- Alyssa remains fully Douglas-Bloodmoon heir by genealogy

---

### Jasper Douglas-Bloodmoon

**Visual Inheritance:** Twin fusion result (Alyssa's twin)

| Attribute | Expression | Source |
|-----------|------------|--------|
| Hair | Caramel-brown | Fusion blend (twin match) |
| Eyes | Mint green | Fusion blend (twin match) |
| Build | Lean athletic | Fusion blend |
| Aesthetic | Hypebeast streetwear | Character-specific |

**Classification:** Fusion-visual (twin inheritance)

**Twin Fusion Rule:**
- Jasper and Alyssa share identical fusion inheritance as twins
- Both express caramel-brown hair and mint-green eyes
- Aesthetic and build differ by character-specific development

---

## Visual Fusion Model — Official Example

### Nixara Bloodmoon Visual Baseline

Nixara serves as the primary morphological template for Alyssa Douglas-Bloodmoon, while Bloodmoon coloration is preserved primarily through Noah Douglas-Bloodmoon.

**Nixara Bloodmoon Visual Definition:**

| Attribute | Value |
|-----------|-------|
| Height | 165 cm |
| Body | Petite hourglass |
| Measurements | 95-55-95 |
| Face | Soft facial structure, delicate jawline, fair skin |
| Eyes | Ice Blue |
| Hair | Blonde, tailbone-length, silky straight |

---

### Visual Inheritance Result

The following inheritance pattern resolves the apparent conflict between "Noah resembles Nixara" and "Alyssa resembles Nixara" by separating morphological inheritance from chromatic inheritance.

#### Nixara (Template)

```
Body Structure: Nixara
Hair: Bloodmoon Blonde
Eyes: Bloodmoon Ice Blue
```

Nixara carries pure Bloodmoon visual DNA and serves as the maternal template.

---

#### Noah Douglas-Bloodmoon

```
Body Structure: Mixed (refined)
Hair: Bloodmoon Blonde
Eyes: Bloodmoon Blue
```

**Inheritance Classification:** Chromatic Inheritance

Noah carries the strongest Bloodmoon coloration. He inherits blonde hair and blue eyes in pure Bloodmoon expression.

**Authority Statement:**
> Noah carries the strongest Bloodmoon coloration.

---

#### Alyssa Douglas-Bloodmoon

```
Body Structure: Nixara Clone
Hair: Caramel Brown
Eyes: Mint Green
```

**Inheritance Classification:** Morphological Inheritance

Alyssa exhibits the strongest facial and body resemblance to Nixara. She inherits Nixara's silhouette, proportions, and facial structure, with fusion-blend coloration.

**Authority Statement:**
> Alyssa physically resembles Nixara more than any other descendant.

---

#### Jasper Douglas-Bloodmoon

```
Body Structure: Male Twin Variant
Hair: Caramel Brown
Eyes: Mint Green
```

**Inheritance Classification:** Twin Fusion Inheritance

Jasper shares identical fusion coloration with Alyssa as her twin. Build and aesthetic differ by character-specific development.

---

### Visual Authority Finding

This distinction enables both statements to be simultaneously true:

| Statement | Authority | Status |
|-----------|-----------|--------|
| Alyssa physically resembles Nixara more than any other descendant | Character Authority | TRUE |
| Noah carries the strongest Bloodmoon coloration | Visual Authority | TRUE |

**Canonical Rule:**
```
Alyssa = Morphological Inheritance (Nixara silhouette)
Noah = Chromatic Inheritance (Bloodmoon coloration)
```

This formulation is precise enough to serve as an official example of the Visual Fusion Model.

---

## Visual Authority Independence

### EXPLICIT SEPARATION

**Visual Authority IS INDEPENDENT from Genealogy Authority:**

1. **Different Domains** — Genealogy owns relationships; Visual owns appearance
2. **Different Rules** — Genealogy follows descent; Visual follows inheritance patterns
3. **Different Mutability** — Genealogy is immutable; Visual may have exceptions
4. **Different Queries** — Genealogy queries "who is parent"; Visual queries "what did child inherit"

### Cross-Authority Reference Model

```
Visual Authority ──references──► Family Authority
     │                                  │
     │ (queries parent-child            │
     │  relationships for               │
     │  inheritance context)            │
     │                                  │
     ▼                                  ▼
[Visual Inheritance Rules]    [Genealogical Records]
     │                                  │
     │                                  │
     ▼                                  ▼
[Character Visual Definition] [Character Family Reference]
```

### What Visual Authority MAY Reference

- Parent-child relationships (from Family Authority)
- Dynasty membership (from Family Authority)
- Surname rules (from Family Authority)

### What Visual Authority MAY NOT Define

- Genealogical relationships
- Dynasty membership
- Surname authority
- Family structure

---

## Authority Boundary Matrix

```
┌─────────────────────────────────────────────────────────────────────┐
│                    VISUAL AUTHORITY BOUNDARY MATRIX                │
├─────────────────┬──────────────┬─────────────┬──────────────────────┤
│ Domain          │ Owner        │ Consumers   │ Override Allowed?  │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Appearance      │ Visual       │ All         │ NO                   │
│ Aesthetic       │ Visual       │ All         │ NO                   │
│ Coloration      │ Visual       │ All         │ NO                   │
│ Build           │ Visual       │ All         │ NO                   │
│ Resemblance     │ Visual       │ All         │ NO                   │
│ Inheritance     │ Visual       │ All         │ NO                   │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Genealogy       │ Family       │ Visual      │ NO (reference only)  │
│ Dynasty         │ Family       │ Visual      │ NO (reference only)  │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Identity        │ Character    │ Visual      │ NO (reference only)  │
│ Personality     │ Character    │ Visual      │ NO (reference only)  │
└─────────────────┴──────────────┴─────────────┴──────────────────────┘
```

---

## Visual Inheritance Authority Records

### Canonical Inheritance Patterns

The following inheritance patterns are explicitly stored as canonical visual authority records.

#### Douglas-Visual-Dominant Inheritance

**Definition:** Child expresses Douglas visual baseline (black hair, amber eyes, massive build).

**Canonical Properties:**
- Strongest Douglas coloration expression
- Example: Malachia Douglas-Bloodmoon

#### Bloodmoon-Visual-Dominant Inheritance

**Definition:** Child expresses Bloodmoon visual baseline (blonde hair, blue eyes, lean build).

**Canonical Properties:**
- Strongest Bloodmoon coloration expression
- Example: Noah Douglas-Bloodmoon

#### Fusion-Visual Inheritance

**Definition:** Child expresses blended visual characteristics from both dynasties.

**Canonical Properties:**
- Blend of Douglas and Bloodmoon visual DNA
- Examples: Alyssa Douglas-Bloodmoon, Jasper Douglas-Bloodmoon

#### Maternal-Resemblance Pattern

**Definition:** Daughter exhibits strongest facial and body resemblance to mother.

**Canonical Properties:**
- Applies to Alyssa Douglas-Bloodmoon (Nixara resemblance)
- Does not override genealogy

---

## Inference Policy

**EXPLICITLY PROHIBITED:** Runtime inference of new visual facts.

### What the Runtime MAY Do

- **Query** Visual Authority records
- **Reference** visual data for rendering context
- **Validate** claimed appearance against authority records
- **Return** read-only visual data to other layers
- **Log** visual queries for audit trail

### What the Runtime MAY NOT Do

- **Infer** appearance from non-visual data
- **Derive** new inheritance patterns from context
- **Create** new visual facts from behavior
- **Modify** Visual Authority without explicit decision
- **Override** canonical appearance definitions

---

## Consequences

### For Visual Implementation

1. **Separation from Genealogy:** Visual files must not define family relationships
2. **Reference-Only Genealogy:** Visual definitions reference Family Authority for parent context
3. **Inheritance Rules:** Visual Authority owns how appearance passes to children

### For Family Authority Layer

1. **No Visual Override:** Family Layer cannot redefine character appearance
2. **Query Interface:** Family Layer provides genealogy; Visual Layer consumes it

### For Character Authority Layer

1. **Visual Reference:** Character Layer references Visual Authority for appearance
2. **No Appearance Definition:** Character Layer owns identity; Visual Layer owns appearance

### For Canon Recovery Workflow

- Any historical archive data contradicting Visual Authority must be escalated
- Visual conflicts require explicit ADR decision
- No automatic resolution of visual contradictions

---

## Authority

Established by: Visual Authority & Architecture Review  
Approved by: Runtime Validation  
Supersedes: All legacy visual definition workflows  
Depends on: ADR-000, ADR-001, ADR-002, ADR-003
