# ENGINE KNOWLEDGE GUIDE

**Version:** 1.0
**Date:** 2026-06-08
**Purpose:** Operational guide to SvartúlfrVerse engine architecture. Companion to ENGINE_SPECIFICATION.md — explains what it means, why it exists, how to use it, and common mistakes to avoid.

---

## 1. WHY ENGINES EXIST

Engines solve one fundamental problem: **the repository contains canonical data, but canonical data alone doesn't generate bot responses.** Engines are the query and knowledge layer that sits between the database and the consumer (bot, lorebook, export, API).

Think of it this way:
- **database/** = the library of record (what's true)
- **engines/** = the librarians (who fetch and deliver specific knowledge)
- **exporters** = the translators (who format specific knowledge for specific platforms)

**The engines don't make decisions about what's canon.** They only serve what the Authority layers have decided. This is the single most important principle of engine design.

---

## 2. ENGINE ARCHITECTURE — THE BIG PICTURE

The engine architecture follows a hub-and-spoke model with a mandatory validation gate:

```
User Request → En_Core (router) → Sector Engine → database/ (fetched data)
                                                    ↓
                                              validation_engine (gate)
                                                    ↓
                                              Validated Output
```

### The Five Engines

| Engine | Role | Scope | Database Access |
|--------|------|-------|----------------|
| **En_Core** | Central router + context manager | Orchestration | Routes to sector engines |
| **family_engine** | Genealogy queries | Family/relationship data | database/families/ (read) |
| **relationship_engine** | Cross-authority relationship computation | Computed connections | database/ (read) |
| **experience_engine** | Scenario context | Situational state | database/experiences/ (read) |
| **validation_engine** | Compliance gatekeeper | All output | database/ (read for verification) |

### What Each Engine ACTUALLY Does (Plain Language)

**En_Core:** The receptionist. Receives every request, decides which engine handles it, combines results if needed, hands everything through validation, returns the final output. It doesn't know about families or experiences — it knows who to ask.

**family_engine:** The genealogy specialist. You give it a person ID and a question ("who are their parents?", "what dynasty do they belong to?"), it looks up the family records and returns structured data. It computes derived relationships (siblings, ancestry) on the fly but NEVER stores them.

**relationship_engine:** The connection finder. Given two entities, it finds how they're connected — through blood, marriage, scenario context, or any combination. It validates claimed relationships against authority records.

**experience_engine:** The scene manager. It knows what scenario a character is in, what role they're playing, what their occupation/residence is in this specific context. It CAN override character occupation/residence for the duration of a scenario.

**validation_engine:** The quality inspector. Before ANY engine output reaches the user, validation checks it against the canonical database. Does this data exist? Does it come from the right authority? Is the canon layer correct? Is the provenance chain complete?

---

## 3. ENGINE BOUNDARIES — THE RULES THAT MATTER

### The Read-Only Principle

**ALL engines read from database/. NO engine writes to database/.**

This is not a suggestion; it is the foundational constraint. The database is the Single Source of Truth (ADR-000). If engines could modify it, the data would no longer be a reliable source of truth.

The ONE exception: `experience_engine` has read/write access to `database/experiences/` because it owns that domain. But even it cannot write to characters/, families/, or worlds/.

### The No-Inference Principle

**Engines do not infer facts not present in database/.**

If Wulfnic's favorite color isn't in his character record, the engine returns `not_found`, not a guess. This is critical for canon integrity. See the Missing Evidence Rule in project_memory.

### The Authority Respect Principle

An engine can never return data that claims authority it doesn't have:
- family_engine returns genealogy — not character personality
- experience_engine returns scenario context — not biography
- No engine creates new canonical records

### The Validation Mandatory Principle

**No output is released without passing validation_engine.** No exceptions. Not even internal calls. The validation gate is always active.

---

## 4. COMMON IMPLEMENTATION MISTAKES

### Mistake 1: Writing to the Database
**What happens:** An engine "helpfully" caches derived data by writing it to the database.
**Why it breaks:** The database is no longer a clean canonical source. Future audits can't distinguish between authority decisions and engine artifacts.
**Fix:** Cache in memory only. Derive at runtime. Never persist.

### Mistake 2: Inferring Missing Data
**What happens:** A character record is missing occupation. The engine says "well, based on their education, they probably work in X."
**Why it breaks:** Inferred data is hallucinated data. It has no canonical source.
**Fix:** Return `not_found` for missing fields. Let the caller (human or bot) handle gaps.

### Mistake 3: Skipping Validation "Just This Once"
**What happens:** During development, an engine bypasses validation for testing.
**Why it breaks:** Unvalidated output may contain authority violations that propagate to exports.
**Fix:** Always validate. If validation is too slow for development, use a test-specific validation mock — but never ship without real validation.

### Mistake 4: Engine Bleed (Cross-Authority Contamination)
**What happens:** family_engine returns personality data because "it's related to the family."
**Why it breaks:** Family Authority doesn't own personality. Each data domain has exactly one owner.
**Fix:** Return only data owned by the queried authority. Cross-reference through relationship_engine if needed.

### Mistake 5: Hardcoding Canon Values
**What happens:** Engine code contains hardcoded values like `if (id === 'C_Wulfnic') return 'Bloodmoon'`.
**Why it breaks:** When canon changes (ADR update), every hardcoded reference becomes stale.
**Fix:** All canon values come from database/. Engine code contains only logic, never data.

### Mistake 6: Excessive Depth in Graph Traversal
**What happens:** family_engine traverses the family graph to depth 20, causing performance issues and returning irrelevant ancestors.
**Why it breaks:** Most use cases need depth 1-3. Excessive depth wastes computation and clutters results.
**Fix:** Default depth to 1. Maximum depth of 5. Let callers request more if needed.

### The Pronoun Macro Boundary — Validated Runtime State

> **Validated Runtime Constraint (as of Phase 15 testing — 2026-06-09)**
>
> **Observed Runtime Behavior:**
>
> | Layer | `{{sub}}` expansion | Status |
> |-------|---------------------|--------|
> | Prompt-facing fields (Personality, Scenario, Initial Message) | Expanded → `he` / `she` / `they` | **Available** |
> | JavaScript runtime (tested) | Not expanded → literal `{{sub}}` | **Unavailable** |
>
> **Validated macros:**
> `{{sub}}`, `{{obj}}`, `{{poss}}`, `{{poss_p}}`, `{{ref}}`
>
> **Current engineering assumption (until contrary evidence exists):**
> - **Prompt Layer Access** = Available
> - **JavaScript Runtime Access** = Unavailable
>
> **ADR Operational Rule:** Pronoun-dependent resolution belongs in prompt construction, not in JavaScript conditional logic. Engine implementations must use:
> - Personality authority layers
> - Scenario authority layers
> - Initial Message authority layers
> - Prompt injections
> - Lorebook injections
> - Other model-visible prompt construction systems
>
> **Future Update Path:** If Phase 16/17 runtime validation reveals a direct pronoun API (e.g., `chat.user.pronouns`), this constraint will be updated. Until then, the above assumption holds.

---

## 5. HOW ENGINES INTERACT WITH OTHER SYSTEMS

### Engine + Bot Export Flow
```
Bot Export Request
    ↓
En_Core receives: query_type='character', entity_id='C_Alyssa'
    ↓
En_Core routes to character query → database/characters/C_Alyssa_Douglas_Bloodmoon.md
En_Core routes to family_engine: query='parents', entity_id='C_Alyssa'
En_Core routes to experience_engine: query='context', experience_id='current'
    ↓
All results aggregated → validation_engine(full)
    ↓
If valid → Format as platform schema → Attach provenance → Return bot card
If invalid → Reject → Return validation error report
```

### Engine + Lorebook Export Flow
```
Lorebook Generation Request (domain: families)
    ↓
En_Core queries: query_type='family', domain='all'
    ↓
family_engine returns: all family records
    ↓
For each record:
    - Extract fields per LOREBOOK_SPECIFICATION.md
    - Classify canon layer
    - Generate entry
    - validation_engine(cross_reference + canon_layer) on each entry
    ↓
All validated entries → Assemble lorebook file with metadata header
    ↓
validation_engine(traceability) on complete file
    ↓
If valid → Write lorebook file
If invalid → Reject file with error report
```

### Engine + Validation Workflow
```
Output generated by any engine
    ↓
validation_engine receives: data, source_engine, validation_type
    ↓
Cross-reference check: Do all entity references resolve?
Canon-layer check: Is each element correctly classified?
Authority check: Does each element come from its owning authority?
Traceability check: Does each element have a provenance chain?
    ↓
All checks pass → status: 'valid'
Any check fails → status: 'invalid' + detailed failure report
Borderline case → status: 'warning' + warning log
```

---

## 6. IMPLEMENTATION GUIDANCE

### Where to Start
**Always start with validation_engine (Phase 15).** Every other engine depends on it. Without validation, you have no way to verify that your other engines are working correctly.

### Implementation Order
```
Phase 15: validation_engine     ← Start here
Phase 16: family_engine         ← Then these three (can be parallel)
         relationship_engine
         experience_engine
Phase 17: En_Core               ← Then the orchestrator
Phase 18: Bot exporters         ← Then exports
Phase 19: Lorebook exporters    ← Then lorebooks
```

### Technology Constraints
- **Language:** JavaScript (ES5) — maximum compatibility, no transpilation needed
- **No external dependencies** for core engine logic
- **Platform adapters** are separate modules that depend on core engines
- **Module structure:** Each engine is a separate file; adapters in subdirectory

### Testing Strategy
1. **Unit tests per engine:** Test each query type with known inputs/expected outputs
2. **Validation integration:** Every engine output must pass validation
3. **Authority boundary tests:** Verify engines return only data from their owning authority
4. **Negative tests:** Verify engines correctly return `not_found` for missing data
5. **Canon compliance tests:** Verify no rejected canon appears in any output

---

## 7. FUTURE IMPLEMENTATION GUIDANCE

### What NOT to Build (Yet)
- **Semantic search / embedding engines:** The current keyword-based system is sufficient for the current scope. Embedding-based retrieval adds complexity without proportional benefit for a 12-character canon.
- **Real-time synchronization:** Batch export is sufficient. Real-time sync adds infrastructure complexity.
- **Multi-language support:** Not needed until the canon explicitly requires it.

### What to Plan For
- **Caching layer:** As the canon grows, repeated queries to the same records should be cached in memory.
- **Batch operations:** Exporting all 12 characters at once should be a single operation, not 12 sequential calls.
- **Incremental lorebook updates:** When one character changes, only their lorebook entries should regenerate, not the entire lorebook.

### When to Expand the Engine Set
Only when a new Authority domain is added (ADR decision required). Each engine maps to an authority layer. New engine = new ADR.

---

## 📚 Cross-References

- **For engine interaction flow and data flow diagrams:** See [ENGINE_INTERACTION_MAP.md](ENGINE_INTERACTION_MAP.md)
- **For implementation sequencing (Phases 15-19):** See [ENGINE_IMPLEMENTATION_ROADMAP.md](ENGINE_IMPLEMENTATION_ROADMAP.md)
- **For bot export using engine output:** See [BOT_EXPORT_KNOWLEDGE_GUIDE.md](../Guidelines/BOT_EXPORT_KNOWLEDGE_GUIDE.md)
- **For validation engine details:** See [VALIDATION_KNOWLEDGE_GUIDE.md](../Guidelines/VALIDATION_KNOWLEDGE_GUIDE.md)
- **For all implementation patterns:** See [IMPLEMENTATION_PATTERNS.md](../Guidelines/IMPLEMENTATION_PATTERNS.md)

---

*This guide is derived from ENGINE_SPECIFICATION.md, ENGINE_INTERACTION_MAP.md, and ENGINE_IMPLEMENTATION_ROADMAP.md. For formal contracts and interface definitions, consult the specifications directly.*
