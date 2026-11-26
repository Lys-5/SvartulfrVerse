import urllib.request
import urllib.error
import json
import sys

import os

REPO_ROOT = r'e:\repository\SvartulfrVerse'
token_path = os.path.join(REPO_ROOT, 'scratch', 'wyvern_token.txt')
with open(token_path, 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'ForensicAuditor/1.0',
    'Content-Type': 'application/json'
}

def get_endpoint(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
            return resp.status, json.loads(content)
    except urllib.error.HTTPError as e:
        content = e.read().decode('utf-8')
        try:
            return e.code, json.loads(content)
        except Exception:
            return e.code, content
    except Exception as e:
        return -1, str(e)

print('=== CHECK 1A: /characters/mine ===')
status, data = get_endpoint('https://app.wyvern.chat/api/characters/mine')
print('Status:', status)
if status == 200:
    chars = data.get('characters', [])
    print(f'Total characters count: {len(chars)}')
    for c in chars:
        print(f"  ID: {c.get('id')} | Name: {c.get('name')}")
else:
    print('Failed:', data)

print('\n=== CHECK 1B: Deleted Jared Thompson (_xJVPtBLL3dxy69RLKL9X9) ===')
status, data = get_endpoint('https://app.wyvern.chat/api/characters/_xJVPtBLL3dxy69RLKL9X9')
print('Status:', status)
print('Response:', data)

print('\n=== CHECK 1C: Alyssa Scenario (char_scenario_CKgwq246DyCj1NNTBV9rt) ===')
status, data = get_endpoint('https://app.wyvern.chat/api/character-scenarios/char_scenario_CKgwq246DyCj1NNTBV9rt')
print('Status:', status)
print('Data type:', type(data))
if status == 200:
    if isinstance(data, dict):
        print('Keys in data:', list(data.keys()))
        # Check if 'data' directly contains scenario fields or if nested
        sc = data if 'revision' in data or 'slots' in data else data.get('scenario')
        if isinstance(sc, dict):
            print(f"Scenario Name: {sc.get('name')}")
            print(f"Revision: {sc.get('revision')}")
            print(f"Lorebook IDs count: {len(sc.get('lorebook_ids', []))}")
            print(f"Slots count: {len(sc.get('slots', []))}")
            for s in sc.get('slots', []):
                print(f"  Slot '{s.get('key')}': unavail={s.get('unavailable_count')}, pool_len={len(s.get('pool', []))}")
            greetings = sc.get('greetings', [])
            print(f"Greetings count: {len(greetings)}")
            for i, g in enumerate(greetings):
                print(f"  Greeting {i}: title='{g.get('title')}', speaker_slot='{g.get('speaker_slot')}', msgs_len={len(g.get('messages', []))}")
        else:
            print('sc is not dict, it is:', type(sc), sc)



print('\n=== CHECK 1D: Jasper Scenario (char_scenario_Kq4mJEBH83j7Q7DdVfFnF) ===')
status, data = get_endpoint('https://app.wyvern.chat/api/character-scenarios/char_scenario_Kq4mJEBH83j7Q7DdVfFnF')
print('Status:', status)
print('Data type:', type(data))
if status == 200:
    if isinstance(data, dict):
        print('Keys in data:', list(data.keys()))
        sc = data if 'revision' in data or 'slots' in data else data.get('scenario')
        if isinstance(sc, dict):
            print(f"Scenario Name: {sc.get('name')}")
            print(f"Revision: {sc.get('revision')}")
            print(f"Lorebook IDs count: {len(sc.get('lorebook_ids', []))}")
            print(f"Slots count: {len(sc.get('slots', []))}")
            for s in sc.get('slots', []):
                print(f"  Slot '{s.get('key')}': unavail={s.get('unavailable_count')}, pool_len={len(s.get('pool', []))}")
            greetings = sc.get('greetings', [])
            print(f"Greetings count: {len(greetings)}")
            for i, g in enumerate(greetings):
                print(f"  Greeting {i}: title='{g.get('title')}', speaker_slot='{g.get('speaker_slot')}', msgs_len={len(g.get('messages', []))}")
        else:
            print('sc is not dict, it is:', type(sc), sc)
    else:
        print('Raw string preview:', str(data)[:200])

print('\n=== CHECK 1E: Lorebook Primary Live (_zwEqgEEzh12X6gHVmMKKC) ===')
status, data = get_endpoint('https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC')
print('Status:', status)
print('Data type:', type(data))
if status == 200:
    if isinstance(data, dict):
        print('Keys in data:', list(data.keys()))
        lb = data if 'entries' in data or 'lexicon' in data else data.get('lorebook', {})
        entries = lb.get('entries') or lb.get('lexicon') or []
        print(f"Entries count on live API: {len(entries)}")
        
        target_ids = {
            '4NzXF4_0hYxmN7Idltzpw': 'Scarlett Rose',
            'ijy8vrlphNv19-p-gbYuY': 'Sierra Cruz',
            'YCxAqNoShpefVvk0_Pc7i': 'Russell Sinclair',
            'ekdQjq63xP7HtNuaPQJQE': 'Stanley Davies Jr.',
            'RM6rcwv8MlY1XWaCTQp0M': 'Jared Thompson',
            'alyssa_world_dossier_2b54a223': 'Alyssa Douglas Bloodmoon',
            'Vcj4h2TL4Usola2A4OOl6': 'Jasper Douglas Bloodmoon'
        }
        
        found_targets = 0
        for e in entries:
            eid = e.get('id')
            if eid in target_ids:
                found_targets += 1
                name = target_ids[eid]
                desc = e.get('description', '')
                print(f"  Live Entry: {name} (ID: {eid})")
                print(f"    type: {e.get('type')}, selective: {e.get('selective')}")
                print(f"    description length: {len(desc)} characters")
                print(f"    ignored_characters: {e.get('ignored_characters')}")
                print(f"    ignored_personas: {e.get('ignored_personas')}")
                print(f"    keys: {e.get('keys')}")
                print(f"    custom_avatar_regex: {e.get('custom_avatar_regex')}")
                print(f"    avatar: {str(e.get('avatar'))[:50]}...")
        print(f"Total target entries matched on live API: {found_targets}/{len(target_ids)}")
    else:
        print('Raw string preview:', str(data)[:200])


