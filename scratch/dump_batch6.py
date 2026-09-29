import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = {c.get('id'): c for c in data.get('world_characters', [])}

batch6_ids = [
    ('_HMwWXF9JtgqRyK3jTq4CB', 'Levi Graham'),
    ('_VXHtHNPy1cgxV2kKEJzJn', 'Lennox McKay'),
    ('_aGV3qat7DTa2k1LQ12Kq7', 'Kai Monroe'),
    ('_qgdVqj1EJbCJCLAmUCa32', 'Kai Mitchell'),
    ('_BAkbA3QcaqpcKVYNNBA3w', 'Kade Leavis'),
    ('_dxqAUrTJ7NF4DYEC2LNmF', 'Julian Bieri'),
    ('_UXn39zTRMxeqXdRtKJttJ', 'Jayce Collins'),
    ('_zMY7rT4xEEMxUXkcHQpyg', 'Ignis'),
    ('_wXfwPkxLAUKUUBkBe7yLL', 'Graham Purcell'),
    ('_H9bkDfxdQjCTb1QmDnFzt', 'Gianni Luciano')
]

for cid, name in batch6_ids:
    c = chars.get(cid)
    if not c:
        print(f"NOT FOUND: {name} ({cid})")
        continue
    safe_name = name.replace(' ', '_').replace('-', '_')
    with open(f"scratch/batch6_{safe_name}.txt", 'w', encoding='utf-8') as out:
        out.write(f"NAME: {c.get('display_name')} (ID: {cid})\n")
        out.write(f"FIRST_NAME: {c.get('first_name')}\n")
        out.write(f"KEYS: {c.get('keys')}\n")
        out.write(f"SUMMARY:\n{c.get('summary')}\n\n")
        out.write(f"LONG SUMMARY:\n{c.get('long_summary')}\n")

print("Dumped all 10 batch 6 characters into scratch/")
