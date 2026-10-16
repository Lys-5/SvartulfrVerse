# IMPLEMENTATION PATTERNS

**Version:** 1.0
**Date:** 2026-06-08
**Purpose:** Practical handbook for implementation work. Extracts recurring patterns from all specifications and provides reusable workflows, dependency mapping, and traceability patterns.

---

## 1. RECURRING PATTERNS ACROSS SPECIFICATIONS

### Pattern 1: The Validation Gate

**Where it appears:** Every specification (ENGINE, BOT_EXPORT, LOREBOOK, VALIDATION_PIPELINE)

**The pattern:**
```
Data produced → Validation Gate → Validated Output (or Rejection)
```

**How to use it:** No data ever flows from production to consumption without passing through validation. This applies to:
- Engine queries → validated before returning to client
- Bot exports → validated before release
- Lorebook entries → validated before inclusion in file
- Any derived artifact → validated before distribution

**Key insight:** Validation is not a final step. It's an integral part of every data flow. Design WITH validation, not as an afterthought.

---

### Pattern 2: Authority-Based Routing

**Where it appears:** ENGINE_SPECIFICATION.md, BOT_EXPORT_SPECIFICATION.md, EXPORT_MAPPING_MATRIX.md

**The pattern:**
```
Data request → Identify owning authority → Route to authority's source → Return data
```

**How to use it:** When you need data about a character:
1. Identity/psychology? → Character Authority → database/characters/
2. Genealogy? → Family Authority → database/families/
3. Visual? → Visual Authority → database/worlds/
4. Scenario? → Experience Authority → database/experiences/

**Key insight:** If you're pulling genealogy data from a character file, something is wrong. Every data domain has exactly one owner.

---

### Pattern 3: Three-Layer Architecture

**Where it appears:** BOT_SEARCH_SPECIFICATION.md (lorebook), JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md (character design)

**The pattern:**
```
Layer 1: Permanent (always in context)     → Essential, concise
Layer 2: Triggered (context-activated)     → Deep, specific
Layer 3: Repository-only (never in context)→ Meta, dev-only
```

**How to use it:**

For character cards:
- Layer 1 (Permanent): Core identity, personality, behavioral anchors
- Layer 2 (Triggered): Backstory, relationship deep-dives, world knowledge
- Layer 3 (Repository): Author notes, rejected content, development history

For lorebooks:
- Layer 1 (Always-on/Constant): Critical world rules
- Layer 2 (Keyword-triggered): Character details, location descriptions
- Layer 3 (Separate files): Historical/cultural entries in separate lorebooks by layer

---

### Pattern 4: Source Attribution Chain

**Where it appears:** All specifications

**The pattern:**
```
Output Element → Engine that produced it → Database file → Authority → Canon Version
```

**How to use it:** Every output element should be traceable. In practice, this means:
- Every field in a bot export maps to a database/ field
- Every lorebook entry has a source_id pointing to a database record
- Every engine response includes a provenance array
- The provenance chain is never broken

**Implementation:** The `extensions.svartulfrverse` block in bot exports IS the attribution chain for that bot.

---

### Pattern 5: Separation of Read and Write

**Where it appears:** ENGINE_SPECIFICATION.md, ARCHITECTURE.md

**The pattern:**
```
Engines: Read from database/ (never write)
Authorities: Write to database/ (through governance workflow)
Exporters: Write to output/ (never to database/)
```

**How to use it:** If you find code where an engine writes to database/, that's a bug. The only write path to database/ is through the Authority governance workflow (ADR update → Authority decision → Database update).

---

### Pattern 6: Canon Layer Tagging

**Where it appears:** LOREBOOK_SPECIFICATION.md, ADR-006, BOT_SEARCH_SPECIFICATION.md

**The pattern:**
```
Every piece of data → Exactly one canon layer tag
```

The five layers and their handling:

| Layer | Tag | Export Handling |
|-------|-----|-----------------|
| Active | `active` | Full inclusion |
| Historical | `historical` | Included with period context |
| Cultural | `cultural` | Included with non-factual disclaimer |
| Deferred | `deferred` | Not included in runtime exports |
| Candidate | `candidate` | Not included until promoted |

---

## 2. RECOMMENDED WORKFLOWS

### Workflow 1: Creating a New Character Bot Export

```
Step 1: Verify character record exists in database/characters/C_[Name].md
Step 2: Verify all authority data is complete
    ├─ Identity data (Character Authority)
    ├─ Genealogy data (Family Authority)
    ├─ Visual data (Visual Authority)
    └─ Default experience (Experience Authority)
Step 3: Identify target platform (JanitorAI / SillyTavern / Generic JSON)
Step 4: Collect data from all authorities
Step 5: Format per platform schema
Step 6: Run validation_engine(full)
Step 7: If PASS → Attach provenance → Release
        If FAIL → Review errors → Fix data → Re-validate
```

### Workflow 2: Creating a Lorebook

```
Step 1: Identify target domain (characters / families / worlds / experiences)
Step 2: Identify target canon layer (active / historical / cultural)
Step 3: Query all relevant records from database/
Step 4: For each record:
    a. Extract relevant fields
    b. Format per entry template
    c. Assign keywords (3-5 specific, contextual)
    d. Assign priority (10-100 based on importance)
    e. Tag with canon layer
    f. Add source attribution
    g. Run validation_engine(cross_reference + canon_layer)
Step 5: Assemble entries into lorebook file with metadata header
Step 6: Run validation_engine(traceability) on complete file
Step 7: If PASS → Release
        If FAIL → Fix failing entries → Re-validate
```

### Workflow 3: Adding a New Character to the Repository

```
Step 1: Create character record following C_Template.md
Step 2: Verify Character Authority compliance (R-003)
Step 3: Verify no genealogy in character file (R-003-CHR-007)
Step 4: Add family relationships to F_Parent_Child.md and/or F_Marriages.md
Step 5: Add visual classification per W_Visual_Inheritance.md
Step 6: Run Character Audit (skill)
Step 7: If PASS → Character is ready for export
        If FAIL → Fix issues → Re-audit
```

### Workflow 4: Canon Layer Change

```
Step 1: Identify the data element to reclassify
Step 2: Verify the new classification complies with ADR-006 definitions
Step 3: Update the source record with new canon layer
Step 4: Update all derived lorebook entries
Step 5: Update all affected bot exports
Step 6: Update all affected lorebooks
Step 7: Run full validation on all affected outputs
Step 8: Document the change in the relevant ADR or appendix
```

---

## 3. IMPLEMENTATION ORDER

### For Engine Development (Phases 15-19)

```
Phase 15: validation_engine     ← ALWAYS FIRST
    ↓
Phase 16: family_engine         ← These three can be parallel
         relationship_engine
         experience_engine
    ↓
Phase 17: En_Core               ← Orchestrator (depends on all above)
    ↓
Phase 18: Bot exporters         ← Depends on En_Core
    ↓
Phase 19: Lorebook exporters    ← Depends on En_Core
```

### For Documentation/Knowledge Development (This Session)

```
Step 1: Read all source specifications
Step 2: Create knowledge guides (companion documents)
Step 3: Create best practices document (external knowledge synthesis)
Step 4: Create external resources index
Step 5: Review all documents for cross-consistency
Step 6: Validate against governance (ADRs, Rules)
```

---

## 4. DEPENDENCY MAPPING

### Specification Dependencies

```
ADR-000 (Runtime Baseline)
    ↓
ADR-001-005 (Authority Definitions)
    ↓
ADR-006 (Canon Layer Architecture)
    ↓
    ├─→ R-007 (Engine Rules)
    │       ↓
    │       └─→ ENGINE_SPECIFICATION.md
    │               ↓
    │               └─→ ENGINE_INTERACTION_MAP.md
    │               └─→ ENGINE_IMPLEMENTATION_ROADMAP.md
    │
    ├─→ R-008 (Bot Rules)
    │       ↓
    │       └─→ BOT_EXPORT_SPECIFICATION.md
    │               ↓
    │               └─→ EXPORT_MAPPING_MATRIX.md
    │
    ├─→ R-009 (Lorebook Rules)
    │       ↓
    │       └─→ LOREBOOK_SPECIFICATION.md
    │               ↓
    │               └─→ BOT_SEARCH_SPECIFICATION.md
    │
    └─→ VALIDATION_PIPELINE_SPECIFICATION.md
```

### Knowledge Guide Dependencies

```
Source Specifications (core/)
    ↓
Knowledge Guides (knowledge/)
    ├─→ ENGINE_KNOWLEDGE_GUIDE.md ← ENGINE_SPECIFICATION.md
    ├─→ BOT_EXPORT_KNOWLEDGE_GUIDE.md ← BOT_EXPORT_SPECIFICATION.md
    ├─→ BOT_SEARCH_KNOWLEDGE_GUIDE.md ← BOT_SEARCH_SPECIFICATION.md
    ├─→ LOREBOOK_KNOWLEDGE_GUIDE.md ← LOREBOOK_SPECIFICATION.md + BOT_SEARCH_SPECIFICATION.md
    ├─→ VALIDATION_KNOWLEDGE_GUIDE.md ← VALIDATION_PIPELINE_SPECIFICATION.md
    └─→ IMPLEMENTATION_PATTERNS.md ← ALL specifications
```

---

## 5. TRACEABILITY PATTERNS

### Pattern: Provenance in Bot Exports

Every bot export includes:

```json
"extensions": {
  "svartulfrverse": {
    "canon_id": "<canonical_identifier>",
    "canon_layer": "<active|historical|cultural>",
    "provenance": ["<source_file_path>", ...],
    "visual_classification": "<classification>",
    "dynasty": "<dynasty_name>",
    "validation_status": "PASS",
    "generation_timestamp": "<ISO_8601>",
    "canon_version": "1.0"
  }
}
```

**When to use:** Every single bot export. No exceptions.

### Pattern: Source Attribution in Lorebook Entries

Every lorebook entry includes:

```markdown
**Canon Layer:** <layer>
**Source:** <database/file/path.md>
**Authority:** <Authority Domain>
**Last Synchronized:** <ISO_8601>
**Entry ID:** <LB-XXX-NNN>
```

**When to use:** Every single lorebook entry. No exceptions.

### Pattern: Engine Traceability

Every engine response includes:

```json
{
  "status": "<ok|not_found|forbidden|invalid>",
  "data": { ... },
  "provenance": ["<source_file_path>", ...],
  "canon_layer": "<active|historical|cultural>",
  "validated": true
}
```

---

## 6. REUSABLE PATTERNS CHECKLIST

Use this checklist when creating any new artifact:

- [ ] Does it trace to a canonical source? (database/ file)
- [ ] Does it have the correct canon layer tag?
- [ ] Does it come from the correct authority?
- [ ] Has it passed validation?
- [ ] Does it include provenance metadata?
- [ ] Does it comply with the relevant Rules (R-000 through R-009)?
- [ ] Does it comply with the relevant ADRs?
- [ ] Is it free of rejected canon content?
- [ ] Is it free of cross-authority contamination?
- [ ] Does it use the correct template/format for its type?

---

## 📚 Cross-References

- **For engine architecture patterns:** See [ENGINE_KNOWLEDGE_GUIDE.md](../Engine_Logic/ENGINE_KNOWLEDGE_GUIDE.md)
- **For export patterns:** See [BOT_EXPORT_KNOWLEDGE_GUIDE.md](./BOT_EXPORT_KNOWLEDGE_GUIDE.md)
- **For search/discovery patterns:** See [BOT_SEARCH_KNOWLEDGE_GUIDE.md](./BOT_SEARCH_KNOWLEDGE_GUIDE.md)
- **For lorebook patterns:** See [LOREBOOK_KNOWLEDGE_GUIDE.md](../Lore_Worldbuilding/LOREBOOK_KNOWLEDGE_GUIDE.md)
- **For validation patterns:** See [VALIDATION_KNOWLEDGE_GUIDE.md](./VALIDATION_KNOWLEDGE_GUIDE.md)
- **For best practices by workflow:** See [JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md](./JANITORAI_AND_ROLEPLAY_BEST_PRACTICES.md)

---

*This document extracts patterns from all project specifications: ENGINE_SPECIFICATION.md, BOT_EXPORT_SPECIFICATION.md, BOT_SEARCH_SPECIFICATION.md, LOREBOOK_SPECIFICATION.md, VALIDATION_PIPELINE_SPECIFICATION.md, EXPORT_MAPPING_MATRIX.md, ADR-000 through ADR-006, and R-000 through R-009.*
