# Marriages — Database Record

---

## Migration Metadata

| Field | Value |
|-------|-------|
| Source | old_template_and_source/family/Marriages.md (decommissioned) |
| Authority | Family Authority |
| Migration Date | 2026-06-08 |
| Status | Migrated |

---

## Purpose

This document defines all canonical marriage and union relationships for the Los Angeles Dynasty. These are **explicit authority records** — immutable facts that establish family units.

---

## Relationship Type Definition

### Marriage / Dynastic Union

**Definition:** A legal or recognized union between two individuals that creates a joint family unit.

**Canonical Properties:**
- Establishes new lineage for children
- Creates in-law relationships
- May be superseded by Former Marriage (divorce, annulment, death)
- Single source: Family Authority
- Direction: Bidirectional (A ↔ B)

---

## Canonical Records

### Active Marriages

| ID | Partner A | Partner B | Type | Date | Authority |
|----|-----------|-----------|------|------|-----------|
| MR-001 | Erik Douglas | Nixara Bloodmoon | Dynastic Union | [Unspecified] | ADR-001 |

**Note:** The Erik Douglas + Nixara Bloodmoon union is the foundational dynastic merge for the Los Angeles Dynasty.

### Former Marriages

| ID | Partner A | Partner B | Type | End Reason | Authority |
|----|-----------|-----------|------|------------|-----------|
| — | [None documented] | — | — | — | — |

**Note:** No former marriages are currently documented for the Los Angeles Dynasty canonical baseline.

---

## Union Details

### MR-001: Douglas-Bloodmoon Union

| Property | Value |
|----------|-------|
| Type | Dynastic Union |
| Partner A | Erik Douglas (Douglas Dynasty) |
| Partner B | Nixara Bloodmoon (Bloodmoon Dynasty) |
| Result | Douglas-Bloodmoon Line |
| Heirs | Malachia, Noah, Jasper, Alyssa |
| Surname Rule | Hyphenated "Douglas-Bloodmoon" (mandatory for first gen) |
| Status | Active |

**Architectural Significance:**

This union represents the merge of two distinct dynasties:
- Douglas Dynasty (England → America, 1700s)
- Bloodmoon Dynasty (Iceland → America, post-1930)

The union creates a new dynasty branch while preserving the distinct root dynasties.

---

## In-Law Relationships

### Derived from MR-001

| In-Law | Relation To | Derived From |
|--------|-------------|--------------|
| Erik Douglas | Wulfnic Bloodmoon (father-in-law) | MR-001 + PC-001 |
| Nixara Bloodmoon | [Douglas in-laws] | MR-001 + [Douglas family records] |

**Note:** In-law relationships are derived from marriage + parent-child edges. They are not stored as independent canon.

---

## Constraints

1. **Distinct Dynasties:** A dynastic union must merge two distinct family lines
2. **No Incestuous Merge:** Partners in a dynastic union must have no blood relation
3. **Surname Authority:** Marriage creates surname rules for children (see [F_Surname_Authority.md](./F_Surname_Authority.md))
4. **Immutability:** Once established, marriage records do not change (status may change to "former")

---

## Prohibited Relationships

**EXPLICITLY REJECTED:**

| Partner A | Partner B | Reason | Status |
|-----------|-----------|--------|--------|
| Wulfnic Bloodmoon | Erik Douglas (as father-son) | Would make union incestuous | REJECTED |

**Rationale:** If Wulfnic were Erik's father, the Erik + Nixara union would be between half-siblings (Nixara being Wulfnic's daughter). This destroys the concept of "dynastic union."

---

## Query Interface

### Valid Queries

```
getSpouse(person) → Person | null
getMarriage(id) → Marriage
getActiveMarriages() → [Marriage]
getFormerMarriages() → [Marriage]
```

### Derived Queries

```
getInLaws(person) → [Person]  // Derived from spouse + parent-child
```

---

## Authority

Established by: ADR-001, ADR-002
Record custodian: Family Authority Layer
Last validated: 2026-06-07
Migrated: 2026-06-08
