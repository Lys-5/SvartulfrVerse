# ADR-003: Character Authority Layer — Identity Ownership Boundaries

**Status:** ACCEPTED  
**Date:** 2026-06-07  
**Title:** Character Layer Authority and Cross-Layer Ownership Prohibition

## Context

ADR-000 established the runtime baseline and canonical stabilization requirement. ADR-001 formalized dynastic origins. ADR-002 defined the Family Authority Layer as sole custodian of genealogical data.

Before any character data can be imported or character systems implemented, the Character Authority Layer must be formally defined. This layer must unambiguously own all identity data while respecting the authority boundaries established by ADR-001 and ADR-002.

## Decision

We establish the Character Authority Layer as the sole canonical source for all identity, personality, and intrinsic character data within SvartulfrVerse.

### Scope

- **Only Human** (no supernatural identity elements)
- **Contemporary** (2020s-2030s timeline)
- **Los Angeles Dynasty** (geographic and familial focus)

### Character Authority Layer Definition

**Character Layer is the sole owner and canonical custodian of:**

1. **Identity** — Name, pronouns, core self-conception
2. **Personality** — Temperament, behavioral tendencies, psychological profile
3. **Biography** — Personal history, formative experiences, memories
4. **Physical Sex** — Biological sex characteristics (immutable baseline)
5. **Skills** — Learned competencies, education, training
6. **Occupation** — Professional identity and career path (baseline only)
7. **Core Relationships** — Significant personal bonds (baseline only)

**Character Layer constraints:**

- **Identity Custodian** — Owns who the character IS, not how they relate genealogically
- **Immutable Core** — Core identity does not change across scenarios
- **Single Source of Truth** — All identity flows from Character Authority; no distributed identity
- **Authority-Driven** — Decisions governed by explicit ADR, not by archive or inference

---

## Canonical Ownership Model

### Character Layer Owns

| Domain | Description | Mutability |
|--------|-------------|------------|
| Identity | Name, pronouns, self-conception | Immutable |
| Personality | Temperament, behavioral baseline | Immutable |
| Biography | Personal history, memories | Append-only |
| Physical Sex | Biological characteristics | Immutable |
| Skills | Competencies, education | Append-only |
| Occupation | Professional identity (baseline) | Scenario-overrideable |
| Core Relationships | Significant bonds (baseline) | Scenario-extendable |

### Family Layer Owns (ADR-002)

| Domain | Description | Character Layer Access |
|--------|-------------|------------------------|
| Genealogy | Parent-child descent | Read-only query |
| Kinship | Family relationships | Read-only query |
| Lineage | Dynastic lines | Read-only query |
| Surname | Family naming authority | Read-only reference |

### World Layer Owns

| Domain | Description | Character Layer Access |
|--------|-------------|------------------------|
| Setting | Geographic context | Read-only reference |
| Environment | Physical world state | Read-only reference |
| Culture | Societal norms | Read-only reference |

### Experience Layer Owns

| Domain | Description | Character Layer Access |
|--------|-------------|------------------------|
| Scenario | Narrative framing | Read-only reference |
| Context | Situational state | Read-only reference |
| Role | Scenario-specific function | Read-only reference |

---

## Cross-Authority Ownership Prohibition

### EXPLICIT PROHIBITIONS

**Character Layer MAY NOT:**

1. **Define Genealogy** — Parent-child relationships belong to Family Authority
2. **Assign Surname Authority** — Surname rules belong to Family Authority
3. **Create Dynasty Membership** — Dynasty assignment belongs to Family Authority
4. **Override World Setting** — Geographic/temporal context belongs to World Layer
5. **Define Scenario Framing** — Narrative context belongs to Experience Layer

**Family Layer MAY NOT:**

1. **Define Personality** — Behavioral traits belong to Character Layer
2. **Assign Occupation** — Professional identity belongs to Character Layer (baseline)
3. **Create Biography** — Personal history belongs to Character Layer
4. **Override Identity** — Name and self-conception belong to Character Layer

**World Layer MAY NOT:**

1. **Define Identity** — Character self belongs to Character Layer
2. **Create Genealogy** — Family structure belongs to Family Authority
3. **Assign Personality** — Behavioral traits belong to Character Layer

**Experience Layer MAY NOT:**

1. **Redefine Identity** — Core self belongs to Character Layer
2. **Redefine Genealogy** — Family structure belongs to Family Authority
3. **Create New Canon** — Experience is consumer, not owner

---

## Authority Boundary Matrix

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AUTHORITY BOUNDARY MATRIX                        │
├─────────────────┬──────────────┬─────────────┬──────────────────────┤
│ Domain          │ Owner        │ Consumers   │ Override Allowed?   │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Identity        │ Character    │ All         │ NO                   │
│ Personality     │ Character    │ All         │ NO                   │
│ Biography       │ Character    │ All         │ NO (append-only)     │
│ Physical Sex    │ Character    │ All         │ NO                   │
│ Skills          │ Character    │ All         │ NO (append-only)     │
│ Occupation      │ Character    │ Experience  │ YES (scenario)       │
│ Core Relations  │ Character    │ Experience  │ YES (extend)         │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Genealogy       │ Family       │ All         │ NO                   │
│ Kinship         │ Family       │ All         │ NO                   │
│ Lineage         │ Family       │ All         │ NO                   │
│ Surname         │ Family       │ All         │ NO                   │
│ Dynasty         │ Family       │ All         │ NO                   │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Setting         │ World        │ All         │ NO                   │
│ Environment     │ World        │ All         │ NO                   │
│ Culture         │ World        │ All         │ NO                   │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Scenario        │ Experience   │ Runtime     │ N/A (owns)           │
│ Context         │ Experience   │ Runtime     │ N/A (owns)           │
│ Role            │ Experience   │ Runtime     │ N/A (owns)           │
└─────────────────┴──────────────┴─────────────┴──────────────────────┘
```

---

## Character Identity Authority Records

### Canonical Identity Elements

The following identity elements are explicitly stored as canonical character authority records. Each represents a binding identity fact that may be referenced but never redefined by other layers.

#### Name

**Definition:** The character's canonical name as established by Character Authority.

**Canonical Properties:**
- Immutable once established
- Single source: Character Layer
- Family Layer provides surname rules; Character Layer owns full name
- Example: "Alyssa Douglas-Bloodmoon"

#### Pronouns

**Definition:** The character's pronoun preference.

**Canonical Properties:**
- Immutable once established
- Single source: Character Layer
- Example: "she/her"

#### Physical Sex

**Definition:** Biological sex characteristics as baseline physical reality.

**Canonical Properties:**
- Immutable once established
- Single source: Character Layer
- Distinct from gender identity (personality domain)
- Example: "female"

#### Personality Baseline

**Definition:** Core temperament and behavioral tendencies.

**Canonical Properties:**
- Immutable baseline
- Single source: Character Layer
- Experience Layer may express different facets; cannot redefine core
- Example: "Introverted, analytical, fiercely loyal"

#### Biography Summary

**Definition:** Canonical personal history and formative experiences.

**Canonical Properties:**
- Append-only (new experiences may be added)
- Single source: Character Layer
- Experience Layer may reference; cannot contradict
- Example: "Born in Los Angeles, raised in Douglas-Bloodmoon household"

---

## Derived Identity Elements

The following identity elements are **NEVER stored as independent canon**. They are derived from explicit authority records or computed at runtime.

#### Full Legal Name

**Derived from:** Character name + Family surname authority

**Constraint:** Must be computed from Character name and Family surname rules.

#### Age

**Derived from:** Birth date (biography) + Current scenario date

**Constraint:** Must be computed at runtime; not stored as static fact.

#### Family Role

**Derived from:** Genealogy (Family Authority) + Character identity

**Constraint:** Family Authority provides position; Character Layer provides identity context.

---

## Inference Policy

**EXPLICITLY PROHIBITED:** Runtime inference of new identity facts.

### What the Runtime MAY Do

- **Query** Character Authority records
- **Reference** identity data for behavioral context
- **Validate** claimed identity against authority records
- **Return** read-only identity data to other layers
- **Log** identity queries for audit trail

### What the Runtime MAY NOT Do

- **Infer** identity from non-identity data
- **Derive** new personality traits from behavior
- **Create** new identity facts from context
- **Modify** Character Authority without explicit decision
- **Override** immutable identity elements

---

## Consequences

### For Character Implementation

1. **Identity Separation:** Character files must clearly separate owned identity from referenced family data
2. **No Genealogy in Character Files:** Parent-child relationships must be queries, not stored facts
3. **Surname Reference Only:** Character files reference Family Authority for surname rules

### For Family Authority Layer

1. **No Identity Override:** Family Layer cannot redefine character personality or biography
2. **Query Interface:** Family Layer must provide read-only genealogy queries to Character Layer

### For Experience Layer

1. **Consumer Role:** Experience Layer consumes identity; cannot redefine it
2. **Scenario Override:** Only occupation and relationship extension may be overridden
3. **No Identity Mutation:** Core identity remains immutable across all scenarios

### For Canon Recovery Workflow

- Any historical archive data contradicting Character Authority must be escalated
- Identity conflicts require explicit ADR decision
- No automatic resolution of identity contradictions

---

## Authority

Established by: Character Authority & Architecture Review  
Approved by: Runtime Validation  
Supersedes: All legacy character definition workflows  
Depends on: ADR-000, ADR-001, ADR-002
