---
name: Lorebook Build Review
description: Use this skill when reviewing lorebook generation, validating entry structure, verifying canon-layer tagging, or auditing lorebook output against repository canon. This skill ensures lorebooks comply with LOREBOOK_SPECIFICATION and R-009_Lorebook_Rules without modifying repository content.
---

# Lorebook Build Review

## Purpose

Review and validate lorebook generation against the canonical lorebook specification and repository governance.

This skill ensures that all lorebook entries are properly sourced, canon-layer tagged, and traceable to database/ records.

This is an audit-only workflow.

---

## Review Scope

Audit:

* LOREBOOK_SPECIFICATION.md compliance
* R-009_Lorebook_Rules compliance
* Entry format compliance
* Canon-layer tagging accuracy
* Source attribution completeness

Validate against:

* ADR-005 Experience Authority
* ADR-006 Canon Layer Architecture
* R-007 Engine Rules
* R-009 Lorebook Rules
* All database/ authority records

---

## Required Checks

### Entry Format Compliance

Verify:

* every entry has a title
* every entry has exactly one canon layer tag
* every entry has source attribution
* every entry has an entry ID
* every entry has synchronization timestamp

Flag:

* missing titles
* missing or multiple canon layer tags
* missing source attribution
* missing entry IDs
* missing timestamps

---

### Canon-Layer Tagging Accuracy

Verify:

* Active Canon entries reference Active Canon records
* Historical Canon entries reference Historical Canon records
* Cultural Canon entries are marked as non-factual
* Deferred Canon entries are excluded from runtime
* Candidate Canon entries are excluded from runtime

Flag:

* incorrect layer assignment
* Cultural Canon presented as Active
* Deferred/Candidate included in runtime
* missing non-factual disclaimer on Cultural entries

---

### Source Attribution Completeness

Verify:

* primary source is identified
* supporting sources are listed (if applicable)
* authority domain is identified
* canon version is present
* all source paths point to existing database/ files

Flag:

* missing primary source
* incomplete supporting sources
* missing authority domain
* broken source paths
* missing canon version

---

### Content Accuracy

Verify:

* entry content matches source record
* no original content added
* no contradictions with database/ records
* no supernatural elements in Active entries
* no rejected canon concepts present

Flag:

* content mismatch with source
* original (unsourced) content
* contradictions with database/
* supernatural content in Active entries
* rejected canon contamination

---

### File Structure Compliance

Verify:

* lorebook file has metadata header
* disclaimer is present
* entries are properly delimited
* file follows top-level organization rules
* synchronization timestamp is current

Flag:

* missing metadata header
* missing disclaimer
* malformed entry delimiters
* incorrect file organization
* stale synchronization timestamp

---

### Generation Rule Compliance

Verify:

* R-009-LRB-001: Lorebooks are derived artifacts, not authority
* R-009-LRB-002: Must not contradict canon
* R-009-LRB-003: All entries reference database/ sources
* R-009-LRB-004: Must mark Active/Historical/Cultural

Flag:

* authority claim violations
* canon contradictions
* unsourced entries
* missing layer tags

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Entry Format Review
3. Canon-Layer Tagging Review
4. Source Attribution Review
5. Content Accuracy Review
6. File Structure Review
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
Lorebook fully compliant.

WARNING:
Non-critical issue or improvement opportunity.

FAIL:
Critical violation — lorebook must not be released.

---

## Remediation Policy

Do not modify repository files.

Do not create reports.

Do not generate lorebook files.

Provide findings only.

Wait for explicit approval before proposing modifications.

---

## Success Criteria

* Repository remains unchanged.
* Lorebook compliance verified.
* All entries validated.
* Canon-layer tagging confirmed.
* Results returned in chat only.
