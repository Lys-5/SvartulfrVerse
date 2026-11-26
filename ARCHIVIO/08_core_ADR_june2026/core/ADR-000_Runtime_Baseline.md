# ADR-000: Runtime Baseline

**Status:** DECISION  
**Date:** 2026-06-07  
**Title:** Canonical Repository Baseline & Archive Freeze

## Context

The Progetti repository (historical archive) contains significant canonical data accumulated over multiple versions, but exhibits documented degradation patterns:

- Noah occupation drift
- Douglas-Bloodmoon naming inconsistencies
- Family relationship degradation
- World canonical compression
- Character role homogenization

The SvartulfrVerse repository has completed migration and achieved Canon Freeze v1.

## Decision

1. **Progetti becomes read-only Historical Archive**
   - No further development in legacy repository
   - Reference only for canon recovery
   - Source for historical verification

2. **SvartulfrVerse becomes Active Runtime Repository**
   - Single source of truth for current canon
   - Runtime behavior validates all data
   - Canonical stabilization before expansion
   - Canon scope: Only Human + Contemporary + Los Angeles Dynasty

3. **Canon Recovery Workflow established**
   - Research collects evidence from archive sources
   - Recovery audit classifies all evidence
   - Architecture review verifies ADR consistency
   - Authority decision gates all additions
   - No direct archive imports

## Rationale

- Runtime preservation prevents behavior loss
- Incremental validation prevents drift recurrence
- Single source of truth reduces contradictions
- Explicit workflow creates audit trail
- Contemporary + Only Human scope enables deep canonical stability before world expansion

## Constraints

- No legacy content imported until validated
- No runtime logic in repository
- No unaudited character definitions
- No world systems without architecture approval
- No supernatural systems without scope expansion approval

## Implications

- Phase 1-8: Migration & Canon Consolidation — COMPLETE (2026-06-08)
- Phase 9: Canon Freeze v1 — ACTIVE
- Phase 10+: Future expansion (requires Authority Decision)

All phases require explicit canon decisions before implementation.

## Authority

Established by: Family Authority & Canon Reconstruction Workspace  
Approved by: Runtime Validation  
Supersedes: All legacy Progetti workflows
