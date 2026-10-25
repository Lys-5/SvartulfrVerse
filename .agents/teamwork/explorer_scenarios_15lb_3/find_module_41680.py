import glob
import re

for p in glob.glob(r'e:\repository\SvartulfrVerse\scratch\*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
        m = re.search(r'[\'"]?41680[\'"]?\s*:\s*(?:function|\()', t)
        if m:
            print(f"Found 41680 in {p} at {m.start()}")
            print(t[m.start():m.start()+2500])
            break
