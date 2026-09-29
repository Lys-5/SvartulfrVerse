import json
import re
from datetime import datetime, timezone

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

with open('scratch/g2_canonical_list.json', 'r', encoding='utf-8') as f:
    g2_meta = json.load(f)

g2_ids = set(m['id'] for m in g2_meta)
chars = {c['id']: c for c in world_data.get('world_characters', []) if c['id'] in g2_ids}

# Epoca: 827-12-21T00:00:00Z
EP_TIMESTAMP = datetime(827, 12, 21, 0, 0, 0, tzinfo=timezone.utc).timestamp()

results = []
for cid, c in chars.items():
    dn = c.get('display_name')
    ls = c.get('long_summary') or ''
    s = c.get('summary') or ''
    text = ls + '\n' + s
    
    # Try finding age
    age_match = re.search(r'AGE:\s*([^;\]\n]+)', text, re.I)
    bday_match = re.search(r'BIRTH(?:DAY|DATE):\s*([^;\]\n]+)', text, re.I)
    
    existing_bd = c.get('birthdate')
    existing_st = c.get('start_timeline_position')
    
    results.append({
        'id': cid,
        'name': dn,
        'existing_bd': existing_bd,
        'existing_st': existing_st,
        'age_raw': age_match.group(1).strip() if age_match else None,
        'bday_raw': bday_match.group(1).strip() if bday_match else None,
        'text_sample': text[:300]
    })

print(f"Audited {len(results)} G2 characters.")
with open('scratch/g2_ages_audit.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, indent=2)
print("Saved to scratch/g2_ages_audit.json")
