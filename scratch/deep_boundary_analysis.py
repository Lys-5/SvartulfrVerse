import json
import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


sc = json.load(open('scratch/inspect_sc_live.json', encoding='utf-8'))
ch = json.load(open('scratch/inspect_ch_live.json', encoding='utf-8'))

def analyze_text(label, text):
    print(f"\n==================== {label} ====================")
    print(f"Total length: {len(text)} chars, {len(text.splitlines())} lines")
    
    # 1. Dash checks
    em_dashes = text.count('—')
    en_dashes = text.count('–')
    horiz_bars = text.count('―')
    double_hyphens = text.count('--')
    print(f"Dashes: em-dash(—)={em_dashes}, en-dash(–)={en_dashes}, bar(―)={horiz_bars}, double-hyphen(--)={double_hyphens}")
    
    # 2. Asterisk checks
    asterisk_total = text.count('*')
    # Asterisks outside quotes
    in_quote = False
    asterisks_outside = 0
    asterisks_inside = 0
    for idx, char in enumerate(text):
        if char == '"':
            in_quote = not in_quote
        elif char == '*':
            if in_quote:
                asterisks_inside += 1
            else:
                asterisks_outside += 1
    print(f"Asterisks: total={asterisk_total}, outside_quotes={asterisks_outside}, inside_quotes={asterisks_inside}")
    
    # 3. Quote checks
    ascii_quotes = text.count('"')
    curly_left = text.count('“')
    curly_right = text.count('”')
    curly_low = text.count('„')
    single_curly_left = text.count('‘')
    single_curly_right = text.count('’')
    print(f"Quotes: ASCII double(\")={ascii_quotes}, curly double(“, ”)={curly_left, curly_right}, curly single(‘, ’)={single_curly_left, single_curly_right}")
    print(f"ASCII quotes parity (balanced): {ascii_quotes % 2 == 0}")
    
    # Check start of text
    starts_with_tag = text.strip().startswith('=>')
    print(f"Starts with '=>': {starts_with_tag}")
    
    # 4. Beat and dialogue analysis
    # Split text by `=>`
    raw_beats = text.split('=>')
    pre_text = raw_beats[0]
    if pre_text.strip():
        print(f"WARNING: Found text before first '=>' tag: {repr(pre_text.strip())}")
        
    beats = raw_beats[1:]
    print(f"Total beats: {len(beats)}")
    
    for b_idx, beat in enumerate(beats):
        lines = beat.strip().splitlines()
        first_line = lines[0]
        if ':' not in first_line:
            print(f"  Beat {b_idx} ERROR: No colon in tag line: {first_line}")
            continue
        speaker = first_line.split(':')[0].strip()
        body = '\n'.join(lines[1:]).strip() if len(lines) > 1 else ""
        rest_of_first_line = first_line.split(':', 1)[1].strip()
        
        # Check if first line has text after colon
        if rest_of_first_line:
            print(f"  Beat {b_idx} ({speaker}): has inline text on tag line: {repr(rest_of_first_line)}")
            
        full_beat_body = (rest_of_first_line + "\n" + body).strip()
        beat_quotes = full_beat_body.count('"')
        quotes_list = re.findall(r'"([^"]*)"', full_beat_body)
        
        # Check beat balance
        if beat_quotes % 2 != 0:
            print(f"  Beat {b_idx} ({speaker}) ERROR: Unbalanced quotes! count={beat_quotes}")
            
        # Check dialogue in narrator
        if speaker.lower() == 'narrator':
            if beat_quotes > 0:
                print(f"  Beat {b_idx} (Narrator) WARNING: Contains quotes: {quotes_list}")
        else:
            # Character speaker beat
            if beat_quotes == 0:
                print(f"  Beat {b_idx} ({speaker}) WARNING: Character has 0 dialogue quotes!")
                
        # Check for plain un-prefixed speaker patterns in beat body
        plain_speakers = re.findall(r'^(?!=>)([A-Z][a-zA-Z0-9_\' \-]+):\s*(?:\"|[A-Z])', full_beat_body, flags=re.MULTILINE)
        if plain_speakers:
            print(f"  Beat {b_idx} ({speaker}) ERROR: Plain un-prefixed speaker detected: {plain_speakers}")
            
        # Check if quotes contain newlines
        for q_idx, q in enumerate(quotes_list):
            if '\n' in q:
                print(f"  Beat {b_idx} ({speaker}) Quote {q_idx} contains newline.")
            if not q.strip():
                print(f"  Beat {b_idx} ({speaker}) Quote {q_idx} is EMPTY.")

for i, scene in enumerate(sc.get('premade_scenes', [])):
    analyze_text(f"Scene {i}: {scene.get('id')}", scene.get('scene_text', ''))

msg0 = ch.get('messages', [])[0]
sw0 = msg0.get('swipes', [])[0]
analyze_text(f"Message #0 Swipe: {sw0.get('id')}", sw0.get('content', ''))
