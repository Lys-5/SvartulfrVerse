# Deferred Canon Policy

**Status:** CANONICAL  
**Date:** 2026-06-07  
**Type:** Repository Operating Policy  
**Authority:** Architecture Review

---

## Purpose

This document formalizes the distinction between three canon categories:

1. **Active Canon** — Information currently allowed inside runtime compilation
2. **Deferred Canon** — Canonically existing entities not currently compiled into runtime
3. **Archive Canon** — Historical material retained solely for research

The purpose is to preserve architectural simplicity while retaining future expansion paths.

---

## Definitions

### Active Canon

**Definition:** Information currently allowed inside runtime compilation.

**Properties:**
- Resides in `database/` (Single Source of Truth)
- May appear in active character records
- May appear in active scenarios
- Subject to all governance rules

**Current Baseline:**

| Character | Dynasty | Status |
|-----------|---------|--------|
| Wulfnic Bloodmoon | Bloodmoon | Active |
| Nixara Bloodmoon | Bloodmoon | Active |
| Erik Douglas | Douglas | Active |
| Logan Douglas | Douglas | Active |
| Malachia Douglas-Bloodmoon | Douglas-Bloodmoon | Active |
| Noah Douglas-Bloodmoon | Douglas-Bloodmoon | Active |
| Jasper Douglas-Bloodmoon | Douglas-Bloodmoon | Active |
| Alyssa Douglas-Bloodmoon | Douglas-Bloodmoon | Active |

---

### Deferred Canon

**Definition:** Canonically existing entities that are not currently compiled into runtime.

**Purpose:** Preserve architectural simplicity while retaining future expansion paths.

**Properties:**

| Property | Status |
|----------|--------|
| Exists historically | ✓ Allowed |
| Possesses recovery audits | ✓ Allowed |
| Possesses genealogy | ✓ Allowed |
| Participates in active runtime | ✗ Prohibited |
| Appears in active family compilation | ✗ Prohibited |
| Appears in active scenarios | ✗ Prohibited |

**Current Deferred Canon:**

#### Rejected Canon — Political Wives

| Name | Status | Notes |
|------|--------|-------|
| Sigrid | **REJECTED** | Political wife concept — incompatible with canonical family structure. No evidence in Active or Historical Canon. |
| Dagmar | **REJECTED** | Political wife concept — incompatible with canonical family structure. No evidence in Active or Historical Canon. |
| Valeria | **REJECTED** | WetNurse/Concubine concept — conflicts with canonical family graph; introduces non-canonical character and "Myrick" name for Jasper. Source: Progetti/docs/canon/CANON_003. Decision: 2026-06-08. |

#### Rejected Canon — Extended Lines

| Name | Status | Notes |
|------|--------|-------|
| Gunnar | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Ingrid | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Astrid II | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Torvald | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Hagen | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Sigrun | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Bram | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Knut | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Lars | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Sven | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Valerius | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Thyra | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |

---

### Archive Canon

**Definition:** Historical material retained solely for research.

**Properties:**

| Property | Status |
|----------|--------|
| Research source | ✓ Allowed |
| Evidence for recovery | ✓ Allowed |
| Runtime authority | ✗ None |
| Import authority | ✗ None |

**Research Archives:**

| Source | Role |
|--------|------|
| NotebookLM | Primary Research Archive — evidence source only |
| Progetti archive | Research Archive — evidence source only |
| Historical reports | Supporting evidence |

Research archives are evidence sources only. They hold no canonical authority.

---

## Policy

### Core Principle

> Recovery Audit does not automatically imply Runtime Inclusion.

A character may be:

```
Recovered
    +
Canonically Valid
    +
Deferred
```

simultaneously.

**Rationale:** Architectural simplicity requires controlled expansion. Not all valid canon belongs in active runtime.

---

### Status Matrix

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CANON STATUS MATRIX                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  ARCHIVE CANON                                               │   │
│  │  - Historical material                                       │   │
│  │  - Research source only                                      │   │
│  │  - No runtime authority                                       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              │ Recovery Audit                       │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  DEFERRED CANON                                              │   │
│  │  - Canonically valid                                         │   │
│  │  - Not in active runtime                                     │   │
│  │  - Future expansion candidate                                │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              │ Import Process                       │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  ACTIVE CANON                                                │   │
│  │  - In active runtime                                         │   │
│  │  - Resides in database/ (Single Source of Truth)             │   │
│  │  - Subject to all governance rules                           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Import Rule

### Deferred → Active Transition

Deferred Canon may only move to Active Canon after:

```
Step 1: Recovery Audit
    ↓
Step 2: Architecture Review
    ↓
Step 3: Runtime Justification
    ↓
Step 4: Authority Decision
```

**Each step is mandatory. No shortcuts.**

---

### Step 1: Recovery Audit

**Objective:** Verify canonical validity.

**Activities:**
- Collect evidence from archive sources
- Classify as Stable/Variant/Conflicting
- Document genealogy if applicable
- Produce Recovery Report

**Output:** Recovery Audit Report

**Status:** AUDITED — Ready for architecture review

---

### Step 2: Architecture Review

**Objective:** Verify consistency with ADRs.

**Checks:**
- Does this character fit the Only Human scope?
- Does this character fit the Contemporary timeline?
- Does this character fit the Los Angeles Dynasty focus?
- Does this character violate any authority boundaries?

**Output:** Architecture Review Decision

**Status:** REVIEWED — Ready for runtime justification

---

### Step 3: Runtime Justification

**Objective:** Demonstrate runtime necessity.

**Questions:**
- Why does this character need to be active now?
- What scenarios require this character?
- What is the minimal viable inclusion?
- What is the maintenance burden?

**Output:** Runtime Justification Document

**Status:** JUSTIFIED — Ready for authority decision

---

### Step 4: Authority Decision

**Objective:** Final approval for import.

**Decision Options:**

| Decision | Definition | Action |
|----------|------------|--------|
| **ACCEPTED** | Character approved for active canon | Proceed to import |
| **REJECTED** | Character not suitable for active canon | Remain deferred |
| **DEFERRED** | Insufficient justification | Hold pending resolution |

**Output:** Authority Decision Record

**Status:** DECIDED — Ready for import (if accepted)

---

## Governance

### Deferred Canon Maintenance

| Activity | Status |
|----------|--------|
| Store recovery audits | ✓ Required |
| Document genealogy | ✓ Required |
| Update deferred registry | ✓ Required |
| Import to active | ✗ Prohibited without process |

### Active Canon Restrictions

| Activity | Status |
|----------|--------|
| Reference deferred characters | ✗ Prohibited |
| Include deferred in family graph | ✗ Prohibited |
| Use deferred in scenarios | ✗ Prohibited |

### Archive Canon Restrictions

| Activity | Status |
|----------|--------|
| Treat as canonical | ✗ Prohibited |
| Import without audit | ✗ Prohibited |
| Bypass governance | ✗ Prohibited |

---

## Enforcement

### Verification

Before any deferred character enters active canon:

| Check | Question |
|-------|----------|
| Audit | Is there a recovery audit report? |
| Review | Is there an architecture review decision? |
| Justification | Is there a runtime justification document? |
| Decision | Is there an authority decision approving import? |

**If any check fails: STOP. Do not import.**

---

## Authority

Established by: Architecture Review & Canon Reconstruction Workspace  
Type: Repository Operating Policy  
Date: 2026-06-07  
Supersedes: Ad-hoc canon inclusion practices  
Depends on: ADR-000, ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, Repository_Governance.md
