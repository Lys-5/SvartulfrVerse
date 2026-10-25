import json
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

sc = json.load(open('scratch/inspect_sc_live.json', encoding='utf-8'))
ch = json.load(open('scratch/inspect_ch_live.json', encoding='utf-8'))

for i, scene in enumerate(sc['premade_scenes']):
    print(f"\n=== SCENE {i} ({scene['id']}) ===")
    beats = [b for b in scene['scene_text'].split('=>') if b.strip()]
    for j, beat in enumerate(beats):
        lines = beat.strip().splitlines()
        speaker = lines[0].split(':')[0]
        quotes = re.findall(r'"([^"]*)"', beat)
        print(f"Beat {j:02d} [{speaker}]: {len(quotes)} quote(s)")
        for q in quotes:
            print(f"   Quote: \"{q[:70]}...\"")

print("\n=== MESSAGE #0 SWIPE ===")
msg0 = ch['messages'][0]['swipes'][0]['content']
beats = [b for b in msg0.split('=>') if b.strip()]
for j, beat in enumerate(beats):
    lines = beat.strip().splitlines()
    speaker = lines[0].split(':')[0]
    quotes = re.findall(r'"([^"]*)"', beat)
    print(f"Beat {j:02d} [{speaker}]: {len(quotes)} quote(s)")
    for q in quotes:
        print(f"   Quote: \"{q[:70]}...\"")
