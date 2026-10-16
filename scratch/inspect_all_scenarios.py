import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
p22 = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\fa5c149a-3193-41b6-a44f-45396c7b7227\.system_generated\steps\22\output.txt')
for line in p22.read_text(encoding='utf-8').splitlines():
    if line.strip().startswith('{'):
        d22 = json.loads(line.strip())
        cs = d22['csEdit']['json']
        out_p = ROOT / 'scratch' / 'live_wyvern_snapshot_oct16' / 'char_scenario_live.json'
        out_p.write_text(json.dumps(cs, indent=2, ensure_ascii=False), encoding='utf-8')
        print('Saved char_scenario_live.json! Keys:', list(cs.keys()))
        scen = cs.get('scenario', cs)
        print('Scenario keys:', list(scen.keys()))
        print('Revision:', scen.get('revision'), 'Slots:', len(scen.get('slots', [])), 'Greetings:', len(scen.get('greetings', [])))
        for s in scen.get('slots', []):
            print('  Slot:', s.get('key'), '|', s.get('label'), '| pool:', s.get('pool'))
        for g in scen.get('greetings', []):
            print('  Greeting:', g.get('id'), '| title:', g.get('title'), '| msgs:', len(g.get('messages', [])))

exp = json.loads((ROOT / 'exports' / 'Svartulfr_Export.json').read_text(encoding='utf-8'))
for sc in exp['world_scenarios']:
    print(f"\n=== World Scenario: {sc.get('name')} ({sc.get('id')}) ===")
    for idx, ps in enumerate(sc.get('premade_scenes', []), 1):
        txt = ps.get('scene_text', '')
        speakers = re.findall(r'^=>([^:\n]+):', txt, re.MULTILINE)
        print(f"  {idx:02d}. {ps.get('description')[:80]} | speakers={speakers} | turns={len(speakers)}")
