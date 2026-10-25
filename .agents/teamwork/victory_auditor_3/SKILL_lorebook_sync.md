# Wyvern Card & Lorebook Native Suppression Sync (Local Skill Copy)

Pipeline modulare per la sincronizzazione card/lorebook/scenari su Wyvern:
soppressione nativa anti-collisione ("Don't Activate When Active" via ignored_characters e ignored_personas),
conversione di Character Card in NPC completi nei Lorebook, bonifica slot inaccessibili (unavailable_count: 0)
e deployment sicuro via Web API.

Key Rules:
1. Native suppression: `ignored_characters` & `ignored_personas` with `selective: false`.
2. JED+ completeness (>2000 chars, no em-dash, dialogs in quotes, plain text narration).
3. Slot sanitization: `pool: []`, `unavailable_count: 0`, preserve slot objects for `speaker_slot` resolution.
4. Macro replacement: replaced with literal names for retired cards.
5. Invariant: `greeting.speaker_slot == messages[0].speaker_slot` and `greeting.content == messages[0].content`.
6. Live API verification: HTTP 200 on GET, 8 characters in `/characters/mine`, 404 on deleted cards.
