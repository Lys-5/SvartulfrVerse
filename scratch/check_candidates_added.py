import json
import glob

candidates = [
    'Russ',
    'Neon Purr',
    'Thrakgor',
    'Warg',
    'Crowe',
    'Morgeth',
    'Thorvald',
    'Harald',
    'Nova Farm',
    'Rory Ballantine'
]

found = {c: [] for c in candidates}

for f in sorted(glob.glob('FINAL/*.json')):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        
        entries = []
        if isinstance(data, dict):
            if 'lexicon' in data:
                entries = data['lexicon']
            elif 'entries' in data:
                entries = data['entries']
            elif 'name' in data:
                entries = [data]
        
        for e in entries:
            name = e.get('name', '')
            desc = e.get('description', '')
            keys = str(e.get('keys', ''))
            
            for c in candidates:
                if c.lower() in name.lower() or c.lower() in keys.lower():
                    found[c].append((f, name, e.get('type', 'card')))
    except Exception as err:
        pass

for c, locs in found.items():
    print(f"=== {c} ===")
    if locs:
        for loc in locs:
            print(f"   Found in {loc[0]} -> Name: '{loc[1]}', Type: {loc[2]}")
    else:
        print("   NOT FOUND!")
