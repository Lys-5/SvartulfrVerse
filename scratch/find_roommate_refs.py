import json
import re

with open('FINAL/Svartulfr_Master_Scenario.json', 'r', encoding='utf-8') as f:
    scen = json.load(f)

print('Occurrences in scenario text:')
for m in re.finditer(r'roommate', scen.get('scenario', ''), re.IGNORECASE):
    s = max(0, m.start() - 30)
    e = min(len(scen['scenario']), m.end() + 30)
    print(' ', repr(scen['scenario'][s:e]))

print('\nOccurrences in greetings:')
for idx, g in enumerate(scen.get('greetings', [])):
    sp = g.get('speaker_slot')
    msp = [m.get('speaker_slot') for m in g.get('messages', [])]
    text = json.dumps(g)
    if 'roommate' in text.lower():
        print(f"Greeting {idx:02d} [{g.get('id')}]: main_sp={sp}, msg_sp={msp}")
        matches = re.findall(r'\{\{scenarioChar [^}]+\}\}', text)
        print('   Tags found:', set(matches))
