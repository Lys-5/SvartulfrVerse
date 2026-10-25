import requests
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
cid = '_TbRM3EdxDjHFgqztTbCpL'

with open('FINAL/Edric_Douglas_card.json', 'r', encoding='utf-8') as f:
    full = json.load(f)

# Safe list of editable character fields
EDITABLE_FIELDS = [
    'name', 'display_name', 'avatar', 'description', 'personality', 'mes_example',
    'first_mes', 'scenario', 'post_history_instructions', 'pre_history_instructions',
    'visual_description', 'creator_notes', 'model_url', 'soundcloud_url', 'character_note',
    'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating', 'chat_name',
    'pronouns', 'outfits', 'default_outfit', 'shared_info', 'alternate_greetings',
    'secretFields', 'secrets', 'fields', 'commands', 'metadata'
]

safe_payload = {k: full[k] for k in EDITABLE_FIELDS if k in full}

r = requests.put(f'https://app.wyvern.chat/api/characters/{cid}', headers=headers, json=safe_payload)
print("PUT safe_payload status:", r.status_code)
if r.status_code != 200:
    print("Error:", r.text[:300])
else:
    print("SUCCESS: Character updated cleanly!")
