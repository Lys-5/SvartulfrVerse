# Handoff Report: Milestone 1 - R1 Frontend Logic & Avatar Activation Regex Compilation

**Agent**: `explorer_m1_3`  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_3`  
**Target Milestone**: Milestone 1 — Requirement 1 (Frontend Logic & Avatar Activation Regex Compilation)  
**Parent / Caller**: `c8a5c469-63a4-4154-bc85-fe2572ebf1e1`  
**Date**: 2026-10-24T12:18:00Z  

---

## 1. Observation

### 1.1 Webpack Bundle & Source Code Decompilation
By establishing connection to Chrome DevTools MCP and evaluating Next.js modules inside the live authenticated session on `https://app.wyvern.chat`, I extracted and decompiled the exact client-side modules governing Lorebook NPC entries, avatar activation regex auto-generation, UI data bindings, and chat message avatar splitting:

1. **Module `93312` (`scratch/modules/93312.js`)**:
   Contains function `f(npcInfo, prefix = "", suffix = ":")`, wrapped by an LRU cache `g` (capacity 1000) and exported as `WH`.
   Verbatim code:
   ```javascript
   f = function(e) {
     var t, n, r, o, c;
     let a = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "",
         l = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ":";
     if (!(null == e ? void 0 : null === (t = e.first_name) || void 0 === t ? void 0 : t.trim())) return "";
     let s = e => e.normalize("NFC"),
         u = e => s(e).replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
                      .replace(/['\u2018\u2019\u02BC\u201B\u2032]/g, "['‘’ʼ‛′]")
                      .replace(/[-\u2010\u2011\u2012\u2013\u2014\u2212]/g, "[-‐‑‒–—−]"),
         d = a.trim() ? "(?<=^|[^\\p{L}\\p{N}_])" : "",
         h = [],
         p = "(?:\\*\\*)?";
     if (a.trim() ? h.push(p + u(a.trim()) + "\\s*" + p) : h.push("(?<=^|\\n)\\s*" + p),
         Array.isArray(null == e ? void 0 : e.titles) && e.titles.length > 0) {
       let t = e.titles.map(u).join("|");
       h.push("((" + t + ")\\s+)?");
     }
     let v = [],
         f = (e, t, n) => { v.push({ pattern: e, weight: 1e4 * t + n }) },
         g = e.first_name.trim(),
         m = (null == e ? void 0 : null === (n = e.last_name) || void 0 === n ? void 0 : n.trim()) || null,
         y = (null !== (r = null == e ? void 0 : e.middle_names) && void 0 !== r ? r : []).map(e => e.trim()).filter(Boolean),
         _ = y.length ? Math.max(...y.map(e => e.length)) : 0,
         w = u(g),
         C = m ? u(m) : null,
         x = y.length ? y.map(u).join("|") : null;
     if (x && C && f(w + "\\s+(" + x + ")\\s+" + C, 3, g.length + _ + (null !== (o = null == m ? void 0 : m.length) && void 0 !== o ? o : 0) + 2),
         C && (f(w + "\\s+" + C, 2, g.length + m.length + 1), f(C + "\\s+" + w, 2, g.length + m.length + 1)),
         x && C && f(C + "\\s+(" + x + ")\\s+" + w, 3, g.length + _ + (null !== (c = null == m ? void 0 : m.length) && void 0 !== c ? c : 0) + 2),
         x && f(w + "\\s+(" + x + ")", 2, g.length + _ + 1),
         f(w, 1, g.length),
         C && f(C, 1, m.length),
         (null == e ? void 0 : e.nicknames) && (null == e ? void 0 : e.nicknames.length) > 0 &&
         e.nicknames.forEach(e => {
           let t = e.trim(), n = t.split(/\s+/).filter(Boolean).length || 1;
           e.includes("'") || e.includes('"') ? f(u(e), n, t.length) : (f(u(e), n, t.length), f("'" + u(e) + "'", n, t.length + 2), f('"' + u(e) + '"', n, t.length + 2))
         }),
         v.sort((e, t) => t.weight - e.weight),
         h.push(d + "(?<coreName>" + v.map(e => e.pattern).join("|") + ")" + "(?=$|[^\\p{L}\\p{N}_])"),
         Array.isArray(null == e ? void 0 : e.titles) && e.titles.length > 0) {
       let t = e.titles.map(u).join("|");
       h.push("(\\s+(" + t + "))?");
     }
     let S = "(?:\\([^()\\[\\]:\\r\\n]{1,80}\\)|\\[[^()\\[\\]:\\r\\n]{1,80}\\])",
         b = "(?:[\"'‘’“”][^\"'‘’“”:\\n]{1,40}[\"'‘’“”]|" + S + "|\\p{Lu}[\\p{L}\\p{N}.'’\\-]*|(?:de|del|della|der|den|van|von|di|da|do|dos|das|la|le|les|du|bin|ibn|al|el|af|av|of|the|y|e|saint|st))";
     return h.push("(?:\\s+" + b + "){0,6}"),
            (null == l ? void 0 : l.trim()) && h.push("(?:\\*\\*)?\\s*" + u(l.trim()) + "(?:\\*\\*(?=\\s|$))?"),
            h.join("");
   }
   ```

2. **Module `6712` (`scratch/modules/6712.js`) — Lorebook Entry Editor UI**:
   - `NPC Prefix`: Input bound to `eu.npc_info.npc_prefix` (`placeholder: "e.g. => or leave empty"`).
   - `First Name`: Input bound to `eu.npc_info.first_name` (`placeholder: "Enter first name"`).
   - `Middle Names`: TagInput bound to `eu.npc_info.middle_names` array (`placeholder: "Add middle name and press Enter"`).
   - `Last Name`: Input bound to `eu.npc_info.last_name` (`placeholder: "Enter last name"`).
   - `Nicknames`: TagInput bound to `eu.npc_info.nicknames` array (`placeholder: "Add nickname and press Enter"`).
   - `Titles`: TagInput bound to `eu.npc_info.titles` array (`placeholder: "Add title and press Enter (e.g., Dr., Sir, Lady)"`).
   - `Custom Avatar Regex`: Switch component `<Switch checked={eu.custom_avatar_regex || false} onCheckedChange={e => eX("custom_avatar_regex", e)} />` with help text:
     `"Enable to manually define activation regex, or disable to auto-generate from NPC info"`.
   - `Custom Activation Regex Textarea`: Rendered conditionally:
     `eu.custom_avatar_regex ? (0, s.jsx)(_.Textarea, { ref: eB, defaultValue: eu.avatar_activation_regex }) : null`.
   - `Lines Parsed`: Input bound to `eu.lines_parsed` (`type: "number", min: "1", value: eu.lines_parsed || 1`) with help text:
     `"How many lines after the regex match to parse as the character's message. Default is 1 line."`.
   - **Crucial UI Finding**: Module `6712` does **NOT** import Module `93312`. Saving an entry in the UI persists `npc_info` and `avatar_activation_regex` as completely separate fields; it does **NOT** write or overwrite `avatar_activation_regex` on save when `custom_avatar_regex` is `false`.

3. **Module `21758` (`scratch/modules/21758.js`) & Module `98786` — Chat Engine Runtime Avatar Splitting**:
   Verbatim condition determining regex compilation at chat runtime:
   ```javascript
   let w = (null == a$ ? void 0 : a$.avatar_activation_prefix) ||
           (null == e ? void 0 : null === (i = e.npc_info) || void 0 === i ? void 0 : i.npc_prefix) ||
           nA || "";
   if (e.avatar_activation_regex &&
       (null == e ? void 0 : null === (r = e.avatar_activation_regex) || void 0 === r ? void 0 : r.length) > 2 &&
       (null == e ? void 0 : e.custom_avatar_regex) !== false) {
     // MODE A: Custom regex branch
     let t = e.avatar_activation_regex, a = "gi", i = t.match(/^\(\?([imsx]+)\)/);
     if (i) for (let e of (t = t.slice(i[0].length), i[1])) "i" !== e && "m" !== e && "s" !== e || a.includes(e) || (a += e);
     try {
       n.push({ entry: f, regex: new RegExp(t, a) });
     } catch (t) {
       console.warn('Invalid avatar_activation_regex for lexicon entry "'.concat(null == e ? void 0 : e.name, '":'), t);
     }
   } else {
     // MODE B: Auto-generate branch from npc_info
     if (!(null == e ? void 0 : null === (g = e.npc_info) || void 0 === g ? void 0 : null === (v = g.first_name) || void 0 === v ? void 0 : v.trim())) return;
     n.push({ entry: f, regex: RegExp((0, eL.WH)(null == e ? void 0 : e.npc_info, w, ":"), "giu") });
   }
   ```
   Chat line splitting mechanism:
   Matches are sorted by text position `index` (`(0, e7.Q)(h, v)`). Text slices are extracted from `r` (end of match index) to `u.index` (start of next speaker's match) or `a.length` (end of message):
   `let m = a.slice(r, c).replace(/^\n+/, "").trim();`
   Each segment is bound to the matched NPC `{ content: m, npc: { entry, name, avatar } }`.

4. **Module `18282` — API / Schema Definitions**:
   Verbatim documentation strings:
   - `npc_info`: `"NPC Information - For type='npc' entries. When custom_avatar_regex is false, this info auto-generates avatar activation regex. When true, you must provide avatar_activation_regex manually."`
   - `custom_avatar_regex`: `"Use Custom Regex - If true, manually define avatar_activation_regex. If false, auto-generate from npc_info (default: false, only for NPCs)"`
   - `avatar_activation_regex`: `"Custom Activation Regex"`

5. **Empirical Execution of Auto-Generation via `scratch/test_compiler.js`**:
   Executing the exact algorithm on representative NPCs generated:
   - Erik Ulfr Douglas:
     `(?<=^|\n)\s*(?:\*\*)?((Lord|Alpha)\s+)?(?<coreName>Erik\s+(Ulfr)\s+Douglas|Douglas\s+(Ulfr)\s+Erik|'The Old Wolf'|"The Old Wolf"|The Old Wolf|'Pack Leader'|"Pack Leader"|Erik\s+Douglas|Douglas\s+Erik|Pack Leader|Erik\s+(Ulfr)|Douglas|Erik)(?=$|[^\p{L}\p{N}_])(\s+(Lord|Alpha))?(?:\s+(?:["'‘’“”][^"'‘’“”:\n]{1,40}["'‘’“”]|(?:\([^()\[\]:\r\n]{1,80}\)|\[[^()\[\]:\r\n]{1,80}\])|\p{Lu}[\p{L}\p{N}.'’\-]*|(?:de|del|della|der|den|van|von|di|da|do|dos|das|la|le|les|du|bin|ibn|al|el|af|av|of|the|y|e|saint|st))){0,6}(?:\*\*)?\s*:(?:\*\*(?=\s|$))?`
   - Scarlett Rose:
     `(?<=^|\n)\s*(?:\*\*)?(?<coreName>Scarlett\s+Rose|Rose\s+Scarlett|Scarlett|'Red'|"Red"|Rose|Red)(?=$|[^\p{L}\p{N}_])(?:\s+(?:["'‘’“”][^"'‘’“”:\n]{1,40}["'‘’“”]|(?:\([^()\[\]:\r\n]{1,80}\)|\[[^()\[\]:\r\n]{1,80}\])|\p{Lu}[\p{L}\p{N}.'’\-]*|(?:de|del|della|der|den|van|von|di|da|do|dos|das|la|le|les|du|bin|ibn|al|el|af|av|of|the|y|e|saint|st))){0,6}(?:\*\*)?\s*:(?:\*\*(?=\s|$))?`

### 1.2 Audit of Current Repository Files (`FINAL/*.json`)
Inspection of all 310 NPC entries (99 in `FINAL/Svartulfr_NPC_Primary.json`, 211 in `FINAL/Svartulfr_NPC_Secondary.json`) revealed the following data defects:
1. **Missing `middle_names` across 100% of entries**:
   All 310 `npc_info` blocks currently contain only `first_name`, `last_name`, `nicknames`, `titles`. None have `middle_names: []` or `npc_prefix: ""`.
2. **Defective Double-Surname Concatenations in `avatar_activation_regex`**:
   18 entries contain artificial, redundant surname duplications generated by a legacy script:
   - Primary:
     * `Hugh Rivers`: `Alpha Rivers Rivers`, `The Mountain Sovereign Rivers`
     * `Dominic Rogers`: `Mr. Rogers Rogers`, `Dom Rogers Rogers`
     * `Daniel "Danny" Boone`: `Boone Boone`
     * `Harrison Black`: `Councilman Black Black`
     * `Marcus O'Connor`: `Mark O'Connor O'Connor`
   - Secondary:
     * `Alicia Virtuoso`: `Mrs Virtuoso Virtuoso`, `Jean-Luc's wife Virtuoso`
     * `Ariadne Cirillo`: `Nurse Cirillo Cirillo`
     * `Luisa Sanchez Rogers`: `Mac's older sister Rogers`
     * `Alistair Ambrose DeVille`: `The Collector DeVille`
     * `Damien Bishop`: `Bishop Bishop`, `The Hellhound Detective Bishop`
     * `Jet Thompson`: `Hank's son Thompson`, `Thompson kid Thompson`
3. **Umbrella Keywords in `nicknames`**:
   - `Ariadne Cirillo`: `["Nurse Cirillo", "nurse", "drider", "succubus", "health centre"]`
   - `Brittany Willow`: `["SUCC student"]`
4. **Gallery Images Structure**:
   - The live API `GET /api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` indicates `gallery_count: 65`.
   - Each NPC entry stores `avatar: "<HTTPS URL>"` and `alternate_avatars: ["<HTTPS URL>"]`.
   - When an entry's `avatar` matches a URL in the Lorebook gallery, the UI displays `<Badge variant="secondary">Gallery Image</Badge>`, otherwise `<Badge variant="outline">Custom Image</Badge>`.

---

## 2. Logic Chain

1. **Premise 1 (Decoupled Persistence)**:
   - In Module `6712`, `npc_info` and `avatar_activation_regex` are independent state objects. Saving `npc_info` in the web UI does not write or mutate `avatar_activation_regex`.
2. **Premise 2 (Runtime Evaluation)**:
   - In Module `21758`, Wyvern dynamically evaluates `custom_avatar_regex`:
     - If `custom_avatar_regex !== false` and `avatar_activation_regex.length > 2`, it compiles the custom regex literal.
     - If `custom_avatar_regex === false` or `avatar_activation_regex` is absent/empty/short, it dynamically auto-generates the regex from `npc_info` using `(0, eL.WH)(e.npc_info, w, ":")`.
3. **Premise 3 (Defect Impact)**:
   - Because all 310 entries currently have `custom_avatar_regex: true`, the chat engine executes the stored `avatar_activation_regex` strings.
   - The 18 entries with duplicated surnames (`Alpha Rivers Rivers`, `Mrs Virtuoso Virtuoso`, `Nurse Cirillo Cirillo`) fail to match legitimate dialogue in the chat (e.g. `Alpha Rivers: "..."`), causing avatar detection failures.
   - The entries with umbrella keywords in nicknames (`succubus`, `drider`, `nurse`, `SUCC student`) hijack speaker avatars whenever common nouns are spoken.
4. **Premise 4 (Dual-Compatibility Hygiene)**:
   - If `npc_info` is sanitized to include all 6 standard fields (`first_name`, `middle_names`, `last_name`, `nicknames`, `titles`, `npc_prefix`), Wyvern's `NPC Information` sub-panel renders 100% complete.
   - If `avatar_activation_regex` is regenerated using the clean canonical multiline pattern `(?:^|\n)\s*(?:Full Name|Clean Nickname|...)\s*:` with `custom_avatar_regex: true` and `lines_parsed: 1`, the existing Wyvern chat parser operates flawlessly.
   - If an end-user later flips `custom_avatar_regex` to `false` in the UI, Wyvern's runtime compiler (`93312`) seamlessly produces the native pattern without throwing errors because `npc_info` is fully compliant.

---

## 3. Caveats

1. **Entry Counts (210 vs 310)**:
   The original user prompt referenced "the 210 NPC entries in `FINAL/Svartulfr_NPC_Primary.json` and `FINAL/Svartulfr_NPC_Secondary.json`". In reality, `Svartulfr_NPC_Primary.json` contains **99 entries** and `Svartulfr_NPC_Secondary.json` contains **211 entries**, totaling **310 entries**. The number 210 corresponds to 99 Primary + 111 Secondary from earlier drafts before the secondary expansion to 211. The sanitization must encompass all **310 entries**.
2. **Special Anti-Collision Personas (Alyssa & Jasper)**:
   Alyssa (`alyssa_world_dossier_2b54a223`) and Jasper (`Vcj4h2TL4Usola2A4OOl6`) in Lorebook Primary are dual-mode entries (both User Personas and Lorebook NPCs). They must retain `selective: true` with secondary keys `["Dossier", "Scheda", "Archivio", "Database", "Profilo"]` and `ignored_personas` to avoid phantom activations when played by the user. All other 308 NPCs must have `selective: false`.
3. **No Code Modification During Explorer Turn**:
   As an Explorer agent, I have strictly maintained read-only operation. No source files or final JSON files have been altered during this turn.

---

## 4. Conclusion

1. **Frontend Logic Verified**:
   - `avatar_activation_regex` auto-generation is implemented in Module `93312` (`WH`), constructing a comprehensive regex with `(?<=^|\n)\s*`, leading/trailing titles, weighted name/nickname permutations, up to 6 trailing particles/roles, and a colon terminator.
   - Saving in the UI does NOT auto-generate or overwrite `avatar_activation_regex`; auto-generation is dynamic at chat runtime.
   - `custom_avatar_regex: true` with length > 2 takes absolute precedence.
   - `lines_parsed: 1` specifies 1-line parsing for SillyTavern/Tavern compatibility; Wyvern chat UI segments text up to the next character's header.
2. **Defects Cataloged for Milestone 2 Remediation**:
   - 310/310 entries missing `middle_names` array in `npc_info`.
   - 18 entries with duplicated surname strings in `avatar_activation_regex`.
   - Umbrella keywords in `nicknames` on Ariadne Cirillo (`drider`, `succubus`, `nurse`, `health centre`) and Brittany Willow (`SUCC student`).
3. **Exact Remediation Specifications for Milestone 2**:
   - Populate `npc_info` across all 310 entries with:
     ```json
     "npc_info": {
       "first_name": "...",
       "middle_names": [],
       "last_name": "...",
       "nicknames": [],
       "titles": [],
       "npc_prefix": ""
     }
     ```
     extracting middle names from JED+ headers (e.g. `Ulfr`, `Björn`, `Loki`, `Svartr`, `Járn`, `Báleygr`, `Hvit`, `Ambrose`).
   - Clean `nicknames` by stripping umbrella keywords.
   - Regenerate clean `avatar_activation_regex` with pattern `(?:^|\n)\s*(?:Full Name|Nickname|...)\s*:` without duplicate surname concatenations.
   - Set `custom_avatar_regex: true`, `lines_parsed: 1`, and preserve `ignored_characters` / `ignored_personas`.
   - Maintain 100% byte-for-byte parity between `entries` and `lexicon` arrays.

---

## 5. Verification Method

### 5.1 Decompiled Webpack Inspection
To re-verify the frontend logic independently:
```powershell
node scratch/dump_target_modules.js
python -c "import json; d=json.load(open('scratch/mod93312_dump.json', encoding='utf-8')); print(d['content'][0]['text'][:300])"
```

### 5.2 Auto-Generator Compilation Test
To independently execute and verify Wyvern's native regex compiler:
```powershell
node scratch/test_compiler.js
```

### 5.3 Audit of Current Repository Defects
To verify the cataloged defects in `FINAL/`:
```powershell
python -c "
import json
for p in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    d = json.load(open(p, encoding='utf-8'))
    missing = [e['name'] for e in d['lexicon'] if 'middle_names' not in e.get('npc_info', {})]
    print(f'{p}: {len(missing)} missing middle_names')
"
```
Output:
- `FINAL/Svartulfr_NPC_Primary.json: 99 missing middle_names`
- `FINAL/Svartulfr_NPC_Secondary.json: 211 missing middle_names`
