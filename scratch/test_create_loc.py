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
env_id = "_cAQ9nDkjmzBRANwAjm1fa"

# Create root location
root_payload = {
    "world_id": world_id,
    "world": world_id,
    "environment": env_id,
    "environment_id": env_id,
    "name": "Bakersfield",
    "description": "[LOCATION INFO:\nEra: 2024 (Modern Fantasy / Post-Gate Era);\nLocation: Bakersfield (Central Valley Agricultural & Oil Hub);\nSetting: Vast flat expanse of pumpjacks, citrus orchards, agricultural canals, and semi-rural working-class towns;\nFactions: Local Werewolf Farmsteads, Human Farm Workers, Independent Demihuman Labor Unions, DCC Freight Depots;\nConflicts: Corporate agricultural water rights vs local werewolf ranchers, environmental runoff from Kern River oil fields;\nSociety: Hardworking blue-collar culture, quiet pack integration, suspicious of big city bureaucracy and outsider intrusions]\n\n[LORE & ENVIRONMENT:\nEnvironment: Dry heat, smell of crude oil, dust, exhaust, and pesticide-scented citrus groves, wide open sun-bleached skies;\nArchitecture: Low-slung single-story ranches, rustic wooden diners, steel grain silos, sprawling rusty oil pump fields;\nSecurity & Wards: Local neighborhood watch, farm perimeter scent posts, private shotguns behind pickup truck truck-racks;\nDemographics: 80% Human, 15% Demihuman laborers, 5% Werewolf farming families;\nRules & Restrictions: No trespassing on private oil leases, respect livestock borders, keep city politics west of the Grapevine]\n\n[CONTEXT & SECRETS:\nHistory: Founded in the 19th century as an agricultural and petroleum powerhouse, long serving as a quiet breadbasket and supply line for Blackwood and Los Angeles;\nSecrets: Abandoned dry oil wells in Kern River canyon occasionally serve as clandestine off-the-grid hideouts for rogue packs and unregistered demihumans]",
    "context_description": "Una vasta distesa pianeggiante di campi petroliferi, frutteti e magazzini agricoli nella Central Valley. L'odore acre del petrolio greggio si mescola alla polvere secca e al profumo amaro degli agrumi riscaldati dal sole.",
    "keys": ["Bakersfield", "Kern River", "Oildale"],
    "key_logic": "AND_ANY",
    "secondary_keys": [],
    "case_sensitive": False,
    "whole_words_only": True,
    "brief_context_description": "",
    "key_position": "after_char",
    "avatar": "",
    "environment_config": {
        "background": "",
        "ambient_sound": "",
        "music": "",
        "particles": ""
    },
    "included_lexicon_entries": [],
    "excluded_lexicon_entries": [],
    "final_instructions": ""
}

req = urllib.request.Request(
    'https://app.wyvern.chat/api/worlds/locations',
    data=json.dumps(root_payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

try:
    with urllib.request.urlopen(req) as resp:
        print("Root Location Status:", resp.status)
        root_data = json.loads(resp.read().decode('utf-8'))
        root_loc_id = root_data.get('id') or root_data.get('_id')
        print("Created root location ID:", root_loc_id)
        print("Keys:", list(root_data.keys()))
        print("Environment on root:", root_data.get('environment'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error on root {e.code}: {e.read().decode('utf-8')}")
    exit(1)
except Exception as e:
    print("Error on root:", e)
    exit(1)

# Now create child location
child_payload = {
    "world_id": world_id,
    "world": world_id,
    "environment": env_id,
    "environment_id": env_id,
    "parent_location": root_loc_id,
    "parent_location_id": root_loc_id,
    "name": "Bakersfield Square",
    "description": "[LOCATION INFO:\nEra: 2024 (Modern Fantasy / Post-Gate Era);\nLocation: Bakersfield Square (Downtown Civic & Commercial Center);\nSetting: Sun-bleached asphalt parking lots, weathered brick storefronts, neon motel signs, and country radio drifting from passing pickups;\nFactions: Local Shopkeepers, Blue-collar Demihumans, Traveling Truckers, Sheriff's Deputies;\nConflicts: Local mom-and-pop commerce vs DCC supply chain takeover, territorial disputes between roving road crews;\nSociety: Relaxed daytime shopping, lively neon nights at country bars, tight-knit local gossip networks]\n\n[LORE & ENVIRONMENT:\nEnvironment: Warm breeze carrying diesel exhaust and fried food aromas from diners, buzz of fluorescent streetlights at dusk;\nArchitecture: Mid-century brick commercial blocks, metal awnings, rustic post office, open square with benches and dusty palm trees;\nSecurity & Wards: Local municipal sheriff patrols, store security cameras, zero DCC biometric drone presence;\nDemographics: Human locals, demihuman service staff, visiting ranchers;\nRules & Restrictions: No loitering after midnight, quiet hours enforced in nearby residential avenues]\n\n[CONTEXT & SECRETS:\nHistory: Historic hub of downtown Bakersfield commerce, holding annual seasonal harvest festivals for both human and demihuman communities;\nSecrets: The basement of the old town hall houses historical archives detailing early 1900s agreements between human civic founders and lupine homesteaders]",
    "context_description": "Il centro civico e commerciale di Bakersfield. Vetrine impolverate, tavole calde illuminate al neon e furgoni parcheggiati sotto il sole californiano.",
    "keys": ["Bakersfield Square", "downtown Bakersfield"],
    "key_logic": "AND_ANY",
    "secondary_keys": [],
    "case_sensitive": False,
    "whole_words_only": True,
    "brief_context_description": "",
    "key_position": "after_char",
    "avatar": "",
    "environment_config": {
        "background": "",
        "ambient_sound": "",
        "music": "",
        "particles": ""
    },
    "included_lexicon_entries": [],
    "excluded_lexicon_entries": [],
    "final_instructions": ""
}

req_child = urllib.request.Request(
    'https://app.wyvern.chat/api/worlds/locations',
    data=json.dumps(child_payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

try:
    with urllib.request.urlopen(req_child) as resp:
        print("Child Location Status:", resp.status)
        child_data = json.loads(resp.read().decode('utf-8'))
        print("Created child location ID:", child_data.get('id') or child_data.get('_id'))
        print("Parent on child:", child_data.get('parent_location'))
        print("Environment on child:", child_data.get('environment'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error on child {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("Error on child:", e)
