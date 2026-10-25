import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
files = [ROOT / 'scratch' / '14685-a6f37bf36e7cf713.js', ROOT / 'scratch' / '53145-79a5e9c927da31b2.js']

for f in files:
    if f.exists():
        text = f.read_text(encoding='utf-8', errors='ignore')
        matches = [m.start() for m in re.finditer('prompt_assembly_id', text)]
        print(f"=== {f.name} ({len(matches)} matches) ===")
        for idx in matches[:5]:
            start = max(0, idx - 100)
            end = min(len(text), idx + 200)
            print("---")
            print(text[start:end])
