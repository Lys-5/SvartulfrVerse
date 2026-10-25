import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

for lb_path in (ROOT / 'FINAL').glob('*.json'):
    if not lb_path.name.startswith('Svartulfr_'):
        continue
    txt = lb_path.read_text(encoding='utf-8')
    for pat in ['1005', '823 AD', '823 d.C.', 'pre-827', '827 AD', '827 d.C.', '864', '848', '849', '819']:
        matches = [m.start() for m in re.finditer(re.escape(pat), txt, re.I)]
        if matches:
            print(f"{lb_path.name}: found '{pat}' {len(matches)} times")
            for idx in matches[:5]:
                snippet = txt[max(0, idx-50):min(len(txt), idx+60)].replace('\n', ' ')
                print(f"   [{idx}]: ...{snippet}...")
