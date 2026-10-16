# ENGINE_INTERACTION_MAP

**Version:** 1.0  
**Date:** 2026-06-08  
**Authority:** ENGINE_SPECIFICATION.md, Architecture.md, R-007  
**Purpose:** Runtime architecture overview — data flow, inputs/outputs, authority boundaries.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          RUNTIME ARCHITECTURE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                        CLIENT / PROMPT LAYER                         │ │
│  │  (User prompts, scenario requests, export requests)                  │ │
│  └──────────────────────────────────┬────────────────────────────────────┘ │
│                                     │                                       │
│                                     ▼                                       │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     En_Core — Central Orchestration                  │ │
│  │  Routes queries, manages context, coordinates engines               │ │
│  └──────────────────────────┬────────────────────────────────────────────┘ │
│                             │                                               │
│         ┌───────────────────┼───────────────────┐                          │
│         │                   │                   │                          │
│         ▼                   ▼                   ▼                          │
│  ┌─────────────┐   ┌──────────────┐   ┌──────────────────┐               │
│  │ family_     │   │ relationship_│   │ experience_      │               │
│  │ engine      │   │ engine       │   │ engine           │               │
│  └──────┬──────┘   └──────┬───────┘   └────────┬─────────┘               │
│         │                 │                     │                         │
│         └─────────────────┼─────────────────────┘                         │
│                           │                                                │
│                           ▼                                                │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │              validation_engine — Mandatory Validation Gate           │ │
│  │  Cross-reference, canon-layer, authority, traceability checks       │ │
│  └──────────────────────────┬────────────────────────────────────────────┘ │
│                             │                                               │
│                             ▼                                               │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     database/ — Single Source of Truth               │ │
│  │  characters/  families/  worlds/  institutions/  experiences/       │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Data Flow: Query to Response

### Step-by-Step Flow

```
1. CLIENT → En_Core
   Input: query_type, entity_id, context, query_mode

2. En_Core → Route to appropriate engine
   - character/visual query → En_Core direct (reads database/)
   - family query → family_engine
   - relationship query → relationship_engine
   - experience query → experience_engine

3. Engine → database/ (READ-ONLY)
   - All engines read from database/
   - No engine writes to database/
   - No engine reads from core/, .trae/, or research archives

4. Engine → Return data + provenance to En_Core
   - Data: canonical records
   - Provenance: list of source file paths
   - Canon layer: active/historical/cultural

5. En_Core → validation_engine
   - Input: data, source_engine, validation_type
   - All output MUST pass validation before release

6. validation_engine → Return validation result
   - valid → proceed
   - warning → proceed with warning log
   - invalid → reject, return error report

7. En_Core → Return validated data to client
   - Data + provenance + canon_layer + validated flag
```

---

## Engine Input/Output Reference

### En_Core — Central Orchestration

**Inputs:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query_type | Enum | Yes | character, family, experience, relationship, visual, world |
| entity_id | String | Yes | Canonical entity identifier (e.g., C_Alyssa) |
| context | Object | No | Scenario context (location, time, role) |
| query_mode | Enum | No | read (default), validate, trace |

**Outputs:**
| Field | Type | Description |
|-------|------|-------------|
| status | Enum | ok, not_found, forbidden, invalid |
| data | Object | Canonical data from relevant authority layer |
| provenance | Array | List of source database/ file paths |
| canon_layer | Enum | active, historical, cultural |
| validated | Boolean | Whether output passed validation_engine |

---

### family_engine — Genealogy Query

**Inputs:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| entity_id | String | Yes | Canonical person identifier |
| query | Enum | Yes | parents, children, siblings, spouse, ancestry, dynasty, surname, full_graph |
| depth | Integer | No | Graph traversal depth (default: 1, max: 5) |

**Outputs:**
| Field | Type | Description |
|-------|------|-------------|
| status | Enum | ok, not_found, invalid_query |
| data | Object | Structured genealogical data |
| provenance | Array | Source file paths from database/families/ |
| canon_layer | Enum | Always active for family records |

**Derived Relationships (Computed, NOT Stored):**
| Query | Computation Rule |
|-------|------------------|
| parents | Direct lookup |
| children | Direct lookup |
| siblings | Compute: share ≥1 parent |
| spouse | Direct lookup |
| ancestry | Transitive parent traversal |
| dynasty | Direct lookup |
| surname | Direct lookup |
| full_graph | Union of all above |

---

### relationship_engine — Relationship Query

**Inputs:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| entity_a | String | Yes | First entity identifier |
| entity_b | String | Yes | Second entity identifier |
| query | Enum | Yes | relationship, connection_path, validate |
| scenario_context | Object | No | Scenario-specific context |

**Outputs:**
| Field | Type | Description |
|-------|------|-------------|
| status | Enum | ok, not_found, forbidden |
| relationship_type | String | Canonical relationship type |
| connection_path | Array | Ordered list of relationships connecting A→B |
| canonical | Boolean | True if relationship exists in authority records |
| scenario_only | Boolean | True if relationship exists only in experience layer |
| provenance | Array | Source file paths |

---

### experience_engine — Experience Context

**Inputs:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| experience_id | String | Yes | Canonical experience identifier |
| query | Enum | Yes | context, roles, occupation_overrides, residence, full_scenario |
| entity_filter | String | No | Optional character identifier filter |

**Outputs:**
| Field | Type | Description |
|-------|------|-------------|
| status | Enum | ok, not_found |
| scenario | Object | Scenario framing and setup |
| context_state | Object | Location, time, circumstances |
| roles | Object | Character→role mapping |
| occupation_overrides | Object | Character→occupation override mapping |
| residence_overrides | Object | Character→residence override mapping |
| provenance | Array | Source file paths from database/experiences/ |

---

### validation_engine — Compliance Check

**Inputs:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| data | Object | Yes | Engine output to validate |
| source_engine | Enum | Yes | Originating engine identifier |
| validation_type | Enum | Yes | cross_reference, canon_layer, authority_ownership, traceability, full |

**Outputs:**
| Field | Type | Description |
|-------|------|-------------|
| status | Enum | valid, invalid, warning |
| checks_passed | Array | List of passed validation checks |
| checks_failed | Array | List of failed checks with details |
| traceability_chain | Array | Complete provenance chain |
| canon_layer_verified | Boolean | Canon layer classification verified |

---

## Authority Boundary Enforcement

### Read-Only Access

All engines have **read-only** access to `database/`:

```
Engine            →  database/ Access
─────────────────────────────────────
family_engine     →  database/families/     (READ)
relationship_engine → database/families/    (READ)
                  →  database/characters/  (READ)
                  →  database/experiences/ (READ)
experience_engine →  database/experiences/ (READ/WRITE — owns this)
                  →  database/characters/  (READ)
                  →  database/families/    (READ)
                  →  database/worlds/     (READ)
validation_engine →  database/*            (READ — all layers)
```

### Write Prohibitions

| Engine | Prohibited Write | Reason |
|--------|------------------|--------|
| family_engine | Cannot write to database/families/ | Only Family Authority decisions modify family data |
| relationship_engine | Cannot store computed relationships | Derived relationships are never stored |
| experience_engine | Cannot write to database/characters/ | Character Authority owns character data |
| experience_engine | Cannot write to database/families/ | Family Authority owns family data |
| experience_engine | Cannot write to database/worlds/ | Visual Authority owns visual data |
| validation_engine | Cannot modify any database/ data | Validation is read-only compliance check |

---

## Traceability Flow

Every output element must have a complete provenance chain:

```
Output Element
    │
    ├── Engine: [engine_name]
    │       │
    │       ├── Source: database/[authority]/[file].md
    │       │       │
    │       │       ├── Authority: [Character/Family/Visual/Experience]
    │       │       ├── Canon Layer: [Active/Historical/Cultural]
    │       │       └── Canon Version: 1.0
    │       │
    │       └── Validation: validation_engine status [valid/invalid/warning]
    │               │
    │               ├── Checks Passed: [list]
    │               └── Checks Failed: [list]
    │
    └── Provenance Chain: [output → engine → database/ file → authority]
```

**Example:**
```
Output: "Alyssa Douglas-Bloodmoon, age 19"
    │
    ├── Engine: En_Core (routed to character query)
    │       │
    │       ├── Source: database/characters/C_Alyssa_Douglas_Bloodmoon.md
    │       │       ├── Authority: Character Authority
    │       │       ├── Canon Layer: Active
    │       │       └── Canon Version: 1.0
    │       │
    │       └── Validation: valid
    │               ├── Checks Passed: CR-001, CR-301, CL-001, AO-001, TR-001
    │               └── Checks Failed: none
    │
    └── Provenance Chain: output → En_Core → C_Alyssa.md → Character Authority
```

---

## Forbidden Operations

| Operation | All Engines | Authority |
|-----------|-------------|-----------|
| Create new canon | PROHIBITED | R-007-ENG-001 |
| Override canonical values | PROHIBITED | R-007-ENG-001 |
| Modify database/ records | PROHIBITED | R-007-ENG-001 |
| Infer facts not in database/ | PROHIBITED | R-007-ENG-001 |
| Store derived relationships as canon | PROHIBITED | ADR-002 |
| Promote scenario data to canon | PROHIBITED | ADR-005 |
| Treat Cultural Canon as Active | PROHIBITED | ADR-006 |
| Bypass validation_engine | PROHIBITED | R-007-ENG-004 |
| Query research archives | PROHIBITED | ENGINE_SPECIFICATION |
| Write engine logic into database/ records | PROHIBITED | R-007-ENG-002 |

---

## Export Pipeline Integration

### Bot Export Flow

```
Bot Generation Request
    │
    ▼
En_Core(character, entity_id, context)
    │
    ├── family_engine → genealogy data
    ├── experience_engine → scenario context
    └── database/characters/ → identity, personality, biography
    │
    ▼
validation_engine(full)
    │
    ├── valid → Format per platform schema → Attach provenance → Release
    └── invalid → Reject → Return error report
```

### Lorebook Export Flow

```
Lorebook Generation Request
    │
    ▼
En_Core(query all records in domain)
    │
    ├── For each record:
    │       Extract fields → Classify canon layer → Generate entry
    │       │
    │       └── validation_engine(cross_reference + canon_layer)
    │               ├── valid → Add to lorebook
    │               └── invalid → Skip + log error
    │
    ▼
validation_engine(traceability) on complete file
    │
    ├── valid → Write lorebook file with metadata header
    └── invalid → Reject file → Return error report
```

---

*This map is derived from ENGINE_SPECIFICATION.md and Architecture.md. All engine behavior is governed by R-007_Engine_Rules.*
