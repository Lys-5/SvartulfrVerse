# Visual Inheritance Rules — Database Record

---

## Migration Metadata

| Field | Value |
|-------|-------|
| Source | old_template_and_source/visual/Inheritance_Rules.md (decommissioned) |
| Authority | Visual Authority |
| Migration Date | 2026-06-08 |
| Status | Migrated |

---

## Purpose

This document defines how visual characteristics pass from parents to children in the Los Angeles Dynasty. These rules are **visual authority only** and do not affect genealogical authority.

---

## Visual Fusion Model

### Definition

The Visual Fusion Model defines how children of the Douglas-Bloodmoon union inherit visual characteristics from both dynasties.

### Core Principle

**Visual inheritance ≠ Genealogical inheritance**

- Genealogy defines WHO is parent to WHOM
- Visual inheritance defines WHAT characteristics pass from parent to child
- These are separate authority domains

---

## Visual DNA Baselines

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

## Inheritance Authority Records

### Canonical Inheritance Patterns

| Pattern | Definition | Example |
|---------|------------|---------|
| Douglas-visual-dominant | Black hair, amber eyes, massive build | Malachia |
| Bloodmoon-visual-dominant | Blonde hair, blue eyes, lean build | Noah |
| Fusion-visual | Blended characteristics from both dynasties | Alyssa, Jasper |
| Maternal-resemblance | Strongest facial/body resemblance to mother | Alyssa |

### Exception Handling

- **Alyssa:** Fusion-visual with maternal-resemblance pattern
- **Noah:** Bloodmoon-visual-dominant despite Douglas genealogy
- These are **visual inheritance patterns** that do not affect genealogy

---

## Query Interface

### Valid Queries

```
getInheritance(child) → InheritanceRecord
getResemblance(child) → Parent
getVisualDominance(child) → Dynasty
validateInheritance(child, attributes) → Boolean
```

### Invalid Operations

```
setInheritance(child, parent)  // PROHIBITED — requires ADR
modifyInheritanceRule()         // PROHIBITED — requires ADR
```

---

## Authority

Established by: ADR-004
Record custodian: Visual Authority Layer
Last validated: 2026-06-07
Migrated: 2026-06-08
