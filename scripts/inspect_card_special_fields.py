import json
import urllib.request
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
CARD_ID = '_MXcEC8Y6B3BNm3b1ttHj6'

token = get_auth_token()
card = get_char(token, CARD_ID)

print("=== RPG STATS ===")
print("rpg_stats:", json.dumps(card.get('rpg_stats'), indent=2))
print("species:", card.get('species'))
print("occupation:", card.get('occupation'))

print("\n=== ATTITUDES ===")
print("attitudes count:", len(card.get('attitudes') or []))
print("attitudes:", json.dumps(card.get('attitudes'), indent=2))

print("\n=== CHARACTER TRAITS ===")
print("character_traits:", card.get('character_traits'))

print("\n=== SPEECH EXAMPLES ===")
print("speech_examples count:", len(card.get('speech_examples') or []))
if card.get('speech_examples'):
    print(card.get('speech_examples')[:2])

print("\n=== FINAL INSTRUCTIONS ===")
print("final_instructions:", card.get('final_instructions'))
