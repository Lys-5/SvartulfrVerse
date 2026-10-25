import re

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\fetch_edit_chunks.py', 'r') as _:
    pass

# We already fetched the HTML in fetch_edit_chunks.py, let's write a script that saves the HTML to a file or searches inside it
req_script = """
import urllib.request
import re

token_file = r'e:\\repository\\SvartulfrVerse\\scratch\\wyvern_token.txt'
with open(token_file, 'r', encoding='utf-8') as f:
    token = f.read().strip()

url = 'https://app.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4/edit'
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

keywords = ['Offer a persona', 'persona', 'lorebook', 'accordion', 'Accordion', 'linked_persona_ids']
for kw in keywords:
    matches = list(re.finditer(re.escape(kw), html, re.IGNORECASE))
    print(f"Keyword '{kw}': {len(matches)} matches in HTML")
    for m in matches[:3]:
        pos = m.start()
        print(f"  Snippet: {repr(html[max(0, pos-100):min(len(html), pos+200)])}")

"""

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\search_html.py', 'w', encoding='utf-8') as f:
    f.write(req_script)
