import urllib.request
import json

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

req = urllib.request.Request('https://app.wyvern.chat/api/prompt-templates?limit=50', headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

with open(r'e:\repository\SvartulfrVerse\scratch\wyvern_prompt_templates.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Total templates:", data.get('total'))
print("Templates count returned:", len(data.get('templates', [])))
for t in data.get('templates', []):
    print("ID:", t.get('id'), "| Name:", t.get('name'), "| is_default:", t.get('is_default'), "| user_id:", t.get('user_id'))
    if 'blocks' in t or 'template' in t or 'params' in t:
        print("   Keys in template:", list(t.keys()))
