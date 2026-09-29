import json
import re

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('exports/Svartulfr_Export.json', encoding='utf-8') as f:
    world = json.load(f)

with open('drive/Svartulfr.md', encoding='utf-8', errors='ignore') as f:
    svart_md = f.read()

with open('drive/Modern Fantasy.md', encoding='utf-8', errors='ignore') as f:
    mf_md = f.read()

chars_by_id = {c['id']: c for c in world['world_characters']}

results = []
for item in g2_list:
    cid = item['id']
    name = item['name']
    c = chars_by_id[cid]
    
    ls = c.get('long_summary') or ''
    s = c.get('summary') or ''
    dd = c.get('display_description') or ''
    
    bd = c.get('birthdate')
    st = c.get('start_timeline_position')
    
    bday_match = re.search(r'BIRTH(?:DAY|DATE):\s*([^;\n\]]+)', ls, re.I)
    bday = bday_match.group(1).strip() if bday_match else None
    
    age_hints = []
    for txt in [dd, s, ls[:1500]]:
        m = re.findall(r'(\d{1,4}(?:st|nd|rd|th)?\s*(?:year[s]?(?:\s*old)?|-year-old|years of age|\bcentury\b))', txt, re.I)
        if m: age_hints.extend(m)
        m2 = re.findall(r'born\s+(?:in\s+)?(\d{3,4}|[A-Za-z]+\s+\d{1,2}(?:,\s*\d{4})?)', txt, re.I)
        if m2: age_hints.extend(['born ' + x for x in m2])
        m3 = re.findall(r'AGE:\s*(\d+)', txt, re.I)
        if m3: age_hints.extend(['AGE: ' + x for x in m3])
        
    # Search in drive docs for name and age
    # extract first occurrence in svart_md and mf_md
    drive_hints = []
    name_pat = re.escape(name)
    m_svart = re.findall(rf'{name_pat}[^\.\n]*?(?:age|years old|born|\d{{2,4}})[^\.\n]*', svart_md, re.I)
    if m_svart:
        drive_hints.extend([x.strip() for x in m_svart[:2]])
    m_mf = re.findall(rf'{name_pat}[^\.\n]*?(?:age|years old|born|\d{{2,4}})[^\.\n]*', mf_md, re.I)
    if m_mf:
        drive_hints.extend([x.strip() for x in m_mf[:2]])

    results.append({
        'id': cid,
        'name': name,
        'birthdate': bd,
        'start_timeline': st,
        'bday_in_card': bday,
        'age_hints': list(set(age_hints)),
        'drive_hints': drive_hints[:2]
    })

print(f"Total G2: {len(results)}")
with_dates = [r for r in results if r['birthdate'] is not None]
print(f"Already have birthdate: {len(with_dates)}")
without_dates = [r for r in results if r['birthdate'] is None]
print(f"Need birthdate: {len(without_dates)}")

with open('scratch/g2_extracted_hints.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

for r in without_dates[:30]:
    print(f"{r['name']:30s} | bday={str(r['bday_in_card']):20s} | hints={str(r['age_hints'])} | drive={str(r['drive_hints'])[:40]}")
