import urllib.request

headers = {'User-Agent': 'Mozilla/5.0'}

for chunk in ['53145-79a5e9c927da31b2.js', '14685-a6f37bf36e7cf713.js']:
    url = f"https://app.wyvern.chat/_next/static/chunks/{chunk}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
    with open(f"e:/repository/SvartulfrVerse/scratch/{chunk}", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Downloaded {chunk}, len={len(content)}")

# Inspect 53145
txt_53145 = open('e:/repository/SvartulfrVerse/scratch/53145-79a5e9c927da31b2.js', encoding='utf-8').read()
for kw in ['prompt_assembly_id', 'prompt_assembly', 'localStorage', 'IndexedDB', 'activePromptAssembly']:
    idx = 0
    while True:
        idx = txt_53145.find(kw, idx)
        if idx == -1:
            break
        print(f"\n[53145] Match for {kw} at {idx}:")
        print(txt_53145[max(0, idx-100):min(len(txt_53145), idx+250)])
        idx += len(kw)

# Inspect 14685
txt_14685 = open('e:/repository/SvartulfrVerse/scratch/14685-a6f37bf36e7cf713.js', encoding='utf-8').read()
idx = 0
while True:
    idx = txt_14685.find('prompt_assembly_id', idx)
    if idx == -1:
        break
    print(f"\n[14685] Match for prompt_assembly_id at {idx}:")
    print(txt_14685[max(0, idx-100):min(len(txt_14685), idx+250)])
    idx += 18
