import json
from pathlib import Path
import sys

sys.path.append(r'e:\repository\SvartulfrVerse')
from scripts.verify_npc_schema_contract import CANONICAL_BROAD_KEYS

def check_umbrella():
    for fn in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
        p = Path(r'e:\repository\SvartulfrVerse') / fn
        data = json.loads(p.read_text(encoding='utf-8'))
        print(f"\n==================== Checking Umbrella in {fn} ====================")
        
        found_in_keys = []
        found_in_sec = []
        found_in_nick = []
        found_in_info_nick = []
        
        for idx, e in enumerate(data['lexicon']):
            name = e.get('name', f'Entry {idx}')
            
            # keys
            for k in e.get('keys', []):
                if k.strip().lower() in CANONICAL_BROAD_KEYS:
                    found_in_keys.append((idx, name, k))
            # secondary_keys
            for k in e.get('secondary_keys', []):
                if k.strip().lower() in CANONICAL_BROAD_KEYS:
                    found_in_sec.append((idx, name, k))
            # nicknames
            for n in e.get('nicknames', []):
                if n.strip().lower() in CANONICAL_BROAD_KEYS:
                    found_in_nick.append((idx, name, n))
            # npc_info.nicknames
            info_nicks = e.get('npc_info', {}).get('nicknames', [])
            for n in info_nicks:
                if n.strip().lower() in CANONICAL_BROAD_KEYS:
                    found_in_info_nick.append((idx, name, n))
                    
        print(f"Found in keys: {len(found_in_keys)}")
        for x in found_in_keys: print(f"  keys: #{x[0]} {x[1]} -> '{x[2]}'")
        print(f"Found in secondary_keys: {len(found_in_sec)}")
        for x in found_in_sec: print(f"  secondary_keys: #{x[0]} {x[1]} -> '{x[2]}'")
        print(f"Found in nicknames: {len(found_in_nick)}")
        for x in found_in_nick: print(f"  nicknames: #{x[0]} {x[1]} -> '{x[2]}'")
        print(f"Found in npc_info.nicknames: {len(found_in_info_nick)}")
        for x in found_in_info_nick: print(f"  info.nicknames: #{x[0]} {x[1]} -> '{x[2]}'")

if __name__ == '__main__':
    check_umbrella()
