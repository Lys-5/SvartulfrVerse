---
alwaysApply: false
description: Apply when creating, importing, auditing, recovering, validating, or modifying character records, identity data, biographies, occupations, skills, or personality definitions.
---
# R-003: Character Rules

**Authority:** ADR-003_Character_Authority.md  
**Type:** Operational Rule  
**Date:** 2026-06-07

---

## R-003-CHR-001: Identity Ownership

### Authority
ADR-003

### Rule
Character Authority Layer owns all identity data.

### Rationale
Identity is the core of character definition. Name, pronouns, and self-conception are immutable and owned exclusively by Character Authority.

### Allowed
- Storing identity in Character Authority
- Character files owning their identity
- Immutable identity once established

### Prohibited
- Other layers defining character identity
- Mutable identity elements
- Identity duplication across layers

---

## R-003-CHR-002: Personality Ownership

### Authority
ADR-003

### Rule
Character Authority owns all personality and behavioral baseline data.

### Rationale
Personality defines who a character IS. This is core character data, not scenario-specific behavior.

### Allowed
- Storing personality in Character Authority
- Stable behavioral traits across scenarios
- Character files defining their personality

### Prohibited
- Experience Layer redefining personality
- Scenario-specific personality mutations
- Personality drift across contexts

---

## R-003-CHR-003: Biography Ownership

### Authority
ADR-003

### Rule
Character Authority owns all biography data with append-only semantics.

### Rationale
Biography is personal history. New experiences may be added, but existing history cannot be contradicted.

### Allowed
- Storing biography in Character Authority
- Append-only updates (new experiences)
- Consistent historical timeline

### Prohibited
- Contradicting established biography
- Removing historical events
- Alternative timeline variants

---

## R-003-CHR-004: Physical Sex Ownership

### Authority
ADR-003

### Rule
Character Authority owns biological sex characteristics as immutable baseline.

### Rationale
Physical sex is baseline physical reality. This is distinct from gender identity (personality domain).

### Allowed
- Storing physical sex in Character Authority
- Immutable biological characteristics
- Reference by other layers (read-only)

### Prohibited
- Mutable physical sex
- Other layers defining biological characteristics
- Contradicting established physical baseline

---

## R-003-CHR-005: Skills Ownership

### Authority
ADR-003

### Rule
Character Authority owns all skills and competencies with append-only semantics.

### Rationale
Skills are learned capabilities. New skills may be added, but existing skills cannot be removed.

### Allowed
- Storing skills in Character Authority
- Append-only updates (new skills)
- Skill progression over time

### Prohibited
- Removing established skills
- Contradicting skill history
- Alternative skill configurations

---

## R-003-CHR-006: Baseline Occupation Ownership

### Authority
ADR-003, ADR-005

### Rule
Character Authority owns baseline occupation; Experience Authority owns occupation override.

### Rationale
Occupation has two domains: baseline professional identity (Character) and scenario-specific role (Experience).

### Allowed
- Character Authority defining baseline occupation
- Experience Authority overriding for specific scenarios
- Clear separation of ownership

### Prohibited
- Experience Authority changing baseline occupation
- Character Authority defining scenario-specific roles
- Occupation ownership confusion

---

## R-003-CHR-007: No Genealogy in Character Files

### Authority
ADR-003, Architecture.md

### Rule
Character files must NOT define genealogy.

### Rationale
Genealogy belongs to Family Authority. Character files reference family relationships; they do not own them.

### Allowed
- Character files referencing family relationships (read-only)
- Querying Family Authority for kinship
- Single source of truth for genealogy

### Prohibited
- Storing parent-child in character files
- Defining family structure in character files
- Duplicating genealogy data

---

## R-003-CHR-008: No Scenario Data in Character Files

### Authority
ADR-003, Architecture.md

### Rule
Character files must NOT contain scenario-specific data.

### Rationale
Scenario data belongs to Experience Authority. Character files define identity; scenarios define context.

### Allowed
- Character files defining stable identity
- Experience Authority defining scenario context
- Clear separation of concerns

### Prohibited
- Storing current residence in character files
- Storing current occupation context in character files
- Scenario-specific relationship data in character files

---

## R-003-CHR-009: Cross-Authority Prohibition

### Authority
ADR-003

### Rule
Character Authority cannot define data owned by other authorities.

### Rationale
Each authority layer has exclusive ownership of its domain. Cross-authority ownership creates conflicts.

### Allowed
- Character Authority owning identity, personality, biography
- Character Authority referencing other authorities (read-only)
- Clear ownership boundaries

### Prohibited
- Character Authority defining genealogy
- Character Authority defining appearance baseline
- Character Authority defining scenario context

---

## R-003-CHR-010: Core Relationships Baseline

### Authority
ADR-003

### Rule
Character Authority owns baseline core relationships; Experience Authority may extend.

### Rationale
Core relationships (family, significant bonds) are part of character identity. Experience may add scenario-specific relationships.

### Allowed
- Character Authority defining core relationships
- Experience Authority extending for specific scenarios
- Extension only (cannot remove core relationships)

### Prohibited
- Experience Authority removing core relationships
- Character Authority defining scenario-specific relationships
- Relationship ownership confusion

---

## Summary

| Rule ID | Description |
|---------|-------------|
| R-003-CHR-001 | Identity Ownership |
| R-003-CHR-002 | Personality Ownership |
| R-003-CHR-003 | Biography Ownership |
| R-003-CHR-004 | Physical Sex Ownership |
| R-003-CHR-005 | Skills Ownership |
| R-003-CHR-006 | Baseline Occupation Ownership |
| R-003-CHR-007 | No Genealogy in Character Files |
| R-003-CHR-008 | No Scenario Data in Character Files |
| R-003-CHR-009 | Cross-Authority Prohibition |
| R-003-CHR-010 | Core Relationships Baseline |
