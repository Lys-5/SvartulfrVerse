---
alwaysApply: false
description: Apply when discussing appearance, visual identity, inheritance, physical traits, character design, visual recovery audits, or Douglas-Bloodmoon visual fusion rules.
---
# R-004: Visual Rules

**Authority:** ADR-004_Visual_Authority.md  
**Type:** Operational Rule  
**Date:** 2026-06-07

---

## R-004-VIS-001: Douglas Visual Baseline

### Authority
ADR-004

### Rule
Douglas Dynasty visual baseline is: black hair, amber eyes, massive muscular build.

### Rationale
Recovered canon establishes Douglas visual DNA. All Douglas-line characters reference this baseline.

### Allowed
- Black hair (may silver with age)
- Amber eyes
- Massive, muscular build
- Corporate monarch aesthetic

### Prohibited
- Blonde hair for Douglas baseline
- Blue eyes for Douglas baseline
- Lean build for Douglas baseline
- Alternative aesthetic baselines

---

## R-004-VIS-002: Bloodmoon Visual Baseline

### Authority
ADR-004

### Rule
Bloodmoon Dynasty visual baseline is: blonde hair, blue eyes, lean refined build.

### Rationale
Recovered canon establishes Bloodmoon visual DNA. All Bloodmoon-line characters reference this baseline.

### Allowed
- Blonde hair
- Blue eyes
- Lean, refined build
- Ancestral nobility aesthetic

### Prohibited
- Black hair for Bloodmoon baseline
- Amber eyes for Bloodmoon baseline
- Massive build for Bloodmoon baseline
- Alternative aesthetic baselines

---

## R-004-VIS-003: Visual Fusion Model

### Authority
ADR-004

### Rule
Children of Douglas + Bloodmoon union inherit according to Visual Fusion Model, not dominant/recessive genetics.

### Rationale
Visual inheritance follows fusion patterns, not genetic probability. Each child expresses a specific fusion result.

### Allowed
- Douglas-visual-dominant (black hair, amber eyes)
- Bloodmoon-visual-dominant (blonde hair, blue eyes)
- Fusion-visual (blended characteristics)

### Prohibited
- Probability-based inheritance (75%/25%)
- Dominant/recessive terminology
- Genetic model assumptions

---

## R-004-VIS-004: Malachia Visual Inheritance

### Authority
ADR-004

### Rule
Malachia Douglas-Bloodmoon expresses Douglas-visual-dominant inheritance: black hair, amber eyes.

### Rationale
Malachia shows strongest Douglas coloration expression. This is a visual inheritance pattern, not a genealogical property.

### Allowed
- Black hair
- Amber eyes
- Tank-like build
- Douglas-visual-dominant classification

### Prohibited
- Blonde hair for Malachia
- Blue eyes for Malachia
- Alternative visual classifications

---

## R-004-VIS-005: Noah Visual Inheritance

### Authority
ADR-004

### Rule
Noah Douglas-Bloodmoon expresses Bloodmoon-visual-dominant inheritance: blonde hair, blue eyes.

### Rationale
Noah shows strongest Bloodmoon coloration expression. This is a visual inheritance pattern, not a genealogical property.

### Allowed
- Blonde hair
- Blue eyes
- Lithe elegant build
- Bloodmoon-visual-dominant classification

### Prohibited
- Black hair for Noah
- Amber eyes for Noah
- Alternative visual classifications

---

## R-004-VIS-006: Alyssa Visual Inheritance

### Authority
ADR-004

### Rule
Alyssa Douglas-Bloodmoon expresses fusion-visual inheritance with maternal resemblance: caramel-brown hair, mint-green eyes, Nixara facial/body structure.

### Rationale
Alyssa shows fusion blend plus strongest maternal resemblance. This is a visual inheritance pattern, not a genealogical property.

### Allowed
- Caramel-brown hair
- Mint-green eyes
- Petite hourglass build
- Nixara facial resemblance
- Fusion-visual with maternal-resemblance classification

### Prohibited
- Pure Douglas or Bloodmoon coloration
- Alternative visual classifications
- Ignoring maternal resemblance pattern

---

## R-004-VIS-007: Jasper Visual Inheritance

### Authority
ADR-004

### Rule
Jasper Douglas-Bloodmoon expresses fusion-visual inheritance as Alyssa's twin: caramel-brown hair, mint-green eyes.

### Rationale
Jasper and Alyssa share identical fusion inheritance as twins. Build and aesthetic differ by character development.

### Allowed
- Caramel-brown hair (twin match)
- Mint-green eyes (twin match)
- Lean athletic build
- Fusion-visual (twin) classification

### Prohibited
- Different coloration from Alyssa
- Alternative visual classifications
- Ignoring twin inheritance pattern

---

## R-004-VIS-008: Visual Authority Independence

### Authority
ADR-004

### Rule
Visual Authority is independent from Family Authority.

### Rationale
Visual inheritance ≠ genealogical inheritance. Genealogy defines WHO is parent to WHOM. Visual defines WHAT characteristics pass from parent to child. These are separate authority domains.

### Allowed
- Visual Authority defining appearance
- Family Authority defining genealogy
- Cross-reference between authorities

### Prohibited
- Visual Authority defining genealogy
- Family Authority defining appearance
- Conflating visual and genealogical inheritance

---

## R-004-VIS-009: Appearance Ownership

### Authority
ADR-004

### Rule
Visual Authority owns all appearance data.

### Rationale
Appearance is a visual domain. Character files reference appearance; they do not own appearance authority.

### Allowed
- Visual Authority defining appearance baseline
- Character files referencing appearance (read-only)
- Querying visual characteristics

### Prohibited
- Character files defining appearance baseline
- Other layers modifying visual inheritance
- Appearance ownership outside Visual Authority

---

## R-004-VIS-010: No Appearance in Character Files

### Authority
ADR-004, Architecture.md

### Rule
Character files must NOT define appearance baseline.

### Rationale
Appearance belongs to Visual Authority. Character files reference appearance; they do not own it.

### Allowed
- Character files referencing appearance (read-only)
- Querying Visual Authority for characteristics
- Single source of truth for appearance

### Prohibited
- Storing appearance baseline in character files
- Defining visual inheritance in character files
- Duplicating appearance data

---

## Summary

| Rule ID | Description |
|---------|-------------|
| R-004-VIS-001 | Douglas Visual Baseline |
| R-004-VIS-002 | Bloodmoon Visual Baseline |
| R-004-VIS-003 | Visual Fusion Model |
| R-004-VIS-004 | Malachia Visual Inheritance |
| R-004-VIS-005 | Noah Visual Inheritance |
| R-004-VIS-006 | Alyssa Visual Inheritance |
| R-004-VIS-007 | Jasper Visual Inheritance |
| R-004-VIS-008 | Visual Authority Independence |
| R-004-VIS-009 | Appearance Ownership |
| R-004-VIS-010 | No Appearance in Character Files |
