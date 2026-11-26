---
alwaysApply: false
description: Apply when generating character cards, bot configurations, personality definitions, or any bot-platform-specific output from repository canon.
---
# R-008: Bot Generation Rules

**Authority:** ADR-003_Character_Authority.md, ADR-006_Canon_Layer_Architecture.md  
**Type:** Operational Rule — Bot Phase  
**Date:** 2026-06-08  
**Status:** ACTIVE (Canon Freeze v1 — Bot Phase)

---

## Purpose

These rules govern the generation of character cards, bot configurations, and platform-specific output for JanitorAI, SillyTavern, and other bot platforms. They ensure that all generated bots faithfully represent canonical data.

---

## R-008-BOT-001: Canon-Derived Generation

### Authority
ADR-003, ADR-006

### Rule
Character cards must be generated from repository canon.

### Rationale
Character cards are derived artifacts. They must reflect what is in database/ — nothing more, nothing less. Manual editing that contradicts canon introduces drift.

### Allowed
- Generating cards from C_Template.md-compliant records
- Pulling personality, biography, and visual data from character records
- Referencing family and relationship data from family records
- Using visual descriptions from visual authority records

### Prohibited
- Creating character cards for characters not in database/
- Manually injecting lore that contradicts canonical records
- Modifying canonical data during card generation
- Generating cards from memory or archive sources instead of database/

---

## R-008-BOT-002: No Manual Lore Injection

### Authority
ADR-003, Repository_Governance.md

### Rule
No manual lore injection outside approved authority layers.

### Rationale
Manual lore injection creates unvalidated content that contradicts the Single Source of Truth principle. All canon must flow from database/.

### Allowed
- Scenario-specific context from experiences/ records
- Relationship extensions from experience authority
- Temporary role assignments within defined scenarios

### Prohibited
- Adding character backstory not found in database/
- Creating family relationships not in family records
- Injecting supernatural elements (violates ADR-000)
- Referencing rejected canon material

---

## R-008-BOT-003: Content Traceability

### Authority
ADR-006, R-007-ENG-003

### Rule
Character card content must be traceable to database/ records.

### Rationale
Traceability enables validation and audit. If a card contains information, it must be possible to identify which canonical record it came from.

### Allowed
- Comments in card source referencing database/ file paths
- Metadata fields linking to canonical record IDs
- Version tracking showing which canon version produced the card

### Prohibited
- Cards with uncited lore or backstory
- Platform-specific content that cannot be mapped to database/
- "Creative interpretation" that deviates from canonical records

---

## R-008-BOT-004: Canon Layer Compliance

### Authority
ADR-006

### Rule
All generated content must comply with Canon Layer Architecture (ADR-006).

### Rationale
Canon layers exist to prevent contamination between fact, history, and myth. Generated assets must respect these boundaries.

### Allowed
- Active Canon content in primary card fields
- Historical Canon content in background/context fields
- Cultural Canon content in dialogue flavor (clearly marked)
- No Deferred or Candidate Canon content without Authority Decision

### Prohibited
- Treating Cultural Canon as Active Canon in generated output
- Treating Deferred Canon as Active Canon
- Treating Candidate Canon as approved
- Treating Rejected Canon as valid content

---

## Summary

| Rule ID | Description |
|---------|-------------|
| R-008-BOT-001 | Character cards must be generated from repository canon. |
| R-008-BOT-002 | No manual lore injection outside approved authority layers. |
| R-008-BOT-003 | Character card content must be traceable to database/ records. |
| R-008-BOT-004 | All generated content must comply with Canon Layer Architecture. |
