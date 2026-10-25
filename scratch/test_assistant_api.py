import urllib.request
import json

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

# 1. Test GET /api/simple-assistant-config
url = "https://app.wyvern.chat/api/simple-assistant-config"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("GET /api/simple-assistant-config status:", resp.status)
        print("Data type:", type(data))
        if isinstance(data, list):
            print(f"Total user assistants: {len(data)}")
            for a in data:
                print(f"ID: {a.get('id')} | Title: {a.get('title')} | Kind: {a.get('kind')}")
                print("Keys:", list(a.keys()))
        elif isinstance(data, dict):
            print("Dict keys:", list(data.keys()))
            results = data.get('results') or data.get('data') or []
            print(f"Results count: {len(results)}")
            for a in results:
                print(f"ID: {a.get('id')} | Title: {a.get('title')} | Kind: {a.get('kind')}")
                print("Keys:", list(a.keys()))
except Exception as e:
    print("GET assistants error:", e)

# 2. Test GET narrator presets
url_presets = "https://app.wyvern.chat/api/simple-assistant-config/narrator-presets"
req_presets = urllib.request.Request(url_presets, headers=headers)
try:
    with urllib.request.urlopen(req_presets) as resp:
        presets = json.loads(resp.read().decode('utf-8'))
        print("\nNarrator presets status:", resp.status)
        print("Presets:", json.dumps(presets, indent=2)[:500])
except Exception as e:
    print("GET presets error:", e)

# 3. Test GET single assistant (from earlier page 4: simple_assistant_6FXbE28w7n8ETrU41ph7V)
url_single = "https://app.wyvern.chat/api/simple-assistant-config/simple_assistant_6FXbE28w7n8ETrU41ph7V"
req_single = urllib.request.Request(url_single, headers=headers)
try:
    with urllib.request.urlopen(req_single) as resp:
        single = json.loads(resp.read().decode('utf-8'))
        print("\nSingle assistant status:", resp.status)
        print("Single assistant keys:", list(single.keys()))
        print("Single assistant JSON:\n", json.dumps(single, indent=2))
except Exception as e:
    print("GET single assistant error:", e)
