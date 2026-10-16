import json
import pathlib
import re

txt = pathlib.Path(r'C:\Users\mande\.gemini\antigravity\brain\03c97466-35b1-423f-aa36-b4ce213b0a4b\.system_generated\steps\2153\content.md').read_text(encoding='utf-8')
raw_tags = re.findall(r'<p><strong>(.*?)</strong>', txt)

clean_tags = []
for t in raw_tags:
    # remove HTML entities and emojis
    # strip characters that are emoji or symbols
    c = re.sub(r'[\U00010000-\U0010ffff]', '', t)
    c = re.sub(r'[\u2000-\u3300]', '', c)
    c = c.replace('🏳️‍⚧️', '').replace('🏳️‍🌈', '').replace('❤️', '').replace('⚔️', '').replace('⛏️', '').strip()
    c = re.sub(r'\s+', ' ', c).strip()
    if c and c not in clean_tags:
        clean_tags.append(c)

pathlib.Path('scratch/wyvern_clean_tags.json').write_text(json.dumps(clean_tags, indent=2), encoding='utf-8')
print(f"Extracted {len(clean_tags)} clean tags.")
