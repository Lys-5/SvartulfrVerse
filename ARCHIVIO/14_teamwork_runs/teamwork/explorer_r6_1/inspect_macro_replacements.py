import json
import re
import pathlib

MY_DIR = pathlib.Path(__file__).parent
live_dump = json.loads((MY_DIR / 'live_scenarios_dump.json').read_text(encoding='utf-8'))

MACRO_REGEX = re.compile(r'\{\{scenarioChar\s+"([^"]+)"\}\}')

TARGET_NPCS = {
    'alyssa': {
        'best_friend': 'Scarlett Rose',
        'roommate': 'Sierra Cruz',
        'quarterback': 'Jared Thompson',
        'friend': 'Stanley Davies Jr.',
        # Also check other slots
        'childhood_friend': 'Finnegan Novak',
        'sports_rival': 'Vincent Campbell',
        'twin': 'Jasper Svartr Douglas Bloodmoon',
        'crush': 'Mackenzie Sanchez-Rogers'
    },
    'jasper': {
        'crush': 'Scarlett Rose',
        'male_roommate': 'Russell Sinclair',
        'quarterback': 'Jared Thompson',
        'friend': 'Stanley Davies Jr.',
        'childhood_friend': 'Finnegan Novak',
        'sports_rival': 'Vincent Campbell',
        'twin': 'Alyssa Hvit Douglas Bloodmoon',
        'ai_companion': 'Echo'
    }
}

def analyze_macros_for(scenario, sc_type):
    name = scenario.get('name')
    greetings = scenario.get('greetings', [])
    print(f"\n=======================================================")
    print(f"=== MACRO REPLACEMENT ANALYSIS: {name} ({sc_type.upper()}) ===")
    print(f"=======================================================")
    
    total_macros = 0
    npc_macros = 0
    mappings = TARGET_NPCS[sc_type]
    
    for g_idx, g in enumerate(greetings):
        g_name = g.get('name')
        g_content = g.get('content', '')
        g_matches = list(MACRO_REGEX.finditer(g_content))
        
        print(f"\n--- GREETING [{g_idx}] '{g_name}' (Speaker: '{g.get('speaker_slot')}') ---")
        if g_matches:
            print(f"  In greeting.content ({len(g_matches)} macros):")
            for m in g_matches:
                k = m.group(1)
                total_macros += 1
                is_target = k in ['best_friend', 'roommate', 'quarterback', 'friend', 'male_roommate', 'crush']
                if is_target:
                    npc_macros += 1
                ctx_start = max(0, m.start() - 30)
                ctx_end = min(len(g_content), m.end() + 30)
                ctx = g_content[ctx_start:ctx_end].replace('\n', ' ')
                target_char = mappings.get(k, 'UNKNOWN')
                print(f"    - Macro: {m.group(0)} | Key: {k} -> Char: {target_char} | Target NPC? {is_target}")
                print(f"      Context: ...{ctx}...")

        messages = g.get('messages', [])
        for m_idx, msg in enumerate(messages):
            m_speaker = msg.get('speaker_slot')
            m_content = msg.get('content', '')
            m_matches = list(MACRO_REGEX.finditer(m_content))
            if m_matches:
                print(f"  In msg[{m_idx}] (speaker_slot: '{m_speaker}') ({len(m_matches)} macros):")
                for m in m_matches:
                    k = m.group(1)
                    total_macros += 1
                    is_target = k in ['best_friend', 'roommate', 'quarterback', 'friend', 'male_roommate', 'crush']
                    if is_target:
                        npc_macros += 1
                    ctx_start = max(0, m.start() - 30)
                    ctx_end = min(len(m_content), m.end() + 30)
                    ctx = m_content[ctx_start:ctx_end].replace('\n', ' ')
                    target_char = mappings.get(k, 'UNKNOWN')
                    print(f"    - Macro: {m.group(0)} | Key: {k} -> Char: {target_char} | Target NPC? {is_target}")
                    print(f"      Context: ...{ctx}...")

    print(f"\nTotal macros in {sc_type}: {total_macros} (NPC target macros: {npc_macros})")

analyze_macros_for(live_dump['char_scenario_CKgwq246DyCj1NNTBV9rt'], 'alyssa')
analyze_macros_for(live_dump['char_scenario_Kq4mJEBH83j7Q7DdVfFnF'], 'jasper')
