# DISPATCH — Explorer GM 2 (Prompt Assembly & Handlebars Templates)
Role: teamwork_preview_explorer
Target: Investigate Custom Prompt Assembly preset structure, Handlebars macros, XML formatting (<npc>, <location>, <item>, <lore_entry>, <special_stats>{{rpg_stats}}</special_stats>), Floating Prompt at Depth 4% (role User), Director's Whisper, and Final Instructions (role User, Italian Sandwich, digital feeds).

## 2026-10-20T17:23:34Z
You are Explorer GM 2 (Prompt Assembly Explorer).
Working Directory: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_2
Authoritative Request: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md (section "## Follow-up — 2026-10-20T17:19:55Z").
Project Scope: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_3\PROJECT.md.
Core rules: GEMINI.md, AGENTS.md.

OBJECTIVE:
Investigate how custom Prompt Assemblies in Wyvern Chat (AI Connections > Prompts) are structured, stored, and configured:
1. Determine how Wyvern manages custom prompt presets: Is there an API endpoint (e.g. /api/prompt-templates, /api/prompts, /api/settings), or are they stored in browser localStorage / IndexedDB, or exported/imported as JSON?
2. Research the exact template blocks and Handlebars macros supported in Wyvern Prompt Assembly:
   - Main Prompt Template with standard Handlebars macros
   - Lore Templates formatted with XML <npc>, <location>, <item>, <lore_entry> and <special_stats>{{rpg_stats}}</special_stats>
   - Floating Prompt Template injected at Depth 4% with HTTP role User containing active anti-drift directives
   - Director's Whisper template configured for OOC instructions
   - Final Instructions post-history with HTTP role User enforcing formatting, situational digital feeds (【 LIVE FEED 】, ❤️Pack-Family❤️), and strict Italian output.
3. Synthesize the exact text / JSON configuration for "Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)".

BOUNDARIES:
- Read-only investigation. Do NOT modify project files.
- Write your comprehensive findings to e:\repository\SvartulfrVerse\.agents\teamwork\explorer_gm_2\analysis.md and a structured handoff.md.
- Signal completion back to parent via send_message with handoff path.
