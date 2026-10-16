import pathlib
import json
import re

root = pathlib.Path('.')
for fname in [
    'Elizabeth_Duskwood_card.json',
    'Jared_Thompson_card.json',
    'Kaladin_Nargathon_card.json',
    'Mackenzie_Sanchez_Rogers_card.json',
    'Magnus_Douglas_III_card.json',
    'Zeera_Darkfire_card.json'
]:
    p = root / 'FINAL' / fname
    txt = p.read_text(encoding='utf-8')
    for m in re.finditer(r'(.{0,40}\{\{age\}\}.{0,40})', txt):
        print(f"{fname}: ...{m.group(1)}...")
