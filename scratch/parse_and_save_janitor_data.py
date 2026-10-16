import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
DEST_DIR = ROOT / 'ARCHIVIO' / 'janitor_sources'
DEST_DIR.mkdir(parents=True, exist_ok=True)
LB_DIR = DEST_DIR / 'lorebooks'
LB_DIR.mkdir(parents=True, exist_ok=True)
SCRIPTS_DIR = DEST_DIR / 'scripts'
SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)

STEP_BASE = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\847025c7-071c-493a-9975-73b0c58cc7b4\.system_generated\steps')

def load_step_output(filepath):
    print(f"Loading {filepath}...")
    content = filepath.read_text(encoding='utf-8')
    match = re.search(r'```json\s*\n(.*?)\n```', content, re.DOTALL)
    raw = match.group(1) if match else content
    return json.loads(raw)

# 1. Target 2: Old Douglas Family Sheet (step 138)
step_138 = STEP_BASE / '138' / 'output.txt'
if step_138.exists():
    data_138 = load_step_output(step_138)
    out_138 = DEST_DIR / 'janitor_douglas_family_historical.json'
    out_138.write_text(json.dumps(data_138, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Saved Douglas Family sheet to {out_138} ({len(json.dumps(data_138))} bytes)")

# 2. Target 3: Following Characters (step 144)
step_144 = STEP_BASE / '144' / 'output.txt'
if step_144.exists():
    data_144 = load_step_output(step_144)
    out_144 = DEST_DIR / 'janitor_following_canon_characters.json'
    out_144.write_text(json.dumps(data_144, indent=2, ensure_ascii=False), encoding='utf-8')
    chars_count = len(data_144.get('characters', []))
    print(f"Saved Following Characters to {out_144} (total: {data_144.get('total')}, items: {chars_count})")

# 3. Target 4: Favorites Characters (step 141)
step_141 = STEP_BASE / '141' / 'output.txt'
if step_141.exists():
    data_141 = load_step_output(step_141)
    out_141 = DEST_DIR / 'janitor_favorites_candidates.json'
    out_141.write_text(json.dumps(data_141, indent=2, ensure_ascii=False), encoding='utf-8')
    fav_count = len(data_141.get('characters', []))
    print(f"Saved Favorites Characters to {out_141} (total: {data_141.get('total')}, items: {fav_count})")

# 4. Target 1: Lorebooks (steps 147, 150, 153)
all_items = []
for step_num in ['147', '150', '153']:
    p = STEP_BASE / step_num / 'output.txt'
    if p.exists():
        batch_data = load_step_output(p)
        lbs = batch_data.get('lorebooks', [])
        all_items.extend(lbs)

print(f"Total lorebook/script items loaded: {len(all_items)}")

# Save consolidated all_14
out_lbs = DEST_DIR / 'janitor_lorebooks_all_14.json'
out_lbs.write_text(json.dumps(all_items, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"Saved consolidated lorebooks to {out_lbs} ({len(all_items)} items)")

# Save individual items in lorebooks directory
for i, item in enumerate(all_items):
    raw_title = item.get('title') or item.get('name') or f"item_{i+1}"
    clean_title = raw_title.replace('\ufffd', 'u').replace('ú', 'u').replace('Ú', 'U')
    safe_title = re.sub(r'[^\w\-_\. ]', '_', clean_title).strip()
    safe_title = re.sub(r'_+', '_', safe_title).replace(' ', '_')
    item_type = item.get('type')
    
    # Save full JSON
    file_name = f"{i+1:02d}_{safe_title}.json"
    dest_path = LB_DIR / file_name
    dest_path.write_text(json.dumps(item, indent=2, ensure_ascii=False), encoding='utf-8')
    
    # If it's a script with raw_code, also save the .js file
    if item.get('raw_code'):
        js_path = SCRIPTS_DIR / f"{i+1:02d}_{safe_title}.js"
        js_path.write_text(item['raw_code'], encoding='utf-8')
        print(f"  [{i+1:02d}] Script: {raw_title} -> {file_name} and {js_path.name} ({len(item['raw_code'])} chars)")
    else:
        entries = item.get('entries', [])
        e_count = len(entries) if isinstance(entries, list) else 0
        print(f"  [{i+1:02d}] Lorebook: {raw_title} -> {file_name} ({e_count} entries)")

print("All Janitor sources parsed and persisted successfully!")
