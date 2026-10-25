# Project: Svartúlfr AI Game Master & Custom TTRPG Prompt Assembly

## Architecture
- Standalone Assistant in Wyvern Chat (`/mine > ASSISTANT`):
  - Name: `Svartúlfr — Game Master & World Engine`
  - System Prompt & Final Instructions: Italian Sandwich language enforcement, third-person present tense, anti-puppeting of `{{user}}`, thought privacy, multi-NPC dialogue format `Nome: "..."`.
  - Resolution Engine: D20 + S.P.E.C.I.A.L. (`STR, PER, END, CHA, INT, AGI, LCK`) skill check resolution engine with isolated diegetic formatting `> [TEST: ...]`.
  - Lorebook Connections: 6 official standalone lorebooks (`_gwwCxCfQ6PQaLEjAQVpJL`, `_HfG7TeV6MJyj6bxMwxkpt`, `_9zWTGqYJNJ4BCDMj8gfcD`, `_EjXxkmPVhpCXg8xABpFkK`, `_zwEqgEEzh12X6gHVmMKKC`, `_Uht3Ckz44JBDrPnUHq7LV`).
- Custom TTRPG Prompt Assembly (`AI Connections > Prompts`):
  - Name: `Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)`
  - Main Prompt Template with standard Handlebars macros.
  - Lore Templates formatted with XML `<npc>`, `<location>`, `<item>`, `<lore_entry>` and `<special_stats>{{rpg_stats}}</special_stats>`.
  - Floating Prompt Template injected at Depth 4% with HTTP role `User` containing active anti-drift directives.
  - Director's Whisper template configured for OOC instructions.
  - Final Instructions post-history with HTTP role `User` enforcing formatting, situational digital feeds (`【 LIVE FEED 】`, `❤️Pack-Family❤️`), and strict Italian output.
- Chrome DevTools Validation:
  - Live inspection on `https://app.wyvern.chat` verifying DOM persistence, zero console errors, HTTP 200 API responses.
  - Live turn verification demonstrating D20 + S.P.E.C.I.A.L. check resolution and no-puppeting compliance.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | GM Assistant Architecture & Schema | Assistant schema, system prompt, final instructions, D20 + S.P.E.C.I.A.L. | M1 | ORIGINAL_REQUEST §R1 |
| 2 | Prompt Assembly Schema & Presets | Handlebars templates, XML tags, Floating prompt, Director's Whisper | M1 | ORIGINAL_REQUEST §R2 |
| 3 | Chrome DevTools MCP & Environment | Inspect live browser session, targets, DOM selectors, API network | M1 | ORIGINAL_REQUEST §R3 |
| 4 | GM Assistant Payload Creation & API Deployment | Build Assistant JSON/payload and deploy via API / UI with 6 lorebooks | M2 | ORIGINAL_REQUEST §R1 |
| 5 | Prompt Assembly Configuration & Deployment | Configure and persist custom Prompt Assembly preset | M2 | ORIGINAL_REQUEST §R2 |
| 6 | Verification & Forensic Audit | Audit prompt assembly, assistant settings, lorebook bindings, zero em-dashes | M3 | ORIGINAL_REQUEST §R1, §R2 |
| 7 | Live Chrome DevTools Validation & Test Turn | Validate DOM, network requests (HTTP 200), console logs, run test roll | M4 | ORIGINAL_REQUEST §R3 |
| 8 | Documentation & Changelog Update | Update CHANGELOG.md and record assistant ID and preset details | M5 | Acceptance Criteria |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Survey & Technical Investigation | Investigate Wyvern API for assistants, prompt presets, and Chrome DevTools setup | none | IN_PROGRESS |
| 2 | Implementation & Deployment | Construct Assistant & Prompt Assembly payloads, deploy to Wyvern | M1 | PLANNED |
| 3 | Verification & Forensic Audit | Reviewers, Challengers, and Forensic Auditor verify invariants | M2 | PLANNED |
| 4 | Chrome DevTools Live Verification | Inspect browser session, DOM, network, and execute live D20 check | M3 | PLANNED |
| 5 | Final Gate & Victory Report | Verify all acceptance criteria and notify Sentinel | M4 | PLANNED |

## Code Layout & Boundaries
- Assistant & Prompt Assembly Payloads: `FINAL/`, `scratch/`
- Authentication / Tokens: `scratch/wyvern_token.txt`, `scratch/refresh_token.py`
- Verification Scripts & Test Harness: `scratch/`
- Documentation: `CHANGELOG.md`
- Metadata & Orchestration: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_3\`
