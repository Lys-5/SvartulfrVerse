import json
import pathlib

SC_DIR = pathlib.Path('FINAL/scenarios')
for fname in [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json"
]:
    f = SC_DIR / fname
    data = json.loads(f.read_text(encoding='utf-8'))
    print(f"\n==========================================")
    print(f"FILE: {f.name}")
    print(f"==========================================")
    print(f"Name: {data.get('name')}")
    print(f"Display description: {data.get('display_description')}")
    print(f"Visibility: {data.get('visibility')}")
    print(f"Rating: {data.get('rating')}")
    print(f"Lorebook IDs: {data.get('lorebook_ids')}")
    
    slots = data.get('slots', [])
    print(f"Slots ({len(slots)}):")
    for s in slots:
        pool_chars = [c.get('character_id') for c in s.get('pool', [])]
        print(f"  - Key: {s.get('key'):<25} Label: {s.get('label'):<35} unavail: {s.get('unavailable_count')} pool: {pool_chars}")
        
    greetings = data.get('greetings', [])
    print(f"Greetings ({len(greetings)}):")
    for g_idx, g in enumerate(greetings):
        msgs = g.get('messages', [])
        print(f"  [{g_idx}] Name: {g.get('name')} | Speaker: {g.get('speaker_slot')} | Messages: {len(msgs)}")
        for m_idx, m in enumerate(msgs):
            c = m.get('content', '')
            print(f"      msg[{m_idx}] slot={m.get('speaker_slot')}: {c[:100]}...")
