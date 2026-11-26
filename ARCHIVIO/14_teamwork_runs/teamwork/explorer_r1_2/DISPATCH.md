# Dispatch for Explorer 2 (Milestone R1)

- **Role**: Pillar 1 & 2 Investigator
- **Working Directory**: e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r1_2
- **Project Root**: e:\repository\SvartulfrVerse
- **Authoritative Request**: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
- **Project Scope**: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_1\PROJECT.md

## Objective
Investigate Pillar 1 and Pillar 2 across all 6 standalone lorebooks in `FINAL/`:
1. **Pillar 1: Spurious Metadata on Non-NPCs**:
   - Inspect all non-NPC entries across all 6 lorebooks (Location, Lorebooks I, II, III, and any non-NPC entries).
   - Identify entries containing `npc_info`, `custom_avatar_regex`, `lines_parsed`, or other NPC-specific fields.
   - List exact counts and sample entries by lorebook.
2. **Pillar 2: Umbrella Keywords (BROAD_KEYS) on NPCs**:
   - Inspect all NPC entries across all 6 lorebooks (especially NPC Primary and NPC Secondary).
   - Check for umbrella keywords: `solarton`, `succ`, `blackwood`, `vampire`, `werewolf`, `college`, `student`, `alpha`, `omega` (case-insensitive) in `keys` / primary keys.
   - Check `selective` setting and `secondary_keys`.
   - List exact counts and sample occurrences.
3. Recommend exact remediation rules and patterns for the Worker.
4. Deliver a structured investigation report in `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r1_2\handoff.md`.


## 2026-10-16T21:48:34Z
[Message from 5c61ad50-aa94-4b67-ad53-492fd2f90e52]
Investigate Pillar 1 and Pillar 2 across all 6 standalone lorebooks in FINAL/:
1. Pillar 1: Spurious NPC metadata (npc_info, custom_avatar_regex, lines_parsed, etc.) on non-NPC entries (locations, concepts, factions, items). Check all 6 files, count violations, and provide examples.
2. Pillar 2: Umbrella keywords (BROAD_KEYS: solarton, succ, blackwood, vampire, werewolf, college, student, alpha, omega) on NPC entries. Check keys/triggers, count violations, and examine selective/secondary_keys usage.
3. Recommend exact remediation rules and patterns for the Worker.
4. Write your comprehensive report in e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r1_2\handoff.md.
5. When finished, send a completion message to the parent orchestrator (conversation ID 5c61ad50-aa94-4b67-ad53-492fd2f90e52) with summary and report path.
