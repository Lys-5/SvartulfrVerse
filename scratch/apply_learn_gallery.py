# 2. Update 08_triage_lorebook_e_lexicon.md
path08 = '.agents/rules/08_triage_lorebook_e_lexicon.md'
with open(path08, 'r', encoding='utf-8') as f:
    c08 = f.read()

target08 = '5. **Standard Obbligatorio Metadati per Entry NPC (Avatar Parsing & UI Splitting):**'
addition08 = '''- **Workflow Immagini & Avatar tramite Gallery:** È tassativamente vietato tentare l'upload diretto di file immagine all'interno dei singoli record o entry del Lorebook (causa errori e mancata persistenza). La procedura canonica corretta prevede:
  1. Caricamento preventivo dei file immagine nella **Gallery** del Lorebook (`gallery[]`);
  2. Assegnazione dell'avatar a ciascuna entry mediante **selezione dalla Gallery** (o URL pubblico registrato nel pool).
'''

if target08 in c08 and addition08 not in c08:
    c08 = c08.replace(target08, f'{addition08}\n{target08}')
    with open(path08, 'w', encoding='utf-8') as f:
        f.write(c08)
    print('Updated rule 08')

# 3. Update GEMINI.md
path_gemini = 'GEMINI.md'
with open(path_gemini, 'r', encoding='utf-8') as f:
    cg = f.read()

target_gemini = '- **HTTP 413 Payload Too Large su Lorebook PUT:** Non includere nel payload JSON sia l\'array legacy `entries` sia l\'array canonico `lexicon` (raddoppia la dimensione). Inviare solo `lexicon` unitamente ai metadati top-level.'
addition_gemini = '''- **Errore Caricamento Immagini su Singola Entry Lorebook:** L'upload diretto di file immagine/avatar nei singoli slot delle entry genera errori o fallimenti di persistenza su Wyvern. Seguire il **Workflow Obbligatorio Gallery**: non caricare file direttamente sulle singole entry, ma caricare prima le immagini nella **GALLERY del Lorebook**, e successivamente selezionare l'immagine desiderata dalla Gallery per ciascuna entry (`entry.avatar`).'''

if target_gemini in cg and addition_gemini not in cg:
    cg = cg.replace(target_gemini, f'{target_gemini}\n{addition_gemini}')
    with open(path_gemini, 'w', encoding='utf-8') as f:
        f.write(cg)
    print('Updated GEMINI.md')
