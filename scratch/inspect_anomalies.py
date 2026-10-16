import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'

# Check empty content in Location
loc_data = json.loads((FINAL_DIR / 'Svartulfr_Location.json').read_text(encoding='utf-8'))
loc_entries = loc_data.get('lexicon') or loc_data.get('entries') or []
for idx, e in enumerate(loc_entries):
    if not (e.get('content') or '').strip():
        print(f"Empty content in Location idx={idx}:")
        print(f"  name: {repr(e.get('name'))}")
        print(f"  keys: {e.get('keys')}")
        print(f"  comment: {repr(e.get('comment'))}")
        print(f"  all dict keys: {list(e.keys())}")
        print(f"  raw entry: {json.dumps(e, indent=2, ensure_ascii=False)}")

# Check the 1 NPC in Lorebook II
lb2_data = json.loads((FINAL_DIR / 'Svartulfr_Lorebook_II.json').read_text(encoding='utf-8'))
lb2_entries = lb2_data.get('lexicon') or lb2_data.get('entries') or []
for idx, e in enumerate(lb2_entries):
    if e.get('type') == 'npc':
        print(f"\nNPC in Lorebook II idx={idx}:")
        print(f"  name: {repr(e.get('name'))}")
        print(f"  keys: {e.get('keys')}")
        print(f"  content prefix: {repr(e.get('content')[:120])}")
        print(f"  avatar: {e.get('avatar')}")
        print(f"  regex: {e.get('avatar_activation_regex')}")
