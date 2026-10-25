import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'User-Agent': 'AuditorBot/1.0'}

lid = '_zwEqgEEzh12X6gHVmMKKC'
candidate_urls = [
    f'https://app.wyvern.chat/api/lorebooks/{lid}/gallery',
    f'https://api.wyvern.chat/lorebooks/{lid}/gallery',
    f'https://app.wyvern.chat/api/gallery?lorebook_id={lid}',
    f'https://app.wyvern.chat/api/gallery/lorebooks/{lid}',
    f'https://app.wyvern.chat/api/lorebooks/gallery/{lid}',
    f'https://app.wyvern.chat/api/gallery',
    f'https://api.wyvern.chat/gallery',
]

for url in candidate_urls:
    try:
        r = requests.get(url, headers=headers, timeout=5)
        print(f"{url} -> {r.status_code} ({len(r.text)} bytes): {r.text[:150]}")
    except Exception as e:
        print(f"{url} -> Error: {e}")
