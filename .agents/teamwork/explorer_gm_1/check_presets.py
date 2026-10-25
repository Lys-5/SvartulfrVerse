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

url = 'https://app.wyvern.chat/api/simple-assistant-config/narrator-presets'
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Narrator Presets status:", resp.status)
        print("Keys:", list(data.keys()))
        presets = data.get('presets', [])
        print(f"Total presets: {len(presets)}")
        for p in presets:
            print(f"- Title: {p.get('title')}, Kind: {p.get('kind')}")
            print(f"  Description: {p.get('description')}")
            print(f"  System prompt: {p.get('system_prompt')[:100]}...")
            print(f"  Final instructions: {p.get('final_instructions', '')[:100]}...")
except Exception as e:
    print("Error:", e)
