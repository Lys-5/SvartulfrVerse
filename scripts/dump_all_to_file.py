import json

p = json.load(open(r'C:\Users\mande\.gemini\antigravity\brain\0d89b0ab-f901-4d1c-afad-d3e640b70dd7\scratch\alyssa_persona_raw.json', encoding='utf-8'))

with open('scratch/all_outfits_raw.txt', 'w', encoding='utf-8') as f:
    for i, o in enumerate(p['outfits']):
        f.write(f"[{i+1}] {o['name'].upper()}\n")
        f.write(o['description'] + "\n\n")

print("Written to scratch/all_outfits_raw.txt")
