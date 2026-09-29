import json
import re
from datetime import datetime, timezone, timedelta

EP = datetime(827, 12, 21, 0, 0, 0, tzinfo=timezone.utc)

def dt_to_hours(year, month, day, hour=0):
    dt = datetime(year, month, day, hour, 0, 0, tzinfo=timezone.utc)
    return int((dt - EP).total_seconds() // 3600)

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('exports/Svartulfr_Export.json', encoding='utf-8') as f:
    world = json.load(f)

chars_by_id = {c['id']: c for c in world['world_characters']}

# Also load drive docs
with open('drive/Svartulfr.md', encoding='utf-8', errors='ignore') as f:
    svart_md = f.read()

with open('drive/Modern Fantasy.md', encoding='utf-8', errors='ignore') as f:
    mf_md = f.read()

combined_drive = svart_md + "\n" + mf_md

cards_report = []

for item in g2_list:
    cid = item['id']
    name = item['name']
    c = chars_by_id[cid]
    
    ls = c.get('long_summary') or ''
    s = c.get('summary') or ''
    dd = c.get('display_description') or ''
    
    # Check JED block in ls
    m_jed = re.search(r'\[NAME:[^\]]+\]', ls)
    jed_block = m_jed.group(0) if m_jed else ''
    
    # Check fields in jed_block
    age_m = re.search(r'AGE:\s*([^;\]\n]+)', jed_block, re.I)
    bday_m = re.search(r'BIRTH(?:DAY|DATE):\s*([^;\]\n]+)', jed_block, re.I)
    species_m = re.search(r'SPECIES:\s*([^;\]\n]+)', jed_block, re.I)
    
    # Look for drive mentions of [NAME: <name>...
    drive_m = re.findall(rf'\[NAME:[^\]]*{re.escape(name.split()[0])}[^\]]*\]', combined_drive, re.I)
    
    # Look for any text mentioning age in ls, s, dd
    age_mentions = re.findall(r'(\b\d{1,3}\b\s*(?:years old|-year-old|yo\b))', ls + " " + s + " " + dd, re.I)
    
    cards_report.append({
        'id': cid,
        'name': name,
        'species': species_m.group(1).strip() if species_m else '',
        'age_field': age_m.group(1).strip() if age_m else '',
        'bday_field': bday_m.group(1).strip() if bday_m else '',
        'birthdate': c.get('birthdate'),
        'start_timeline': c.get('start_timeline_position'),
        'is_global': c.get('is_global'),
        'has_final_instructions': bool(c.get('final_instructions')),
        'outfits_count': len(c.get('outfits') or []),
        'attitudes_count': len(c.get('attitudes') or []),
        'speech_count': len(c.get('speech_examples') or []),
        'age_mentions': list(set(age_mentions))
    })

with open('scratch/g2_full_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(cards_report, f, indent=2, ensure_ascii=False)

print(f"Audited {len(cards_report)} G2 cards.")
