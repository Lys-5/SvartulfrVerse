with open('GEMINI.md', 'r', encoding='utf-8') as f:
    cg = f.read()

idx = cg.find("- **HTTP 413 Payload Too Large su Lorebook PUT:**")
if idx != -1:
    end_idx = cg.find('\n', idx)
    line = cg[idx:end_idx]
    addition_gemini = "\n- **Errore Caricamento Immagini su Singola Entry Lorebook:** L'upload diretto di file immagine/avatar nei singoli slot delle entry genera errori o fallimenti di persistenza su Wyvern. Seguire il **Workflow Obbligatorio Gallery**: non caricare file direttamente sulle singole entry, ma caricare prima le immagini nella **GALLERY del Lorebook**, e successivamente selezionare l'immagine desiderata dalla Gallery per ciascuna entry (`entry.avatar`)."
    if addition_gemini not in cg:
        cg = cg[:end_idx] + addition_gemini + cg[end_idx:]
        with open('GEMINI.md', 'w', encoding='utf-8') as f:
            f.write(cg)
        print('Updated GEMINI.md')
    else:
        print('Already present in GEMINI.md')
