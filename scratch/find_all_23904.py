import glob
import re

for fpath in glob.glob('scratch/*.js'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    for m in re.finditer(r'23904', c):
        idx = m.start()
        print(f"{fpath} at {idx}:")
        print(c[max(0, idx-50):min(len(c), idx+100)])
