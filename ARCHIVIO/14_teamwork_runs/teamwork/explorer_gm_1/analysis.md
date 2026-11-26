# Technical Investigation Report: Wyvern Assistant Architecture & API Schema

**Author:** Explorer GM 1 (Assistant Architecture Explorer)  
**Date:** 2026-10-20  
**Scope:** Standalone Assistants in Wyvern Chat (`/mine > ASSISTANT`), Wyvern Web API endpoints, JSON payload schema, lorebook bindings, D20 + S.P.E.C.I.A.L. resolution engine, and canon invariants.

---

## 1. Wyvern Web API Endpoint for Assistants

### 1.1 Endpoint Discovery & Validation
Through deep inspection of Next.js frontend application bundles (`app/(content)/mine/page-4fad869ea17238ea.js` and `54866-5b1f01a517163780.js`) and live HTTP testing with Bearer tokens from `scratch/wyvern_token.txt`:

- **Negative / False Paths:**
  - `GET /api/assistants` -> HTTP 404 Not Found (`{"message":"Route GET:/assistants not found"}`)
  - `GET /api/characters?type=assistant` -> HTTP 404 Not Found
  - `GET /api/mine/assistants` -> HTTP 404 Not Found
  - `GET /api/characters/mine` -> Returns characters, but assistants are NOT stored as characters.

- **Authoritative Endpoint:**
  The Wyvern backend implements standalone assistants under the entity name **`SimpleAssistantConfig`**, exposed via the REST endpoint:
  **`https://app.wyvern.chat/api/simple-assistant-config`**

### 1.2 Full Endpoint Route Map
| HTTP Method | Route | Description |
|---|---|---|
| `GET` | `/api/simple-assistant-config` | List current user's assistants (`{ configs, total, page, limit, totalPages }`) |
| `GET` | `/api/simple-assistant-config/{id}` | Get full assistant details by ID |
| `POST` | `/api/simple-assistant-config` | Create a new assistant |
| `PUT` | `/api/simple-assistant-config/{id}` | Update an existing assistant |
| `DELETE` | `/api/simple-assistant-config/{id}` | Delete an assistant |
| `GET` | `/api/simple-assistant-config/browse` | Browse community/public assistant configs |
| `GET` | `/api/simple-assistant-config/usable` | Query usable assistants (supports query param `?kind=narrator` or `?kind=sidechat`) |
| `GET` | `/api/simple-assistant-config/narrator-presets` | Built-in system narrator presets (`preset:storyteller`, `preset:screenwriter`, `preset:game-master`, `preset:erotica-writer`) |
| `POST` | `/api/simple-assistant-config/{id}/fork` | Fork an existing assistant config into user's account |
| `POST` | `/api/simple-assistant-config/{id}/like` | Like an assistant config |
| `POST` | `/api/simple-assistant-config/{id}/bookmark` | Bookmark an assistant config |

---

## 2. Entity Model & JSON Payload Schema

### 2.1 Backend MikroORM Entity Model
Directly extracted from the backend validation response:
```text
entity: SimpleAssistantConfig {
  created_at: ISODate,
  updated_at: ISODate,
  _id: string ('simple_assistant_...'),
  title: string (REQUIRED),
  description: string,
  system_prompt: string,
  final_instructions: string,
  avatar: string,
  kind: 'narrator' | 'sidechat',
  visibility: 'private' | 'public',
  rating: 'none' | 'mature' | 'explicit',
  status: 'approved' | 'pending' | 'declined',
  tags: string[],
  approval_date: null | ISODate,
  rejection_date: null | ISODate,
  approval_comment: null | string,
  rejection_comment: null | string,
  forked_from: null | object,
  user: UserInfo
}
```

### 2.2 Frontend Form Mapping (from `54866-5b1f01a517163780.js`)
```javascript
// Default Values
Y = () => ({
  title: "",
  description: "",
  system_prompt: "",
  final_instructions: "",
  avatar: "",
  visibility: "private",
  rating: "none",
  tags: []
});

// Edit Mapper
J = e => ({
  title: e.title,
  description: e.description || "",
  system_prompt: e.system_prompt || "",
  final_instructions: e.final_instructions || "",
  avatar: e.avatar || "",
  visibility: e.visibility ?? "private",
  rating: e.rating ?? "none",
  tags: e.tags ?? []
});
```

### 2.3 Exact Creation Payload for "Svartúlfr — Game Master & World Engine"
```json
{
  "title": "Svartúlfr — Game Master & World Engine",
  "description": "TTRPG Game Master, World Engine e arbitro narrativo per l'universo Svartúlfr. Gestisce conseguenze diegetiche, check D20 + S.P.E.C.I.A.L., reazioni corali del cast e rigida aderenza al canone in lingua italiana.",
  "system_prompt": "<system_prompt_content>",
  "final_instructions": "<final_instructions_content>",
  "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public",
  "kind": "narrator",
  "visibility": "private",
  "rating": "explicit",
  "tags": [
    "Svartulfr",
    "Game Master",
    "TTRPG",
    "D20",
    "Narrator",
    "World Engine"
  ]
}
```

### 2.4 Values Breakdown
1. **`kind`:** Must be `"narrator"`. In Wyvern Chat, an assistant with `kind: "narrator"` acts as the Narrator/Game Master replacing the default engine. An assistant with `kind: "sidechat"` is routed to the sidechat/analyzer drawer.
2. **`visibility`:** `"private"` is safe for development and immediate use in `/mine > ASSISTANT`.
3. **`rating`:** `"explicit"` matches the Svartúlfr Verse adult modern fantasy setting.
4. **`avatar`:** Uses the canonical Svartúlfr Crest fallback (`https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public`).

---

## 3. Lorebook Attachments Architecture

### 3.1 Architecture Truth
`SimpleAssistantConfig` does **not** maintain a `lorebook_ids` field directly on its table. In Wyvern Chat's decoupled modular architecture:
- **Character Scenarios** bind Lorebooks via `lorebook_ids: [...]`. All 6 scenarios deployed in the previous milestone already link the 6 official Svartúlfr Lorebooks:
  1. `_gwwCxCfQ6PQaLEjAQVpJL` (Lorebook I)
  2. `_HfG7TeV6MJyj6bxMwxkpt` (Lorebook II)
  3. `_9zWTGqYJNJ4BCDMj8gfcD` (Lorebook III)
  4. `_EjXxkmPVhpCXg8xABpFkK` (Location)
  5. `_zwEqgEEzh12X6gHVmMKKC` (NPC Primary)
  6. `_Uht3Ckz44JBDrPnUHq7LV` (NPC Secondary)
- **Standalone Characters** bind Lorebooks via `lorebooks: [...]`.
- **Chat Session / UI:** When entering a chat, active Lorebooks are attached to the chat session context. The selected Assistant provides the narrative rules (`system_prompt` + `final_instructions`).
- **Prompt Assembly Synergy:** In R2, the custom Prompt Assembly (`AI Connections > Prompts`) defines XML templates (`<npc>`, `<location>`, `<item>`, `<lore_entry>`, `<special_stats>`), ensuring that when the 6 Lorebooks activate, they are structured exactly as expected by the Game Master.

---

## 4. D20 + S.P.E.C.I.A.L. Skill Check Resolution Engine

### 4.1 S.P.E.C.I.A.L. Attribute Matrix
Based on repository canon (`CanonDecisions.md`, `scratch/compute_final_rpg_stats.py`):
- **STR (Strength):** Potenza muscolare, attacco in mischia, sollevamento carichi pesanti, presa, sfondamento.
- **PER (Perception):** Sensi lupini affinati, olfatto predatorio, udito direzionale, individuazione anomalie eteriche, mira a distanza.
- **END (Endurance):** Tolleranza al danno, resistenza metabolica al freddo, rigenerazione cellulare, resistenza a miasmi e veleni, reazione all'argento.
- **CHA (Charisma):** Presenza scenica, comando dell'Alpha, fascino magnetico, diplomazia, persuasione, negoziazione commerciale.
- **INT (Intelligence):** Teoria magica, crittografia avanzata, technomancy, programmazione di droni, conoscenza accademica SUCC/CUMS.
- **AGI (Agility):** Velocità di scatto, acrobazia, riflessi in combattimento, furtività, destrezza manuale, transizione parziale di forma.
- **LCK (Luck):** Fato, intuito cieco, deviazione provvidenziale dei colpi, drop rari nei dungeon, coincidenze fortunate.

### 4.2 Resolution Mechanics
- **Formula:** `D20 + Modificatore Attributo vs DC (Classe Difficoltà)`.
- **Difficulty Classes (DC):**
  - DC 5: Routine (azione elementare con minima pressione).
  - DC 10: Facile (azione standard per un civile addestrato).
  - DC 15: Moderata (sfida significativa che richiede competenza).
  - DC 20: Difficile (azione complessa ad alto rischio).
  - DC 25: Estrema (prodezza quasi impossibile, riservata a veterani o Alpha).
  - DC 30: Mitica / Ascended (sfida sovrumana al limite delle leggi della realtà).
- **Esiti:**
  - `Fallimento Critico (Natural 1)`: Fallimento totale con complicazione diegetica immediata.
  - `Fallimento`: Risultato totale < DC. L'azione non ha successo e la situazione evolve con tensione.
  - `Successo`: Risultato totale >= DC. L'azione ha successo pieno.
  - `Successo Critico (Natural 20)`: Successo spettacolare con vantaggio narrativo aggiuntivo.

### 4.3 Isolated Diegetic Formatting
The check must be rendered on a dedicated standalone line with no narrative wrapping:
```text
> [TEST: <Attributo> (D20: <Tiro> + <Mod> = <Totale> vs DC <Target>) -> ESITO: <SUCCESSO / FALLIMENTO / SUCCESSO CRITICO / FALLIMENTO CRITICO>]
```
Example:
```text
> [TEST: PER (D20: 15 + 8 = 23 vs DC 15) -> ESITO: SUCCESSO]
```

---

## 5. Canon Rules & Formatting Invariants

1. **Italian Sandwich Language Enforcement:**
   - **System Prompt Header:**
     ```xml
     [MANDATORY LANGUAGE DIRECTIVE: Output strictly in Italian. All narration, dialogue, and resolution blocks must be generated in natural, fluent Italian.]
     ```
   - **Final Instructions Tail:**
     ```xml
     [ORDINE FINALE ASSOLUTO: Scrivi l'intera risposta (narrazione, dialoghi, pensieri intrusivi, test di risoluzione) ESCLUSIVAMENTE IN LINGUA ITALIANA. Non usare mai il trattino lungo (—).]
     ```
2. **Zero Em-Dash (`—`) Invariant:**
   - Absolute ban on the unicode em-dash (`—`). Use commas, colons, or periods.
3. **Dialogue and Action Discipline:**
   - Spoken dialogue: standard double quotes (`"..."`).
   - Plain text narration: actions and sensory descriptions without asterisks.
   - Internal thoughts: enclosed strictly in asterisks (`*...*`).
4. **Anti-Puppeting & Thought Privacy:**
   - Never write dialogue, choices, or thoughts for `{{user}}`.
   - NPCs cannot read unvoiced internal thoughts.
5. **Multi-NPC Dialogue Prefix:**
   - Secondary NPCs speak using `Nome Completo: "..."` on a new line to trigger regex avatar parsing.
6. **Situational Digital Feeds:**
   - `【 LIVE FEED 】` and `❤️Pack-Family❤️` trigger only when devices or social media are actively accessed in-scene.

---

## 6. Repository Inventory of Existing Assistant Payloads

- **`FINAL/`:** Zero assistant JSON payloads currently exist.
- **`scratch/`:** Zero assistant deployment scripts exist (all existing scripts targeted characters, scenarios, and lorebooks).
- **`ARCHIVIO/`:** Contains raw source cards and drafts, no Wyvern assistant configs.
- **Wyvern Live Cloud:**
  - 2 forked assistants present on user account:
    - `simple_assistant_83jBt419dRWR76at1PwPD` (Comments Thread, `sidechat`)
    - `simple_assistant_VhbAk8GFNq3Rz19FVgBfJ` (All Seeing Eye, `sidechat`)
  - 4 built-in system presets available via `/api/simple-assistant-config/narrator-presets`.

---

## 7. Next Actions for Implementation (Milestone 2)
1. Assemble `FINAL/assistants/Svartulfr_Game_Master_Assistant.json` adhering to the validated `SimpleAssistantConfig` schema.
2. Deploy via `POST https://app.wyvern.chat/api/simple-assistant-config` using Bearer auth from `scratch/wyvern_token.txt`.
3. Verify live persistence via `GET https://app.wyvern.chat/api/simple-assistant-config/{id}`.
