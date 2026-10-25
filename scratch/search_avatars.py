import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

target_names = {
    'Scarlett': 'Scarlett Rose',
    'Sierra': 'Sierra Cruz',
    'Russ': 'Russ Sinclair',
    'Stan': 'Stan Davies',
    'Jared': 'Jared Thompson',
    'Alyssa': 'Alyssa Douglas'
}

print("Searching for avatar URLs for each target in repo...")

# Check database/assets and lorebooks and scratch
for p in [
    ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json',
    ROOT / 'FINAL' / 'Svartulfr_NPC_Secondary.json',
    ROOT / 'scratch' / 'live_primary_lorebook.json',
    ROOT / 'lorebooks' / 'source' / 'Svartulfr_NPC_Primary.json',
    ROOT / 'database' / 'assets' / 'alyssa_avatar.md'
]:
    if not p.exists():
        continue
    txt = p.read_text(encoding='utf-8', errors='ignore')
    print(f"\n--- In {p.name} ---")
    if p.suffix == '.json':
        try:
            d = json.loads(txt)
            entries = d.get('lexicon', d.get('entries', []))
            for e in entries:
                name = e.get('name', '')
                avatar = e.get('avatar')
                for k, tn in target_names.items():
                    if k.lower() in name.lower() or any(k.lower() in str(x).lower() for x in e.get('keys', [])):
                        print(f"  [{tn}] name='{name}', avatar='{avatar}'")
        except Exception as ex:
            print(f"Error parsing json: {ex}")
    else:
        for line in txt.splitlines():
            if 'http' in line:
                print(f"  line: {line.strip()}")
