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
        print(f"NOT FOUND: {cid}")
        continue
    print("=" * 60)
    print(f"NAME: {c.get('display_name')} (ID: {cid})")
    ls = c.get('long_summary', '')
    s = c.get('summary', '')
    print(f"LS Length: {len(ls)} | Summary Length: {len(s)}")
    text = ls if ls else s
    print("CONTENT PREVIEW:")
    print(text[:800])
    print("\n--- END PREVIEW ---")
