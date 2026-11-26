import urllib.request
import json
import re
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

# 1. Inspect /characters/mine
url = 'https://app.wyvern.chat/api/characters/mine'
req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        mine_data = json.loads(resp.read().decode('utf-8'))
        chars = mine_data.get('characters', [])
        print(f"Total characters in /characters/mine: {len(chars)}")
        types_found = set()
        for c in chars:
            for k in ['type', 'kind', 'category', 'is_assistant', 'role', 'assistant']:
                if k in c:
                    types_found.add(f"{k}={c[k]}")
        print("Types found in characters:", types_found)
        if chars:
            print("First char keys:", list(chars[0].keys()))
            # check if any character has 'assistant' in name or description or tags
            for c in chars:
                name = c.get('name', '')
                tags = c.get('tags', [])
                if 'assistant' in name.lower() or any('assistant' in str(t).lower() for t in tags):
                    print(f"Found character possibly assistant: id={c.get('id')}, name={name}, tags={tags}")
except Exception as e:
    print("Error querying /characters/mine:", e)

# 2. Inspect /mine HTML and JS chunks
print("\n--- Inspecting /mine page chunks ---")
mine_url = 'https://app.wyvern.chat/mine'
req = urllib.request.Request(mine_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        chunks = set(re.findall(r'/_next/static/chunks/[^\"]+\.js', html))
        print(f"Found {len(chunks)} chunks in /mine HTML")
        
        matches = {}
        for c in chunks:
            cu = 'https://app.wyvern.chat' + c
            try:
                txt = urllib.request.urlopen(urllib.request.Request(cu, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
                for kw in ['ASSISTANT', 'assistant', 'Assistant', 'create-assistant', '/assistants', 'story-engine', 'story_engine']:
                    if kw in txt:
                        if c not in matches:
                            matches[c] = []
                        matches[c].append(kw)
            except Exception as e:
                pass
        
        for c, kws in matches.items():
            print(f"Chunk {c} matched {kws}")

        # Let's search inside the most promising chunks for ASSISTANT tabs or endpoints
        for c, kws in matches.items():
            if 'ASSISTANT' in kws or 'create-assistant' in kws or 'assistant' in kws:
                cu = 'https://app.wyvern.chat' + c
                txt = urllib.request.urlopen(urllib.request.Request(cu, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
                for kw in ['ASSISTANT', 'assistant', 'story-engine']:
                    for m in re.finditer(re.escape(kw), txt):
                        idx = m.start()
                        snippet = txt[max(0, idx-150):min(len(txt), idx+250)]
                        # filter out mundane noise
                        if any(term in snippet for term in ['tab', 'mine', 'api', 'endpoint', 'create', 'href', 'route', 'filter', 'type']):
                            print(f"\n[SNIPPET in {c} for '{kw}']:\n{snippet}\n")
except Exception as e:
    print("Error inspecting /mine:", e)
