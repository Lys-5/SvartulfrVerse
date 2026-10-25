import json
import glob

for fpath in glob.glob('FINAL/*_card.json'):
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        cid = data.get('id')
        name = data.get('name')
        print(f"{cid} -> {name} ({fpath})")
