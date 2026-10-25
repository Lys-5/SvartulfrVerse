import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

for filename in ['Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json']:
    filepath = ROOT / 'FINAL' / filename
    print(f"\n==================== LOCAL {filename} ====================")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("Top-level keys:", sorted(list(data.keys())))
    print("gallery present:", 'gallery' in data)
    if 'gallery' in data:
        print("gallery type:", type(data['gallery']), "len:", len(data['gallery']))
        if len(data['gallery']) > 0:
            print("Sample gallery item:", json.dumps(data['gallery'][0], indent=2))
    print("gallery_count:", data.get('gallery_count'))
    
    entries = data.get('entries', [])
    lexicon = data.get('lexicon', [])
    print(f"entries count: {len(entries)}, lexicon count: {len(lexicon)}")
    print(f"Parity check byte-for-byte: {json.dumps(entries) == json.dumps(lexicon)}")
    
    # Analyze entries
    all_keys = set()
    for e in entries:
        all_keys.update(e.keys())
    print("All entry keys present:", sorted(list(all_keys)))
    
    npc_info_count = sum(1 for e in entries if 'npc_info' in e and e['npc_info'])
    print(f"Entries with npc_info: {npc_info_count}/{len(entries)}")
    if npc_info_count > 0:
        sample = next(e for e in entries if 'npc_info' in e and e['npc_info'])
        print(f"Sample entry '{sample.get('name')}' npc_info keys:", sorted(list(sample['npc_info'].keys())))
        print("Sample npc_info content:", json.dumps(sample['npc_info'], indent=2))
        
    ign_char_count = sum(1 for e in entries if e.get('ignored_characters'))
    print(f"Entries with ignored_characters: {ign_char_count}")
    for e in entries:
        if e.get('ignored_characters'):
            print(f"  {e.get('name')}: ignored_characters = {e.get('ignored_characters')}")
            
    ign_pers_count = sum(1 for e in entries if e.get('ignored_personas'))
    print(f"Entries with ignored_personas: {ign_pers_count}")
    for e in entries:
        if e.get('ignored_personas'):
            print(f"  {e.get('name')}: ignored_personas = {e.get('ignored_personas')}")
            
    avatar_count = sum(1 for e in entries if e.get('avatar'))
    print(f"Entries with avatar: {avatar_count}/{len(entries)}")
