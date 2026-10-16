# DECISION_REGISTRY

**Version:** 1.0  
**Date:** 2026-06-08  
**Purpose:** Condensed architecture reference for rapid consultation by future chats.

---

## ADR-000: Runtime Baseline

**Decision:** Progetti archive becomes read-only Historical Archive. SvartulfrVerse becomes Active Runtime Repository. Canon Recovery Workflow established.

**Rationale:** Runtime preservation prevents behavior loss. Single source of truth reduces contradictions. Contemporary + Only Human scope enables deep canonical stability.

**Key Constraints:**
- No legacy content imported until validated
- No runtime logic in repository
- No unaudited character definitions
- No world systems without architecture approval
- No supernatural systems without scope expansion approval

**Implications:** All phases require explicit canon decisions before implementation. Canon Freeze v1 is ACTIVE.

---

## ADR-001: Dynastic Origins

**Decision:** Bloodmoon Dynasty originates from Iceland (post-1930 migration). Douglas Dynasty originates from England (1700s migration). Erik Douglas + Nixara Bloodmoon are union principals. All four children carry hyphenated "Douglas-Bloodmoon" surname.

**Rationale:** Distinct origins preserve conceptual integrity of dynastic union. False paternal relationships (Wulfnic → Erik) are legacy drift and must be rejected.

**Key Constraints:**
- Wulfnic Bloodmoon is NOT the father of Erik Douglas
- Hyphenated surname is mandatory for first-generation heirs
- No surname variations permitted
- Union principals: exactly Erik Douglas + Nixara Bloodmoon

**Implications:** Family engine must treat Bloodmoon and Douglas as separate root nodes. No genealogical path may connect Wulfnic to Erik.

---

## ADR-002: Family Authority

**Decision:** Family Authority Layer is sole owner of all genealogical, kinship, and dynastic data. Knowledge-only layer (no behavioral computation). Explicit relationships stored; derived relationships computed at runtime.

**Rationale:** Single source of truth for genealogy prevents drift. Knowledge-only constraint prevents behavioral logic from corrupting family data.

**Key Constraints:**
- Only explicit parent-child and marriage relationships are stored
- Siblings, grandparents, cousins are derived (computed, not stored)
- Family Authority contains NO behavioral logic
- Genealogy must enter `database/families/` before appearing anywhere else

**Implications:** Character files reference genealogy (read-only). No character file may define parent-child relationships.

---

## ADR-003: Character Authority

**Decision:** Character Authority Layer is sole owner of identity, personality, biography, skills, education, and baseline occupation. Cross-authority ownership is explicitly prohibited.

**Rationale:** Clear ownership boundaries prevent character files from becoming genealogy databases or scenario stores. Identity is immutable core.

**Key Constraints:**
- Character files must NOT contain genealogy
- Character files must NOT contain scenario-specific data
- Character files must NOT contain appearance baseline
- Identity is immutable; biography and skills are append-only
- Baseline occupation owned by Character; Experience may override per scenario

**Implications:** Character imports require genealogy to be validated first. Character files reference Family, Visual, and Experience authorities.

---

## ADR-004: Visual Authority

**Decision:** Visual Authority Layer is sole owner of appearance, aesthetic, and visual inheritance data. Visual inheritance is independent from genealogical inheritance. Visual Fusion Model governs Douglas-Bloodmoon children.

**Rationale:** Visual inheritance ≠ genealogical inheritance. Separating these domains prevents conflation of appearance with family structure.

**Key Constraints:**
- Douglas baseline: black hair, amber eyes, massive build
- Bloodmoon baseline: blonde hair, blue eyes, lean build
- Visual Fusion Model (not dominant/recessive genetics)
- Visual Authority is independent from Family Authority
- Character files must NOT define appearance baseline

**Implications:** Visual data enters `database/worlds/` first. Character files reference Visual Authority for appearance.

---

## ADR-005: Experience Authority

**Decision:** Experience Authority Layer is a consumer (not owner) of canonical data. Owns scenario framing, context state, role assignments, occupation overrides, and relationship extensions.

**Rationale:** Scenarios consume canonical data but must never create new canon. Consumer role prevents scenario drift from corrupting authority layers.

**Key Constraints:**
- Experience Layer is ALWAYS a consumer, never an authority source
- May override occupation for scenario scope only
- May extend relationships but cannot remove core relationships
- Cannot redefine identity, genealogy, or appearance
- Current residence and employment are scenario-scoped, never stored as canon

**Implications:** Experience definitions require separate validation. Scenario data must not be imported as canonical.

---

## ADR-006: Canon Layer Architecture

**Decision:** Five-layer Canon Architecture: Active, Historical, Cultural, Deferred, Candidate. Each layer has explicit governance rules. Cultural Canon is never factual. Rejected canon cannot re-enter.

**Rationale:** Layer classification prevents contamination between fact, history, and myth. Explicit rules prevent drift and ensure runtime systems distinguish between truth and flavor.

**Key Constraints:**
- **Active Canon:** Runtime-eligible, full ADR compliance required
- **Historical Canon:** Documented facts, reference only
- **Cultural Canon:** Family traditions/myths, dialogue flavor only, NEVER factual
- **Deferred Canon:** Valid but not active, requires activation process
- **Candidate Canon:** Proposed, requires full review
- **Rejected Canon:** Cannot be reintroduced (14 entities rejected)
- Cultural → Active promotion is PROHIBITED

**Implications:** All canon classification must reference ADR-006. Runtime queries must respect layer boundaries. Lorebooks must tag all entries with canon layer.

---

## AUTHORITY HIERARCHY (Conflict Resolution)

```
1. ADRs (Architectural Decision Records) — HIGHEST
2. Authority Records (database/ canonical data)
3. Imported Canon (approved through workflow)
4. Experience Content (consumer data)
5. Historical Archive (evidence source only) — LOWEST
```

**Rule:** When sources conflict, higher authority wins. ADRs supersede all other sources.

---

## CANON FREEZE v1 — KEY RULES

1. No new canon creation without Authority Decision
2. No lore expansion without Authority Decision
3. No recovery workflow for rejected canon
4. No direct archive imports
5. No supernatural system introduction
6. Bug fixes to existing records are allowed
7. Documentation maintenance is allowed
8. Canon Recovery Workflow for new candidates is allowed (with full audit)

---

*This registry summarizes ADR-000 through ADR-006. For full details, consult the ADR files in `core/`.*
