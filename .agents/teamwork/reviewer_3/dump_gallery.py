import requests
import json

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'AuditorBot/1.0'}

r = requests.get('https://app.wyvern.chat/api/gallery/lorebook/_zwEqgEEzh12X6gHVmMKKC', headers=headers)
data = r.json()
print(f"Total gallery items in Primary: {len(data)}")
for item in data:
    title = item.get('title', '')
    url = item.get('imageURL', '')
    print(f"{title:25} | {url}")

with open('.agents/teamwork/reviewer_3/primary_gallery.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, indent=2)
