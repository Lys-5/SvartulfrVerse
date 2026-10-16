# Character Audit Protocol

**Status:** CANONICAL — Phase 2 (Character Validation) COMPLETE  
**Date:** 2026-06-07  
**Updated:** 2026-06-08 (Canon Freeze v1 — all 12 characters validated and frozen)  
**Authority:** ADR-000, ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, ADR-006

---

## Purpose

Character recovery must occur before character import because:

1. **Legacy Drift Exists** — The historical archive contains documented degradation patterns (Noah occupation drift, Douglas-Bloodmoon naming inconsistencies, family relationship degradation)

2. **Authority Architecture Requires Validation** — The new repository enforces strict authority boundaries. Characters must be validated against ADR decisions before import.

3. **Runtime Preservation** — Importing unvalidated characters risks corrupting the canonical baseline and propagating drift into the new system.

4. **Audit Trail Required** — Every character import must have explicit documentation of what was validated, what conflicts were resolved, and what baseline was established.

**Rule:** No character may be imported without passing this audit protocol.

---

## Authority Sources

Audit authority follows this precedence order:

| Priority | Source | Role |
|----------|--------|------|
| 1 | Accepted ADRs | Highest authority — defines canonical architecture |
| 2 | Authority Records | Owned canonical data (family, visual, character, experience) |
| 3 | Active Canon | Approved information in repository |
| 4 | Research Evidence | Evidence from research archives |
| 5 | Runtime Validation Findings | Behavioral evidence — how character actually behaves |

**Research Evidence includes:** NotebookLM, Progetti — all evidence sources only, no authority ranking among them.

### Authority Resolution

When sources conflict:

```
ADR Decision > Authority Records > Active Canon > Research Evidence > Runtime Findings
```

If ADR is silent on a specific conflict, escalate to Architecture Review for explicit decision. Research evidence from archives has no precedence ranking — all research archives are equal evidence sources.

---

## Required Audit Categories

Every character must be audited across all categories before import.

### Identity

| Element | Definition | Authority |
|---------|------------|-----------|
| Name | Canonical given name | Character Authority (ADR-003) |
| Surname | Family surname | Family Authority (ADR-002) |
| Dynasty | Dynasty membership | Family Authority (ADR-002) |
| Family Position | Role in family structure | Family Authority (ADR-002) |

**Validation Rules:**
- Name must be consistent across all sources
- Surname must match Surname Authority rules (ADR-001, ADR-002)
- Dynasty must match Family Graph (ADR-002)
- Family Position must match Character Roles

> **Note:** `Character Roles` — Phase 2 COMPLETE. All character roles validated and frozen per Canon Freeze v1.

---

### Narrative Function

| Element | Definition | Authority |
|---------|------------|-----------|
| Purpose | Why the character exists | Character Authority |
| Role | Function in narrative | Experience Authority (ADR-005) |
| Significance | Importance to story | Character Authority |

**Validation Rules:**
- Must have explicit narrative purpose
- Must not duplicate another character's function
- Must align with Los Angeles experience scope

---

### Behavioral Canon

| Element | Definition | Authority |
|---------|------------|-----------|
| Personality | Core temperament | Character Authority (ADR-003) |
| Behavioral Baseline | Stable traits | Character Authority (ADR-003) |
| Speech Patterns | How character speaks | Character Authority |
| Decision Patterns | How character decides | Character Authority |

**Validation Rules:**
- Personality must be stable across scenarios
- Behavioral traits must not contradict genealogy constraints
- Must distinguish from other family members

---

### Visual Canon

| Element | Definition | Authority |
|---------|------------|-----------|
| Hair Color | Canonical hair color | Visual Authority (ADR-004) |
| Eye Color | Canonical eye color | Visual Authority (ADR-004) |
| Build | Physical build | Visual Authority (ADR-004) |
| Height | Canonical height | Visual Authority (ADR-004) |
| Aesthetic | Style/fashion baseline | Visual Authority (ADR-004) |

**Validation Rules:**
- Must match Visual Baseline for dynasty (Douglas or Bloodmoon)
- Must follow Visual Fusion Model if Douglas-Bloodmoon heir
- Must match Inheritance Rules for parent resemblance

---

### Relationship Authority

| Element | Definition | Authority |
|---------|------------|-----------|
| Parents | Parent-child relationships | Family Authority (ADR-002) |
| Siblings | Sibling relationships | Family Authority (ADR-002) |
| Spouse | Marriage relationships | Family Authority (ADR-002) |
| Extended | Extended family | Family Authority (ADR-002) |

**Validation Rules:**
- All relationships must match Family Graph
- No relationship may contradict ADR-001 or ADR-002
- Wulfnic → Erik relationship is EXPLICITLY REJECTED

> **Note:** `Family Graph` — Phase 2 COMPLETE. Family graph fully populated in database/families/ and validated per Canon Freeze v1.

---

### Timeline Authority

| Element | Definition | Authority |
|---------|------------|-----------|
| Age | Current age | Character Authority |
| Education | Educational history | Character Authority |
| Career | Professional history | Character Authority |
| Historical Events | Significant life events | Character Authority |

**Validation Rules:**
- Age must be consistent with birth date and current timeline
- Education must align with contemporary era (2020s-2030s)
- Career must align with Only Human scope (no supernatural elements)

---

## Classification System

Every audit must classify each element into one of four categories:

### Stable Canon

**Definition:** Element is consistent across all sources and matches ADR authority.

**Criteria:**
- No conflicts between sources
- Matches ADR decisions
- No drift detected

**Action:** Accept as canonical baseline.

---

### Variant Canon

**Definition:** Element has acceptable variations that do not contradict authority.

**Criteria:**
- Minor variations between sources
- Variations do not contradict ADR
- No architectural impact

**Action:** Document variants, select primary baseline.

---

### Conflicting Canon

**Definition:** Element has contradictions that must be resolved.

**Criteria:**
- Direct contradiction between sources
- Contradicts ADR authority
- Architectural impact

**Action:** Escalate for explicit resolution. Cannot import until resolved.

---

### Recommended Baseline

**Definition:** The proposed canonical value after conflict resolution.

**Criteria:**
- Based on highest authority source
- Documented rationale for selection
- Approved by Architecture Review

**Action:** Becomes canonical baseline for import.

---

## Migration Drift Detection

### Repository Drift

**Definition:** Character data that has changed within the historical repository across versions.

**Detection Method:**
1. Compare character data across repository versions
2. Identify elements that changed without explicit decision
3. Classify changes as intentional or drift

**Indicators:**
- Occupation changes without narrative reason
- Relationship changes without story justification
- Personality shifts across scenarios

---

### Archive Drift

**Definition:** Character data that differs between research archive sources (NotebookLM, Svartulfr_LA, Progetti) vs. repository files.

**Detection Method:**
1. Collect character data from research archives
2. Compare with repository file data
3. Identify discrepancies

**Indicators:**
- Different names or spellings
- Different relationship claims
- Different timeline details

---

### Runtime Drift

**Definition:** Character behavior that differs from documented canon during actual use.

**Detection Method:**
1. Compare runtime behavior with documented traits
2. Identify behavioral inconsistencies
3. Classify as feature or bug

**Indicators:**
- Character acts against documented personality
- Relationships not reflected in behavior
- Timeline events contradicted by actions

---

## Import Readiness

### Classification Levels

| Level | Definition | Action |
|-------|------------|--------|
| **READY** | All conflicts resolved, baseline established | Import permitted |
| **PARTIAL** | Some conflicts resolved, others pending | Import with caveats |
| **BLOCKED** | Unresolved conflicts prevent import | Cannot import until resolved |

---

### READY Criteria

Character may be imported when:

- [ ] All Identity elements validated
- [ ] Genealogy matches Family Graph (ADR-002)
- [ ] Visual matches Visual Baseline (ADR-004)
- [ ] No Conflicting Canon elements remain
- [ ] Recommended Baseline documented
- [ ] Architecture Review approved

---

### PARTIAL Criteria

Character may be partially imported when:

- [ ] Core Identity validated
- [ ] Genealogy validated
- [ ] Visual baseline validated
- [ ] Some Timeline elements pending
- [ ] Non-critical elements deferred

**Note:** Partial imports must document pending elements and resolution plan.

---

### BLOCKED Criteria

Character cannot be imported when:

- [ ] Genealogy conflicts with ADR-001 or ADR-002
- [ ] Identity conflicts with Character Authority
- [ ] Visual conflicts with Visual Authority
- [ ] Critical Timeline conflicts unresolved
- [ ] Architecture Review rejected

**Action:** Document blocking issues, escalate for resolution.

---

## Audit Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CHARACTER AUDIT WORKFLOW                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐                                                    │
│  │  START      │                                                    │
│  └──────┬──────┘                                                    │
│         │                                                           │
│         ▼                                                           │
│  ┌─────────────┐     ┌─────────────┐                               │
│  │  Identity   │────►│  Genealogy  │                               │
│  │   Audit     │     │   Audit     │                               │
│  └──────┬──────┘     └──────┬──────┘                               │
│         │                   │                                       │
│         │    ┌──────────────┘                                       │
│         │    │                                                      │
│         ▼    ▼                                                      │
│  ┌─────────────┐     ┌─────────────┐                               │
│  │  Visual     │────►│ Behavioral  │                               │
│  │   Audit     │     │   Audit     │                               │
│  └──────┬──────┘     └──────┬──────┘                               │
│         │                   │                                       │
│         │    ┌──────────────┘                                       │
│         │    │                                                      │
│         ▼    ▼                                                      │
│  ┌─────────────┐     ┌─────────────┐                               │
│  │ Relationship│────►│  Timeline   │                               │
│  │   Audit     │     │   Audit     │                               │
│  └──────┬──────┘     └──────┬──────┘                               │
│         │                   │                                       │
│         │    ┌──────────────┘                                       │
│         │    │                                                      │
│         ▼    ▼                                                      │
│  ┌─────────────────────────────────┐                               │
│  │       CLASSIFICATION             │                               │
│  │  Stable / Variant / Conflicting  │                               │
│  └──────────────┬──────────────────┘                               │
│                 │                                                   │
│                 ▼                                                   │
│  ┌─────────────────────────────────┐                               │
│  │      IMPORT READINESS           │                               │
│  │   READY / PARTIAL / BLOCKED    │                               │
│  └──────────────┬──────────────────┘                               │
│                 │                                                   │
│         ┌───────┴───────┐                                           │
│         │               │                                           │
│         ▼               ▼                                           │
│  ┌─────────────┐ ┌─────────────┐                                   │
│  │   IMPORT    │ │  ESCALATE   │                                   │
│  │  PERMITTED  │ │  BLOCKED    │                                   │
│  └─────────────┘ └─────────────┘                                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Audit Documentation

Every audit must produce:

1. **Audit Record** — Element-by-element classification
2. **Conflict Log** — All conflicts identified and resolution
3. **Baseline Document** — Recommended canonical values
4. **Import Status** — READY / PARTIAL / BLOCKED classification

---

## Authority

Established by: Architecture Review & Canon Reconstruction Workspace  
Approved by: Runtime Validation  
Date: 2026-06-07  
Depends on: ADR-000, ADR-001, ADR-002, ADR-003, ADR-004, ADR-005
