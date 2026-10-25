with open('.agents/rules/08_triage_lorebook_e_lexicon.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = '     - Associare `entry.avatar` selezionando la thumbnail Cloudflare (`https://imagedelivery.net/...`) dalla Gallery salvata.'
replacement = '''     - Associare `entry.avatar` selezionando la thumbnail Cloudflare (`https://imagedelivery.net/...`) dalla Gallery salvata (`GET /api/gallery/lorebook/{lorebook_id}`). L'URL deve coincidere byte-for-byte con il record Gallery per prevenire l'avviso `Custom Image ⚠️ Unknown source`.
     - **Parità Zod Schema Frontend (`entries == lexicon`):** Il form editor di Wyvern richiede che `entries` sia presente come array (`entries: z.array(...)`). Mantenere sempre `entries` e `lexicon` identici byte-for-byte in ogni salvataggio per evitare il blocco silenzioso con errore `entries: Required`.'''

if target in text:
    text = text.replace(target, replacement)
    with open('.agents/rules/08_triage_lorebook_e_lexicon.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("08_triage_lorebook_e_lexicon.md updated successfully.")
else:
    print("Target not found in 08_triage_lorebook_e_lexicon.md")
