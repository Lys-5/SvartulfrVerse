import json
import re
import sys
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

EP = datetime(827, 12, 21, 0, 0, 0, tzinfo=timezone.utc)

def date_to_hours(year, month, day, hour=0):
    dt = datetime(year, month, day, hour, 0, 0, tzinfo=timezone.utc)
    return int((dt - EP).total_seconds() // 3600)

def hours_to_date(h):
    dt = EP + timedelta(hours=h)
    return dt.strftime('%Y-%m-%d %H:%M')

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('exports/Svartulfr_Export.json', encoding='utf-8') as f:
    world = json.load(f)

with open('drive/claude_export/extracted/projects/projects/01a03cfa-cebb-74ef-be69-f24d0ae96ed0.json', encoding='utf-8') as f:
    claude_proj = json.load(f)
claude_docs = {d['filename']: d['content'] for d in claude_proj.get('docs', [])}

with open('drive/Svartulfr.md', encoding='utf-8', errors='ignore') as f:
    svart_md = f.read()

with open('drive/Modern Fantasy.md', encoding='utf-8', errors='ignore') as f:
    mf_md = f.read()

chars_by_id = {c['id']: c for c in world['world_characters']}

# Month map
months = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12,
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'sept': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

dossier = []

for item in g2_list:
    cid = item['id']
    name = item['name']
    c = chars_by_id[cid]
    
    ls = c.get('long_summary') or ''
    s = c.get('summary') or ''
    dd = c.get('display_description') or ''
    
    # Extract JED+ fields
    jed_m = re.search(r'\[NAME:[^\]]+\]', ls)
    jed_block = jed_m.group(0) if jed_m else ''
    
    species_m = re.search(r'SPECIES:\s*([^;\]\n]+)', jed_block, re.I)
    species = species_m.group(1).strip() if species_m else ''
    
    age_field_m = re.search(r'AGE:\s*([^;\]\n]+)', jed_block, re.I)
    age_field = age_field_m.group(1).strip() if age_field_m else ''
    
    bday_field_m = re.search(r'BIRTH(?:DAY|DATE):\s*([^;\]\n]+)', jed_block, re.I)
    bday_field = bday_field_m.group(1).strip() if bday_field_m else ''
    
    # Search for ages in all docs
    clean_name = name.split('(')[0].split('"')[0].strip()
    
    found_ages = []
    found_bdays = []
    
    # Search in card text
    for txt in [ls, s, dd]:
        m_ages = re.findall(r'(\b\d{1,4}\b)\s*(?:years old|-year-old|years of age)', txt, re.I)
        found_ages.extend(m_ages)
        m_born = re.findall(r'born\s+(?:in\s+)?(\d{3,4})', txt, re.I)
        if m_born:
            found_ages.extend([f"born_{y}" for y in m_born])
            
    # Search in claude docs
    for fname, content in claude_docs.items():
        if clean_name.lower() in content.lower():
            # lines mentioning clean_name
            for line in content.split('\n'):
                if clean_name.lower() in line.lower():
                    # check table: | Name | ... | Age | ...
                    parts = [p.strip() for p in line.split('|')]
                    for p in parts:
                        if re.match(r'^\d{1,4}$', p) and int(p) in range(14, 1500):
                            found_ages.append(p)
                    # check regex in line
                    m_a = re.findall(r'(?:age|età|anni)\s*[:=]?\s*(\d{1,4})', line, re.I)
                    found_ages.extend(m_a)
                    m_y = re.findall(r'(\d{1,4})\s*(?:anni|-year-old|years old)', line, re.I)
                    found_ages.extend(m_y)
                    m_b = re.findall(r'birth(?:day|date)\s*[:=]?\s*([A-Za-z]+\s+\d{1,2}(?:,\s*\d{4})?)', line, re.I)
                    found_bdays.extend(m_b)

    dossier.append({
        'id': cid,
        'name': name,
        'species': species,
        'current_birthdate': c.get('birthdate'),
        'current_start_timeline': c.get('start_timeline_position'),
        'current_is_global': c.get('is_global'),
        'current_final_instructions': c.get('final_instructions'),
        'age_field': age_field,
        'bday_field': bday_field,
        'found_ages': list(set(found_ages)),
        'found_bdays': list(set(found_bdays))
    })

with open('scratch/g2_dossier.json', 'w', encoding='utf-8') as f:
    json.dump(dossier, f, indent=2, ensure_ascii=False)

print(f"Master dossier built for {len(dossier)} characters.")
