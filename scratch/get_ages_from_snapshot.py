import json
import pathlib

p = pathlib.Path('ARCHIVIO/05_Snapshots_and_Extractions/entities/Svartulfr_Characters.json')
data = json.loads(p.read_text(encoding='utf-8', errors='ignore'))
entries = data.get('entries', [])

target_names = ['Elizabeth Duskwood', 'Kaladin', 'Mackenzie', 'Magnus Douglas', 'Zeera', 'Aras', 'Boros', 'Karshin', 'Varg', 'Stanley Davies']

for e in entries:
    name = e.get('name') or ''
    for t in target_names:
        if t.lower() in name.lower():
            b = e.get('birthdate')
            summary = e.get('summary', '')
            desc = e.get('display_description', '')
            print(f"=== {name} ({e.get('id')}) ===")
            print(f"  birthdate (hours): {b}")
            # check if age mentioned in summary
            for line in summary.splitlines()[:5]:
                print(f"  summary: {line[:100]}")
            break
