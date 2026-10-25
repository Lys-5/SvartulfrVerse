import glob
import re

for fpath in glob.glob('scratch/*.js'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    for m in re.finditer(r'IM\s*:\s*function', c):
        print(f"Found IM:function in {fpath} at {m.start()}:")
        print(c[m.start():m.start()+300])
