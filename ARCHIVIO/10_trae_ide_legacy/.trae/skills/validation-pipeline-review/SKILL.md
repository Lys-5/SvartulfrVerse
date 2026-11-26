---
name: Validation Pipeline Review
description: Use this skill when reviewing the validation pipeline, verifying check coverage, auditing validation rules, or assessing pipeline readiness. This skill validates the 47-check validation pipeline against repository governance and canon freeze requirements without modifying repository content.
---

# Validation Pipeline Review

## Purpose

Review and validate the completeness, correctness, and coverage of the validation pipeline defined in VALIDATION_PIPELINE_SPECIFICATION.md.

This skill ensures that all 47 automated checks are properly defined, non-overlapping, and aligned with repository governance.

This is an audit-only workflow.

---

## Review Scope

Audit:

* VALIDATION_PIPELINE_SPECIFICATION.md
* Cross-Reference checks (CR-001 through CR-304)
* Canon-Layer checks (CL-001 through CL-205)
- Authority Ownership checks (AO-001 through AO-104)
* Traceability checks (TR-001 through TR-103)

Validate against:

* ADR-000 Runtime Baseline
* ADR-006 Canon Layer Architecture
* R-007 Engine Rules
* R-008 Bot Rules
* R-009 Lorebook Rules

---

## Required Checks

### Specification Completeness

Verify:

* all 47 checks are defined
* each check has a unique ID
* each check has a severity level
* each check has a clear description

Flag:

* missing check IDs
* duplicate check IDs
* undefined severity levels
* ambiguous descriptions

---

### Cross-Reference Coverage

Verify:

* entity resolution covers all authority layers
* relationship consistency covers parent-child, marriage, sibling
* visual consistency covers baseline and inheritance
* identity consistency covers name, personality, education, occupation

Flag:

* missing entity types
* incomplete relationship coverage
* unvalidated visual claims

---

### Canon-Layer Coverage

Verify:

* all 5 canon layers are covered (Active, Historical, Cultural, Deferred, Candidate)
* layer boundary enforcement is complete
* rejected canon detection includes all known rejected concepts

Flag:

* missing layer coverage
* incomplete boundary rules
* missing rejected canon entries

---

### Authority Ownership Coverage

Verify:

* all 4 authority domains are covered (Character, Family, Visual, Experience)
* cross-layer boundary rules are complete
* no ownership gaps exist

Flag:

* missing domain coverage
* incomplete boundary rules
* ownership gaps

---

### Traceability Coverage

Verify:

* source attribution requirements are complete
* version tracking requirements are defined
* provenance chain is verifiable

Flag:

* missing attribution fields
* incomplete version tracking
* unverifiable provenance

---

### Governance Alignment

Verify:

* pipeline aligns with ADR-000 (Runtime Baseline)
* pipeline aligns with ADR-006 (Canon Layer Architecture)
* pipeline aligns with R-007, R-008, R-009
* no governance conflicts exist

Flag:

* ADR misalignment
* rule conflicts
* governance gaps

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Specification Completeness
3. Check Coverage Review
4. Governance Alignment
5. Findings
6. Coverage Gaps
7. Risk Assessment
8. Recommended Actions

---

## Status Levels

Use:

* PASS
* WARNING
* FAIL

Definitions:

PASS:
Check category fully covered.

WARNING:
Minor gaps or ambiguities detected.

FAIL:
Critical coverage gap or governance conflict.

---

## Remediation Policy

Do not modify repository files.

Do not create reports.

Do not create remediation artifacts.

Provide findings only.

Wait for explicit approval before proposing modifications.

---

## Success Criteria

* Repository remains unchanged.
* All 47 checks reviewed.
* Coverage gaps documented.
* Governance alignment verified.
* Results returned in chat only.
