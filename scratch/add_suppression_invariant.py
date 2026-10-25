import json

sc_path = 'FINAL/Svartulfr_Master_Scenario.json'
sc = json.load(open(sc_path, encoding='utf-8'))

scenario_text = sc['scenario']
suppression_rule = """[PERSPECTIVE & LOREBOOK SUPPRESSION INVARIANT]:
The active {{user}} and the active assigned {{scenarioChar "twin"}} are the definitive twin protagonists of this story. Any background lorebook entries or encyclopedic dossiers referring to either Alyssa or Jasper serve exclusively as passive world-building reference and must NEVER create duplicate character personas, third-person ghost dialogue, split-personality narration, or alter the active speaker slot of {{scenarioChar "twin"}}."""

if '[PERSPECTIVE & LOREBOOK SUPPRESSION INVARIANT]' not in scenario_text:
    sc['scenario'] = scenario_text.strip() + '\n\n' + suppression_rule.strip()
    print('Added suppression directive to scenario!')
else:
    print('Suppression directive already present!')

with open(sc_path, 'w', encoding='utf-8') as f:
    json.dump(sc, f, ensure_ascii=False, indent=2)

print('Scenario text len:', len(sc['scenario']))
