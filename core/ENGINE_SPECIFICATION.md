# ENGINE SPECIFICATION

**Status:** CANONICAL  
**Date:** 2026-06-08  
**Authority:** ADR-000, ADR-006, R-007_Engine_Rules, Architecture.md  
**Version:** 1.0 — Canon Freeze v1

---

## Purpose

This document defines the formal operational contracts for all engine systems in SvartulfrVerse. Engines are **query and knowledge layers** — they serve canon, never override it.

**Authority:** All engine behavior is governed by R-007_Engine_Rules.md. This specification translates R-007 principles into operational interface definitions.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     ENGINE ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  En_Core — Central Orchestration Layer                       │ │
│  │  Routes queries, manages context, coordinates engines        │ │
│  └───────────────────────────┬───────────────────────────────────┘ │
│                              │                                      │
│         ┌────────────────────┼────────────────────┐                │
│         │                    │                    │                │
│         ▼                    ▼                    ▼                │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐        │
│  │ family_     │  │ relationship_│  │ experience_       │        │
│  │ engine      │  │ engine       │  │ engine            │        │
│  └──────┬──────┘  └──────┬───────┘  └────────┬──────────┘        │
│         │                │                    │                   │
│         ▼                ▼                    ▼                   │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  validation_engine — Cross-reference & compliance check   │   │
│  └───────────────────────────────────────────────────────────┘   │
│                              │                                     │
│                              ▼                                     │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  database/ — Single Source of Truth (all engines read)    │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Engine Contracts

### 1. En_Core — Central Orchestration Engine

**Role:** Central query router and context coordinator.

#### Inputs

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `query_type` | Enum | One of: `character`, `family`, `experience`, `relationship`, `visual`, `world` | Yes |
| `entity_id` | String | Canonical entity identifier (e.g., `C_Alyssa`) | Yes |
| `context` | Object | Scenario context (location, time, role) | No |
| `query_mode` | Enum | One of: `read`, `validate`, `trace` | No (default: `read`) |

#### Outputs

| Field | Type | Description |
|-------|------|-------------|
| `status` | Enum | `ok`, `not_found`, `forbidden`, `invalid` |
| `data` | Object | Canonical data from the relevant authority layer |
| `provenance` | Array | List of source database/ file paths |
| `canon_layer` | Enum | `active`, `historical`, `cultural` |
| `validated` | Boolean | Whether output passed validation_engine |

#### Query Boundaries

```
En_Core MAY:
  - Route queries to appropriate engine
  - Aggregate responses from multiple engines
  - Manage scenario context resolution
  - Return provenance metadata for all responses
  - Invoke validation_engine on any output

En_Core MAY NOT:
  - Modify canonical data
  - Create new canonical records
  - Infer data not present in database/
  - Override authority layer boundaries
  - Bypass validation for any output
```

#### Canon Authority Dependencies

| Layer | Engine | Access |
|-------|--------|--------|
| Character | character_engine | Read-only |
| Family | family_engine | Read-only |
| Visual | visual query (via En_Core) | Read-only |
| Experience | experience_engine | Read-only |
| World | world query (via En_Core) | Read-only |

---

### 2. family_engine — Genealogy Query Engine

**Role:** Exclusive interface to Family Authority data. Knowledge-only. No computation.

#### Inputs

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `entity_id` | String | Canonical person identifier | Yes |
| `query` | Enum | One of: `parents`, `children`, `siblings`, `spouse`, `ancestry`, `dynasty`, `surname`, `full_graph` | Yes |
| `depth` | Integer | Graph traversal depth (default: 1, max: 5) | No |

#### Outputs

| Field | Type | Description |
|-------|------|-------------|
| `status` | Enum | `ok`, `not_found`, `invalid_query` |
| `data` | Object | Structured genealogical data |
| `provenance` | Array | Source file paths from database/families/ |
| `canon_layer` | Enum | Always `active` for family records |

#### Query Definitions

**Derived Relationships — family_engine computes but does NOT store:**

| Query Type | Computation Rule | Source Records |
|------------|------------------|----------------|
| `parents` | Direct lookup | Parent-Child records |
| `children` | Direct lookup | Parent-Child records |
| `siblings` | Compute: share ≥1 parent | Parent-Child records |
| `spouse` | Direct lookup | Marriage records |
| `ancestry` | Transitive parent traversal | Parent-Child records |
| `dynasty` | Direct lookup | Family record |
| `surname` | Direct lookup | Surname Authority record |
| `full_graph` | Union of all above | All family records |

#### Query Boundaries

```
family_engine MAY:
  - Query parent-child relationships from database/families/
  - Compute derived relationships (siblings, ancestors) at runtime
  - Return dynasty membership and surname authority
  - Provide full graph traversal up to depth 5

family_engine MAY NOT:
  - Create new family relationships
  - Modify existing family records
  - Store computed derived relationships as facts
  - Infer genealogy from non-genealogical data
  - Override Family Authority decisions
```

#### Canon Authority Dependencies

| Source | File | Access |
|--------|------|--------|
| Parent-Child | database/families/F_Parent_Child.md | Read-only |
| Marriages | database/families/F_Marriages.md | Read-only |
| Surname | database/families/F_Surname_Authority.md | Read-only |
| Dynasty | database/families/F_Douglas_Bloodmoon.md | Read-only |

---

### 3. relationship_engine — Relationship Query Engine

**Role:** Computes and validates relationship queries across authority layers. Read-only aggregator.

#### Inputs

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `entity_a` | String | First entity identifier | Yes |
| `entity_b` | String | Second entity identifier | Yes |
| `query` | Enum | One of: `relationship`, `connection_path`, `validate` | Yes |
| `scenario_context` | Object | Scenario-specific context | No |

#### Outputs

| Field | Type | Description |
|-------|------|-------------|
| `status` | Enum | `ok`, `not_found`, `forbidden` |
| `relationship_type` | String | Canonical relationship type |
| `connection_path` | Array | Ordered list of relationships connecting A→B |
| `canonical` | Boolean | True if relationship exists in authority records |
| `scenario_only` | Boolean | True if relationship exists only in experience layer |
| `provenance` | Array | Source file paths |

#### Query Boundaries

```
relationship_engine MAY:
  - Compute relationship paths between any two entities
  - Return both canonical and scenario-specific relationships
  - Validate claimed relationships against authority records
  - Reference experience-layer extensions

relationship_engine MAY NOT:
  - Create new canonical relationships
  - Override genealogical relationships with experience data
  - Store computed relationships as authority
  - Infer relationships from behavioral patterns
```

#### Canon Authority Dependencies

| Source | Access Type |
|--------|-------------|
| family_engine | Query (read-only) |
| Experience records | Query (read-only, extension only) |
| Character records | Query (read-only, identity verification) |

---

### 4. experience_engine — Experience Context Engine

**Role:** Provides scenario framing, context state, and role assignments. Owns experience-layer data.

#### Inputs

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `experience_id` | String | Canonical experience identifier (e.g., `Ex_DJFrequency`) | Yes |
| `query` | Enum | One of: `context`, `roles`, `occupation_overrides`, `residence`, `full_scenario` | Yes |
| `entity_filter` | String | Optional character identifier to filter results | No |

#### Outputs

| Field | Type | Description |
|-------|------|-------------|
| `status` | Enum | `ok`, `not_found` |
| `scenario` | Object | Scenario framing and setup |
| `context_state` | Object | Location, time, circumstances |
| `roles` | Object | Character→role mapping |
| `occupation_overrides` | Object | Character→occupation override mapping |
| `residence_overrides` | Object | Character→residence override mapping |
| `provenance` | Array | Source file paths from database/experiences/ |

#### Query Boundaries

```
experience_engine MAY:
  - Return scenario framing and context state
  - Provide role assignments within scenario scope
  - Override occupation and residence for scenario duration
  - Extend (not replace) canonical relationships

experience_engine MAY NOT:
  - Redefine character identity
  - Redefine genealogy
  - Redefine appearance
  - Create new canonical facts
  - Promote scenario data to canonical status
```

#### Canon Authority Dependencies

| Source | Access Type |
|--------|-------------|
| database/experiences/ | Read/Write (experience layer owns this) |
| Character records | Query (read-only, identity reference) |
| Family records | Query (read-only, genealogy reference) |
| Visual records | Query (read-only, appearance reference) |

---

### 5. validation_engine — Cross-Reference & Compliance Engine

**Role:** Validates all engine output against canonical authority. Mandatory gate before any output is released.

#### Inputs

| Parameter | Type | Description | Required |
|-----------|------|-------------|----------|
| `data` | Object | Engine output to validate | Yes |
| `source_engine` | Enum | Originating engine identifier | Yes |
| `validation_type` | Enum | One of: `cross_reference`, `canon_layer`, `authority_ownership`, `traceability`, `full` | Yes |

#### Outputs

| Field | Type | Description |
|-------|------|-------------|
| `status` | Enum | `valid`, `invalid`, `warning` |
| `checks_passed` | Array | List of passed validation checks |
| `checks_failed` | Array | List of failed validation checks with details |
| `traceability_chain` | Array | Complete provenance chain from output to source |
| `canon_layer_verified` | Boolean | Canon layer classification verified |

#### Validation Check Types

**Cross-Reference Validation:**
- Verify all entity references resolve to existing database/ records
- Verify all relationship claims match Family Authority
- Verify all visual claims match Visual Authority
- Verify all identity claims match Character Authority

**Canon-Layer Validation:**
- Verify Active Canon content is not mixed with Cultural Canon
- Verify Historical Canon content is properly classified
- Verify no Deferred or Candidate Canon content is treated as Active
- Verify Cultural Canon is never presented as factual

**Authority Ownership Validation:**
- Verify no engine output claims ownership of data it doesn't own
- Verify Character data comes from Character Authority
- Verify Family data comes from Family Authority
- Verify Visual data comes from Visual Authority
- Verify Experience data comes from Experience Authority

**Traceability Validation:**
- Verify every output element has a provenance chain
- Verify all source paths point to existing database/ files
- Verify no orphaned output exists without canonical source

#### Query Boundaries

```
validation_engine MAY:
  - Query any authority layer for verification
  - Reject output that fails validation checks
  - Flag warnings for borderline cases
  - Generate traceability reports
  - Log all validation results for audit

validation_engine MAY NOT:
  - Modify data to make it pass validation
  - Override authority decisions
  - Bypass checks for any engine
  - Create new canonical records to resolve conflicts
```

---

## Engine Interaction Protocol

### Query Flow

```
1. Client → En_Core(query_type, entity_id, context)
2. En_Core → Route to appropriate engine
3. Engine → Query database/ (read-only)
4. Engine → Return data + provenance to En_Core
5. En_Core → validation_engine(data, source_engine, 'full')
6. validation_engine → Return validation result
7. IF valid: En_Core → Return data to client
8. IF invalid: En_Core → Return error + validation report
```

### Forbidden Operations (All Engines)

| Operation | Rule | Authority |
|-----------|------|-----------|
| Create new canon | PROHIBITED | R-007-ENG-001 |
| Override canonical values | PROHIBITED | R-007-ENG-001 |
| Modify database/ records | PROHIBITED | R-007-ENG-001 |
| Infer facts not in database/ | PROHIBITED | R-007-ENG-001 |
| Store derived relationships as canon | PROHIBITED | ADR-002 |
| Promote scenario data to canon | PROHIBITED | ADR-005 |
| Treat Cultural Canon as Active | PROHIBITED | ADR-006 |
| Bypass validation_engine | PROHIBITED | R-007-ENG-004 |

---

## Implementation Constraints

### Language & Platform
- **Target:** JavaScript (ES5) for maximum compatibility
- **No external dependencies** for core engine logic
- **Platform adapters** may be added for specific deployment targets

### Module Structure (Future)

```
engines/
├── en_core.js              — Central orchestration
├── family_engine.js        — Genealogy queries
├── relationship_engine.js  — Relationship computation
├── experience_engine.js    — Scenario context
├── validation_engine.js    — Compliance checking
└── adapters/
    ├── janitorai_adapter.js    — JanitorAI export
    ├── sillytavern_adapter.js  — SillyTavern export
    └── json_adapter.js         — Generic JSON export
```

### Data Access Rules
- All engines read from `database/` only
- No engine writes to `database/`
- No engine reads from `core/`, `.trae/`, or `reports/` for canonical data
- Research archives (NotebookLM, Progetti) are never queried by engines

---

## Authority

**Established by:** Architecture Review & Canon Authority  
**Approved by:** Canon Freeze v1 Governance  
**Depends on:** ADR-000 through ADR-006, R-007, Architecture.md  
**Version:** 1.0 — Frozen under Canon Freeze v1
