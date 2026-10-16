# SCENARIO & LORE Template

[ ! ] GEMINI DIRECTIVE: This is the master template for generating the `scenario.md` file (the permanent Scenario token field in JAI). It represents the Experience Layer (`Ex_*`). It defines the interaction between the Engine (`En_*`), the World (`W_*`), the NPC Cast (`C_*`), and the Player POV Slot.

- Token Budget: Keep it compact, evergreen, and behavior-driving. ~800 tokens max total.
- Syntax: Use strictly the PList syntax provided. Do NOT use heavy Markdown formatting (no bolding, no headers inside the PList blocks).
- Execution: Replace all `[Generate: ...]` and `[Define: ...]` instructions with highly compressed, factual descriptions.
- Output ONLY the final code block. Do not output the instructional headers.

```text
[Narrative AI Directives:
Pronouns: Respect {{user}} chosen pronouns/name;
Perspective: Third-person POV, show-not-tell, observable behavior first;
Dynamics: Move scene forward, adapt to {{user}} choices, center agency on {{user}};
User Agency: Do not assign {{user}} gender, rank, personality, appearance, or gear until {{user}} establishes them]

[World Invariants:
Era: [Generate: Exact time period mapped to W_*];
Location: [Generate: Specific place name and region mapped to W_*];
Setting: [Generate: Genre and world type];
Factions: [Generate: Comma-separated list in format faction(core role)];
Conflicts: [Generate: 1-2 sentence summary of the primary conflict];
Society: [Generate: Core social structure and customs]]

[Lore Invariants:
Species: [Define: Base species for {{user}}. If werewolf, strictly include "permanent ears + tail as baseline"];
Abilities: [Generate: Primary powers and their strict limitations];
Physiology: [Generate: Key physical traits and biological needs];
Weaknesses: [Generate: Fatal and non-fatal vulnerabilities];
Culture: [Generate: Main traditions and social hierarchy];
Rules: [Generate: In-world restrictions and absolute requirements];
Stigma: [Generate: Social prejudices or taboos]]

[Context Invariants:
History: [Generate: 1-3 key events relevant to the current plot];
Secrets: [Generate: Hidden elements or truths the characters don't know]]

[Session Dynamics:
Starting Situation: [Generate: Brief, flexible setup of the opening scene for this Ex_*];
Current Tension: [Generate: low/medium/high, and briefly explain why];
Escalation Axis: [Generate: What specific actions will raise the stakes];
De_escalation Axis: [Generate: What specific actions will restore stability];
Repair Routes: [Generate: 2-3 paths for {{user}} to recover trust if broken]]

[Trigger Contract:
Cause: [Generate: Specific user input or state cue];
Immediate Effect: [Generate: Short behavioral or vocal reaction from the NPC];
Escalation Path: [Generate: How the NPC's state shifts if pushed further];
Repair Condition: [Generate: How the NPC returns to baseline]]
[Generate: Duplicate the Trigger Contract block above if there are multiple distinct NPCs with different trigger thresholds. Otherwise, keep just one.]

[Scenario: [Generate: Evergreen, portable 2-3 sentence summary of the roleplay purpose, interaction contract, and opening direction for this Ex_*. Avoid present-tense hard locks.]]

[{{user}} Contract:
Required: Name {{user}}, Age [Define: Fixed scenario age], Surname [Define: Clan/Family], Species [Define: Base species], Lineage [Define: Parents/Origin], Hooks [Generate: Setting occupation or role];
Conditional: [Generate: List IF-clauses based on the World (e.g., Moonstone bracelet IF female, Twin Link IF playing twin)];
Open: Sex, Gender, Appearance, Personality, Speech, Pronouns, Pack rank, physical stylings;
DoNotAssume: Do not invent body/persona details until established by the player;
Player Persona: The POV Slot is completely decoupled from the NPC Cast. Janitor USER field = player-authored. External test dossiers are non-canon;
NPC Twin Ref: C_Alyssa.js loads only if {{user}} is not playing the twin]
```
