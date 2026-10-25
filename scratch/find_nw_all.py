txt = open('e:/repository/SvartulfrVerse/scratch/36457-688d656b1534b9f0.js', encoding='utf-8').read()

idx = 0
while True:
    idx = txt.find("N.W", idx)
    if idx == -1:
        break
    print(f"Match for N.W at {idx}:")
    print(txt[max(0, idx-50):min(len(txt), idx+200)])
    print("-" * 50)
    idx += 3
