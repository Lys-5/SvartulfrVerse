import urllib.request
import json
import re
import os

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

endpoints = [
    '/api/prompts',
    '/api/prompts/mine',
    '/api/prompt-templates',
    '/api/prompt-templates/mine',
    '/api/prompt-assemblies',
    '/api/prompt-presets',
    '/api/presets',
    '/api/presets/mine',
    '/api/ai-connections',
    '/api/connections',
    '/api/settings',
    '/api/user-settings',
    '/api/users/me',
    '/api/user/settings',
    '/api/assistants',
    '/api/assistants/mine',
    '/api/story-engines/mine'
]

print("=== PROBING WYVERN API ENDPOINTS ===")
for ep in endpoints:
    url = f'https://app.wyvern.chat{ep}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read().decode('utf-8')
            try:
                parsed = json.loads(data)
                count = len(parsed) if isinstance(parsed, list) else (len(parsed.keys()) if isinstance(parsed, dict) else 'scalar')
                print(f"[OK 200] {ep}: type={type(parsed).__name__}, count/keys={count}")
                if isinstance(parsed, list) and len(parsed) > 0:
                    print(f"   Sample item: {parsed[0] if isinstance(parsed[0], str) else list(parsed[0].keys())[:8]}")
                elif isinstance(parsed, dict):
                    print(f"   Keys: {list(parsed.keys())[:10]}")
            except Exception:
                print(f"[OK 200] {ep}: text len={len(data)}")
    except urllib.error.HTTPError as e:
        print(f"[{e.code}] {ep}")
    except Exception as e:
        print(f"[ERR] {ep}: {e}")

print("\n=== FETCHING FRONTEND BUNDLES ===")
try:
    req_html = urllib.request.Request('https://app.wyvern.chat/', headers={'User-Agent': headers['User-Agent']})
    with urllib.request.urlopen(req_html, timeout=10) as resp:
        html = resp.read().decode('utf-8')
    print("HTML length:", len(html))
    scripts = re.findall(r'src="(/[^"]+\.js)"', html)
    print("Scripts found in HTML:", scripts)
except Exception as e:
    print("Error fetching HTML:", e)
