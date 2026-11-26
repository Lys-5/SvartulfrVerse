import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
MY_DIR = pathlib.Path(__file__).parent
live_dump = json.loads((MY_DIR / 'live_scenarios_dump.json').read_text(encoding='utf-8'))

alyssa_live = live_dump['char_scenario_CKgwq246DyCj1NNTBV9rt']
jasper_live = live_dump['char_scenario_Kq4mJEBH83j7Q7DdVfFnF']

alyssa_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json').read_text(encoding='utf-8'))
jasper_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json').read_text(encoding='utf-8'))

def compare(live, local, name):
    print(f"==================== COMPARING {name} ====================")
    keys = set(live.keys()) | set(local.keys())
    for k in sorted(keys):
        if k in ['greetings', 'slots']:
            continue
        v_live = live.get(k)
        v_local = local.get(k)
        if v_live != v_local:
            print(f"Key '{k}' differs:")
            print(f"  LIVE : {repr(v_live)[:150]}")
            print(f"  LOCAL: {repr(v_local)[:150]}")

    print("\n-- SLOTS DIFF --")
    slots_live = live.get('slots', [])
    slots_local = local.get('slots', [])
    print(f"Live slots ({len(slots_live)}): {[s['key'] for s in slots_live]}")
    print(f"Local slots ({len(slots_local)}): {[s['key'] for s in slots_local]}")

    print("\n-- GREETINGS COUNT & IDS --")
    g_live = live.get('greetings', [])
    g_local = local.get('greetings', [])
    print(f"Live greetings count: {len(g_live)}")
    print(f"Local greetings count: {len(g_local)}")
    for i in range(max(len(g_live), len(g_local))):
        gl = g_live[i] if i < len(g_live) else None
        loc = g_local[i] if i < len(g_local) else None
        gl_id = gl.get('id') if gl else 'NONE'
        loc_id = loc.get('id') if loc else 'NONE'
        gl_name = gl.get('name') if gl else 'NONE'
        loc_name = loc.get('name') if loc else 'NONE'
        diff = "MATCH" if gl_id == loc_id and gl_name == loc_name else "DIFF"
        print(f"  [{i}] LIVE: ({gl_id}) '{gl_name}' | LOCAL: ({loc_id}) '{loc_name}' -> {diff}")

compare(alyssa_live, alyssa_local, "ALYSSA")
compare(jasper_live, jasper_local, "JASPER")
