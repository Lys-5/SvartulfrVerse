import json
import re

for name in ['Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'Svartulfr_Scenario_SUCC_Route_Jasper.json']:
    print(f"\n==================== {name} ====================")
    data = json.load(open(f'FINAL/scenarios/{name}', encoding='utf-8'))
    for i, g in enumerate(data.get('greetings', [])):
        print(f"\n--- Greeting {i}: {g.get('name')} (speaker_slot: {g.get('speaker_slot')}) ---")
        g_macros = re.findall(r'\{\{scenarioChar\s+"([^"]+)"\}\}', g.get('content', ''))
        if g_macros:
            print(f"  greeting.content macros: {g_macros}")
        for j, m in enumerate(g.get('messages', [])):
            m_macros = re.findall(r'\{\{scenarioChar\s+"([^"]+)"\}\}', m.get('content', ''))
            if m_macros:
                print(f"  msg[{j}] (speaker: {m.get('speaker_slot')}): {m_macros}")
                # print snippet of matching lines
                for line in m.get('content', '').split('\n'):
                    if 'scenarioChar' in line:
                        print(f"    Line: {line.strip()}")
