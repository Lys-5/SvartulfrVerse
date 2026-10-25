import urllib.request
import re

url = 'https://app.wyvern.chat/mine'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
chunks = set(re.findall(r'/_next/static/chunks/[^\"]+\.js', html))

print(f"Scanning {len(chunks)} chunks for Prompt Assembly and AI Connections...")

for c in chunks:
    cu = 'https://app.wyvern.chat' + c
    try:
        txt = urllib.request.urlopen(urllib.request.Request(cu, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
        if any(term in txt for term in ['Prompt Assembly', 'Floating Prompt', "Director's Whisper", 'Main Prompt Template', 'prompt_assembly', 'prompt-assemblies']):
            print(f"Match in chunk {c}")
            for kw in ['Floating Prompt', "Director's Whisper", 'Prompt Assembly', 'Lore Template', 'Main Prompt']:
                for m in re.finditer(re.escape(kw), txt):
                    idx = m.start()
                    print(f"  [{kw}] in {c}:\n{txt[max(0, idx-100):min(len(txt), idx+200)]}\n")
    except Exception:
        pass
