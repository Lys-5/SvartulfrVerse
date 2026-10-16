import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
avatars = set()

for p in ROOT.rglob('*.json'):
    if any(skip in p.parts for skip in ['node_modules', '.git', '.gemini']):
        continue
    try:
        txt = p.read_text(encoding='utf-8')
        if 'imagedelivery.net' in txt:
            urls = re.findall(r'https://imagedelivery\.net/[^\s"\'\\]+', txt)
            for u in urls:
                avatars.add(u)
    except Exception:
        pass

print(f"Total unique imagedelivery URLs: {len(avatars)}")
for a in sorted(avatars)[:15]:
    print(" ", a)
