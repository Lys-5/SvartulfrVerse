import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chunk_dir = ROOT / 'scratch' / 'lorebook_chunks'

for f in chunk_dir.glob('*.js'):
    text = f.read_text(encoding='utf-8')
    if 'api/lorebooks' in text or 'lorebooks.update' in text:
        print(f"=== Matches in {f.name} ===")
        for m in re.finditer(r'(lorebooks\.update|/api/lorebooks/[^\"]+)', text):
            pos = m.start()
            print(' ', ' '.join(text[max(0, pos-100):min(len(text), pos+200)].split()))
