import json
import re
from pathlib import Path

sc = json.load(open('scratch/inspect_sc_live.json', encoding='utf-8'))
ch = json.load(open('scratch/inspect_ch_live.json', encoding='utf-8'))

scenes = sc.get('premade_scenes', [])
print(f'Total premade scenes: {len(scenes)}')
for i, s in enumerate(scenes):
    text = s.get('scene_text', '')
    print(f"\n================ Scene {i}: {s.get('id')} ({s.get('name')}) ================")
    print(f"Length: {len(text)}")
    print(f"Em-dash ('—') count: {text.count('—')}")
    print(f"En-dash ('–') count: {text.count('–')}")
    print(f"Asterisk ('*') count: {text.count('*')}")
    print(f"ASCII double quote count: {text.count('\"')}")
    print(f"Curly left quote count: {text.count('“')}")
    print(f"Curly right quote count: {text.count('”')}")
    
    # Check quotes balance
    q_count = text.count('"')
    print(f"Quotes balanced (even count): {q_count % 2 == 0}")
    
    # Check beats
    beats = [b for b in text.split('=>') if b.strip()]
    print(f"Beats count: {len(beats)}")
    for j, b in enumerate(beats):
        lines = b.strip().split('\n')
        tag_line = lines[0]
        tag = tag_line.split(':')[0]
        has_dialogue = '"' in b
        # Find all quoted dialogue
        quotes = re.findall(r'"([^"]*)"', b)
        print(f"  Beat {j}: tag={tag}, quotes_count={len(quotes)}, has_dialogue={has_dialogue}")
        if tag == 'Narrator' and has_dialogue:
            print(f"    WARNING: Narrator has dialogue quotes! {quotes}")

msg0 = ch.get('messages', [])[0]
sw0 = msg0.get('swipes', [])[0]
content = sw0.get('content', '')
print(f"\n================ Message #0 Swipe ({sw0.get('id')}) ================")
print(f"Length: {len(content)}")
print(f"Em-dash ('—') count: {content.count('—')}")
print(f"En-dash ('–') count: {content.count('–')}")
print(f"Asterisk ('*') count: {content.count('*')}")
print(f"ASCII double quote count: {content.count('\"')}")
print(f"Curly left quote count: {content.count('“')}")
print(f"Curly right quote count: {content.count('”')}")
q_count = content.count('"')
print(f"Quotes balanced (even count): {q_count % 2 == 0}")

beats = [b for b in content.split('=>') if b.strip()]
print(f"Beats count: {len(beats)}")
for j, b in enumerate(beats):
    lines = b.strip().split('\n')
    tag_line = lines[0]
    tag = tag_line.split(':')[0]
    quotes = re.findall(r'"([^"]*)"', b)
    print(f"  Beat {j}: tag={tag}, quotes_count={len(quotes)}, has_dialogue={bool(quotes)}")
    if tag == 'Narrator' and quotes:
        print(f"    WARNING: Narrator has dialogue quotes! {quotes}")
