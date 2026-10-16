import json
import re

with open('FINAL/Svartulfr_Master_Scenario.json', 'r', encoding='utf-8') as f:
    scen = json.load(f)

print('Current slots in JSON:')
for s in scen.get('slots', []):
    pool = [p.get('character_id') for p in s.get('pool', [])]
    print(f"  {s.get('key')}: label='{s.get('label')}', pool={pool}")

tags_used = set()
for g in scen.get('greetings', []):
    for m in g.get('messages', []):
        tags_used.update(re.findall(r'\{\{scenarioChar [^}]+\}\}', m.get('content', '')))
    tags_used.update(re.findall(r'\{\{scenarioChar [^}]+\}\}', g.get('content', '')))

print('\nScenarioChar tags used across all greetings:')
for t in sorted(tags_used):
    print(' ', t)

print('\nSpeaker slots used across all greetings:')
speakers = set()
for g in scen.get('greetings', []):
    speakers.add(g.get('speaker_slot'))
    for m in g.get('messages', []):
        speakers.add(m.get('speaker_slot'))
for sp in sorted(speakers):
    print(' ', sp)
