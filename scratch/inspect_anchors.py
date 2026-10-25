import json

with open('scratch/backup_consolidated_snapshot/world_locations.json', encoding='utf-8') as f:
    locs = json.load(f)

targets = {
    '_EwMMJ7KEg9ATJ3mTXBaha': 'Seven Hills',
    '_j67Dp2PVwFCpdrfWRYV2M': 'SUCC',
    '_761mFFeCcQyR9JxhLCWcy': 'Solarton',
    '_D8B9QAfHPn3NfD4mAnJen': 'Blackwood City',
    '_4k3RT1nxw994yHRM66LQb': 'Simi Valley'
}

for l in locs:
    lid = l.get('id') or l.get('_id')
    if lid in targets:
        print(f"=== {targets[lid]} ({lid}) ===")
        print("Name:", l.get('name'))
        print("Description:\n", l.get('description'))
        print("Context Description:\n", l.get('context_description'))
        print("Keys:", l.get('keys'))
        print("-" * 50)
