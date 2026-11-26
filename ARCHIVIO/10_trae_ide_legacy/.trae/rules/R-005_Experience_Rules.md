---
alwaysApply: false
description: Apply when creating scenarios, experiences, roleplay contexts, runtime situations, occupations, residences, relationship extensions, or experience-layer content.
---
# R-005: Experience Rules

**Authority:** ADR-005_Experience_Authority.md  
**Type:** Operational Rule  
**Date:** 2026-06-07

---

## R-005-EXP-001: Experience Authority Role

### Authority
ADR-005

### Rule
Experience Authority Layer is a consumer, not an owner, of canonical data.

### Rationale
Experience Layer provides scenario context. It consumes data from Character, Family, and Visual authorities. It does not create new canon.

### Allowed
- Referencing Character Authority for identity
- Referencing Family Authority for genealogy
- Referencing Visual Authority for appearance
- Defining scenario-specific context

### Prohibited
- Creating new canonical facts
- Redefining character identity
- Redefining genealogy
- Redefining appearance

---

## R-005-EXP-002: Scenario Ownership

### Authority
ADR-005

### Rule
Experience Authority owns scenario framing and context state.

### Rationale
Scenario context is specific to each experience. Experience Authority defines location, time, circumstances, and situational state.

### Allowed
- Defining scenario location
- Defining scenario time
- Defining scenario circumstances
- Managing context state

### Prohibited
- Defining character identity
- Defining genealogy
- Defining appearance baseline
- Creating canonical facts

---

## R-005-EXP-003: Occupation Override

### Authority
ADR-005, ADR-003

### Rule
Experience Authority may override occupation for scenario scope only.

### Rationale
Baseline occupation belongs to Character Authority. Experience Authority may assign scenario-specific roles that temporarily override occupation.

### Allowed
- Scenario-specific occupation assignment
- Temporary role definitions
- Clear scope limitation (scenario only)

### Prohibited
- Changing baseline occupation
- Permanent occupation modification
- Occupation override without scenario scope

---

## R-005-EXP-004: Relationship Extension

### Authority
ADR-005, ADR-003

### Rule
Experience Authority may extend relationships; cannot remove core relationships.

### Rationale
Core relationships belong to Character Authority. Experience may add scenario-specific bonds but cannot remove canonical relationships.

### Allowed
- Adding scenario-specific relationships
- Temporary relationship dynamics
- Extension of existing relationship networks

### Prohibited
- Removing core family relationships
- Contradicting established bonds
- Permanent relationship modification

---

## R-005-EXP-005: No Identity Redefinition

### Authority
ADR-005, ADR-003

### Rule
Experience Authority cannot redefine character identity.

### Rationale
Identity (name, pronouns, self-conception) belongs to Character Authority. Experience provides context but cannot change who a character IS.

### Allowed
- Scenario-specific role assignments
- Contextual behavior expressions
- Temporary situational adaptations

### Prohibited
- Changing character name
- Changing character pronouns
- Redefining core personality
- Identity mutation across scenarios

---

## R-005-EXP-006: No Genealogy Redefinition

### Authority
ADR-005, ADR-002

### Rule
Experience Authority cannot redefine genealogy.

### Rationale
Genealogy belongs to Family Authority. Experience provides context but cannot change family relationships.

### Allowed
- Scenario-specific family dynamics
- Temporary relationship tensions
- Contextual family interactions

### Prohibited
- Changing parent-child relationships
- Adding or removing family members
- Redefining dynasty membership

---

## R-005-EXP-007: No Appearance Redefinition

### Authority
ADR-005, ADR-004

### Rule
Experience Authority cannot redefine appearance.

### Rationale
Appearance belongs to Visual Authority. Experience provides context but cannot change visual characteristics.

### Allowed
- Scenario-specific styling
- Temporary aesthetic adaptations
- Contextual appearance expressions

### Prohibited
- Changing baseline appearance
- Modifying visual inheritance
- Alternative appearance configurations

---

## R-005-EXP-008: Consumer Layer Status

### Authority
ADR-005, Architecture.md

### Rule
Experience Layer is always a consumer, never an authority source.

### Rationale
Worlds, scenarios, and experiences consume canonical data. They do not create it. This prevents drift and maintains single source of truth.

### Allowed
- Referencing authority layers
- Consuming canonical data
- Providing scenario context

### Prohibited
- Creating new canon
- Being treated as authority source
- Defining canonical facts

---

## R-005-EXP-009: Current Residence Scope

### Authority
ADR-005, Architecture.md

### Rule
Current residence is scenario-scoped, never stored as canonical fact.

### Rationale
Residence varies by scenario. Storing "current home" creates drift and contradicts the consumer model.

### Allowed
- Scenario-specific residence assignment
- Temporary location context
- Clear scope limitation

### Prohibited
- Storing residence in character files
- Defining permanent residence
- Residence ownership outside Experience Authority

---

## R-005-EXP-010: Employment Context Scope

### Authority
ADR-005, Architecture.md

### Rule
Current employment context is scenario-scoped, never stored as canonical fact.

### Rationale
Employment context varies by scenario. Storing "current job" creates drift and contradicts the consumer model.

### Allowed
- Scenario-specific employment assignment
- Temporary role context
- Clear scope limitation

### Prohibited
- Storing employment context in character files
- Defining permanent employment
- Employment context ownership outside Experience Authority

---

## Summary

| Rule ID | Description |
|---------|-------------|
| R-005-EXP-001 | Experience Authority Role (Consumer) |
| R-005-EXP-002 | Scenario Ownership |
| R-005-EXP-003 | Occupation Override |
| R-005-EXP-004 | Relationship Extension |
| R-005-EXP-005 | No Identity Redefinition |
| R-005-EXP-006 | No Genealogy Redefinition |
| R-005-EXP-007 | No Appearance Redefinition |
| R-005-EXP-008 | Consumer Layer Status |
| R-005-EXP-009 | Current Residence Scope |
| R-005-EXP-010 | Employment Context Scope |
