import json
import pathlib

MY_DIR = pathlib.Path(__file__).parent
data = json.loads((MY_DIR / 'all_macros_extracted.json').read_text(encoding='utf-8'))

print("=== ALYSSA TARGET NPC MACROS ===")
for m in data['alyssa']:
    if m['key'] in ['best_friend', 'roommate', 'quarterback', 'friend']:
        print(f"G{m['greeting_idx']} | {m['location']} | key: '{m['key']}'")
        print(f"   Context: {repr(m['context'])}")

print("\n=== JASPER TARGET NPC MACROS ===")
for m in data['jasper']:
    if m['key'] in ['crush', 'male_roommate', 'quarterback', 'friend']:
        print(f"G{m['greeting_idx']} | {m['location']} | key: '{m['key']}'")
        print(f"   Context: {repr(m['context'])}")
