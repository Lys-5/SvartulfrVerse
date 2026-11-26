---
alwaysApply: false
description: Apply when creating, modifying, auditing, validating, or discussing family relationships, genealogy, parent-child structures, marriages, and family authority.
---
# R-002: Family Rules

**Authority:** ADR-002_Family_Authority.md  
**Type:** Operational Rule  
**Date:** 2026-06-07

---

## R-002-FAM-001: Genealogy Ownership

### Authority
ADR-002

### Rule
Family Authority Layer is the sole owner of all genealogical data.

### Rationale
Genealogy is a knowledge layer, not a behavior engine. All parent-child relationships, marriages, and kinship data belong exclusively to Family Authority.

### Allowed
- Storing genealogy in `database/families/`
- Querying Family Authority for relationships
- Single source of truth for family data

### Prohibited
- Storing genealogy in character files
- Computing relationships outside Family Authority
- Duplicating family data in other layers

---

## R-002-FAM-002: Explicit Relationships

### Authority
ADR-002

### Rule
Only explicitly defined parent-child and marriage relationships are canonical.

### Rationale
Derived relationships (siblings, grandparents, cousins) are computed at runtime. Only explicit edges are stored.

### Allowed
- Defining parent → child relationships
- Defining marriage relationships
- Querying derived relationships at runtime

### Prohibited
- Storing sibling relationships directly
- Storing grandparent relationships directly
- Storing cousin relationships directly

---

## R-002-FAM-003: Derived Relationships

### Authority
ADR-002

### Rule
Sibling, grandparent, and cousin relationships are derived, not stored.

### Rationale
Derived relationships must be computed from explicit parent-child edges. Storing them creates maintenance burden and drift risk.

### Allowed
- Computing siblings from shared parents
- Computing grandparents from parent chains
- Computing cousins from parent-sibling chains

### Prohibited
- Storing sibling as independent fact
- Storing grandparent as independent fact
- Treating derived relationships as canonical

---

## R-002-FAM-004: Knowledge Layer Only

### Authority
ADR-002, Architecture.md

### Rule
Family Authority contains NO behavioral logic.

### Rationale
Family Authority is a knowledge layer. It provides data, not behavior. No relationship computation, no state management, no simulation.

### Allowed
- Storing genealogy facts
- Providing query interfaces
- Returning canonical family data

### Prohibited
- Relationship computation logic
- State management
- Behavior simulation
- Character generation

---

## R-002-FAM-005: No Genealogy Duplication

### Authority
ADR-002, Architecture.md

### Rule
Genealogy must not be duplicated outside Family Authority.

### Rationale
Duplication creates sync burden and drift risk. Character files reference genealogy; they do not own it.

### Allowed
- Character files referencing family relationships (read-only)
- Querying Family Authority for kinship
- Single storage location for genealogy

### Prohibited
- Storing parent-child in character files
- Duplicating family data in world layer
- Parallel genealogy documentation

---

## R-002-FAM-006: Family Graph Structure

### Authority
ADR-002

### Rule
Family relationships form a directed graph with explicit edges only.

### Rationale
Graph structure enables efficient queries while preventing drift. Only explicit edges are canonical.

### Allowed
- Parent → child directed edges
- Marriage bidirectional edges
- Graph traversal for derived relationships

### Prohibited
- Undirected parent-child edges
- Storing derived relationships as edges
- Circular family structures

---

## R-002-FAM-007: Dynasty Membership

### Authority
ADR-002

### Rule
Dynasty membership is defined by Family Authority, not character files.

### Rationale
Dynasty is a genealogical property. Character files reference dynasty membership; they do not define it.

### Allowed
- Family Authority defining dynasty membership
- Character files referencing dynasty (read-only)
- Querying dynasty membership

### Prohibited
- Character files defining dynasty
- Multiple dynasty membership sources
- Dynasty assignment outside Family Authority

---

## R-002-FAM-008: Surname Authority

### Authority
ADR-002

### Rule
Surname rules are owned by Family Authority.

### Rationale
Surname inheritance is a genealogical property. Family Authority defines surname rules; characters reference their surname.

### Allowed
- Family Authority defining surname rules
- Character files referencing surname (read-only)
- Hyphenated surname mandate for first generation

### Prohibited
- Character files defining surname rules
- Alternative surname conventions without ADR
- Surname drift in character documentation

---

## Summary

| Rule ID | Description |
|---------|-------------|
| R-002-FAM-001 | Genealogy Ownership |
| R-002-FAM-002 | Explicit Relationships |
| R-002-FAM-003 | Derived Relationships |
| R-002-FAM-004 | Knowledge Layer Only |
| R-002-FAM-005 | No Genealogy Duplication |
| R-002-FAM-006 | Family Graph Structure |
| R-002-FAM-007 | Dynasty Membership |
| R-002-FAM-008 | Surname Authority |
