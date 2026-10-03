import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
chars = {c['id']: c for c in d['world_characters']}

print("--- Malachia ---")
for cid in ['_gYagUj1CAE7grnRCVLnyU', '_rAcN9GXD1Le4WxY28e49W']:
    c = chars[cid]
    print(cid, c['display_name'], "keys:", c.get('keys'), "summary len:", len(c.get('summary') or ''))

print("\n--- Logan ---")
for cid in ['_gCzaABFtVKTVCwcHmNGW6', '_JL37wK9PQMNDChULCDrWj']:
    c = chars[cid]
    print(cid, c['display_name'], "keys:", c.get('keys'), "summary len:", len(c.get('summary') or ''))

print("\n--- Dominic ---")
for cid in ['_dDXdeJrcYHbwagGFQVKQR', '_6h1dDQpmqTAckYaWRT2er', '_8wjMyUNV6yB7ACLk4dhWd']:
    c = chars[cid]
    print(cid, c['display_name'], "keys:", c.get('keys'), "display_desc:", c.get('display_description'))

print("\n--- Stanley & Stan ---")
for cid in ['_gqFXEaVj4aG9a8QL8R7f1', '_C18UjnQzGMLcQaNW3UaKq']:
    c = chars[cid]
    print(cid, c['display_name'], "nicknames:", c.get('nicknames'), "keys:", c.get('keys'))

print("\n--- Dullahan & Mithers ---")
for cid in ['_F8ee4UpyLr7Fyr69KKhzV', '_71Bc3wDdCkKmXD8EmLgFe']:
    c = chars[cid]
    print(cid, c['display_name'], "keys:", c.get('keys'), "display_desc:", c.get('display_description'))

print("\n--- Finnegan ---")
for cid, c in chars.items():
    if 'finn' in c['display_name'].lower() or 'finn' in (c.get('first_name') or '').lower():
        print(cid, c['display_name'], "keys:", c.get('keys'))
