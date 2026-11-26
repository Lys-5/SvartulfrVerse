import glob

for p in glob.glob(r'e:\repository\SvartulfrVerse\scratch\*.js'):
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        t = f.read()
        if '41680' in t:
            pos = t.find('41680')
            print(f"Found in {p} at {pos}:")
            print(t[max(0, pos-100):min(len(t), pos+300)])
