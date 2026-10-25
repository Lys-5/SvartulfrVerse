txt = open('e:/repository/SvartulfrVerse/scratch/54866-5b1f01a517163780.js', encoding='utf-8').read()

idx = 0
while True:
    idx = txt.find("AI Connections", idx)
    if idx == -1:
        break
    print(f"Match for 'AI Connections' at {idx}:")
    print(txt[max(0, idx-100):min(len(txt), idx+300)])
    print("=" * 50)
    idx += 14

for kw in ['prompt_assembly_id', 'promptAssemblyId', 'prompt_assembly', 'promptAssembly', 'activeAssembly']:
    idx = txt.find(kw)
    if idx != -1:
        print(f"Match for {kw} at {idx}:")
        print(txt[max(0, idx-100):min(len(txt), idx+300)])
        print("=" * 50)
