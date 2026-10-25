import urllib.request
import re
import os

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

req_html = urllib.request.Request('https://app.wyvern.chat/', headers=headers)
with urllib.request.urlopen(req_html) as resp:
    html = resp.read().decode('utf-8')

scripts = re.findall(r'src="(/_next/static/chunks/[^"]+\.js)"', html)
print(f"Total script chunks in HTML: {len(scripts)}")

keywords = [
    'prompt-templates',
    'prompt_template',
    'promptTemplate',
    'Prompt Assembly',
    'floating_prompt',
    'floatingPrompt',
    'directors_whisper',
    'directorsWhisper',
    "Director's Whisper",
    'Floating Prompt',
    'special_stats',
    'rpg_stats',
    'AI Connections',
    'handlebar',
    'Handlebars',
    'post_history_instructions',
    'lore_entry'
]

results = {}

for s in scripts:
    url = f"https://app.wyvern.chat{s}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            content = resp.read().decode('utf-8')
        
        matches = []
        for kw in keywords:
            if kw.lower() in content.lower():
                matches.append(kw)
        
        if matches:
            results[s] = matches
            print(f"[MATCH] {s} -> {matches}")
    except Exception as e:
        pass

with open(r'e:\repository\SvartulfrVerse\scratch\js_bundle_matches.json', 'w', encoding='utf-8') as f:
    import json
    json.dump(results, f, indent=2)
