import json
import re
import pathlib

MY_DIR = pathlib.Path(__file__).parent
all_macros = json.loads((MY_DIR / 'all_macros_extracted.json').read_text(encoding='utf-8'))
ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
alyssa_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json').read_text(encoding='utf-8'))
jasper_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json').read_text(encoding='utf-8'))

MACRO_REGEX = re.compile(r'\{\{scenarioChar\s+"([^"]+)"\}\}')

REPLACEMENTS_ALYSSA = {
    'best_friend': 'Scarlett Rose',
    'roommate': 'Sierra Cruz',
    'quarterback': 'Jared Thompson',
    'friend': 'Stanley Davies Jr.',
    # also note:
    'childhood_friend': 'Finnegan Novak',
    'sports_rival': 'Vincent Campbell'
}

REPLACEMENTS_JASPER = {
    'crush': 'Scarlett Rose',
    'male_roommate': 'Russell Sinclair',
    'quarterback': 'Jared Thompson',
    'friend': 'Stanley Davies Jr.',
    # also note:
    'twin': 'Alyssa Hvit Douglas Bloodmoon',
    'childhood_friend': 'Finnegan Novak',
    'sports_rival': 'Vincent Campbell'
}

def show_transformed(sc, reps, sc_name):
    print(f"\n=======================================================")
    print(f"=== FULL SENTENCE TRANSFORMATIONS FOR {sc_name} ===")
    print(f"=======================================================")
    for g_idx, g in enumerate(sc['greetings']):
        print(f"\n--- GREETING {g_idx}: {g['name']} ---")
        g_content = g['content']
        for m in MACRO_REGEX.finditer(g_content):
            k = m.group(1)
            if k in reps:
                rep_val = reps[k]
                # let's see replaced version
                replaced = g_content.replace(m.group(0), rep_val)
                print(f"  [G.content] Key '{k}' -> '{rep_val}'")
                print(f"    ORIGINAL : {g_content[:120]}...")
                print(f"    REPLACED : {replaced[:120]}...")
        
        for m_idx, msg in enumerate(g['messages']):
            m_content = msg['content']
            for m in MACRO_REGEX.finditer(m_content):
                k = m.group(1)
                if k in reps:
                    rep_val = reps[k]
                    replaced = m_content.replace(m.group(0), rep_val)
                    print(f"  [msg[{m_idx}] ({msg['speaker_slot']})] Key '{k}' -> '{rep_val}'")
                    print(f"    ORIGINAL : {m_content[:120]}...")
                    print(f"    REPLACED : {replaced[:120]}...")

show_transformed(alyssa_local, REPLACEMENTS_ALYSSA, "ALYSSA ROUTE")
show_transformed(jasper_local, REPLACEMENTS_JASPER, "JASPER ROUTE")
