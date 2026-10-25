import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

for name in ['Alyssa_Persona.json', 'Jasper_Persona.json']:
    p = ROOT / 'FINAL' / 'personas' / name
    d = json.loads(p.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    first_line = desc.split('\n')[0]
    m = re.match(r'^\s*(\[[^\]]*\])', desc, flags=re.DOTALL)
    bracket_lines = len(m.group(1).split('\n')) if m else 0
    age_m = re.search(r'AGE:[^;\]]+[;\]]', desc[:500])
    can_fork = d.get('can_fork')
    headers = re.findall(r'^([A-Z][A-Z0-9 &\'"/\(\)\-,]+):', desc, flags=re.M)
    em_dash_count = desc.count('—')
    asterisk_count = desc.count('*')
    print(f"\n{'='*20} {name} {'='*20}")
    print(f"  ID: {d.get('id') or d.get('persona_id')}")
    print(f"  Bracket lines: {bracket_lines} | Length of line 1: {len(first_line)}")
    print(f"  AGE match: {age_m.group(0) if age_m else 'NONE'}")
    print(f"  can_fork: {can_fork}")
    print(f"  em_dash: {em_dash_count} | asterisk: {asterisk_count}")
    print(f"  Headers ({len(headers)}): {headers[:8]}")
