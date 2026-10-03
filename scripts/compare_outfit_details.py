import json

p = json.load(open(r'C:\Users\mande\.gemini\antigravity\brain\0d89b0ab-f901-4d1c-afad-d3e640b70dd7\scratch\alyssa_persona_raw.json', encoding='utf-8'))
c = json.load(open('scratch/alyssa_world_card_live.json', encoding='utf-8'))

print("=== PERSONA OUTFITS ===")
for o in p.get('outfits', []):
    print(f"Name: {o.get('name'):22s} | ID: {o.get('id'):26s} | img: {o.get('image_url')}")

print("\n=== CARD OUTFITS ===")
for o in c.get('outfits', []):
    print(f"Name: {o.get('name'):22s} | ID: {o.get('id'):26s} | av:  {o.get('avatar')}")
