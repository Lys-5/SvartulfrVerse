import json
import re
from pathlib import Path

ROOT = Path('e:/repository/SvartulfrVerse')
with open(ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_World_Scenario_SUCC_Welcome_Day.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def inspect_blocks(text, label):
    print(f"\n==================== {label} ====================")
    # Split by =>
    parts = re.split(r'(?=(?:^|\n)=>[A-Za-z0-9_]+:)', text)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        m = re.match(r'^=>([A-Za-z0-9_]+):\s*(.*)', part, flags=re.DOTALL)
        if not m:
            print(f"[UNTAGGED CONTENT]: {part[:100]}...")
            continue
        speaker = m.group(1)
        body = m.group(2).strip()
        quotes = re.findall(r'"([^"]*)"', body)
        # Check text outside quotes
        non_quotes = re.sub(r'"[^"]*"', '', body).strip()
        print(f"[{speaker}]: quotes_count={len(quotes)}, body_len={len(body)}")
        if speaker != 'Narrator':
            if len(quotes) == 0:
                print(f"  WARNING: Character {speaker} has NO quotes in body: {body[:100]}")
            else:
                for q in quotes:
                    print(f"  Spoken: \"{q[:60]}...\"")
        else:
            if len(quotes) > 0:
                print(f"  NOTE: Narrator has quotes: {quotes}")

inspect_blocks(data['premade_scenes'][0]['scene_text'], "Scene 0 (Alyssa POV)")
inspect_blocks(data['premade_scenes'][1]['scene_text'], "Scene 1 (Jasper POV)")
inspect_blocks(data['premade_scenes'][2]['scene_text'], "Scene 2 (Corale)")
