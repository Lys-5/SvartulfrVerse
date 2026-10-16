# VALIDATION PIPELINE SPECIFICATION

**Status:** CANONICAL  
**Date:** 2026-06-08  
**Authority:** ADR-000, ADR-006, R-007_Engine_Rules, R-008_Bot_Rules, R-009_Lorebook_Rules  
**Version:** 1.0 — Canon Freeze v1

---

## Purpose

This document defines the automated validation checks that form the validation pipeline for all engine output, bot generation, and lorebook generation. The validation pipeline is the **mandatory gate** — no output may be released without passing all applicable checks.

**Authority:** validation_engine (defined in ENGINE_SPECIFICATION.md) implements this specification.

---

## Validation Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    VALIDATION PIPELINE                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  INPUT: Engine output / Bot export / Lorebook entry          │ │
│  └───────────────────────────┬───────────────────────────────────┘ │
│                              │                                      │
│         ┌────────────────────┼────────────────────┐                │
│         │                    │                    │                │
│         ▼                    ▼                    ▼                │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐        │
│  │ Cross-      │  │ Canon-Layer  │  │ Authority         │        │
│  │ Reference   │  │ Validation   │  │ Ownership         │        │
│  │ Validation  │  │              │  │ Validation        │        │
│  └──────┬──────┘  └──────┬───────┘  └────────┬──────────┘        │
│         │                │                    │                   │
│         └────────────────┼────────────────────┘                   │
│                          │                                        │
│                          ▼                                        │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Traceability Validation                                   │   │
│  └───────────────────────────┬───────────────────────────────┘   │
│                              │                                     │
│                              ▼                                     │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  RESULT: valid / invalid / warning                        │   │
│  │  + Detailed report                                        │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Validation Check Categories

### 1. Cross-Reference Validation

**Purpose:** Verify all entity references resolve to existing, consistent database/ records.

#### Check 1.1: Entity Resolution

| Check ID | Description | Severity |
|----------|-------------|----------|
| CR-001 | All character references resolve to existing `database/characters/C_*.md` records | ERROR |
| CR-002 | All family references resolve to existing `database/families/F_*.md` records | ERROR |
| CR-003 | All visual references resolve to existing `database/worlds/W_*.md` records | ERROR |
| CR-004 | All institution references resolve to existing `database/institutions/I_*.md` records | ERROR |
| CR-005 | All experience references resolve to existing `database/experiences/Ex_*.md` records | ERROR |

#### Check 1.2: Relationship Consistency

| Check ID | Description | Severity |
|----------|-------------|----------|
| CR-101 | All parent-child claims match `database/families/F_Parent_Child.md` | ERROR |
| CR-102 | All marriage claims match `database/families/F_Marriages.md` | ERROR |
| CR-103 | All sibling claims are computable from parent-child records | ERROR |
| CR-104 | No circular genealogical references exist | ERROR |
| CR-105 | Wulfnic → Erik father-son relationship is ABSENT (legacy drift check) | ERROR |

#### Check 1.3: Visual Consistency

| Check ID | Description | Severity |
|----------|-------------|----------|
| CR-201 | All visual claims match `database/worlds/W_Visual_Baseline.md` or character record | ERROR |
| CR-202 | All visual inheritance classifications match `database/worlds/W_Visual_Inheritance.md` | ERROR |
| CR-203 | No supernatural visual elements present (ADR-000 compliance) | ERROR |

#### Check 1.4: Identity Consistency

| Check ID | Description | Severity |
|----------|-------------|----------|
| CR-301 | All character names match `database/characters/C_*.md` identity records | ERROR |
| CR-302 | All personality claims match character psychology records | ERROR |
| CR-303 | All education claims match character capability records | ERROR |
| CR-304 | All occupation claims match character capability records | WARNING |

---

### 2. Canon-Layer Validation

**Purpose:** Verify correct classification and separation of Active, Historical, and Cultural Canon.

#### Check 2.1: Layer Classification

| Check ID | Description | Severity |
|----------|-------------|----------|
| CL-001 | Every output element has exactly one canon layer classification | ERROR |
| CL-002 | Active Canon content is not mixed with Cultural Canon | ERROR |
| CL-003 | Historical Canon content is properly classified as Historical | ERROR |
| CL-004 | Cultural Canon content is clearly marked as non-factual | ERROR |
| CL-005 | No Deferred Canon content is treated as Active | ERROR |
| CL-006 | No Candidate Canon content is treated as approved | ERROR |

#### Check 2.2: Layer Boundary Enforcement

| Check ID | Description | Severity |
|----------|-------------|----------|
| CL-101 | Cultural Canon is never presented as runtime fact | ERROR |
| CL-102 | Historical Canon is not compiled as Active without Authority Decision | ERROR |
| CL-103 | Active Canon content is not downgraded to Cultural | ERROR |
| CL-104 | Rejected canon material is not present in any output | ERROR |

#### Check 2.3: Rejected Canon Detection

| Check ID | Description | Severity |
|----------|-------------|----------|
| CL-201 | Valeria / WetNurse / Concubine concept is ABSENT | ERROR |
| CL-202 | Miss Twin Peaks origin story is ABSENT | ERROR |
| CL-203 | KSA origin story is ABSENT | ERROR |
| CL-204 | Supernatural systems (werewolves, pack hierarchy) are ABSENT from Active output | ERROR |
| CL-205 | Immortal Founder / Ancient Patriarch claims are ABSENT | ERROR |

---

### 3. Authority Ownership Validation

**Purpose:** Verify no engine output claims ownership of data it doesn't own.

#### Check 3.1: Domain Ownership

| Check ID | Description | Severity |
|----------|-------------|----------|
| AO-001 | Character data comes from Character Authority (database/characters/) | ERROR |
| AO-002 | Family data comes from Family Authority (database/families/) | ERROR |
| AO-003 | Visual data comes from Visual Authority (database/worlds/) | ERROR |
| AO-004 | Experience data comes from Experience Authority (database/experiences/) | ERROR |
| AO-005 | No character file contains genealogical definitions | ERROR |
| AO-006 | No family file contains character identity definitions | ERROR |
| AO-007 | No experience file contains canonical identity overrides | ERROR |

#### Check 3.2: Cross-Layer Boundary

| Check ID | Description | Severity |
|----------|-------------|----------|
| AO-101 | Character files reference but do not define genealogy | ERROR |
| AO-102 | Experience files reference but do not redefine identity | ERROR |
| AO-103 | Lorebook entries reference but do not replace database/ records | ERROR |
| AO-104 | Bot exports reference but do not modify canonical data | ERROR |

---

### 4. Traceability Validation

**Purpose:** Verify every output element has a complete provenance chain.

#### Check 4.1: Source Attribution

| Check ID | Description | Severity |
|----------|-------------|----------|
| TR-001 | Every output element has at least one source file path | ERROR |
| TR-002 | All source paths point to existing database/ files | ERROR |
| TR-003 | No orphaned output exists without canonical source | ERROR |
| TR-004 | Provenance chain is complete (output → engine → database/ record) | ERROR |

#### Check 4.2: Version Tracking

| Check ID | Description | Severity |
|----------|-------------|----------|
| TR-101 | All generated output includes canon version identifier | WARNING |
| TR-102 | All generated output includes generation timestamp | WARNING |
| TR-103 | All generated output includes validation status | ERROR |

---

## Validation Execution Rules

### When Validation Runs

| Trigger | Validation Type | Scope |
|---------|----------------|-------|
| Engine query response | `cross_reference` + `traceability` | Single query output |
| Bot generation | `full` | Complete character card |
| Lorebook generation | `full` | Complete lorebook file |
| Batch export | `full` | All output files |
| Repository change | `cross_reference` + `authority_ownership` | All affected records |

### Validation Outcomes

| Outcome | Description | Action |
|---------|-------------|--------|
| `valid` | All checks passed | Release output |
| `warning` | Non-critical issues detected | Release with warning log |
| `invalid` | Critical checks failed | Reject output, return error report |

### Error Report Format

```json
{
  "validation_id": "VAL-[timestamp]-[random]",
  "timestamp": "[ISO timestamp]",
  "source_engine": "[engine_name]",
  "validation_type": "[type]",
  "outcome": "invalid",
  "checks_passed": ["CR-001", "CR-002", ...],
  "checks_failed": [
    {
      "check_id": "CR-105",
      "severity": "ERROR",
      "description": "Wulfnic → Erik father-son relationship detected",
      "location": "[file path and line]",
      "resolution": "Remove false relationship. Reference ADR-001 for canonical genealogy."
    }
  ],
  "traceability_chain": ["[source paths]"],
  "recommendation": "REJECT output. Correct source data and re-validate."
}
```

---

## Automated Validation Checks — Implementation Reference

### Check Implementation Matrix

| Check Category | Check Count | Automation Level | Priority |
|----------------|-------------|------------------|----------|
| Cross-Reference (CR) | 17 | Fully automatable | HIGH |
| Canon-Layer (CL) | 12 | Fully automatable | HIGH |
| Authority Ownership (AO) | 11 | Fully automatable | HIGH |
| Traceability (TR) | 7 | Fully automatable | MEDIUM |
| **Total** | **47** | | |

### Automation Notes

**Fully automatable checks** can be implemented as validation_engine functions that:
1. Parse output data
2. Query database/ for verification
3. Return pass/fail with detailed error information

**Checks requiring ADR knowledge** (rejected canon detection) require:
1. ADR-006 rejected canon list as reference data
2. Pattern matching against known rejected concepts
3. Flagging any matches for manual review

---

## Validation Pipeline Integration

### Integration with Engine Layer

```
Engine Output → validation_engine → [valid/invalid/warning]
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
              [valid]         [warning]       [invalid]
                    │               │               │
                    ▼               ▼               ▼
              Release         Release +         Reject
              Output          Warning Log       + Error Report
```

### Integration with Bot Generation

```
Bot Generation Request
    │
    ▼
En_Core Query
    │
    ▼
Engine Output
    │
    ▼
validation_engine (full)
    │
    ├── valid → Format per platform schema → Attach provenance → Release
    │
    └── invalid → Reject → Return error report → Log failure
```

### Integration with Lorebook Generation

```
Lorebook Generation Request
    │
    ▼
En_Core Query (all records in domain)
    │
    ▼
For each record:
    Generate entry → validation_engine (cross_reference + canon_layer)
    │
    ├── valid → Add to lorebook file
    │
    └── invalid → Skip entry → Log error
    │
    ▼
Final validation_engine (traceability) on complete file
    │
    ├── valid → Write lorebook file with metadata header
    │
    └── invalid → Reject file → Return error report
```

---

## Authority

**Established by:** Architecture Review & Canon Authority  
**Approved by:** Canon Freeze v1 Governance  
**Depends on:** ADR-000, ADR-006, R-007, R-008, R-009, ENGINE_SPECIFICATION.md  
**Version:** 1.0 — Frozen under Canon Freeze v1
