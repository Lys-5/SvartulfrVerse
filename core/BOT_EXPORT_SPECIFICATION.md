# BOT EXPORT SPECIFICATION

**Status:** CANONICAL  
**Date:** 2026-06-08  
**Authority:** ADR-003, ADR-006, R-008_Bot_Rules, R-007_Engine_Rules  
**Version:** 1.0 — Canon Freeze v1

---

## Purpose

This document defines the canonical export schema for character card generation across all supported bot platforms. Every bot field is mapped to authoritative repository sources. All generated output must comply with R-008_Bot_Rules.

**Authority:** No character card may be generated without traceable provenance to database/ records.

---

## Export Platforms

| Platform | Format | Target Use |
|----------|--------|------------|
| JanitorAI | JSON + Markdown | JanitorAI character cards |
| SillyTavern | JSON (Character Card V3) | SillyTavern character cards |
| Generic JSON | Structured JSON | Cross-platform interchange |

---

## Canonical Export Schema

### Field Mapping — All Platforms

Every bot field maps to exactly one authoritative source. No field may be populated from memory, inference, or research archives.

#### Core Identity Fields

| Bot Field | Repository Source | Authority | Access Path |
|-----------|-------------------|-----------|-------------|
| `name` | C_Template → Identity.Name | Character Authority | `database/characters/C_[Name].md` |
| `aliases` | C_Template → Identity.Aliases | Character Authority | `database/characters/C_[Name].md` |
| `age` | Computed: Birth Date → Current Year | Character Authority | `database/characters/C_[Name].md` |
| `birth_date` | C_Template → Identity.Birth Date | Character Authority | `database/characters/C_[Name].md` |
| `nationality` | C_Template → Identity.Nationality | Character Authority | `database/characters/C_[Name].md` |
| `gender` | C_Template → Identity.Gender | Character Authority | `database/characters/C_[Name].md` |
| `pronouns` | C_Template → Identity.Pronouns | Character Authority | `database/characters/C_[Name].md` |
| `dynasty` | F_Douglas_Bloodmoon → Membership | Family Authority | `database/families/F_Douglas_Bloodmoon.md` |
| `surname` | F_Surname_Authority → Rules | Family Authority | `database/families/F_Surname_Authority.md` |

#### Visual Fields

| Bot Field | Repository Source | Authority | Access Path |
|-----------|-------------------|-----------|-------------|
| `hair_color` | W_Visual_Baseline or C record → Visual | Visual Authority | `database/worlds/W_Visual_Baseline.md` or `database/characters/C_[Name].md` |
| `eye_color` | W_Visual_Baseline or C record → Visual | Visual Authority | `database/worlds/W_Visual_Baseline.md` or `database/characters/C_[Name].md` |
| `build` | C record → Physical.Build | Visual Authority | `database/characters/C_[Name].md` |
| `height` | C record → Physical.Height | Visual Authority | `database/characters/C_[Name].md` |
| `visual_classification` | W_Visual_Inheritance → Classification | Visual Authority | `database/worlds/W_Visual_Inheritance.md` |
| `appearance_description` | Composite: Visual fields above | Visual Authority | Engine-aggregated |

#### Psychology & Personality Fields

| Bot Field | Repository Source | Authority | Access Path |
|-----------|-------------------|-----------|-------------|
| `personality` | C_Template → Psychology.Core Traits | Character Authority | `database/characters/C_[Name].md` |
| `fears` | C_Template → Psychology.Fears | Character Authority | `database/characters/C_[Name].md` |
| `motivations` | C_Template → Psychology.Motivations | Character Authority | `database/characters/C_[Name].md` |
| `behavioral_patterns` | C_Template → Psychology.Behavioral Patterns | Character Authority | `database/characters/C_[Name].md` |

#### Capability Fields

| Bot Field | Repository Source | Authority | Access Path |
|-----------|-------------------|-----------|-------------|
| `skills` | C_Template → Capabilities.Skills | Character Authority | `database/characters/C_[Name].md` |
| `education` | C_Template → Capabilities.Education | Character Authority | `database/characters/C_[Name].md` |
| `occupation` | C_Template → Capabilities.Occupation | Character Authority | `database/characters/C_[Name].md` |

#### Relationship Fields

| Bot Field | Repository Source | Authority | Access Path |
|-----------|-------------------|-----------|-------------|
| `parents` | F_Parent_Child → Parent records | Family Authority | `database/families/F_Parent_Child.md` |
| `siblings` | Computed from F_Parent_Child | Family Authority | `database/families/F_Parent_Child.md` |
| `spouse` | F_Marriages → Marriage records | Family Authority | `database/families/F_Marriages.md` |
| `children` | F_Parent_Child → Child records | Family Authority | `database/families/F_Parent_Child.md` |
| `non_familial_relationships` | C_Template → Relationships | Character Authority | `database/characters/C_[Name].md` |

#### Biography Fields

| Bot Field | Repository Source | Authority | Access Path |
|-----------|-------------------|-----------|-------------|
| `backstory` | C_Template → History | Character Authority | `database/characters/C_[Name].md` |
| `character_memory` | C_Template → History (key events) | Character Authority | `database/characters/C_[Name].md` |
| `current_status` | C_Template → Current Status | Character Authority | `database/characters/C_[Name].md` |

---

## Platform-Specific Schemas

### JanitorAI Export

**Format:** JSON with embedded Markdown

```json
{
  "name": "{{name}}",
  "description": "{{appearance_description}}",
  "personality": "{{personality}}",
  "scenario": "{{default_scenario_context}}",
  "first_mes": "{{opening_dialogue}}",
  "mes_example": "{{dialogue_examples}}",
  "system_prompt": "{{system_prompt}}",
  "creator_notes": "{{backstory}}",
  "post_history_instructions": "{{behavioral_constraints}}",
  "tags": ["{{canon_layer}}", "{{dynasty}}", "{{character_id}}"],
  "creator": "SvartulfrVerse",
  "character_version": "1.0",
  "extensions": {
    "svartulfrverse": {
      "canon_id": "{{character_id}}",
      "canon_layer": "{{canon_layer}}",
      "provenance": ["{{source_file_paths}}"],
      "authority": "{{authority_domain}}",
      "visual_classification": "{{visual_classification}}",
      "dynasty": "{{dynasty}}",
      "validation_status": "validated"
    }
  }
}
```

**JanitorAI Field Mapping:**

| JanitorAI Field | Source | Notes |
|-----------------|--------|-------|
| `name` | Character Identity.Name | Required |
| `description` | Composite visual + personality | Max 5000 chars |
| `personality` | Psychology.Core Traits | Formatted as prose |
| `scenario` | Default experience context | From Experience Authority |
| `first_mes` | Generated from personality + context | Must not contradict canon |
| `mes_example` | Generated from personality | Must reflect canonical speech patterns |
| `system_prompt` | Composite: identity + constraints | Includes authority boundaries |
| `creator_notes` | History + backstory | For bot context only |
| `tags` | Canon layer + dynasty + ID | Must include `SvartulfrVerse` |
| `extensions.svartulfrverse` | Engine metadata | Traceability data |

### SillyTavern Export

**Format:** Character Card V3 (JSON)

```json
{
  "name": "{{name}}",
  "description": "{{personality_and_appearance}}",
  "personality": "{{personality_summary}}",
  "scenario": "{{scenario_context}}",
  "first_mes": "{{opening_dialogue}}",
  "mes_example": "{{dialogue_examples}}",
  "system_prompt": "{{system_prompt}}",
  "creator_notes": "{{backstory_and_notes}}",
  "post_history_instructions": "{{behavioral_constraints}}",
  "tags": ["{{canon_layer}}", "{{dynasty}}"],
  "creator": "SvartulfrVerse",
  "character_version": "1.0",
  "spec": "chara_card_v3",
  "spec_version": "3.0",
  "data": {
    "name": "{{name}}",
    "description": "{{full_description}}",
    "personality": "{{personality}}",
    "scenario": "{{scenario}}",
    "first_mes": "{{first_mes}}",
    "mes_example": "{{mes_example}}",
    "creator_notes": "{{creator_notes}}",
    "system_prompt": "{{system_prompt}}",
    "post_history_instructions": "{{post_history_instructions}}",
    "tags": ["{{tags}}"],
    "creator": "SvartulfrVerse",
    "character_version": "1.0",
    "extensions": {
      "svartulfrverse": {
        "canon_id": "{{character_id}}",
        "canon_layer": "active",
        "provenance": ["{{source_file_paths}}"],
        "authority": "{{authority_domain}}",
        "dynasty": "{{dynasty}}",
        "visual_classification": "{{visual_classification}}",
        "validation_status": "validated",
        "generation_timestamp": "{{iso_timestamp}}",
        "canon_version": "1.0"
      }
    }
  }
}
```

### Generic JSON Export

**Format:** Structured JSON for cross-platform interchange

```json
{
  "schema_version": "1.0",
  "schema": "svartulfrverse_character_v1",
  "character": {
    "id": "{{character_id}}",
    "canon_layer": "{{canon_layer}}",
    "identity": {
      "name": "{{name}}",
      "aliases": ["{{aliases}}"],
      "age": "{{age}}",
      "birth_date": "{{birth_date}}",
      "nationality": "{{nationality}}",
      "gender": "{{gender}}",
      "pronouns": "{{pronouns}}",
      "dynasty": "{{dynasty}}",
      "surname": "{{surname}}"
    },
    "visual": {
      "hair_color": "{{hair_color}}",
      "eye_color": "{{eye_color}}",
      "build": "{{build}}",
      "height": "{{height}}",
      "classification": "{{visual_classification}}",
      "description": "{{appearance_description}}"
    },
    "psychology": {
      "core_traits": ["{{core_traits}}"],
      "fears": ["{{fears}}"],
      "motivations": ["{{motivations}}"],
      "behavioral_patterns": ["{{behavioral_patterns}}"]
    },
    "capabilities": {
      "skills": ["{{skills}}"],
      "education": "{{education}}",
      "occupation": "{{occupation}}"
    },
    "relationships": {
      "parents": ["{{parent_ids}}"],
      "siblings": ["{{sibling_ids}}"],
      "spouse": ["{{spouse_ids}}"],
      "children": ["{{child_ids}}"],
      "non_familial": ["{{non_familial_relationships}}"]
    },
    "biography": {
      "backstory": "{{backstory}}",
      "key_events": ["{{history_events}}"],
      "current_status": "{{current_status}}"
    }
  },
  "provenance": {
    "source_files": ["{{database_file_paths}}"],
    "authority": "{{authority_domain}}",
    "canon_version": "1.0",
    "generation_timestamp": "{{iso_timestamp}}",
    "validation_status": "validated"
  }
}
```

---

## Generation Rules

### R-008 Compliance

All bot generation must comply with R-008_Bot_Rules:

| Rule | Requirement | Enforcement |
|------|-------------|-------------|
| R-008-BOT-001 | Cards generated from repository canon only | validation_engine checks all source paths |
| R-008-BOT-002 | No manual lore injection | All fields must have mapped source |
| R-008-BOT-003 | Content traceable to database/ records | Provenance metadata required |
| R-008-BOT-004 | Canon Layer Architecture compliance | Active/Historical/Cultural separation |

### Generation Workflow

```
1. Select character_id from database/characters/
2. Query En_Core(character, entity_id, context)
3. En_Core → family_engine (genealogy)
4. En_Core → experience_engine (scenario context)
5. En_Core → validation_engine (full validation)
6. IF valid: Format output per target platform schema
7. IF invalid: Reject generation, return error report
8. Attach provenance metadata to output
9. Write output to deployment/ directory
```

### Forbidden Generation Operations

| Operation | Rule | Authority |
|-----------|------|-----------|
| Generate card for character not in database/ | PROHIBITED | R-008-BOT-001 |
| Inject lore not in database/ | PROHIBITED | R-008-BOT-002 |
| Modify canonical data during generation | PROHIBITED | R-007-ENG-001 |
| Generate from memory or archive | PROHIBITED | R-008-BOT-001 |
| Treat Cultural Canon as Active | PROHIBITED | R-008-BOT-004 |
| Omit provenance metadata | PROHIBITED | R-008-BOT-003 |
| Bypass validation_engine | PROHIBITED | R-007-ENG-004 |

---

## Character Card Inventory

### Active Canon Characters Available for Export

| Character ID | Name | Dynasty | Status |
|--------------|------|---------|--------|
| C_Wulfnic | Wulfnic Bloodmoon | Bloodmoon | ✅ Exportable |
| C_Nixara | Nixara Bloodmoon | Bloodmoon | ✅ Exportable |
| C_Erik | Erik Douglas | Douglas | ✅ Exportable |
| C_Logan | Logan Douglas | Douglas | ✅ Exportable |
| C_Malachia | Malachia Douglas-Bloodmoon | Douglas-Bloodmoon | ✅ Exportable |
| C_Noah | Noah Douglas-Bloodmoon | Douglas-Bloodmoon | ✅ Exportable |
| C_Jasper | Jasper Douglas-Bloodmoon | Douglas-Bloodmoon | ✅ Exportable |
| C_Alyssa | Alyssa Douglas-Bloodmoon | Douglas-Bloodmoon | ✅ Exportable |
| C_Kaladin_Nargathon | Kaladin Nargathon | — | ✅ Exportable |
| C_Marcus_Thornfield | Marcus Thornfield | — | ✅ Exportable |
| C_Angel_Moreno | Angel Moreno | — | ✅ Exportable |
| C_Edric_Douglas | Edric Douglas | Douglas | ✅ Exportable |

### Historical Canon Characters

| Character ID | Name | Canon Layer | Export Notes |
|--------------|------|-------------|--------------|
| HC_Edric_Aettfadir | Edric Ættfaðir Svartúlfa (725 AD) | Historical | Export with `historical` tag |
| HC_Douglas_Lineage | Douglas Commercial Lineage (1666) | Historical | Export with `historical` tag |

---

## Authority

**Established by:** Architecture Review & Canon Authority  
**Approved by:** Canon Freeze v1 Governance  
**Depends on:** ADR-003, ADR-006, R-007, R-008  
**Version:** 1.0 — Frozen under Canon Freeze v1
