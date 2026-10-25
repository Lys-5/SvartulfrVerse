import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chunk_dir = ROOT / 'scratch' / 'lorebook_chunks'

for f in chunk_dir.glob('*.js'):
    text = f.read_text(encoding='utf-8')
    if 'getLorebookGalleryImages' in text:
        print(f"=== getLorebookGalleryImages in {f.name} ===")
        for m in re.finditer(r'getLorebookGalleryImages', text):
            pos = m.start()
            print(' '.join(text[max(0, pos-150):min(len(text), pos+400)].split()))
