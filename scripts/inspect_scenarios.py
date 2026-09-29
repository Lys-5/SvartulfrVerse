import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

scens = d.get('world_scenarios', [])
print(f"Total scenarios: {len(scens)}")
for i, s in enumerate(scens):
    sid = s.get('id')
    title = s.get('title') or s.get('name')
    loc = s.get('location_id')
    tagline = s.get('tagline')
    desc = s.get('description') or ''
    print(f"\n--- Scenario {i+1} [{sid}] ---")
    print(f"Current Title: {title}")
    print(f"Tagline: {tagline}")
    print(f"Location ID: {loc}")
    print(f"Description: {desc[:200]}...")
