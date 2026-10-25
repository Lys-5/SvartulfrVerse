import glob
import re

for f in glob.glob('e:/repository/SvartulfrVerse/scratch/*.js'):
    txt = open(f, encoding='utf-8').read()
    matches = re.finditer(r'(/api/[^"\'`]*prompt-templates[^"\'`]*)', txt)
    for m in matches:
        print(f"Found in {f}: {m.group(0)}")
        idx = m.start()
        print(txt[max(0, idx-100):min(len(txt), idx+200)])
        print("="*40)
