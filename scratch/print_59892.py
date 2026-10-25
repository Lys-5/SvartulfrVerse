txt = open('e:/repository/SvartulfrVerse/scratch/36457-688d656b1534b9f0.js', encoding='utf-8').read()

idx = 0
while True:
    idx = txt.find("59892", idx)
    if idx == -1:
        break
    print(f"Match at {idx}:")
    print(txt[max(0, idx-50):min(len(txt), idx+300)])
    print("-" * 50)
    idx += 5
