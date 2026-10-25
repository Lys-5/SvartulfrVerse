import json

with open('scratch/campmystic_full_card.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== CAMP MYSTIC NARRATOR CARD ===")
print("ID:", data.get('id'))
print("NAME:", data.get('name').encode('ascii', errors='replace').decode('ascii'))
print("TAGLINE:", data.get('tagline'))
print("\nFIRST_MES (length", len(data.get('first_mes') or ''), "):")
print((data.get('first_mes') or '')[:500].encode('ascii', errors='replace').decode('ascii'))
print("\nSCENARIO (length", len(data.get('scenario') or ''), "):")
print((data.get('scenario') or '')[:1000].encode('ascii', errors='replace').decode('ascii'))
print("\nDESCRIPTION (length", len(data.get('description') or ''), "):")
print((data.get('description') or '')[:1000].encode('ascii', errors='replace').decode('ascii'))
