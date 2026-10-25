import glob

for f in glob.glob('e:/repository/SvartulfrVerse/scratch/*.js'):
    txt = open(f, encoding='utf-8').read()
    if '59892' in txt:
        print(f"Found 59892 in {f}")
        for m in txt.split('59892:'):
            if len(m) < len(txt):
                print("Snippet from definition:\n", m[:300])
