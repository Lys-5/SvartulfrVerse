import json
import re

for fname in ['FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json']:
    with open(fname, 'r', encoding='utf-8') as f:
        sc = json.load(f)
    print(f"\n=== {fname} ===")
    slots = sc.get('slots', [])
    print(f"Slots count: {len(slots)}")
    for s in slots:
        k = s.get('key')
        lbl = s.get('label')
        plen = len(s.get('pool', []))
        unavail = s.get('unavailable_count')
        print(f"  slot: {k} | label: {lbl} | pool_len: {plen} | unavail: {unavail}")
    
    greetings = sc.get('greetings', [])
    print(f"Greetings count: {len(greetings)}")
    macro_matches = []
    for gi, g in enumerate(greetings):
        text = g.get('content', '')
        for m in re.finditer(r'\{\{([^}]+)\}\}', text):
            macro_matches.append((gi, 'greeting', m.group(0)))
        for mi, msg in enumerate(g.get('messages', [])):
            m_text = msg.get('content', '')
            for m in re.finditer(r'\{\{([^}]+)\}\}', m_text):
                macro_matches.append((gi, f'msg_{mi}', m.group(0)))
    print("Macros found in text:", set(m[2] for m in macro_matches))


print("\n--- SPEAKER_SLOT & GREETINGS INVARIANTS ---")
for fname in ['FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json']:
    with open(fname, 'r', encoding='utf-8') as f:
        sc = json.load(f)
    print(f"\n{fname}:")
    slot_keys = set(s['key'] for s in sc['slots'])
    for gi, g in enumerate(sc['greetings']):
        spk = g.get('speaker_slot')
        msgs = g.get('messages', [])
        m0_spk = msgs[0].get('speaker_slot') if msgs else None
        valid_spk = spk in slot_keys
        match_m0 = spk == m0_spk
        content_match = g.get('content') == (msgs[0].get('content') if msgs else None)
        print(f"  g{gi} ({g.get('title')}): spk={spk}, m0_spk={m0_spk}, valid_slot={valid_spk}, match_m0={match_m0}, content_match={content_match}")
