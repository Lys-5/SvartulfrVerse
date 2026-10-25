import json
from pathlib import Path

final_dir = Path('FINAL')
lorebooks = [
    'Svartulfr_Location.json',
    'Svartulfr_Lorebook_I.json',
    'Svartulfr_Lorebook_II.json',
    'Svartulfr_Lorebook_III.json',
    'Svartulfr_NPC_Primary.json',
    'Svartulfr_NPC_Secondary.json',
]

print("="*80)
print("CHECKING ENTRIES == LEXICON PARITY ON ALL 6 LOREBOOKS")
print("="*80)

for lb_name in lorebooks:
    p = final_dir / lb_name
    data = json.load(open(p, encoding='utf-8'))
    entries = data.get('entries')
    lexicon = data.get('lexicon')
    
    if entries is None or lexicon is None:
        print(f"[FAIL] {lb_name}: Missing entries or lexicon (entries: {entries is not None}, lexicon: {lexicon is not None})")
        continue
        
    if len(entries) != len(lexicon):
        print(f"[FAIL] {lb_name}: Length mismatch (entries: {len(entries)}, lexicon: {len(lexicon)})")
        continue
        
    s_entries = json.dumps(entries, sort_keys=True)
    s_lexicon = json.dumps(lexicon, sort_keys=True)
    
    if s_entries == s_lexicon:
        print(f"[OK] {lb_name}: entries == lexicon 100% identical ({len(entries)} items)")
    else:
        print(f"[FAIL] {lb_name}: Content mismatch between entries and lexicon!")
