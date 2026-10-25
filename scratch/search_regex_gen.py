import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chunk_dir = ROOT / 'scratch' / 'lorebook_chunks'

for f in chunk_dir.glob('*.js'):
    text = f.read_text(encoding='utf-8')
    # search for regex pattern generators or prefix
    if 'npc_prefix' in text:
        print(f"=== npc_prefix in {f.name} ===")
        for m in re.finditer(r'npc_prefix', text):
            pos = m.start()
            print(' '.join(text[max(0, pos-200):min(len(text), pos+300)].split()))

    if 'avatar_activation_regex' in text:
        for m in re.finditer(r'avatar_activation_regex\s*[:=]', text):
            pos = m.start()
            print(f"avatar_activation_regex assignment in {f.name}:")
            print(' '.join(text[max(0, pos-150):min(len(text), pos+300)].split()))
