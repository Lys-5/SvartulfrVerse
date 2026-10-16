import json

with open('FINAL/Svartulfr_Master_Scenario.json', 'r', encoding='utf-8') as f:
    scen = json.load(f)

valid_slots = {
    'maternal_grandfather',
    'father',
    'eldest_brother',
    'brother',
    'twin',
    'uncle',
    'cousin',
    'quarterback',
    'crush',
    'friend',
    'roommate',
    'best_friend',
    'dorm_roommate'
}

print(f"Total greetings: {len(scen.get('greetings', []))}")
for idx, g in enumerate(scen.get('greetings', [])):
    sp = g.get('speaker_slot')
    msp = [m.get('speaker_slot') for m in g.get('messages', [])]
    all_sp = set([sp] + msp)
    invalid = all_sp - valid_slots
    if invalid:
        print(f"Greeting {idx:02d} [{g.get('id')}]: invalid speaker slots: {invalid}")
