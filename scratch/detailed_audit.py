import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

print("=" * 60)
print("AUDIT 8 FINAL CARDS")
print("=" * 60)

final_cards = [
    'Edric_Douglas_card.json',
    'Erik_Douglas_card.json',
    'Jasper_Douglas_Bloodmoon_card.json',
    'Logan_Douglas_card.json',
    'Mackenzie_Sanchez_Rogers_card.json',
    'Malachia_Douglas_Bloodmoon_card.json',
    'Noah_Douglas_Bloodmoon_card.json',
    'Wulfnic_Bloodmoon_card.json'
]

for fname in final_cards:
    p = ROOT / 'FINAL' / fname
    d = json.loads(p.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    first_line = desc.split('\n')[0] if desc else ''
    first_bracket = ''
    m = re.match(r'^\s*(\[[^\]]*\])', desc, flags=re.DOTALL)
    bracket_lines = 0
    if m:
        first_bracket = m.group(1)
        bracket_lines = len(first_bracket.split('\n'))
    elif desc.strip().startswith('['):
        # find matching bracket
        end_idx = desc.find(']')
        if end_idx != -1:
            first_bracket = desc[:end_idx+1]
            bracket_lines = len(first_bracket.split('\n'))

    # Check age in first_bracket or desc
    age_match = re.search(r'AGE:\s*([^;\]\n]+)', first_bracket if first_bracket else desc)
    age_str = age_match.group(0) if age_match else 'NO AGE FOUND'

    # Check headers
    headers = re.findall(r'^([A-Z][A-Z0-9 &\'"/\(\)\-,]+):', desc, flags=re.M)
    
    # Check personality
    pers = d.get('personality', '')
    pers_bracket = pers.strip().startswith('[') and pers.strip().endswith(']')
    
    # Check asterisks / em-dash in desc, personality, first_mes, mes_example, post_history_instructions
    fields_to_check = ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']
    em_dash_count = sum(d.get(f, '').count('—') for f in fields_to_check if isinstance(d.get(f), str))
    asterisk_count = sum(d.get(f, '').count('*') for f in fields_to_check if isinstance(d.get(f), str))
    phi = d.get('post_history_instructions', '')
    has_format_clause = 'Format discipline' in phi or 'dialogue in quotes' in phi

    print(f"\n--- {fname} ---")
    print(f"  Bracket lines: {bracket_lines} | First line len: {len(first_line)}")
    print(f"  Age str: {age_str}")
    print(f"  Headers ({len(headers)}): {headers[:6]}...")
    print(f"  Personality is bracket: {pers_bracket} | len: {len(pers)} | preview: {pers[:60]}...")
    print(f"  Em-dash: {em_dash_count} | Asterisk: {asterisk_count} | Has format clause: {has_format_clause}")
    if 'Noah' in fname:
        print(f"  [Noah initial bracket preview]:\n{first_bracket[:300]}...")
    if 'Malachia' in fname:
        print(f"  Malachia mes_example asterisk count: {d.get('mes_example', '').count('*')}")
        if '*' in d.get('mes_example', ''):
            print(f"  Malachia mes_example with asterisks:\n{d.get('mes_example')}")

print("\n" + "=" * 60)
print("AUDIT 3 PERSONAS")
print("=" * 60)

for pf in ['Alyssa_Persona.json', 'Echo_Persona.json', 'Jasper_Persona.json']:
    p = ROOT / 'FINAL' / 'personas' / pf
    d = json.loads(p.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    headers = re.findall(r'^([A-Z][A-Z0-9 &\'"/\(\)\-,]+):', desc, flags=re.M)
    m = re.match(r'^\s*(\[[^\]]*\])', desc, flags=re.DOTALL)
    bracket_lines = len(m.group(1).split('\n')) if m else (len(desc.split(']')[0].split('\n')) if desc.startswith('[') else 0)
    age_match = re.search(r'AGE:\s*([^;\]\n]+)', desc[:500])
    age_str = age_match.group(0) if age_match else 'NO AGE'
    em_dash_count = desc.count('—')
    asterisk_count = desc.count('*')
    print(f"\n--- {pf} (id: {d.get('id') or d.get('persona_id')}) ---")
    print(f"  Bracket lines: {bracket_lines} | Age: {age_str} | can_fork: {d.get('can_fork')}")
    print(f"  Headers: {headers}")
    print(f"  Em-dash: {em_dash_count} | Asterisk: {asterisk_count}")

print("\n" + "=" * 60)
print("AUDIT 6 LEGACY CARDS")
print("=" * 60)

for lf in sorted((ROOT / 'ARCHIVIO' / 'cards_legacy').glob('*_card.json')):
    d = json.loads(lf.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    headers = re.findall(r'^([A-Z][A-Z0-9 &\'"/\(\)\-,]+):', desc, flags=re.M)
    m = re.match(r'^\s*(\[[^\]]*\])', desc, flags=re.DOTALL)
    bracket_lines = len(m.group(1).split('\n')) if m else 0
    age_match = re.search(r'AGE:\s*([^;\]\n]+)', desc[:500])
    age_str = age_match.group(0) if age_match else 'NO AGE'
    pers = d.get('personality', '')
    pers_bracket = pers.strip().startswith('[') and pers.strip().endswith(']')
    fields_to_check = ['description', 'personality', 'first_mes', 'mes_example', 'post_history_instructions']
    em_dash_count = sum(d.get(f, '').count('—') for f in fields_to_check if isinstance(d.get(f), str))
    asterisk_count = sum(d.get(f, '').count('*') for f in fields_to_check if isinstance(d.get(f), str))
    print(f"\n--- {lf.name} ---")
    print(f"  Bracket lines: {bracket_lines} | Age: {age_str}")
    print(f"  Headers: {headers}")
    print(f"  Personality is bracket: {pers_bracket} | preview: {pers[:60]}...")
    print(f"  Em-dash: {em_dash_count} | Asterisk: {asterisk_count}")
