import json

live = json.load(open('scratch/live_raw_location.json', encoding='utf-8'))['lexicon']
local = json.load(open('FINAL/Svartulfr_Location.json', encoding='utf-8'))['lexicon']

print(f"Live total: {len(live)}, Local total: {len(local)}")
match_count = 0
for i in range(min(len(live), len(local))):
    if live[i].get('name') == local[i].get('name'):
        match_count += 1
    else:
        print(f"Mismatch at {i}: live='{live[i].get('name')}' vs local='{local[i].get('name')}'")
        break
print(f"Matching names in sequence: {match_count}")
print(f"Entry 187: '{local[187].get('name')}'")
