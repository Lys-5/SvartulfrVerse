import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = {c.get('id'): c for c in data.get('world_characters', [])}

batch4_ids = [
    ('_egd2NVErGy86WFbyzRJfK', 'Bartholomew'),
    ('_kP1gWeyLw9jKbz3Xf73GH', 'Marek'),
    ('_nH4tNHagQ1Cthad7gYRWU', 'Warg'),
    ('_Ch7VqzHF7fDeDMyh4xreP', 'Vero Walker'),
    ('_d1rcReg8z8wKTUmyy9na8', 'Venera Dolce'),
    ('_8C743QJxh9WU1JhnCUXzL', 'Vale Roberts'),
    ('_cq3JLw8gydDJm8zC2C3B2', 'Talia Grimwood'),
    ('_3FKFrWjmMVBFGmwHEAYDq', 'Siebren Dijkstra'),
    ('_NdmDLH9q9QCK7qHnjXKME', 'Rue'),
    ('_K3Czda6EXGW1GG8aezh3M', 'Romeo Dean')
]

for cid, name in batch4_ids:
    c = chars.get(cid)
    if not c:
        print(f"NOT FOUND: {name} ({cid})")
        continue
    with open(f"scratch/batch4_{name}.txt", 'w', encoding='utf-8') as out:
        out.write(f"NAME: {c.get('display_name')} (ID: {cid})\n")
        out.write(f"FIRST_NAME: {c.get('first_name')}\n")
        out.write(f"KEYS: {c.get('keys')}\n")
        out.write(f"SUMMARY:\n{c.get('summary')}\n\n")
        out.write(f"LONG SUMMARY:\n{c.get('long_summary')}\n")

print("Dumped all 10 batch 4 characters into scratch/")
