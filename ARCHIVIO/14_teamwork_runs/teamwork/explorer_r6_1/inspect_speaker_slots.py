import json
import pathlib

MY_DIR = pathlib.Path(__file__).parent
live_dump = json.loads((MY_DIR / 'live_scenarios_dump.json').read_text(encoding='utf-8'))
ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
alyssa_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json').read_text(encoding='utf-8'))
jasper_local = json.loads((ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json').read_text(encoding='utf-8'))

def inspect_speakers(sc, name):
    print(f"\n=======================================================")
    print(f"=== SPEAKER_SLOT INSPECTION: {name} ===")
    print(f"=======================================================")
    slot_keys = [s['key'] for s in sc.get('slots', [])]
    slot_pools = {s['key']: s.get('pool', []) for s in sc.get('slots', [])}
    slot_unavail = {s['key']: s.get('unavailable_count', 0) for s in sc.get('slots', [])}
    print(f"Defined slots ({len(slot_keys)}): {slot_keys}")
    for k in slot_keys:
        p = slot_pools[k]
        u = slot_unavail[k]
        print(f"  Slot '{k}': unavail={u}, pool={[item['character_id'] for item in p]}")

    print("\nGreetings & Messages Speaker Slots:")
    for g_idx, g in enumerate(sc.get('greetings', [])):
        g_speaker = g.get('speaker_slot')
        g_valid = g_speaker in slot_keys
        msgs = g.get('messages', [])
        print(f"\n  G[{g_idx}] '{g.get('name')}':")
        print(f"    g.speaker_slot: '{g_speaker}' (Valid in slots: {g_valid}, Pool size: {len(slot_pools.get(g_speaker, []))}, Unavail: {slot_unavail.get(g_speaker, 'N/A')})")
        for m_idx, m in enumerate(msgs):
            m_speaker = m.get('speaker_slot')
            m_valid = m_speaker in slot_keys
            print(f"    m[{m_idx}].speaker_slot: '{m_speaker}' (Valid in slots: {m_valid}, Pool size: {len(slot_pools.get(m_speaker, []))}, Unavail: {slot_unavail.get(m_speaker, 'N/A')})")
            if not m_valid:
                print(f"      *** ERROR: m[{m_idx}].speaker_slot '{m_speaker}' is NOT in scenario slots! ***")
        if g_speaker != msgs[0].get('speaker_slot'):
            print(f"      *** WARNING: g.speaker_slot '{g_speaker}' != m[0].speaker_slot '{msgs[0].get('speaker_slot')}' ***")

inspect_speakers(live_dump['char_scenario_CKgwq246DyCj1NNTBV9rt'], "ALYSSA LIVE (rev 10)")
inspect_speakers(alyssa_local, "ALYSSA LOCAL (rev 8)")
inspect_speakers(live_dump['char_scenario_Kq4mJEBH83j7Q7DdVfFnF'], "JASPER LIVE (rev 4)")
inspect_speakers(jasper_local, "JASPER LOCAL (rev 4)")
