import json
from pathlib import Path

def inspect_clean_regex():
    for fn in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
        p = Path(r'e:\repository\SvartulfrVerse') / fn
        data = json.loads(p.read_text(encoding='utf-8'))
        print(f"\n==================== Clean regex samples in {fn} ====================")
        
        # Look at entry 1, 2, 3
        for idx in [1, 2, 3, 5, 20]:
            if idx < len(data['lexicon']):
                e = data['lexicon'][idx]
                print(f"Entry #{idx}: {e.get('name')}")
                print(f"  Regex: {e.get('avatar_activation_regex')}")
                print(f"  NPC Info: {e.get('npc_info')}")

if __name__ == '__main__':
    inspect_clean_regex()
