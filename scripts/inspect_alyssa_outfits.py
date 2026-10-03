import json
import urllib.request
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
token = get_auth_token()

alyssa = get_char(token, '_MXcEC8Y6B3BNm3b1ttHj6')
outfits = alyssa.get('outfits', [])

print(f"Total outfits on Alyssa: {len(outfits)}")
for o in outfits:
    print(f"ID: {o['id']:25s} | Name: {o['name']:15s} | Current Avatar: {o.get('avatar')}")
