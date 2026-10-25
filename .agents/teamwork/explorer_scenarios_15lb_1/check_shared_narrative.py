import json

fpath = 'FINAL/Svartulfr_Master_Scenario.json'
with open(fpath, 'r', encoding='utf-8') as f:
    data = json.load(f)

greetings = data.get('greetings', [])

shared_indices = [0, 1, 4, 5, 10, 11, 13, 14, 15, 19, 22, 23, 24, 25, 26, 27]

print(f"Checking {len(shared_indices)} shared greetings:")
for idx in shared_indices:
    g = greetings[idx]
    gid = g.get('id')
    name = g.get('name')
    content = g.get('content', '')
    print(f"\n[{idx}] {gid} | {name}")
    print(f"Content snippet: {content[:150]}...")
