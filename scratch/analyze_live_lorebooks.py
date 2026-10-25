import json
import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'User-Agent': 'AuditorBot/1.0'}

for name, lid in [('Primary', '_zwEqgEEzh12X6gHVmMKKC'), ('Secondary', '_Uht3Ckz44JBDrPnUHq7LV')]:
    r = requests.get(f'https://app.wyvern.chat/api/lorebooks/{lid}', headers=headers)
    data = r.json()
    print(f"\n==================== LIVE {name} ({lid}) ====================")
    print("Top-level keys:", sorted(list(data.keys())))
    print("gallery type:", type(data.get('gallery')), "len:", len(data.get('gallery', [])) if isinstance(data.get('gallery'), list) else data.get('gallery'))
    if data.get('gallery'):
        print("Gallery items count:", len(data['gallery']))
        for i, g in enumerate(data['gallery'][:5]):
            print(f"  Gallery item [{i}]:", json.dumps(g))
    
    lex = data.get('lexicon', [])
    print("Lexicon entries count:", len(lex))
    all_keys = set()
    for e in lex:
        all_keys.update(e.keys())
    print("All entry keys present across lexicon:", sorted(list(all_keys)))
    
    # Check entries with npc_info
    npc_info_entries = [e for e in lex if 'npc_info' in e and e['npc_info']]
    print("Entries with npc_info:", len(npc_info_entries))
    if npc_info_entries:
        for e in npc_info_entries[:5]:
            print(f"  Entry '{e.get('name')}': npc_info =", json.dumps(e.get('npc_info')))
            
    # Check entries with ignored_characters / ignored_personas
    ign_char_entries = [e for e in lex if e.get('ignored_characters')]
    ign_pers_entries = [e for e in lex if e.get('ignored_personas')]
    print("Entries with ignored_characters:", len(ign_char_entries))
    for e in ign_char_entries[:5]:
        print(f"  Entry '{e.get('name')}': ignored_characters =", e.get('ignored_characters'))
    print("Entries with ignored_personas:", len(ign_pers_entries))
    for e in ign_pers_entries[:5]:
        print(f"  Entry '{e.get('name')}': ignored_personas =", e.get('ignored_personas'))

    # Check avatar fields
    avatars = [e.get('avatar') for e in lex if e.get('avatar')]
    print("Entries with avatar:", len(avatars), "Unique avatars:", len(set(avatars)))
    sample_avatars = list(set(avatars))[:5]
    for sa in sample_avatars:
        print("  Sample avatar URL:", sa)
        
    # Check regex fields
    reg_entries = [e for e in lex if e.get('avatar_activation_regex')]
    print("Entries with avatar_activation_regex:", len(reg_entries))
    if reg_entries:
        print("  Sample regex:", reg_entries[0].get('avatar_activation_regex'))
