import requests
import re
import urllib.parse
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'text/html', 'User-Agent': 'AuditorBot/1.0'}

r = requests.get('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
print("Edit page status:", r.status_code)
scripts = re.findall(r'src=["\']([^"\']+\.js[^"\']*)["\']', r.text)
print(f"Found {len(scripts)} scripts on lorebook edit page")
for s in scripts:
    if 'chunks' in s:
        print("Chunk:", s)
