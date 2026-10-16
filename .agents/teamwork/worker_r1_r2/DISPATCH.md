# Dispatch for Worker 1 (Milestones R1 & R2)

- **Role**: Data Remediation & Backup Specialist
- **Working Directory**: e:\repository\SvartulfrVerse\.agents\teamwork\worker_r1_r2
- **Project Root**: e:\repository\SvartulfrVerse
- **Authoritative Request**: e:\repository\SvartulfrVerse\.agents\teamwork\ORIGINAL_REQUEST.md
- **Project Scope**: e:\repository\SvartulfrVerse\.agents\teamwork\orchestrator_1\PROJECT.md
- **Explorer Reports**:
  - `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r1_1\handoff.md`
  - `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r1_2\handoff.md`
  - `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_r1_3\handoff.md`

## File Ownership
- Exclusively owns:
  - `scratch/backup_pre_audit_lorebooks/*.json`
  - `scratch/missing_npc_avatars.json`
  - `FINAL/Svartulfr_Lorebook_I.json`
  - `FINAL/Svartulfr_Lorebook_II.json`
  - `FINAL/Svartulfr_Lorebook_III.json`
  - `FINAL/Svartulfr_Location.json`
  - `FINAL/Svartulfr_NPC_Primary.json`
  - `FINAL/Svartulfr_NPC_Secondary.json`
  - `lorebooks/optimized/*.json`

## Tasks & Instructions

### Step 1: Safety Backup (Milestone R1)
Before any modifications, create directory `scratch/backup_pre_audit_lorebooks/` and copy all 6 unmodified lorebook files from `FINAL/` into `scratch/backup_pre_audit_lorebooks/`:
- `Svartulfr_Lorebook_I.json`
- `Svartulfr_Lorebook_II.json`
- `Svartulfr_Lorebook_III.json`
- `Svartulfr_Location.json`
- `Svartulfr_NPC_Primary.json`
- `Svartulfr_NPC_Secondary.json`

### Step 2: Automated Remediation (Milestone R2)
Implement a robust, clean Python remediation script (e.g., in `scratch/remediate_lorebooks.py`) and execute it:

1. **Pillar 1: Purge Spurious Metadata on Non-NPC Entries**:
   - For all non-NPC entries across `FINAL/Svartulfr_Lorebook_I.json`, `Svartulfr_Lorebook_II.json`, `Svartulfr_Lorebook_III.json`, and `Svartulfr_Location.json`:
     - Delete `avatar_activation_regex` if present.
     - Delete `custom_avatar_regex`, `lines_parsed`, `npc_info` if present.
     - If `avatar == ""` (empty string), remove it from non-NPC entries (preserve valid URLs on the 18 decorative factions/locations).
   - In `FINAL/Svartulfr_Lorebook_III.json`:
     - Replace `entries` array with a deep copy of `lexicon` (so that all 35 entries share the uniform Wyvern schema and `entries == lexicon`).

2. **Pillar 2: Eliminate Umbrella Keywords & Generic Role Triggers on NPCs**:
   - On `FINAL/Svartulfr_NPC_Primary.json` and `FINAL/Svartulfr_NPC_Secondary.json`:
     - Remove `"Alpha"` from Malachia Björn Douglas Bloodmoon's `secondary_keys` (Entry #60 in Primary).
     - Prune generic multi-word umbrella trigger keys from primary `keys`:
       - `"SUCC student"` on Brittany Willow (#18 in Secondary).
       - `"Pack Leader"` on 11 Primary NPCs: Vito Marino #40, Naomi Black #57, Marcus O'Connor #59, Isobel Blackwater #71, Helena Weiss #73, Eclipse Noir #85, Dominic Chen #89, Darius Vale #90, Cass Harrow #93, Bianca Rossi #96, Aurora Night #100.
       - `"Blackwood Council"` on 4 Primary NPCs: Zeera Darkfire #38, Harlan Beaumont #75, Brak Ironfist #95, Barrow #97.
       - `"alligator demihuman"` on Cato (Secondary #7).
       - `"Demon Representative"` on Zeera Darkfire (Primary #38).
       - `"Human Representative"` on Harlan Beaumont (Primary #75).
     - Ensure proper names (e.g. `"Roman Blackwood"`, `"Katarina 'Kat' Blackwood"`) are NEVER stripped.
     - Ensure every NPC retains >=2 distinctive keys.
     - Ensure `selective: false` unless `secondary_keys` are populated.

3. **Pillar 3: Validate Zero `{{age}}` Macros**:
   - Assert 0 occurrences of `{{age}}` across all entries in all 6 files.

4. **Pillar 4: Avatar Fallback & Logging**:
   - For every NPC entry in `FINAL/Svartulfr_NPC_Primary.json` (44 missing) and `FINAL/Svartulfr_NPC_Secondary.json` (258 missing):
     - If `avatar` is empty `""`, set:
       `avatar = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"`
     - Retain `custom_avatar_regex: true`, `lines_parsed: 1`, and multiline regex.
   - Write comprehensive log of all 302 remediated NPCs to `scratch/missing_npc_avatars.json` matching the schema recommended in Explorer 3's handoff.

5. **Dual Array Synchronization**:
   - Apply every mutation identically to both `entries` and `lexicon` lists in each file.
   - Assert `entries == lexicon` for all 6 lorebooks.

6. **Repository Mirroring**:
   - Mirror all 6 remediated JSON files from `FINAL/` into `lorebooks/optimized/`.

### Step 3: Self-Verification
Execute a verification script testing all Acceptance Criteria:
- Non-NPCs contain 0 spurious fields (`avatar_activation_regex`, `npc_info`, `custom_avatar_regex`, `lines_parsed`).
- Zero BROAD_KEYS or banned generic role triggers on NPC primary `keys`.
- Zero `{{age}}` macros across all 6 files.
- 100% of NPCs have valid `avatar` (HTTP URL), `custom_avatar_regex: true`, `lines_parsed: 1`, and multiline regex.
- `entries` and `lexicon` are completely identical in length and content across all 6 lorebooks.
- `scratch/missing_npc_avatars.json` exists and logs exactly 302 entries.
- `lorebooks/optimized/` is completely synchronized with `FINAL/`.

### Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

### Deliverables
Write your comprehensive handoff report to:
`e:\repository\SvartulfrVerse\.agents\teamwork\worker_r1_r2\handoff.md`
Including Observation, Logic Chain, Caveats, Conclusion, and Verification Method.
Notify orchestrator when complete via send_message.
