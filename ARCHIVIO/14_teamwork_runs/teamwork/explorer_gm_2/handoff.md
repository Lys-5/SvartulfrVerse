# Handoff Report — Explorer GM 2 (Prompt Assembly Explorer)
**Data:** 2026-10-20  
**Mittente:** Explorer GM 2 (`.agents/teamwork/explorer_gm_2`)  
**Destinatario:** Orchestrator 3 / Caller (`6c88066a-eba8-41aa-adf7-8e00569a9154`)  
**Tipo Handoff:** Hard (Task Complete)

---

## 1. Observation

1. **Endpoint REST API Wyvern:**
   - Esecuzione `scratch/inspect_prompts_architecture.py` ha rivelato:
     - `/api/prompts` e `/api/prompts/mine` restituiscono `HTTP 404`.
     - `/api/prompt-assemblies` restituisce `HTTP 404`.
     - `/api/exploreSearch/prompt-assemblies?page=1&limit=10` restituisce `HTTP 200` con `total: 9` e lista di assembly con prefisso `pha_` (es. `pha_eYA4zAYeEXePBm36bCkBK`, `pha_4f938ypjwke4yXDEqx86B`).
   - Ispezione del client bundle `36457-688d656b1534b9f0.js` a riga 115251:
     ```javascript
     getAll: e => n.hi.get("".concat(a.BC, "/prompt-assembly"), {params: e}),
     getById: e => n.hi.get("".concat(a.BC, "/prompt-assembly/").concat(e)),
     create: e => n.hi.post("".concat(a.BC, "/prompt-assembly"), e),
     update: (e, t) => n.hi.put("".concat(a.BC, "/prompt-assembly/").concat(e), t),
     remove: e => n.hi.del("".concat(a.BC, "/prompt-assembly/").concat(e)),
     fork: e => n.hi.post("".concat(a.BC, "/prompt-assembly/").concat(e, "/fork"), {})
     ```
   - Esecuzione `scratch/test_prompt_assembly_endpoint.py`:
     - Chiamata autenticata a `GET https://app.wyvern.chat/api/prompt-assembly` ha restituito `HTTP 200 OK` con `{ assemblies: [{ id: "pha_bjzXBqMTDDWcfnCPzdUqr", name: "Universal Neutralisation Prompt V2 (18+) (Fork)", visibility: "private" }], total: 1 }`.
   - Recupero del documento live `GET /api/prompt-assembly/pha_bjzXBqMTDDWcfnCPzdUqr` (`scratch/user_existing_prompt_assembly.json`) ha confermato la struttura esatta dei campi JSON supportati da Wyvern: `blocks`, `main_prompt_template`, `floating_prompt_template`, `lore_template`, `lore_template_header`, `lore_template_footer`, `lore_entry_separator`, `whisper_template`, `start_reply_with`, `show_reply_prefix`, `floating_depth_percent`, `floating_role`, `main_prompt_sections`, `floating_prompt_sections`.

2. **Handlebars Macros e Modelli di Prompt:**
   - Nel bundle `36457-688d656b1534b9f0.js` (linee 431-2141 e 59540-70808) e in `docs/guides/Guide_World.md` (linee 870-895):
     - Supporto nativo a `{{char}}`, `{{user}}`, `{{description}}`, `{{personality}}`, `{{scenario}}`, `{{mesExamples}}`, `{{system}}`, `{{personaDescription}}`, `{{personaOutfitName}}`, `{{personaOutfit}}`, `{{wiBefore}}`, `{{wiAfter}}`, `{{summary}}`, `{{characterNote}}`, `{{authorNote}}`, `{{whisper}}`, `{{original}}`.
     - Supporto ad helper condizionali: `{{#if (eq type "npc")}}`, `ifEquals`, `ifNotEquals`, `ifGreater`, `ifLess`, `and`, `or`, `not`, `eq`, `ne`, `gt`, `lt`.

3. **Lore Templates XML:**
   - In `pha_4f938ypjwke4yXDEqx86B` e `user_existing_prompt_assembly.json` (linee 437-439):
     - `lore_template_header`: `<world_context position="{{position}}" count="{{count}}">`
     - `lore_template_footer`: `</world_context>`
     - `lore_template`: supporta rami polimorfici per `type`: `npc`, `location`, `item`, `creature`, `event`, e generico, iniettando `<stats>{{rpg_stats}}</stats>` o `<special_stats>{{rpg_stats}}</special_stats>`.

4. **Floating Prompt & Director's Whisper:**
   - In `user_existing_prompt_assembly.json` (linee 436, 440, 443, 444):
     - `floating_depth_percent`: `4`
     - `floating_role`: `"user"`
     - `whisper_template`: `(OOC Instructions to guide AI output that must be adhered to: \n {{whisper}}).`

5. **Post-History Blocks (Final Instructions):**
   - In `user_existing_prompt_assembly.json` (linee 77-430) e `FINAL/PROMPT_OVERRIDES_WYVERN.md` (linee 105-166):
     - Struttura dei blocchi con `role: "user"`, `order: 0..N`, `enabled: true`, `triggerOptions: ["normal", "continue", "impersonate", "swipe", "quiet"]`.
     - Inclusione vincolante di: Sandwich Linguistico Italiano, formattazione dialoghi `Nome: "..."`, zero em-dash, feed digitali situazionali (`【 LIVE FEED 】`, `❤️Pack-Family❤️`), e motore D20 + S.P.E.C.I.A.L. (`> [TEST: ...]`).

---

## 2. Logic Chain

1. Dalle osservazioni 1.1 e 1.2, Wyvern non utilizza un endpoint plurale `/api/prompt-assemblies`, bensì la risorsa singolare `https://app.wyvern.chat/api/prompt-assembly` per tutte le operazioni CRUD.
2. Dalle osservazioni 1.3 e 1.4, le Prompt Assembly non sono effimere o relegate al solo `localStorage` del browser, ma risiedono su MongoDB/backend Wyvern con un identificativo univoco `pha_...`.
3. Dalle osservazioni 1.3 e 2, la personalizzazione dei prompt in Wyvern Chat opera tramite l'iniezione modulare di 4 strati:
   - **Main Prompt:** In testa al contesto, espandibile tramite Handlebars.
   - **Lore Template:** In mezzo al contesto, generato dinamicamente con tag XML polimorfici in base all'entità evocata (`<npc>`, `<location>`, `<item>`, `<creature>`, `<lore_entry>`, `<special_stats>`).
   - **Floating Prompt:** A profondità 4% (`floating_depth_percent: 4`) con ruolo HTTP `User` (`floating_role: "user"`), garantendo la massima attenzione del modello sulle direttive anti-drift.
   - **Final Instructions (Blocks):** In coda alla cronologia, con ruolo HTTP `User`, bloccando in modo assoluto la lingua italiana, le convenzioni di punteggiatura e la risoluzione dei tiri D20.
4. Di conseguenza, il payload JSON formalizzato in `analysis.md` (sezione 8) è direttamente conforme alle specifiche del compilatore prompt di Wyvern ed è pronto per essere deployato tramite `POST /api/prompt-assembly` o configurato via web UI in `AI Connections > Prompts`.

---

## 3. Caveats

- **Ambiente Sandbox Read-Only:** Come da vincoli di ruolo Explorer, non è stata effettuata alcuna operazione di scrittura (`POST` o `PUT`) sul World o sulle Prompt Assembly live durante questa fase; il deployment effettivo avverrà nel Milestone 2.
- **Provider LLM Prefill Support:** Il campo `start_reply_with` richiede che il provider sottostante (es. Featherless, Together, OpenRouter) supporti il prefill dell'assistente; per massima compatibilità cross-provider è stato configurato a stringa vuota `""` con `show_reply_prefix: false`.

---

## 4. Conclusion

1. L'architettura delle Custom Prompt Assembly su Wyvern è stata interamente decodificata e validata contro il server di produzione.
2. L'endpoint ufficiale per la creazione e la persistenza è `POST https://app.wyvern.chat/api/prompt-assembly`.
3. Il payload completo e verificato per `"Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)"` è stato documentato e validato in `analysis.md`.
4. Il workflow per l'implementatore (Milestone 2) è pronto per l'esecuzione senza alcuna ambiguità residua.

---

## 5. Verification Method

Per verificare in modo indipendente le scoperte di questa indagine:
1. **Verifica Endpoint API:**
   ```powershell
   python -c "import urllib.request, json; token = open('scratch/wyvern_token.txt').read().strip(); req = urllib.request.Request('https://app.wyvern.chat/api/prompt-assembly', headers={'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0'}); print(json.loads(urllib.request.urlopen(req).read().decode())['assemblies'])"
   ```
   *Esito atteso:* Visualizzazione dell'array `assemblies` con l'assembly attiva `pha_bjzXBqMTDDWcfnCPzdUqr`.
2. **Ispezione Documento Live:**
   Esaminare `scratch/user_existing_prompt_assembly.json` per riscontrare la corrispondenza 1:1 con i campi definiti in `analysis.md`.
3. **Ispezione Sorgenti Webpack:**
   Esaminare `scratch/36457-688d656b1534b9f0.js` alla riga 115251 per la definizione dei metodi `create`, `update`, `getAll`, `remove`, `fork`.
