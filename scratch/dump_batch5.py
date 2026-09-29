import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = {c.get('id'): c for c in data.get('world_characters', [])}

batch5_ids = [
    ('_Hat1j7nNjUG11VmU7f76R', 'Rifle Maddox'),
    ('_EFQqYW4crGnCXBEHXmBeY', 'Rhett Moore'),
    ('_NhewaHtr8dMb7F6nXW6bV', 'Rafael Callaway'),
    ('_XGhNaj7aPmnEa9HbbDm1k', 'Persephone'),
    ('_7MnMHDCeKtNwwaUKLXhkm', 'Park Jae-Sung'),
    ('_mqQXacnFftjXafhTtDDeh', 'Nickolas Wolffe'),
    ('_HprRJXTV1CaCWtXktW1pR', 'Nic Lucero'),
    ('_Y3HUfA4Y2QwpAHNncDx3a', 'Neon Purr'),
    ('_8tmte32HpV239AcrUFcRD', 'Milo Grayson'),
    ('_zccx36g3CpyD6j1a8fdwn', 'Miles Airhardt')
]

for cid, name in batch5_ids:
    c = chars.get(cid)
    if not c:
        print(f"NOT FOUND: {name} ({cid})")
        continue
    safe_name = name.replace(' ', '_').replace('-', '_')
    with open(f"scratch/batch5_{safe_name}.txt", 'w', encoding='utf-8') as out:
        out.write(f"NAME: {c.get('display_name')} (ID: {cid})\n")
        out.write(f"FIRST_NAME: {c.get('first_name')}\n")
        out.write(f"KEYS: {c.get('keys')}\n")
        out.write(f"SUMMARY:\n{c.get('summary')}\n\n")
        out.write(f"LONG SUMMARY:\n{c.get('long_summary')}\n")

print("Dumped all 10 batch 5 characters into scratch/")
