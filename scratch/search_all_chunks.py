import urllib.request
import re

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'User-Agent': 'Mozilla/5.0'}

req_html = urllib.request.Request('https://app.wyvern.chat/', headers=headers)
with urllib.request.urlopen(req_html) as resp:
    html = resp.read().decode('utf-8')

scripts = re.findall(r'src="(/_next/static/chunks/[^"]+\.js)"', html)

print(f"Checking {len(scripts)} scripts for '59892' or 'prompt-assemblies' or API endpoints...")

found = []
for s in scripts:
    url = f"https://app.wyvern.chat{s}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
        if '59892' in content or 'pha_' in content or 'prompt_assembly' in content or 'promptAssembly' in content:
            found.append(s)
            print(f"[FOUND] {s}")
            for term in ['59892', 'pha_', 'prompt_assembly', 'promptAssembly']:
                if term in content:
                    idx = content.find(term)
                    print(f"   Snippet for {term}: {content[max(0, idx-50):min(len(content), idx+150)]}")
    except Exception as e:
        pass

print("Done. Found in:", found)
