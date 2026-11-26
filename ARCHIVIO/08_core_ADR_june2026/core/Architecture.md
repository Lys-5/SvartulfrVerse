# Repository Architecture

## Core Principles

### 1. Runtime First
Preserve behavior before optimization. Observable runtime behavior is the ground truth.

### 2. Preserve Behavior Before Refactoring
Character age, education, occupation, and family relationships must remain internally consistent. Refactoring must never silently corrupt these relationships.

### 3. Knowledge vs Behavior Separation
Family Authority (genealogy layer) is knowledge-only: it does not compute relationships or manage state. Family data is immutable source material, not behavior engine.

### 4. Character Canonicality
Characters own identity (personality, sex, education, biography). Characters reference genealogy but never own it. Characters contain no scenario data, no contextual roles, no temporary residence data.

### 5. Incremental Reintroduction
Archived systems (Urban Fantasy, Cyber, Wasteland, Norse Mythic, etc.) remain archived until explicitly validated through canon recovery workflow.

### 6. Canonical Stabilization Before Expansion
Depth precedes breadth. A complete, validated contemporary + only-human Los Angeles Dynasty is prerequisite for world system expansion.

## Authority Layers

- **Family Authority**: Genealogy, dynasties, surnames, kinship relationships (knowledge-only)
- **Character Authority**: Identity, personality, biography, skills, education, baseline occupation
- **Visual Authority**: Appearance, phenotype, resemblance rules, visual inheritance
- **Experience Authority**: Scenario framing, context, roles, occupation override, current residence, current employment context

### Critical Rules

- Character files contain NO genealogy (Family Authority only owns this)
- Character files contain NO contextual scenario data (Experience Authority owns this)
- Family Authority contains NO behavioral logic (knowledge layer only)
- Visual Authority is independent from Family Authority (visual inheritance ≠ genealogical inheritance)
- Titles are genealogical artifacts (owned by Family Authority, referenced by Character)
- Age is calculated from birth date (never stored; varies by scenario time)
- Residence is scenario-contextual (never stored as "current home")
- Baseline occupation is owned by Character Authority; occupation override is owned by Experience Authority

## Validation Paradigm

### LA_OnlyHuman_Academic_Timeline

Character age, education, and occupation must form plausible real-world timeline:

- **19**: Freshman / Sophomore
- **22-23**: Bachelor Graduate
- **25**: 3L Law Student / Graduate Student / Early Career Professional
- **28**: PhD Candidate / Medical Resident / Early Management
- **31+**: Marriage / Children / Senior Management

**Purpose:** Prevent character drift toward unrealistic prodigy careers and preserve contemporary realism.

## Data Model

### Character Authority owns:

- Given Name
- Sex
- Birth Date (immutable, not age)
- Personality
- Values
- Education Level
- Skills / Competencies
- Biography
- Character Memory
- Baseline Occupation (professional identity)

### Character Authority references:

- Surname (from Family Authority)
- Dynastic Membership (from Family Authority)
- Family Relationships (from Family Authority)
- Titles (from Family Authority)
- Appearance (from Visual Authority)

### Experience Authority owns:

- Scenario Framing
- Context State
- Role Assignment
- Occupation Override (scenario-scoped)
- Current Residence (scenario-scoped)
- Current Employment Context (scenario-scoped)
- Relationship Extensions (scenario-specific)

### Experience Authority references:

- Identity (from Character Authority)
- Genealogy (from Family Authority)
- Appearance (from Visual Authority)

### Family Authority owns:

- Dynasties
- Parent-Child Relationships
- Marriages
- Surnames
- Genealogical Relationships
- Dynastic Lines
- Hereditary Titles

### Visual Authority owns:

- Appearance Baseline
- Aesthetic Profile
- Visual Inheritance Rules
- Coloration Authority
- Resemblance Rules

### Visual Authority references:

- Parent-Child Relationships (from Family Authority)
- Dynasty Membership (from Family Authority)

## Repository Scope

### Supported

- Only Human (no supernatural)
- Contemporary (2020s-2030s)
- Los Angeles Dynasty (geographic + familial focus)

### Not Supported (Archived)

- Urban Fantasy
- Cyber
- Wasteland
- Fantasy
- Norse Mythic
- Regency
- Overlay Systems
- Pack Systems
- Supernatural Systems

These may be reintroduced only after canonical stabilization of base Los Angeles Dynasty.

## Engine Layer Role

Engines are **knowledge and query layers**, not behavior generators:

- **En_Core**: Central orchestration and query routing
- **family_engine**: Genealogy database and kinship queries
- **relationship_engine**: Cross-authority relationship queries; no relationship computation
- **experience_engine**: Experience Authority queries and scenario context
- **validation_engine**: Cross-reference and compliance validation (mandatory gate)

Engines DO NOT:
- Generate characters
- Create relationships
- Compute state
- Simulate behavior
- Import legacy data

Engines DO:
- Query authority layers
- Verify consistency
- Return canonical data
- Maintain single source of truth
