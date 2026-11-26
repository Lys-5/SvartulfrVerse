import json
import re
import pathlib

MY_DIR = pathlib.Path(__file__).parent
ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
live_dump = json.loads((MY_DIR / 'live_scenarios_dump.json').read_text(encoding='utf-8'))
alyssa_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json').read_text(encoding='utf-8'))
jasper_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json').read_text(encoding='utf-8'))

MACRO_REGEX = re.compile(r'\{\{scenarioChar\s+"([^"]+)"\}\}')

def extract_all(sc, sc_name):
    rows = []
    for g_idx, g in enumerate(sc.get('greetings', [])):
        g_name = g.get('name')
        g_id = g.get('id')
        g_speaker = g.get('speaker_slot')
        
        # greeting content
        for m in MACRO_REGEX.finditer(g.get('content', '')):
            k = m.group(1)
            span = m.span()
            ctx = g.get('content', '')[max(0, span[0]-35):min(len(g.get('content', '')), span[1]+35)].replace('\n', ' ')
            rows.append({
                'scenario': sc_name,
                'greeting_idx': g_idx,
                'greeting_name': g_name,
                'location': 'greeting.content',
                'speaker_slot': g_speaker,
                'macro': m.group(0),
                'key': k,
                'span': span,
                'context': ctx
            })
            
        # messages
        for m_idx, msg in enumerate(g.get('messages', [])):
            for m in MACRO_REGEX.finditer(msg.get('content', '')):
                k = m.group(1)
                span = m.span()
                ctx = msg.get('content', '')[max(0, span[0]-35):min(len(msg.get('content', '')), span[1]+35)].replace('\n', ' ')
                rows.append({
                    'scenario': sc_name,
                    'greeting_idx': g_idx,
                    'greeting_name': g_name,
                    'location': f"messages[{m_idx}]",
                    'msg_speaker_slot': msg.get('speaker_slot'),
                    'macro': m.group(0),
                    'key': k,
                    'span': span,
                    'context': ctx
                })
    return rows

alyssa_rows = extract_all(alyssa_local, 'Alyssa Route')
jasper_rows = extract_all(jasper_local, 'Jasper Route')

out_data = {
    'alyssa': alyssa_rows,
    'jasper': jasper_rows
}

(MY_DIR / 'all_macros_extracted.json').write_text(json.dumps(out_data, indent=2, ensure_ascii=False), encoding='utf-8')

print(f"Extracted {len(alyssa_rows)} macros for Alyssa, {len(jasper_rows)} macros for Jasper.")
