import json
from pathlib import Path
import sys

sys.path.append(r'e:\repository\SvartulfrVerse')
from scripts.verify_npc_schema_contract import detect_duplicate_surnames, compile_wyvern_avatar_regex

def dump_all_dupes():
    for fn in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
        p = Path(r'e:\repository\SvartulfrVerse') / fn
        data = json.loads(p.read_text(encoding='utf-8'))
        print(f"\n==================== Dupes in {fn} ====================")
        
        for idx, e in enumerate(data['lexicon']):
            reg = e.get('avatar_activation_regex', '')
            dupes = detect_duplicate_surnames(reg)
            if dupes:
                print(f"\nEntry #{idx}: {e.get('name')}")
                print(f"  ID: {e.get('entry_id')}")
                print(f"  Current Regex: {reg}")
                print(f"  Current NPC Info: {e.get('npc_info')}")
                print(f"  Detected dupes: {dupes}")

if __name__ == '__main__':
    dump_all_dupes()
