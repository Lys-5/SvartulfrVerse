import urllib.request
import re

url = 'https://app.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4/edit'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

for kw in ['char_scenario_1DC43ggb6mB8YLJDJKrU4', 'lorebook', 'Villa Douglas', 'Svartulfr', 'slots', 'greetings']:
    cnt = len(re.findall(re.escape(kw), html, re.IGNORECASE))
    print(f"Keyword '{kw}': {cnt} matches in HTML")
