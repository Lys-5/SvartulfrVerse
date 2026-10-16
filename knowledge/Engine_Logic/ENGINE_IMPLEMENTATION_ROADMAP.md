# ENGINE_IMPLEMENTATION_ROADMAP

**Version:** 1.0  
**Date:** 2026-06-08  
**Authority:** ENGINE_SPECIFICATION.md, ADR-000, ADR-006, R-007  
**Purpose:** Implementation sequencing guide for all engine systems.

---

## Current State

**Phase:** Canon Freeze v1 — ACTIVE  
**Repository Status:** SOURCE INTEGRATION COMPLETE — READY_FOR_SCRIPT_GENERATION  
**Database:** All 12 Active Canon characters, 3 Historical Canon records, governance documents complete.

**What Exists:**
- Complete ADR architecture (ADR-000 through ADR-006)
- Complete rule set (R-000 through R-009)
- Complete skill set (11 skills)
- Complete command set (12 commands)
- Complete specifications (ENGINE, BOT_EXPORT, LOREBOOK, VALIDATION_PIPELINE)
- Complete canonical data in `database/`
- Reference knowledge layer in `knowledge/`

**What Does NOT Exist:**
- No engine code has been written
- No validation engine implementation
- No family engine implementation
- No bot exporter implementation
- No lorebook exporter implementation

---

## Implementation Phases

### Phase 15: Validation Engine

**Priority:** CRITICAL — Must be first. All other engines depend on validation.

**Scope:** Implement `validation_engine` as defined in ENGINE_SPECIFICATION.md.

**Dependencies:**
- ✅ Canon Freeze v1 (complete)
- ✅ All database/ records (complete)
- ✅ VALIDATION_PIPELINE_SPECIFICATION.md (complete)
- ✅ All ADRs (complete)

**Implementation Order:**

```
Step 1: validation_engine.js — Core validation module
    │
    ├── Step 1a: Entity Resolution (CR-001 through CR-005)
    │       Verify all references resolve to existing database/ records
    │
    ├── Step 1b: Relationship Consistency (CR-101 through CR-105)
    │       Verify family relationship claims against F_Parent_Child.md
    │
    ├── Step 1c: Visual Consistency (CR-201 through CR-203)
    │       Verify visual claims against W_Visual_Baseline.md
    │
    ├── Step 1d: Identity Consistency (CR-301 through CR-304)
    │       Verify identity claims against character records
    │
    ├── Step 1e: Canon-Layer Classification (CL-001 through CL-006)
    │       Verify layer boundaries and classification
    │
    ├── Step 1f: Rejected Canon Detection (CL-201 through CL-205)
    │       Detect and reject known rejected concepts
    │
    ├── Step 1g: Authority Ownership (AO-001 through AO-104)
    │       Verify data comes from correct authority layer
    │
    └── Step 1h: Traceability (TR-001 through TR-103)
            Verify provenance chains and version tracking
```

**Output:** `validation_engine.js` — 47-check validation module.

**Success Criteria:**
- All 47 checks implemented
- All checks return pass/fail with detailed error information
- Integration test: validate all existing database/ records → all PASS

---

### Phase 16: Query Engines

**Priority:** HIGH — Required for any runtime functionality.

**Scope:** Implement `family_engine`, `relationship_engine`, and `experience_engine`.

**Dependencies:**
- ✅ Phase 15 (validation_engine must be complete)
- ✅ All database/ records (complete)

**Implementation Order:**

```
Step 1: family_engine.js — Genealogy Query Engine
    │
    ├── Parent-Child queries (direct lookup)
    ├── Marriage queries (direct lookup)
    ├── Dynasty membership queries
    ├── Surname authority queries
    ├── Derived relationship computation (siblings, ancestry)
    │       Note: Derived relationships are computed, NEVER stored
    └── validation_engine integration (all queries validated)

Step 2: relationship_engine.js — Relationship Query Engine
    │
    ├── Canonical relationship path computation
    ├── Scenario-specific relationship queries
    ├── Cross-authority relationship validation
    └── validation_engine integration

Step 3: experience_engine.js — Experience Context Engine
    │
    ├── Scenario framing queries
    ├── Context state management
    ├── Role assignment queries
    ├── Occupation override management
    ├── Residence override management
    └── validation_engine integration
```

**Output:** `family_engine.js`, `relationship_engine.js`, `experience_engine.js`.

**Success Criteria:**
- All engines read from `database/` only (no writes)
- All engines pass validation_engine checks
- Derived relationships are computed, not stored
- Family graph traverses correctly up to depth 5

---

### Phase 17: Central Orchestration

**Priority:** HIGH — Required for unified query interface.

**Scope:** Implement `En_Core` — central orchestration and query routing.

**Dependencies:**
- ✅ Phase 16 (all query engines must be complete)
- ✅ Phase 15 (validation_engine must be complete)

**Implementation:**

```
En_Core.js — Central Orchestration Engine
    │
    ├── Query router (routes to appropriate engine)
    ├── Context resolver (manages scenario context)
    ├── Response aggregator (combines multi-engine responses)
    ├── Provenance tracker (maintains source attribution)
    └── Validation gate (all output passes validation_engine)
```

**Output:** `en_core.js`.

**Success Criteria:**
- Single entry point for all queries
- All queries routed to correct engine
- All output validated before return
- Provenance metadata attached to all responses

---

### Phase 18: Bot Exporter

**Priority:** MEDIUM — Required for JanitorAI/SillyTavern export.

**Scope:** Implement bot character card generation for all supported platforms.

**Dependencies:**
- ✅ Phase 17 (En_Core must be complete)
- ✅ BOT_EXPORT_SPECIFICATION.md (complete)
- ✅ All character records in database/ (complete)

**Implementation Order:**

```
Step 1: Generic JSON exporter
    │       Canonical export schema per BOT_EXPORT_SPECIFICATION.md
    │
    ├── Step 2: JanitorAI adapter
    │       JSON + Markdown format per JanitorAI character card schema
    │
    └── Step 3: SillyTavern adapter
            Character Card V3 format per SillyTavern schema
```

**Output:** `adapters/janitorai_adapter.js`, `adapters/sillytavern_adapter.js`, `adapters/json_adapter.js`.

**Success Criteria:**
- All 12 Active Canon characters exportable
- All exports pass validation_engine (full)
- All exports include provenance metadata
- All exports include `extensions.svartulfrverse` traceability block
- Platform-specific schemas validated

---

### Phase 19: Lorebook Exporter

**Priority:** MEDIUM — Required for world knowledge base generation.

**Scope:** Implement lorebook generation with canon-layer tagging.

**Dependencies:**
- ✅ Phase 17 (En_Core must be complete)
- ✅ LOREBOOK_SPECIFICATION.md (complete)

**Implementation Order:**

```
Step 1: Lorebook entry generator
    │       Standardized entry format per LOREBOOK_SPECIFICATION.md
    │
    ├── Step 2: Canon-layer tagging system
    │       Active/Historical/Cultural classification per ADR-006
    │
    ├── Step 3: Source attribution system
    │       Primary and supporting source citation
    │
    └── Step 4: Platform adapters
            JanitorAI lorebook format, SillyTavern format
```

**Output:** Lorebook generation module with platform adapters.

**Success Criteria:**
- Separate lorebook files per canon layer
- All entries tagged with exactly one canon layer
- All entries include source attribution
- Cultural Canon entries include non-factual disclaimer
- Deferred/Candidate entries excluded from runtime lorebooks

---

### Future Phases (Post-Phase 19)

| Phase | Scope | Dependencies |
|-------|-------|--------------|
| Phase 20 | Batch export pipeline (all characters at once) | Phase 18 |
| Phase 21 | Lorebook synchronization system (auto-regenerate on DB change) | Phase 19 |
| Phase 22 | Runtime integration testing (full end-to-end) | Phases 15-19 |
| Phase 23 | Performance optimization (caching, indexing) | Phase 22 |
| Phase 24+ | World system expansion (requires new ADR) | ADR approval |

---

## Dependency Graph

```
                    ┌─────────────────────┐
                    │   Canon Freeze v1   │
                    │   database/ (complete)│
                    │   ADRs (complete)    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Phase 15            │
                    │  validation_engine   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
     ┌────────────┐  ┌──────────────┐  ┌──────────────┐
     │ family_    │  │ relationship_│  │ experience_  │
     │ engine     │  │ engine       │  │ engine       │
     └─────┬──────┘  └──────┬───────┘  └──────┬───────┘
           │                │                  │
           └────────────────┼──────────────────┘
                            │
                            ▼
                 ┌────────────────────┐
                 │  Phase 17          │
                 │  En_Core           │
                 └─────────┬──────────┘
                           │
              ┌────────────┼────────────┐
              │                         │
              ▼                         ▼
     ┌────────────────┐      ┌────────────────┐
     │  Phase 18      │      │  Phase 19      │
     │  Bot Exporter  │      │  Lorebook      │
     │                │      │  Exporter      │
     └────────────────┘      └────────────────┘
```

---

## Implementation Constraints

All engine implementation must comply with:

| Constraint | Rule | Authority |
|------------|------|-----------|
| No engine writes to `database/` | MANDATORY | R-007-ENG-001 |
| All engine output passes validation | MANDATORY | R-007-ENG-004 |
| All engine output is traceable | MANDATORY | R-007-ENG-003 |
| Engine logic separate from canon data | MANDATORY | R-007-ENG-002 |
| Target: JavaScript (ES5) | MANDATORY | ENGINE_SPECIFICATION |
| No external dependencies for core logic | MANDATORY | ENGINE_SPECIFICATION |
| Research archives never queried by engines | MANDATORY | ENGINE_SPECIFICATION |

---

## Module Structure (Target)

```
engines/
├── en_core.js                 — Central orchestration (Phase 17)
├── family_engine.js           — Genealogy queries (Phase 16)
├── relationship_engine.js     — Relationship computation (Phase 16)
├── experience_engine.js       — Scenario context (Phase 16)
├── validation_engine.js       — Compliance checking (Phase 15)
└── adapters/
    ├── janitorai_adapter.js   — JanitorAI export (Phase 18)
    ├── sillytavern_adapter.js — SillyTavern export (Phase 18)
    ├── json_adapter.js        — Generic JSON export (Phase 18)
    └── lorebook_adapter.js    — Lorebook generation (Phase 19)
```

---

*This roadmap is derived from ENGINE_SPECIFICATION.md and ADR-000 through ADR-006. Implementation cannot begin until Canon Freeze v1 is maintained and all database/ records are stable.*
