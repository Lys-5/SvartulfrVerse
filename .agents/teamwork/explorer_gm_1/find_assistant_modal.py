import urllib.request
import re

url = 'https://app.wyvern.chat/mine'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
chunks = set(re.findall(r'/_next/static/chunks/[^\"]+\.js', html))

print(f"Scanning {len(chunks)} chunks for assistant creation form...")

for c in chunks:
    cu = 'https://app.wyvern.chat' + c
    try:
        txt = urllib.request.urlopen(urllib.request.Request(cu, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
        if 'createAssistant' in txt or 'Create Assistant' in txt or 'create_assistant' in txt or 'system_prompt' in txt:
            # check if it has input or form fields for assistant
            if 'system_prompt' in txt and ('title' in txt or 'description' in txt):
                print(f"Found form in chunk: {c}")
                for kw in ['Create Assistant', 'Edit Assistant', 'kind', 'narrator', 'sidechat']:
                    for m in re.finditer(re.escape(kw), txt):
                        idx = m.start()
                        print(f"  [{kw}] in {c}:\n{txt[max(0, idx-100):min(len(txt), idx+200)]}\n")
    except Exception:
        pass
