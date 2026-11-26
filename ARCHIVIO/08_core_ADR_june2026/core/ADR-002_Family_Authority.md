# ADR-002: Family Authority Layer — Genealogical Authority Architecture

**Status:** ACCEPTED  
**Date:** 2026-06-07  
**Title:** Family Authority Layer Definition and Genealogical Ownership Model

## Context

ADR-000 established the runtime-first baseline and canonical stabilization requirement. ADR-001 formalized the dynastic origins and explicitly rejected legacy genealogical drift (Wulfnic → Erik false paternity). 

Before any family data can be imported or any genealogy engine implemented, the Family Authority Layer must be formally defined. This layer must unambiguously own all genealogical data while remaining strictly knowledge-only (no behavioral computation).

## Decision

We establish the Family Authority Layer as the sole canonical source for all genealogical, kinship, and dynastic data within SvartulfrVerse.

### Scope

- **Only Human** (no supernatural genealogy)
- **Contemporary** (2020s-2030s timeline)
- **Los Angeles Dynasty** (geographic and familial focus)

### Family Authority Layer Definition

**Family Authority Layer is the sole owner and canonical custodian of:**

1. Genealogy — All parent-child descent relationships
2. Kinship — All family relationship structures
3. Lineage — All dynastic lines and inheritance chains
4. Dynastic Ownership — Dynasty membership and succession
5. Surname Authority — Authorized family surnames and naming conventions

**Family Authority Layer constraints:**

- **Knowledge-Only Custodian** — No behavioral computation, no state management, no relationship inference
- **Immutable Records** — Once established, genealogical facts do not change across scenarios
- **Single Source of Truth** — All genealogy flows from Family Authority; no distributed genealogy
- **Authority-Driven** — Decisions governed by explicit ADR, not by archive or NotebookLM inference

### Canonical Ownership Model

#### Character Layer
- **Owns:** Identity (personality, sex, biography, skills, education)
- **References:** Family relationships (read-only queries to Family Authority)
- **Prohibited:** Genealogy definition, surname authority, dynasty ownership

#### World/Experience Layer
- **Owns:** Context (occupation, residence, scenario role, current relationships)
- **References:** Dynasty membership (read-only queries to Family Authority)
- **Prohibited:** Genealogy definition, family structure, inheritance rules

#### Family Authority Layer
- **Owns:** Genealogy, kinship, lineage, dynastic membership, surnames
- **Provides:** Read-only genealogy queries to Character and World layers
- **Prohibited:** Character identity, experience context, behavioral computation

---

## Canonical Relationship Authority

### Explicit Authority Records

The following relationships are explicitly stored as canonical family authority records. Each represents a binding genealogical fact that may be queried but never inferred.

#### Parent

**Definition:** A biological or adoptive parent relationship.

**Canonical Properties:**
- Immutable once established
- Creates biologically-derived relationships (siblings, grandparents, etc.)
- Cannot be inferred; must be explicitly defined
- Single source: Family Authority
- Example: Wulfnic Bloodmoon is the parent of Nixara Bloodmoon

#### Child

**Definition:** A biological or adoptive child relationship (inverse of Parent).

**Canonical Properties:**
- Immutable once established
- Uniquely identifies parent in genealogical graph
- Cannot be inferred; must be explicitly defined
- Single source: Family Authority
- Example: Malachia Douglas-Bloodmoon is a child of Erik Douglas and Nixara Bloodmoon

#### Marriage

**Definition:** A legal or recognized union between two individuals that creates a joint family unit.

**Canonical Properties:**
- Establishes new lineage for children
- Creates in-law relationships
- May be superseded by Former Marriage (see below)
- Single source: Family Authority
- Example: Erik Douglas married Nixara Bloodmoon

#### Former Marriage

**Definition:** A marriage relationship that has ended through divorce, annulment, or death.

**Canonical Properties:**
- Preserves historical marriage record
- Does not create current in-law relationships
- Children from former marriage retain biological connection to both parents
- Single source: Family Authority
- Example: (None currently documented for Los Angeles Dynasty)

#### Adoption

**Definition:** A legal relationship that establishes parent-child connection without biological descent.

**Canonical Properties:**
- Treated equivalently to biological parent-child relationship
- Creates kinship relationships as if biological
- Explicitly marked as adoption in genealogical record
- Single source: Family Authority
- Example: (None currently documented for Los Angeles Dynasty)

#### Half-Sibling

**Definition:** A sibling relationship where only one parent is shared.

**Canonical Properties:**
- Explicitly stored (not derived from two-parent sibling calculation)
- Marks shared-parent status
- Required when genealogy spans multiple partnerships
- Single source: Family Authority
- Example: (None currently documented for Los Angeles Dynasty)

---

### Derived Relationships

The following relationships are **NEVER stored as independent canon**. They are derived algorithmically from explicit authority records. Runtime systems may compute these relationships but must never store them as facts or create independent genealogical authority.

#### Sibling

**Derived from:** Two individuals sharing at least one parent.

**Constraint:** Must be computed from Parent records, never stored as independent fact.

**Example:** Noah Douglas-Bloodmoon and Jasper Douglas-Bloodmoon are siblings (derived from both having Erik and Nixara as parents).

#### Grandparent

**Derived from:** Transitive parent relationship (parent of parent).

**Constraint:** Must be computed from Parent records, never stored.

**Example:** Wulfnic Bloodmoon is grandparent to his son/daughter's children.

#### Grandchild

**Derived from:** Transitive child relationship (child of child).

**Constraint:** Must be computed from Child records, never stored.

#### Uncle / Aunt

**Derived from:** Sibling of parent.

**Constraint:** Must be computed from Parent + Sibling records, never stored.

#### Nephew / Niece

**Derived from:** Child of sibling.

**Constraint:** Must be computed from Child + Sibling records, never stored.

#### Cousin

**Derived from:** Child of parent's sibling.

**Constraint:** Must be computed from multiple Parent + Sibling records, never stored.

#### In-Law

**Derived from:** Spouse of relative.

**Constraint:** Must be computed from Marriage + genealogical path, never stored.

---

## Inference Policy

**EXPLICITLY PROHIBITED:** Runtime inference of new genealogical facts.

### What the Runtime MAY Do

- **Query** Family Authority records
- **Compute** derived relationships from authority records
- **Validate** claimed relationships against authority records
- **Return** read-only genealogy data to Character and World layers
- **Log** relationship queries for audit trail

### What the Runtime MAY NOT Do

- **Infer** genealogy from non-genealogical data
- **Derive** new parent-child relationships from context
- **Assume** family membership based on occupation or residence
- **Create** genealogical facts from behavioral patterns
- **Modify** Family Authority records without explicit Family Authority decision
- **Store** derived relationships as independent facts

### Inference Prevention Example

**Failure Case:** Character file contains occupation "lawyer" and lives in Los Angeles. Runtime attempts to infer relationship to other "lawyer" characters or Los Angeles Dynasty members.

**Prevention:** Runtime has zero permission to create genealogical inference. Relationships exist only in Family Authority. No pattern-based inference permitted.

---

## Dynasty Authority

### Bloodmoon Dynasty

**Origin:** Iceland  
**Migration:** Iceland → North America (post-1930)  
**American Founder:** Wulfnic Bloodmoon (first American-born generation)  
**Current Primary Member:** Nixara Bloodmoon (daughter of Wulfnic)  

**Dynasty Authority Rules:**
- Membership defined by descent from Icelandic Bloodmoon line
- Explicitly tracked in Family Authority
- Cannot be assumed from surname alone
- No fictional genealogy permitted

**Dynasty Status in Los Angeles Dynasty:**
- Represented through Erik-Nixara union
- Creates Douglas-Bloodmoon line (see below)
- Original Bloodmoon line continues as background authority

---

### Douglas Dynasty

**Origin:** England  
**Migration:** England → America (1700s)  
**American Establishment:** Multiple generations established in America by contemporary era  
**Current Primary Member:** Erik Douglas (contemporary era)  

**Dynasty Authority Rules:**
- Membership defined by descent from English Douglas line
- Explicitly tracked in Family Authority
- Cannot be assumed from surname alone
- Separate and complete dynasty (not merged with Bloodmoon until Erik-Nixara union)

**Dynasty Status in Los Angeles Dynasty:**
- Represented through Erik Douglas as founding member of union
- Creates Douglas-Bloodmoon line (see below)
- Original Douglas line continues as background authority

---

### Douglas-Bloodmoon Dynasty

**Origin:** Union of Erik Douglas (Douglas Dynasty) and Nixara Bloodmoon (Bloodmoon Dynasty)  
**Founding Date:** Contemporary era (unspecified in ADR-001)  
**Founding Members:** Erik Douglas, Nixara Bloodmoon  

**Dynasty Authority Rules:**
- **Membership:** Exclusively defined as children of Erik Douglas + Nixara Bloodmoon union
- **Founder Status:** Erik and Nixara are founding members; their parents (Wulfnic, Erik's Douglas ancestors) are background authorities
- **Expansion Rules:** Future descendants inherit Douglas-Bloodmoon membership through biological descent or approved adoption
- **Sovereignty:** Douglas-Bloodmoon is a complete dynasty in its own right, not a subsidiary of Bloodmoon or Douglas
- **Authority:** Family Authority owns all Douglas-Bloodmoon genealogy

**Current Douglas-Bloodmoon Membership:**
- Erik Douglas (founder)
- Nixara Bloodmoon (founder)
- Malachia Douglas-Bloodmoon (child)
- Noah Douglas-Bloodmoon (child)
- Jasper Douglas-Bloodmoon (child)
- Alyssa Douglas-Bloodmoon (child)

---

## Surname Authority

### Douglas (Surname Authority)

**Origin:** English Douglas Dynasty (1700s)  
**Current Authority:** Douglas Dynasty members  
**Los Angeles Dynasty Member:** Erik Douglas  

**Surname Rules:**
- Generic family surname
- Passed through Douglas Dynasty descent
- No mandate for hyphenation or modification
- Multiple Douglas family lines may exist (extended genealogy)
- Variants permitted (Douglass, etc.) where historically documented

**Inheritance Rules:** Standard patrilineal descent (historically); future rules require ADR-003 definition.

---

### Bloodmoon (Surname Authority)

**Origin:** Icelandic Bloodmoon Dynasty  
**Current Authority:** Bloodmoon Dynasty members  
**Los Angeles Dynasty Member:** Nixara Bloodmoon  

**Surname Rules:**
- Generic family surname
- Passed through Bloodmoon Dynasty descent
- No mandate for hyphenation or modification
- Multiple Bloodmoon family lines may exist (extended genealogy)
- Variants permitted where historically documented

**Inheritance Rules:** Standard descent rules (unspecified for contemporary era); future rules require ADR-003 definition.

---

### Douglas-Bloodmoon (Dynastic Surname Authority)

**Origin:** Union of Erik Douglas + Nixara Bloodmoon (ADR-001)  
**Authority:** Explicitly established as dynastic surname  
**Current Authority:** Erik Douglas (founder), Nixara Bloodmoon (founder), and all authorized children  

**Surname Rules:**

1. **Hyphenation Mandatory** — Douglas-Bloodmoon must always be hyphenated; no variations (Douglasbloodmoon, Douglas Bloodmoon, etc.) permitted

2. **Union-Derived Origin** — The hyphenated form originates exclusively from the Erik Douglas + Nixara Bloodmoon union; no other source creates this surname

3. **Exclusive Membership** — Only authorized children of Erik and Nixara may carry Douglas-Bloodmoon surname; no collateral lines

4. **Not Generic** — Douglas-Bloodmoon is NOT a family surname in the traditional sense; it is a dynastic designation marking membership in the union-derived line. It is NOT automatically inherited; it is exclusively reserved for the four union heirs (Malachia, Noah, Jasper, Alyssa) and no other individuals without explicit Family Authority approval

5. **Canonical Authority** — Family Authority owns Douglas-Bloodmoon surname authority; no deviation permitted without explicit ADR approval

6. **Current Mandate** — All four first-generation heirs MUST carry Douglas-Bloodmoon surname:
   - Malachia Douglas-Bloodmoon ✅
   - Noah Douglas-Bloodmoon ✅
   - Jasper Douglas-Bloodmoon ✅
   - Alyssa Douglas-Bloodmoon ✅

**Future Inheritance Rules:** UNRESOLVED

The following inheritance questions remain open and must be resolved through future ADR:

- Do second-generation descendants (children of Malachia/Noah/Jasper/Alyssa) retain Douglas-Bloodmoon?
- If a Douglas-Bloodmoon heir marries outside the dynasty, does their child carry Douglas-Bloodmoon or spouse's surname?
- Are there collateral lines (e.g., siblings of Malachia) who may claim Douglas-Bloodmoon?
- What happens if adoption introduces non-biological children to the union?
- Can maiden names be retained alongside Douglas-Bloodmoon?

**Note:** These rules are intentionally left open. ADR-003 (Inheritance and Succession) will address them explicitly.

---

## Historical Runtime Failures

The following historical runtime failures have been identified in the legacy archive. Lessons learned inform the Family Authority Layer design.

### Failure: Valerius

**Affected Component:** Character layer  
**Root Cause:** Authority conflict (character file vs. genealogy mismatch)  
**Symptoms:** Unknown genealogical status; unclear family relationships  
**Lesson Learned:** Character files must reference genealogy, never define it. Family Authority must be single source of truth.

### Failure: Cassia

**Affected Component:** Character layer  
**Root Cause:** Authority conflict (multiple genealogical claims)  
**Symptoms:** Conflicting parent relationships across archive versions  
**Lesson Learned:** Genealogy must be explicitly declared in Family Authority, not inferred from character context or behavior.

### Failure: Hati

**Affected Component:** World/Experience layer  
**Root Cause:** Inference failure (derived relationships stored as canon)  
**Symptoms:** Incorrect kinship claims; relationship computation errors  
**Lesson Learned:** Derived relationships must never be stored as independent facts. Compute from authority records only.

### Failure: Sköll

**Affected Component:** Dynasty layer  
**Root Cause:** Missing data (incomplete genealogy)  
**Symptoms:** Dynasty membership unclear; inheritance rules ambiguous  
**Lesson Learned:** Explicit authority records required. Absence of data means absence of relationship; no assumptions permitted.

---

## Consequences

### Benefits

1. **Single Source of Truth** — All genealogy flows from Family Authority; no distributed genealogical claims

2. **Authority Clarity** — Clear ownership boundaries prevent character files from becoming genealogy databases

3. **Runtime Safety** — No inference permitted; relationships must be explicitly declared

4. **Legacy Drift Prevention** — ADR-001 legacy drift (Wulfnic → Erik) cannot recur; all genealogy requires explicit authority

5. **Future Scalability** — Authority framework scales to extended genealogy without architectural change

6. **Audit Trail** — Every genealogical decision traceable to Family Authority source

### Risks

1. **Genealogy Gaps** — If Family Authority data is incomplete, runtime cannot infer missing relationships; this is intentional, but creates discovery gaps

2. **Implementation Complexity** — Family Authority implementation requires explicit parent-child record creation; cannot import genealogy from archive without audit

3. **Character Birth Dependency** — Characters cannot be fully understood without querying Family Authority; this adds query burden to character layer

4. **Surname Authority Gaps** — Douglas-Bloodmoon inheritance rules remain undefined; future ADR required before multi-generational expansion

5. **Adoption Edge Cases** — Adoption relationships must be explicitly marked; system cannot distinguish adopted vs. biological without explicit data

### Future Work

1. **ADR-003: Inheritance and Succession** — Define how Douglas-Bloodmoon surname transfers to second generation; establish general inheritance rules

2. **ADR-004: Extended Genealogy** — Define treatment of collateral lines, extended family, and background dynasties

3. **ADR-005: Character-Genealogy Integration** — Define character query interface for genealogy; establish reference patterns

4. **Family Engine Implementation** — Once all ADRs complete, implement family_engine.js knowledge layer

5. **Genealogy Data Migration** — Once Family Engine ready, migrate validated genealogy from archive to repository

6. **Character Import** — After Family Authority complete, begin character validation and import phase

### Open Questions

1. **Extended Genealogy** — What is the complete genealogy of Iceland Bloodmoons prior to Wulfnic? When does history matter?

2. **Douglas Collateral Lines** — Does Erik have siblings? What genealogy applies to extended Douglas family?

3. **Adoption Rules** — Are adoptions treated identically to biological relationships? Any special marking required?

4. **Marriage Timeline** — When did Erik and Nixara marry? Does marriage date affect inheritance rules?

5. **Relationship Precedence** — If genealogical data conflicts with character documentation, which has authority? (Answer: Family Authority, but needs explicit rule)

6. **Background Dynasties** — Do Bloodmoon and Douglas dynasties continue as background authorities, or are they fully merged into Douglas-Bloodmoon?

7. **Naming Conventions** — Are there other dynastic surnames? How are they distinguished from regular family surnames?

8. **Supernatural Genealogy** — If supernatural systems are reintroduced, does Family Authority expand to handle paranormal genealogy? (Answer: Requires separate ADR)

---

## Explicitly Prohibited Actions

**The following actions are strictly prohibited in the context of Family Authority Layer:**

### 1. Modification of family_engine.js

- Do not implement logic in family_engine.js
- Do not create genealogy data structures
- Do not populate family relationships
- This ADR is architecture-only; implementation is future work

### 2. Creation of Genealogy Data

- Do not import genealogy from archive without ADR audit
- Do not create family graphs in code
- Do not populate family_engine.js with relationship data
- Do not create character files with embedded genealogy

### 3. Creation of Family Graph Entries

- Do not create graph data structures
- Do not implement relationship computation
- Do not create index structures for genealogy
- Architecture documented; implementation deferred

### 4. Character File Creation

- Do not create character files until Character Authority ADR approved
- Do not embed genealogy in character files
- Do not assume character properties from family relationships
- Family Authority must precede character imports

### 5. World File Creation

- Do not create world files that define genealogy
- Do not assume dynasty membership from world context
- Do not create scenario-based family relationships
- Family Authority is single source of truth

### 6. Introduction of Runtime Logic

- Do not implement relationship inference
- Do not create genealogy computation algorithms
- Do not derive new family relationships from behavior
- Do not compute dynasty membership from other properties
- Knowledge-only; no behavioral computation

---

## Implementation Prerequisites

Before any Family Authority Layer code is written:

1. ✅ ADR-000: Runtime Baseline (COMPLETE)
2. ✅ ADR-001: Dynastic Origins (COMPLETE)
3. ✅ ADR-002: Family Authority (THIS DOCUMENT)
4. ⏳ ADR-003: Inheritance and Succession (REQUIRED)
5. ⏳ ADR-004: Extended Genealogy (REQUIRED)
6. ⏳ ADR-005: Character-Genealogy Integration (REQUIRED)
7. ⏳ Family Engine Schema Definition (REQUIRED)
8. ⏳ Genealogy Migration Plan (REQUIRED)

Implementation cannot proceed until all prerequisite ADRs are approved.

---

## Authority

- **Established by:** Family Authority & Canon Reconstruction Workspace
- **Approved by:** Runtime Validation
- **Supersedes:** All legacy genealogy practices in Progetti archive
- **Basis:** ADR-000 + ADR-001 + Authority Framework
- **Scope:** Los Angeles Dynasty baseline (Only Human, Contemporary)

**This ADR represents the canonical family authority governance model for SvartulfrVerse.**
