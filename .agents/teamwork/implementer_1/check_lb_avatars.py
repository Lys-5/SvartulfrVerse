import json
from pathlib import Path
ROOT = Path(r'e:\repository\SvartulfrVerse')

c_ids = {
    '_TbRM3EdxDjHFgqztTbCpL': 'Edric',
    '_QPea6g4Q1QfeYCVHCLMPR': 'Erik',
    '_t4J9aQNJM36cUKAP4wB4U': 'Jasper',
    '_T8Ywcr9FEqNf9JxbK6eHP': 'Logan',
    '_zn24784jfcchQ7EwCyAnm': 'Mackenzie',
    '_RDfz7XzTpM23LpPALVXHM': 'Malachia',
    '_zFLUjV8aVxQRAfQxGcAcY': 'Noah',
    '_HEQQbbRFwKdG8QE2Fh1z1': 'Wulfnic'
}

files_to_check = [
    ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json',
    ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json',
    ROOT / 'FINAL' / 'Svartulfr_NPC_Secondary.json',
    ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Secondary.json'
]

for p in files_to_check:
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print('===', p.relative_to(ROOT), '===')
    for e in d.get('lexicon', []):
        for cid, name in c_ids.items():
            if cid in e.get('ignored_characters', []):
                print(f'  {name:10} -> avatar: {e.get("avatar")}')
