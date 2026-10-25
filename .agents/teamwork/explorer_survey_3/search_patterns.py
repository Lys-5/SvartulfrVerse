import glob, re

patterns = [
    r'auto[_\s-]?apply',
    r'content[_\s-]?creation',
    r'scene[_\s-]?auto',
    r'party[_\s-]?auto',
    r'auto[_\s-]?party',
    r'auto[_\s-]?scene',
    r'auto[_\s-]?advance',
    r'ai[_\s-]?content',
    r'apply[_\s-]?scene',
    r'apply[_\s-]?party'
]

for f in glob.glob('scratch/*.js'):
    txt = open(f, encoding='utf-8', errors='ignore').read()
    for pat in patterns:
        for m in re.finditer(pat, txt, re.IGNORECASE):
            idx = m.start()
            print(f"[{f}] Matched '{pat}' at {idx}:")
            print(txt[max(0, idx-100):min(len(txt), idx+200)].replace('\n', ' '))
            print("-" * 50)
