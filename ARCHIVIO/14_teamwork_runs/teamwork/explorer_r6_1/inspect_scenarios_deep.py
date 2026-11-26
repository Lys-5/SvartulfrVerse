import json
import re
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
MY_DIR = pathlib.Path(__file__).parent

# Load live dump
live_dump_path = MY_DIR / 'live_scenarios_dump.json'
live_dump = json.loads(live_dump_path.read_text(encoding='utf-8'))

# Load local scenarios
alyssa_local_path = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json'
jasper_local_path = ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json'

alyssa_local = json.loads(alyssa_local_path.read_text(encoding='utf-8'))
jasper_local = json.loads(jasper_local_path.read_text(encoding='utf-8'))

MACRO_REGEX = re.compile(r'\{\{scenarioChar\s+"([^"]+)"\}\}')

def analyze_scenario(sc_data, sc_name, is_live=False):
    report = {
        'name': sc_name,
        'id': sc_data.get('id'),
        'revision': sc_data.get('revision'),
        'visibility': sc_data.get('visibility'),
        'rating': sc_data.get('rating'),
        'lorebook_ids_count': len(sc_data.get('lorebook_ids', [])),
        'lorebook_ids': sc_data.get('lorebook_ids', []),
        'slots': [],
        'slots_with_unavailable_count_gt_0': [],
        'macro_occurrences_scenario_text': [],
        'greetings_analysis': []
    }

    # Inspect slots
    slots = sc_data.get('slots', [])
    slot_keys = set()
    for s in slots:
        key = s.get('key')
        label = s.get('label')
        unavail = s.get('unavailable_count', 0)
        pool = s.get('pool', [])
        slot_keys.add(key)
        slot_info = {
            'key': key,
            'label': label,
            'unavailable_count': unavail,
            'pool_size': len(pool),
            'pool_items': pool
        }
        report['slots'].append(slot_info)
        if unavail > 0:
            report['slots_with_unavailable_count_gt_0'].append(slot_info)

    # Inspect scenario text for macros
    sc_text = sc_data.get('scenario', '')
    for m in MACRO_REGEX.finditer(sc_text):
        report['macro_occurrences_scenario_text'].append({
            'macro': m.group(0),
            'key': m.group(1),
            'context': sc_text[max(0, m.start()-20):min(len(sc_text), m.end()+40)]
        })

    # Inspect greetings
    greetings = sc_data.get('greetings', [])
    for g_idx, g in enumerate(greetings):
        g_id = g.get('id')
        g_name = g.get('name')
        g_speaker = g.get('speaker_slot')
        g_content = g.get('content', '')
        g_linked_personas = g.get('linked_persona_ids', [])
        messages = g.get('messages', [])

        g_macros = []
        for m in MACRO_REGEX.finditer(g_content):
            g_macros.append({
                'macro': m.group(0),
                'key': m.group(1),
                'context': g_content[max(0, m.start()-20):min(len(g_content), m.end()+40)]
            })

        msg_list = []
        for m_idx, msg in enumerate(messages):
            m_id = msg.get('id')
            m_speaker = msg.get('speaker_slot')
            m_content = msg.get('content', '')
            m_macros = []
            for m in MACRO_REGEX.finditer(m_content):
                m_macros.append({
                    'macro': m.group(0),
                    'key': m.group(1),
                    'context': m_content[max(0, m.start()-20):min(len(m_content), m.end()+40)]
                })
            msg_list.append({
                'msg_index': m_idx,
                'id': m_id,
                'speaker_slot': m_speaker,
                'speaker_valid_slot': m_speaker in slot_keys,
                'content_len': len(m_content),
                'content_preview': m_content[:80],
                'macros': m_macros
            })

        # Invariant check
        m0_speaker = messages[0].get('speaker_slot') if messages else None
        m0_content = messages[0].get('content') if messages else None
        invariant_speaker = (g_speaker == m0_speaker)
        invariant_content = (g_content == m0_content)

        report['greetings_analysis'].append({
            'index': g_idx,
            'id': g_id,
            'name': g_name,
            'speaker_slot': g_speaker,
            'speaker_valid_slot': g_speaker in slot_keys,
            'invariant_speaker_m0': invariant_speaker,
            'invariant_content_m0': invariant_content,
            'linked_persona_ids': g_linked_personas,
            'g_macros': g_macros,
            'messages_count': len(messages),
            'messages': msg_list
        })

    return report

analysis = {
    'live_alyssa': analyze_scenario(live_dump['char_scenario_CKgwq246DyCj1NNTBV9rt'], 'Alyssa Live (CKgwq246DyCj1NNTBV9rt)', is_live=True),
    'live_jasper': analyze_scenario(live_dump['char_scenario_Kq4mJEBH83j7Q7DdVfFnF'], 'Jasper Live (Kq4mJEBH83j7Q7DdVfFnF)', is_live=True),
    'local_alyssa': analyze_scenario(alyssa_local, 'Alyssa Local'),
    'local_jasper': analyze_scenario(jasper_local, 'Jasper Local')
}

out_report_path = MY_DIR / 'scenario_deep_analysis.json'
out_report_path.write_text(json.dumps(analysis, indent=2, ensure_ascii=False), encoding='utf-8')
print("Analysis complete, saved to", out_report_path)
