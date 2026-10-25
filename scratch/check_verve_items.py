import json

with open('scratch/world_new_deployed.json', 'r', encoding='utf-8') as f:
    snap = json.load(f)

lex = snap.get('world_lexicon', [])
target_ids = ['_YxGJRFDkjdVyeH1mJNM1T', '_UVX1RAqE8CWz8ywYkT4Fm', '_BRjbkk8JM3Jw1xyJGgzDH']
lex_map = {e.get('id') or e.get('_id'): e for e in lex}

print("Checking Verve 3 item IDs in snapshot world_lexicon:")
for tid in target_ids:
    if tid in lex_map:
        e = lex_map[tid]
        print(f"FOUND {tid}: Name: {e.get('name')} | Type: {e.get('type')} | Content: {e.get('content')}")
    else:
        print(f"NOT FOUND BY ID in snapshot: {tid}")

names = ['Wireless Earbuds', 'Lighter', 'Keys']
for e in lex:
    if e.get('name') in names:
        print(f"By name '{e.get('name')}': ID={e.get('id') or e.get('_id')}")
