import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
text = (ROOT / 'scratch' / '53145-79a5e9c927da31b2.js').read_text(encoding='utf-8', errors='ignore')
idx = text.find('prompt_assembly_id')
if idx != -1:
    print(text[max(0, idx - 600):min(len(text), idx + 1000)])
