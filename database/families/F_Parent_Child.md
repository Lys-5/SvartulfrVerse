# Parent-Child Relationships — Database Record

---

## Migration Metadata

| Field | Value |
|-------|-------|
| Source | authority/family/Parent_Child.md |
| Authority | Family Authority |
| Migration Date | 2026-06-08 |
| Status | Migrated |

---

## Purpose

This document defines all canonical parent-child relationships for the Los Angeles Dynasty. These are **explicit authority records** — immutable facts that may be queried but never inferred.

---

## Relationship Type Definition

### Parent → Child

**Definition:** A biological or adoptive parent relationship.

**Canonical Properties:**
- Immutable once established
- Creates biologically-derived relationships (siblings, grandparents)
- Cannot be inferred; must be explicitly defined
- Single source: Family Authority
- Direction: Parent → Child (unidirectional)

---

## Canonical Records

### Bloodmoon Line (Pre-Union)

| ID | Parent | Child | Type | Authority |
|----|--------|-------|------|-----------|
| PC-001 | Wulfnic Bloodmoon | Nixara Bloodmoon | Biological | ADR-001 |

### Douglas Line (Pre-Union)

| ID | Parent | Child | Type | Authority |
|----|--------|-------|------|-----------|
| — | [No explicit records] | — | — | — |

**Note:** Douglas line has multiple generations in America but no explicit parent-child records are required for canonical baseline beyond Erik Douglas as union principal.

### Douglas-Bloodmoon Line (First Generation)

| ID | Parent | Child | Type | Authority |
|----|--------|-------|------|-----------|
| PC-002 | Erik Douglas | Malachia Douglas-Bloodmoon | Biological | ADR-001 |
| PC-003 | Erik Douglas | Noah Douglas-Bloodmoon | Biological | ADR-001 |
| PC-004 | Erik Douglas | Jasper Douglas-Bloodmoon | Biological | ADR-001 |
| PC-005 | Erik Douglas | Alyssa Douglas-Bloodmoon | Biological | ADR-001 |
| PC-006 | Nixara Bloodmoon | Malachia Douglas-Bloodmoon | Biological | ADR-001 |
| PC-007 | Nixara Bloodmoon | Noah Douglas-Bloodmoon | Biological | ADR-001 |
| PC-008 | Nixara Bloodmoon | Jasper Douglas-Bloodmoon | Biological | ADR-001 |
| PC-009 | Nixara Bloodmoon | Alyssa Douglas-Bloodmoon | Biological | ADR-001 |

---

## Derived Relationships

The following relationships are **derived** from parent-child records. They are computed at runtime and **never stored as independent canon**.

### Sibling Relationships

| Sibling A | Sibling B | Derived From |
|-----------|-----------|--------------|
| Malachia | Noah | PC-002, PC-003, PC-006, PC-007 |
| Malachia | Jasper | PC-002, PC-004, PC-006, PC-008 |
| Malachia | Alyssa | PC-002, PC-005, PC-006, PC-009 |
| Noah | Jasper | PC-003, PC-004, PC-007, PC-008 |
| Noah | Alyssa | PC-003, PC-005, PC-007, PC-009 |
| Jasper | Alyssa | PC-004, PC-005, PC-008, PC-009 |

### Grandparent Relationships

| Grandparent | Grandchild | Derived From |
|-------------|------------|--------------|
| Wulfnic Bloodmoon | Malachia | PC-001 + PC-006 |
| Wulfnic Bloodmoon | Noah | PC-001 + PC-007 |
| Wulfnic Bloodmoon | Jasper | PC-001 + PC-008 |
| Wulfnic Bloodmoon | Alyssa | PC-001 + PC-009 |

---

## Prohibited Relationships

**EXPLICITLY REJECTED:**

| Parent | Child | Reason | Status |
|--------|-------|--------|--------|
| Wulfnic Bloodmoon | Erik Douglas | Legacy drift | REJECTED |
| Erik Douglas | Wulfnic Bloodmoon | Legacy drift | REJECTED |

**Rationale:** These false relationships would corrupt the dynastic structure. Erik Douglas and Wulfnic Bloodmoon are from separate dynasties with no blood relation.

---

## Query Interface

### Valid Queries

```
getParents(child) → [Parent]
getChildren(parent) → [Child]
hasParent(child, parent) → Boolean
hasChild(parent, child) → Boolean
```

### Derived Queries

```
getSiblings(node) → [Sibling]  // Derived from shared parents
getGrandparents(node) → [Grandparent]  // Derived from parent → parent
getGrandchildren(node) → [Grandchild]  // Derived from child → child
```

---

## Constraints

1. **Immutability:** Once established, parent-child relationships do not change
2. **No Inference:** Runtime may not infer new parent-child relationships
3. **Single Source:** All parent-child data flows from this record
4. **Validation Required:** Any historical archive data contradicting these records must be escalated

---

## Cross-References

- [F_Douglas_Bloodmoon.md](./F_Douglas_Bloodmoon.md) — Graph structure
- [F_Marriages.md](./F_Marriages.md) — Marriage records
- [F_Surname_Authority.md](./F_Surname_Authority.md) — Naming conventions

---

## Authority

Established by: ADR-001, ADR-002
Record custodian: Family Authority Layer
Last validated: 2026-06-07
Migrated: 2026-06-08
