# Milestone 1 (R1) Handoff Report: Network & Payload Reverse-Engineering for Lorebook NPCs and Gallery

**Explorer Agent ID**: `explorer_m1_2`  
**Working Directory**: `e:\repository\SvartulfrVerse\.agents\teamwork\explorer_m1_2`  
**Parent Agent ID**: `c8a5c469-63a4-4154-bc85-fe2572ebf1e1`  
**Timestamp**: `2026-10-24T10:24:00Z`

---

## 1. Observation

### 1.1 Network & DevTools Authentication & API Status
- **DevTools / CDP Port 9222**: Port 9222 was open by process 35528 (`chrome.exe`), but Chrome was launched without `--remote-allow-origins=*`, resulting in `403 Forbidden` on incoming WebSocket handshakes from non-matching origins.
- **Wyvern Web API Direct Access**: Authenticated directly using Bearer JWT refreshed via `scratch/refresh_token.py` (generating valid 1142-byte token targeting `https://securetoken.googleapis.com/v1/token?key=AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw`).
- **Live Endpoint Calls**:
  - `GET https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC` (Primary) -> `HTTP 200 OK`, 724,067 bytes, 99 entries in `lexicon`.
  - `GET https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV` (Secondary) -> `HTTP 200 OK`, 1,031,163 bytes, 209 entries in `lexicon`.
  - `GET https://app.wyvern.chat/api/characters/mine` -> `HTTP 200 OK`, exactly 8 approved characters.
  - `GET https://app.wyvern.chat/api/user-personas` -> `HTTP 200 OK`, 3 personas (`persona_1786335754946` Alyssa, `1791389790053` Echo, `1792155173728` Jasper).

### 1.2 Frontend Production Bundle Extraction & Reverse-Engineering
Inspected Next.js production JavaScript chunks serving `https://app.wyvern.chat/lorebooks/edit/[id]`:
- `scratch/lorebook_chunks/66353-44918b7fd11ff8ae.js` (Lorebook Entry & NPC editor modal)
- `scratch/lorebook_chunks/95148-b515b69ac26da978.js` (Lorebook & NPC parsing/converter logic)
- `scratch/lorebook_chunks/page-385df219b0dca31a.js` (Lorebook edit page layout & gallery masonry)
- `scratch/lorebook_chunks/32697-2c943326ca1bc2fe.js` (API client definition: `o.hi.lorebooks.*`)
- `scratch/lorebook_chunks/83840-065c925af9ce7024.js` (Gallery queries and mutations)

#### Verbatim Code Snippet 1: `NPC Information` Sub-Panel UI (`66353-44918b7fd11ff8ae.js`, line ~34009)
```javascript
(0, s.jsxs)("div", {
  className: "space-y-4 p-4 border rounded-md bg-muted/20",
  children: [
    (0, s.jsxs)("div", {
      className: "space-y-2",
      children: [
        (0, s.jsx)(z.Label, { className: "text-sm font-medium", children: "NPC Information" }),
        (0, s.jsx)("p", { className: "text-xs text-muted-foreground", children: "Provide NPC details to automatically generate avatar activation regex" })
      ]
    }),
    (0, s.jsxs)("div", {
      className: "space-y-2",
      children: [
        (0, s.jsx)(z.Label, { className: "text-sm", children: "NPC Prefix" }),
        (0, s.jsx)(k.Input, {
          value: (null === (t = eu.npc_info) || void 0 === t ? void 0 : t.npc_prefix) || "",
          onChange: e => {
            var a;
            return eX("npc_info", {
              ...eu.npc_info,
              first_name: (null === (a = eu.npc_info) || void 0 === a ? void 0 : a.first_name) || "",
              npc_prefix: e.target.value || void 0
            })
          },
          placeholder: "e.g. => or leave empty",
          className: "h-8",
          disabled: !en
        }),
        (0, s.jsxs)("p", { className: "text-xs text-muted-foreground", children: ["Optional prefix marker before the NPC name, e.g. ", "\"=>\""] })
      ]
    }),
    (0, s.jsxs)("div", {
      className: "space-y-2",
      children: [
        (0, s.jsx)(z.Label, { className: "text-sm", children: "First Name *" }),
        (0, s.jsx)(k.Input, {
          value: (null === (T = eu.npc_info) || void 0 === T ? void 0 : T.first_name) || "",
          onChange: e => eX("npc_info", { ...eu.npc_info, first_name: e.target.value }),
          placeholder: "Enter first name",
          className: "h-8",
          disabled: !en
        })
      ]
    }),
    (0, s.jsxs)("div", {
      className: "space-y-2",
      children: [
        (0, s.jsx)(z.Label, { className: "text-sm", children: "Middle Names" }),
        (0, s.jsx)(m.E, {
          value: (null === (W = eu.npc_info) || void 0 === W ? void 0 : W.middle_names) || [],
          onChange: e => {
            var a;
            return eX("npc_info", {
              ...eu.npc_info,
              first_name: (null === (a = eu.npc_info) || void 0 === a ? void 0 : a.first_name) || "",
              middle_names: e.length > 0 ? e : void 0
            })
          },
          placeholder: "Add middle name and press Enter",
          disabled: !en
        })
      ]
    }),
    (0, s.jsxs)("div", {
      className: "space-y-2",
      children: [
        (0, s.jsx)(z.Label, { className: "text-sm", children: "Last Name" }),
        (0, s.jsx)(k.Input, {
          value: (null === (G = eu.npc_info) || void 0 === G ? void 0 : G.last_name) || "",
          onChange: e => {
            var a;
            return eX("npc_info", {
              ...eu.npc_info,
              first_name: (null === (a = eu.npc_info) || void 0 === a ? void 0 : a.first_name) || "",
              last_name: e.target.value || void 0
            })
          },
          placeholder: "Enter last name",
          className: "h-8",
          disabled: !en
        })
      ]
    }),
    (0, s.jsxs)("div", {
      className: "space-y-2",
      children: [
        (0, s.jsx)(z.Label, { className: "text-sm", children: "Nicknames" }),
        (0, s.jsx)(m.E, {
          value: (null === (J = eu.npc_info) || void 0 === J ? void 0 : J.nicknames) || [],
          onChange: e => {
            var a;
            return eX("npc_info", {
              ...eu.npc_info,
              first_name: (null === (a = eu.npc_info) || void 0 === a ? void 0 : a.first_name) || "",
              nicknames: e.length > 0 ? e : void 0
            })
          },
          placeholder: "Add nickname and press Enter",
          disabled: !en
        })
      ]
    }),
    (0, s.jsxs)("div", {
      className: "space-y-2",
      children: [
        (0, s.jsx)(z.Label, { className: "text-sm", children: "Titles" }),
        (0, s.jsx)(m.E, {
          value: (null === (K = eu.npc_info) || void 0 === K ? void 0 : K.titles) || [],
          onChange: e => {
            var a;
            return eX("npc_info", {
              ...eu.npc_info,
              first_name: (null === (a = eu.npc_info) || void 0 === a ? void 0 : a.first_name) || "",
              titles: e.length > 0 ? e : void 0
            })
          },
          placeholder: "Add title and press Enter (e.g., Dr., Sir, Lady)",
          disabled: !en
        })
      ]
    })
  ]
}),
(0, s.jsxs)("div", {
  className: "space-y-2",
  children: [
    (0, s.jsx)(z.Label, { className: "text-sm", children: "Lines Parsed" }),
    (0, s.jsx)(k.Input, {
      type: "number",
      min: "1",
      value: eu.lines_parsed || 1,
      onChange: e => eX("lines_parsed", parseInt(e.target.value) || 1),
      className: "h-8",
      disabled: !en
    }),
    (0, s.jsx)("p", { className: "text-xs text-muted-foreground", children: "How many lines after the regex match to parse as the character's message. Default is 1 line." })
  ]
})
```

#### Verbatim Code Snippet 2: Gallery Avatar Selection Mechanism (`66353-44918b7fd11ff8ae.js`, lines 18425–19200)
```javascript
// Popover listing gallery images passed via galleryImages prop (el)
Array.isArray(el) && el.length > 0 ? el.map(e => (
  (0, s.jsxs)("div", {
    "data-gallery-item": !0,
    "data-title": e.title,
    "data-type": e.type,
    className: "flex items-center gap-2 w-full p-2 rounded-md hover:bg-accent cursor-pointer transition-colors",
    onClick: () => e7(e.imageURL), // <--- Directly calls e7 with e.imageURL!
    children: [
      (0, s.jsx)("div", { className: "w-8 h-8 rounded overflow-hidden bg-muted flex-shrink-0", children: (0, s.jsx)("img", { src: e.imageURL, alt: e.title, className: "w-full h-full object-cover" }) }),
      (0, s.jsxs)("div", { className: "flex-1 min-w-0", children: [(0, s.jsx)("div", { className: "font-medium truncate text-sm", children: e.title }), (0, s.jsx)("div", { className: "text-xs text-muted-foreground truncate", children: e.type })] }),
      (0, s.jsx)(j.Z, { className: (0, B.cn)("ml-auto h-4 w-4", eu.avatar === e.imageURL ? "opacity-100" : "opacity-0") })
    ]
  }, e.id)
)) : (0, s.jsx)("div", { className: "p-4 text-center text-sm text-muted-foreground", children: "No gallery images available" })

// Callback e7:
e7 = (0, i.useCallback)(e => {
  eX("avatar", e);
  ek(!1);
}, [eX]);
```

#### Verbatim Code Snippet 3: `ignored_characters` & `ignored_personas` Wiring (`66353-44918b7fd11ff8ae.js`, lines ~10079)
```javascript
eV = null !== ($ = null == eu ? void 0 : eu.ignored_characters) && void 0 !== $ ? $ : [];
eY = null !== (X = null == eu ? void 0 : eu.ignored_personas) && void 0 !== X ? X : [];

eJ = (0, i.useCallback)(async e => {
  ex(a => {
    var t;
    if (!a) return a;
    let s = null !== (t = a.ignored_characters) && void 0 !== t ? t : [];
    let n = s.includes(e.id) ? s.filter(a => a !== e.id) : [...s, e.id];
    return { ...a, ignored_characters: n };
  });
  ep(!0);
}, []);

eK = (0, i.useCallback)(e => {
  ex(a => {
    var t;
    if (!a) return a;
    let s = null !== (t = a.ignored_personas) && void 0 !== t ? t : [];
    let n = s.includes(e.persona_id) ? s.filter(a => a !== e.persona_id) : [...s, e.persona_id];
    return { ...a, ignored_personas: n };
  });
  ep(!0);
}, []);
```

#### Verbatim Code Snippet 4: PUT API Call Structure (`32697-2c943326ca1bc2fe.js`, line ~42500)
```javascript
lorebooks: {
  get: t => g("".concat(r.BC, "/lorebooks/").concat(t)).then(t => t ? { ...t } : null),
  add: t => v("".concat(r.BC, "/lorebooks"), t).then(t => ({ ...t })),
  update: (t, e) => B("".concat(r.BC, "/lorebooks/").concat(t), e).then(t => ({ ...t })),
  delete: t => y("".concat(r.BC, "/lorebooks/").concat(t)),
  ...
}
```
`B` executes an HTTP `PUT` request with `Content-Type: application/json` to `https://app.wyvern.chat/api/lorebooks/{id}` (or `https://api.wyvern.chat/lorebooks/{id}`).

---

## 2. Logic Chain

1. **Evidence 1.2 Snippet 1 establishes the exact schema of `npc_info`**:
   The input fields directly correspond to:
   - `first_name`: string (required)
   - `middle_names`: `string[]` (array of strings, omitted or undefined if empty)
   - `last_name`: string (optional, omitted or undefined if empty)
   - `nicknames`: `string[]` (array of strings, omitted or undefined if empty)
   - `titles`: `string[]` (array of strings, omitted or undefined if empty)
   - `npc_prefix`: string (optional, e.g. `"=>"`, omitted or undefined if empty)
   - `lines_parsed`: number (default: 1)
   - `custom_avatar_regex`: boolean (if true, uses custom `avatar_activation_regex`; if false, auto-generates regex from `npc_info`)

2. **Evidence 1.2 Snippet 2 establishes the avatar reference mechanism**:
   - The Lorebook gallery holds objects of type `LorebookGalleryItem` (each having `id`, `imageURL`, `title`, `type`, etc.).
   - When an avatar is selected from the gallery, the callback `e7(e.imageURL)` assigns `e.imageURL` (the string HTTPS URL) directly to `entry.avatar`.
   - The entry does **NOT** hold a foreign key or gallery item ID. It stores the exact Cloudflare Image CDN URL:
     `"avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/<hash>/public"`.
   - `alternate_avatars` stores an array of string URLs (`string[]`).

3. **Evidence 1.2 Snippet 3 and Snippet 4 establish how anti-collision fields are transmitted**:
   - `ignored_characters` is an array of Character Card IDs (`string[]`).
   - `ignored_personas` is an array of User Persona IDs (`string[]`).
   - Both arrays reside directly inside each entry object within the `lexicon` array of the Lorebook.
   - When `PUT /api/lorebooks/{id}` is executed, the entire `lexicon` array (with entries holding `ignored_characters` and `ignored_personas`) is sent in the request body.

4. **Comparative Analysis of Local Files vs Target Schema**:
   Running `scratch/inspect_local_lorebooks.py` and `scratch/compare_local_live.py` revealed:
   - **`FINAL/Svartulfr_NPC_Primary.json`**:
     - `gallery` property: **MISSING** at root level! (Needs `gallery: []`, `gallery_count: 0`).
     - `entries` and `lexicon` byte-for-byte parity: `True` (99 entries).
     - `npc_info`: Present on all 99 entries, but contains ONLY `{ first_name, last_name, nicknames, titles }`.
     - `npc_info.middle_names`: **0/99 entries** have this field. Completely missing.
     - `npc_info.npc_prefix`: **0/99 entries** have this field. Completely missing.
     - `titles`: Only 2/99 entries have non-empty titles (`Professor Loewe`, `Dr. Arthur Sinclair`).
     - `ignored_characters`: Populated on 13 entries (the 8 Douglas/Bloodmoon characters + 5 retired card NPCs).
     - `ignored_personas`: Populated on 2 entries (`Jasper Svartr Douglas Bloodmoon` -> `['1792155173728']`, `Alyssa Hvit Douglas Bloodmoon` -> `['persona_1786335754946']`).
     - `avatar`: Populated on 100% of entries (59 unique URLs, Cloudflare imagedelivery).
   - **`FINAL/Svartulfr_NPC_Secondary.json`**:
     - `gallery` property: **PRESENT** (`gallery: []`, `gallery_count: 0`).
     - `entries` and `lexicon` byte-for-byte parity: `True` (211 entries).
     - Local vs Live Entry Count Difference: Local has **211 entries** while Live Wyvern currently has **209 entries**.
       The 2 local entries missing from Live are:
       - `Finn the Satyr` (`quJQvjvUWQLUeOCNv2Wko`)
       - `Jasper Rowan` (`d1Qg6eRvuKC8iI5kNWPzb`)
     - `npc_info`: Present on all 211 entries, but contains ONLY `{ first_name, last_name, nicknames, titles }`.
     - `npc_info.middle_names`: **0/211 entries** have this field. Completely missing.
     - `npc_info.npc_prefix`: **0/211 entries** have this field. Completely missing.
     - `titles`: 110/211 entries have non-empty titles (`Coach`, `Professor`, `Dean`, etc.).
     - `ignored_characters`: Populated on 1 entry (`Edric Douglas` -> `['_TbRM3EdxDjHFgqztTbCpL']`).
     - `ignored_personas`: 0 entries.
     - `avatar`: Populated on 100% of entries (53 unique URLs).

---

## 3. Caveats

1. **CDP Direct Port 9222 Handshake**: Chrome on port 9222 rejected incoming WebSocket requests with 403 Forbidden because Chrome was running without `--remote-allow-origins=*`. However, full network and payload reverse-engineering was accomplished by downloading the exact production bundles from `https://app.wyvern.chat/_next/static/chunks/` and querying the live Web API endpoints via authenticated HTTPS requests.
2. **Gallery Backend Storage**: On the live Wyvern API, both Lorebooks currently have `gallery: []` and `gallery_count: 0` because avatar images were assigned directly via public Cloudflare Images URLs without populating the optional asset catalog array `gallery`.
3. **Entries Parity vs PUT Payload**: Local files must maintain 100% byte-for-byte equality between `entries` and `lexicon`. When issuing `PUT /api/lorebooks/{id}` to the live Wyvern API, only `lexicon` and top-level metadata should be sent to avoid HTTP 413 Payload Too Large.

---

## 4. Conclusion

1. **`npc_info` Schema**:
   The exact schema within each entry is:
   ```json
   "npc_info": {
     "first_name": "String (Required)",
     "middle_names": ["String (Array)"],
     "last_name": "String (Optional)",
     "nicknames": ["String (Array)"],
     "titles": ["String (Array)"],
     "npc_prefix": "String (Optional)"
   }
   ```
2. **Lorebook `gallery` Schema**:
   The top-level Lorebook schema is:
   ```json
   {
     "gallery": [
       {
         "id": "String (Unique ID)",
         "imageURL": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/<hash>/public",
         "title": "String",
         "type": "image | avatar | portrait",
         "description": "String",
         "tags": ["String"],
         "like_count": 0,
         "comment_count": 0,
         "awards": { "tiers": [] },
         "gridRowSpan": 14
       }
     ],
     "gallery_count": 0
   }
   ```
3. **Avatar Reference**:
   Entries reference avatars by the direct Cloudflare HTTPS URL string in `entry.avatar` (e.g. `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/.../public`), not via foreign keys or IDs.
4. **Anti-Collision Payloads**:
   `ignored_characters` (`string[]` of card IDs) and `ignored_personas` (`string[]` of persona IDs) are transmitted directly within each entry of the `lexicon` array in `PUT /api/lorebooks/{id}`.
5. **Remediation Action Items for Milestone 2 (M2)**:
   - Add `"gallery": []` and `"gallery_count": 0` to root of `FINAL/Svartulfr_NPC_Primary.json`.
   - Populate `middle_names: []` (or extracted middle names, e.g. for Douglas family and Project Blackwolf) and `npc_prefix: ""` on all 99 entries of Primary and 211 entries of Secondary.
   - Deploy both Lorebooks to live Wyvern API via `PUT` and ensure Secondary increments from 209 to 211 entries.

---

## 5. Verification Method

To independently verify the observations and schema conclusions:

1. **Verify Live API Endpoints & Entry Counts**:
   ```powershell
   python scratch/analyze_live_lorebooks.py
   ```
   *Expected output*: Primary returns HTTP 200 with 99 entries; Secondary returns HTTP 200 with 209 entries; `gallery: []`, `gallery_count: 0`.

2. **Verify Frontend UI Field Extraction in Production JS**:
   ```powershell
   python scratch/inspect_npc_info_ui.py
   ```
   *Expected output*: Verbatim JSX matching `NPC Prefix`, `First Name *`, `Middle Names`, `Last Name`, `Nicknames`, `Titles`, and `Lines Parsed`.

3. **Verify Gallery Selection Callback**:
   ```powershell
   python scratch/inspect_gallery_select.py
   ```
   *Expected output*: Verbatim JSX showing `onClick: () => e7(e.imageURL)` and `eu.avatar === e.imageURL`.

4. **Verify Local Diff & Missing Fields**:
   ```powershell
   python scratch/compare_local_live.py
   python scratch/inspect_local_lorebooks.py
   ```
   *Expected output*: Confirmation that `middle_names` and `npc_prefix` are currently absent across all entries in both local files, and Primary lacks `gallery` at root.
