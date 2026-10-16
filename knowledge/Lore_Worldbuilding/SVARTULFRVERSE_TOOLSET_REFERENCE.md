# SVARTÚLFRVERSE TOOLSET REFERENCE

**Version:** 1.0  
**Date:** 2026-06-08  
**Status:** Canon Freeze v1 — ACTIVE  
**Purpose:** Prompt-writing reference for all future project chats.

---

## 1. EXECUTIVE SUMMARY

The SvartúlfrVerse project operates a governed repository with three tooling layers:

| Layer | Location | Purpose |
|-------|----------|---------|
| **Rules** | `.trae/rules/R-000` → `R-009` | Operational constraints. Always active. Define what is allowed/prohibited per domain. |
| **Skills** | `.trae/skills/*/SKILL.md` | Audit and review workflows. Invoked on demand. Read-only by default. |
| **Commands** | `.trae/commands/*.md` | Shortcut entry points. Each command delegates to one or more skills. |

**Core Principle:** Rules define governance. Skills define workflows. Commands are convenience entry points. Future prompts should reference these assets instead of rewriting workflow instructions.

**Governance Authority:** ADR-000 through ADR-006 define the canonical architecture. ADR-006 (Canon Layer Architecture) is the authoritative reference for all canon classification decisions.

---

## 2. RULES REFERENCE

### 2.1 Rules by Governance Domain

#### Domain: Runtime & Baseline Governance

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-000** | Runtime Rules | Establishes runtime behavior as ground truth; enforces Canon Freeze v1, evidence-based decisions, Single Source of Truth | ADR-000 | Architecture decisions, migration validation, runtime behavior analysis, canon authority determination |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-000-RUN-001 | Runtime First Principle — Observable runtime behavior is ground truth |
| R-000-RUN-002 | Evidence Before Assumption — No canon without documented evidence |
| R-000-RUN-003 | Canon Freeze Compliance — Canon Freeze v1 is ACTIVE |
| R-000-RUN-004 | Single Source of Truth — One canonical owner per data domain |
| R-000-RUN-005 | No Migration Without Audit — All imports must pass audit workflow |
| R-000-RUN-006 | Correctness Before Optimization — Stability before expansion |
| R-000-RUN-007 | Archive First — Query historical sources before canonical decisions |

---

#### Domain: Dynastic & Lineage Governance

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-001** | Dynastic Rules | Defines dynasty origins, migration timelines, surname mandates, union principals, and prohibited relationships | ADR-001 | Dynasty discussions, bloodline validation, surname enforcement, Douglas/Bloodmoon relationship management |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-001-DYN-001 | Bloodmoon Dynasty Origin — Iceland (not Norway) |
| R-001-DYN-002 | Bloodmoon Migration Timeline — Post-1930 to North America |
| R-001-DYN-003 | Douglas Dynasty Origin — England, 1700s migration |
| R-001-DYN-004 | Dynasty Distinction — No pre-union genealogical connection |
| R-001-DYN-005 | Hyphenated Surname Mandate — "Douglas-Bloodmoon" required |
| R-001-DYN-006 | Prohibited Surname Drift — No variations permitted |
| R-001-DYN-007 | Wulfnic-Erik Relationship Rejection — NOT father-son |
| R-001-DYN-008 | Union Principals — Erik Douglas + Nixara Bloodmoon only |

---

#### Domain: Family & Genealogy Governance

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-002** | Family Rules | Establishes Family Authority as sole genealogy owner; defines explicit vs derived relationships, graph structure, surname authority | ADR-002 | Family relationship creation/modification, genealogy audits, parent-child structures, marriage records |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-002-FAM-001 | Genealogy Ownership — Family Authority owns all genealogy |
| R-002-FAM-002 | Explicit Relationships — Only parent-child and marriage stored |
| R-002-FAM-003 | Derived Relationships — Siblings/grandparents computed at runtime |
| R-002-FAM-004 | Knowledge Layer Only — No behavioral logic in Family Authority |
| R-002-FAM-005 | No Genealogy Duplication — Single storage location |
| R-002-FAM-006 | Family Graph Structure — Directed graph with explicit edges |
| R-002-FAM-007 | Dynasty Membership — Defined by Family Authority |
| R-002-FAM-008 | Surname Authority — Surname rules owned by Family Authority |

---

#### Domain: Character & Identity Governance

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-003** | Character Rules | Establishes Character Authority as owner of identity, personality, biography, skills; prohibits genealogy/scenario data in character files | ADR-003 | Character creation/import/audit, identity validation, biography management, skill definitions |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-003-CHR-001 | Identity Ownership — Name, pronouns, self-conception owned by Character Authority |
| R-003-CHR-002 | Personality Ownership — Behavioral baseline owned by Character Authority |
| R-003-CHR-003 | Biography Ownership — Append-only semantics |
| R-003-CHR-004 | Physical Sex Ownership — Immutable biological baseline |
| R-003-CHR-005 | Skills Ownership — Append-only semantics |
| R-003-CHR-006 | Baseline Occupation Ownership — Character owns baseline, Experience overrides per scenario |
| R-003-CHR-007 | No Genealogy in Character Files — Reference only |
| R-003-CHR-008 | No Scenario Data in Character Files — Identity only |
| R-003-CHR-009 | Cross-Authority Prohibition — Cannot define other authorities' data |
| R-003-CHR-010 | Core Relationships Baseline — Character owns core, Experience extends |

---

#### Domain: Visual & Appearance Governance

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-004** | Visual Rules | Defines Visual Authority as owner of appearance data; establishes Douglas/Bloodmoon visual baselines and Visual Fusion Model for inheritance | ADR-004 | Appearance design, visual inheritance validation, character design audits, Douglas-Bloodmoon visual fusion |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-004-VIS-001 | Douglas Visual Baseline — Black hair, amber eyes, massive build |
| R-004-VIS-002 | Bloodmoon Visual Baseline — Blonde hair, blue eyes, lean build |
| R-004-VIS-003 | Visual Fusion Model — Not dominant/recessive genetics |
| R-004-VIS-004 | Malachia Visual Inheritance — Douglas-dominant |
| R-004-VIS-005 | Noah Visual Inheritance — Bloodmoon-dominant |
| R-004-VIS-006 | Alyssa Visual Inheritance — Fusion with maternal resemblance |
| R-004-VIS-007 | Jasper Visual Inheritance — Fusion (twin of Alyssa) |
| R-004-VIS-008 | Visual Authority Independence — Separate from Family Authority |
| R-004-VIS-009 | Appearance Ownership — Visual Authority owns all appearance |
| R-004-VIS-010 | No Appearance in Character Files — Reference only |

---

#### Domain: Experience & Scenario Governance

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-005** | Experience Rules | Establishes Experience Authority as consumer (not owner) of canon; defines scenario ownership, occupation override, relationship extension rules | ADR-005 | Scenario creation, experience-layer content, occupation overrides, relationship extensions |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-005-EXP-001 | Experience Authority Role — Consumer, not owner |
| R-005-EXP-002 | Scenario Ownership — Location, time, circumstances |
| R-005-EXP-003 | Occupation Override — Scenario scope only |
| R-005-EXP-004 | Relationship Extension — Cannot remove core |
| R-005-EXP-005 | No Identity Redefinition — Identity is Character Authority domain |
| R-005-EXP-006 | No Genealogy Redefinition — Genealogy is Family Authority domain |
| R-005-EXP-007 | No Appearance Redefinition — Appearance is Visual Authority domain |
| R-005-EXP-008 | Consumer Layer Status — Never an authority source |
| R-005-EXP-009 | Current Residence Scope — Scenario-scoped only |
| R-005-EXP-010 | Employment Context Scope — Scenario-scoped only |

---

#### Domain: Repository & Canon Governance

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-006** | Governance Rules | Defines Canon Recovery Workflow, authority hierarchy, audit trail requirements, naming conventions, repository structure authority, rejected canon enforcement | ADR-006, Repository_Governance | Repository governance, canon validation, recovery audits, architecture reviews, workflow enforcement |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-006-GOV-001 | Canon Recovery Workflow — 5-step mandatory process |
| R-006-GOV-002 | Authority Hierarchy — ADRs > Authority Records > Imported Canon > Experience > Archive |
| R-006-GOV-003 | No Bypass — Workflow is mandatory, no exceptions |
| R-006-GOV-004 | Evidence ≠ Canon — Archive evidence requires classification |
| R-006-GOV-005 | Single Source of Truth — One authority per domain |
| R-006-GOV-006 | Preserve Historical Evidence — Progetti archive is read-only |
| R-006-GOV-007 | Audit Trail Required — All imports must reference reports |
| R-006-GOV-008 | Rejection is Valid — REJECTED/DEFERRED are valid outcomes |
| R-006-GOV-009 | Character Recovery Rule — Full audit before import |
| R-006-GOV-010 | Import Destinations — Correct authority layer per data type |
| R-006-GOV-011 | No Direct Archive Imports — Prohibited without audit |
| R-006-GOV-012 | Family Authority Before Expansion — Foundation first |
| R-006-GOV-013 | Rejected Canon Enforcement — No reintroduction of rejected material |
| R-006-GOV-014 | Naming Convention Standard — Mandatory file prefixes |
| R-006-GOV-015 | Repository Structure Authority — Structure is immutable without review |

---

#### Domain: Engine & Runtime Systems

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-007** | Engine Rules | Governs engine development; establishes canon authority over runtime, separation of concerns, traceability, and validation pipeline requirements | ADR-000, Architecture | Engine development, runtime logic, query layers, state management, validation pipeline |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-007-ENG-001 | Canon Authority — Runtime cannot override canon |
| R-007-ENG-002 | Runtime Separation — Engine logic and canon data are separate |
| R-007-ENG-003 | Traceability — All engine output traceable to canonical records |
| R-007-ENG-004 | Validation Pipeline — Generated assets require validation before release |
| R-007-ENG-005 | Validation Pipeline Execution — 47-check pipeline mandatory |
| R-007-ENG-006 | Validation Coverage Requirement — All 4 categories required |

---

#### Domain: Bot Generation

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-008** | Bot Rules | Governs character card and bot configuration generation; enforces canon-derived generation, no manual lore injection, traceability, canon layer compliance | ADR-003, ADR-006 | Bot character card generation, platform exports (JanitorAI, SillyTavern), personality definitions |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-008-BOT-001 | Canon-Derived Generation — Cards from repository canon only |
| R-008-BOT-002 | No Manual Lore Injection — No unvalidated content |
| R-008-BOT-003 | Content Traceability — All content traceable to database/ |
| R-008-BOT-004 | Canon Layer Compliance — Respect layer boundaries |

---

#### Domain: Lorebook Generation

| Rule ID | Name | Purpose | Authority | Typical Use |
|---------|------|---------|-----------|-------------|
| **R-009** | Lorebook Rules | Governs lorebook and world knowledge base generation; establishes derived artifact status, canon non-contradiction, source attribution, canon layer distinction | ADR-005, ADR-006 | Lorebook generation, world knowledge bases, encyclopedic reference content |

**Sub-rules:**

| Sub-Rule | Description |
|----------|-------------|
| R-009-LRB-001 | Derived Artifact Status — Lorebooks are not authority records |
| R-009-LRB-002 | Canon Non-Contradiction — Repository is authoritative |
| R-009-LRB-003 | Source Attribution — All entries reference database/ |
| R-009-LRB-004 | Canon Layer Distinction — Active/Historical/Cultural marked |

---

## 3. SKILLS REFERENCE

### 3.1 Skills by Workflow Domain

#### Domain: General Repository Audit

| Skill | Purpose | When to Use | When NOT to Use | Typical Outputs |
|-------|---------|-------------|-----------------|-----------------|
| **Audit** | Repository-wide audit, consistency checks, structural reviews, governance validation, duplication analysis | Repository health checks, pre-implementation reviews, migration validation, governance audits | When a domain-specific skill exists (use targeted skill instead) | Executive Summary, Findings, Anomalies Detected, Risk Assessment, Recommended Remediation |

---

#### Domain: Authority & Boundary Validation

| Skill | Purpose | When to Use | When NOT to Use | Typical Outputs |
|-------|---------|-------------|-----------------|-----------------|
| **Authority Boundary Audit** | Audits authority boundaries, verifies ownership separation, detects cross-authority contamination | Validating separation between Character/Family/Visual/Experience authorities, post-migration verification | When auditing a single character (use Character Audit instead) | Executive Summary, Authority Layer Review, Cross-Contamination Detection, Boundary Violations, Template Compliance |
| **Cross Reference Audit** | Validates relationships, references, dependencies, links across authority layers | Verifying reference integrity, detecting broken links, validating family graph consistency | When only template compliance is needed (use Authority Boundary Audit) | Executive Summary, Reference Integrity Status, Broken References, Ownership Violations |

---

#### Domain: Character Engineering

| Skill | Purpose | When to Use | When NOT to Use | Typical Outputs |
|-------|---------|-------------|-----------------|-----------------|
| **Character Audit** | Complete compliance audit of a character record against all authority boundaries and governance rules | Character validation, import review, modification verification, recovery audit | When auditing repository structure (use Repository Hardening) | Executive Summary, Compliance Results, Authority Boundary Review, Findings, Anomalies, Risk Assessment |

---

#### Domain: Canon Governance

| Skill | Purpose | When to Use | When NOT to Use | Typical Outputs |
|-------|---------|-------------|-----------------|-----------------|
| **Canon Candidate Review** | Evaluates proposed canon before repository entry; enforces Canon Recovery Workflow | New canon proposals, recovered archive material, imported records, deferred canon evaluation | When canon is already approved (use Export Readiness instead) | Executive Summary, Evidence Assessment, Governance Review, Authority Review, Canon Layer Classification, Final Recommendation (APPROVE/DEFER/REJECT) |

---

#### Domain: Export & Generation

| Skill | Purpose | When to Use | When NOT to Use | Typical Outputs |
|-------|---------|-------------|-----------------|-----------------|
| **Export Readiness** | Evaluates whether content is ready for runtime generation and export (bot, lorebook, engine) | Pre-export validation, bot generation readiness, lorebook readiness, engine consumption check | When content is not yet complete (use Character Audit first) | Executive Summary, Export Status, Bot/Lorebook/Engine Readiness, Export Blockers |
| **Bot Build Review** | Reviews bot character card generation against export schema and repository canon | Bot export validation, platform compatibility check, field mapping verification | When bot is not yet generated (use Export Readiness first) | Executive Summary, Schema Compliance, Field Mapping, Canon Compliance, Platform Compatibility, Provenance |
| **Lorebook Build Review** | Reviews lorebook generation against lorebook specification and repository canon | Lorebook validation, entry structure verification, canon-layer tagging audit | When lorebook is not yet generated (use Export Readiness first) | Executive Summary, Entry Format, Canon-Layer Tagging, Source Attribution, Content Accuracy |

---

#### Domain: Engine & Architecture

| Skill | Purpose | When to Use | When NOT to Use | Typical Outputs |
|-------|---------|-------------|-----------------|-----------------|
| **Engine Contract Validation** | Validates engine architecture, specifications, runtime contracts, exporter compatibility | Engine development, specification review, validation pipeline assessment, implementation readiness | When not developing engine systems (use Repository Hardening for general structure) | Executive Summary, Contract Consistency, Authority Boundary Review, Specification Compatibility, Validation Coverage |
| **Validation Pipeline Review** | Reviews the 47-check validation pipeline for completeness, correctness, coverage | Pipeline audit, check coverage verification, governance alignment, pipeline readiness | When not working on validation pipeline (use Engine Contract Validation for broader scope) | Executive Summary, Specification Completeness, Check Coverage, Governance Alignment, Coverage Gaps |

---

#### Domain: Repository Structure

| Skill | Purpose | When to Use | When NOT to Use | Typical Outputs |
|-------|---------|-------------|-----------------|-----------------|
| **Repository Hardening** | Evaluates repository health, structural consistency, governance alignment, implementation readiness | Pre-implementation reviews, stabilization phases, migration validation, structural maintenance | When auditing specific content (use domain-specific skills) | Executive Summary, Repository Health Score, Structural Review, Governance Review, Hardening Recommendations |

---

### 3.2 Skill Invocation Rules

1. **All skills are audit-only by default.** They do not modify repository content.
2. **All skills return findings in chat only.** No files are created.
3. **All skills require explicit user approval** before any remediation is proposed.
4. **Severity levels:** PASS / WARNING / FAIL (or READY / READY WITH WARNINGS / NOT READY for Export Readiness).
5. **Skills validate against:** ADRs, Rules, Specifications, and canonical records in `database/`.

---

## 4. COMMANDS REFERENCE

### 4.1 Commands by Workflow Domain

#### Domain: General Audit

| Command | Associated Skill(s) | Purpose | Typical Usage |
|---------|---------------------|---------|---------------|
| `/audit` | Audit | Run repository-wide audit | Structure, governance, ADR consistency, migration residue checks |

#### Domain: Character Engineering

| Command | Associated Skill(s) | Purpose | Typical Usage |
|---------|---------------------|---------|---------------|
| `/character-audit` | Character Audit | Audit a single character record | Character validation, import review, modification verification |
| `/character-ready` | Export Readiness | Evaluate character export readiness | Pre-export check, bot generation readiness |

#### Domain: Bot & Lorebook Generation

| Command | Associated Skill(s) | Purpose | Typical Usage |
|---------|---------------------|---------|---------------|
| `/build-bot` | Export Readiness | Generate bot configuration | Bot character card generation, platform export |
| `/build-lorebook` | Export Readiness | Generate lorebook content | Lorebook creation, world knowledge base generation |
| `/bot-check` | Export Readiness | Validate bot export compatibility | Pre-release bot validation, platform compliance |
| `/lorebook-check` | Export Readiness | Validate lorebook export compatibility | Pre-release lorebook validation, canon compliance |

#### Domain: Engine & Architecture

| Command | Associated Skill(s) | Purpose | Typical Usage |
|---------|---------------------|---------|---------------|
| `/build-engine` | Engine Contract Validation | Validate engine architecture | Engine specification review, runtime contract validation |
| `/engine-check` | Engine Contract Validation | Validate engine contracts | Engine compliance, specification alignment |

#### Domain: Repository & Release

| Command | Associated Skill(s) | Purpose | Typical Usage |
|---------|---------------------|---------|---------------|
| `/repo-check` | Repository Hardening | Run repository hardening check | Structural integrity, governance consistency, implementation readiness |
| `/validate` | Export Readiness + Engine Contract Validation | Run cross-validation | Combined export and engine validation |
| `/release-check` | Repository Hardening + Export Readiness + Engine Contract Validation | Full release validation | Pre-release comprehensive audit |

---

### 4.2 Command-to-Skill Mapping

```
Commands                    Skills
─────────                   ──────
/audit              →       Audit
/character-audit    →       Character Audit
/character-ready    →       Export Readiness
/build-bot          →       Export Readiness
/build-lorebook     →       Export Readiness
/bot-check          →       Export Readiness
/lorebook-check     →       Export Readiness
/build-engine       →       Engine Contract Validation
/engine-check       →       Engine Contract Validation
/repo-check         →       Repository Hardening
/validate           →       Export Readiness + Engine Contract Validation
/release-check      →       Repository Hardening + Export Readiness + Engine Contract Validation
```

---

## 5. TOOL SELECTION MATRIX

### 5.1 Decision Matrix: Objective → Tool

| Objective | Use Skill | Use Command |
|-----------|-----------|-------------|
| **Repository audit** (structure, governance, consistency) | Repository Hardening | `/repo-check` |
| **Character validation** (single record compliance) | Character Audit | `/character-audit` |
| **Cross-reference verification** (links, references, dependencies) | Cross Reference Audit | *(invoke skill directly)* |
| **Canon review** (new proposals, candidate evaluation) | Canon Candidate Review | *(invoke skill directly)* |
| **Export readiness** (bot/lorebook/engine generation prep) | Export Readiness | `/character-ready` |
| **Engine validation** (architecture, contracts, specifications) | Engine Contract Validation | `/engine-check` |
| **Lorebook validation** (entry structure, canon-layer tagging) | Lorebook Build Review | `/lorebook-check` |
| **Bot validation** (character card, platform compatibility) | Bot Build Review | `/bot-check` |
| **Authority ownership review** (boundary separation, contamination) | Authority Boundary Audit | *(invoke skill directly)* |
| **Pipeline validation** (47-check coverage, governance alignment) | Validation Pipeline Review | *(invoke skill directly)* |
| **Full release validation** | Repository Hardening + Export Readiness + Engine Contract Validation | `/release-check` |
| **Cross-validation** (export + engine) | Export Readiness + Engine Contract Validation | `/validate` |

### 5.2 Decision Matrix: Domain → Rules

| Domain | Primary Rules | Supporting Rules |
|--------|---------------|-----------------|
| Runtime behavior | R-000 | R-006 |
| Dynasty/lineage | R-001 | R-002, R-006 |
| Family/genealogy | R-002 | R-001, R-003, R-006 |
| Character/identity | R-003 | R-002, R-004, R-005, R-006 |
| Visual/appearance | R-004 | R-003, R-006 |
| Experience/scenario | R-005 | R-003, R-006 |
| Repository governance | R-006 | R-000 |
| Engine/runtime systems | R-007 | R-000, R-006 |
| Bot generation | R-008 | R-003, R-006, R-007 |
| Lorebook generation | R-009 | R-005, R-006, R-007 |

---

## 6. PROMPT WRITING GUIDELINES

### 6.1 When to Invoke Commands

Use **commands** when:
- The objective maps directly to a single workflow (e.g., "audit this character" → `/character-audit`)
- You want a standard audit/review with default scope
- The task is a common operation with a predefined skill path

**Pattern:**
```
/[command-name]
Target: [specific record or scope]
Constraints: [audit-only / specific focus]
```

### 6.2 When to Invoke Skills Directly

Use **skills** when:
- The objective requires a specific audit workflow not covered by a command
- You need to combine multiple skills in a custom way
- The task requires explicit control over the audit scope
- No command exists for the workflow (e.g., Authority Boundary Audit, Canon Candidate Review)

**Pattern:**
```
Invoke: [Skill Name]
Target: [specific records or scope]
Objective: [what you want to verify]
Constraints: [audit-only / specific rules to apply]
Expected Output: [specific findings needed]
```

### 6.3 When to Reference Rules

Reference **rules** when:
- The task involves governance decisions (cite specific R-XXX sub-rules)
- You need to enforce authority boundaries during an operation
- The task requires validation against specific operational constraints
- You need to justify why something is allowed or prohibited

**Pattern:**
```
Validate against: R-003-CHR-007 (No Genealogy in Character Files)
Enforce: R-001-DYN-005 (Hyphenated Surname Mandate)
```

### 6.4 When to Reference ADRs

Reference **ADRs** when:
- The task involves canon classification (cite ADR-006)
- You need to resolve authority conflicts (cite ADR-000 hierarchy)
- The task requires architectural decision context
- You need to justify layer assignments or authority ownership

**Pattern:**
```
Canon Layer: Active Canon per ADR-006 Section "Layer 1"
Authority: Character Authority per ADR-003
Conflict Resolution: ADR-006 Section "Conflict Resolution"
```

### 6.5 General Prompt Principles

1. **Be specific about scope.** "Audit repository" is vague. "Audit "database/characters/C_Malachia_Douglas_Bloodmoon.md` for Character Authority boundary compliance" is precise.

2. **State constraints explicitly.** "Audit only" vs "Audit and propose remediation" are different tasks.

3. **Reference, don't repeat.** Instead of rewriting the Canon Recovery Workflow steps, reference "R-006-GOV-001: Canon Recovery Workflow."

4. **Use the Standard Prompt Pattern** (see Section 7) for complex tasks.

5. **Never bypass governance.** If evidence is missing, STOP and classify as "MISSING EVIDENCE" per project_memory Missing Evidence Rule.

---

## 7. PROMPT TEMPLATES

### 7.1 Standard Project Prompt Template

```
Context:
  [Background information. What exists. What changed. Why this matters.]

Command or Skill:
  [Specific command (/command) or skill name (Skill Name)]

Target:
  [Specific file, record, authority layer, or scope]

Objective:
  [What you want to achieve. Single, clear goal.]

Constraints:
  [Audit-only / Specific rules to apply / Canon Freeze compliance / etc.]

Expected Output:
  [Specific deliverables. Report format. Findings structure.]
```

### 7.2 Simplification Examples

#### Example 1: Character Audit

**Before (long procedural prompt):**
```
I need you to check the character record for Malachia Douglas-Bloodmoon. 
First, verify that the identity data is correct — name, pronouns, surname. 
Then check that there's no genealogy stored in the file. Then verify that 
appearance data is not defined in the file. Then check that there's no 
scenario data stored as canon. Then validate against the Character Authority 
rules and the Family Authority rules. Then check template compliance. 
Return findings in chat only. Do not modify any files.
```

**After (using skill):**
```
Invoke: Character Audit
Target: database/characters/C_Malachia_Douglas_Bloodmoon.md
Objective: Full compliance audit against all authority boundaries
Constraints: Audit-only. Validate against R-002, R-003, R-004, R-005, R-006.
Expected Output: Executive Summary, Compliance Results, Findings, Risk Assessment
```

#### Example 2: Repository Hardening

**Before (long procedural prompt):**
```
I need you to check the entire repository structure. Verify that the 
directory structure is correct, that there are no duplicate files, that 
governance documents are aligned, that there's no migration residue, that 
internal references resolve, and that the repository is ready for 
implementation. Return findings in chat only.
```

**After (using command):**
```
/repo-check
Scope: Full repository
Constraints: Audit-only
```

#### Example 3: Export Readiness

**Before (long procedural prompt):**
```
Check if the character Alyssa Douglas-Bloodmoon is ready for bot generation. 
Verify that all required fields exist, that personality data is present, 
that biography is complete, that visual references resolve, that family 
references are correct, and that the record can be exported to JanitorAI 
and SillyTavern formats. Return findings in chat only.
```

**After (using command):**
```
/character-ready
Target: database/characters/C_Alyssa_Douglas_Bloodmoon.md
Platforms: JanitorAI, SillyTavern
Constraints: Audit-only
```

#### Example 4: Canon Candidate Review

**Before (long procedural prompt):**
```
I have a new character proposal that I want to evaluate before it enters 
the repository. Check if the evidence exists, if the sources are documented, 
if the canon recovery workflow has been completed, if the authority ownership 
is correct, if it violates Canon Freeze, and classify the canon layer. 
Return a recommendation: APPROVE, DEFER, or REJECT.
```

**After (using skill):**
```
Invoke: Canon Candidate Review
Target: [candidate record or proposal]
Objective: Governance review and classification recommendation
Constraints: Audit-only. Validate against R-000, R-006, ADR-006.
Expected Output: Evidence Assessment, Governance Review, Final Recommendation
```

#### Example 5: Cross-Reference Audit

**Before (long procedural prompt):**
```
Check all cross-references in the repository. Verify that character files 
reference existing family records, that visual references resolve, that 
experience links are valid, that the family graph has no orphaned nodes, 
that authority boundaries are respected, and that canon layer assignments 
are consistent. Return findings in chat only.
```

**After (using skill):**
```
Invoke: Cross Reference Audit
Target: Full repository
Objective: Reference integrity validation across all authority layers
Constraints: Audit-only. Validate against R-002, R-003, R-004, R-005.
```

---

## 8. FUTURE EXPANSION RECOMMENDATIONS

### 8.1 Potential New Skills

| Skill | Purpose | Trigger |
|-------|---------|---------|
| **Experience Audit** | Validate experience/scenario records against Experience Authority rules | When experience records are created or modified |
| **World Audit** | Validate world/visual records against Visual Authority rules | When world records are created or modified |
| **Family Graph Audit** | Validate family graph integrity, detect circular references, orphaned nodes | When family records are modified |
| **Canon Promotion Review** | Evaluate Deferred → Active or Candidate → classified promotions | When canon layer changes are proposed |

### 8.2 Potential New Commands

| Command | Associated Skill | Purpose |
|---------|------------------|---------|
| `/experience-audit` | Experience Audit (future) | Audit experience records |
| `/family-audit` | Family Graph Audit (future) | Audit family graph integrity |
| `/canon-review` | Canon Candidate Review | Evaluate canon proposals |
| `/boundary-check` | Authority Boundary Audit | Check authority boundaries |

### 8.3 Potential New Rules

| Rule | Purpose | Authority |
|------|---------|-----------|
| **R-010** | World System Rules — Govern world/location records when world systems are introduced | Future ADR |
| **R-011** | Institution Rules — Govern institutional records (DCC, Seven Hills, etc.) | Future ADR |
| **R-012** | Temporal Rules — Govern timeline consistency and cross-record temporal validation | Future ADR |

### 8.4 Expansion Constraints

All future expansion must comply with:
- **Canon Freeze v1** (R-000-RUN-003) — No new canon without Authority Decision
- **Family Authority Before Expansion** (R-006-GOV-012) — Foundation must be stable
- **Authority Hierarchy** (R-006-GOV-002) — ADRs supersede all other sources
- **Naming Convention Standard** (R-006-GOV-014) — All new files must use correct prefixes
- **Repository Structure Authority** (R-006-GOV-015) — No structural changes without Architecture Review

---

## APPENDIX A: Complete File Inventory

### Rules (10 files)
```
d:\SvartulfrVerse\.trae\rules\R-000_Runtime_Rules.md
d:\SvartulfrVerse\.trae\rules\R-001_Dynastic_Rules.md
d:\SvartulfrVerse\.trae\rules\R-002_Family_Rules.md
d:\SvartulfrVerse\.trae\rules\R-003_Character_Rules.md
d:\SvartulfrVerse\.trae\rules\R-004_Visual_Rules.md
d:\SvartulfrVerse\.trae\rules\R-005_Experience_Rules.md
d:\SvartulfrVerse\.trae\rules\R-006_Governance_Rules.md
d:\SvartulfrVerse\.trae\rules\R-007_Engine_Rules.md
d:\SvartulfrVerse\.trae\rules\R-008_Bot_Rules.md
d:\SvartulfrVerse\.trae\rules\R-009_Lorebook_Rules.md
```

### Skills (11 files)
```
d:\SvartulfrVerse\.trae\skills\audit\SKILL.md
d:\SvartulfrVerse\.trae\skills\authority-boundary-audit\SKILL.md
d:\SvartulfrVerse\.trae\skills\bot-build-review\SKILL.md
d:\SvartulfrVerse\.trae\skills\canon-candidate-review\SKILL.md
d:\SvartulfrVerse\.trae\skills\character-audit\SKILL.md
d:\SvartulfrVerse\.trae\skills\cross-reference-audit\SKILL.md
d:\SvartulfrVerse\.trae\skills\engine-contract-validation\SKILL.md
d:\SvartulfrVerse\.trae\skills\export-readiness\SKILL.md
d:\SvartulfrVerse\.trae\skills\lorebook-build-review\SKILL.md
d:\SvartulfrVerse\.trae\skills\repository-hardening\SKILL.md
d:\SvartulfrVerse\.trae\skills\validation-pipeline-review\SKILL.md
```

### Commands (12 files)
```
d:\SvartulfrVerse\.trae\commands\audit.md
d:\SvartulfrVerse\.trae\commands\bot-check.md
d:\SvartulfrVerse\.trae\commands\build-bot.md
d:\SvartulfrVerse\.trae\commands\build-engine.md
d:\SvartulfrVerse\.trae\commands\build-lorebook.md
d:\SvartulfrVerse\.trae\commands\character-audit.md
d:\SvartulfrVerse\.trae\commands\character-ready.md
d:\SvartulfrVerse\.trae\commands\engine-check.md
d:\SvartulfrVerse\.trae\commands\lorebook-check.md
d:\SvartulfrVerse\.trae\commands\release-check.md
d:\SvartulfrVerse\.trae\commands\repo-check.md
d:\SvartulfrVerse\.trae\commands\validate.md
```

### ADRs (7 files)
```
d:\SvartulfrVerse\core\ADR-000_Runtime_Baseline.md
d:\SvartulfrVerse\core\ADR-001_Dynastic_Origins.md
d:\SvartulfrVerse\core\ADR-002_Family_Authority.md
d:\SvartulfrVerse\core\ADR-003_Character_Authority.md
d:\SvartulfrVerse\core\ADR-004_Visual_Authority.md
d:\SvartulfrVerse\core\ADR-005_Experience_Authority.md
d:\SvartulfrVerse\core\ADR-006_Canon_Layer_Architecture.md
```

### Specifications (4 files)
```
d:\SvartulfrVerse\core\BOT_EXPORT_SPECIFICATION.md
d:\SvartulfrVerse\core\ENGINE_SPECIFICATION.md
d:\SvartulfrVerse\core\LOREBOOK_SPECIFICATION.md
d:\SvartulfrVerse\core\VALIDATION_PIPELINE_SPECIFICATION.md
```

---

*This document is project source material. It does not modify repository governance. All authority remains with ADRs, Rules, and canonical records in `database/`.*
