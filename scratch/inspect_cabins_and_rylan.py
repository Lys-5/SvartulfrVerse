import json

with open('FINAL/Svartulfr_Location.json', 'r', encoding='utf-8') as f:
    loc_data = json.load(f)

for idx, e in enumerate(loc_data.get('entries', [])):
    t = e.get('comment') or e.get('title') or ''
    if any(k in t for k in ['G-01', 'B-01', 'B-07']):
        print(f"=== IDX {idx}: ID={e.get('id')} COMMENT={e.get('comment')} ===")
        print("KEYS:", e.get('keys'))
        print("SEC KEYS:", e.get('secondary_keys'))
        print("CONTENT PREVIEW:", e.get('content', '')[:300])
        print("---")

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    npc_data = json.load(f)

for idx, e in enumerate(npc_data.get('entries', [])):
    t = e.get('comment') or e.get('title') or ''
    if 'Rylan' in t or 'Cade' in t:
        print(f"=== NPC IDX {idx}: ID={e.get('id')} COMMENT={e.get('comment')} ===")
        print("KEYS:", e.get('keys'))
        print("CONTENT:", e.get('content'))
        print("---")
