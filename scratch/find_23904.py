import glob
import re

for fpath in glob.glob('scratch/*.js'):
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    m = re.search(r'23904\s*:\s*function|23904\s*:\s*\(', c)
    if m:
        print(f"Found module 23904 definition in {fpath} at {m.start()}")
        print(c[m.start():m.start()+600])
