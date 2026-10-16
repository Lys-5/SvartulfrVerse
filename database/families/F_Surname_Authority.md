# Surname Authority — Database Record

---

## Migration Metadata

| Field | Value |
|-------|-------|
| Source | authority/family/Surname_Authority.md |
| Authority | Family Authority |
| Migration Date | 2026-06-08 |
| Status | Migrated |

---

## Purpose

This document defines all canonical surname rules and naming conventions for the Los Angeles Dynasty. Surname authority belongs exclusively to the Family Authority Layer.

---

## Authority Definition

**Family Authority Layer owns surname authority:**

1. **Surname Assignment** — Which surname a person carries
2. **Surname Inheritance** — How surnames pass to children
3. **Surname Modification** — Hyphenation, compound names
4. **Surname Validation** — Checking surname correctness

**Constraints:**
- Character Layer may not define surname rules
- Experience Layer may not modify surname rules
- Surname rules are immutable once established

---

## Surname Registry

### Dynasty Surnames

| Dynasty | Surname | Inheritance | Status |
|---------|---------|-------------|--------|
| Douglas | Douglas | Patrilineal (default) | Active |
| Bloodmoon | Bloodmoon | Patrilineal (default) | Active |
| Douglas-Bloodmoon | Douglas-Bloodmoon | Exception (hyphenated) | Active |

### Hyphenated Surname Exception

**Rule:** The Douglas-Bloodmoon hyphenated surname is an **exceptional dynastic designation** for the first generation heirs of the Erik + Nixara union.

**Mandate:**

| Person | Surname | Type | Authority |
|--------|---------|------|-----------|
| Malachia | Douglas-Bloodmoon | Hyphenated (mandatory) | ADR-001 |
| Noah | Douglas-Bloodmoon | Hyphenated (mandatory) | ADR-001 |
| Jasper | Douglas-Bloodmoon | Hyphenated (mandatory) | ADR-001 |
| Alyssa | Douglas-Bloodmoon | Hyphenated (mandatory) | ADR-001 |

**Constraints:**
- Hyphenated surname is **non-negotiable** for first generation
- Hyphenated surname is **NOT automatically hereditary**
- Second-generation inheritance rules are **unresolved** (pending future ADR)

---

## Inheritance Rules

### Default Rule: Patrilineal

```
Father's surname → Children's surname
```

**Applies to:**
- Douglas Dynasty (default)
- Bloodmoon Dynasty (default)

### Exception Rule: Hyphenated Union

```
Union of two dynasties → Hyphenated surname for first generation
```

**Applies to:**
- Douglas-Bloodmoon Line (exception)

### Unresolved Rules

| Scenario | Status | Notes |
|----------|--------|-------|
| Second generation inheritance | PENDING | Requires future ADR |
| Marriage into Douglas-Bloodmoon | PENDING | Requires future ADR |
| Adoption scenarios | PENDING | Requires future ADR |

---

## Surname Validation

### Valid Surnames

| Person | Expected Surname | Validation |
|--------|------------------|------------|
| Erik | Douglas | ✓ Valid |
| Nixara | Bloodmoon | ✓ Valid |
| Wulfnic | Bloodmoon | ✓ Valid |
| Malachia | Douglas-Bloodmoon | ✓ Valid |
| Noah | Douglas-Bloodmoon | ✓ Valid |
| Jasper | Douglas-Bloodmoon | ✓ Valid |
| Alyssa | Douglas-Bloodmoon | ✓ Valid |

### Invalid Surnames

| Person | Invalid Surname | Reason |
|--------|-----------------|--------|
| Malachia | Douglas | Missing Bloodmoon |
| Malachia | Bloodmoon | Missing Douglas |
| Noah | Douglas | Missing Bloodmoon |
| Alyssa | Bloodmoon | Missing Douglas |

---

## Query Interface

### Valid Queries

```
getSurname(person) → String
validateSurname(person, surname) → Boolean
getDynastyFromSurname(surname) → Dynasty
getSurnameRule(dynasty) → Rule
```

### Invalid Operations

```
setSurname(person, surname)  // PROHIBITED — requires ADR
modifySurnameRule(dynasty)    // PROHIBITED — requires ADR
```

---

## Authority

Established by: ADR-001, ADR-002
Record custodian: Family Authority Layer
Last validated: 2026-06-07
Migrated: 2026-06-08
