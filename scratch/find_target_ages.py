import json
import pathlib

root = pathlib.Path('.')
names = ['Elizabeth', 'Jared', 'Kaladin', 'Mackenzie', 'Mac', 'Magnus', 'Zeera', 'Aras', 'Boros', 'Karshin', 'Varg']

for p in root.glob('**/*.json'):
    if 'FINAL' in str(p) or 'entities' in str(p) or 'scratch' in str(p):
        try:
            txt = p.read_text(encoding='utf-8', errors='ignore')
            for n in ['Elizabeth_Duskwood', 'Jared_Thompson', 'Kaladin_Nargathon', 'Mackenzie', 'Magnus_Douglas', 'Zeera_Darkfire']:
                if n in str(p):
                    # print some age info
                    data = json.loads(txt)
                    if isinstance(data, dict):
                        print(f"File: {p.name}")
                        print(f"  name: {data.get('name')}")
                        print(f"  birthdate: {data.get('birthdate')}")
                        print(f"  character_note: {data.get('character_note')}")
                        print(f"  tagline: {data.get('tagline')}")
        except:
            pass
