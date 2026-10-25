# E2E Test Infra: Svartúlfr Verse — World Simulation & VN Engine Optimization

## Test Philosophy
- Opaque-box, requirement-driven verification covering live API states, data integrity, formatting discipline, and DOM rendering.
- Methodology: Category-Partition + Boundary Value Analysis + Pairwise Combinatorial Testing + Workload Testing.

## Feature Inventory
| # | Feature | Source (requirement) | Tier 1 | Tier 2 | Tier 3 |
|---|---------|---------------------|:------:|:------:|:------:|
| 1 | 13 Primary World Characters Deployment | Req 1 (POST /api/worlds/characters) | 5 | 5 | ✓ |
| 2 | Scenario =>Speaker: Syntax Standardization | Req 2 (PUT /api/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H) | 5 | 5 | ✓ |
| 3 | Active Chat Message #0 Swipe Patch | Req 2 (PUT /api/new/chat-logs/swipe/message_swipe_99mmMgEEQjk2pkJN3hXkQ) | 5 | 5 | ✓ |
| 4 | VN Mode Display Settings | Req 3 (PUT /api/new/chat-logs/:id chat_overrides) | 5 | 5 | ✓ |
| 5 | Right Sidebar Flags & Stats Tab Sheet Loading | Req 3 (Sidebar flags & simulation engine) | 5 | 5 | ✓ |
| 6 | Chrome DevTools Live Browser Validation | Req 4 (Console, DOM, Network inspection) | 5 | 5 | ✓ |

## Test Architecture
- **Test Runner**: Python test scripts in `scripts/verify_*.py` and Playwright tests in `scratch/validate_*.py`.
- **Pass/Fail Semantics**: Exit code 0 for all passing tests; non-zero exit code on assertion failure.
- **Verification Channels**:
  - Live Wyvern REST API queries (`GET /api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ`, `GET /api/worlds/scenarios/_2MTWKjxrQPdQVaz9y4Q7H`, `GET /api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN`).
  - Formatting discipline audits (zero em-dashes `—`, zero narrative asterisks `*`, dialogue in quotes `"..."`).
  - Headless/Attached browser validation evaluating console messages and DOM presence of VN sprites and Stats character cards.

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Complexity |
|---|----------|--------------------|------------|
| 1 | Full Welcome Day Dialogue Flow | F1, F2, F3, F4 (Visual Novel sprite splitting, dialogue playback, correct character nameplates) | High |
| 2 | Simulation & Character Sheet Rendering | F1, F4, F5 (Stats tab displays 13 characters with 25-pt 6-stat bars, level <= 99) | High |
| 3 | Multi-character Party & Scene Auto-Apply | F1, F5 (Party synchronization and scene auto-apply without unreviewed AI injection) | Medium |
| 4 | Offline/Online State Continuity | F1, F2, F3, F4, F5 (Persistence across page refresh and API fetch without schema mismatch) | Medium |
| 5 | Live Browser Performance & Zero Error Assertions | F1, F2, F3, F4, F5, F6 (Console error-free turn execution under CDP) | High |

## Coverage Thresholds
- Tier 1: ≥5 per feature (Total ≥ 30)
- Tier 2: ≥5 per feature (Total ≥ 30)
- Tier 3: Major pairwise interactions (Total ≥ 10)
- Tier 4: Realistic application workflows (Total ≥ 5)
