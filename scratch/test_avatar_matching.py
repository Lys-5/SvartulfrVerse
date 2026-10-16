import json, re

following = json.load(open('ARCHIVIO/janitor_sources/janitor_following_canon_characters.json', encoding='utf-8')).get('characters', [])
favs = json.load(open('ARCHIVIO/janitor_sources/janitor_favorites_candidates.json', encoding='utf-8')).get('characters', [])

janitor_map = {}
for c in following + favs:
    nm = c.get('name', '').strip()
    av = c.get('avatar', '').strip()
    if nm and av:
        url = f'https://ella.janitorai.com/bot-avatars/{av}'
        janitor_map[nm.lower()] = url
        # also add without tags/brackets
        clean = re.sub(r'\[.*?\]|\(.*?\)|\|.*', '', nm).strip().lower()
        if clean:
            janitor_map[clean] = url
        # also first word if distinctive
        parts = clean.split()
        if len(parts) >= 2:
            first_last = f"{parts[0]} {parts[-1]}"
            janitor_map[first_last] = url

print(f"Total indexed Janitor name variations: {len(janitor_map)}")

matches = 0
for fname in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    data = json.load(open(fname, encoding='utf-8'))
    for e in data.get('entries', []):
        nm = e.get('name', '').strip().lower()
        av = e.get('avatar', '')
        if '98e2d06d' in av or not av:
            found = janitor_map.get(nm)
            if not found:
                clean_e = re.sub(r'\[.*?\]|\(.*?\)|\|.*', '', nm).strip().lower()
                found = janitor_map.get(clean_e)
            if not found:
                for k in e.get('keys', []):
                    k_clean = k.strip().lower()
                    if k_clean in janitor_map and len(k_clean) > 3:
                        found = janitor_map[k_clean]
                        break
            if found:
                matches += 1
                print(f"Match for {e.get('name')}: {found}")

print(f"\nTotal additional matches from Janitor: {matches}")
