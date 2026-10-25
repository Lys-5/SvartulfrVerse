import urllib.request
import json

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

url = "https://app.wyvern.chat/api/exploreSearch/prompt-assemblies?page=1&limit=50"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

with open(r'e:\repository\SvartulfrVerse\scratch\explore_prompt_assemblies.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Total: {data.get('total')}")
for item in data.get('results', []):
    print(f"ID: {item.get('id')} | Name: {item.get('name')} | user_id: {item.get('user_id')}")
    print("   Keys:", list(item.keys()))
    if 'blocks' in item:
        print("   Blocks count:", len(item.get('blocks', [])))
        if len(item['blocks']) > 0:
            print("   Block 0 keys:", list(item['blocks'][0].keys()))
            print("   Block labels:", [b.get('label') or b.get('name') for b in item['blocks']])
    if 'main_prompt_sections' in item:
        print("   Main sections count:", len(item.get('main_prompt_sections', [])))
        print("   Main sections:", [s.get('name') for s in item['main_prompt_sections']])
    if 'floating_prompt_sections' in item:
        print("   Floating sections count:", len(item.get('floating_prompt_sections', [])))
        print("   Floating sections:", [s.get('name') for s in item['floating_prompt_sections']])
    print("   lore_template length:", len(item.get('lore_template', '') or ''))
    print("   whisper_template length:", len(item.get('whisper_template', '') or ''))
    print("-" * 50)
