import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
scen = json.loads((FINAL / 'Svartulfr_Master_Scenario.json').read_text(encoding='utf-8'))

for idx, g in enumerate(scen['greetings'], 1):
    for m_i, m in enumerate(g.get('messages', [])):
        mc = m['content']
        for match in re.finditer(r'.{0,60}\{\{user\}\}.{0,60}', mc):
            s = match.group(0).replace('\n', ' ')
            if '"' in s:
                print(f"G{idx:02d} msg[{m_i}]: {s}")
