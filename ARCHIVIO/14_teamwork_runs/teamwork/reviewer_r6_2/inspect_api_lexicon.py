import urllib.request
import json

token = open('scratch/wyvern_token.txt', 'r', encoding='utf-8').read().strip()
h = {'Authorization': f'Bearer {token}', 'User-Agent': 'ReviewerBot/1.0'}
req = urllib.request.Request('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=h)
d = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

print('Keys returned by API:', list(d.keys()))
print('Entries in API:', len(d.get('entries', [])))
print('Lexicon in API:', len(d.get('lexicon', [])))

if d.get('lexicon'):
    lex = d['lexicon']
    print('First item in lexicon keys:', list(lex[0].keys()))
    print('Names in lexicon:', [e.get('name') for e in lex[:10]])
    target_ids = {
        'Scarlett Rose': '4NzXF4_0hYxmN7Idltzpw',
        'Sierra Cruz': 'ijy8vrlphNv19-p-gbYuY',
        'Russell Russ Sinclair': 'YCxAqNoShpefVvk0_Pc7i',
        'Stanley Davies Jr': 'ekdQjq63xP7HtNuaPQJQE',
        'Jared Thompson': 'RM6rcwv8MlY1XWaCTQp0M',
        'Alyssa Hvit Douglas Bloodmoon': 'alyssa_world_dossier_2b54a223',
        'Jasper Svartr Douglas Bloodmoon': 'Vcj4h2TL4Usola2A4OOl6'
    }
    lex_map = {e.get('entry_id'): e for e in lex}
    for name, tid in target_ids.items():
        found = lex_map.get(tid)
        if found:
            print(f"Found in API lexicon: {name} ({tid}) -> {found.get('name')}, type={found.get('type')}, desc_len={len(found.get('content', ''))}, ignored_chars={found.get('ignored_characters')}, ignored_personas={found.get('ignored_personas')}")
        else:
            print(f"NOT found in API lexicon: {name} ({tid})")

print("\n--- SECONDARY LOREBOOK ---")
req_s = urllib.request.Request('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=h)
d_s = json.loads(urllib.request.urlopen(req_s).read().decode('utf-8'))
print('Secondary Keys returned by API:', list(d_s.keys()))
print('Secondary Entries in API:', len(d_s.get('entries', [])))
print('Secondary Lexicon in API:', len(d_s.get('lexicon', [])))
if d_s.get('lexicon'):
    lex_s = d_s['lexicon']
    edric = next((e for e in lex_s if e.get('entry_id') == 'h-ttmlgJYeRXqyDvQjSX7'), None)
    if edric:
        print(f"Edric found in API lexicon: name={edric.get('name')}, type={edric.get('type')}, ignored_chars={edric.get('ignored_characters')}")
    else:
        print("Edric NOT found in API lexicon")
