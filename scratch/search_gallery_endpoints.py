import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

for f in ROOT.glob('scratch/**/*.js'):
    text = f.read_text(encoding='utf-8', errors='ignore')
    if '/gallery' in text or 'api/gallery' in text or 'lorebooks/' in text and 'gallery' in text:
        matches = [m.start() for m in re.finditer(r'(/api/[^"\'`\s]*gallery[^"\'`\s]*)', text)]
        if matches:
            print(f"=== File {f.name} matches: ===")
            for pos in matches[:5]:
                print(' ', text[pos:pos+100])
        matches2 = [m.start() for m in re.finditer(r'(getLorebookGalleryImages|addLorebookGalleryImage)', text)]
        if matches2:
            print(f"=== File {f.name} function matches: ===")
            for pos in matches2:
                print(' ', ' '.join(text[max(0, pos-100):min(len(text), pos+300)].split()))
