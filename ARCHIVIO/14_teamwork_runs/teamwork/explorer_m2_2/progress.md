# Progress — explorer_m2_2

- Last visited: 2026-10-24T11:24:00Z
- Status: Investigation Completed — Drafting Handoff Report
- Current task: Writing handoff.md with comprehensive findings across all 211 entries
- Key findings summary:
  1. All 211 entries currently have incomplete `npc_info` (0/211 valid per new contract, missing `middle_names: []` and `npc_prefix: None`).
  2. Identified exactly 102 entries with middle names (100 Camp Mystic + Luisa Sanchez Rogers + Alistair Ambrose DeVille).
  3. Identified 110 entries with titles (80 Campers, 20 Counselors, 3 Professors, 2 Coaches, 5 Faction/Rank titles).
  4. Cataloged the 10 legacy duplicate surname entries in `avatar_activation_regex` and the root cause (naive nickname+last_name concatenation).
  5. Confirmed live sync difference: Wyvern live API has 209 entries vs local 211 entries (missing Finn the Satyr `quJQvjvUWQLUeOCNv2Wko` and Jasper Rowan `d1Qg6eRvuKC8iI5kNWPzb`).
  6. Verified anti-collision requirements: Edric Douglas `ignored_characters: ["_TbRM3EdxDjHFgqztTbCpL"]` must be preserved; all 211 entries must have `selective: false`; `demon` purged from Damien Bishop's secondary_keys.
