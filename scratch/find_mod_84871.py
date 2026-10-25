import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chunk_dir = ROOT / 'scratch' / 'lorebook_chunks'

for f in chunk_dir.glob('*.js'):
    text = f.read_text(encoding='utf-8')
    if '84871:' in text:
        print(f"=== Module 84871 defined in {f.name} ===")
        pos = text.find('84871:')
        print(text[pos:pos+1500])
