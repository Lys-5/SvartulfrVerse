---
name: Character Audit
description: Use this skill when auditing, validating, reviewing, importing, modifying, recovering, or troubleshooting character records. This skill verifies compliance with Character Authority, Family Authority, Visual Authority, Experience Authority, governance rules, and repository standards without modifying the repository.
---

# Character Audit

## Purpose

Perform a complete compliance audit of a character record against repository governance, authority boundaries, canonical ownership rules, and repository structure.

This is an audit-only workflow.

---

## Audit Scope

Validate the character against:

* R-002 Family Rules
* R-003 Character Rules
* R-004 Visual Rules
* R-005 Experience Rules
* R-006 Governance Rules

Verify compliance with:

* Character Authority
* Family Authority
* Visual Authority
* Experience Authority
* Canon Layer Architecture

---

## Required Checks

### Identity Validation

Verify:

* name consistency
* surname consistency
* pronouns
* identity ownership

Flag:

* conflicting identity data
* duplicated identity ownership
* non-canonical naming

---

### Genealogy Validation

Verify:

* genealogy ownership
* family references
* dynasty membership

Flag:

* genealogy stored in character file
* duplicated family data
* authority violations

---

### Appearance Validation

Verify:

* appearance references
* visual inheritance classification
* visual authority compliance

Flag:

* appearance ownership violations
* visual baseline contradictions
* duplicated visual data

---

### Experience Validation

Verify:

* scenario-scoped data
* occupation overrides
* relationship extensions

Flag:

* scenario data stored as canon
* residence ownership violations
* employment ownership violations

---

### Governance Validation

Verify:

* source traceability
* authority ownership
* canon compliance
* rejected canon contamination

Flag:

* undocumented imports
* authority conflicts
* governance violations

---

## Output Format

Return the audit report in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Compliance Results
3. Authority Boundary Review
4. Findings
5. Anomalies
6. Risk Assessment
7. Recommended Actions

---

## Severity Levels

Use:

* PASS
* WARNING
* FAIL

Definitions:

PASS:
No issue detected.

WARNING:
Potential issue or incomplete information.

FAIL:
Confirmed violation of repository rules.

---

## Remediation Policy

Do not modify repository files.

Do not create reports.

Do not create remediation artifacts.

Provide findings only.

Wait for explicit user approval before proposing modifications.

---

## Success Criteria

* Repository remains unchanged.
* All authority boundaries validated.
* All violations documented.
* Findings returned in chat only.
