import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
master_file = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
data = json.loads(master_file.read_text(encoding='utf-8'))

greetings = data.get('greetings', [])
print(f"Master Scenario greetings count: {len(greetings)}")

for idx, g in enumerate(greetings):
    gid = g.get('id', '')
    gname = g.get('name', '')
    gdesc = g.get('description', '')
    glp = g.get('linked_persona_ids', [])
    content = g.get('content', '')
    first_msg = g.get('messages', [{}])[0].get('content', '') if g.get('messages') else ''
    preview = (content or first_msg)[:80].replace('\n', ' ')
    
    # check for FemPOV / MalePOV or POV indicators in name, desc, content
    pov_indicator = []
    text_to_check = f"{gname} {gdesc} {preview}"
    if '[FemPOV]' in text_to_check or 'FemPOV' in text_to_check:
        pov_indicator.append('[FemPOV]')
    if '[MalePOV]' in text_to_check or 'MalePOV' in text_to_check:
        pov_indicator.append('[MalePOV]')
    if 'Alyssa' in gname or 'Alyssa' in gdesc:
        pov_indicator.append('Alyssa in meta')
    if 'Jasper' in gname or 'Jasper' in gdesc:
        pov_indicator.append('Jasper in meta')

    print(f"[{idx:02d}] ID: {gid[:12]} | Name: '{gname}' | linked_persona_ids: {glp} | POV: {pov_indicator} | Preview: {preview[:60]}")
