---
name: Authority Boundary Audit
description: Use this skill when auditing authority boundaries, verifying ownership separation, detecting cross-authority contamination, or validating domain isolation between Character, Family, Visual, and Experience authorities. This skill ensures strict separation of concerns without modifying repository content.
---

# Authority Boundary Audit

## Purpose

Audit the strict separation of authority domains across the repository. Verify that no authority layer owns, defines, or modifies data belonging to another authority layer.

This is an audit-only workflow.

---

## Audit Scope

Audit all authority layers:

* Character Authority (database/characters/)
* Family Authority (database/families/)
* Visual Authority (database/worlds/)
* Experience Authority (database/experiences/)

Validate against:

* ADR-002 Family Authority
* ADR-003 Character Authority
* ADR-004 Visual Authority
* ADR-005 Experience Authority
* R-002 Family Rules
* R-003 Character Rules
* R-004 Visual Rules
* R-005 Experience Rules
* R-006 Governance Rules

---

## Required Checks

### Character Authority Boundary

Verify:

* character files contain identity, personality, biography, skills, education
* character files do NOT contain genealogical definitions
* character files do NOT contain visual baseline definitions
* character files do NOT contain scenario-scoped data as canon

Flag:

* genealogy stored in character file
* visual baseline defined in character file
* scenario data stored as canonical fact
* family relationships defined in character file

---

### Family Authority Boundary

Verify:

* family files contain genealogy, marriages, parent-child, surnames
* family files do NOT contain character identity data
* family files do NOT contain personality or biography
* family files do NOT contain visual appearance data

Flag:

* character identity in family file
* personality data in family file
* visual data in family file
* experience data in family file

---

### Visual Authority Boundary

Verify:

* visual files contain appearance baselines, inheritance rules, color palettes
* visual files do NOT contain character identity data
* visual files do NOT contain genealogical data
* visual files do NOT contain scenario data

Flag:

* character identity in visual file
* genealogy in visual file
* scenario data in visual file
* family relationships in visual file

---

### Experience Authority Boundary

Verify:

* experience files contain scenario framing, context, roles, overrides
* experience files do NOT contain canonical identity data
* experience files do NOT redefine character identity
* experience files do NOT create new canon

Flag:

* canonical identity in experience file
* new genealogy in experience file
* permanent residence stored as canon
* occupation override treated as canonical

---

### Cross-Reference Integrity

Verify:

* character files reference (not define) family data
* character files reference (not define) visual data
* experience files reference (not redefine) character identity
* all references resolve to existing authority records

Flag:

* broken references
* self-referencing authority violations
* unresolved authority references
* circular authority dependencies

---

### Template Compliance

Verify:

* C_Template.md contains only Character Authority fields
* Family_Template.md contains only Family Authority fields
* W_Template.md contains only Visual Authority fields
* Ex_Template.md contains only Experience Authority fields

Flag:

* cross-authority fields in templates
* missing required authority fields
* authority field duplication across templates

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Authority Layer Review
3. Cross-Contamination Detection
4. Boundary Violations
5. Template Compliance
6. Findings
7. Risk Assessment
8. Recommended Actions

---

## Severity Levels

Use:

* PASS
* WARNING
* FAIL

Definitions:

PASS:
Authority boundary intact.

WARNING:
Potential boundary ambiguity or incomplete separation.

FAIL:
Confirmed cross-authority contamination.

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
* All contamination documented.
* Template compliance verified.
* Results returned in chat only.
