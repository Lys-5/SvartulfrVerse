---
name: Cross Reference Audit
description: Use this skill when validating relationships, references, dependencies, links, ownership boundaries, or cross-authority consistency between characters, families, worlds, institutions, experiences, and canon layers. This skill identifies broken references and structural inconsistencies without modifying repository content.
---

# Cross Reference Audit

## Purpose

Validate repository-wide reference integrity.

This skill verifies that all authority layers, records, references, and relationships remain internally consistent.

This is an audit-only workflow.

---

## Validation Scope

Audit:

* characters
* families
* worlds
* institutions
* experiences
* historical records
* canon candidates

Verify consistency between authority layers.

---

## Required Checks

### Character → Family References

Verify:

* referenced family records exist
* dynasty references resolve correctly
* surname authority resolves correctly

Flag:

* missing family records
* broken dynasty references
* invalid surname ownership

---

### Character → Visual References

Verify:

* appearance references resolve
* visual inheritance references exist
* visual authority ownership respected

Flag:

* missing visual records
* invalid appearance references
* ownership violations

---

### Character → Experience References

Verify:

* experience references exist
* scenario links resolve correctly
* context ownership respected

Flag:

* broken experience references
* invalid context links
* scope violations

---

### Family Graph Integrity

Verify:

* parent-child relationships resolve
* marriages resolve
* dynasty membership resolves

Flag:

* orphaned nodes
* broken edges
* circular structures
* invalid relationships

---

### Authority Boundary Validation

Verify:

* ownership remains within authority layer
* no duplicated ownership exists
* no conflicting authority sources exist

Flag:

* cross-authority contamination
* duplicate ownership
* conflicting records

---

### Canon Layer Consistency

Verify:

* Active Canon references valid records
* Historical Canon references valid records
* Cultural Canon references valid records
* Deferred Canon references valid records
* Candidate Canon references valid records

Flag:

* missing layer assignments
* invalid layer references
* layer contamination

---

### Repository Reference Integrity

Verify:

* internal file references
* path references
* source attribution references

Flag:

* broken paths
* missing files
* orphaned references

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Reference Integrity Status
3. Authority Layer Review
4. Broken References
5. Ownership Violations
6. Findings
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
Reference validated.

WARNING:
Reference incomplete or ambiguous.

FAIL:
Reference broken or invalid.

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
* All references validated.
* Broken references documented.
* Authority boundaries verified.
* Results returned in chat only.
