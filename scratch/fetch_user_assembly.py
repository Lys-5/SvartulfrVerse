import urllib.request
import json

token = open(r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

url = "https://app.wyvern.chat/api/prompt-assembly/pha_bjzXBqMTDDWcfnCPzdUqr"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

with open('e:/repository/SvartulfrVerse/scratch/user_existing_prompt_assembly.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Fetched existing user assembly successfully!")
print("Keys:", list(data.keys()))
print("Name:", data.get('name'))
print("Visibility:", data.get('visibility'))
print("Blocks count:", len(data.get('blocks', [])))
print("Main sections count:", len(data.get('main_prompt_sections', [])))
print("Floating sections count:", len(data.get('floating_prompt_sections', [])))
print("floating_depth_percent:", data.get('floating_depth_percent'))
print("floating_role:", data.get('floating_role'))
