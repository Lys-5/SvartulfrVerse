---
name: Bot Build Review
description: Use this skill when reviewing bot character card generation, validating export schema compliance, verifying platform compatibility, or auditing bot output against repository canon. This skill ensures bot exports comply with BOT_EXPORT_SPECIFICATION and R-008_Bot_Rules without modifying repository content.
---

# Bot Build Review

## Purpose

Review and validate bot character card generation against the canonical export schema and repository governance.

This skill ensures that all bot exports are traceable, platform-compatible, and canonically accurate.

This is an audit-only workflow.

---

## Review Scope

Audit:

* BOT_EXPORT_SPECIFICATION.md compliance
* R-008_Bot_Rules compliance
* Platform schema compliance (JanitorAI, SillyTavern, Generic JSON)
* Field mapping accuracy
* Provenance metadata completeness

Validate against:

* ADR-003 Character Authority
* ADR-006 Canon Layer Architecture
* R-007 Engine Rules
* R-008 Bot Rules
* Character records in database/characters/

---

## Required Checks

### Schema Compliance

Verify:

* all required fields are present per target platform
* field types match platform schema
* no extra fields violate platform constraints
* extensions.svartulfrverse metadata is present

Flag:

* missing required fields
* type mismatches
* schema violations
* missing provenance metadata

---

### Field Mapping Accuracy

Verify:

* each bot field maps to exactly one authoritative source
* no field is populated from memory or inference
* visual fields resolve to Visual Authority
* relationship fields resolve to Family Authority
* identity fields resolve to Character Authority

Flag:

* unmapped fields
* inferred data
* wrong authority source
* missing source attribution

---

### Canon Compliance

Verify:

* no supernatural elements in Active Canon exports
* no rejected canon concepts present
* canon layer tags are correct
* Cultural Canon is not presented as Active

Flag:

* supernatural content
* rejected canon contamination
* incorrect layer tags
* cultural canon misclassified

---

### Platform Compatibility

Verify:

* JanitorAI JSON structure is valid
* SillyTavern Character Card V3 structure is valid
* Generic JSON schema is valid
* all platform-specific constraints are respected

Flag:

* invalid JSON structure
* missing platform-specific fields
* constraint violations
* format errors

---

### Provenance Completeness

Verify:

* source_files list is complete
* canon_version is present
* generation_timestamp is present
* validation_status is present
* authority domain is identified

Flag:

* missing provenance fields
* incomplete source list
* missing timestamps
* unvalidated output

---

### Generation Rule Compliance

Verify:

* R-008-BOT-001: Cards generated from repository canon only
* R-008-BOT-002: No manual lore injection
* R-008-BOT-003: Content traceable to database/ records
* R-008-BOT-004: Canon Layer Architecture compliance

Flag:

* canon-only violations
* manual lore injection
* untraceable content
* layer architecture violations

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Schema Compliance Review
3. Field Mapping Review
4. Canon Compliance Review
5. Platform Compatibility
6. Provenance Review
7. Findings
8. Risk Assessment
9. Recommended Actions

---

## Status Levels

Use:

* PASS
* WARNING
* FAIL

Definitions:

PASS:
Bot export fully compliant.

WARNING:
Non-critical issue or improvement opportunity.

FAIL:
Critical violation — export must not proceed.

---

## Remediation Policy

Do not modify repository files.

Do not create reports.

Do not generate bot exports.

Provide findings only.

Wait for explicit approval before proposing modifications.

---

## Success Criteria

* Repository remains unchanged.
* Bot export compliance verified.
* All platform schemas validated.
* Provenance completeness confirmed.
* Results returned in chat only.
