import json, re
import sys
sys.path.append('.')
from scratch.build_camp_mystic_npcs import clean_text, COLLIDING_NAMES

COLLIDING_NAMES['jas'] = True
COLLIDING_NAMES['lys'] = True
COLLIDING_NAMES['mal'] = True

def build_location_entry(entry):
    raw_name = entry.get('name', '')
    clean_name = re.sub(r'^[\s\U00010000-\U0010ffff\u2600-\u27ff🚐🌙🌲🧺🪟🛋💻🎨🤸🏀🏊🏢🧪🖥🩺🩸🛡🌊🛶🔥🎣🛖\-\—]+\s*', '', raw_name).strip()
    clean_name = clean_text(clean_name)
    
    raw_content = entry.get('content', '')
    clean_content = clean_text(raw_content)
    
    raw_keys = entry.get('keys', [])
    clean_keys = []
    if clean_name not in clean_keys:
        clean_keys.append(clean_name)
        
    for k in raw_keys:
        k_clean = clean_text(k).strip()
        if not k_clean: continue
        if k_clean.lower() in COLLIDING_NAMES: continue
        if k_clean not in clean_keys:
            clean_keys.append(k_clean)
            
    entry['name'] = clean_name
    entry['type'] = 'location'
    entry['content'] = clean_content
    entry['keys'] = clean_keys
    return entry

live_loc = json.load(open('scratch/live_raw_location.json', encoding='utf-8'))['lexicon']
sample_indices = [188, 189, 192, 209, 224]

for idx in sample_indices:
    e = live_loc[idx]
    built = build_location_entry(e)
    print(f"=== LOCATION INDEX {idx}: {built['name']} ===")
    print("Type:", built['type'])
    print("Keys:", built['keys'])
    print("Content preview:")
    for l in built['content'].splitlines()[:5]:
        print(" ", l[:120])
    print()
