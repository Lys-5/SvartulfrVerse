import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
legacy_dir = ROOT / 'ARCHIVIO' / 'cards_legacy'

for f in sorted(legacy_dir.glob('*_card.json')):
    d = json.loads(f.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    first_line = desc.split('\n')[0]
    m = re.match(r'^\s*(\[[^\]]*\])', desc, flags=re.DOTALL)
    bracket_lines = len(m.group(1).split('\n')) if m else 0
    age_m = re.search(r'AGE:[^;\]]+[;\]]', desc[:500])
    headers = re.findall(r'^([A-Z][A-Z0-9 &\'"/\(\)\-,]+):', desc, flags=re.M)
    pers = d.get('personality', '')
    pers_bracket = pers.strip().startswith('[') and pers.strip().endswith(']')
    fields = ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']
    em_dashes = sum(d.get(k, '').count('—') for k in fields if isinstance(d.get(k), str))
    asterisks = sum(d.get(k, '').count('*') for k in fields if isinstance(d.get(k), str))
    print(f"\n{'='*20} {f.name} {'='*20}")
    print(f"  Bracket lines: {bracket_lines} | First line len: {len(first_line)}")
    print(f"  Current AGE match: {age_m.group(0) if age_m else 'NONE'}")
    print(f"  Headers: {headers}")
    print(f"  Personality is bracket: {pers_bracket} | len: {len(pers)}")
    print(f"  Personality preview: {pers[:100]}...")
    print(f"  Em-dashes: {em_dashes} | Asterisks: {asterisks}")
