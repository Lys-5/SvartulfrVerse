import glob
import re

for fpath in glob.glob('scratch/*.js'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    for m in re.finditer(r'\bIM\b', c):
        idx = m.start()
        # check if it looks like an export or declaration
        snippet = c[max(0, idx-40):min(len(c), idx+60)]
        if any(k in snippet for k in ['export', 'function', 'return', 'a.d', '=>', ':']):
            print(f"{fpath} at {idx}: {snippet}")
