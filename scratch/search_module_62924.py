import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
text = (ROOT / 'scratch' / '53145-79a5e9c927da31b2.js').read_text(encoding='utf-8', errors='ignore')
matches = [m.start() for m in re.finditer(r'62924', text)]
print("Matches in 53145:", len(matches))
for idx in matches:
    print(text[max(0, idx - 100):min(len(text), idx + 200)])
    print("---")
