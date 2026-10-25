import glob

for f in glob.glob('scratch/*.js'):
    txt = open(f, encoding='utf-8', errors='ignore').read()
    pos = txt.find('98043')
    while pos != -1:
        prefix = txt[max(0, pos-40):pos]
        suffix = txt[pos+5:min(len(txt), pos+60)]
        print(f"[{f}] pos={pos}: ...{prefix} -> 98043 <- {suffix}...")
        pos = txt.find('98043', pos+5)
