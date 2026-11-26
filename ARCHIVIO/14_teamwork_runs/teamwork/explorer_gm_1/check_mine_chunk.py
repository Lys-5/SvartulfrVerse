import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

print("Page chunk length:", len(content))

# Look for tabs, routes, words like assistant, scenario, character, lorebook
print("\n--- Tabs / labels search ---")
for kw in ['assistant', 'Assistant', 'ASSISTANT', 'tab', 'Tab', 'tabs', 'persona', 'scenario', 'lorebook', 'engine']:
    matches = list(re.finditer(re.escape(kw), content))
    print(f"Keyword '{kw}': {len(matches)} matches")

# Print snippets for 'assistant' or 'Assistant' or 'ASSISTANT'
for kw in ['ASSISTANT', 'Assistant', 'assistant']:
    for m in re.finditer(re.escape(kw), content):
        idx = m.start()
        print(f"\n[Match for {kw}]:")
        print(content[max(0, idx-100):min(len(content), idx+200)])

# Also let's find all tab names in the page
print("\n--- Strings in page chunk ---")
strings = set(re.findall(r'"([A-Za-z0-9_\-\s/]{3,30})"', content))
interesting = [s for s in strings if any(k in s.lower() for k in ['char', 'assist', 'scen', 'lore', 'engin', 'creat', 'mine', 'world', 'prompt'])]
print("Interesting string literals:", interesting)
