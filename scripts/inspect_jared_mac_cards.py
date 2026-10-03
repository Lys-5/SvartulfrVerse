import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for c in d.get('world_characters', []):
    cid = c.get('id')
    if cid in ['_BzKwAkgpPfbVkBzbDaEth', '_YY8VbpgzYk4dfFAL78rM3']:
        print(f"\n==========================================")
        print(f"Character: {c.get('display_name')} (ID: {cid})")
        print(f"Summary: {c.get('summary')}")
        print(f"Birthdate: {c.get('birthdate')}")
        print(f"Start timeline pos: {c.get('start_timeline_position')}")
        print(f"Long Summary snippet:\n{c.get('long_summary', '')[:500]}...\n")
        outfits = c.get('appearance_outfits', [])
        print(f"Appearance Outfits: {len(outfits)}")
        for o in outfits:
            print(f"  - Outfit: {o.get('name')}")
