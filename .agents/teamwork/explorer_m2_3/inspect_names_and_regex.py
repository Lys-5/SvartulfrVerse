import json
from pathlib import Path
import re
import sys

sys.path.append(r'e:\repository\SvartulfrVerse')
from scripts.verify_npc_schema_contract import detect_duplicate_surnames, CANONICAL_BROAD_KEYS, validate_npc_info_schema

def inspect():
    for fn in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
        p = Path(r'e:\repository\SvartulfrVerse') / fn
        data = json.loads(p.read_text(encoding='utf-8'))
        print(f"\n==================== {fn} ====================")
        print(f"Total entries: {len(data['lexicon'])}")
        
        dupe_count = 0
        umbrella_count = 0
        npc_info_count = 0
        
        for idx, e in enumerate(data['lexicon']):
            name = e.get('name', '')
            content = e.get('content', '')
            reg = e.get('avatar_activation_regex', '')
            npc_info = e.get('npc_info')
            
            # Check dupes
            dupes = detect_duplicate_surnames(reg)
            if dupes:
                dupe_count += 1
                print(f"[DUPE REGEX] #{idx} '{name}': {dupes} in regex: {reg[:70]}")
            
            # Check broad keys
            keys = e.get('keys', [])
            broad_found = [k for k in keys if k.strip().lower() in CANONICAL_BROAD_KEYS]
            if broad_found:
                umbrella_count += 1
                print(f"[BROAD KEY] #{idx} '{name}': {broad_found}")
                
            # Check npc_info
            if npc_info:
                npc_info_count += 1
                
        print(f"Summary for {fn}: {dupe_count} regex dupes, {umbrella_count} broad keys, {npc_info_count} existing npc_info")

if __name__ == '__main__':
    inspect()
