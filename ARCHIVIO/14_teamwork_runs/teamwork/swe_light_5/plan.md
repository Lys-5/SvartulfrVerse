# Orchestration Plan — SWE Light

## Objective
Execute avatar synchronization for 5 active Character Cards with official Lorebook Gallery assets, deploy live via Wyvern Web API (`PUT /api/characters/:id`), and validate 100% 1:1 byte-for-byte text, visual, and `ignored_characters` parity between the 8 Character Cards and Standalone Lorebooks.

## Execution Strategy
- Pattern: SWE Light (sequential refinement)
- Floor: 1 Implementation + At least 3 Review rounds + 1 Victory Audit
- Worker 1: `teamwork_preview_implementer` (initial diff, live API deploy, contract checks)
- Worker 2: `teamwork_preview_reviewer` (Round 1: adversarial review & verification)
- Worker 3: `teamwork_preview_reviewer` (Round 2: adversarial review & verification)
- Worker 4: `teamwork_preview_reviewer` (Round 3: adversarial review & verification)
- Worker 5: `teamwork_preview_victory_auditor` (Independent post-victory audit)

## Open Issues Ledger
*(Ledger initialized empty. Open issues from workers will be tracked here.)*
