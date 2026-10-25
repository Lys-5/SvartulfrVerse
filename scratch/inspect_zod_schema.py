import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
text = (ROOT / 'scratch' / '14685-a6f37bf36e7cf713.js').read_text(encoding='utf-8', errors='ignore')
idx = text.find('prompt_assembly_id')
if idx != -1:
    print(text[max(0, idx - 600):min(len(text), idx + 800)])
