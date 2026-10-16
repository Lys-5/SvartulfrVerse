# AUTHORITY MATRIX

**Version:** 1.0  
**Date:** 2026-06-08  
**Authority:** ADR-002, ADR-003, ADR-004, ADR-005, R-002, R-003, R-004, R-005  
**Purpose:** Single-source reference for ownership boundaries across all authority domains.

---

## 1. FAMILY AUTHORITY

**Owner:** `database/families/`  
**Governing ADR:** ADR-002  
**Governing Rules:** R-002

### Owns
| Data Element | Description | Storage |
|--------------|-------------|---------|
| Parent-Child Relationships | Biological and adoptive descent | `F_Parent_Child.md` |
| Marriages | Legal unions | `F_Marriages.md` |
| Surname Rules | Naming conventions and authority | `F_Surname_Authority.md` |
| Dynasty Membership | Bloodmoon, Douglas, Douglas-Bloodmoon | `F_Douglas_Bloodmoon.md` |
| Genealogical Graph | All explicit edges (directed) | `database/families/` |
| Hereditary Titles | Genealogical artifacts | Family records |

### May Reference
| Data Element | Source | Access |
|--------------|--------|--------|
| Character Identity | `database/characters/` | Read-only (for context) |
| Dynasty Origins | ADR-001 | Read-only |

### Prohibited Ownership
| Data Element | Actual Owner | Rule |
|--------------|--------------|------|
| Character Identity (name, pronouns, personality) | Character Authority | R-002-FAM-004, R-003-CHR-001 |
| Character Biography | Character Authority | R-002-FAM-004 |
| Appearance / Visual Data | Visual Authority | R-002-FAM-004, R-004-VIS-008 |
| Scenario / Experience Data | Experience Authority | R-002-FAM-004 |
| Behavioral Logic | None (knowledge-only layer) | R-002-FAM-004 |

### Common Violations
| Violation | Detection | Resolution |
|-----------|-----------|------------|
| Genealogy stored in character files | Character Audit | Move to `database/families/` |
| Character personality in family files | Authority Boundary Audit | Move to `database/characters/` |
| Visual data in family files | Authority Boundary Audit | Move to `database/worlds/` |
| Derived relationships stored as facts | Cross Reference Audit | Remove; compute at runtime |
| Wulfnic → Erik father-son relationship | Cross Reference Audit (CR-105) | Remove; legacy drift |

---

## 2. CHARACTER AUTHORITY

**Owner:** `database/characters/`  
**Governing ADR:** ADR-003  
**Governing Rules:** R-003

### Owns
| Data Element | Description | Storage |
|--------------|-------------|---------|
| Identity | Name, pronouns, self-conception | `C_[Name].md` → Identity |
| Personality | Core traits, fears, motivations | `C_[Name].md` → Psychology |
| Biography | Personal history, memories | `C_[Name].md` → History |
| Physical Sex | Biological baseline | `C_[Name].md` → Physical |
| Skills | Learned competencies | `C_[Name].md` → Capabilities |
| Education | Academic records | `C_[Name].md` → Capabilities |
| Baseline Occupation | Professional identity | `C_[Name].md` → Capabilities |
| Core Relationships | Significant bonds | `C_[Name].md` → Relationships |
| Current Status | Present situation summary | `C_[Name].md` |

### May Reference
| Data Element | Source | Access |
|--------------|--------|--------|
| Surname | `database/families/F_Surname_Authority.md` | Read-only |
| Dynasty Membership | `database/families/F_Douglas_Bloodmoon.md` | Read-only |
| Family Relationships | `database/families/F_Parent_Child.md` | Read-only |
| Appearance | `database/worlds/W_Visual_Baseline.md` | Read-only |

### Prohibited Ownership
| Data Element | Actual Owner | Rule |
|--------------|--------------|------|
| Genealogy (parent-child) | Family Authority | R-003-CHR-007, R-002-FAM-001 |
| Appearance Baseline | Visual Authority | R-003-CHR-009, R-004-VIS-010 |
| Scenario-Scoped Data | Experience Authority | R-003-CHR-008 |
| Surname Rules | Family Authority | R-002-FAM-008 |
| Dynasty Membership | Family Authority | R-002-FAM-007 |

### Common Violations
| Violation | Detection | Resolution |
|-----------|-----------|------------|
| Parent-child in character file | Character Audit | Move to `database/families/` |
| Appearance defined in character file | Authority Boundary Audit | Move to `database/worlds/` |
| Current residence as canonical fact | Character Audit | Move to `database/experiences/` |
| Scenario data in character file | Character Audit | Move to `database/experiences/` |
| Surname rules in character file | Authority Boundary Audit | Move to `database/families/` |

---

## 3. VISUAL AUTHORITY

**Owner:** `database/worlds/`  
**Governing ADR:** ADR-004  
**Governing Rules:** R-004

### Owns
| Data Element | Description | Storage |
|--------------|-------------|---------|
| Appearance Baseline | Hair, eyes, build, skin | `W_Visual_Baseline.md` |
| Visual Inheritance Rules | How appearance passes to children | `W_Visual_Inheritance.md` |
| Coloration Authority | Eye/hair/skin color inheritance | `W_Visual_Inheritance.md` |
| Resemblance Rules | Which parent child resembles | `W_Visual_Inheritance.md` |
| Aesthetic Profiles | Style, fashion, visual vibe | `W_Visual_Baseline.md` |
| Visual Fusion Model | Douglas-Bloodmoon inheritance | `W_Visual_Inheritance.md` |

### May Reference
| Data Element | Source | Access |
|--------------|--------|--------|
| Parent-Child Relationships | `database/families/F_Parent_Child.md` | Read-only |
| Dynasty Membership | `database/families/` | Read-only |
| Character Identity | `database/characters/` | Read-only (for context) |

### Prohibited Ownership
| Data Element | Actual Owner | Rule |
|--------------|--------------|------|
| Genealogy | Family Authority | R-004-VIS-008 |
| Character Identity | Character Authority | R-004-VIS-009 |
| Personality | Character Authority | R-004-VIS-009 |
| Scenario Data | Experience Authority | R-004-VIS-009 |

### Common Violations
| Violation | Detection | Resolution |
|-----------|-----------|------------|
| Appearance defined in character file | Authority Boundary Audit | Move to `database/worlds/` |
| Genealogy in visual file | Authority Boundary Audit | Move to `database/families/` |
| Character identity in visual file | Authority Boundary Audit | Move to `database/characters/` |
| Genetic model terminology (dominant/recessive) | Visual Audit | Use Visual Fusion Model |

---

## 4. EXPERIENCE AUTHORITY

**Owner:** `database/experiences/`  
**Governing ADR:** ADR-005  
**Governing Rules:** R-005

### Owns
| Data Element | Description | Storage |
|--------------|-------------|---------|
| Scenario Framing | Narrative context and setup | `Ex_[Name].md` |
| Context State | Location, time, circumstances | `Ex_[Name].md` |
| Role Assignment | Character function in scenario | `Ex_[Name].md` |
| Occupation Override | Scenario-specific profession | `Ex_[Name].md` |
| Residence Override | Scenario-specific location | `Ex_[Name].md` |
| Relationship Extensions | Scenario-specific bonds | `Ex_[Name].md` |
| Employment Context | Scenario-specific work context | `Ex_[Name].md` |

### May Reference
| Data Element | Source | Access |
|--------------|--------|--------|
| Character Identity | `database/characters/` | Read-only |
| Genealogy | `database/families/` | Read-only |
| Appearance | `database/worlds/` | Read-only |
| Baseline Occupation | `database/characters/` | Read-only (for override context) |

### Prohibited Ownership
| Data Element | Actual Owner | Rule |
|--------------|--------------|------|
| Character Identity | Character Authority | R-005-EXP-005 |
| Genealogy | Family Authority | R-005-EXP-006 |
| Appearance | Visual Authority | R-005-EXP-007 |
| New Canon (any type) | Respective Authority | R-005-EXP-008 |
| Permanent Residence | None (scenario-scoped) | R-005-EXP-009 |
| Permanent Employment | Character Authority (baseline) | R-005-EXP-010 |

### Common Violations
| Violation | Detection | Resolution |
|-----------|-----------|------------|
| Identity redefinition in experience | Authority Boundary Audit | Remove; reference Character Authority |
| Genealogy changes in experience | Authority Boundary Audit | Remove; reference Family Authority |
| Permanent residence as canon | Experience Audit | Mark as scenario-scoped |
| New canon created in experience | Canon Candidate Review | Reject; use Canon Recovery Workflow |

---

## 5. CANON LAYERS

**Governing ADR:** ADR-006  
**Governing Rules:** R-006

### Layer Structure

| Layer | Runtime-Eligible | Modification Rule | Authority |
|-------|------------------|-------------------|-----------|
| **Active Canon** | ✅ Full compilation | Requires Authority Decision | Full ADR governance |
| **Historical Canon** | ✅ Reference only | Requires evidence | ADR-001 oversight |
| **Cultural Canon** | ❌ Dialogue flavor only | Append-only | Preservation focus |
| **Deferred Canon** | ❌ Prohibited | Activation process required | Deferred Canon Policy |
| **Candidate Canon** | ❌ Prohibited | Full review + approval | Review process |

### Layer Content

#### Active Canon
- All 12 contemporary characters (Wulfnic, Nixara, Erik, Logan, Malachia, Noah, Jasper, Alyssa, Kaladin, Marcus, Angel, Edric)
- Douglas-Bloodmoon dynasty and heirs
- Visual Fusion Model and baselines
- Timeline: 1930s migration through 2024
- Institutions: Seven Hills, DCC, UCLA
- The Verve (Logan's nightclub/workshop/residence)
- Seven Hills Estate (Douglas ancestral estate, DCC Heritage Site)

#### Historical Canon
- Edric Ættfaðir Svartúlfa (725 AD)
- Douglas Commercial Lineage (1666)
- Dynasty origins (Iceland/England)
- Migration timelines
- Seven Hills Estate history

#### Cultural Canon
- Svartúlfr (Black Wolf) — ancestral clan identity
- Fenrir, Werewolves, Trolls, Draugr — family legends
- Seiðr, Jötnar, Moon spirits — folklore
- Alpha hierarchy — storytelling metaphor

#### Deferred Canon
- 0 currently deferred entities
- 14 rejected entities (see below)

#### Candidate Canon
- Regency Era Layer (requires historical audit)
- Colonial Timeline Details (requires historical audit)
- Early Douglas Genealogy (requires historical audit)

### Rejected Canon (Cannot Re-enter)
| Concept | Classification | Source |
|---------|----------------|--------|
| Valeria / WetNurse / Concubine | REJECTED | CANON_003 |
| Miss Twin Peaks origin | REJECTED | CANON_002 |
| KSA origin story | REJECTED | CANON_001 |
| Political Wives (Sigrid, Dagmar) | REJECTED | ADR-006 |
| Extended Lines (Gunnar, Ingrid, etc.) | REJECTED | ADR-006 |
| Vanguard PMC | REJECTED | Replaced by DCC Security — BlackWolf |

---

## 6. COMPLETE OWNERSHIP MATRIX

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        COMPLETE OWNERSHIP MATRIX                                │
├─────────────────┬──────────┬──────────┬──────────┬──────────┬──────────────────┤
│ Data Element    │ Family   │ Character│ Visual   │ Experience│ Canon Layer     │
├─────────────────┼──────────┼──────────┼──────────┼──────────┼──────────────────┤
│ Parent-Child    │ OWN      │ REF      │ REF      │ REF      │ Active          │
│ Marriages       │ OWN      │ REF      │ REF      │ REF      │ Active          │
│ Surname Rules   │ OWN      │ REF      │ REF      │ REF      │ Active          │
│ Dynasty         │ OWN      │ REF      │ REF      │ REF      │ Active          │
│ Name            │ —        │ OWN      │ —        │ REF      │ Active          │
│ Pronouns        │ —        │ OWN      │ —        │ REF      │ Active          │
│ Personality     │ —        │ OWN      │ —        │ REF      │ Active          │
│ Biography       │ —        │ OWN      │ —        │ REF      │ Active          │
│ Physical Sex    │ —        │ OWN      │ —        │ REF      │ Active          │
│ Skills          │ —        │ OWN      │ —        │ REF      │ Active          │
│ Education       │ —        │ OWN      │ —        │ REF      │ Active          │
│ Occupation (BL) │ —        │ OWN      │ —        │ OVERRIDE │ Active          │
│ Core Relations  │ —        │ OWN      │ —        │ EXTEND   │ Active          │
│ Hair Color      │ —        │ REF      │ OWN      │ REF      │ Active          │
│ Eye Color       │ —        │ REF      │ OWN      │ REF      │ Active          │
│ Build           │ —        │ REF      │ OWN      │ REF      │ Active          │
│ Height          │ —        │ REF      │ OWN      │ REF      │ Active          │
│ Inheritance     │ REF      │ REF      │ OWN      │ REF      │ Active          │
│ Resemblance     │ REF      │ REF      │ OWN      │ REF      │ Active          │
│ Scenario        │ —        │ REF      │ —        │ OWN      │ Active          │
│ Context State   │ —        │ REF      │ —        │ OWN      │ Active          │
│ Role            │ —        │ REF      │ —        │ OWN      │ Active          │
│ Residence (SC)  │ —        │ —        │ —        │ OWN      │ Active          │
│ Employment (SC) │ —        │ —        │ —        │ OWN      │ Active          │
│ Ext. Relations  │ —        │ REF      │ —        │ OWN      │ Active          │
│ Family Legends  │ OWN      │ —        │ —        │ REF      │ Cultural        │
│ Origin Stories  │ OWN      │ —        │ —        │ REF      │ Historical      │
│ Migration Data  │ OWN      │ —        │ —        │ REF      │ Historical      │
└─────────────────┴──────────┴──────────┴──────────┴──────────┴──────────────────┘

Legend:
  OWN      = This authority owns this data element
  REF      = This authority may reference (read-only) this data element
  OVERRIDE = This authority may override for scenario scope only
  EXTEND   = This authority may extend (not remove) this data element
  —        = No relationship
  (BL)     = Baseline
  (SC)     = Scenario-Scoped
```

## 7. VALIDATED RUNTIME CONSTRAINTS

### 7.1 Pronoun Macro Boundary — Validated Runtime State

> **Validated Runtime Constraint (as of Phase 15 testing — 2026-06-09)**

**Observed Behavior:**

| Layer | `{{sub}}` expansion | Status |
|-------|---------------------|--------|
| Prompt-facing fields | Expanded | **Available** |
| JavaScript runtime | Not expanded (literal `{{sub}}`) | **Unavailable** |

**Validated macros:** `{{sub}}`, `{{obj}}`, `{{poss}}`, `{{poss_p}}`, `{{ref}}`

**Current assumption (until contrary evidence):**
- Prompt Layer Access = **Available**
- JavaScript Runtime Access = **Unavailable**

**ADR Operational Rule:** Pronoun-dependent resolution belongs in prompt construction, not in JavaScript conditional logic.

**Future Update Path:** If Phase 16/17 reveals a direct pronoun API (e.g., `chat.user.pronouns`), this constraint will be updated.

---

## 8. CONFLICT RESOLUTION

When data conflicts occur between authority layers:

| Conflict | Resolution | Authority |
|----------|------------|-----------|
| Character file defines genealogy | Family Authority wins; remove from character | R-002-FAM-001 |
| Experience redefines identity | Character Authority wins; reject experience | R-005-EXP-005 |
| Visual file defines genealogy | Family Authority wins; remove from visual | R-004-VIS-008 |
| Cultural Canon presented as fact | Active Canon wins; reclassify as flavor | ADR-006 |
| Historical contradicts Active | Active Canon prevails | ADR-006 |
| ADR contradicts any record | ADR wins (highest authority) | R-006-GOV-002 |

---

*This matrix is derived from ADR-002 through ADR-006 and R-002 through R-005. Any modification requires Architecture Review and ADR update.*
