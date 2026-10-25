import json
from pathlib import Path

ROOT = Path('e:/repository/SvartulfrVerse')
with open(ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json', 'r', encoding='utf-8') as f:
    raw_json = f.read()

em_dashes = [c for c in raw_json if c in '—\u2014']
print(f"Em-dashes in entire raw JSON string of Svartulfr_World_Scenario_SUCC_Welcome_Day.json: {len(em_dashes)}")

# Also check for other dashes like en-dash
en_dashes = [c for c in raw_json if c == '\u2013']
print(f"En-dashes in raw JSON: {len(en_dashes)}")

# Check asterisks in raw JSON
asterisks = [c for c in raw_json if c == '*']
print(f"Asterisks in entire raw JSON: {len(asterisks)}")
