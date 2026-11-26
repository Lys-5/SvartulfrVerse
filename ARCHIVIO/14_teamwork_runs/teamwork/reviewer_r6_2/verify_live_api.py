import urllib.request
import urllib.error
import json

token = open('scratch/wyvern_token.txt', 'r', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'ReviewerBot/1.0'
}

def get_url(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            return resp.status, json.loads(data)
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8')
    except Exception as e:
        return 0, str(e)

print("=== CHECKING LOREBOOK PRIMARY (_zwEqgEEzh12X6gHVmMKKC) ===")
status_p, data_p = get_url('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC')
print(f"Status: {status_p}")
if status_p == 200:
    entries = data_p.get('entries', [])
    lexicon = data_p.get('lexicon', [])
    print(f"Entries count: {len(entries)}")
    print(f"Lexicon count: {len(lexicon)}")
    # Find target entries
    target_ids = {
        'Scarlett': '4NzXF4_0hYxmN7Idltzpw',
        'Sierra': 'ijy8vrlphNv19-p-gbYuY',
        'Russ': 'YCxAqNoShpefVvk0_Pc7i',
        'Stan': 'ekdQjq63xP7HtNuaPQJQE',
        'Jared': 'RM6rcwv8MlY1XWaCTQp0M',
        'Alyssa': 'alyssa_world_dossier_2b54a223',
        'Jasper': 'Vcj4h2TL4Usola2A4OOl6'
    }
    entries_map = {e.get('entry_id'): e for e in entries}
    for name, eid in target_ids.items():
        e = entries_map.get(eid)
        if e:
            print(f"  {name} ({eid}): type={e.get('type')}, desc_len={len(e.get('content', ''))}, ignored_chars={e.get('ignored_characters')}, ignored_personas={e.get('ignored_personas')}")
        else:
            print(f"  {name} ({eid}): NOT FOUND")

print("\n=== CHECKING LOREBOOK SECONDARY (_Uht3Ckz44JBDrPnUHq7LV) ===")
status_s, data_s = get_url('https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV')
print(f"Status: {status_s}")
if status_s == 200:
    entries_s = data_s.get('entries', [])
    lexicon_s = data_s.get('lexicon', [])
    print(f"Entries count: {len(entries_s)}")
    print(f"Lexicon count: {len(lexicon_s)}")
    # Find Edric
    edric = next((e for e in entries_s if e.get('entry_id') == 'h-ttmlgJYeRXqyDvQjSX7'), None)
    if edric:
        print(f"  Edric: type={edric.get('type')}, ignored_chars={edric.get('ignored_characters')}")
    else:
        print("  Edric: NOT FOUND")

print("\n=== CHECKING /characters/mine ===")
status_mine, data_mine = get_url('https://app.wyvern.chat/api/characters/mine')
print(f"Status: {status_mine}")
if status_mine == 200:
    chars = data_mine.get('characters', [])
    print(f"Mine characters count: {len(chars)}")
    for c in chars:
        print(f"  - {c.get('id')} | {c.get('name')}")

print("\n=== CHECKING DELETED JARED (_xJVPtBLL3dxy69RLKL9X9) ===")
status_jared, data_jared = get_url('https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9')
print(f"Status: {status_jared} (expected 404)")

print("\n=== CHECKING 2 SUCC SCENARIOS ===")
status_alyssa, data_alyssa = get_url('https://app.wyvern.chat/api/character-scenarios/char_scenario_CKgwq246DyCj1NNTBV9rt')
print(f"Alyssa Scenario Status: {status_alyssa}, rev={data_alyssa.get('revision') if status_alyssa==200 else 'N/A'}")
status_jasper, data_jasper = get_url('https://app.wyvern.chat/api/character-scenarios/char_scenario_Kq4mJEBH83j7Q7DdVfFnF')
print(f"Jasper Scenario Status: {status_jasper}, rev={data_jasper.get('revision') if status_jasper==200 else 'N/A'}")
