# ADR-001: Dynastic Origins — Los Angeles Dynasty Baseline

**Status:** ACCEPTED  
**Date:** 2026-06-07  
**Title:** Canonical Origins and Genealogical Structure of the Los Angeles Dynasty

## Context

The repository bootstrap (ADR-000) established the need for canonical stabilization and explicitly identified legacy relationship degradation as a critical failure mode. A significant genealogical conflict exists in the historical archive regarding the lineages of Erik Douglas and Wulfnic Bloodmoon.

Before any Family Authority Layer logic is implemented, the foundational dynastic origins, early migrations, and family structures must be formally established and canonicalized. This ADR resolves the genealogical foundation for all future Los Angeles Dynasty character and family development.

## Decision

We establish the following as absolute canonical authority for the Los Angeles Dynasty baseline:

### Scope

- **Only Human** (no supernatural elements)
- **Contemporary** (2020s-2030s timeline)
- **Los Angeles Dynasty** (geographic and familial focus)

### Dynasty Origins and Early Migration

#### Bloodmoon Dynasty

- **Origin:** Iceland
- **Early Migration:** Migration from Iceland to North America occurred after 1930
- **Generation Structure:**
  - First generation in Iceland (parents of Wulfnic, born in Iceland)
  - Second generation: **Wulfnic Bloodmoon** — first American-born Bloodmoon generation
  - Third generation: **Nixara Bloodmoon** — daughter of Wulfnic Bloodmoon

#### Douglas Dynasty

- **Origin:** England
- **Migration:** Migrated to America during 1700s
- **Generation Structure:**
  - Multiple established generations in America by contemporary era
  - **Erik Douglas** — canonically established member of Douglas Dynasty (separate from Bloodmoon line)

### Genealogical Structure

#### Bloodmoon Dynasty (Pre-Union)

`Iceland Bloodmoons (pre-1930)
    ↓
Wulfnic Bloodmoon (first American-born)
    ↓
Nixara Bloodmoon (daughter of Wulfnic)`

#### Douglas Dynasty (Pre-Union)

`England Douglas line (1700s+)
    ↓
    ↓ (multiple generations)
    ↓
Erik Douglas (contemporary era)`

#### The Dynastic Union

- **Principals:** Erik Douglas + Nixara Bloodmoon
- **Result:** Douglas-Bloodmoon Line (first generation heirs)
- **Surname Authority:** All four children of Erik Douglas + Nixara Bloodmoon union carry the hyphenated **Douglas-Bloodmoon** surname as an exceptional dynastic designation
- **Mandate:** The hyphenated surname is non-negotiable for the four first-generation heirs (Malachia, Noah, Jasper, Alyssa). The surname is NOT automatically hereditary; second-generation inheritance rules are unresolved and pending ADR-003

#### Douglas-Bloodmoon Core Line (First Generation)

All of the following are children of Erik Douglas + Nixara Bloodmoon:

- Malachia Douglas-Bloodmoon
- Noah Douglas-Bloodmoon
- Jasper Douglas-Bloodmoon
- Alyssa Douglas-Bloodmoon

### Legacy Migration Drift Rejection

**EXPLICITLY REJECTED:** The historical archive contains the following genealogical claim:

`Wulfnic Bloodmoon → Erik Douglas (father-son relationship)`

**Status:** ANNULLED FROM CANON

**Classification:** Legacy migration drift—an error introduced during archive consolidation that fundamentally corrupts the dynastic structure.

**Canonical Reality:**

- Erik Douglas bears **NO blood relation** to Wulfnic Bloodmoon
- Wulfnic and Erik are from completely separate dynasties
- The relationship is contemporaneous (union-era), not paternal

**Rationale for Rejection:** Permitting this false relationship would imply an incestuous or conceptually flawed dynastic merge when Erik forms a union with Nixara (Wulfnic's daughter). The entire purpose of a "dynastic union" is to merge two distinct family lines. The false father-son relationship destroys this architectural integrity.

### Genealogy Authority

**This document serves as the absolute canonical genealogy authority for the Los Angeles Dynasty.**

Authority hierarchy:

1. **This ADR-001 decision** (canonical baseline)
2. Character Authority Layer decisions (references family data)
3. Historical archive documentation (read-only reference)

Research archives (NotebookLM, Svartulfr_LA, Progetti) are evidence sources only and hold no authority position.

All contradictions between this ADR and historical sources must be immediately escalated and resolved through the Canon Recovery Workflow.

## Rationale

### Why Distinct Origins Matter

1. **Conceptual Integrity:** A dynastic union must merge two distinct entities. False paternal relationships undermine this fundamental concept.

2. **Genealogical Authenticity:** Bloodmoon (Iceland → America) and Douglas (England → America) follow different migration patterns and timelines. Preserving these distinct origins preserves historical authenticity.

3. **Authority Boundaries:** When Family Authority Layer is implemented, it requires clean root nodes for each dynasty. Merged or incestuous relationships complicate root node definition.

4. **Future Expansion:** When additional dynasties or worlds are reintroduced (archived systems: Cyber, Fantasy, Wasteland), the clean Douglas + Bloodmoon baseline will provide a stable foundation for comparison and differentiation.

### Why the False Relationship Must Be Rejected

The archived claim that "Wulfnic is Erik's father" is inconsistent with:

- The concept of a "dynastic union" (which requires distinct founding families)
- The contemporary era timeline (Wulfnic and Erik as generational peers at union time)
- Nixara's position as bridge between dynasties (daughter of one, partner in union with the other)
- Contemporary academic timeline validation (LA_OnlyHuman_Academic_Timeline)

This false relationship represents legacy migration drift—the accidental corruption of canon during multi-version archive consolidation. It must not propagate into the current repository.

## Consequences

### For Family Authority Layer Implementation

1. **Root Node Definition:** The family_engine.js knowledge layer must treat Bloodmoon and Douglas as entirely separate root nodes
   - Root Node A: Bloodmoon Dynasty (Iceland origin)
   - Root Node B: Douglas Dynasty (England origin)
   - Union Node: Erik + Nixara (merger point creating Douglas-Bloodmoon line)

2. **No Paternal Bridge:** No genealogical path may connect Wulfnic → Erik under any circumstance

3. **Lineage Validation:** All first-generation heirs (Malachia, Noah, Jasper, Alyssa) trace exclusively to the Erik + Nixara union, with no alternative parent claims permitted

### For Canon Recovery Workflow

- Any historical archive data referencing Wulfnic → Erik (father-son) must be immediately classified as legacy drift
- Such data must not be imported into SvartulfrVerse repository without explicit override decision
- All such references must be documented in Canon Recovery audit trail

### For Character Authority Implementation

- Character files for Douglas-Bloodmoon core line members must reference only Erik + Nixara as parents
- No conflicting genealogy may appear in character biography or family reference data
- Character files must enforce the Douglas-Bloodmoon hyphenated surname mandate

## Future Implementation Notes

### Family Authority Layer Structure

When family_engine.js is implemented:

`
FamilyEngine {
rootNodes: {
Bloodmoon: { origin: "Iceland", firstAmerican: "Wulfnic" },
Douglas: { origin: "England", migrationEra: "1700s" }
},

unions: {
DouglasBloodmoon: {
partners: ["Erik Douglas", "Nixara Bloodmoon"],
result: "Douglas-Bloodmoon line",
heirs: ["Malachia", "Noah", "Jasper", "Alyssa"]
}
},

constraints: {
noWulfnicErikRelationship: true,
surnameMandatory: "Douglas-Bloodmoon",
lineageRoot: "union"
}
}
`

### No Implementation Now

- **EXPLICIT RESTRICTION:** No engine logic will be created at this time
- **EXPLICIT RESTRICTION:** No family graph data structures will be created
- **EXPLICIT RESTRICTION:** No relationship computation will be implemented

This ADR establishes authority only. Implementation follows separate ADR and phase planning.

### Character Validation Phase — COMPLETE

ADR-001 established the genealogical foundation. Phase 2 (Character Validation) is **COMPLETE**:

1. ✅ Evidence collected from research archives
2. ✅ All characters verified against ADR authority
3. ✅ Character Audits produced for Malachia, Noah, Jasper, Alyssa
4. ✅ All characters validated against LA_OnlyHuman_Academic_Timeline
5. ✅ Explicit character import decisions documented
6. ✅ All 12 characters integrated into database/ and frozen under Canon Freeze v1

All character work respects the genealogical authority established in ADR-001.

## Authority

- **Established by:** Family Authority & Canon Reconstruction Workspace
- **Approved by:** Runtime Validation
- **Supersedes:** All legacy archive genealogical claims regarding Bloodmoon + Douglas dynasties
- **Basis:** ADR-000 Runtime Baseline + Character Authority Audit + Authority Reconciliation framework

**This ADR represents the canonical ground truth for Los Angeles Dynasty genealogy.**
