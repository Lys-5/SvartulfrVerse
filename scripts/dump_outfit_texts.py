import json

p = json.load(open(r'C:\Users\mande\.gemini\antigravity\brain\0d89b0ab-f901-4d1c-afad-d3e640b70dd7\scratch\alyssa_persona_raw.json', encoding='utf-8'))

for o in p['outfits']:
    print(f"=== OUTFIT: {o['name']} ===")
    print(o['description'])
    print()
