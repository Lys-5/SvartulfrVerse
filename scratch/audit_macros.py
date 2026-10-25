import json
import re

for fname in ['Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'Svartulfr_Scenario_SUCC_Route_Jasper.json']:
    print('=== ' + fname + ' ===')
    with open('FINAL/scenarios/' + fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Check slots
    print('Slots:')
    for s in data.get('slots', []):
        k = s.get('key')
        plen = len(s.get('pool', []))
        unavail = s.get('unavailable_count')
        print(f"  slot '{k}': pool_len={plen}, unavailable_count={unavail}")
        
    # Check macros in greetings
    print('\nGreetings macros:')
    for gi, g in enumerate(data.get('greetings', [])):
        title = g.get('name') or g.get('title')
        gm = re.findall(r'\{\{[^}]+\}\}', g.get('content', ''))
        spk = g.get('speaker_slot')
        print(f"  Greeting {gi} ({title}): speaker_slot={spk}, content_macros={gm}")
        for mi, m in enumerate(g.get('messages', [])):
            mm = re.findall(r'\{\{[^}]+\}\}', m.get('content', ''))
            mspk = m.get('speaker_slot')
            if mm:
                print(f"    Msg {mi} (speaker={mspk}): macros={mm}")
    
    # Check macros in scenario description
    desc_macros = re.findall(r'\{\{[^}]+\}\}', data.get('scenario', ''))
    print('\nScenario description macros:', desc_macros)
    print()
