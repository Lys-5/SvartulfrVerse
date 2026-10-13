import subprocess
import json

out = subprocess.check_output(['git', 'show', '036bff6:exports/Svartulfr_Export.json'], text=True, encoding='utf-8')
data = json.loads(out)['world']
print("Commit 036bff6 species count:", len(data.get('species', [])))
print(json.dumps(data.get('species', [])[:5], indent=2))
print("Commit 036bff6 occupations count:", len(data.get('occupations', [])))
print(json.dumps(data.get('occupations', [])[:5], indent=2))
