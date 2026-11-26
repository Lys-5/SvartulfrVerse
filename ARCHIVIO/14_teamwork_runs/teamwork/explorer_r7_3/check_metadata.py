import json

for path in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"=== {path} ===")
    for k, v in data.items():
        if k not in ['entries', 'lexicon']:
            print(f"  {k}: {repr(v)}")
