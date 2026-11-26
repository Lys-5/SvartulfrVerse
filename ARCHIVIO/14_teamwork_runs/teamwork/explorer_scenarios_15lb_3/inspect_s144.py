import urllib.request
import re

url = 'https://app.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4/edit'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

inline_scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
s144 = inline_scripts[144]
print(f"Script 144 length: {len(s144)}")

for kw in ['lorebook_ids', 'linked_persona_ids', 'Offer a persona']:
    matches = list(re.finditer(re.escape(kw), s144))
    print(f"Keyword '{kw}': {len(matches)} matches in script 144")
    for m in matches[:3]:
        pos = m.start()
        print(f"  Snippet:\n{s144[max(0, pos-100):min(len(s144), pos+200)]}\n")
