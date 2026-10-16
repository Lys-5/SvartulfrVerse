# EXPORT_MAPPING_MATRIX

**Version:** 1.0  
**Date:** 2026-06-08  
**Authority:** BOT_EXPORT_SPECIFICATION.md, LOREBOOK_SPECIFICATION.md, R-008, R-009  
**Purpose:** Reference mapping between repository data and export fields.

---

## 1. REPOSITORY → BOT EXPORT MAPPING

### 1.1 Identity Fields

| Bot Export Field | Repository Source | Authority | Access Path |
|------------------|-------------------|-----------|-------------|
| `name` | C_Template → Identity.Name | Character | `database/characters/C_[Name].md` |
| `aliases` | C_Template → Identity.Aliases | Character | `database/characters/C_[Name].md` |
| `age` | Computed: Birth Date → Current Year | Character | `database/characters/C_[Name].md` |
| `birth_date` | C_Template → Identity.Birth Date | Character | `database/characters/C_[Name].md` |
| `nationality` | C_Template → Identity.Nationality | Character | `database/characters/C_[Name].md` |
| `gender` | C_Template → Identity.Gender | Character | `database/characters/C_[Name].md` |
| `pronouns` | C_Template → Identity.Pronouns | Character | `database/characters/C_[Name].md` |
| `dynasty` | F_Douglas_Bloodmoon → Membership | Family | `database/families/F_Douglas_Bloodmoon.md` |
| `surname` | F_Surname_Authority → Rules | Family | `database/families/F_Surname_Authority.md` |

### 1.2 Visual Fields

| Bot Export Field | Repository Source | Authority | Access Path |
|------------------|-------------------|-----------|-------------|
| `hair_color` | W_Visual_Baseline or C record → Visual | Visual | `database/worlds/W_Visual_Baseline.md` |
| `eye_color` | W_Visual_Baseline or C record → Visual | Visual | `database/worlds/W_Visual_Baseline.md` |
| `build` | C record → Physical.Build | Visual | `database/characters/C_[Name].md` |
| `height` | C record → Physical.Height | Visual | `database/characters/C_[Name].md` |
| `visual_classification` | W_Visual_Inheritance → Classification | Visual | `database/worlds/W_Visual_Inheritance.md` |
| `appearance_description` | Composite: all visual fields | Visual | Engine-aggregated |

### 1.3 Psychology & Personality Fields

| Bot Export Field | Repository Source | Authority | Access Path |
|------------------|-------------------|-----------|-------------|
| `personality` | C_Template → Psychology.Core Traits | Character | `database/characters/C_[Name].md` |
| `fears` | C_Template → Psychology.Fears | Character | `database/characters/C_[Name].md` |
| `motivations` | C_Template → Psychology.Motivations | Character | `database/characters/C_[Name].md` |
| `behavioral_patterns` | C_Template → Psychology.Behavioral Patterns | Character | `database/characters/C_[Name].md` |

### 1.4 Capability Fields

| Bot Export Field | Repository Source | Authority | Access Path |
|------------------|-------------------|-----------|-------------|
| `skills` | C_Template → Capabilities.Skills | Character | `database/characters/C_[Name].md` |
| `education` | C_Template → Capabilities.Education | Character | `database/characters/C_[Name].md` |
| `occupation` | C_Template → Capabilities.Occupation | Character | `database/characters/C_[Name].md` |

### 1.5 Relationship Fields

| Bot Export Field | Repository Source | Authority | Access Path |
|------------------|-------------------|-----------|-------------|
| `parents` | F_Parent_Child → Parent records | Family | `database/families/F_Parent_Child.md` |
| `siblings` | Computed from F_Parent_Child | Family | `database/families/F_Parent_Child.md` |
| `spouse` | F_Marriages → Marriage records | Family | `database/families/F_Marriages.md` |
| `children` | F_Parent_Child → Child records | Family | `database/families/F_Parent_Child.md` |
| `non_familial_relationships` | C_Template → Relationships | Character | `database/characters/C_[Name].md` |

### 1.6 Biography Fields

| Bot Export Field | Repository Source | Authority | Access Path |
|------------------|-------------------|-----------|-------------|
| `backstory` | C_Template → History | Character | `database/characters/C_[Name].md` |
| `character_memory` | C_Template → History (key events) | Character | `database/characters/C_[Name].md` |
| `current_status` | C_Template → Current Status | Character | `database/characters/C_[Name].md` |

---

## 2. REPOSITORY → LOREBOOK ENTRY MAPPING

### 2.1 Character Lorebook

| Entry Type | Canon Layer | Source Fields | Repository Path |
|------------|-------------|---------------|-----------------|
| Character Identity | Active | Name, age, dynasty, role | `database/characters/C_*.md` |
| Character Personality | Active | Core traits, fears, motivations | `database/characters/C_*.md` |
| Character Visual | Active | Hair, eyes, build, height | `database/characters/C_*.md` + `database/worlds/W_Visual_*.md` |
| Character Biography | Active | Backstory, key events | `database/characters/C_*.md` |
| Character Relationships | Active | Non-familial relationships | `database/characters/C_*.md` |
| Character Education | Active | Institution, level, track | `database/characters/C_*.md` |
| Character Occupation | Active | Baseline profession | `database/characters/C_*.md` |

### 2.2 Family Lorebook

| Entry Type | Canon Layer | Source Fields | Repository Path |
|------------|-------------|---------------|-----------------|
| Dynasty Structure | Active | Dynasty membership, founding | `database/families/F_Douglas_Bloodmoon.md` |
| Parent-Child | Active | Biological relationships | `database/families/F_Parent_Child.md` |
| Marriages | Active | Union records | `database/families/F_Marriages.md` |
| Surname Rules | Active | Naming conventions | `database/families/F_Surname_Authority.md` |
| Historical Lineage | Historical | Pre-contemporary genealogy | ADR-001, Historical Canon records |

### 2.3 World Lorebook

| Entry Type | Canon Layer | Source Fields | Repository Path |
|------------|-------------|---------------|-----------------|
| Setting | Active | Geographic context, timeline | `database/worlds/W_*.md` |
| Visual Baseline | Active | Dynasty appearance standards | `database/worlds/W_Visual_Baseline.md` |
| Visual Inheritance | Active | Inheritance rules, fusion model | `database/worlds/W_Visual_Inheritance.md` |
| Style Guide | Active | Aesthetic guidelines | `database/worlds/W_Visual_Baseline.md` |

### 2.4 Institution Lorebook

| Entry Type | Canon Layer | Source Fields | Repository Path |
|------------|-------------|---------------|-----------------|
| Institution Identity | Active | Name, type, scope | `database/institutions/I_*.md` |
| Personnel | Active | Key personnel, roles | `database/institutions/I_*.md` |
| Relationships | Active | Character affiliations | `database/institutions/I_*.md` |

### 2.5 Experience Lorebook

| Entry Type | Canon Layer | Source Fields | Repository Path |
|------------|-------------|---------------|-----------------|
| Scenario | Active | Framing, context | `database/experiences/Ex_*.md` |
| Roles | Active | Character assignments | `database/experiences/Ex_*.md` |
| Occupation Overrides | Active | Scenario-specific roles | `database/experiences/Ex_*.md` |

### 2.6 Cultural Lorebook

| Entry Type | Canon Layer | Source Fields | Repository Path |
|------------|-------------|---------------|-----------------|
| Family Traditions | Cultural | Oral traditions, stories | ADR-006 Cultural Canon classification |
| Myths & Legends | Cultural | Mythological references | ADR-006 Cultural Canon classification |
| Cultural Identity | Cultural | Ancestral clan identity | ADR-006 Cultural Canon classification |

---

## 3. PLATFORM-SPECIFIC FIELD MAPPING

### 3.1 JanitorAI

| JanitorAI Field | Repository Source | Notes |
|-----------------|-------------------|-------|
| `name` | Character Identity.Name | Required |
| `description` | Composite: visual + personality | Max 5000 chars |
| `personality` | Psychology.Core Traits | Formatted as prose |
| `scenario` | Default experience context | From Experience Authority |
| `first_mes` | Generated from personality + context | Must not contradict canon |
| `mes_example` | Generated from personality | Must reflect canonical speech patterns |
| `system_prompt` | Composite: identity + constraints | Includes authority boundaries |
| `creator_notes` | History + backstory | For bot context only |
| `post_history_instructions` | Behavioral constraints | From psychology + rules |
| `tags` | Canon layer + dynasty + ID | Must include `SvartulfrVerse` |
| `extensions.svartulfrverse` | Engine metadata | Traceability data (required) |

### 3.2 SillyTavern (Character Card V3)

| SillyTavern Field | Repository Source | Notes |
|-------------------|-------------------|-------|
| `name` | Character Identity.Name | Required |
| `description` | Composite: personality + appearance | Full description |
| `personality` | Psychology.Core Traits | Summary |
| `scenario` | Default experience context | From Experience Authority |
| `first_mes` | Generated from personality + context | Opening dialogue |
| `mes_example` | Generated from personality | Dialogue examples |
| `system_prompt` | Composite: identity + constraints | System-level instructions |
| `creator_notes` | History + backstory | For bot context |
| `post_history_instructions` | Behavioral constraints | Post-history instructions |
| `tags` | Canon layer + dynasty | Tag array |
| `extensions.svartulfrverse` | Engine metadata | Traceability data (required) |

### 3.3 Generic JSON

| Generic JSON Path | Repository Source | Notes |
|-------------------|-------------------|-------|
| `character.id` | Character identifier | e.g., C_Alyssa |
| `character.canon_layer` | ADR-006 classification | active/historical/cultural |
| `character.identity.*` | Character Identity fields | Name, age, birth_date, etc. |
| `character.visual.*` | Visual Authority fields | Hair, eyes, build, height |
| `character.psychology.*` | Psychology fields | Traits, fears, motivations |
| `character.capabilities.*` | Capability fields | Skills, education, occupation |
| `character.relationships.*` | Family + Character relationships | Parents, siblings, spouse, children |
| `character.biography.*` | Biography fields | Backstory, key events, status |
| `provenance.*` | Engine metadata | Source files, version, timestamp |

---

## 4. TRACEABILITY REQUIREMENTS

### 4.1 Bot Export Traceability

Every bot export MUST include:

| Field | Source | Required |
|-------|--------|----------|
| `extensions.svartulfrverse.canon_id` | Character identifier | ✅ Yes |
| `extensions.svartulfrverse.canon_layer` | ADR-006 classification | ✅ Yes |
| `extensions.svartulfrverse.provenance` | List of source file paths | ✅ Yes |
| `extensions.svartulfrverse.authority` | Authority domain | ✅ Yes |
| `extensions.svartulfrverse.visual_classification` | Visual inheritance class | ✅ Yes |
| `extensions.svartulfrverse.dynasty` | Dynasty membership | ✅ Yes |
| `extensions.svartulfrverse.validation_status` | validation_engine result | ✅ Yes |
| `extensions.svartulfrverse.generation_timestamp` | ISO timestamp | ✅ Yes |
| `extensions.svartulfrverse.canon_version` | Canon version (1.0) | ✅ Yes |

### 4.2 Lorebook Traceability

Every lorebook entry MUST include:

| Field | Source | Required |
|-------|--------|----------|
| `Entry ID` | Unique identifier (LB-XXX-NNN) | ✅ Yes |
| `Canon Layer` | Active/Historical/Cultural tag | ✅ Yes |
| `Source` | database/ file path | ✅ Yes |
| `Authority` | Authority domain | ✅ Yes |
| `Last Synchronized` | ISO timestamp | ✅ Yes |

---

## 5. FIELD OWNERSHIP SUMMARY

| Export Field Category | Owner Authority | Consumer | Override Allowed? |
|-----------------------|-----------------|----------|-------------------|
| Identity fields | Character | Bot/Lorebook | ❌ No |
| Visual fields | Visual | Bot/Lorebook | ❌ No |
| Psychology fields | Character | Bot/Lorebook | ❌ No |
| Capability fields | Character | Bot/Lorebook | ❌ No |
| Relationship fields | Family (canonical) + Character (non-familial) | Bot/Lorebook | ❌ No |
| Biography fields | Character | Bot/Lorebook | ❌ No |
| Scenario fields | Experience | Bot/Lorebook | ❌ No |
| Role fields | Experience | Bot/Lorebook | ❌ No |
| Occupation override | Experience | Bot (scenario) | ✅ Yes (scenario) |
| Provenance metadata | Engine | Bot/Lorebook | ❌ No (auto-generated) |

---

## 6. CHARACTER EXPORT STATUS

### Active Canon — Ready for Export

| Character ID | Name | Dynasty | Export Ready |
|--------------|------|---------|--------------|
| C_Wulfnic | Wulfnic Bloodmoon | Bloodmoon | ✅ Yes |
| C_Nixara | Nixara Bloodmoon | Bloodmoon | ✅ Yes |
| C_Erik | Erik Douglas | Douglas | ✅ Yes |
| C_Logan | Logan Douglas | Douglas | ✅ Yes |
| C_Malachia | Malachia Douglas-Bloodmoon | Douglas-Bloodmoon | ✅ Yes |
| C_Noah | Noah Douglas-Bloodmoon | Douglas-Bloodmoon | ✅ Yes |
| C_Jasper | Jasper Douglas-Bloodmoon | Douglas-Bloodmoon | ✅ Yes |
| C_Alyssa | Alyssa Douglas-Bloodmoon | Douglas-Bloodmoon | ✅ Yes |
| C_Kaladin_Nargathon | Kaladin Nargathon | — | ✅ Yes |
| C_Marcus_Thornfield | Marcus Thornfield | — | ✅ Yes |
| C_Angel_Moreno | Angel Moreno | — | ✅ Yes |
| C_Edric_Douglas | Edric Douglas | Douglas | ✅ Yes |

### Historical Canon — Export with `historical` Tag

| Character ID | Name | Canon Layer |
|--------------|------|-------------|
| HC_Edric_Aettfadir | Edric Ættfaðir Svartúlfa (725 AD) | Historical |
| HC_Douglas_Lineage | Douglas Commercial Lineage (1666) | Historical |

---

*This matrix is derived from BOT_EXPORT_SPECIFICATION.md and LOREBOOK_SPECIFICATION.md. All exports must comply with R-008_Bot_Rules and R-009_Lorebook_Rules.*
