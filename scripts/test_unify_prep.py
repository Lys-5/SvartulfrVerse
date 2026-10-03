import json
import urllib.request
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
PERSONA_ID = 'persona_1786335754946'
CARD_ID = '_MXcEC8Y6B3BNm3b1ttHj6'

token = get_auth_token()

# 1. Fetch gallery
req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/{WORLD_ID}/gallery', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
gal = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
gal_map = {item['title']: item['imageURL'] for item in gal}

# 2. Fetch live Persona
req_p = urllib.request.Request(f'https://app.wyvern.chat/api/user-personas/{PERSONA_ID}', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
persona = json.loads(urllib.request.urlopen(req_p).read().decode('utf-8'))

# 3. Fetch live Card
card = get_char(token, CARD_ID)

print("Loaded Persona and Card.")
print("Persona Outfits:", len(persona.get('outfits', [])))
print("Card Outfits:", len(card.get('outfits', [])))
