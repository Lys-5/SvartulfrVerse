import json
import sys
sys.path.insert(0, ".")
from scripts.verify_npc_schema_contract import CANONICAL_BROAD_KEYS

records = json.load(open('scratch/detailed_records.json', encoding='utf-8'))

for r in records:
    idx = r['index']
    name = r['entry_name']
    nicks = r['existing_npc_info'].get('nicknames', []) if r['existing_npc_info'] else []
    keys = r['keys']
    
    # Check if any individual word in nicknames matches broad keys
    for n in nicks:
        words = [w.strip().lower() for w in n.split()]
        if any(w in CANONICAL_BROAD_KEYS for w in words):
            # check if the nickname is exactly a broad key or multi-word
            if n.strip().lower() in CANONICAL_BROAD_KEYS:
                print(f"EXACT BROAD NICKNAME: [{idx}] {name} -> '{n}'")
            else:
                pass # compound like 'Pack Leader'
    for k in keys:
        if k.strip().lower() in CANONICAL_BROAD_KEYS:
            print(f"EXACT BROAD KEY: [{idx}] {name} -> '{k}'")
