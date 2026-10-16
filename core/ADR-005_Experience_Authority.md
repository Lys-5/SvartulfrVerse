# ADR-005: Experience Authority Layer — Scenario Framing Architecture

**Status:** ACCEPTED  
**Date:** 2026-06-07  
**Title:** Experience Authority Layer Definition and Scenario Ownership Model

## Context

ADR-000 established the runtime baseline. ADR-001 formalized dynastic origins. ADR-002 defined Family Authority as sole custodian of genealogy. ADR-003 defined Character Authority as sole custodian of identity. ADR-004 defined Visual Authority as sole custodian of appearance and inheritance.

Experience Layer represents the scenario framing system—the context in which characters exist and interact. This layer must be formally defined to prevent scenario definitions from corrupting canonical authority layers.

## Decision

We establish the Experience Authority Layer as the sole canonical source for all scenario, context, and situational framing data within SvartulfrVerse.

### Scope

- **Only Human** (no supernatural scenario elements)
- **Contemporary** (2024 canonical year)
- **Los Angeles Dynasty** (geographic and familial focus)

### Experience Authority Layer Definition

**Experience Authority Layer is the sole owner and canonical custodian of:**

1. **Scenario Framing** — Narrative context and situational setup
2. **Context State** — Current situation, location, temporal position
3. **Role Assignment** — Character functions within scenario
4. **Relationship Extension** — Scenario-specific relationship additions
5. **Occupation Override** — Scenario-specific professional context

**Experience Authority Layer constraints:**

- **Consumer Role** — Consumes authority layers; does not own them
- **Reference-Only Authority** — May reference but not redefine Character, Family, or Visual authority
- **Scenario-Scoped** — All definitions are scenario-specific, not canonical
- **Authority-Driven** — Decisions governed by explicit ADR, not by archive inference

---

## Canonical Ownership Model

### Experience Layer Owns

| Domain | Description | Scope |
|--------|-------------|-------|
| Scenario | Narrative framing and setup | Scenario-specific |
| Context | Current situation state | Scenario-specific |
| Role | Character function in scenario | Scenario-specific |
| Relationship Extension | Scenario-specific bonds | Scenario-specific |
| Occupation Override | Scenario-specific profession | Scenario-specific |

### Experience Layer References (Read-Only)

| Domain | Owner | Access Type |
|--------|-------|-------------|
| Identity | Character Layer | Read-only reference |
| Personality | Character Layer | Read-only reference |
| Genealogy | Family Layer | Read-only reference |
| Dynasty | Family Layer | Read-only reference |
| Appearance | Visual Layer | Read-only reference |

### Experience Layer MAY NOT Own

| Domain | Reason | Owner |
|--------|--------|-------|
| Identity | Immutable core | Character Layer |
| Genealogy | Immutable canon | Family Layer |
| Dynasty | Immutable canon | Family Layer |
| Appearance | Immutable canon | Visual Layer |
| Personality | Immutable core | Character Layer |

---

## Experience Authority Constraints

### EXPLICIT PROHIBITIONS

**Experience Layer MAY NOT:**

1. **Redefine Character Identity** — Names, pronouns, core self-conception belong to Character Authority
2. **Redefine Genealogy** — Parent-child relationships belong to Family Authority
3. **Redefine Dynasty Membership** — Dynasty assignment belongs to Family Authority
4. **Redefine Appearance** — Visual characteristics belong to Visual Authority
5. **Create New Canon** — Experience is consumer, not owner of canonical truth

### PERMITTED OPERATIONS

**Experience Layer MAY:**

1. **Reference Authority Layers** — Query Character, Family, Visual for context
2. **Extend Relationships** — Add scenario-specific bonds (does not remove canonical bonds)
3. **Override Occupation** — Assign scenario-specific professional role (baseline preserved)
4. **Assign Roles** — Define character function within scenario scope
5. **Set Context** — Establish situational framing (location, time, circumstances)

---

## Authority Boundary Matrix

```
┌─────────────────────────────────────────────────────────────────────┐
│                 EXPERIENCE AUTHORITY BOUNDARY MATRIX                │
├─────────────────┬──────────────┬─────────────┬──────────────────────┤
│ Domain          │ Owner        │ Experience  │ Override Allowed?   │
│                 │              │ Access      │                      │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Identity        │ Character    │ Read-only   │ NO                   │
│ Personality     │ Character    │ Read-only   │ NO                   │
│ Biography       │ Character    │ Read-only   │ NO                   │
│ Physical Sex    │ Character    │ Read-only   │ NO                   │
│ Skills          │ Character    │ Read-only   │ NO                   │
│ Occupation      │ Character    │ Read-only   │ YES (scenario)       │
│ Core Relations  │ Character    │ Read-only   │ EXTEND only          │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Genealogy       │ Family       │ Read-only   │ NO                   │
│ Kinship         │ Family       │ Read-only   │ NO                   │
│ Lineage         │ Family       │ Read-only   │ NO                   │
│ Surname         │ Family       │ Read-only   │ NO                   │
│ Dynasty         │ Family       │ Read-only   │ NO                   │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Appearance      │ Visual       │ Read-only   │ NO                   │
│ Aesthetic       │ Visual       │ Read-only   │ NO                   │
│ Coloration      │ Visual       │ Read-only   │ NO                   │
│ Build           │ Visual       │ Read-only   │ NO                   │
│ Resemblance     │ Visual       │ Read-only   │ NO                   │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Scenario        │ Experience   │ OWN         │ N/A (owns)           │
│ Context         │ Experience   │ OWN         │ N/A (owns)           │
│ Role            │ Experience   │ OWN         │ N/A (owns)           │
│ Ext. Relations  │ Experience   │ OWN         │ N/A (owns)           │
│ Occ. Override   │ Experience   │ OWN         │ N/A (owns)           │
└─────────────────┴──────────────┴─────────────┴──────────────────────┘
```

---

## Experience Authority Records

### Canonical Experience Elements

The following elements are explicitly stored as canonical experience authority records. Each represents a scenario-specific framing that may reference but never redefine authority layers.

#### Scenario

**Definition:** The narrative framing and situational setup for a specific experience.

**Canonical Properties:**
- Scenario-specific (not canonical)
- May reference Character, Family, Visual authority
- Cannot contradict canonical authority
- Example: "Family gathering at Douglas estate for holiday dinner"

#### Context

**Definition:** The current situation state including location, time, and circumstances.

**Canonical Properties:**
- Scenario-specific (not canonical)
- Mutable during experience
- Cannot redefine character identity or genealogy
- Example: "Los Angeles, December 2024, evening, Douglas family home"

#### Role

**Definition:** The function a character serves within the scenario.

**Canonical Properties:**
- Scenario-specific (not canonical)
- May reference but cannot redefine occupation baseline
- Cannot contradict character personality
- Example: "Alyssa serves as mediator between Noah and Malachia"

#### Relationship Extension

**Definition:** Scenario-specific bonds or dynamics added for the experience.

**Canonical Properties:**
- Scenario-specific (not canonical)
- EXTENDS canonical relationships; does not replace
- Cannot remove canonical family bonds
- Example: "In this scenario, Alyssa has a temporary conflict with Jasper"

#### Occupation Override

**Definition:** Scenario-specific professional role that differs from baseline.

**Canonical Properties:**
- Scenario-specific (not canonical)
- Overrides baseline occupation for scenario duration only
- Baseline occupation preserved in Character Authority
- Example: "Noah serves as family representative at corporate event (baseline: student)"

---

## Consumer-Owner Model

### Experience Layer as Consumer

**Definition:** Experience Layer consumes authority layers; it does not own them.

**Consumer Properties:**
- Read-only access to Character, Family, Visual authority
- May reference canonical data for scenario context
- May not modify canonical authority
- All scenario definitions are scoped, not canonical

### Authority Layer Reference Model

```
Experience Layer (Consumer)
    │
    ├──► Character Authority (Owner)
    │         │
    │         ├── Identity (read-only)
    │         ├── Personality (read-only)
    │         ├── Biography (read-only)
    │         ├── Occupation (read-only, overrideable)
    │         └── Core Relations (read-only, extendable)
    │
    ├──► Family Authority (Owner)
    │         │
    │         ├── Genealogy (read-only)
    │         ├── Kinship (read-only)
    │         ├── Dynasty (read-only)
    │         └── Surname (read-only)
    │
    └──► Visual Authority (Owner)
              │
              ├── Appearance (read-only)
              ├── Aesthetic (read-only)
              └── Inheritance (read-only)
```

---

## Cross-Authority Interaction Rules

### Scenario Definition Rules

1. **Identity Preservation:** Scenario must preserve character identity from Character Authority
2. **Genealogy Preservation:** Scenario must preserve family relationships from Family Authority
3. **Appearance Preservation:** Scenario must preserve visual characteristics from Visual Authority
4. **Extension Only:** Scenario may extend relationships; may not remove canonical bonds
5. **Override Scope:** Occupation override is scenario-scoped; baseline preserved

### Conflict Resolution

When scenario definition conflicts with authority layers:

| Conflict Type | Resolution |
|---------------|------------|
| Identity contradiction | REJECT scenario definition |
| Genealogy contradiction | REJECT scenario definition |
| Appearance contradiction | REJECT scenario definition |
| Relationship removal | REJECT (extension only) |
| Occupation override | ACCEPT (scenario-scoped) |
| Relationship extension | ACCEPT (scenario-scoped) |

---

## Inference Policy

**EXPLICITLY PROHIBITED:** Runtime inference of new canonical facts from scenario context.

### What the Runtime MAY Do

- **Query** Experience Authority records for scenario context
- **Reference** Character, Family, Visual authority for canonical data
- **Validate** scenario definitions against authority layers
- **Return** scenario context to runtime systems
- **Log** scenario queries for audit trail

### What the Runtime MAY NOT Do

- **Infer** new canonical facts from scenario behavior
- **Promote** scenario-specific data to canonical authority
- **Override** immutable authority elements
- **Remove** canonical relationships through scenario definition
- **Create** new canon without explicit ADR decision

---

## Consequences

### For Experience Implementation

1. **Consumer Architecture:** Experience systems must be designed as consumers, not owners
2. **Reference Layer:** All canonical data must be queried from authority layers
3. **No Canon Creation:** Experience cannot create new canonical facts

### For Authority Layers

1. **Query Interface:** Authority layers must provide read-only query interfaces
2. **Validation Hooks:** Authority layers may validate scenario definitions
3. **Rejection Authority:** Authority layers may reject contradictory scenarios

### For Canon Recovery Workflow

- Any scenario data contradicting authority layers must be rejected
- Scenario-specific data must not be imported as canonical
- Experience definitions require separate validation from canonical imports

---

## Authority

Established by: Experience Authority & Architecture Review  
Approved by: Runtime Validation  
Supersedes: All legacy scenario definition workflows  
Depends on: ADR-000, ADR-001, ADR-002, ADR-003, ADR-004
