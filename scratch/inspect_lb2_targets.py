import json

with open('FINAL/Svartulfr_Lorebook_II.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Total entries in LB2: {len(d.get('entries', []))}")

srf_void_entries = [
    e for e in d.get('entries', [])
    if any(k in e.get('name', '').lower() or k in str(e.get('keys', '')).lower() for k in ['srf', 'supernatural reserve', 'voidspace', 'ddm', 'dungeon', 'contratt'])
]

print(f"Matched {len(srf_void_entries)} entries in LB2:")
for e in srf_void_entries[:10]:
    print(f"- {e.get('name')} (keys: {e.get('keys')})")
