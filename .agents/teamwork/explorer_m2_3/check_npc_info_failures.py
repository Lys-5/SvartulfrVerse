import json
from pathlib import Path
import sys

sys.path.append(r'e:\repository\SvartulfrVerse')
from scripts.verify_npc_schema_contract import validate_npc_info_schema

def check_why_invalid():
    for fn in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
        p = Path(r'e:\repository\SvartulfrVerse') / fn
        data = json.loads(p.read_text(encoding='utf-8'))
        print(f"\nChecking why npc_info failed in {fn}:")
        
        err_samples = {}
        for idx, e in enumerate(data['lexicon']):
            npc_info = e.get('npc_info')
            ok, errs = validate_npc_info_schema(npc_info)
            if not ok:
                for err in errs:
                    err_samples[err] = err_samples.get(err, 0) + 1
                    
        print("Error frequencies:")
        for err, count in err_samples.items():
            print(f"  [{count}x] {err}")
            
        # Print a sample entry's npc_info
        print("\nSample npc_info from entry #0:")
        print(json.dumps(data['lexicon'][0].get('npc_info'), indent=2))

if __name__ == '__main__':
    check_why_invalid()
