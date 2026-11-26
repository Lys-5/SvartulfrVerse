import glob, re

for f in glob.glob('scratch/*.js'):
    txt = open(f, encoding='utf-8', errors='ignore').read()
    for m in re.finditer(r'chat_overrides', txt):
        idx = m.start()
        print(f"[{f}] at {idx}:")
        print(txt[max(0, idx-100):min(len(txt), idx+250)])
        print("-" * 60)
