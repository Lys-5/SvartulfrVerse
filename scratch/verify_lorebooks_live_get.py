import json
import urllib.request

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'AuditorBot/1.0',
    'Accept': 'application/json'
}

# Verify Primary
req_prim = urllib.request.Request('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
with urllib.request.urlopen(req_prim, timeout=30) as resp:
    assert resp.status == 200
    prim_live = json.loads(resp.read().decode('utf-8'))

lex_prim = prim_live.get('lexicon', [])
print(f"Primary live entries count: {len(lex_prim)}")
assert len(lex_prim) == 99

check_ids = {
    '4NzXF4_0hYxmN7Idltzpw': ('Scarlett Rose', 4777),
    'ijy8vrlphNv19-p-gbYuY': ('Sierra Cruz', 5117),
    'YCxAqNoShpefVvk0_Pc7i': ("Russell 'Russ' Sinclair", 5505),
    'ekdQjq63xP7HtNuaPQJQE': ('Stanley Davies Jr.', 8008),
    'RM6rcwv8MlY1XWaCTQp0M': ('Jared Thompson', 8696),
    'alyssa_world_dossier_2b54a223': ('Alyssa Hvit Douglas Bloodmoon', 16957),
    'Vcj4h2TL4Usola2A4OOl6': ('Jasper Svartr Douglas Bloodmoon', 14483),
}

for eid, (expected_name, min_len) in check_ids.items():
    entry = next(e for e in lex_prim if e.get('entry_id') == eid)
    content_len = len(entry.get('content', ''))
    print(f"Verified {expected_name} ({eid}): type={entry.get('type')}, selective={entry.get('selective')}, "
          f"content_len={content_len}, ignored_chars={entry.get('ignored_characters')}, ignored_personas={entry.get('ignored_personas')}")
    assert entry.get('type') == 'npc'
    assert entry.get('selective') is False
    assert content_len >= min_len
    assert entry.get('avatar_activation_regex') is not None
    assert entry.get('npc_info') is not None

# Verify Secondary Edric
req_sec = urllib.request.Request('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', headers=headers)
with urllib.request.urlopen(req_sec, timeout=30) as resp:
    assert resp.status == 200
    sec_live = json.loads(resp.read().decode('utf-8'))

lex_sec = sec_live.get('lexicon', [])
edric_entry = next(e for e in lex_sec if e.get('entry_id') == 'h-ttmlgJYeRXqyDvQjSX7')
print(f"\nVerified Secondary Edric ({edric_entry.get('name')}): ignored_characters={edric_entry.get('ignored_characters')}")
assert edric_entry.get('ignored_characters') == ['_TbRM3EdxDjHFgqztTbCpL']

print("\n100% of live lorebook verifications passed!")
