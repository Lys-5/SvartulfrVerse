import urllib.request
import re

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\edit_page_chunks.txt', 'r', encoding='utf-8') as f:
    chunks = [line.strip() for line in f if line.strip()]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

matches = []
for c in chunks:
    url = 'https://app.wyvern.chat' + c
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
            for kw in ['Offer a persona', 'linked_persona_ids', 'lorebook_ids']:
                if kw in content:
                    print(f"Match '{kw}' in {c}")
                    matches.append((c, kw))
                    for m in re.finditer(re.escape(kw), content):
                        idx = m.start()
                        print(f"  [{kw}] snippet:\n{content[max(0, idx-150):min(len(content), idx+300)]}\n")
    except Exception as e:
        # print(f"Err {c}: {e}")
        pass

print(f"Done scanning {len(chunks)} chunks. Found {len(matches)} matches.")
