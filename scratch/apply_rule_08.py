with open('.agents/rules/08_triage_lorebook_e_lexicon.md', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

new_block = [
    '3. **Workflow Obbligatorio Gallery & Riconciliazione Asset (`GET /api/gallery/lorebook/{lorebook_id}`):**\n',
    '   - L\'endpoint ufficiale della Gallery del Lorebook su Wyvern è `GET /api/gallery/lorebook/{lorebook_id}` (upload via `POST /api/gallery/lorebook/{lorebook_id}`).\n',
    '   - Associare `entry.avatar` selezionando la thumbnail Cloudflare registrata nella Gallery. L\'URL deve coincidere byte-for-byte con l\'asset della Gallery per evitare che il frontend lo contrassegni come `Custom Image ⚠️ Unknown source`.\n',
    '   - **Parità di Validazione Zod Frontend (`entries == lexicon`):** Il form editor di Wyvern (`react-hook-form` con schema Zod) richiede tassativamente che la proprietà `entries` sia popolata come array (`entries: z.array(...)`). Mantenere sempre `entries` e `lexicon` identici byte-for-byte in ogni salvataggio per evitare il blocco silenzioso con errore `entries: Required`.\n'
]

lines[126:129] = new_block

with open('.agents/rules/08_triage_lorebook_e_lexicon.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Updated .agents/rules/08_triage_lorebook_e_lexicon.md successfully!")
