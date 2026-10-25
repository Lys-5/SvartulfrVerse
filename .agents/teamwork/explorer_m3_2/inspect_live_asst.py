import urllib.request
import json
import pathlib
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.append(str(ROOT / 'scratch'))
import refresh_token

token = refresh_token.refresh()
url = "https://app.wyvern.chat/api/simple-assistant-config/simple_assistant_xRfBnV7wq48QppqbPPpTM"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req) as resp:
        print("HTTP Status:", resp.status)
        data = json.loads(resp.read().decode())
        print("ID:", data.get("id"))
        print("Title:", data.get("title"))
        print("Kind:", data.get("kind"))
        print("Keys:", list(data.keys()))
        print("System prompt len:", len(data.get("system_prompt", "")))
        print("Final instructions len:", len(data.get("final_instructions", "")))
        out_path = ROOT / '.agents' / 'teamwork' / 'explorer_m3_2' / 'live_assistant.json'
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Saved live assistant payload to:", out_path)
except Exception as e:
    print("Error:", e)
