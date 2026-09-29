import json
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('exports/Svartulfr_Export.json', encoding='utf-8') as f:
    world = json.load(f)

chars_by_id = {c['id']: c for c in world['world_characters']}

extracted_chrono = {}

for item in g2_list:
    cid = item['id']
    name = item['name']
    c = chars_by_id[cid]
    
    ls = c.get('long_summary') or ''
    s = c.get('summary') or ''
    dd = c.get('display_description') or ''
    
    # Extract BACKSTORY block
    m_bs = re.search(r'BACKSTORY:\s*(.*?)(?=\n[A-Z\s&]+:|$)', ls, re.DOTALL)
    bs = m_bs.group(1).strip() if m_bs else ''
    
    # Extract JED+ block
    m_jed = re.search(r'\[NAME:[^\]]+\]', ls, re.DOTALL)
    jed = m_jed.group(0).strip() if m_jed else ''
    
    # Find years (4 digits like 1484, 1846, 1901, 1990, 2000, etc.)
    years = re.findall(r'\b(1[0-9]{3}|200[0-9]|201[0-9]|202[0-4])\b', f"{jed}\n{bs}\n{s}\n{dd}")
    # filter out common non-year numbers like 193cm, 208cm etc
    valid_years = [y for y in set(years) if not any(f"{y}cm" in ls for _ in [1])]
    
    # Find ages like "35 years old", "in his twenties", "mid-thirties", etc.
    age_descs = re.findall(r'(\b\d{1,3}\b\s*(?:years old|-year-old|years of age))', f"{jed}\n{bs}\n{s}\n{dd}", re.I)
    approx_ages = re.findall(r'((?:early|mid|late)\s*(?:twenties|thirties|forties|fifties|sixties|seventies|eighties|nineties)|\bcentury-old\b)', f"{jed}\n{bs}\n{s}\n{dd}", re.I)
    
    # Find explicit birthday in jed
    bday_m = re.search(r'BIRTH(?:DAY|DATE):\s*([^;\]\n]+)', jed, re.I)
    bday = bday_m.group(1).strip() if bday_m else None
    
    # Find species in jed
    sp_m = re.search(r'SPECIES:\s*([^;\]\n]+)', jed, re.I)
    species = sp_m.group(1).strip() if sp_m else ''

    extracted_chrono[name] = {
        'id': cid,
        'species': species,
        'current_bd': c.get('birthdate'),
        'bday_in_jed': bday,
        'valid_years': valid_years,
        'age_descs': list(set(age_descs)),
        'approx_ages': list(set(approx_ages)),
        'bs_snippet': bs[:250].replace('\n', ' ')
    }

with open('scratch/g2_chrono_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(extracted_chrono, f, indent=2, ensure_ascii=False)

for name, info in extracted_chrono.items():
    print(f"=== {name} ({info['species'][:20]}) ===")
    print(f"  bday_in_jed: {info['bday_in_jed']} | years: {info['valid_years']} | age_descs: {info['age_descs']} | approx: {info['approx_ages']}")
    print(f"  snippet: {info['bs_snippet'][:120]}")
