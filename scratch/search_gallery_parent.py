import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chunk_dir = ROOT / 'scratch' / 'lorebook_chunks'

for f in chunk_dir.glob('*.js'):
    text = f.read_text(encoding='utf-8')
    matches = [m.start() for m in re.finditer(r'gallery', text)]
    if len(matches) > 0 and f.name != '66353-44918b7fd11ff8ae.js':
        print(f"=== File {f.name}: {len(matches)} matches for gallery ===")
        for pos in matches[:5]:
            snippet = text[max(0, pos-150):min(len(text), pos+300)]
            print(f"Pos {pos}:")
            print(' '.join(snippet.split()))
            print("-" * 50)
