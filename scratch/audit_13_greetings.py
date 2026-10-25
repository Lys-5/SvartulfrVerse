import json
import pathlib
import urllib.request
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'ChallengerBot/1.0'}

def api_get(url):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

alyssa = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_CKgwq246DyCj1NNTBV9rt')
jasper = api_get('https://app.wyvern.chat/api/character-scenarios/char_scenario_Kq4mJEBH83j7Q7DdVfFnF')

print('=================== ALL 13 GREETINGS AUDIT ===================')

for sc_name, sc in [('Alyssa Route', alyssa), ('Jasper Route', jasper)]:
    print(f'\n--- {sc_name} (ID: {sc["id"]}, Rev: {sc["revision"]}) ---')
    slots = {s['key']: s for s in sc['slots']}
    for g_idx, g in enumerate(sc['greetings']):
        msgs = g['messages']
        m0 = msgs[0]
        spk_g = g['speaker_slot']
        spk_m0 = m0['speaker_slot']
        content_g = g['content']
        content_m0 = m0['content']
        
        # Check invariants
        assert spk_g == spk_m0, f'Speaker mismatch: g={spk_g}, m0={spk_m0}'
        assert content_g == content_m0, f'Content mismatch in G{g_idx}'
        assert spk_g in slots, f'Speaker {spk_g} not in slots!'
        
        # Check em-dash
        em_dash_count = sum(m['content'].count('\u2014') for m in msgs) + content_g.count('\u2014')
        assert em_dash_count == 0, f'Em-dash found in G{g_idx}'
        
        # Check macros
        macros_found = []
        for m_idx, m in enumerate(msgs):
            for match in re.findall(r'\{\{[^\}]+\}\}', m['content']):
                macros_found.append((m_idx, match))
                
        print(f'G{g_idx}: "{g.get("name")}" | Speaker: {spk_g} (pool={len(slots[spk_g]["pool"])}) | Msgs: {len(msgs)} | Em-dashes: {em_dash_count} | Macros: {macros_found}')
