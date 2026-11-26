# DISPATCH — Orchestrator 3

## Task
Implement and deploy the Svartúlfr AI Game Master / Narrator and custom Prompt Assembly on Wyvern Chat, validating the result via Chrome DevTools.

## Instructions
Refer to `.agents/teamwork/ORIGINAL_REQUEST.md` (section `## Follow-up — 2026-10-20T17:19:55Z`).
Working Directory: `e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_3`
Coordinate the necessary specialist agents (explorers, workers, reviewers) to implement, deploy, and validate the requirements.

## 2026-10-20T17:21:33Z
You are the Project Orchestrator for Svartúlfr Verse.
Your working directory is: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_3
The authoritative request is in: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md under section "## Follow-up — 2026-10-20T17:19:55Z".

Your mission:
Implement and deploy the Svartúlfr AI Game Master / Narrator and custom Prompt Assembly on Wyvern Chat, validating the result via Chrome DevTools.

## Requirements Overview
1. R1. Svartúlfr Game Master Assistant Configuration & Deployment
   Create and deploy a standalone Assistant in Wyvern Chat (`/mine > ASSISTANT`) named `Svartúlfr — Game Master & World Engine`:
   - Configured with official System Prompt and Final Instructions adhering to Svartúlfr canon rules (Italian Sandwich language enforcement, third-person present tense, anti-puppeting of `{{user}}`, thought privacy, multi-NPC dialogue format `Nome: "..."`).
   - Integrates the D20 + S.P.E.C.I.A.L. (`STR, PER, END, CHA, INT, AGI, LCK`) skill check resolution engine with isolated diegetic formatting `> [TEST: ...]`.
   - Connects to the 6 official Standalone Lorebooks (`Lore I`, `Lore II`, `Lore III`, `Locations`, `NPC Primary`, `NPC Secondary`).

2. R2. Custom TTRPG Prompt Assembly Setup
   Create and configure the custom Prompt Assembly preset in `AI Connections > Prompts` named `Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)`:
   - Main Prompt Template with standard Handlebars macros.
   - Lore Templates formatted with XML `<npc>`, `<location>`, `<item>`, `<lore_entry>` and `<special_stats>{{rpg_stats}}</special_stats>`.
   - Floating Prompt Template injected at Depth 4% with HTTP role `User` containing active anti-drift directives.
   - Director's Whisper template configured for OOC instructions.
   - Final Instructions post-history with HTTP role `User` enforcing formatting, situational digital feeds (`【 LIVE FEED 】`, `❤️Pack-Family❤️`), and strict Italian output.

3. R3. Chrome DevTools & Network Validation
   Validate the deployed Assistant and Prompt Assembly in the live browser session on `https://app.wyvern.chat`:
   - Inspect DOM elements, ensure values and settings are correctly populated and saved.
   - Check browser console for errors or warnings and ensure network API requests succeed with HTTP 200 OK.
   - Execute a test verification turn demonstrating the D20 + S.P.E.C.I.A.L. check resolution.
