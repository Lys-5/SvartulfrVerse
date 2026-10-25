import urllib.request
import json

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

url = "https://app.wyvern.chat/api/prompt-assembly?limit=50&sort=updated_at&order=DESC"
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Status: 200 OK")
        print("Keys:", list(data.keys()))
        print("assemblies count:", len(data.get('assemblies', [])))
        for a in data.get('assemblies', []):
            print(f"- {a.get('id')} | {a.get('name')} | visibility={a.get('visibility')}")
except urllib.error.HTTPError as e:
    print(f"HTTPError {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("Error:", e)
