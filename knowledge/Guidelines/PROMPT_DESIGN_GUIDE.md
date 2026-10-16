# PROMPT_DESIGN_GUIDE

**Version:** 1.0  
**Date:** 2026-06-08  
**Purpose:** Guide for writing effective project prompts. Reference this document to leverage existing Rules, Skills, and Commands instead of rewriting workflow instructions.

---

## 1. PROMPT ARCHITECTURE

### Standard Prompt Pattern

Every project prompt should follow this structure:

```
Context:
  [What exists. What changed. Why this matters.]

Command or Skill:
  [/command-name] or [Skill Name]

Target:
  [Specific file, record, authority layer, or scope]

Objective:
  [Single, clear goal.]

Constraints:
  [Audit-only / Specific rules / Canon Freeze compliance]

Expected Output:
  [Specific deliverables. Report format.]
```

### Prompt Decision Tree

```
What is your objective?
    │
    ├── Repository audit → /repo-check (Repository Hardening skill)
    │
    ├── Character validation → /character-audit (Character Audit skill)
    │
    ├── Character export readiness → /character-ready (Export Readiness skill)
    │
    ├── Bot generation → /build-bot (Export Readiness skill)
    │
    ├── Bot validation → /bot-check (Export Readiness skill)
    │
    ├── Lorebook generation → /build-lorebook (Export Readiness skill)
    │
    ├── Lorebook validation → /lorebook-check (Export Readiness skill)
    │
    ├── Engine validation → /engine-check (Engine Contract Validation skill)
    │
    ├── Cross-validation → /validate (Export Readiness + Engine Contract Validation)
    │
    ├── Full release → /release-check (All three skills)
    │
    ├── General audit → /audit (Audit skill)
    │
    ├── Authority boundary check → Authority Boundary Audit skill (no command)
    │
    ├── Cross-reference check → Cross Reference Audit skill (no command)
    │
    ├── Canon candidate evaluation → Canon Candidate Review skill (no command)
    │
    └── Pipeline review → Validation Pipeline Review skill (no command)
```

---

## 2. WHEN TO USE ADRs

Reference **ADRs** when:
- The task involves canon classification (cite ADR-006)
- You need to resolve authority conflicts (cite ADR-000 hierarchy)
- The task requires architectural decision context
- You need to justify layer assignments or authority ownership
- You need to reference dynastic origins (ADR-001) or family structure (ADR-002)

**Pattern:**
```
Validate against: ADR-006 Section "Layer 1: Active Canon"
Authority: ADR-003 Character Authority
Conflict Resolution: ADR-006 Section "Conflict Resolution"
```

**Do NOT reference ADRs for:**
- Routine validation (use Rules instead)
- Skill invocation (use skill names instead)
- Field-level mapping (use specifications instead)

---

## 3. WHEN TO USE Rules

Reference **Rules** when:
- The task involves governance decisions (cite specific R-XXX sub-rules)
- You need to enforce authority boundaries during an operation
- The task requires validation against specific operational constraints
- You need to justify why something is allowed or prohibited

**Pattern:**
```
Enforce: R-003-CHR-007 (No Genealogy in Character Files)
Validate against: R-002-FAM-001 (Genealogy Ownership)
Check: R-006-GOV-013 (Rejected Canon Enforcement)
```

**Common Rule References by Task:**

| Task | Primary Rules |
|------|---------------|
| Character audit | R-002, R-003, R-004, R-005, R-006 |
| Family validation | R-001, R-002, R-006 |
| Visual validation | R-004, R-006 |
| Experience validation | R-005, R-006 |
| Bot generation | R-007, R-008 |
| Lorebook generation | R-007, R-009 |
| Engine development | R-000, R-006, R-007 |
| Canon classification | R-000, R-006 |
| Repository structure | R-006 |

---

## 4. WHEN TO USE Skills

Use **Skills** when:
- The task requires a specific audit workflow
- You need explicit control over the audit scope
- No command exists for the workflow
- You need to combine multiple skills in a custom way

**Pattern:**
```
Invoke: [Skill Name]
Target: [specific records or scope]
Objective: [what you want to verify]
Constraints: [audit-only / specific rules to apply]
Expected Output: [specific findings needed]
```

**Skill Selection Guide:**

| Skill | Use When |
|-------|----------|
| Audit | General repository audit, no specific target |
| Authority Boundary Audit | Checking separation between authorities |
| Character Audit | Validating a single character record |
| Cross Reference Audit | Validating references across layers |
| Canon Candidate Review | Evaluating new canon proposals |
| Export Readiness | Pre-export validation |
| Bot Build Review | Post-generation bot validation |
| Lorebook Build Review | Post-generation lorebook validation |
| Engine Contract Validation | Engine specification compliance |
| Validation Pipeline Review | Pipeline coverage audit |
| Repository Hardening | Structural integrity check |

---

## 5. WHEN TO USE Commands

Use **Commands** when:
- The objective maps directly to a single workflow
- You want a standard audit/review with default scope
- The task is a common operation with a predefined skill path

**Pattern:**
```
/[command-name]
Target: [specific record or scope]
Constraints: [audit-only / specific focus]
```

**Command Quick Reference:**

| Command | Skill | Use |
|---------|-------|-----|
| `/audit` | Audit | General repository audit |
| `/character-audit` | Character Audit | Single character validation |
| `/character-ready` | Export Readiness | Character export check |
| `/build-bot` | Export Readiness | Bot generation |
| `/bot-check` | Export Readiness | Bot validation |
| `/build-lorebook` | Export Readiness | Lorebook generation |
| `/lorebook-check` | Export Readiness | Lorebook validation |
| `/build-engine` | Engine Contract Validation | Engine architecture check |
| `/engine-check` | Engine Contract Validation | Engine contract check |
| `/repo-check` | Repository Hardening | Repository structure check |
| `/validate` | Export Readiness + Engine | Cross-validation |
| `/release-check` | All three | Full release validation |

---

## 6. PROMPT PATTERNS BY WORKFLOW

### 6.1 Audit Workflow

**Purpose:** Validate repository content without modification.

```
Context:
  [What is being audited and why]

Invoke: [Audit | Character Audit | Authority Boundary Audit | Cross Reference Audit]
Target: [specific scope]
Objective: [what to verify]
Constraints: Audit-only. No modifications. Validate against [relevant rules].
Expected Output: Executive Summary, Findings, Risk Assessment, Recommended Actions
```

**Example:**
```
Context: Post-migration validation of all character records.

Invoke: Character Audit
Target: database/characters/ (all C_*.md files)
Objective: Verify Character Authority boundary compliance
Constraints: Audit-only. Validate against R-003, R-002, R-004, R-005.
Expected Output: Per-character compliance report with PASS/WARNING/FAIL
```

### 6.2 Character Work

**Purpose:** Create, validate, or modify character records.

```
Context:
  [Character background and current state]

Invoke: Character Audit
Target: database/characters/C_[Name].md
Objective: [validation | import | modification]
Constraints: [audit-only | specific rules]
Expected Output: [compliance report | import recommendation]
```

**Example:**
```
Context: New character proposal for evaluation.

Invoke: Canon Candidate Review
Target: [candidate record]
Objective: Evaluate evidence and classify canon layer
Constraints: Audit-only. Validate against R-000, R-006, ADR-006.
Expected Output: Evidence Assessment, Governance Review, Final Recommendation
```

### 6.3 Export Work

**Purpose:** Generate or validate bot/lorebook exports.

```
Context:
  [Export target and platform]

Command: /character-ready
Target: database/characters/C_[Name].md
Platforms: [JanitorAI | SillyTavern | Generic JSON]
Constraints: Audit-only. Validate against R-008, BOT_EXPORT_SPECIFICATION.
Expected Output: Export readiness report with READY/NOT READY status
```

**Example:**
```
Context: Generate bot character card for Alyssa.

Command: /build-bot
Target: database/characters/C_Alyssa_Douglas_Bloodmoon.md
Platform: JanitorAI
Constraints: Canon-derived only. R-008-BOT-001 compliance.
Expected Output: JanitorAI JSON character card with provenance metadata
```

### 6.4 Engine Work

**Purpose:** Validate or develop engine systems.

```
Context:
  [Engine scope and current state]

Invoke: Engine Contract Validation
Target: [engine specification or code]
Objective: [validate architecture | check compliance]
Constraints: Audit-only. Validate against R-007, ENGINE_SPECIFICATION.
Expected Output: Contract consistency review, governance alignment
```

### 6.5 Lorebook Work

**Purpose:** Generate or validate lorebook content.

```
Context:
  [Lorebook scope and target platform]

Command: /build-lorebook
Target: [domain: characters | families | worlds | institutions]
Platform: [JanitorAI | SillyTavern]
Constraints: Derived artifact only. R-009 compliance. Canon-layer tagging required.
Expected Output: Lorebook file with metadata header and source attribution
```

---

## 7. BEFORE/AFTER EXAMPLES

### Example 1: Repository Audit

**Before (verbose):**
```
I need you to check the entire repository. Look at the directory structure, 
check for duplicate files, verify governance documents are aligned, check 
for migration residue, verify internal references resolve, and check if the 
repository is ready for implementation. Don't modify anything. Return 
findings in chat only.
```

**After (using command):**
```
/repo-check
Scope: Full repository
Constraints: Audit-only
```

### Example 2: Character Validation

**Before (verbose):**
```
Check the character Malachia Douglas-Bloodmoon. Verify his name is correct, 
check that his surname is Douglas-Bloodmoon with the hyphen, verify his 
parents are Erik and Nixara, check that there's no genealogy stored in his 
file, verify his visual classification is Douglas-dominant, check his 
education is UCLA PhD Sport Sciences, and verify his occupation. Return 
findings in chat only.
```

**After (using skill):**
```
Invoke: Character Audit
Target: database/characters/C_Malachia_Douglas_Bloodmoon.md
Objective: Full compliance audit against all authority boundaries
Constraints: Audit-only. Validate against R-002, R-003, R-004, R-005, R-006.
```

### Example 3: Bot Export

**Before (verbose):**
```
Generate a JanitorAI character card for Alyssa Douglas-Bloodmoon. Pull her 
name, personality, biography, visual description, family relationships, and 
education from the database. Make sure everything traces back to database/ 
files. Include provenance metadata. Don't add any lore that isn't in the 
database. Validate everything before releasing.
```

**After (using command):**
```
/build-bot
Target: database/characters/C_Alyssa.md
Platform: JanitorAI
Constraints: Canon-derived only. R-008-BOT-001 compliance.
```

### Example 4: Canon Evaluation

**Before (verbose):**
```
I found some old material in the archive about a character named Valeria who 
was a wet nurse. Can we evaluate if this should be added to the repository? 
Check if there's evidence, if it conflicts with existing canon, and if it 
violates any rules.
```

**After (using skill + rule reference):**
```
Invoke: Canon Candidate Review
Target: [Valeria / WetNurse / Concubine concept — Progetti archive]
Objective: Evaluate for canon suitability
Constraints: Audit-only. Check R-006-GOV-013 (Rejected Canon Enforcement).
Note: Valeria concept listed as REJECTED in ADR-006.
Expected Output: Evidence Assessment, Governance Review, Final Recommendation
```

### Example 5: Cross-Reference Check

**Before (verbose):**
```
Check all the references in the repository. Make sure character files point 
to existing family records, that visual references are valid, that experience 
links work, that the family graph doesn't have any circular references, and 
that canon layers are consistent. Return findings in chat only.
```

**After (using skill):**
```
Invoke: Cross Reference Audit
Target: Full repository
Objective: Reference integrity validation across all authority layers
Constraints: Audit-only. Validate against R-002, R-003, R-004, R-005.
```

---

## 8. COMMON MISTAKES TO AVOID

### ❌ Don't Rewrite Workflow Instructions

**Bad:** "First, check the directory structure. Then check for duplicates. Then verify governance alignment. Then check for migration residue. Then verify internal references..."

**Good:** `/repo-check` — The Repository Hardening skill already defines this workflow.

### ❌ Don't Reference Skills That Don't Exist

**Bad:** "Use the Character Export skill" (no such skill exists)

**Good:** "Use the Export Readiness skill" or `/character-ready`

### ❌ Don't Skip Constraints

**Bad:** "Audit the repository" (no constraints specified)

**Good:** "Audit the repository. Constraints: Audit-only. No modifications."

### ❌ Don't Invent Governance

**Bad:** "Check that all files follow the new naming convention I just thought of"

**Good:** "Validate against R-006-GOV-014 (Naming Convention Standard)"

### ❌ Don't Combine Multiple Objectives

**Bad:** "Audit the repository, generate bot cards, and validate the engine"

**Good:** Split into three separate prompts, one per objective.

---

## 9. MISSING EVIDENCE PROTOCOL

**MANDATORY:** If required evidence cannot be located:

1. **STOP** evaluation of that item
2. **DO NOT** infer, reconstruct, generate replacement, or assume
3. **Classify** as "MISSING EVIDENCE"
4. **Generate** Manual NotebookLM Audit Required section:
   - Record Name
   - Missing Data
   - Why Required
   - Locations Checked
   - Recommended NotebookLM Query

**Evidence Search Order:**
1. SvartulfrVerse repository
2. `old_template_and_source/`
3. Frozen reports
4. Approved ADRs
5. Migrated authority records
6. Progetti archive (only if missing from above)

**Missing Evidence = STOP CONDITION, NOT Warning Condition.**

---

*This guide is derived from the project toolset: ADR-000 through ADR-006, R-000 through R-009, 11 Skills, 12 Commands, and 4 Specifications.*
