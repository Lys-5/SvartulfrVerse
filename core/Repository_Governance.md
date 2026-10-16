# Repository Governance

**Status:** CANONICAL  
**Date:** 2026-06-07  
**Type:** Repository Operating Rule  
**Authority:** Architecture Review

---

## Purpose

This document defines the mandatory workflow for all future canon additions to SvartulfrVerse.

**The purpose is to prevent:**

| Risk | Description |
|------|-------------|
| Migration Drift | Information changing during import without explicit decision |
| Archive Contamination | Historical errors propagating into canonical records |
| Authority Duplication | Same data owned by multiple layers |
| Direct Imports | Bypassing audit and review process |

**Core Principle:**

> Archive evidence does not become canon automatically.

---

## Authority Sources

### Research Archives

| Source | Role |
|--------|------|
| NotebookLM | Primary Research Archive — evidence source only |
| Progetti archive repository | Research Archive — evidence source only |
| Historical reports and audits | Supporting evidence — migration documentation |

**Critical Distinction:**

Research archives are **evidence sources only**. They are **NOT canonical authority**. They hold no authority position in the hierarchy.

Evidence from research archives must pass through the Canon Recovery Workflow before entering the repository.

---

## Repository Authority Hierarchy

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AUTHORITY HIERARCHY                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  ADRs (Architectural Decision Records)                       │   │
│  │  Highest authority — defines canonical architecture          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Authority Records                                            │   │
│  │  Owned canonical data (family, visual, future characters)    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Imported Canon                                               │   │
│  │  Approved information from recovery workflow                │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Experience Content                                          │   │
│  │  Scenario-specific data (consumer, not owner)               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Historical Archive                                          │   │
│  │  Lowest authority — evidence source only                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Authority Resolution:**

When sources conflict:

```
ADR Decision > Authority Records > Imported Canon > Experience Content > Historical Archive
```

---

## Canon Recovery Workflow

All information must pass through this workflow before entering the repository.

### Step 1: Research

**Objective:** Collect evidence from archive sources.

**Activities:**
- Collect evidence from all research archives (NotebookLM, Progetti)
- Review historical reports and audits
- Compile evidence for audit

**Output:** Research collection (raw evidence, not canonical)

**Status:** EVIDENCE ONLY — Not eligible for import

---

### Step 2: Recovery Audit

**Objective:** Produce a recovery report classifying all evidence.

**Activities:**
- Analyze collected evidence
- Identify conflicts between sources
- Classify each element

**Classification:**

| Class | Definition | Action |
|-------|------------|--------|
| **Stable Canon** | Consistent across all sources, matches ADR authority | Accept as baseline |
| **Variant Canon** | Acceptable variations, no architectural impact | Document, select primary |
| **Conflicting Canon** | Direct contradictions between sources | Escalate for resolution |
| **Recommended Baseline** | Proposed canonical value after analysis | Subject to approval |

**Output:** Recovery Report with classification

**Status:** AUDITED — Ready for architecture review

---

### Step 3: Architecture Review

**Objective:** Verify consistency with accepted ADRs.

**Activities:**
- Check alignment with ADR-000 (Runtime Baseline)
- Check alignment with ADR-001 (Dynastic Origins)
- Check alignment with ADR-002 (Family Authority)
- Check alignment with ADR-003 (Character Authority)
- Check alignment with ADR-004 (Visual Authority)
- Check alignment with ADR-005 (Experience Authority)

**Verification Points:**

| Check | Question |
|-------|----------|
| Ownership | Does this data belong to the correct authority layer? |
| Boundary | Does this violate any cross-authority prohibition? |
| Consistency | Does this contradict any accepted ADR decision? |
| Terminology | Does this use approved terminology? |

**Output:** Architecture Review decision

**Status:** REVIEWED — Ready for authority decision

---

### Step 4: Authority Decision

**Objective:** Determine final status of proposed canon.

**Decision Options:**

| Decision | Definition | Action |
|----------|------------|--------|
| **ACCEPTED** | Information approved for import | Proceed to Step 5 |
| **REJECTED** | Information contradicts canonical authority | Do not import |
| **DEFERRED** | Insufficient evidence or pending resolution | Hold until resolved |

**Output:** Authority Decision record

**Status:** DECIDED — Ready for import (if accepted)

---

### Step 5: Import

**Objective:** Enter approved information into canonical records.

**Import Destinations:**

| Data Type | Destination |
|-----------|-------------|
| Genealogy | `database/families/` |
| Visual Data | `database/worlds/` (visual baseline/inheritance records) |
| Character Records | `database/characters/` |
| Scenario Records | `database/experiences/` |

**Import Rules:**
- Only ACCEPTED information may be imported
- Import must go to correct authority layer
- Import must reference Authority Decision record
- Import must not duplicate existing authority

**Status:** CANONICAL — Information is now part of repository

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CANON RECOVERY WORKFLOW                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐                                                    │
│  │  RESEARCH   │                                                    │
│  │  Step 1     │                                                    │
│  └──────┬──────┘                                                    │
│         │                                                           │
│         ▼                                                           │
│  ┌─────────────┐     ┌─────────────────────────────────────┐       │
│  │  RECOVERY   │────►│ Classification:                     │       │
│  │  AUDIT      │     │ - Stable Canon                       │       │
│  │  Step 2     │     │ - Variant Canon                      │       │
│  └──────┬──────┘     │ - Conflicting Canon                  │       │
│         │            │ - Recommended Baseline               │       │
│         │            └─────────────────────────────────────┘       │
│         ▼                                                           │
│  ┌─────────────┐     ┌─────────────────────────────────────┐       │
│  │ ARCHITECTURE│────►│ Verify against:                      │       │
│  │  REVIEW     │     │ - ADR-000 through ADR-005            │       │
│  │  Step 3     │     │ - Authority boundaries               │       │
│  └──────┬──────┘     │ - Terminology                        │       │
│         │            └─────────────────────────────────────┘       │
│         ▼                                                           │
│  ┌─────────────┐     ┌─────────────────────────────────────┐       │
│  │  AUTHORITY  │────►│ Decision:                            │       │
│  │  DECISION   │     │ - ACCEPTED → Proceed                 │       │
│  │  Step 4     │     │ - REJECTED → Stop                    │       │
│  └──────┬──────┘     │ - DEFERRED → Hold                    │       │
│         │            └─────────────────────────────────────┘       │
│         │                                                           │
│         │ [ACCEPTED only]                                           │
│         ▼                                                           │
│  ┌─────────────┐                                                    │
│  │   IMPORT    │                                                    │
│  │  Step 5     │                                                    │
│  └─────────────┘                                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Import Restrictions

### PROHIBITED

| Action | Reason |
|--------|--------|
| Direct archive imports | Bypasses audit and review |
| Copy-paste migration | Propagates drift and errors |
| World-layer canon creation | Worlds are consumers, not owners |
| Experience-layer canon creation | Experiences are consumers, not owners |
| Character-defined genealogy | Genealogy belongs to Family Authority |
| Character-defined appearance | Appearance belongs to Visual Authority |

### REQUIRED

| Action | Reason |
|--------|--------|
| Audit first | Classify evidence before import |
| Review second | Verify consistency with ADRs |
| Import third | Only approved information enters |

---

## Character Recovery Rule

**No character may enter the repository until:**

- [ ] Recovery audit completed
- [ ] Architecture review completed
- [ ] Authority decision completed

**Character Import Sequence:**

1. Genealogy enters `database/families/`
2. Visual data enters `database/worlds/` (visual baseline/inheritance records)
3. Character record enters `database/characters/`

**Character files may reference authority records. They may not define authority.**

---

## Family Authority Rule

**Genealogy must enter:**

```
database/families/
```

**before appearing anywhere else.**

**Character files may:**
- Reference genealogy (read-only)
- Query family relationships

**Character files may NOT:**
- Define parent-child relationships
- Modify family structure
- Own genealogy authority

---

## Visual Authority Rule

**Appearance data must enter:**

```
database/worlds/
```

**before appearing anywhere else.**

**Character files may:**
- Reference appearance (read-only)
- Query visual characteristics

**Character files may NOT:**
- Define appearance baseline
- Modify visual inheritance
- Own appearance authority

---

## Future Expansion Rule

**Worlds, scenarios, and experiences are consumers.**

They are **NOT authority sources.**

| Layer | Role | Authority |
|-------|------|-----------|
| Worlds | Consumer | References authority |
| Scenarios | Consumer | References authority |
| Experiences | Consumer | References authority |

**Consumer layers may:**
- Reference authority records
- Extend relationships (scenario-specific)
- Override occupation (scenario-scoped)

**Consumer layers may NOT:**
- Create new canon
- Redefine authority records
- Own canonical data

---

## Enforcement Principles

### 1. No Bypass

The Canon Recovery Workflow is mandatory. No exceptions.

### 2. Evidence ≠ Canon

Historical archive evidence is not canonical until processed through the workflow.

### 3. Authority Hierarchy

ADRs always supersede historical evidence. When in doubt, escalate.

### 4. Single Source of Truth

Each data domain has exactly one owner. No duplication.

### 5. Audit Trail Required

All imports must reference:
- Recovery Report
- Architecture Review decision
- Authority Decision record

### 6. Rejection is Valid

REJECTED information must not enter the repository. DEFERRED information must wait for resolution.

---

## Governance Verification

Before any import, verify:

| Check | Question |
|-------|----------|
| Workflow | Has this information passed through all 5 steps? |
| Authority | Is this information entering the correct layer? |
| Ownership | Does this layer own this data domain? |
| Consistency | Does this contradict any ADR? |
| Audit | Is there a recovery report for this information? |
| Decision | Is there an authority decision approving this? |

**If any check fails, STOP. Do not import.**

---

## Authority

Established by: Architecture Review & Canon Reconstruction Workspace  
Type: Repository Operating Rule  
Date: 2026-06-07  
Supersedes: All ad-hoc import practices  
Depends on: ADR-000, ADR-001, ADR-002, ADR-003, ADR-004, ADR-005
