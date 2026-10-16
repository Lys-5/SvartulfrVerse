import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
exp = json.loads((ROOT / 'exports' / 'Svartulfr_Export.json').read_text(encoding='utf-8'))

out_lines = []
for sc in exp['world_scenarios']:
    out_lines.append(f"==================================================")
    out_lines.append(f"SCENARIO: {sc.get('name')} ({sc.get('id')})")
    out_lines.append(f"==================================================")
    for idx, ps in enumerate(sc.get('premade_scenes', []), 1):
        out_lines.append(f"\n--- SCENE {idx:02d}: {ps.get('id')} | {ps.get('description')} ---")
        out_lines.append(ps.get('scene_text', ''))

(ROOT / 'scratch' / 'all_world_scenes_dump.txt').write_text('\n'.join(out_lines), encoding='utf-8')
print('Dumped all scenes to scratch/all_world_scenes_dump.txt, lines:', len('\n'.join(out_lines).splitlines()))
