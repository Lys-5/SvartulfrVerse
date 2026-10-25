import os

# 1. Update GEMINI.md
with open('GEMINI.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = '    - **Standard Obbligatorio Metadati NPC & Terna di Flag (Wyvern VN Mega Patch):**'
idx = text.find(target)
end_target = '  - **Soppressione Nativa Wyvern ("Don\'t Activate When Active"): `ignored_characters` & `ignored_personas`:**'
end_idx = text.find(end_target)

if idx != -1 and end_idx != -1:
    replacement = '''    - **Standard Obbligatorio Metadati NPC & Terna di Flag (Wyvern VN Mega Patch):**
      Ogni entry `npc` deve possedere l'oggetto `npc_info` completo con `first_name` (obbligatorio), `middle_names` (array), `last_name` (opzionale), `nicknames` (array), `titles` (array) e `npc_prefix` (stringa o vuoto), sfruttando la compilazione automatica pesata delle regex del frontend Wyvern (modulo 93312 / WH).
    - **Terna di Flag Obbligatoria su ON (`true`):**
      - `scan_persona: true` (Scan Persona: Yes): garantisce la scansione dei trigger anche all'interno della User Persona attiva.
      - `whole_words_only: true` (Whole Words Only: Yes): previene attivazioni spurie su sottostringhe parziali.
      - `enableEntryHighlighting: true` / `highlight_keys: true`: attiva l'evidenziazione visiva delle entry attivate nei messaggi della chat.
    - **Workflow Obbligatorio Gallery & Riconciliazione Asset (`GET /api/gallery/lorebook/{lorebook_id}`):**
      - L'endpoint ufficiale della Gallery Lorebook su Wyvern è `GET /api/gallery/lorebook/{lorebook_id}` (upload via `POST /api/gallery/lorebook/{lorebook_id}`).
      - Il campo `entry.avatar` deve contenere esattamente la stringa `imageURL` registrata nella Gallery del Lorebook. Se l'URL non coincide byte-for-byte con un asset censito nella Gallery del Lorebook, il frontend di Wyvern visualizza l'avviso di anomalia `Custom Image ⚠️ Unknown source`.
      - **Parità di Validazione Zod Frontend (`entries == lexicon`):** Il form editor di Wyvern (`react-hook-form` con schema Zod) richiede tassativamente che la proprietà `entries` sia popolata come array (`entries: z.array(...)`). Poiché il server GET invia le voci sotto la chiave `lexicon`, qualsiasi payload o stato deve mantenere `entries` e `lexicon` identici byte-for-byte per evitare blocchi silenziosi al salvataggio con errore `entries: Required`.
'''
    text = text[:idx] + replacement + text[end_idx:]
    with open('GEMINI.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("GEMINI.md updated successfully.")

# 2. Update .agents/rules/08_triage_lorebook_e_lexicon.md
rule_path = '.agents/rules/08_triage_lorebook_e_lexicon.md'
if os.path.exists(rule_path):
    with open(rule_path, 'r', encoding='utf-8') as f:
        rtext = f.read()
    ridx = rtext.find(target)
    rend_idx = rtext.find(end_target)
    if ridx != -1 and rend_idx != -1:
        rtext = rtext[:ridx] + replacement + rtext[rend_idx:]
        with open(rule_path, 'w', encoding='utf-8') as f:
            f.write(rtext)
        print(f"{rule_path} updated successfully.")

# 3. Update .agents/skills/wyvern-card-lorebook-sync/SKILL.md
skill_path = '.agents/skills/wyvern-card-lorebook-sync/SKILL.md'
if os.path.exists(skill_path):
    with open(skill_path, 'r', encoding='utf-8') as f:
        stext = f.read()
    gallery_addition = '''
### 6. Riconciliazione Asset Gallery Lorebook (`GET /api/gallery/lorebook/{id}`)
* **Endpoint Ufficiale**: Le immagini registrate nella Gallery del Lorebook risiedono su `GET /api/gallery/lorebook/{lorebook_id}`.
* **Binding URL Diretto**: Assegnare a ciascuna entry l'esatto `imageURL` del corrispondente record di Gallery (es. `erikMain` -> `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public`). Questo elimina l'avviso `Custom Image ⚠️ Unknown source`.
* **Zod Schema Parity**: Mantenere sempre `entries` e `lexicon` identici byte-for-byte in ogni payload di salvataggio per evitare l'errore silenzioso di validazione frontend `entries: Required`.
'''
    if 'Riconciliazione Asset Gallery Lorebook' not in stext:
        stext += gallery_addition
        with open(skill_path, 'w', encoding='utf-8') as f:
            f.write(stext)
        print(f"{skill_path} updated successfully.")
