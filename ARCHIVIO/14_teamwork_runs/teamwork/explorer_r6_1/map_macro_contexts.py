import json
import re
import pathlib

MY_DIR = pathlib.Path(__file__).parent
live_dump = json.loads((MY_DIR / 'live_scenarios_dump.json').read_text(encoding='utf-8'))
ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
alyssa_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json').read_text(encoding='utf-8'))
jasper_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json').read_text(encoding='utf-8'))

MACRO_REGEX = re.compile(r'\{\{scenarioChar\s+"([^"]+)"\}\}')

def map_replacements_for(sc, sc_name):
    print(f"\n=======================================================")
    print(f"=== DETAILED MACRO REPLACEMENT MAP FOR: {sc_name} ===")
    print(f"=======================================================")
    
    # We want to inspect all greeting content and message content
    greetings = sc.get('greetings', [])
    for g_idx, g in enumerate(greetings):
        g_name = g.get('name')
        print(f"\n-------------------------------------------------------")
        print(f"Greeting [{g_idx}]: '{g_name}' (id: {g.get('id')})")
        print(f"speaker_slot: {g.get('speaker_slot')}")
        
        # Check greeting.content
        g_content = g.get('content', '')
        matches = list(MACRO_REGEX.finditer(g_content))
        if matches:
            print(f"  greeting.content has {len(matches)} macros:")
            for m in matches:
                k = m.group(1)
                span = m.span()
                surround = g_content[max(0, span[0]-25):min(len(g_content), span[1]+25)]
                print(f"    Macro: {m.group(0)} (key: '{k}')")
                print(f"    Surround: ...{repr(surround)}...")

        # Check messages
        for m_idx, msg in enumerate(g.get('messages', [])):
            m_content = msg.get('content', '')
            m_matches = list(MACRO_REGEX.finditer(m_content))
            if m_matches:
                print(f"  msg[{m_idx}] (speaker_slot: '{msg.get('speaker_slot')}'): {len(m_matches)} macros:")
                for m in m_matches:
                    k = m.group(1)
                    span = m.span()
                    surround = m_content[max(0, span[0]-25):min(len(m_content), span[1]+25)]
                    print(f"    Macro: {m.group(0)} (key: '{k}')")
                    print(f"    Surround: ...{repr(surround)}...")

map_replacements_for(alyssa_local, "ALYSSA LOCAL (7 greetings)")
map_replacements_for(jasper_local, "JASPER LOCAL (6 greetings)")
