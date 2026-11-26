import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
live_file = ROOT / '.agents' / 'teamwork' / 'explorer_scenarios_15lb_2' / 'live_scenarios_inspection.json'
data = json.loads(live_file.read_text(encoding='utf-8'))

for sc_name, sc_info in data.items():
    sc_id = sc_info['id']
    rev = sc_info['revision']
    print(f"\n==========================================")
    print(f"Scenario: {sc_name} ({sc_id})")
    print(f"Revision: {rev} | Lorebooks count: {sc_info['lorebook_ids_count']} | Greetings count: {sc_info['greeting_count']}")
    
    # Check greetings in live data
    # Let's see greeting summary
    g_sum = sc_info.get('greetings_summary', [])
    for g in g_sum:
        print(f"  G[{g['index']}] Title/Name: '{g.get('title')}' | has_linked_persona_ids: {g['has_linked_persona_ids']} | linked_persona_ids: {g['linked_persona_ids']} | Preview: {g['first_msg_preview'][:50]}")
