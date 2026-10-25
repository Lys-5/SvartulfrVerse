import json
import pathlib

for f in sorted(pathlib.Path('FINAL/scenarios').glob('*.json')):
    d = json.loads(f.read_text(encoding='utf-8'))
    print(f"\n--- {f.name} ---")
    for s in d.get('slots', []):
        for c in s.get('pool', []):
            print(f"  slot={s.get('key'):<25} label={s.get('label'):<35} id={c.get('character_id')} weight={c.get('weight')}")
