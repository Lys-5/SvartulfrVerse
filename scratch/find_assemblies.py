import glob
import re

for f in glob.glob('e:/repository/SvartulfrVerse/scratch/*.js'):
    txt = open(f, encoding='utf-8').read()
    for m in re.finditer(r'assemblies', txt):
        idx = m.start()
        print(f"In {f} at {idx}:")
        print(txt[max(0, idx-100):min(len(txt), idx+200)])
        print("="*40)
