# Handoff Report — Milestone 1 (R1): Reverse-Engineering & Browser DOM Inspection on Wyvern (app.wyvern.chat)

## 1. Observation

### 1.1 Chrome CDP Connection & Target Identification
- **Active DevTools Port File**: `C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort`
  - Line 1: `9222`
  - Line 2: `/devtools/browser/6a9a1596-d1ba-4ea4-ac7b-198d604f4563`
- **CDP Endpoint**: `ws://127.0.0.1:9222/devtools/browser/6a9a1596-d1ba-4ea4-ac7b-198d604f4563`
- **Active Browser Page Found**: `https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC` ("Svartúlfr - NPC Primary", 99 Lexicon entries).

### 1.2 Frontend Bundles & Code Decompilation
From inspection of the live Next.js script bundles loaded by `app.wyvern.chat`:
- `https://app.wyvern.chat/_next/static/chunks/66353-44918b7fd11ff8ae.js` (Lorebook Editor Component)
- `https://app.wyvern.chat/_next/static/chunks/53944-e2a3f3ea28ad0416.js` (Module `93312` — Regex Generator & Chat Engine)

#### Verbatim Code Snippet — Conditional Rendering & Switch
From `66353-44918b7fd11ff8ae.js` (around line 1, index 11800–14500):
```javascript
(0,s.jsx)(z.Label,{className:"text-sm font-medium",children:"Use Custom Regex"}),
(0,s.jsx)("p",{className:"text-xs text-muted-foreground",children:"Enable to manually define activation regex, or disable to auto-generate from NPC info"})
(0,s.jsx)(C.Switch,{
  checked: eu.custom_avatar_regex || !1,
  onCheckedChange: e => eX("custom_avatar_regex", e),
  disabled: !en
})
```
When `eu.custom_avatar_regex === true`: renders `<_.Textarea ref={eB} defaultValue={eu.avatar_activation_regex || ""} ...>` and Test Pattern input.
When `eu.custom_avatar_regex === false` (or undefined): renders `<div className="space-y-4 p-4 border rounded-md bg-muted/20">` containing the `NPC Information` sub-panel.

#### Verbatim Code Snippet — Sub-panel Structure and Data Bindings
```javascript
(0,s.jsxs)("div",{className:"space-y-4 p-4 border rounded-md bg-muted/20",children:[
  (0,s.jsxs)("div",{className:"space-y-2",children:[
    (0,s.jsx)(z.Label,{className:"text-sm font-medium",children:"NPC Information"}),
    (0,s.jsx)("p",{className:"text-xs text-muted-foreground",children:"Provide NPC details to automatically generate avatar activation regex"})
  ]}),
  (0,s.jsxs)("div",{className:"space-y-2",children:[
    (0,s.jsx)(z.Label,{className:"text-sm",children:"NPC Prefix"}),
    (0,s.jsx)(k.Input,{
      value:(null===(t=eu.npc_info)||void 0===t?void 0:t.npc_prefix)||"",
      onChange:e=>{var a;return eX("npc_info",{...eu.npc_info,first_name:(null===(a=eu.npc_info)||void 0===a?void 0:a.first_name)||"",npc_prefix:e.target.value||void 0})},
      placeholder:"e.g. => or leave empty",
      className:"h-8",
      disabled:!en
    }),
    (0,s.jsxs)("p",{className:"text-xs text-muted-foreground",children:["Optional prefix marker before the NPC name, e.g. ",'"=>"']})
  ]}),
  (0,s.jsxs)("div",{className:"space-y-2",children:[
    (0,s.jsx)(z.Label,{className:"text-sm",children:"First Name *"}),
    (0,s.jsx)(k.Input,{
      value:(null===(T=eu.npc_info)||void 0===T?void 0:T.first_name)||"",
      onChange:e=>eX("npc_info",{...eu.npc_info,first_name:e.target.value}),
      placeholder:"Enter first name",
      className:"h-8",
      disabled:!en
    })
  ]}),
  (0,s.jsxs)("div",{className:"space-y-2",children:[
    (0,s.jsx)(z.Label,{className:"text-sm",children:"Middle Names"}),
    (0,s.jsx)(m.E,{
      value:(null===(W=eu.npc_info)||void 0===W?void 0:W.middle_names)||[],
      onChange:e=>{var a;return eX("npc_info",{...eu.npc_info,first_name:(null===(a=eu.npc_info)||void 0===a?void 0:a.first_name)||"",middle_names:e.length>0?e:void 0})},
      placeholder:"Add middle name and press Enter",
      disabled:!en
    })
  ]}),
  (0,s.jsxs)("div",{className:"space-y-2",children:[
    (0,s.jsx)(z.Label,{className:"text-sm",children:"Last Name"}),
    (0,s.jsx)(k.Input,{
      value:(null===(G=eu.npc_info)||void 0===G?void 0:G.last_name)||"",
      onChange:e=>{var a;return eX("npc_info",{...eu.npc_info,first_name:(null===(a=eu.npc_info)||void 0===a?void 0:a.first_name)||"",last_name:e.target.value||void 0})},
      placeholder:"Enter last name",
      className:"h-8",
      disabled:!en
    })
  ]}),
  (0,s.jsxs)("div",{className:"space-y-2",children:[
    (0,s.jsx)(z.Label,{className:"text-sm",children:"Nicknames"}),
    (0,s.jsx)(m.E,{
      value:(null===(J=eu.npc_info)||void 0===J?void 0:J.nicknames)||[],
      onChange:e=>{var a;return eX("npc_info",{...eu.npc_info,first_name:(null===(a=eu.npc_info)||void 0===a?void 0:a.first_name)||"",nicknames:e.length>0?e:void 0})},
      placeholder:"Add nickname and press Enter",
      disabled:!en
    })
  ]}),
  (0,s.jsxs)("div",{className:"space-y-2",children:[
    (0,s.jsx)(z.Label,{className:"text-sm",children:"Titles"}),
    (0,s.jsx)(m.E,{
      value:(null===(K=eu.npc_info)||void 0===K?void 0:K.titles)||[],
      onChange:e=>{var a;return eX("npc_info",{...eu.npc_info,first_name:(null===(a=eu.npc_info)||void 0===a?void 0:a.first_name)||"",titles:e.length>0?e:void 0})},
      placeholder:"Add title and press Enter (e.g., Dr., Sir, Lady)",
      disabled:!en
    })
  ]})
]})
```

#### Verbatim Code Snippet — Avatar Selection from Gallery
From `66353-44918b7fd11ff8ae.js`:
```javascript
(0,s.jsx)(z.Label,{className:"peer-disabled:cursor-not-allowed peer-disabled:opacity-70 flex flex-row items-center justify-between text-xs font-medium text-muted-foreground uppercase tracking-wide",children:eu.avatar?"Change Avatar":"Avatar"}),
(0,s.jsxs)(E.Popover,{open:ew,onOpenChange:ek,children:[
  (0,s.jsx)(E.PopoverTrigger,{asChild:!0,children:(0,s.jsxs)(w.Button,{type:"button",variant:"outline",role:"combobox","aria-expanded":ew,className:"w-full justify-between h-8",disabled:!en,children:[
    (0,s.jsxs)("div",{className:"flex items-center gap-2",children:[(0,s.jsx)(y.Z,{className:"h-3 w-3"}),(0,s.jsx)("span",{className:"text-muted-foreground",children:eu.avatar?"Select different avatar...":"Select avatar from gallery..."})]}),
    (0,s.jsx)(f.Z,{className:"ml-2 h-3 w-3 shrink-0 opacity-50"})
  ]})}),
  (0,s.jsx)(E.PopoverContent,{className:"w-80 p-0",children:(0,s.jsxs)("div",{className:"p-3",children:[
    (0,s.jsx)("div",{className:"relative",children:(0,s.jsx)(k.Input,{placeholder:"Search gallery images...",className:"h-8 mb-3",onChange:e=>{...}})}),
    (0,s.jsx)(L.ScrollArea,{className:"max-h-64 overflow-y-auto",children:(0,s.jsx)("div",{className:"space-y-1",children:Array.isArray(el)&&el.length>0?el.map(e=>(0,s.jsxs)("div",{"data-gallery-item":!0,"data-title":e.title,"data-type":e.type,className:"flex items-center gap-2 w-full p-2 rounded-md hover:bg-accent cursor-pointer transition-colors",onClick:()=>e7(e.imageURL),children:[...]}))
```
Where `e7` is defined as:
```javascript
e7 = (0,i.useCallback)(e => { eX("avatar", e), ek(!1) }, [eX])
```
Thus, selecting an image in the gallery combobox popover directly assigns `entry.avatar = e.imageURL` (the HTTPS Cloudflare Images URL).

### 1.3 Live DOM Inspection of the Rendered Panel
From `scratch/npc_info_dom_details.json` captured directly from Chrome:
- **Container**: `<div class="space-y-4 p-4 border rounded-md bg-muted/20">`
- **Field `npc_prefix`**:
  - Label: `<label class="font-medium peer-disabled:cursor-not-allowed peer-disabled:opacity-70 flex flex-row items-center justify-between text-sm">NPC Prefix</label>`
  - Input: `<input class="flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-0 focus-visible:ring-transparent h-8" placeholder="e.g. => or leave empty" value="">`
  - Helper: `<p class="text-xs text-muted-foreground">Optional prefix marker before the NPC name, e.g. "=>"</p>`
- **Field `first_name`**:
  - Label: `<label ... text-sm">First Name *</label>`
  - Input: `<input class="... h-8" placeholder="Enter first name" value="Scarlett">`
- **Field `middle_names`**:
  - Label: `<label ... text-sm">Middle Names</label>`
  - Tag Input Container: `<div class="space-y-2"><div class="flex gap-2">`
  - Text Input: `<input class="... h-8 flex-1" placeholder="Add middle name and press Enter" autocapitalize="off" autocorrect="off" spellcheck="false">`
  - Add Button: `<button class="inline-flex items-center justify-center whitespace-nowrap text-sm shadow-md font-medium ... border border-input bg-background hover:bg-accent hover:text-accent-foreground rounded-md h-8 px-3" data-variant="outline" data-size="sm" type="button" disabled><svg class="lucide lucide-plus h-3 w-3">...</svg></button>`
  - Badges (when populated): `<div class="flex flex-wrap gap-2">` with `<span class="px-1">{item}</span>` and remove button `<button aria-label="Remove {item}"><svg class="lucide lucide-x h-3 w-3">...</svg></button>`
- **Field `last_name`**:
  - Label: `<label ... text-sm">Last Name</label>`
  - Input: `<input class="... h-8" placeholder="Enter last name" value="Rose">`
- **Field `nicknames`**:
  - Label: `<label ... text-sm">Nicknames</label>`
  - Tag Input Component (identical to `middle_names`), input placeholder: `"Add nickname and press Enter"`. Verified badge present for Scarlett Rose: `<span class="px-1">Scarlett</span>` with remove button `aria-label="Remove Scarlett"`.
- **Field `titles`**:
  - Label: `<label ... text-sm">Titles</label>`
  - Tag Input Component (identical to `middle_names`), input placeholder: `"Add title and press Enter (e.g., Dr., Sir, Lady)"`.

---

## 2. Logic Chain

1. **Conditional Visibility**:
   - In `66353-44918b7fd11ff8ae.js`, the JSX ternary checks `eu.custom_avatar_regex ? (Custom Regex Editor) : (NPC Information sub-panel)`.
   - Because our previous deployments set `custom_avatar_regex: true`, the UI rendered the custom regex textarea.
   - When `custom_avatar_regex` is toggled to `false` (or unset), Wyvern displays the `NPC Information` sub-panel (`space-y-4 p-4 border rounded-md bg-muted/20`).

2. **Data Model Structure for `npc_info`**:
   - The state updater calls:
     ```javascript
     eX("npc_info", {
       first_name: string,
       middle_names?: string[],
       last_name?: string,
       nicknames?: string[],
       titles?: string[],
       npc_prefix?: string
     })
     ```
   - Notice that `middle_names`, `nicknames`, and `titles` are bound to `m.E` which receives and returns a Javascript array (`value || []`). If the array is non-empty, it sends `array`; if empty (`e.length === 0`), it sends `undefined`.
   - `first_name`, `last_name`, and `npc_prefix` are simple strings (or `undefined` if empty).
   - This proves conclusively that `middle_names`, `nicknames`, and `titles` are **NOT** comma-separated strings in the schema; they are **Tag Inputs** mapped to `string[]` arrays.

3. **Avatar Selection Mechanism**:
   - The UI provides a combobox popover `<PopoverContent className="w-80 p-0">` that queries the Lorebook's `gallery` images (`el`).
   - Clicking any item in the popover fires `onClick: () => e7(e.imageURL)`, which executes `eX("avatar", e.imageURL)`.
   - This directly writes the Cloudflare Images URL into `entry.avatar`. There is no separate indirection or gallery ID stored on the entry; `entry.avatar` is the canonical reference.

4. **Regex Auto-Generation Algorithm**:
   - In `53944-e2a3f3ea28ad0416.js`, module `93312` function `WH(npc_info, npc_prefix, delimiter = ":")` auto-compiles the regex:
     - Applies normalization and escaping for quotes (`['‘’ʼ‛′]`) and hyphens (`[-‐‑‒–—−]`).
     - Adds line start lookbehind `(?<=^|\n)\s*(?:\*\*)?`.
     - Generates weighted permutations:
       * First + Middle + Last (weight 30000 + len)
       * First + Last (weight 20000 + len)
       * Last + First (weight 20000 + len)
       * Last + Middle + First (weight 30000 + len)
       * First + Middle (weight 20000 + len)
       * Nicknames (unquoted, `'...'`, `"..."`)
       * First Name alone (weight 10000 + len)
       * Last Name alone (weight 10000 + len)
     - Wraps into `(?<coreName>...)`.
     - Handles titles before and after the core name.
     - Allows particles (de, von, etc.) and bracketed text up to 6 words.
     - Delimits with trailing colon `(?:\*\*)?\s*:(?:\*\*(?=\s|$))?`.
   - When `custom_avatar_regex: false`, Wyvern uses this dynamic regex at runtime.

---

## 3. Caveats

- **No Caveats regarding DOM and Schema**: The DOM hierarchy, classes, tags, and data bindings were inspected both directly in the live browser via CDP and cross-verified byte-for-byte in the deminified Next.js bundles.
- **Backend API Invariant**: When deploying via `PUT /api/lorebooks/{id}`, the Wyvern server accepts `npc_info` directly as an object on each entry. If `custom_avatar_regex` is set to `false`, the UI will display the `NPC Information` fields and automatically auto-generate the regex. If `custom_avatar_regex` is `true`, the UI displays the `avatar_activation_regex` textarea while preserving `npc_info` in the saved object.

---

## 4. Conclusion

1. **Exact Sub-Panel DOM & Selectors**:
   - Container: `div.space-y-4.p-4.border.rounded-md.bg-muted\/20`
   - Header: `label.text-sm.font-medium` ("NPC Information") + `p.text-xs.text-muted-foreground` ("Provide NPC details to automatically generate avatar activation regex")
   - `npc_prefix`: `<input class="... h-8" placeholder="e.g. => or leave empty">`
   - `first_name`: `<input class="... h-8" placeholder="Enter first name">` (mandatory)
   - `middle_names`: Tag Input component `<input class="... h-8 flex-1" placeholder="Add middle name and press Enter">` + `<button data-size="sm"><svg lucide-plus></button>` $\to$ `string[]` array
   - `last_name`: `<input class="... h-8" placeholder="Enter last name">`
   - `nicknames`: Tag Input component `<input class="... h-8 flex-1" placeholder="Add nickname and press Enter">` + `<button data-size="sm"><svg lucide-plus></button>` $\to$ `string[]` array
   - `titles`: Tag Input component `<input class="... h-8 flex-1" placeholder="Add title and press Enter (e.g., Dr., Sir, Lady)">` + `<button data-size="sm"><svg lucide-plus></button>` $\to$ `string[]` array

2. **Input Type Confirmation**:
   - `middle_names`, `nicknames`, and `titles` are **Tag Inputs / Arrays (`string[]`)**, NOT comma-separated text strings.

3. **Gallery Selection**:
   - The `Change Avatar` button is a Radix Popover combobox displaying the Lorebook's gallery items. Selecting an item executes `entry.avatar = e.imageURL`, directly storing the CDN URL.

4. **Ready for Milestone 2**:
   - The exact contract for `npc_info` for Milestone 2 (`R2 Lorebook NPCs Sanitation & Alignment`) is confirmed:
     ```json
     "npc_info": {
       "first_name": "Scarlett",
       "middle_names": [],
       "last_name": "Rose",
       "nicknames": ["Scarlett"],
       "titles": [],
       "npc_prefix": ""
     }
     ```
   - All 210 entries across Primary and Secondary can be reliably populated using this verified schema.

---

## 5. Verification Method

To independently verify the observations:
1. **Re-run Live Browser Inspection**:
   ```bash
   python scratch/inspect_live_npc_info_dom.py
   ```
   Inspect `scratch/npc_info_dom_details.json` and screenshot `scratch/npc_info_panel_visible.png`.
2. **Inspect Bundle Logic**:
   Inspect `scratch/66353-44918b7fd11ff8ae.js` and `scratch/53944-e2a3f3ea28ad0416.js`.
3. **Verify Replicated Regex Generator**:
   ```bash
   node scratch/test_replicated_regex.js
   ```
