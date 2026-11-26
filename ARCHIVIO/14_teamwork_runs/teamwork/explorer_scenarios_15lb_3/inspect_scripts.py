import urllib.request
import re

url = 'https://app.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4/edit'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

scripts = re.findall(r'<script[^>]*src=[\'"]([^\'"]+)[\'"]', html)
print(f"Total script src tags: {len(scripts)}")
for s in scripts:
    print(s)

# Also let's check inline scripts or self.__next_f
inline_scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"\nTotal inline scripts: {len(inline_scripts)}")
for i, s in enumerate(inline_scripts):
    if 'self.__next_f' in s:
        print(f"Inline script {i} has self.__next_f (len: {len(s)})")
        # search for chunks referenced inside self.__next_f
        c_matches = re.findall(r'static/chunks/[a-zA-Z0-9_\-\.]+\.js', s)
        if c_matches:
            print("  Referenced chunks in self.__next_f:", sorted(set(c_matches)))
