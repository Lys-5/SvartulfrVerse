import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
for p in (ROOT / 'scratch').glob('*.js'):
    content = p.read_text(encoding='utf-8', errors='ignore')
    if '62924' in content and p.name != '53145-79a5e9c927da31b2.js':
        print(f"Found 62924 in {p.name}")
        for m in re.finditer(r'62924', content):
            idx = m.start()
            print(content[max(0, idx - 100):min(len(content), idx + 200)])
            print("---")
