import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chunk_dir = ROOT / 'scratch' / 'lorebook_chunks'

for f in chunk_dir.glob('*.js'):
    text = f.read_text(encoding='utf-8')
    if 'auto-generate from NPC info' in text or 'Provide NPC details to automatically generate' in text:
        print(f"=== Found in {f.name} ===")
        # Find where avatar_activation_regex is generated
        matches = [m.start() for m in re.finditer(r'avatar_activation_regex', text)]
        for pos in matches:
            snippet = text[max(0, pos-200):min(len(text), pos+300)]
            print(f"Match at {pos}:")
            print(' '.join(snippet.split()))
            print("-" * 50)
