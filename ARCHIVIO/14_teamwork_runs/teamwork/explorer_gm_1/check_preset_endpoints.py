import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

endpoints = [
    '/settings-presets',
    '/presets',
    '/prompt-templates/default',
    '/prompt-templates/browse',
    '/prompt-templates/usable',
    '/prompt-assemblies',
    '/prompts/default'
]

for ep in endpoints:
    url = f'https://app.wyvern.chat/api{ep}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = resp.read().decode('utf-8')
            print(f"[HTTP {resp.status}] GET {ep} -> len: {len(data)}")
    except urllib.error.HTTPError as e:
        print(f"[HTTP {e.code}] GET {ep} -> {e.read().decode('utf-8')[:150]}")
    except Exception as e:
        print(f"[ERR] GET {ep}: {e}")
