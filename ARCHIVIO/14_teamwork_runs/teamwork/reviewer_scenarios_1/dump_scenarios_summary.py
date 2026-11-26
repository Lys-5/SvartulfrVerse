import json
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
SCENARIOS_DIR = ROOT / 'FINAL' / 'scenarios'

files = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
]

for fname in files:
    fpath = SCENARIOS_DIR / fname
    data = json.loads(fpath.read_text(encoding='utf-8'))
    print(f"\n========================================================")
    print(f"FILE: {fname}")
    print(f"Name: {data.get('name')}")
    print(f"Visibility: {data.get('visibility')} | Rating: {data.get('rating')}")
    print(f"Avatar: {data.get('avatar')}")
    print(f"Tags: {data.get('tags')}")
    print(f"Lorebooks: {data.get('lorebook_ids')}")
    print(f"Scenario length: {len(data.get('scenario', ''))} chars")
    print(f"Startup script length: {len(data.get('startup_script') or '')} chars")
    
    slots = data.get('slots', [])
    print(f"\nSLOTS ({len(slots)}):")
    for s in slots:
        pool_str = ", ".join([f"{p.get('character_id')}(w:{p.get('weight')})" for p in s.get('pool', [])])
        print(f"  - Key: '{s.get('key')}' | Label: '{s.get('label')}' | Unavail: {s.get('unavailable_count')} | Pool: [{pool_str}]")
        
    greetings = data.get('greetings', [])
    print(f"\nGREETINGS ({len(greetings)}):")
    for g_idx, g in enumerate(greetings):
        msgs = g.get('messages', [])
        speakers = [m.get('speaker_slot') for m in msgs]
        word_count = sum(len(m.get('content', '').split()) for m in msgs)
        print(f"  [{g_idx}] Name: '{g.get('name')}' | SpeakerSlot: '{g.get('speaker_slot')}' | Msgs: {len(msgs)} | Words: {word_count} | Flow: {' -> '.join(speakers)}")

