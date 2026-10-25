# Adversarial Review & Handoff Report: Milestone 3

**Reviewer**: reviewer_m3_2 (Adversarial Critic & Quality Reviewer)  
**Milestone**: Milestone 3 — Display Settings & Right Sidebar Flags  
**Final Verdict**: `REQUEST_CHANGES`

---

## 1. Observation

### 1.1 Chunk 14685 Schema `$` vs Deployed `chat_overrides`
1. In `scratch/14685-a6f37bf36e7cf713.js` (lines 60195–60600), the Display Settings schema `$` is defined as:
   ```javascript
   $ = V.z.object({
     version: V.z.literal(1),
     values: V.z.object({
       use_reply_options: V.z.boolean(),
       reply_options_instructions: V.z.string(),
       use_impersonate_override: V.z.boolean(),
       impersonate_prompt: V.z.string(),
       immersiveMode: V.z.boolean(),
       vnMode: V.z.boolean(),
       spriteLocation: V.z.enum(["left", "right", "center"]),
       spriteSize: V.z.number().finite(),
       disableSprites: V.z.boolean(),
       useSpriteAsAvatar: V.z.boolean(),
       showBackgroundOverlay: V.z.boolean(),
       backgroundOverlayColor: V.z.string(),
       disableBlur: V.z.boolean(),
       hideThinkBlocks: V.z.boolean(),
       showLiveReasoning: V.z.boolean(),
       reasoningAutoScroll: V.z.boolean(),
       reasoningPosition: V.z.enum(Y.ch),
       musicPlayerEnabled: V.z.boolean(),
       musicPlayerAutoplay: V.z.boolean(),
       messageLayout: V.z.enum(Y.Yj),
       experimentalVariant: V.z.enum(Y.qv),
       experimentalAvatarPosition: V.z.enum(Y.YX),
       experimentalInlineAvatar: V.z.boolean(),
       experimentalDisableAvatarFade: V.z.boolean(),
       showAvatars: V.z.boolean(),
       avatarShape: V.z.enum(Y.Vi),
       avatarSize: V.z.enum(Y.DV),
       hideAvatarBorder: V.z.boolean(),
       borderStyle: V.z.string(),
       textAdventureActionPrefix: V.z.string(),
       textAdventureShowDividers: V.z.boolean(),
       font: V.z.string(),
       textAlignment: V.z.enum(Y.aj),
       showUsernames: V.z.boolean(),
       showModelName: V.z.boolean(),
       enableEntryHighlighting: V.z.boolean(),
       character_final_instructions: V.z.boolean(),
       theme_id: V.z.string()
     }).partial(),
     notes: V.z.record(V.z.string())
   });
   ```
   Schema `$` defines exactly **38 valid keys** in `values`. Under the Visual Novel mode section, the **only** defined property is `vnMode: V.z.boolean()`.

2. In `scratch/14685-a6f37bf36e7cf713.js` (lines 155717–156350), the frontend form sanitization logic enforces:
   ```javascript
   u = o ? function(e) {
     var t;
     let a = {}, s = {};
     for (let [t, s] of Object.entries(e.values))
       (0, Y.IM)(t) && Object.assign(a, { [t]: s });
     for (let [a, r] of Object.entries(null !== (t = e.notes) && void 0 !== t ? t : {}))
       (0, Y.IM)(a) && Object.assign(s, { [a]: r });
     return { version: 1, values: a, notes: s };
   }(o) : void 0;
   ```
   The validator `(0, Y.IM)(t)` evaluates keys against the 38 registered schema fields. Any key not in the 38 registered keys is stripped during client-side serialization.

3. In `scripts/configure_display_settings_and_flags.py` (lines 50–64) and `tests/test_milestone3_display_settings.py` (lines 36–46), `worker_m3` deployed and asserted:
   ```python
   EXPECTED_VN_OVERRIDES = {
       "version": 1,
       "values": {
           "vnMode": True,
           "vnTextSpeed": "normal",
           "vnDirections": True,
           "vnAutoAdvance": False,
           "vnAutoDelayMs": 2500,
           "vnSkipRead": False,
           "vnTextboxOpacity": 0.85,
           "vnSpriteLimit": 3,
           "vnItalicAsThought": False
       },
       "notes": {}
   }
   ```
   Direct comparison confirms:
   - `vnMode`: Valid in schema `$`.
   - `vnTextSpeed`: **Extraneous. NOT in schema `$`**.
   - `vnDirections`: **Extraneous. NOT in schema `$`**.
   - `vnAutoAdvance`: **Extraneous. NOT in schema `$`**.
   - `vnAutoDelayMs`: **Extraneous. NOT in schema `$`**.
   - `vnSkipRead`: **Extraneous. NOT in schema `$`**.
   - `vnTextboxOpacity`: **Extraneous. NOT in schema `$`**.
   - `vnSpriteLimit`: **Extraneous. NOT in schema `$`**.
   - `vnItalicAsThought`: **Extraneous. NOT in schema `$`**.

4. In `scratch/19010-2f567930ecf4f745.js` (module 98043, offset 331900), the 8 extraneous fields originate from the client-side local React UI state array:
   ```javascript
   let u = ["vnMode", "vnTextSpeed", "vnAutoAdvance", "vnAutoDelayMs", "vnSkipRead", "vnTextboxOpacity", "vnDirections", "vnSpriteLimit", "vnItalicAsThought"];
   ```
   These represent in-browser display preferences for the upcoming VN player, not server-persisted schema `$` fields.

5. In `GET https://app.wyvern.chat/api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN`:
   - Top-level `chat_overrides` evaluates to `None`.
   - The overrides payload was persisted solely inside `memory.chat_overrides`.
   - In `scratch/19010-2f567930ecf4f745.js` line 238653, the client inspects `t.chatLog.chat_overrides` (which is `None`), but Visual Novel mode falls back to `world.world_features.vn_mode: true` via chunk 81904 offset 296305 (`function o(e, t) { return "boolean" == typeof e ? e : (null == t ? void 0 : t.vn_mode) === !0; }`).

### 1.2 Right Sidebar Flags Audit
Direct API query on `https://app.wyvern.chat/api/new/chat-logs/chat_log_PJx1W1rg3WUzRM7MnQrkN`:
- `party_tied`: `True`.
- `memory.scene_summaries.auto_enabled`: `True`.
- `memory.scene_summaries.replace_enabled`: `True`.
- `memory.scene_summaries.dynamic_enabled`: `True`.
- `memory.scene_summaries.auto_approve`: `False` (CRITICAL: prevents unprompted AI overwrites).
- `memory.scene_summaries.tail_n`: `12` (preserves the last 12 messages from replacement).
- `memory.memory_scan.auto_approve`: `False` (AI content creation OFF).

Direct API query on `https://app.wyvern.chat/api/worlds/_YpX47fNraQFw2dD7TdycJ`:
- `enable_ai_tool_creation`: `False` (AI content creation OFF).
- `world_features.creature_catcher`: `False`.
- `world_features.ships`: `False`.
- `world_features.vn_mode`: `True`.
- `world_features.rpg_stats`: `True`.
- `world_features.combat`: `True`.
- `world_features.show_party_stats`: `True`.

### 1.3 Stats Tab Character Sheets Readiness Audit
Direct API query on `https://app.wyvern.chat/api/worlds/characters/world/_YpX47fNraQFw2dD7TdycJ`:
- Exactly 13 Primary World Characters returned.
- 13/13 have `rpg_stats.enabled: True`.
- 13/13 have levels between 1 and 99 (Wulfnic: 99, Zefir: 99, Erik: 55, Logan: 49, Malachia: 28, Noah: 25, Scarlett: 20, Alyssa: 19, Jasper: 19, Mackenzie: 19, Finnegan: 19, Sierra: 18, Edric: 13).
- 13/13 have 25-point 6-stat base stat sums equal to exactly 31.
- Zero zeroed attributes: every single stat (`might`, `resilience`, `agility`, `wit`, `presence`, `scouting`) has a non-zero positive integer value between 1 and 9.
- 13/13 have valid Cloudflare CDN avatars (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/...`).
- Live HTTP HEAD requests confirmed **13/13 avatar URLs return HTTP 200 OK**.

### 1.4 Automated Test Suite Execution
- `python -m unittest tests/test_milestone3_display_settings.py`: 16/16 passed in 2.854s.
- `python scripts/configure_display_settings_and_flags.py --verify-only`: exited with code 0.
- `python -m unittest discover tests`: 207/207 passed in 15.834s.
- Formatting discipline: exactly 0 em-dashes across all files.

---

## 2. Logic Chain

1. **Schema Non-Conformance (Observation 1.1)**:
   - Chunk 14685 formally defines schema `$` for `chat_overrides`.
   - Schema `$` allows exactly 38 keys in `values`, of which `vnMode` is the only VN-related key.
   - `worker_m3` populated `chat_overrides.values` with 8 extraneous keys (`vnTextSpeed`, `vnDirections`, `vnAutoAdvance`, `vnAutoDelayMs`, `vnSkipRead`, `vnTextboxOpacity`, `vnSpriteLimit`, `vnItalicAsThought`).
   - Although Zod does not fail on unrecognized keys by default when parsing, frontend chunk 14685 applies `(0, Y.IM)(t)` which explicitly filters out any key not registered in the schema.
   - Therefore, `chat_overrides` does not conform strictly to schema `$` without extraneous unvalidated fields.

2. **Self-Certifying Test Hazard (Observation 1.1, 1.4)**:
   - In `test_milestone3_display_settings.py`, `test_02_vn_display_settings_values` asserted that `chat_overrides` matched `EXPECTED_VN_VALUES`.
   - `EXPECTED_VN_VALUES` was hardcoded to mirror the 8 extraneous fields rather than checking against schema `$`.
   - This represents self-certifying verification where the test certifies the implementation against its own assumptions rather than the actual frontend contract.

3. **Sidebar Flags and Character Sheets (Observations 1.2, 1.3)**:
   - `scene/party auto-apply` is guaranteed by `party_tied: true` and `scene_summaries.auto_enabled: true`, while unprompted overwrites are strictly blocked by `auto_approve: false` and `tail_n: 12`.
   - `AI content creation` is guaranteed OFF by `memory_scan.auto_approve: false` and `world.enable_ai_tool_creation: false`.
   - Character sheets are 100% ready to render in the Stats tab with no missing portraits (13/13 HTTP 200) and no zeroed attributes.

---

## 3. Caveats

1. **VN Mode Runtime Impact**:
   The presence of the 8 extraneous fields does not break VN mode in the browser because Wyvern falls back to `world.world_features.vn_mode: true` (chunk 81904). However, keeping extraneous unvalidated fields violates the clean contract requirement of Milestone 3 and creates drift between client expectations and backend persistence.
2. **Top-Level `chat_overrides` Persistence**:
   The backend MongoDB `ChatLog` model does not expose a schema path for top-level `chat_overrides`. Embedding in `memory.chat_overrides` is currently the only way it persists on `ChatLog`, but this is distinct from Character-level `metadata.chat_overrides`.

---

## 4. Conclusion & Required Actions

**Verdict**: `REQUEST_CHANGES`

### Finding 1: [Major] Extraneous Unvalidated Fields in `chat_overrides`
- **Location**: `scripts/configure_display_settings_and_flags.py` (lines 50–64), `tests/test_milestone3_display_settings.py` (lines 36–46), and live chat `chat_log_PJx1W1rg3WUzRM7MnQrkN`.
- **Issue**: `chat_overrides.values` contains 8 extraneous keys (`vnTextSpeed`, `vnDirections`, `vnAutoAdvance`, `vnAutoDelayMs`, `vnSkipRead`, `vnTextboxOpacity`, `vnSpriteLimit`, `vnItalicAsThought`) that are not present in schema `$` of chunk 14685.
- **Remediation**:
  1. In `scripts/configure_display_settings_and_flags.py`, update `EXPECTED_VN_OVERRIDES` so that `values` contains strictly validated schema `$` fields:
     ```python
     EXPECTED_VN_OVERRIDES = {
         "version": 1,
         "values": {
             "vnMode": True
         },
         "notes": {}
     }
     ```
  2. Deploy the cleaned payload to `chat_log_PJx1W1rg3WUzRM7MnQrkN` via PUT.
  3. In `tests/test_milestone3_display_settings.py`, update `EXPECTED_VN_VALUES` to `{"vnMode": True}` and add a test asserting that zero extraneous unvalidated keys exist in `chat_overrides.values`.
  4. Regenerate `scratch/m3_display_settings_and_flags_verified.json`.

---

## 5. Verification Method

1. **Verify Strict Schema Conformance:**
   ```bash
   python -c "
   import json
   from pathlib import Path
   snap = json.loads(Path('scratch/m3_display_settings_and_flags_verified.json').read_text(encoding='utf-8'))
   vals = snap['chat_overrides']['values']
   # 38 registered keys in chunk 14685 schema $
   ALLOWED = {'use_reply_options', 'reply_options_instructions', 'use_impersonate_override', 'impersonate_prompt', 'immersiveMode', 'vnMode', 'spriteLocation', 'spriteSize', 'disableSprites', 'useSpriteAsAvatar', 'showBackgroundOverlay', 'backgroundOverlayColor', 'disableBlur', 'hideThinkBlocks', 'showLiveReasoning', 'reasoningAutoScroll', 'reasoningPosition', 'musicPlayerEnabled', 'musicPlayerAutoplay', 'messageLayout', 'experimentalVariant', 'experimentalAvatarPosition', 'experimentalInlineAvatar', 'experimentalDisableAvatarFade', 'showAvatars', 'avatarShape', 'avatarSize', 'hideAvatarBorder', 'borderStyle', 'textAdventureActionPrefix', 'textAdventureShowDividers', 'font', 'textAlignment', 'showUsernames', 'showModelName', 'enableEntryHighlighting', 'character_final_instructions', 'theme_id'}
   extraneous = set(vals.keys()) - ALLOWED
   assert not extraneous, f'Extraneous keys found: {extraneous}'
   print('Strict schema $ conformance: PASS')
   "
   ```

2. **Verify Live Cloud Flags:**
   ```bash
   python scripts/configure_display_settings_and_flags.py --verify-only
   ```

3. **Verify All Tests:**
   ```bash
   python -m unittest tests/test_milestone3_display_settings.py
   python -m unittest discover tests
   ```
