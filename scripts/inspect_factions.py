import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

lex = {l['id']: l for l in world_data['world_lexicon_entries']}
for lid in ['_LyHK91bhWrej3K4XyWW6h', '_C6JqdNxNgtqeneW1DxbrK', '_X2qqf3HhhdMahnhFUW3j7']:
    item = lex.get(lid, {})
    print(f"=== {item.get('name')} [{lid}] ===")
    print("Type:", item.get('type'))
    print("Avatar:", item.get('avatar'))
    print("Keys:", item.get('keys'))
    print("Content:\n", item.get('content'))
    print("-" * 50)
