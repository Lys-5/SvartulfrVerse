import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import urllib.request, json
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}

for wid in ['_CgYT8fHXpDC4crjmegQF7', '_YpX47fNraQFw2dD7TdycJ']:
    url = f'https://app.wyvern.chat/api/worlds/{wid}'
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as resp:
        w = json.loads(resp.read().decode('utf-8'))
        print(f"=== WORLD {wid} ===")
        print("Name:", w.get("name"))
        print("Creator:", w.get("creator"))
        print("Locations:", w.get("locations_count"))
        print("Lexicon:", w.get("lexicon_count"))
        print("Environments:", w.get("environments_count"))
        print("Linked Chars:", w.get("linked_characters_count"))
        print("Updated:", w.get("updated_at"))
