# Families Domain

## Purpose

Repository for canonical family/genealogy records.

## Authority

Family Authority (ADR-002)

## Allowed Content

- Approved family records
- Family templates
- Genealogy structures

## Forbidden Content

- Unapproved families
- Legacy imports without audit
- Inferred relationships
- Contradictory genealogies

## Relationships

- Referenced by: characters/
- Referenced by: institutions/

## Domain Status

| Status | Value |
|--------|-------|
| Phase | Canon Freeze v1 |
| Status | COMPLETE |
| Date | 2026-06-08 |
| Records | 4 |

## Records

| Record | Description | Status |
|--------|-------------|--------|
| F_Douglas_Bloodmoon.md | Dynastic union structure | ✓ ACTIVE |
| F_Marriages.md | Marriage records | ✓ ACTIVE |
| F_Parent_Child.md | Parent-child relationships | ✓ ACTIVE |
| F_Surname_Authority.md | Surname governance rules | ✓ ACTIVE |

## Canonical Family Graph

```text
Wulfnic Bloodmoon (1948) ←→ Nixara Bloodmoon (1975-2005)
                                ↓
Erik Douglas (1970) ←→ Nixara Bloodmoon
                                ↓
                ┌───────────────┼───────────────┐
                ↓               ↓               ↓
          Malachia (1996)   Noah (1999)   Jasper (2005)
                                              ↓
                                          Alyssa (2005)
                                              ↓
                Logan Douglas → Edric Douglas (2018)
```

## Validation Status

| Check | Result |
|-------|--------|
| Family Graph Consistency | ✓ PASS |
| Surname Authority Consistency | ✓ PASS |
| Parent-Child Consistency | ✓ PASS |
| Marriage Consistency | ✓ PASS |
| Unresolved References | ✓ NONE |
| No Canon Conflicts | ✓ PASS |

## Canon Layer Compliance

All 4 records are classified as **Active Canon (Layer 1)** per ADR-006.

---

**Last Updated:** 2026-06-08  
**Canon Freeze:** v1.0
