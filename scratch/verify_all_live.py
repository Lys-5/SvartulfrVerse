import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {TOKEN}', 'User-Agent': 'Mozilla/5.0'}

print('=== 1. VERIFY LOREBOOKS ===')
for lid in ['_zwEqgEEzh12X6gHVmMKKC', '_Uht3Ckz44JBDrPnUHq7LV']:
    req = urllib.request.Request(f'https://app.wyvern.chat/api/lorebooks/{lid}', headers=headers)
    with urllib.request.urlopen(req) as resp:
        lb = json.loads(resp.read().decode('utf-8'))
        lex = lb.get('lexicon', [])
        print(f"{lb.get('name')} ({lid}):")
        desc = lb.get('description', '')
        print(f"  description: {desc[:60]}...")
        print(f"  entries count: {len(lex)}")
        
        santiago = next((e for e in lex if 'Santiago' in e.get('name', '')), None)
        if santiago:
            print('  -> Santiago Herrera verified:')
            print('     name:', santiago.get('name'))
            print('     type:', santiago.get('type'))
            print('     avatar:', santiago.get('avatar'))
            print('     avatar_activation_regex:', santiago.get('avatar_activation_regex'))
            print('     lines_parsed:', santiago.get('lines_parsed'))
            print('     npc_info:', santiago.get('npc_info'))

print('\n=== 2. VERIFY CHARACTERS ===')
for cid, name in [('_cL86CRDAYABmaBWgdLQNw', 'Marek'), ('_x4F8TKXcU6naKT2CpKdHN', 'Russ'), ('_2EezhhEVdL677DULVdE9h', 'Neon Purr')]:
    req = urllib.request.Request(f'https://app.wyvern.chat/api/characters/{cid}', headers=headers)
    with urllib.request.urlopen(req) as resp:
        char = json.loads(resp.read().decode('utf-8'))
        print(f"{name} ({cid}) avatar: {char.get('avatar')}")

print('\n=== 3. VERIFY SCENARIO ===')
req = urllib.request.Request('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4', headers=headers)
with urllib.request.urlopen(req) as resp:
    scen = json.loads(resp.read().decode('utf-8'))
    print('Scenario name:', scen.get('name'))
    print('Scenario revision:', scen.get('revision'))
    has_npc_rule = '[NPC FORMATTING DISCIPLINE]' in scen.get('scenario', '')
    print('Has NPC Formatting Discipline:', has_npc_rule)
