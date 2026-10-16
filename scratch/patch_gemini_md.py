with open('GEMINI.md', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()

new_block = [
    '    - **Disciplina dei Ruoli per gli Slot (`slots`):**',
    '      - Gli slot non utilizzano i nomi dei personaggi ma esclusivamente i ruoli funzionali o relazionali:',
    '        - `maternal_grandfather` -> Wulfnic Báleygr Bloodmoon (`_HEQQbbRFwKdG8QE2Fh1z1`)',
    '        - `paternal_grandfather` -> Magnus Douglas III (`_dJ7nRMQEbcUgdWG96MqLz`)',
    '        - `paternal_grandmother` -> Elizabeth Duskwood (`_zBD6rWUkJBAjLfXnja4xh`)',
    '        - `father` -> Erik Ulfr Douglas (`_QPea6g4Q1QfeYCVHCLMPR`)',
    '        - `twin` -> Pool bilanciato: Jasper Svartr (`_t4J9aQNJM36cUKAP4wB4U`) + Alyssa Hvit (`_6exg3yPfe2eCDK4hTftkh`)',
    '        - `brother` -> Noah Loki Douglas Bloodmoon (`_zFLUjV8aVxQRAfQxGcAcY`)',
    '        - `eldest_brother` -> Malachia Björn Douglas Bloodmoon (`_RDfz7XzTpM23LpPALVXHM`)',
    '        - `uncle` -> Logan Járn Douglas (`_T8Ywcr9FEqNf9JxbK6eHP`)',
    '        - `cousin` -> Edric Douglas (`_TbRM3EdxDjHFgqztTbCpL`)',
    '        - `boss` -> Zeera Darkfire (`_3tMk6cRAFewRnKMkdJ4XU`)',
    '        - `quarterback` -> Jared Thompson (`_xJVPtBLL3dxy69RLKL9X9`)',
    '        - `crush` -> Mackenzie "Mac" Sanchez-Rogers (`_zn24784jfcchQ7EwCyAnm`)',
    '        - `major` -> Major Kaladin Blackwolf Nargathon (`_EnRGd1jfbjTTGmz4EFJdd`)',
    '      - *Card esterne del portale:* I personaggi pubblici di altri autori (come Marek di Kakihara) non possono essere inseriti nei pool degli slot per vincoli API; nelle scene corali il loro speaker_slot è affidato a `twin` (Jasper o Alyssa a vegliare sulla scena) preservando intatti i dialoghi dell\'Oni.'
]

lines[490:492] = new_block
with open('GEMINI.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print("Successfully replaced lines in GEMINI.md!")
