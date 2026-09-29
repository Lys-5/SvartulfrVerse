import os
import re
import json
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
chars_by_id = {c['id']: c for c in world['world_characters']}

doc_dir = 'docs/claude_project_docs'
docs = {}
for fname in os.listdir(doc_dir):
    with open(os.path.join(doc_dir, fname), encoding='utf-8', errors='ignore') as f:
        docs[fname] = f.read()

months_map = {
    'gennaio': 1, 'febbraio': 2, 'marzo': 3, 'aprile': 4, 'maggio': 5, 'giugno': 6,
    'luglio': 7, 'agosto': 8, 'settembre': 9, 'ottobre': 10, 'novembre': 11, 'dicembre': 12,
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

results = {}

for item in g2_list:
    name = item['name']
    cid = item['id']
    c = chars_by_id[cid]
    
    current_bd = c.get('birthdate')
    current_st = c.get('start_timeline_position')
    
    found_dates = []
    found_hours = []
    found_notes = []
    
    clean_name = name.split('(')[0].split('"')[0].strip()
    
    for fname, content in docs.items():
        if clean_name.lower() in content.lower():
            # Search for patterns like:
            # "Birthdate: 10044480"
            # "Birthdate 15 aprile 1979"
            # "nato il 3 novembre 2002"
            # "Start Position = birthdate = 10..."
            lines = content.split('\n')
            for line in lines:
                if any(w in line.lower() for w in ['birthdate', 'start position', 'timeline', 'nato', 'nata', 'born', 'età anagrafica', 'anni']):
                    # Check for direct hour number
                    m_hr = re.findall(r'(?:birthdate|start position|start_timeline_position)\D{0,15}(\d{7,8})', line, re.I)
                    for hr in m_hr:
                        found_hours.append((int(hr), f"{fname}: {line.strip()}"))
                    
                    # Check for date pattern in Italian: "15 aprile 1979" or "3 novembre 2002"
                    m_d_it = re.findall(r'(\d{1,2})\s+(gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|novembre|dicembre)\s+(\d{3,4})', line, re.I)
                    for day, mname, yr in m_d_it:
                        mo = months_map[mname.lower()]
                        hr = date_to_hours(int(yr), mo, int(day))
                        found_dates.append((f"{yr}-{mo:02d}-{int(day):02d}", hr, f"{fname}: {line.strip()}"))
                        
                    # Check for date pattern in English: "April 15, 1979" or "August 8, 2000"
                    m_d_en = re.findall(r'(january|february|march|april|may|june|july|august|september|october|november|december)\s+(\d{1,2})(?:st|nd|rd|th)?(?:,?\s+(\d{3,4}))?', line, re.I)
                    for mname, day, yr in m_d_en:
                        mo = months_map[mname.lower()]
                        if yr:
                            hr = date_to_hours(int(yr), mo, int(day))
                            found_dates.append((f"{yr}-{mo:02d}-{int(day):02d}", hr, f"{fname}: {line.strip()}"))
                        else:
                            found_dates.append((f"--{mo:02d}-{int(day):02d}", None, f"{fname}: {line.strip()}"))

    results[name] = {
        'id': cid,
        'current_bd': current_bd,
        'current_st': current_st,
        'found_hours': found_hours,
        'found_dates': found_dates
    }

with open('scratch/g2_dates_scraped.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"Scraped date data for {len(results)} G2 characters.")
