import json
import re

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('drive/Svartulfr.md', encoding='utf-8', errors='ignore') as f:
    svart_md = f.read()

with open('drive/Modern Fantasy.md', encoding='utf-8', errors='ignore') as f:
    mf_md = f.read()

combined_docs = svart_md + "\n" + mf_md

found_data = {}

for item in g2_list:
    cid = item['id']
    name = item['name']
    
    # Try searching for [NAME: <name>... or similar
    # Clean name for search
    clean_name = name.split('"')[0].strip()
    
    # Search patterns
    patterns = [
        rf'\[NAME:\s*{re.escape(name)}[^\]]*\]',
        rf'\[NAME:\s*{re.escape(clean_name)}[^\]]*\]',
        rf'{re.escape(name)}[^\n]*?AGE:\s*([^;\n\]]+)',
        rf'{re.escape(clean_name)}[^\n]*?AGE:\s*([^;\n\]]+)'
    ]
    
    match_card = None
    # Let's search for blocks starting with [NAME: ...name... ]
    blocks = re.findall(r'(\[NAME:[^\]]+\])', combined_docs, re.IGNORECASE)
    for b in blocks:
        if clean_name.lower() in b.lower():
            match_card = b
            break
            
    found_data[cid] = {
        'name': name,
        'matched_block': match_card
    }

print("Inspection of found blocks:")
count_found = 0
for cid, info in found_data.items():
    b = info['matched_block']
    if b:
        count_found += 1
        # extract age and bday
        age_m = re.search(r'AGE:\s*([^;\]\n]+)', b, re.I)
        bday_m = re.search(r'BIRTH(?:DAY|DATE):\s*([^;\]\n]+)', b, re.I)
        species_m = re.search(r'SPECIES:\s*([^;\]\n]+)', b, re.I)
        a_str = age_m.group(1).strip() if age_m else 'N/A'
        bd_str = bday_m.group(1).strip() if bday_m else 'N/A'
        sp_str = species_m.group(1).strip() if species_m else 'N/A'
        print(f"{info['name']:30s} | AGE: {a_str:20s} | BDAY: {bd_str:25s} | {sp_str[:25]}")
    else:
        print(f"{info['name']:30s} | NOT FOUND IN [NAME:...]")

print(f"\nTotal matched blocks: {count_found} / {len(g2_list)}")
