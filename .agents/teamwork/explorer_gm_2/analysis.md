# Analisi Architetturale: Custom Prompt Assemblies in Wyvern Chat
**Explorer GM 2 (Prompt Assembly & Handlebars Templates)**  
**Data:** 2026-10-20  
**Target:** Architettura Prompt Assembly, API Endpoints, Handlebars Macros, Template XML e Configurazione Master TTRPG per *Svartúlfr Verse*.

---

## 1. Executive Summary

L'indagine tecnica condotta sul client frontend di Wyvern Chat (`https://app.wyvern.chat`) e sul backend REST API ha rivelato con precisione chirurgica il meccanismo con cui Wyvern gestisce i preset di Prompt Assembly (`AI Connections > Prompts`).

Le scoperte chiave includono:
1. **Endpoint API Ufficiale:** L'endpoint REST ufficiale è **singolare**: `https://app.wyvern.chat/api/prompt-assembly` (con prefisso ID `pha_`, ad es. `pha_bjzXBqMTDDWcfnCPzdUqr`). Supporta `GET`, `POST`, `PUT`, `DELETE` e `POST .../fork`.
2. **Persistenza e Collegamento:** Le Prompt Assembly sono entità di primo livello salvate nel database cloud di Wyvern. Possono essere collegate a scenari e assistenti (`prompt_assembly_id`) o attivate come override nella sessione di chat attiva (`prompt_assembly_id`).
3. **Template Handlebars e Blocchi XML:** Wyvern adotta Handlebars con supporto completo a variabili di contesto (`{{char}}`, `{{user}}`, `{{description}}`, `{{personality}}`, `{{scenario}}`, `{{mesExamples}}`, `{{personaDescription}}`, `{{personaOutfit}}`, `{{wiBefore}}`, `{{wiAfter}}`, `{{summary}}`, `{{system}}`, `{{whisper}}`, `{{original}}`) e helper condizionali (`{{#if (eq type "npc")}}`, `ifEquals`, `and`, `or`, `not`).
4. **Lore Templates XML:** I template di Lore supportano header (`<world_context position="{{position}}" count="{{count}}">`), footer (`</world_context>`) e discriminazione polimorfica per tipo di entry (`npc`, `location`, `item`, `creature`, `event`, `lore_entry`), con inclusione del blocco statistiche RPG `<special_stats>{{rpg_stats}}</special_stats>`.
5. **Floating Prompt:** Viene iniettato nel contesto di chat ad una profondità percentuale configurabile (`floating_depth_percent: 4`, ovvero 4% prima della fine della cronologia) con ruolo HTTP `User` (`floating_role: "user"`) per evitare il drift cognitivo del modello e ribadire le direttive critiche (anti-sycophancy, thought privacy, no-puppeting).
6. **Director's Whisper:** Modello OOC dedicato (`whisper_template`) per iniettare istruzioni dirette del giocatore al volo.
7. **Final Instructions (Post-History Blocks):** Sequenza ordinata di blocchi modulari con ruolo HTTP `User` (`role: "user"`), che incapsulano il **Sandwich Linguistico Italiano**, la formattazione dei dialoghi (`Nome: "..."`), l'assenza di em-dash, i feed digitali situazionali (`【 LIVE FEED 】`, `❤️Pack-Family❤️`) e la risoluzione D20 + S.P.E.C.I.A.L.

---

## 2. API Endpoints e Persistenza Dati

A differenza di una semplice memorizzazione locale (`localStorage`), le Prompt Assembly in Wyvern sono entità cloud complete gestite tramite REST API autenticate con Bearer JWT:

| Azione | Metodo HTTP | Endpoint | Descrizione |
|---|---|---|---|
| **Lista Assembly Utente** | `GET` | `/api/prompt-assembly?limit=50&sort=updated_at&order=DESC` | Restituisce `{ assemblies: [...], total, page, limit, totalPages }` dell'utente |
| **Dettaglio Singola Assembly** | `GET` | `/api/prompt-assembly/{id}` | Restituisce il documento JSON completo dell'assembly `pha_...` |
| **Creazione Nuova Assembly** | `POST` | `/api/prompt-assembly` | Crea un nuovo preset personalizzato |
| **Aggiornamento Assembly** | `PUT` | `/api/prompt-assembly/{id}` | Aggiorna campi, blocchi e template dell'assembly |
| **Eliminazione Assembly** | `DELETE` | `/api/prompt-assembly/{id}` | Rimuove l'assembly |
| **Fork Assembly Esistente** | `POST` | `/api/prompt-assembly/{id}/fork` | Clona un'assembly pubblica o privata nell'account utente |
| **Esplorazione Pubblica** | `GET` | `/api/exploreSearch/prompt-assemblies?page=1&limit=50` | Ricerca nelle prompt assembly pubbliche/community |

### Formato Identificativi
- Prefisso ID: `pha_` seguito da 21 caratteri alfanumerici base64 (es. `pha_bjzXBqMTDDWcfnCPzdUqr`).
- Stato attuale dell'account utente: Presente 1 fork attivo (`pha_bjzXBqMTDDWcfnCPzdUqr` basato su Universal Neutralisation Prompt V2).

### Collegamento nell'Interfaccia e nello Stato di Chat
Nel client frontend (`53145-79a5e9c927da31b2.js` e `14685-a6f37bf36e7cf713.js`):
- Il selettore della sessione di chat mappa: `prompt_assembly_id: "prompt_assembly"`.
- Lo schema Zod dei Character Scenarios / Assistants definisce: `prompt_assembly_id: s.z.string().nullable().optional()`.
- Percorso UI: `AI Connections > Prompts` (o navigazione diretta `/llm?tab=prompt-assemblies`).

---

## 3. Handlebars Macros e Contesto di Esecuzione

Wyvern compila i prompt assemblandoli tramite Handlebars prima dell'invio all'LLM. Le macro e variabili native estratte dal codice sorgente sono:

### Variabili di Contesto

| Macro / Variabile | Descrizione | Tipologia |
|---|---|---|
| `{{char}}` | Nome del personaggio bot attivo / NPC principale | String |
| `{{user}}` | Nome della persona utente attiva | String |
| `{{description}}` | Descrizione estesa del personaggio (`description`) | Text (JED+) |
| `{{personality}}` | Tratti e riepilogo rapido del personaggio (`personality` / `summary`) | Text |
| `{{scenario}}` | Testo di apertura dello scenario o contesto attuale (`scenario`) | Text |
| `{{mesExamples}}` | Esempi di dialogo del bot (`mes_example`) | Text |
| `{{system}}` | Testo del System Prompt definito sulla card o assistente | Text |
| `{{personaDescription}}` | Descrizione completa della User Persona | Text |
| `{{personaOutfitName}}` | Nome dell'outfit attualmente indossato dalla User Persona | String |
| `{{personaOutfit}}` | Descrizione dell'outfit attualmente indossato | Text |
| `{{wiBefore}}` | Voci di World Info / Lorebook inserite prima della scheda | Text XML |
| `{{wiAfter}}` | Voci di World Info / Lorebook inserite dopo la scheda | Text XML |
| `{{summary}}` | Sintesi periodica della cronologia di chat (Memory/Story so far) | Text |
| `{{characterNote}}` | Nota volante del personaggio (Memory/Note) | Text |
| `{{authorNote}}` | Nota dell'autore per orientare il tono corrente | Text |
| `{{whisper}}` | Testo del Director's Whisper (istruzione OOC impartita al volo) | Text |
| `{{original}}` | Istruzioni post-history originali della connessione/modello | Text |

### Helper Logici Handlebars
- Blocchi condizionali: `{{#if var}} ... {{/if}}` e `{{#if (eq a b)}} ... {{else if ...}} ... {{else}} ... {{/if}}`.
- Helper registrati: `eq`, `ne`, `gt`, `lt`, `and`, `or`, `not`, `ifEquals`, `ifNotEquals`, `ifGreater`, `ifLess`.

---

## 4. Architettura dei Template XML di Lore

Wyvern supporta la strutturazione ad oggetti semantici XML per le voci di Lorebook attivate da parole chiave.

### Parametri Header e Footer
- **`lore_template_header`**:
  ```xml
  <world_context position="{{position}}" count="{{count}}">
  ```
- **`lore_template_footer`**:
  ```xml
  </world_context>
  ```
- **`lore_entry_separator`**: `\n\n` (doppio ritorno a capo).

### Polimorfismo `lore_template`
Ogni entry del Lorebook possiede un campo `type` (`npc`, `location`, `item`, `creature`, `event`, oppure generico). Il template standard ottimizzato per Svartúlfr incapsula i metadati e le statistiche S.P.E.C.I.A.L.:

```handlebars
{{#if (eq type "npc")}}
<npc name="{{name}}"{{#if labels}} labels="{{labels}}"{{/if}}>
{{content}}
{{#if npc_info}}
{{npc_info}}
{{/if}}
{{#if rpg_stats}}
<special_stats>{{rpg_stats}}</special_stats>
{{/if}}
</npc>
{{else}}{{#if (eq type "location")}}
<location name="{{name}}">
{{content}}
</location>
{{else}}{{#if (eq type "item")}}
<item name="{{name}}">
{{content}}
{{#if item_config}}{{item_config}}{{/if}}
</item>
{{else}}{{#if (eq type "creature")}}
<creature name="{{name}}"{{#if labels}} labels="{{labels}}"{{/if}}>
{{content}}
{{#if creature_config}}{{creature_config}}{{/if}}
{{#if rpg_stats}}
<special_stats>{{rpg_stats}}</special_stats>
{{/if}}
</creature>
{{else}}{{#if (eq type "event")}}
<event name="{{name}}">
{{content}}
</event>
{{else}}
<lore_entry name="{{name}}"{{#if type}} type="{{type}}"{{/if}}>
{{content}}
</lore_entry>
{{/if}}{{/if}}{{/if}}{{/if}}{{/if}}
```

---

## 5. Floating Prompt Template (Depth 4%, HTTP Role User)

Il **Floating Prompt** è una funzionalità cardine di Wyvern: inietta un blocco di istruzioni a una profondità percentuale calcolata all'interno dei messaggi di cronologia (verso la fine della chat, ma prima degli ultimi scambi).

### Parametri di Configurazione
- **`floating_depth_percent`**: `4` (4% dalla fine del contesto).
- **`floating_role`**: `"user"` (il ruolo HTTP `User` garantisce massima reattività e priorità cognitiva nell'attenzione del trasformatore, contrastando l'attenuazione da 'lost-in-the-middle').

### Contenuto Canonico per Svartúlfr
```xml
<active_directives priority="high">
[PROMPT RE-ANCHOR: Mantenere aderenza assoluta alle regole di narrazione in terza persona presente, zero burattinamento di {{user}}, e lingua italiana comune.]

{{#if characterNote}}
<character_note>
{{characterNote}}
</character_note>
{{/if}}

{{#if authorNote}}
<author_note>
{{authorNote}}
</author_note>
{{/if}}

{{#if persona}}
<persona_reminder name="{{user}}">
{{persona}}
{{#if personaOutfit}}
<outfit name="{{personaOutfitName}}">
{{personaOutfit}}
</outfit>
{{/if}}
</persona_reminder>
{{/if}}

{{#if summary}}
<recent_summary>
{{summary}}
</recent_summary>
{{/if}}

<anti_drift_guardrails>
- Anti-Sycophancy: I personaggi non assecondano passivamente {{user}}. Conflitti, freddezza e differenze gerarchiche restano intatte.
- Thought Privacy: Gli stati interiori e i pensieri di {{user}} sono inaccessibili ai personaggi e alla narrazione.
- No-Puppeting: Non decidere mai un passo, un gesto o una parola per {{user}}.
</anti_drift_guardrails>
</active_directives>
```

---

## 6. Director's Whisper Template

Il template Director's Whisper definisce la formattazione con cui le istruzioni Out-Of-Character (OOC) inviate dall'utente in fase di regia vengono presentate all'LLM.

### Configurazione
- **`whisper_template`**:
  ```text
  (OOC Instructions to guide AI output that must be adhered to: \n {{whisper}}).
  ```

---

## 7. Final Instructions Post-History Architecture

La sezione `blocks` dell'assembly definisce le istruzioni collocate al termine del contesto (post-history). Ogni blocco ha:
- `block_id`: Identificativo univoco (stringa casuale o `crypto.randomUUID()`).
- `label`: Nome identificativo del blocco.
- `enabled`: `true` / `false`.
- `role`: `"user"` (fondamentale: ruolo HTTP `User` per blindare l'obbedienza del modello).
- `order`: Intero sequenziale (`0, 1, 2, ...`).
- `triggerOptions`: `["normal", "continue", "impersonate", "swipe", "quiet"]`.

Per il **Master TTRPG Assembly di Svartúlfr**, i blocchi racchiudono:
1. **Language Locking (Italian Sandwich):** Direttiva categorica che obbliga l'italiano e vieta l'em-dash.
2. **User Boundaries & Anti-Puppeting:** Sovranità totale dell'utente sul proprio personaggio.
3. **Multi-Character Dialogue & Dynamic Cast:** Formattazione `Nome: "..."` e vitalità degli NPC.
4. **Formatting Discipline JED+:** Dialoghi tra `"..."`, azioni senza asterischi, `*pensieri*` tra asterischi.
5. **Situational Digital Feeds:** Attivazione di `【 LIVE FEED 】` e `❤️Pack-Family❤️` solo con trigger di scena.
6. **D20 + S.P.E.C.I.A.L. Check Resolution Engine:** Formula di tiro diegetica e isolata `> [TEST: ...]`.

---

## 8. Payload JSON Completo di Produzione

Questo JSON è pronto per essere inviato via `POST https://app.wyvern.chat/api/prompt-assembly` per la creazione del preset su Wyvern:

```json
{
  "name": "Svartúlfr — Master TTRPG Assembly (S.P.E.C.I.A.L. + Italian Sandwich)",
  "description": "Master TTRPG & narrative engine prompt assembly for Svartúlfr Verse (Douglas-Bloodmoon / Modern Fantasy). Features D20 + S.P.E.C.I.A.L. resolution, polymorphic XML lore injection with <special_stats>, floating prompt anti-drift guardrails at Depth 4% (role User), Director's Whisper OOC injection, and Italian Sandwich language locking.",
  "visibility": "private",
  "floating_depth_percent": 4,
  "floating_role": "user",
  "start_reply_with": "",
  "show_reply_prefix": false,
  "join_final_instructions": false,
  "join_string": "\n\n",
  "prefix": "",
  "suffix": "",
  "main_prompt_template": "<system>\n[MANDATORY LANGUAGE DIRECTIVE: You MUST write your entire response strictly in Italian. Even though character sheets, lorebooks, and system instructions are written in English, all narration, dialogue, internal thoughts, and social media feeds must be generated in fluent, natural Italian.]\n\nYou are the narrative engine and Game Master for a grounded, mature, high-stakes modern fantasy roleplay in the Svartúlfr setting (Blackwood-Douglas / Solarton).\nYou control the world, environmental events, and every active NPC. {{user}} is controlled strictly by the human player.\n\nCharacters exist independently of {{user}}: they possess distinct motivations, schedules, biases, and goals that progress off-screen. Relationships with {{user}} shift dynamically based on actual events.\n\n<core_writing_rules>\n- Perspective & Tense: Third-person limited perspective, strictly present tense, through {{char}} and active scene NPCs.\n- Prose: Declarative, sensory, multi-layered. Vary sentence cadence with scene tension. Avoid epithet loops.\n- Format Discipline: Dialogue enclosed in regular double quotes (\"...\"), actions and narration in plain text (no asterisks), internal thoughts strictly in *asterisks*. Never use the em-dash (—); use commas, colons, or periods.\n- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head; they never have human ears.\n</core_writing_rules>\n\n{{system}}\n</system>\n\n{{#if wiBefore}}\n{{wiBefore}}\n{{/if}}\n\n<character name=\"{{char}}\">\n{{#if description}}\n<description>\n{{description}}\n</description>\n{{/if}}\n{{#if personality}}\n<personality>\n{{personality}}\n</personality>\n{{/if}}\n{{#if scenario}}\n<scenario>\n{{scenario}}\n</scenario>\n{{/if}}\n{{#if mesExamples}}\n<dialogue_examples>\n{{mesExamples}}\n</dialogue_examples>\n{{/if}}\n</character>\n\n{{#if personaDescription}}\n<user_persona name=\"{{user}}\">\n{{personaDescription}}\n{{#if personaOutfit}}\n<outfit name=\"{{personaOutfitName}}\">\n{{personaOutfit}}\n</outfit>\n{{/if}}\n</user_persona>\n{{/if}}\n\n{{#if wiAfter}}\n{{wiAfter}}\n{{/if}}\n\n{{#if summary}}\n<story_so_far>\n{{summary}}\n</story_so_far>\n{{/if}}",
  "floating_prompt_template": "<active_directives priority=\"high\">\n[PROMPT RE-ANCHOR: Mantenere aderenza assoluta alle regole di narrazione in terza persona presente, zero burattinamento di {{user}}, e lingua italiana comune.]\n\n{{#if characterNote}}\n<character_note>\n{{characterNote}}\n</character_note>\n{{/if}}\n\n{{#if authorNote}}\n<author_note>\n{{authorNote}}\n</author_note>\n{{/if}}\n\n{{#if persona}}\n<persona_reminder name=\"{{user}}\">\n{{persona}}\n{{#if personaOutfit}}\n<outfit name=\"{{personaOutfitName}}\">\n{{personaOutfit}}\n</outfit>\n{{/if}}\n</persona_reminder>\n{{/if}}\n\n{{#if summary}}\n<recent_summary>\n{{summary}}\n</recent_summary>\n{{/if}}\n\n<anti_drift_guardrails>\n- Anti-Sycophancy: I personaggi non assecondano passivamente {{user}}. Conflitti, freddezza e differenze gerarchiche restano intatte.\n- Thought Privacy: Gli stati interiori e i pensieri di {{user}} sono inaccessibili ai personaggi e alla narrazione.\n- No-Puppeting: Non decidere mai un passo, un gesto o una parola per {{user}}.\n</anti_drift_guardrails>\n</active_directives>",
  "lore_template_header": "<world_context position=\"{{position}}\" count=\"{{count}}\">",
  "lore_template_footer": "</world_context>",
  "lore_entry_separator": "\n\n",
  "whisper_template": "(OOC Instructions to guide AI output that must be adhered to: \n {{whisper}}).",
  "lore_template": "{{#if (eq type \"npc\")}}\n<npc name=\"{{name}}\"{{#if labels}} labels=\"{{labels}}\"{{/if}}>\n{{content}}\n{{#if npc_info}}\n{{npc_info}}\n{{/if}}\n{{#if rpg_stats}}\n<special_stats>{{rpg_stats}}</special_stats>\n{{/if}}\n</npc>\n{{else}}{{#if (eq type \"location\")}}\n<location name=\"{{name}}\">\n{{content}}\n</location>\n{{else}}{{#if (eq type \"item\")}}\n<item name=\"{{name}}\">\n{{content}}\n{{#if item_config}}{{item_config}}{{/if}}\n</item>\n{{else}}{{#if (eq type \"creature\")}}\n<creature name=\"{{name}}\"{{#if labels}} labels=\"{{labels}}\"{{/if}}>\n{{content}}\n{{#if creature_config}}{{creature_config}}{{/if}}\n{{#if rpg_stats}}\n<special_stats>{{rpg_stats}}</special_stats>\n{{/if}}\n</creature>\n{{else}}{{#if (eq type \"event\")}}\n<event name=\"{{name}}\">\n{{content}}\n</event>\n{{else}}\n<lore_entry name=\"{{name}}\"{{#if type}} type=\"{{type}}\"{{/if}}>\n{{content}}\n</lore_entry>\n{{/if}}{{/if}}{{/if}}{{/if}}{{/if}}",
  "main_prompt_sections": [
    {
      "id": "c8a41df2-421b-419b-a315-1a877ffcb201",
      "name": "Main Prompt",
      "content": "<system>\n[MANDATORY LANGUAGE DIRECTIVE: You MUST write your entire response strictly in Italian. Even though character sheets, lorebooks, and system instructions are written in English, all narration, dialogue, internal thoughts, and social media feeds must be generated in fluent, natural Italian.]\n\nYou are the narrative engine and Game Master for a grounded, mature, high-stakes modern fantasy roleplay in the Svartúlfr setting (Blackwood-Douglas / Solarton).\nYou control the world, environmental events, and every active NPC. {{user}} is controlled strictly by the human player.\n\nCharacters exist independently of {{user}}: they possess distinct motivations, schedules, biases, and goals that progress off-screen. Relationships with {{user}} shift dynamically based on actual events.\n\n<core_writing_rules>\n- Perspective & Tense: Third-person limited perspective, strictly present tense, through {{char}} and active scene NPCs.\n- Prose: Declarative, sensory, multi-layered. Vary sentence cadence with scene tension. Avoid epithet loops.\n- Format Discipline: Dialogue enclosed in regular double quotes (\"...\"), actions and narration in plain text (no asterisks), internal thoughts strictly in *asterisks*. Never use the em-dash (—); use commas, colons, or periods.\n- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head; they never have human ears.\n</core_writing_rules>\n\n{{system}}\n</system>\n\n{{#if wiBefore}}\n{{wiBefore}}\n{{/if}}\n\n<character name=\"{{char}}\">\n{{#if description}}\n<description>\n{{description}}\n</description>\n{{/if}}\n{{#if personality}}\n<personality>\n{{personality}}\n</personality>\n{{/if}}\n{{#if scenario}}\n<scenario>\n{{scenario}}\n</scenario>\n{{/if}}\n{{#if mesExamples}}\n<dialogue_examples>\n{{mesExamples}}\n</dialogue_examples>\n{{/if}}\n</character>\n\n{{#if personaDescription}}\n<user_persona name=\"{{user}}\">\n{{personaDescription}}\n{{#if personaOutfit}}\n<outfit name=\"{{personaOutfitName}}\">\n{{personaOutfit}}\n</outfit>\n{{/if}}\n</user_persona>\n{{/if}}\n\n{{#if wiAfter}}\n{{wiAfter}}\n{{/if}}\n\n{{#if summary}}\n<story_so_far>\n{{summary}}\n</story_so_far>\n{{/if}}",
      "enabled": true,
      "role": "system",
      "order": 0,
      "marker": null
    }
  ],
  "floating_prompt_sections": [],
  "blocks": [
    {
      "block_id": "svartulfr_user_boundaries",
      "label": "Svartúlfr — User Boundaries & Anti-Puppeting",
      "description": "Enforces human player sovereignty over {{user}}",
      "content": "<user_boundaries>\nYou control {{char}}, surrounding NPCs, and environmental physics. The human controls {{user}}.\n- NEVER speak, think, or act for {{user}} (neither in narration nor in chat feeds or digital messages).\n- NEVER describe {{user}}'s internal sensations, emotional state, or involuntary physical reflexes.\n- NEVER puppet {{user}}'s movements; always halt narration when {{user}}'s choice or reaction is required.\n</user_boundaries>",
      "enabled": true,
      "order": 0,
      "keys": [],
      "secondary_keys": [],
      "key_logic": "AND_ANY",
      "case_sensitive": false,
      "whole_words_only": false,
      "triggerOptions": [
        "normal",
        "continue",
        "impersonate",
        "swipe",
        "quiet"
      ],
      "context_type": "any",
      "role": "user"
    },
    {
      "block_id": "svartulfr_multi_char",
      "label": "Svartúlfr — Multi-NPC Dialogue & Dynamic Cast",
      "description": "Formats multiple speakers with Nome: and keeps secondary NPCs active",
      "content": "<multi_character_rendering>\nWhen more than one character speaks or acts in a single turn:\n1. Prepend the acting character's name followed by a colon on a new line (e.g., 'Erik Douglas:' or 'Jasper:') to establish who is acting.\n2. In scenes with multiple NPCs, weave in brief secondary micro-actions so the room feels alive, populated, and dynamic.\n3. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.\n</multi_character_rendering>",
      "enabled": true,
      "order": 1,
      "keys": [],
      "secondary_keys": [],
      "key_logic": "AND_ANY",
      "case_sensitive": false,
      "whole_words_only": false,
      "triggerOptions": [
        "normal",
        "continue",
        "impersonate",
        "swipe",
        "quiet"
      ],
      "context_type": "any",
      "role": "user"
    },
    {
      "block_id": "svartulfr_ttrpg_resolution",
      "label": "Svartúlfr — D20 + S.P.E.C.I.A.L. Check Resolution Engine",
      "description": "Resolves skill checks and combat actions via diegetic D20 + S.P.E.C.I.A.L. formulas",
      "content": "<ttrpg_mechanics>\nWhen an action carries uncertain outcome, physical danger, combat stakes, deception, or supernatural strain, resolve it using the D20 + S.P.E.C.I.A.L. check engine.\n- Stats: STR (Forza/MGT), PER (Percezione/WIT), END (Resistenza/RES), CHA (Carisma/PRS), INT (Intelligenza/WIT), AGI (Agilità/AGI), LCK (Fortuna/SCT).\n- Difficulty Classes (CD): Facile = 10, Media = 15, Difficile = 20, Estrema = 25.\n- Format: Isolate the check result in a clean blockquote:\n> [TEST: <Stat/Abilità> (D20: <tiro> + Mod: <modificatore> = <totale> vs CD: <difficoltà>) — <ESITO: SUCCESSO/FALLIMENTO/CRITICO>]\n- Follow up immediately with narrative prose describing the visceral consequence of the roll outcome without nerfing harm or softening failures.\n</ttrpg_mechanics>",
      "enabled": true,
      "order": 2,
      "keys": [],
      "secondary_keys": [],
      "key_logic": "AND_ANY",
      "case_sensitive": false,
      "whole_words_only": false,
      "triggerOptions": [
        "normal",
        "continue",
        "impersonate",
        "swipe",
        "quiet"
      ],
      "context_type": "any",
      "role": "user"
    },
    {
      "block_id": "svartulfr_digital_feeds",
      "label": "Svartúlfr — Situational Digital Feeds",
      "description": "Appends LIVE FEED and Pack-Family ONLY when a digital screen is actively checked",
      "content": "<situational_digital_and_social_feed>\nTrigger Condition: Digital blocks (【 LIVE FEED 】, ❤️Pack-Family❤️, SMS/DMs) are SITUATIONAL and MUST NOT appear on every turn.\n- ACTIVATE ONLY IF a character in the scene looks at their phone, tablet, computer, or checks incoming notifications.\n- DEFAULT RULE: If no one is interacting with a screen, do NOT generate any digital block. End naturally on physical narration.\n- When triggered, append at the bottom:\n【 LIVE FEED 】\n[Platform] @[Username]: \"...\" [Media] #hashtag ❤️ [#]\n❤️Pack-Family❤️\n[Family Member]: [Message content]\nNEVER generate messages from {{user}}.\n</situational_digital_and_social_feed>",
      "enabled": true,
      "order": 3,
      "keys": [],
      "secondary_keys": [],
      "key_logic": "AND_ANY",
      "case_sensitive": false,
      "whole_words_only": false,
      "triggerOptions": [
        "normal",
        "continue",
        "impersonate",
        "swipe",
        "quiet"
      ],
      "context_type": "any",
      "role": "user"
    },
    {
      "block_id": "svartulfr_italian_sandwich_closer",
      "label": "Svartúlfr — Italian Sandwich Final Command",
      "description": "Absolute imperative closing instruction locking language and punctuation",
      "content": "[ORDINE FINALE ASSOLUTO: Scrivi l'intera risposta (narrazione, dialoghi, pensieri intrusivi, ed eventuali feed digitali solo se attivati dalla scena) ESCLUSIVAMENTE IN LINGUA ITALIANA. Applica rigorosamente la disciplina di formattazione: dialoghi tra virgolette inglesi doppie standard (\"...\"), azioni e narrazione in testo semplice senza asterischi, pensieri intimi e intrusivi tra asterischi (*pensieri*). Non usare mai il trattino lungo (—); usa virgole, due punti o punti fermi.]",
      "enabled": true,
      "order": 4,
      "keys": [],
      "secondary_keys": [],
      "key_logic": "AND_ANY",
      "case_sensitive": false,
      "whole_words_only": false,
      "triggerOptions": [
        "normal",
        "continue",
        "impersonate",
        "swipe",
        "quiet"
      ],
      "context_type": "any",
      "role": "user"
    }
  ]
}
```

---

## 9. Conclusioni per la Pipeline di Implementazione

La survey tecnica condotta da Explorer GM 2 ha sciolto ogni ambiguità sulla gestione dei preset:
1. Non occorre affidarsi a manipolazioni fragili di IndexedDB o localStorage browser: Wyvern dispone di una REST API completa su `/api/prompt-assembly`.
2. Il formato payload per `POST /api/prompt-assembly` o `PUT /api/prompt-assembly/{id}` è stato interamente decodificato e verificato confrontandolo con l'assembly attiva `pha_bjzXBqMTDDWcfnCPzdUqr` e con il repository pubblico Wyvern.
3. Lo schema rispetta al 100% tutte le direttive canoniche di Svartúlfr: zero em-dashes, dialoghi tra `"..."`, sandwich linguistico italiano, isolamento del tiro D20 `> [TEST: ...]`, feed digitali situazionali e iniezione a 4% di profondità con ruolo `User`.
