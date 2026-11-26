---
alwaysApply: false
description: Apply when developing engine systems, runtime logic, query layers, state management, context building, or any system that interacts with canonical data.
---
# R-007: Engine Rules

**Authority:** ADR-000_Runtime_Baseline.md, Architecture.md  
**Type:** Operational Rule — Engine Phase  
**Date:** 2026-06-08  
**Status:** ACTIVE (Canon Freeze v1 — Engine Phase)

---

## Purpose

These rules govern all engine development, runtime systems, query layers, and any software that interacts with canonical data. They ensure that runtime systems serve canon — never override it.

---

## R-007-ENG-001: Canon Authority

### Authority
ADR-000, ADR-006, Repository_Governance.md

### Rule
Canon data is source of truth. Runtime systems cannot override canon.

### Rationale
The database/ directory is the Single Source of Truth. Engines are query and presentation layers. They may organize, filter, and present canonical data — but never modify, override, or contradict it.

### Allowed
- Querying database/ records
- Organizing canon data for runtime presentation
- Filtering canon data by context (scenario, timeline, etc.)
- Caching canonical data for performance
- Validating runtime output against canonical records

### Prohibited
- Overriding canonical values at runtime
- Generating canonical facts not present in database/
- Modifying authority boundaries through engine logic
- Treating engine output as equivalent to canonical data

---

## R-007-ENG-002: Runtime Separation

### Authority
Architecture.md, ADR-000

### Rule
Engine logic and canon data remain separate domains.

### Rationale
Mixing engine behavior with canonical data creates migration fragility and prevents independent evolution of runtime systems.

### Allowed
- Separate modules for engine logic and data access
- Configuration files independent of canon records
- Platform-specific adapters that read from database/

### Prohibited
- Embedding engine logic in database/ records
- Embedding canonical data in engine code
- Creating dependencies from database/ to engine modules

---

## R-007-ENG-003: Traceability

### Authority
ADR-006, Repository_Governance.md

### Rule
All engine output must be traceable to canonical records.

### Rationale
If generated content cannot be traced to a specific canonical record, it cannot be validated for compliance.

### Allowed
- Output records that reference source database/ file paths
- Cross-reference IDs linking generated content to source
- Audit trails showing which canon data produced which output

### Prohibited
- Generated content with no canonical source attribution
- Orphaned output that cannot be mapped back to database/
- Black-box generation with no provenance

---

## R-007-ENG-004: Validation Pipeline

### Authority
ADR-000, Repository_Governance.md, ADR-006

### Rule
Generated assets require validation against authority records before release.

### Rationale
Unvalidated output risks propagating errors, contradicting canon, or introducing drift.

### Allowed
- Automated validation checks against frozen templates
- Authority boundary validation (no ownership violations)
- Canon layer classification verification
- Cross-reference integrity checks

### Prohibited
- Release of unvalidated generated assets
- Bypassing validation for "minor" changes
- Assuming generation is correct without verification

---

## R-007-ENG-005: Validation Pipeline Execution

### Authority
ADR-000, VALIDATION_PIPELINE_SPECIFICATION.md, R-007-ENG-004

### Rule
All generated assets must pass the 47-check validation pipeline before release. No export, bot card, or lorebook may be released without successful pipeline execution.

### Rationale
The validation pipeline is the mandatory gate between repository canon and runtime output. Unvalidated output risks propagating errors, contradicting canon, or introducing drift into downstream systems.

### Allowed
- Running full validation pipeline (all 47 checks) before any release
- Automated validation via validation_engine
- Manual review for edge cases not covered by automated checks
- Releasing assets with `valid` or `warning` status

### Prohibited
- Releasing assets with `invalid` status
- Partial validation (skipping check categories)
- Bypassing pipeline for "minor" or "urgent" changes
- Treating pipeline as optional for any output type

---

## R-007-ENG-006: Validation Coverage Requirement

### Authority
VALIDATION_PIPELINE_SPECIFICATION.md, ADR-006

### Rule
Validation coverage must include all 47 checks across 4 categories: Cross-Reference (CR), Canon-Layer (CL), Authority Ownership (AO), and Traceability (TR). No category may be skipped.

### Rationale
Each check category protects a different governance dimension. Partial validation leaves gaps that allow drift, contamination, or untraceable output to reach runtime systems.

### Allowed
- Automated implementation of all 47 checks
- Coverage reporting showing pass/fail per category
- Progressive implementation with documented coverage gaps
- Validation Pipeline Review skill for coverage audits

### Prohibited
- Skipping any of the 4 check categories
- Releasing output with incomplete coverage
- Treating any check category as optional
- Coverage gaps without documented remediation plan

---

## Summary

| Rule ID | Description |
|---------|-------------|
| R-007-ENG-001 | Canon data is source of truth. Runtime systems cannot override canon. |
| R-007-ENG-002 | Engine logic and canon data remain separate domains. |
| R-007-ENG-003 | All engine output must be traceable to canonical records. |
| R-007-ENG-004 | Generated assets require validation against authority records before release. |
| R-007-ENG-005 | All generated assets must pass the 47-check validation pipeline before release. |
| R-007-ENG-006 | Validation coverage must include all 47 checks across 4 categories. |
