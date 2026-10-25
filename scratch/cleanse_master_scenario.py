import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
p = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'

data = json.loads(p.read_text(encoding='utf-8'))

# 1. Linked personas comments
fixed_comments = 0
for g in data.get('greetings', []):
    for lp in g.get('linked_personas', []):
        c = lp.get('comment', '')
        if '—' in c:
            lp['comment'] = c.replace('—', ', ')
            fixed_comments += 1

print(f'Fixed {fixed_comments} linked_personas comments.')

# 2. Scenario name
if '—' in data.get('name', ''):
    data['name'] = data['name'].replace('—', '-')
    print('Fixed name em-dash.')

# 3. Final instructions
if '—' in data.get('final_instructions', ''):
    data['final_instructions'] = data['final_instructions'].replace('NEVER use em-dashes (—)', 'NEVER use em-dashes')
    print('Fixed final_instructions em-dash.')

# 4. Wulfnic age in scenario
if '1,197-year-old' in data.get('scenario', ''):
    data['scenario'] = data['scenario'].replace('1,197-year-old', '1,200-year-old')
    print('Fixed Wulfnic age in scenario description.')

# Verify 0 em-dashes remaining in JSON
raw_txt = json.dumps(data, indent=2, ensure_ascii=False)
assert '—' not in raw_txt, f"Em-dash still found in Master Scenario! Count: {raw_txt.count('—')}"

p.write_text(raw_txt, encoding='utf-8')
print('Successfully cleansed FINAL/Svartulfr_Master_Scenario.json! 0 em-dashes remaining.')
