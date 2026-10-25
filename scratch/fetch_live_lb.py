import json
import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json',
    'User-Agent': 'AuditorBot/1.0'
}

# Fetch Primary and Secondary Lorebooks
for name, lid in [('Primary', '_zwEqgEEzh12X6gHVmMKKC'), ('Secondary', '_Uht3Ckz44JBDrPnUHq7LV')]:
    print(f"\n=================== {name} ({lid}) ===================")
    r = requests.get(f'https://app.wyvern.chat/api/lorebooks/{lid}', headers=headers, timeout=10)
    print("Status:", r.status_code)
    if r.status_code == 200:
        data = r.json()
        print("Top level keys:", list(data.keys()))
        print("gallery in keys:", 'gallery' in data)
        if 'gallery' in data:
            print("gallery type:", type(data['gallery']))
            print("gallery length:", len(data['gallery']) if isinstance(data['gallery'], list) else 'N/A')
            if isinstance(data['gallery'], list) and len(data['gallery']) > 0:
                print("First gallery item sample:", json.dumps(data['gallery'][0], indent=2))
        for k in data.keys():
            if 'gallery' in k.lower() or 'image' in k.lower() or 'photo' in k.lower() or 'asset' in k.lower():
                print(f"Media key '{k}':", str(data[k])[:150])
    else:
        print("Error text:", r.text[:300])
