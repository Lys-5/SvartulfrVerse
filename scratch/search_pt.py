for fname in ['69712-af83c29ebab813a8.js', '29079-b6a0d5e327fba37e.js', '61929-5cc0e3b134146cf3.js']:
    txt = open(f'e:/repository/SvartulfrVerse/scratch/{fname}', encoding='utf-8').read()
    idx = 0
    while True:
        idx = txt.find("prompt-template", idx)
        if idx == -1:
            break
        print(f"=== {fname} at {idx} ===")
        print(txt[max(0, idx-100):min(len(txt), idx+300)])
        idx += 15
