import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('FINAL/scenarios/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    print(f"\n========================================================")
    print(f"SAMPLE GREETINGS & MACRO VERIFICATION: {f}")
    
    slots = {s['key']: s for s in d.get('slots', [])}
    
    # Check scenarioChar macros
    scenario_txt = d.get('scenario', '')
    macro_slots = re.findall(r'\{\{scenarioChar \\?"([a-zA-Z0-9_-]+)\\?"\}\}', scenario_txt)
    for ms in macro_slots:
        if ms not in slots:
            print(f"  ERROR: Macro slot '{ms}' not defined in slots!")
        else:
            print(f"  Macro slot verified: '{ms}' in slots")
            
    # Sample first greeting messages
    first_greeting = d.get('greetings', [])[0]
    print(f"\nGreeting 0 ('{first_greeting.get('name')}'):")
    for m in first_greeting.get('messages', []):
        slot_key = m.get('speaker_slot')
        print(f"  [{slot_key}]: {m.get('content')[:140]}...")
