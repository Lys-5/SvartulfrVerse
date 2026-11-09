# Project: Svartúlfr Verse — Production Evolution (R1, R2, R3)

## Architecture
- **Canonical Heights & Proportions Layer (R1)**:
  * Unified metric and imperial height representation across all Character Cards (`FINAL/*_card.json`), User Personas (`FINAL/personas/*.json`), and Standalone Lorebooks (`FINAL/Svartulfr_NPC_Primary.json`, `lorebooks/optimized/Svartulfr_NPC_Primary.json`).
  * Direct proportional reference clauses embedded in character dossiers and visual style guide (`database/assets/style_guide.md`).
  * Strict byte-for-byte parity (`entries == lexicon`) preserved across all 6 standalone lorebooks.
- **Visual References & Sacred Marks Layer (R2)**:
  * Formal design specifications and lore guardrails in `docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md`.
  * High-fidelity reference image assets in `asset/references/` (with mirror/pointer in `assets/references/`).
  * Strict compliance with anatomical invariants (Gebo on left wrist in cold iron ink; Máni solely on Alyssa's left hip; Sól solely on Jasper's right hip; pack marks for Logan, Malachia, Erik, Wulfnic).
- **Local Micro-Proxy Engine Layer (R3)**:
  * Loopback isolation on `127.0.0.1:5005` in `proxy/config_free_proxy.json` and `proxy/free_tier_proxy.py`.
  * Generalized, non-destructive 5-phase `PayloadCompactor` eliminating redundant XML entries, duplicate active NPC dossiers, empty tags, and newline cascades.
  * Comprehensive automated test suite in `tests/test_proxy_compaction.py` asserting startup, compaction benchmarks (15–35% reduction), and zero semantic data loss.
- **Verification & Forensic Audit Layer (R4 / E2E)**:
  * Independent programmatic verification scripts checking all heights, parity, image presence, and proxy tests.
  * Rigorous forensic integrity audit (`teamwork_auditor`) with non-negotiable hard veto.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Canonical Heights Alignment | Update heights for Alyssa (155 cm / 5' 1"), Jasper (193 cm / 6' 4"), Noah (197 cm / 6' 5.6"), Malachia (208 cm / 6' 9.9"), Erik (213 cm / 6' 11.9"), Wulfnic (220 cm / 7' 2.6") across cards, personas, lorebooks, and legacy records. | M1 | Survey (Explorer 1) |
| 2 | Proportional Reference Insertion | Embed the 3 direct proportional scale references into character cards, personas, lorebook dossiers, and group visual prompts (`style_guide.md`). | M1 | Survey (Explorer 1) |
| 3 | Lorebook Parity & Invariants Verification | Verify byte-for-byte `entries == lexicon` parity and JED+ single-line bracket formatting across all modified lorebooks via automated verification script. | M1 | Survey (Explorer 1) |
| 4 | Runic & Divine Marks Documentation | Author `docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md` detailing lore invariants, cold iron ink ritual, anatomical placements, and visual prompts. | M2 | Survey (Explorer 2) |
| 5 | Sacred Marks Visual Image Generation | Generate high-fidelity reference images for Gebo wrist, Máni left hip, Sól right hip, twins paired polarity, and Logan/Malachia/Erik/Wulfnic pack marks in `asset/references/`. | M2 | Survey (Explorer 2) |
| 6 | Micro-Proxy Loopback Standard | Set `"host": "127.0.0.1"` in `proxy/config_free_proxy.json` and enforce loopback adapter binding in `proxy/free_tier_proxy.py`. | M3 | Survey (Explorer 3) |
| 7 | Non-Destructive PayloadCompactor | Implement generalized 5-phase compaction pipeline in `proxy/free_tier_proxy.py` (parameter sanitization, XML lore & active NPC dedup, empty tag pruning, whitespace collapsing, role-based merging). | M3 | Survey (Explorer 3) |
| 8 | Proxy Compaction Test Suite | Create `tests/test_proxy_compaction.py` testing loopback startup, payload reduction benchmarks, and strict semantic invariance. | M3 | Survey (Explorer 3) |
| 9 | Dual-Track E2E Test Suite & Forensic Audit | Run end-to-end multi-tier verification and forensic integrity audit ensuring zero regressions and clean verdicts. | M4 | Survey (Orchestrator) |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Canonical Heights & Proportions | Update and verify canonical heights and proportional references across `FINAL/`, personas, lorebooks, and prompts. | none | DONE |
| 2 | Runic & Divine Marks References | Author specification document and generate sacred marks visual images in `asset/references/` and `docs/references/`. | none | DONE |
| 3 | Micro-Proxy Compaction & Tests | Optimize micro-proxy for non-destructive payload compaction, update loopback host, and implement test suite. | none | DONE |
| 4 | Final E2E Verification & Forensic Audit | Execute full verification scripts and forensic integrity audit across all deliverables. | M1, M2, M3 | DONE |

## Interface Contracts
### M1 ↔ Repository Data Format
- Character Card JED+ block: `[NAME: ...; HEIGHT: <cm> (<feet>' <inches>"); ...]` on single line.
- Lorebooks JSON: `entries` array and `lexicon` array must remain 100% byte-for-byte identical.
- Zero em-dash (`—`) in text fields; plain text narration with quotes for dialogue.

### M2 ↔ Asset and Documentation Layout
- Specifications: `docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md`.
- Reference Images: `asset/references/*.png` with mirror in `assets/references/*.png`.
- Divine marks strictly on hips (Máni left hip Alyssa, Sól right hip Jasper). Gebo exclusively on inner left wrist in cold iron ink.

### M3 ↔ Micro-Proxy Execution Interface
- Host: `127.0.0.1`, Port: `5005`.
- Endpoints: `GET /health`, `GET /v1/models`, `POST /v1/chat/completions`.
- Compaction: strictly non-destructive (zero data loss on narrative, rules, characters, lore, or dialogue).
- Test suite: `pytest tests/test_proxy_compaction.py -v`.

## Code Layout
- `FINAL/` (Character cards, personas, standalone lorebooks)
- `lorebooks/optimized/` (Mirrored standalone lorebooks)
- `database/characters/` & `database/assets/style_guide.md` (Legacy dossiers and visual style guide)
- `docs/references/` (Design specifications for marks and references)
- `asset/references/` & `assets/references/` (Generated reference images)
- `proxy/free_tier_proxy.py` & `proxy/config_free_proxy.json` (Local micro-proxy service)
- `tests/test_proxy_compaction.py` (Automated compaction and startup test suite)
- `scripts/` (Operational verification scripts)
- `.agents/teamwork/` (Agent metadata, plans, and handoff reports)
