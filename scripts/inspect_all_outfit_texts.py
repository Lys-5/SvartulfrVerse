import json

p = json.load(open(r'C:\Users\mande\.gemini\antigravity\brain\0d89b0ab-f901-4d1c-afad-d3e640b70dd7\scratch\alyssa_persona_raw.json', encoding='utf-8'))
c = json.load(open('scratch/alyssa_world_card_live.json', encoding='utf-8'))

p_outfits = {o['name'].lower(): o for o in p['outfits']}
c_outfits = {o['name'].lower(): o for o in c['outfits']}

all_names = list(p_outfits.keys())

for name in all_names:
    po = p_outfits[name]
    co = c_outfits.get(name)
    print(f"==================================================")
    print(f"OUTFIT: {name.upper()}")
    print(f"Persona image_url: {po.get('image_url')}")
    print(f"Card avatar:       {co.get('avatar') if co else 'MISSING IN CARD'}")
    if co:
        print("\n--- Persona Desc (first 150 chars) ---")
        print(po.get('description', '')[:150])
        print("\n--- Card Desc (first 150 chars) ---")
        print(co.get('description', '')[:150])
    else:
        print("\n--- Persona Desc (FULL) ---")
        print(po.get('description', ''))
