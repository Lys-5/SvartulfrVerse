---
name: Repository Hardening
description: Use this skill when evaluating repository structure, governance consistency, documentation alignment, duplicate content, orphaned files, migration residue, path integrity, or implementation readiness. This skill identifies structural weaknesses and hardening opportunities without modifying repository content.
---

# Repository Hardening

## Purpose

Evaluate repository health, structural consistency, governance alignment, and implementation readiness.

This skill is intended for pre-implementation reviews, stabilization phases, migration validation, and repository maintenance.

This is an audit-only workflow.

---

## Validation Scope

Audit:

* repository structure
* governance documents
* ADRs
* specifications
* rules
* database records
* templates
* documentation

Verify alignment with:

* Repository_Scope
* Repository_Governance
* Repository_Configuration
* Architecture
* ADRs
* Rules

---

## Required Checks

### Repository Structure

Verify:

* directory structure compliance
* expected folders exist
* naming conventions respected

Flag:

* structural deviations
* inconsistent layouts
* unexpected folders

---

### Duplicate Analysis

Detect:

* duplicated files
* duplicated governance documents
* duplicated ADRs
* duplicated specifications
* duplicated templates

Flag:

* competing authority sources
* duplicate ownership
* redundant documentation

---

### Documentation Consistency

Verify:

* README alignment
* Architecture alignment
* Governance alignment
* Specification alignment

Flag:

* outdated documentation
* conflicting documentation
* stale references

---

### Migration Residue Detection

Verify:

* deprecated references removed
* old repository names removed
* legacy migration artifacts removed

Flag:

* residual migration paths
* obsolete references
* deprecated structures

---

### Repository Integrity

Verify:

* internal references resolve
* paths remain valid
* ownership boundaries respected

Flag:

* broken references
* invalid paths
* ownership conflicts

---

### Implementation Readiness

Verify:

* engine prerequisites satisfied
* export prerequisites satisfied
* validation prerequisites satisfied

Flag:

* missing dependencies
* unresolved blockers
* incomplete preparation

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Repository Health Score
3. Structural Review
4. Governance Review
5. Documentation Review
6. Findings
7. Risk Assessment
8. Hardening Recommendations

---

## Status Levels

Use:

* PASS
* WARNING
* FAIL

Definitions:

PASS:
No issue detected.

WARNING:
Issue exists but does not block implementation.

FAIL:
Issue blocks implementation or creates governance risk.

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
* Structural integrity verified.
* Governance consistency verified.
* Implementation blockers identified.
* Results returned in chat only.
