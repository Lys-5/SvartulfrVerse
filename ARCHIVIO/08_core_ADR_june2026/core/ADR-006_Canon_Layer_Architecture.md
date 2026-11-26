# ADR-006: Canon Layer Architecture

**Status:** ACCEPTED  
**Date:** 2026-06-07  
**Title:** Canon Layer Classification and Cross-Layer Governance

## Context

ADR-000 through ADR-005 established the authority layer architecture for SvartúlfrVerse. The Program Status Report identified that the repository now operates with multiple canon categories:

- Active Canon (runtime-eligible)
- Historical Material (documented facts)
- Deferred Canon (valid but not runtime-active)
- Canon Candidates (proposed but not approved)

These categories exist de facto but lack formal definition de jure. Without explicit layer classification, character reviews risk using categories that exist in practice but not in governance.

Furthermore, the Canon Layer Architecture Report proposed a three-tier structure (Active/Historical/Cultural) that requires formal adoption.

## Decision

We establish a five-layer Canon Architecture with explicit governance rules for each layer.

### Canon Layer Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│  CANON LAYER ARCHITECTURE                                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  ACTIVE CANON                                                │   │
│  │  Runtime-eligible, governance-enforced                        │   │
│  │  Authority: Full ADR compliance required                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              ↑                                      │
│                              │ Promotion                            │
│                              │                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  HISTORICAL CANON                                            │   │
│  │  Documented facts, verifiable records                        │   │
│  │  Authority: Documentation required                           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              ↑                                      │
│                              │ Classification                       │
│                              │                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  CULTURAL CANON                                              │   │
│  │  Family traditions, oral history, myths                     │   │
│  │  Authority: Preservation focus, not runtime truth           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              ↑                                      │
│                              │ Acknowledgment                       │
│                              │                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  DEFERRED CANON                                              │   │
│  │  Valid entities, not currently active                        │   │
│  │  Authority: Future expansion candidates                      │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              ↑                                      │
│                              │ Proposal                             │
│                              │                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  CANDIDATE CANON                                             │   │
│  │  Proposed material, not yet approved                         │   │
│  │  Authority: Requires full review process                     │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Layer Definitions

### Layer 1: Active Canon

**Definition:** Information currently eligible for runtime compilation.

**Properties:**

| Property | Status |
|----------|--------|
| Runtime-eligible | ✓ Yes |
| Governance-enforced | ✓ Yes |
| ADR compliance | ✓ Required |
| Modification | Requires Authority Decision |

**Authority:** Full ADR governance (ADR-000 through ADR-005).

**Current Contents:**

| Category | Elements |
|----------|----------|
| Dynasties | Bloodmoon, Douglas, Douglas-Bloodmoon |
| Characters | Wulfnic, Nixara, Erik, Malachia, Noah, Jasper, Alyssa |
| Visual Canon | Fusion Model, Baselines, Inheritance Rules |
| Timeline | 1930s migration through 2024 |
| Institutions | Seven Hills, DCC, UCLA |

**Constraints:**

```
Active Canon MUST:
  - Comply with all ADRs
  - Remain human-only
  - Stay within contemporary timeline
  - Follow authority layer boundaries

Active Canon MUST NOT:
  - Include supernatural elements as facts
  - Accept Cultural Canon as runtime truth
  - Bypass governance for modification
```

---

### Layer 2: Historical Canon

**Definition:** Documented historical facts about the dynasties.

**Properties:**

| Property | Status |
|----------|--------|
| Runtime-eligible | ✓ Reference only |
| Documentation | ✓ Required |
| Verifiable | ✓ Preferred |
| Modification | Requires evidence |

**Authority:** Historical documentation with ADR-001 oversight.

**Current Contents:**

| Element | Status | Evidence |
|---------|--------|----------|
| English origin (Douglas) | ACCEPTED | ADR-001 |
| Icelandic origin (Bloodmoon) | ACCEPTED | ADR-001 |
| Colonial expansion | ACCEPTED | Recovery Audit |
| Seven Hills Estate | ACCEPTED | Architecture Baseline |
| Merchant tradition | ACCEPTED | Recovery Audit |
| DCC evolution | ACCEPTED | Recovery Audit |
| Edric Ættfaðir Svartúlfa (725 AD) | ACCEPTED | Authority Decision 2026-06-08 |
| 1666 Foundation — Merchant House Douglas (Founder: Lord Cornelius Vance Douglas) | ACCEPTED | Authority Decision 2026-06-08 |
| Douglas Colonial Trading Company (1700s) | ACCEPTED | Authority Decision 2026-06-08 |
| Douglas California Establishment (tradition) | ACCEPTED | Authority Decision 2026-06-08 |

**Constraints:**

```
Historical Canon MUST:
  - Be documented or documentable
  - Remain human-only
  - Connect to Active Canon through lineage
  - Provide verifiable evidence

Historical Canon MUST NOT:
  - Include mythological elements as facts
  - Contradict Active Canon
  - Require supernatural explanation
```

---

### Layer 3: Cultural Canon

**Definition:** Family stories, oral traditions, myths, and legends preserved within lineage.

**Properties:**

| Property | Status |
|----------|--------|
| Runtime-eligible | ✗ No (reference only) |
| Documentation | Oral tradition |
| Verifiable | ✗ Not required |
| Modification | Append-only |

**Authority:** Preservation-focused, not runtime truth.

**Current Contents:**

| Element | Classification | Notes |
|---------|----------------|-------|
| Svartúlfr (Black Wolf) | CULTURAL | Ancestral clan identity |
| Fenrir | CULTURAL | Mythological reference |
| Werewolves | CULTURAL | Family legend |
| Trolls | CULTURAL | Folklore element |
| Draugr | CULTURAL | Undead myth |
| Seiðr | CULTURAL | Magic tradition |
| Jötnar | CULTURAL | Giant myths |
| Moon spirits | CULTURAL | Spiritual element |
| Alpha hierarchy | CULTURAL | Storytelling metaphor |

**Critical Distinction:**

```
Cultural Canon IS:
  - Stories the Bloodmoon family tells
  - Part of family identity and heritage
  - Preserved through oral tradition
  - Valid as cultural expression

Cultural Canon IS NOT:
  - Runtime facts
  - Supernatural truth
  - Active Canon elements
  - Required belief
```

**Usage in Active Canon:**

Cultural Canon may be referenced in:
- Character dialogue (family stories)
- Background flavor (Icelandic heritage)
- Wulfnic's custodial role (memory keeper)

Cultural Canon must NOT be compiled as:
- Runtime facts
- Character abilities
- World mechanics

---

### Layer 4: Deferred Canon

**Definition:** Canonically valid entities not currently active in runtime.

**Properties:**

| Property | Status |
|----------|--------|
| Exists historically | ✓ Yes |
| Recovery audits | ✓ Allowed |
| Runtime participation | ✗ Prohibited |
| Future expansion | ✓ Candidate |

**Authority:** Deferred Canon Policy governance.

**Current Contents:**

#### Rejected Canon — Political Wives

| Name | Status | Notes |
|------|--------|-------|
| Sigrid | **REJECTED** | Political wife concept — incompatible with canonical family structure. No evidence in Active or Historical Canon. |
| Dagmar | **REJECTED** | Political wife concept — incompatible with canonical family structure. No evidence in Active or Historical Canon. |
| Valeria | **REJECTED** | WetNurse/Concubine concept — conflicts with canonical family graph; introduces non-canonical character and "Myrick" name for Jasper. Source: Progetti/docs/canon/CANON_003. Decision: 2026-06-08. |

#### Rejected Canon — Extended Lines

| Name | Status | Notes |
|------|--------|-------|
| Gunnar | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Ingrid | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Astrid II | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Torvald | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Hagen | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Sigrun | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Bram | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Knut | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Lars | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Sven | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Valerius | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |
| Thyra | **REJECTED** | Extended line concept — incompatible with canonical layer architecture. No Active Canon evidence. |

**Total Deferred:** 0 entities
**Total Rejected:** 14 entities (formerly listed as Deferred)

**Activation Process:**

Deferred Canon may move to Active Canon only after:

```
Step 1: Recovery Audit
    ↓
Step 2: Architecture Review
    ↓
Step 3: Runtime Justification
    ↓
Step 4: Authority Decision
```

---

### Layer 5: Candidate Canon

**Definition:** Proposed material not yet approved for any active layer.

**Properties:**

| Property | Status |
|----------|--------|
| Proposed | ✓ Yes |
| Approved | ✗ No |
| Review required | ✓ Yes |
| Authority Decision | ✓ Required |

**Authority:** Full review process mandatory.

**Current Contents:**

| Element | Status | Notes |
|---------|--------|-------|
| 1666 Foundation Year | HISTORICAL CANON | Authority Decision 2026-06-08 |
| Regency Era Layer | CANDIDATE | Requires historical audit |
| Colonial Timeline Details | CANDIDATE | Requires historical audit |
| Early Douglas Genealogy | CANDIDATE | Requires historical audit |
| Vanguard PMC | **REJECTED** | Replaced by DCC Security — BlackWolf Division. See I_DCC_Security_BlackWolf.md |
| DCC Security — BlackWolf | ACTIVE CANON | See I_DCC_Security_BlackWolf.md |

**Promotion Process:**

Candidate Canon must complete full review before classification to any other layer.

---

## Cross-Layer Governance

### Layer Authority Matrix

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LAYER AUTHORITY MATRIX                           │
├─────────────────┬──────────────┬─────────────┬──────────────────────┤
│ Layer           │ Authority    │ Modification│ Runtime Access      │
├─────────────────┼──────────────┼─────────────┼──────────────────────┤
│ Active Canon    │ Full ADR     │ Decision    │ Full compilation     │
│ Historical      │ ADR-001      │ Evidence    │ Reference only       │
│ Cultural        │ Preservation │ Append-only │ Dialogue flavor       │
│ Deferred        │ DCP          │ Activation  │ Prohibited           │
│ Candidate       │ Review       │ Approval    │ Prohibited           │
└─────────────────┴──────────────┴─────────────┴──────────────────────┘
```

### Promotion Rules

| From | To | Process |
|------|-----|---------|
| Candidate | Any | Full review + Authority Decision |
| Deferred | Active | Recovery + Review + Justification + Decision |
| Historical | Active | Documentation + Authority Decision |
| Cultural | Active | PROHIBITED (Cultural is never factual) |

### Retrocession Rules

| From | To | Process |
|------|-----|---------|
| Active | Deferred | Authority Decision (runtime removal) |
| Active | Historical | Authority Decision (deprecation) |
| Historical | Deferred | Evidence of invalidity |

### Consultation Rules

| Query Type | Allowed Sources |
|------------|-----------------|
| Runtime compilation | Active Canon only |
| Character background | Active + Historical + Cultural (flavor) |
| Genealogy verification | Active + Historical |
| Family traditions | Cultural Canon |
| Future expansion | Deferred + Candidate |

### Conflict Resolution

**When layers conflict:**

| Conflict | Resolution |
|----------|------------|
| Active vs Historical | Active Canon prevails |
| Active vs Cultural | Active Canon prevails (Cultural is not factual) |
| Historical vs Cultural | Historical prevails (documentation over story) |
| Deferred vs Active | Active prevails (Deferred is not active) |

---

## Dynasty Duality Integration

### Douglas Dynasty

**Primary Layer:** Historical Canon

```
Douglas (Documentary):
  - Land deeds
  - Corporate records
  - Legal contracts
  - Institutional history
  - Verifiable facts
```

### Bloodmoon Dynasty

**Primary Layer:** Cultural Canon

```
Bloodmoon (Narrative):
  - Family sagas
  - Oral traditions
  - Ancestral myths
  - Cultural identity
  - Preserved stories
```

### Union Integration

```
Douglas-Bloodmoon heirs inherit:
  - Material power (Douglas → Historical)
  - Cultural heritage (Bloodmoon → Cultural)
  - Active status (Union → Active Canon)
```

---

## Consequences

### For Character Reviews

All character reviews must now explicitly classify findings:

```
Character Review Template:
  - Active Canon findings
  - Historical Canon findings
  - Cultural Canon references
  - Deferred Canon connections
  - Candidate Canon proposals
```

### For Runtime Implementation

Runtime queries must respect layer boundaries:

```javascript
// VALID: Query Active Canon for compilation
runtime.compile(character.fromActiveCanon());

// VALID: Reference Historical Canon for background
character.addBackground(historicalCanon.get("Douglas origin"));

// INVALID: Compile Cultural Canon as fact
runtime.compile(culturalCanon.get("Werewolves")); // REJECTED

// VALID: Use Cultural Canon for dialogue flavor
character.addDialogueFlavor(culturalCanon.get("Svartúlfr"));
```

### For Governance

- ADR-006 becomes the authoritative reference for canon classification
- All future ADRs must specify which layer they affect
- Layer transitions require explicit Authority Decisions

---

## Authority

Established by: Architecture Review & Canon Reconstruction Workspace  
Approved by: Runtime Validation  
Supersedes: Ad-hoc canon classification practices  
Depends on: ADR-000, ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, Deferred Canon Policy

**This ADR represents the definitive canon layer architecture for SvartúlfrVerse.**
