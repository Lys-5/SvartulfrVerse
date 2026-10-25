import urllib.request
import urllib.error
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

id1 = '_YpX47fNraQFw2dD7TdycJ'
id2 = '_43gzGmT8gXga9aJTrqTUM'

for wid in [id1, id2]:
    print(f"\n==================== WORLD {wid} ====================")
    url = f"https://app.wyvern.chat/api/worlds/{wid}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print("Name:", data.get('name'))
            print("Created at:", data.get('created_at'))
            print("Updated at:", data.get('updated_at'))
            print("Locations count:", data.get('locations_count'))
            print("Lexicon count:", data.get('lexicon_count'))
            print("Environments count:", data.get('environments_count'))
            print("Linked characters count:", data.get('linked_characters_count'))
            print("Status:", data.get('status'))
            print("Visibility:", data.get('visibility'))
            print("Disable enhanced instructions:", data.get('disable_enhanced_instructions'))
            print("System prompt override len:", len(data.get('system_prompt_override') or ''))
    except Exception as e:
        print("Error fetching:", e)
