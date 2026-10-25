import glob
import re

for f in glob.glob('e:/repository/SvartulfrVerse/scratch/*.js'):
    txt = open(f, encoding='utf-8').read()
    # Search for create: or getAll: or update: associated with assemblies
    for m in re.finditer(r'getAll:\s*async\s*function|\.getAll\s*=\s*|getAll:\s*\(', txt):
        idx = m.start()
        print(f"In {f} at {idx}:")
        print(txt[max(0, idx-50):min(len(txt), idx+300)])
        print("="*40)
