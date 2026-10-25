import json
import urllib.request

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

world_id = "_qWLGbk24Dm3JzydjXx7mQ"

payload = {
    "world_id": world_id,
    "world": world_id,
    "name": "California Coast",
    "description": "[ENVIRONMENT INFO:\nName: California Coast;\nDomain: Regional Coastal Macro-Biome;\nCoordinates & Span: Central California Pacific coastline spanning Blackwood County, Solarton, and northern Los Angeles;\nSetting & Metaphysics: Modern Supernatural Urban Fantasy, stable terrestrial reality, open supernatural society;\nDominant Presence: Werewolf Great Houses (Douglas, Marino, Rossi), SUCC Academic Body, Demi-human Communities, DCC, Mortal Municipalities]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Pacific ocean salt spray and ozone mingling with coastal pine resin, humid morning marine layer giving way to warm sunny afternoons, neon city glow after sunset;\nSpatial Architecture: Rugged Pacific cliffs, sandy beachheads, deep old-growth forests, urban commercial downtowns, coastal highway corridors;\nRifts & Dimensional Drift: Generally stable terrestrial baseline, though localized Reality Tears occasionally breach in remote canyons or deep forest clearings;\nHazards & Rules: Strict territorial pack jurisdictions, DCC private security enforcement, local council bylaws governing public supernatural manifestations]\n\n[CONTEXT & SECRETS:\nCosmology & Origins: Historic ancestral hub for native lupine lineages and modern supernatural integration, anchored along the Route 101 corridor;\nSecrets: Underground smuggling tunnels in Dockside, ancient Firstborn resting sites beneath the inland hills, concealed rift wards managed by the Douglas family]",
    "context_description": "[ENVIRONMENT INFO:\nName: California Coast;\nDomain: Regional Coastal Macro-Biome;\nCoordinates & Span: Central California Pacific coastline spanning Blackwood County, Solarton, and northern Los Angeles;\nSetting & Metaphysics: Modern Supernatural Urban Fantasy, stable terrestrial reality, open supernatural society;\nDominant Presence: Werewolf Great Houses (Douglas, Marino, Rossi), SUCC Academic Body, Demi-human Communities, DCC, Mortal Municipalities]\n\n[LORE & ENVIRONMENT:\nAtmosphere & Senses: Pacific ocean salt spray and ozone mingling with coastal pine resin, humid morning marine layer giving way to warm sunny afternoons, neon city glow after sunset;\nSpatial Architecture: Rugged Pacific cliffs, sandy beachheads, deep old-growth forests, urban commercial downtowns, coastal highway corridors;\nRifts & Dimensional Drift: Generally stable terrestrial baseline, though localized Reality Tears occasionally breach in remote canyons or deep forest clearings;\nHazards & Rules: Strict territorial pack jurisdictions, DCC private security enforcement, local council bylaws governing public supernatural manifestations]\n\n[CONTEXT & SECRETS:\nCosmology & Origins: Historic ancestral hub for native lupine lineages and modern supernatural integration, anchored along the Route 101 corridor;\nSecrets: Underground smuggling tunnels in Dockside, ancient Firstborn resting sites beneath the inland hills, concealed rift wards managed by the Douglas family]",
    "avatar": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba180ed1-e61d-4f1e-2305-c08aa7b40400/public",
    "environment_config": {
        "background": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba180ed1-e61d-4f1e-2305-c08aa7b40400/public",
        "ambient_sound": "",
        "music": "",
        "particles": ""
    },
    "keys": [
        "California Coast",
        "California",
        "Pacific Coast",
        "Blackwood",
        "Solarton"
    ],
    "key_logic": "AND_ANY",
    "secondary_keys": [],
    "case_sensitive": False,
    "whole_words_only": True,
    "brief_context_description": "",
    "key_position": "after_char",
    "included_lexicon_entries": [],
    "excluded_lexicon_entries": [],
    "final_instructions": ""
}

req = urllib.request.Request(
    'https://app.wyvern.chat/api/worlds/environments',
    data=json.dumps(payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

try:
    with urllib.request.urlopen(req) as resp:
        print("Status:", resp.status)
        data = json.loads(resp.read().decode('utf-8'))
        print("Created environment ID:", data.get('id') or data.get('_id'))
        print("Keys:", list(data.keys()))
        print(json.dumps(data, indent=2))
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("Error:", e)
