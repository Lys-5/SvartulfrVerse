import urllib.request
import urllib.error
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

token = open("scratch/wyvern_token.txt", "r", encoding="utf-8").read().strip()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

# Let's inspect _YpX47fNraQFw2dD7TdycJ
print("--- Checking _YpX47fNraQFw2dD7TdycJ ---")
req = urllib.request.Request("https://app.wyvern.chat/api/worlds/_YpX47fNraQFw2dD7TdycJ", headers=headers)
with urllib.request.urlopen(req) as resp:
    d1 = json.loads(resp.read().decode('utf-8'))
    print("ID: _YpX47fNraQFw2dD7TdycJ | Created:", d1.get('created_at'), "| Loc:", d1.get('locations_count'), "| Lex:", d1.get('lexicon_count'))

# Now where is the second one?
# Could the ID be in the user's inventory or recent chat logs or somewhere?
