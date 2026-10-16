# VALIDATION_CHECKLIST

**Version:** 1.0  
**Date:** 2026-06-08  
**Authority:** VALIDATION_PIPELINE_SPECIFICATION.md, R-007_Engine_Rules  
**Purpose:** Human-readable operational validation guide. Complements (does not duplicate) the technical specification.

---

## How to Use This Checklist

This checklist is for manual validation audits. For automated validation, see `VALIDATION_PIPELINE_SPECIFICATION.md` (47-check automated pipeline).

**Severity Levels:**
- ✅ **PASS** — No issue detected
- ⚠️ **WARNING** — Non-critical issue or improvement opportunity
- ❌ **FAIL** — Critical violation; output must not proceed

**Workflow:** Execute checks in order. On first FAIL, STOP and report. Do not continue validation until FAIL is resolved.

---

## 1. CROSS-REFERENCE VALIDATION

**Purpose:** Verify all entity references resolve to existing, consistent database/ records.

### 1.1 Entity Resolution

| Check | Question | Severity |
|-------|----------|----------|
| ☐ CR-001 | Do all character references resolve to existing `database/characters/C_*.md` records? | ❌ FAIL |
| ☐ CR-002 | Do all family references resolve to existing `database/families/F_*.md` records? | ❌ FAIL |
| ☐ CR-003 | Do all visual references resolve to existing `database/worlds/W_*.md` records? | ❌ FAIL |
| ☐ CR-004 | Do all institution references resolve to existing `database/institutions/I_*.md` records? | ❌ FAIL |
| ☐ CR-005 | Do all experience references resolve to existing `database/experiences/Ex_*.md` records? | ❌ FAIL |

### 1.2 Relationship Consistency

| Check | Question | Severity |
|-------|----------|----------|
| ☐ CR-101 | Do all parent-child claims match `database/families/F_Parent_Child.md`? | ❌ FAIL |
| ☐ CR-102 | Do all marriage claims match `database/families/F_Marriages.md`? | ❌ FAIL |
| ☐ CR-103 | Are all sibling claims computable from parent-child records? | ❌ FAIL |
| ☐ CR-104 | Are there no circular genealogical references? | ❌ FAIL |
| ☐ CR-105 | Is the Wulfnic → Erik father-son relationship ABSENT? | ❌ FAIL |

### 1.3 Visual Consistency

| Check | Question | Severity |
|-------|----------|----------|
| ☐ CR-201 | Do all visual claims match `database/worlds/W_Visual_Baseline.md` or character record? | ❌ FAIL |
| ☐ CR-202 | Do all visual inheritance classifications match `database/worlds/W_Visual_Inheritance.md`? | ❌ FAIL |
| ☐ CR-203 | Are there no supernatural visual elements present? | ❌ FAIL |

### 1.4 Identity Consistency

| Check | Question | Severity |
|-------|----------|----------|
| ☐ CR-301 | Do all character names match `database/characters/C_*.md` identity records? | ❌ FAIL |
| ☐ CR-302 | Do all personality claims match character psychology records? | ❌ FAIL |
| ☐ CR-303 | Do all education claims match character capability records? | ❌ FAIL |
| ☐ CR-304 | Do all occupation claims match character capability records? | ⚠️ WARNING |

---

## 2. CANON-LAYER VALIDATION

**Purpose:** Verify correct classification and separation of Active, Historical, and Cultural Canon.

### 2.1 Layer Classification

| Check | Question | Severity |
|-------|----------|----------|
| ☐ CL-001 | Does every output element have exactly one canon layer classification? | ❌ FAIL |
| ☐ CL-002 | Is Active Canon content not mixed with Cultural Canon? | ❌ FAIL |
| ☐ CL-003 | Is Historical Canon content properly classified as Historical? | ❌ FAIL |
| ☐ CL-004 | Is Cultural Canon content clearly marked as non-factual? | ❌ FAIL |
| ☐ CL-005 | Is no Deferred Canon content treated as Active? | ❌ FAIL |
| ☐ CL-006 | Is no Candidate Canon content treated as approved? | ❌ FAIL |

### 2.2 Layer Boundary Enforcement

| Check | Question | Severity |
|-------|----------|----------|
| ☐ CL-101 | Is Cultural Canon never presented as runtime fact? | ❌ FAIL |
| ☐ CL-102 | Is Historical Canon not compiled as Active without Authority Decision? | ❌ FAIL |
| ☐ CL-103 | Is Active Canon content not downgraded to Cultural? | ❌ FAIL |
| ☐ CL-104 | Is rejected canon material absent from all output? | ❌ FAIL |

### 2.3 Rejected Canon Detection

| Check | Question | Severity |
|-------|----------|----------|
| ☐ CL-201 | Is Valeria / WetNurse / Concubine concept ABSENT? | ❌ FAIL |
| ☐ CL-202 | Is Miss Twin Peaks origin story ABSENT? | ❌ FAIL |
| ☐ CL-203 | Is KSA origin story ABSENT? | ❌ FAIL |
| ☐ CL-204 | Are supernatural systems (werewolves, pack hierarchy) ABSENT from Active output? | ❌ FAIL |
| ☐ CL-205 | Are Immortal Founder / Ancient Patriarch claims ABSENT? | ❌ FAIL |

---

## 3. AUTHORITY OWNERSHIP VALIDATION

**Purpose:** Verify no output claims ownership of data it doesn't own.

### 3.1 Domain Ownership

| Check | Question | Severity |
|-------|----------|----------|
| ☐ AO-001 | Does character data come from Character Authority (`database/characters/`)? | ❌ FAIL |
| ☐ AO-002 | Does family data come from Family Authority (`database/families/`)? | ❌ FAIL |
| ☐ AO-003 | Does visual data come from Visual Authority (`database/worlds/`)? | ❌ FAIL |
| ☐ AO-004 | Does experience data come from Experience Authority (`database/experiences/`)? | ❌ FAIL |
| ☐ AO-005 | Does any character file contain genealogical definitions? | ❌ FAIL |
| ☐ AO-006 | Does any family file contain character identity definitions? | ❌ FAIL |
| ☐ AO-007 | Does any experience file contain canonical identity overrides? | ❌ FAIL |

### 3.2 Cross-Layer Boundary

| Check | Question | Severity |
|-------|----------|----------|
| ☐ AO-101 | Do character files reference but not define genealogy? | ❌ FAIL |
| ☐ AO-102 | Do experience files reference but not redefine identity? | ❌ FAIL |
| ☐ AO-103 | Do lorebook entries reference but not replace database/ records? | ❌ FAIL |
| ☐ AO-104 | Do bot exports reference but not modify canonical data? | ❌ FAIL |

---

## 4. TRACEABILITY VALIDATION

**Purpose:** Verify every output element has a complete provenance chain.

### 4.1 Source Attribution

| Check | Question | Severity |
|-------|----------|----------|
| ☐ TR-001 | Does every output element have at least one source file path? | ❌ FAIL |
| ☐ TR-002 | Do all source paths point to existing database/ files? | ❌ FAIL |
| ☐ TR-003 | Is there no orphaned output without canonical source? | ❌ FAIL |
| ☐ TR-004 | Is the provenance chain complete (output → engine → database/ record)? | ❌ FAIL |

### 4.2 Version Tracking

| Check | Question | Severity |
|-------|----------|----------|
| ☐ TR-101 | Does all generated output include canon version identifier? | ⚠️ WARNING |
| ☐ TR-102 | Does all generated output include generation timestamp? | ⚠️ WARNING |
| ☐ TR-103 | Does all generated output include validation status? | ❌ FAIL |

---

## 5. AUDIT WORKFLOW

### 5.1 Pre-Validation Steps

Before running validation:

1. ☐ Identify the scope (single record, batch, full repository)
2. ☐ Identify the validation type needed:
   - **Cross-Reference** — For engine query responses
   - **Canon-Layer** — For bot/lorebook generation
   - **Authority Ownership** — For repository changes
   - **Traceability** — For all generated output
   - **Full** — For release candidates
3. ☐ Verify Canon Freeze v1 compliance (no rejected canon present)
4. ☐ Verify all source files exist in `database/`

### 5.2 Execution Order

```
Step 1: Cross-Reference Validation (Section 1)
    │
    ├── FAIL → STOP. Report broken references. Do not proceed.
    │
    ▼
Step 2: Canon-Layer Validation (Section 2)
    │
    ├── FAIL → STOP. Report layer violations. Do not proceed.
    │
    ▼
Step 3: Authority Ownership Validation (Section 3)
    │
    ├── FAIL → STOP. Report ownership violations. Do not proceed.
    │
    ▼
Step 4: Traceability Validation (Section 4)
    │
    ├── FAIL → STOP. Report traceability gaps. Do not proceed.
    │
    ▼
Step 5: Compile Results
    │
    ├── All PASS → Output is VALID
    ├── Any WARNING → Output is VALID WITH WARNINGS
    └── Any FAIL → Output is INVALID
```

### 5.3 Post-Validation Actions

| Outcome | Action |
|---------|--------|
| **VALID** | Release output. Log validation result. |
| **VALID WITH WARNINGS** | Release output. Log warnings. Recommend improvements. |
| **INVALID** | Reject output. Return error report. Log failure. Do not release. |

### 5.4 Error Report Format

For each FAIL, document:
1. **Check ID** (e.g., CR-105)
2. **Description** (what was found)
3. **Location** (file path and line)
4. **Resolution** (what must be fixed)
5. **Authority** (which ADR/Rule governs this check)

---

## 6. QUICK REFERENCE — COMMON FAILURES

| Failure | Check | Resolution |
|---------|-------|------------|
| Character file defines parent-child | AO-005 | Move to `database/families/F_Parent_Child.md` |
| Wulfnic → Erik father-son found | CR-105 | Remove; legacy drift per ADR-001 |
| Cultural Canon presented as fact | CL-101 | Reclassify as flavor; add disclaimer |
| Valeria concept detected | CL-201 | Remove; rejected canon per ADR-006 |
| Bot card has no source attribution | TR-001 | Add provenance metadata |
| Experience redefines character name | AO-007 | Remove; identity is Character Authority |
| Lorebook contradicts database/ | CL-004 | Update lorebook; database/ is authoritative |

---

*This checklist is derived from VALIDATION_PIPELINE_SPECIFICATION.md. For the full 47-check automated specification, consult the technical document in `core/`.*
