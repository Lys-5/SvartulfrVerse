---
name: Export Readiness
description: Use this skill when evaluating whether a character, authority record, lorebook source, or repository section is ready for export into JanitorAI, SillyTavern, Generic JSON, or future runtime engines. This skill validates export compatibility, traceability, authority compliance, and generation readiness without modifying repository content.
---

# Export Readiness

## Purpose

Determine whether repository content is ready for runtime generation and export.

This includes:

* Bot generation
* Lorebook generation
* Engine consumption
* Platform exports

This is an audit-only workflow.

---

## Validation Scope

Validate against:

* R-007 Engine Rules
* R-008 Bot Rules
* R-009 Lorebook Rules

Verify compliance with:

* ENGINE_SPECIFICATION
* BOT_EXPORT_SPECIFICATION
* LOREBOOK_SPECIFICATION
* VALIDATION_PIPELINE_SPECIFICATION

---

## Required Checks

### Traceability Validation

Verify:

* all exported content maps to canonical records
* source attribution exists
* authority ownership is identifiable

Flag:

* orphaned content
* undocumented sources
* non-traceable data

---

### Authority Validation

Verify:

* ownership boundaries respected
* no cross-authority contamination
* no duplicated authority data

Flag:

* ownership violations
* duplicated records
* conflicting authority sources

---

### Bot Generation Readiness

Verify:

* required character fields exist
* personality data exists
* biography data exists
* visual references exist
* family references resolve correctly

Flag:

* missing export fields
* unresolved references
* incomplete character records

---

### Lorebook Readiness

Verify:

* source records exist
* canon layer classification exists
* source attribution exists

Flag:

* missing canon layers
* uncited entries
* unresolved dependencies

---

### Engine Readiness

Verify:

* records are machine-consumable
* references resolve correctly
* validation pipeline can process records

Flag:

* broken paths
* invalid references
* export blockers

---

## Output Format

Return results in chat only.

Do not create files.

Structure:

1. Executive Summary
2. Export Status
3. Bot Readiness
4. Lorebook Readiness
5. Engine Readiness
6. Findings
7. Export Blockers
8. Recommended Actions

---

## Status Levels

Use:

* READY
* READY WITH WARNINGS
* NOT READY

Definitions:

READY:
Export can proceed immediately.

READY WITH WARNINGS:
Export possible but improvements recommended.

NOT READY:
Export blocked by unresolved issues.

---

## Remediation Policy

Do not modify repository files.

Do not generate exports.

Do not create reports.

Provide findings only.

Wait for explicit approval before recommending repository changes.

---

## Success Criteria

* Repository remains unchanged.
* Export blockers identified.
* Traceability validated.
* Runtime compatibility verified.
* Results returned in chat only.
