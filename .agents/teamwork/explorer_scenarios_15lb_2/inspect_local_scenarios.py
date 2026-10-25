import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
scenarios_dir = ROOT / 'FINAL' / 'scenarios'
master_file = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'

files = list(scenarios_dir.glob('*.json')) + [master_file]

print(f"Found {len(files)} local scenario files:")
for f in files:
    data = json.loads(f.read_text(encoding='utf-8'))
    print(f"\n--- {f.name} ---")
    print(f"ID: {data.get('id')}")
    print(f"Name: {data.get('name')}")
    print(f"Revision in file: {data.get('revision')}")
    print(f"Lorebook IDs count: {len(data.get('lorebook_ids', []))}")
    print(f"Lorebook IDs: {data.get('lorebook_ids')}")
    greetings = data.get('greetings', [])
    print(f"Greetings count: {len(greetings)}")
    if greetings:
        g0 = greetings[0]
        print(f"Greeting 0 keys: {list(g0.keys())}")
        print(f"Greeting 0 linked_persona_ids: {g0.get('linked_persona_ids')}")
        # check all greetings for linked_persona_ids
        lp_list = [g.get('linked_persona_ids') for g in greetings]
        print(f"All greetings linked_persona_ids: {lp_list}")
