---
name: Engine Contract Validation
description: Use this skill when validating engine architecture, specifications, runtime contracts, exporter compatibility, validation pipelines, or implementation readiness. This skill verifies consistency between engine specifications, repository governance, authority boundaries, and runtime expectations without modifying repository content.
---

# Engine Contract Validation

## Purpose

Validate consistency between engine specifications, authority architecture, governance rules, export systems, and runtime contracts.

This skill ensures that implementation remains aligned with repository architecture.

This is an audit-only workflow.

---

## Validation Scope

Audit:

* ENGINE_SPECIFICATION
* BOT_EXPORT_SPECIFICATION
* LOREBOOK_SPECIFICATION
* VALIDATION_PIPELINE_SPECIFICATION

Validate against:

* ADR-000 Runtime Baseline
* ADR-002 Family Authority
* ADR-003 Character Authority
* ADR-004 Visual Authority
* ADR-005 Experience Authority
* ADR-006 Canon Layer Architecture
* R-007 Engine Rules
* R-008 Bot Rules
* R-009 Lorebook Rules

---

## Required Checks

### Engine Boundary Validation

Verify:

* engines respect authority ownership
* engines consume canon without owning canon
* runtime remains downstream from repository

Flag:

* ownership violations
* canon creation logic
* authority overlap

---

### Engine Specification Consistency

Verify:

* engine responsibilities are clearly defined
* engine scopes do not overlap
* engine outputs remain traceable

Flag:

* duplicated responsibilities
* undefined responsibilities
* conflicting engine definitions

---

### Export Contract Validation

Verify:

* bot exports remain compatible with engine outputs
* lorebook exports remain compatible with canon layers
* export specifications remain aligned

Flag:

* incompatible contracts
* missing export requirements
* specification drift

---

### Validation Pipeline Compatibility

Verify:

* validation requirements exist
* validation coverage remains complete
* outputs are verifiable

Flag:

* missing validation stages
* unverifiable outputs
* incomplete coverage

---

### Runtime Governance Compliance

Verify:

* runtime systems remain consumers
* repository remains authority
* traceability remains possible

Flag:

* governance violations
* runtime authority drift
* non-traceable outputs

---

### Future Implementation Readiness

Verify:

* specifications can be implemented
* dependencies are clearly defined
* build sequence is coherent

Flag:

* implementation blockers
* circular dependencies
* undefined prerequisites

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Contract Consistency Review
3. Authority Boundary Review
4. Specification Compatibility
5. Validation Coverage
6. Findings
7. Risks
8. Recommended Actions

---

## Status Levels

Use:

* PASS
* WARNING
* FAIL

Definitions:

PASS:
Contract validated.

WARNING:
Potential incompatibility or ambiguity.

FAIL:
Confirmed architectural conflict.

---

## Remediation Policy

Do not modify repository files.

Do not create reports.

Do not generate implementation code.

Provide findings only.

Wait for explicit approval before recommending modifications.

---

## Success Criteria

* Repository remains unchanged.
* Engine contracts validated.
* Specification consistency verified.
* Governance compliance verified.
* Results returned in chat only.
