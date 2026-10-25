import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chunk_dir = ROOT / 'scratch' / 'lorebook_chunks'

for f in chunk_dir.glob('*.js'):
    text = f.read_text(encoding='utf-8')
    # search for first_name combined with regex or escape
    matches = [m.start() for m in re.finditer(r'first_name', text)]
    if matches:
        print(f"=== File {f.name}: {len(matches)} matches for first_name ===")
        for pos in matches:
            snippet = text[max(0, pos-200):min(len(text), pos+300)]
            print(f"Pos {pos}:")
            print(' '.join(snippet.split()))
            print("-" * 50)
