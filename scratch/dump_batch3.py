import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = {c.get('id'): c for c in data.get('world_characters', [])}

batch3_ids = [
    '_t8mPAn3cBqn4EqYprFjKT', # Ashton Crowley
    '_LwReg93k28wBNxKQKRtpX', # Amerian de Vian
    '_qxHwY974NUP39pmh8ghFt', # Aeril Royen
    '_9gG1cFVyPHmL86FbpwYbj', # Caien Vaelion
    '_a9BmgN8NJB3b1kAYz3t2j', # Lestat Oreven
    '_j4eNzGKnK1tkJHz7r1CXP', # Xaiden Nershatar
    '_NHhBhxqm9B1y2GyU2DLTW', # Zaire Ziisis
    '_emHyPKTD1gL2NqPEFXVAt', # Wren Lark
    '_RTVEcAQpeX94kV8QFtGGg', # Angui
    '_YpKdVLTX16pLrUDb6a1ra'  # Madge
]

for cid in batch3_ids:
    c = chars.get(cid)
    if not c:
        continue
    with open(f"scratch/batch3_{c.get('first_name') or c.get('display_name')}.txt", 'w', encoding='utf-8') as out:
        out.write(f"NAME: {c.get('display_name')} (ID: {cid})\n")
        out.write(f"KEYS: {c.get('first_name')}\n")
        out.write(f"SUMMARY:\n{c.get('summary')}\n\n")
        out.write(f"LONG SUMMARY:\n{c.get('long_summary')}\n")

print("Dumped all 10 batch 3 files into scratch/")
