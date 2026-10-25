import urllib.request
import re

# Fetch main chunks list or search chunks on /mine
url = 'https://app.wyvern.chat/mine'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
chunks = set(re.findall(r'/_next/static/chunks/[^\"]+\.js', html))

# Let's search all chunks for assistant creation form, fields, kind options, lorebook options, etc.
for c in chunks:
    cu = 'https://app.wyvern.chat' + c
    try:
        txt = urllib.request.urlopen(urllib.request.Request(cu, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
        if 'simple-assistant-config' in txt or 'simple_assistant' in txt:
            print(f"Match in chunk: {c}")
            for kw in ['kind', 'narrator', 'sidechat', 'lorebook', 'system_prompt', 'final_instructions']:
                if kw in txt:
                    for m in re.finditer(re.escape(kw), txt):
                        idx = m.start()
                        snip = txt[max(0, idx-100):min(len(txt), idx+200)]
                        if any(t in snip for t in ['options', 'schema', 'select', 'kind', 'system_prompt', 'lorebook', 'create']):
                            print(f"  [{kw}] -> {snip}\n")
    except Exception:
        pass
