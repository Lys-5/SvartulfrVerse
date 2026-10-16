import json
import urllib.request
import time

def main():
    # 1. Update Svartulfr_NPC_Primary.json
    with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
        prim = json.load(f)

    sierra_content = '''[NAME: Sierra Cruz; SPECIES: Lamia (Naga / Serpentine Demihuman); AGE: 18 (Born September 8, 2005); OCCUPATION: SUCC Undergrad, Applied Necromancy Major; RESIDENCE: Wyrm Hall Dorm Suite, SUCC Campus]

PUBLIC DOSSIER: An adorable, expressive Lamia (Naga) student at SUCC with an expressive human upper torso and a massive four-meter iridescent rainbow-emerald serpentine tail. Roommate of Alyssa Douglas-Bloodmoon and Scarlett Rose. Sierra is sweet, grounded, and slightly bashful about her enormous coils, studying Applied Necromancy while balancing dorm life with Scarlett's glamorous parties and Alyssa's sunny escapades.

EXTERNAL HOOKS: Friendly, protective, and unique on campus. Her immense serpentine coils make her impossible to miss, yet her gentle demeanor and shy smile make her instantly approachable.'''

    for key in ['entries', 'lexicon']:
        for e in prim.get(key, []):
            if e.get('name') in ['Sierra', 'Sierra Cruz']:
                e['name'] = 'Sierra Cruz'
                e['content'] = sierra_content
                e['keys'] = ['Sierra Cruz', 'Sierra']
                e['type'] = 'lore/concept'
                for field in ['avatar_activation_regex', 'lines_parsed', 'custom_avatar_regex', 'npc_info']:
                    e.pop(field, None)
            elif e.get('name') == 'Dominic Rogers':
                c = e['content']
                c = c.replace('AGE: 20;', 'AGE: 50 (Born November 3, 1974);')
                e['content'] = c
                e['keys'] = ['Dominic Rogers', 'Dom Rogers', 'Mr. Rogers', 'Mr Rogers', "Bailey's Dad"]

    with open('FINAL/Svartulfr_NPC_Primary.json', 'w', encoding='utf-8') as f:
        json.dump(prim, f, indent=2, ensure_ascii=False)
    with open('lorebooks/optimized/Svartulfr_NPC_Primary.json', 'w', encoding='utf-8') as f:
        json.dump(prim, f, indent=2, ensure_ascii=False)
    print('Primary Lorebook updated with corrected Sierra and Dominic Rogers!')

    # 2. Deploy to Wyvern API
    token = open('scratch/wyvern_token.txt').read().strip()
    base_payload = {
        'name': prim.get('name', 'Svartúlfr - NPC Primary'),
        'description': prim.get('description', ''),
        'visibility': prim.get('visibility', 'private'),
        'rating': prim.get('rating', 'explicit'),
        'scan_depth': prim.get('scan_depth', 5),
        'token_budget': prim.get('token_budget', 5000),
        'recursive_scanning': prim.get('recursive_scanning', True),
        'lexicon': prim.get('lexicon', [])
    }

    payload_bytes = json.dumps(base_payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }

    req = urllib.request.Request(
        'https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC',
        data=payload_bytes,
        headers=headers,
        method='PUT'
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            print('PUT Svartulfr - NPC Primary status:', resp.status)
    except urllib.error.HTTPError as e:
        print('PUT error:', e.code, e.read().decode('utf-8'))

if __name__ == '__main__':
    main()
