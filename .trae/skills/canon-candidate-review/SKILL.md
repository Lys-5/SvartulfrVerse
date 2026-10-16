---
name: Canon Candidate Review
description: Use this skill when evaluating new canon proposals, recovered archive material, imported records, unresolved evidence, or content stored in canon_candidates. This skill performs a governance review and produces an approval recommendation without modifying the repository.
---

# Canon Candidate Review

## Purpose

Evaluate proposed canon before it enters the repository.

This skill enforces the Canon Recovery Workflow and Canon Freeze policies.

This is an audit-only workflow.

---

## Review Scope

Validate against:

* R-000 Runtime Rules
* R-006 Governance Rules
* ADR-006 Canon Layer Architecture

Review:

* candidate records
* recovered archive content
* imported material
* unresolved evidence
* deferred canon proposals

---

## Required Checks

### Evidence Review

Verify:

* evidence exists
* evidence sources are documented
* evidence is traceable

Classify:

* Stable
* Variant
* Conflicting
* Unsupported

Flag:

* unsupported claims
* undocumented sources
* missing evidence

---

### Canon Recovery Workflow Validation

Verify completion of:

1. Research
2. Recovery Audit
3. Architecture Review
4. Authority Decision
5. Import Readiness

Flag:

* skipped workflow stages
* incomplete reviews
* undocumented decisions

---

### Authority Ownership Validation

Verify:

* correct authority destination
* ownership boundaries respected
* no cross-authority contamination

Flag:

* ownership conflicts
* wrong destination layer
* duplicated authority ownership

---

### Canon Freeze Validation

Verify:

* no rejected canon is reintroduced
* no prohibited recovery attempts exist
* no freeze violations exist

Flag:

* rejected canon contamination
* prohibited recovery requests
* unauthorized canon creation

---

### Canon Layer Classification

Determine:

* Active Canon
* Historical Canon
* Cultural Canon
* Deferred Canon
* Candidate Canon

Flag:

* missing classification
* incorrect classification
* unresolved status

---

## Recommendation Engine

Produce exactly one recommendation:

### APPROVE

Evidence is sufficient.

Authority ownership is correct.

Candidate may proceed to Authority Decision.

---

### DEFER

Evidence exists but requires clarification.

Additional review required.

Candidate remains unresolved.

---

### REJECT

Evidence insufficient or conflicts with governance.

Candidate must not enter repository.

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Evidence Assessment
3. Governance Review
4. Authority Review
5. Canon Layer Classification
6. Findings
7. Risks
8. Final Recommendation

---

## Severity Levels

Use:

* PASS
* WARNING
* FAIL

---

## Remediation Policy

Do not modify repository files.

Do not import content.

Do not create reports.

Do not update canon.

Provide findings only.

Wait for explicit approval before any repository modification.

---

## Success Criteria

* Repository remains unchanged.
* Candidate properly classified.
* Governance validated.
* Recommendation clearly produced.
* Results returned in chat only.
