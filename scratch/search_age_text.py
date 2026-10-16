import json
import pathlib
import re

p = pathlib.Path('ARCHIVIO/05_Snapshots_and_Extractions/entities/Svartulfr_Characters.json')
data = json.loads(p.read_text(encoding='utf-8', errors='ignore'))
entries = data.get('entries', [])

target_names = ['Elizabeth Duskwood', 'Kaladin', 'Mackenzie', 'Magnus Douglas', 'Zeera', 'Stanley Davies Jr.']

for e in entries:
    name = e.get('name') or ''
    for t in target_names:
        if t.lower() in name.lower():
            txt = e.get('summary', '') + ' ' + e.get('display_description', '')
            print(f"=== {name} ===")
            # Look for numbers or age mentions
            ages = re.findall(r'(?:age|years old|born|\b\d{1,3}\b)[^;\n]{0,30}', txt, re.IGNORECASE)
            print("  Mentions:", ages[:10])
            break
