import urllib.request
import json
import pathlib
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.append(str(ROOT / 'scratch'))
import refresh_token

token = refresh_token.refresh()
url = "https://app.wyvern.chat/api/prompt-assembly/pha_kWkWUAfTJTF9q72c2bC98"
req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req) as resp:
        print("HTTP Status:", resp.status)
        data = json.loads(resp.read().decode())
        print("ID:", data.get("id"))
        print("Name:", data.get("name"))
        print("Description:", data.get("description"))
        print("Visibility:", data.get("visibility"))
        print("Floating Depth:", data.get("floating_depth_percent"))
        print("Floating Role:", data.get("floating_role"))
        print("Keys in payload:", list(data.keys()))
        print("Blocks count:", len(data.get("blocks", [])))
        for i, b in enumerate(data.get("blocks", [])):
            print(f"Block {i}: id={b.get('block_id')}, label={b.get('label')}, role={b.get('role')}, order={b.get('order')}, content_len={len(b.get('content', ''))}")
        
        # Save a copy in our folder for detailed analysis
        out_path = ROOT / '.agents' / 'teamwork' / 'explorer_m3_2' / 'live_prompt_assembly.json'
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Saved live payload to:", out_path)
except Exception as e:
    print("Error:", e)
