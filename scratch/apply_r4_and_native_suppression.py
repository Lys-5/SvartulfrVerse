import json
import pathlib
import urllib.request
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
final_dir = ROOT / 'FINAL'

# Load card sources
scarlett_card = json.loads((final_dir / 'Scarlett_Rose_card.json').read_text(encoding='utf-8'))
sierra_card = json.loads((final_dir / 'Sierra_Cruz_card.json').read_text(encoding='utf-8'))
russ_card = json.loads((final_dir / 'Russ_card.json').read_text(encoding='utf-8'))
stan_card = json.loads((final_dir / 'Stan_Davies_Jr_card.json').read_text(encoding='utf-8'))
jared_card = json.loads((final_dir / 'Jared_Thompson_card.json').read_text(encoding='utf-8'))
alyssa_card = json.loads((final_dir / 'Alyssa_Douglas_Bloodmoon_card.json').read_text(encoding='utf-8'))
jasper_card = json.loads((final_dir / 'Jasper_Douglas_Bloodmoon_card.json').read_text(encoding='utf-8'))

# Define updates for NPC Primary
primary_updates = {
    '4NzXF4_0hYxmN7Idltzpw': {
        'name': 'Scarlett Rose',
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ['Scarlett Rose', 'Scarlett'],
        'key_logic': 'AND_ANY',
        'avatar': scarlett_card.get('avatar'),
        'custom_avatar_regex': True,
        'lines_parsed': 1,
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Scarlett\ Rose|Scarlett)\s*:',
        'npc_info': {
            'first_name': 'Scarlett',
            'last_name': 'Rose',
            'nicknames': ['Scarlett'],
            'titles': []
        },
        'content': scarlett_card.get('description'),
        'ignored_characters': ['_qXgBMbFYJfc84hbLHhe92'],
        'ignored_personas': []
    },
    'ijy8vrlphNv19-p-gbYuY': {
        'name': 'Sierra Cruz',
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ['Sierra Cruz', 'Sierra'],
        'key_logic': 'AND_ANY',
        'avatar': sierra_card.get('avatar'),
        'custom_avatar_regex': True,
        'lines_parsed': 1,
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Sierra\ Cruz|Sierra)\s*:',
        'npc_info': {
            'first_name': 'Sierra',
            'last_name': 'Cruz',
            'nicknames': ['Sierra'],
            'titles': []
        },
        'content': sierra_card.get('description'),
        'ignored_characters': ['_pnrXbkWqcgmFAf3meRWFY'],
        'ignored_personas': []
    },
    'YCxAqNoShpefVvk0_Pc7i': {
        'name': "Russell 'Russ' Sinclair",
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ["Russell 'Russ' Sinclair", "Russell Sinclair", "Russ Sinclair", "Russ"],
        'key_logic': 'AND_ANY',
        'avatar': russ_card.get('avatar'),
        'custom_avatar_regex': True,
        'lines_parsed': 1,
        'avatar_activation_regex': r"(?:^|\n)\s*(?:Russell\ Sinclair|Russ\ Sinclair|Russell\ 'Russ'|Russell|Russ)\s*:",
        'npc_info': {
            'first_name': 'Russell',
            'last_name': 'Sinclair',
            'nicknames': ['Russ'],
            'titles': []
        },
        'content': russ_card.get('description'),
        'ignored_characters': ['_wn6DkCcg3Xqa2Xpx9ttnT'],
        'ignored_personas': []
    },
    'ekdQjq63xP7HtNuaPQJQE': {
        'name': 'Stanley Davies Jr.',
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ['Stanley Davies Jr.', 'Stan Davies', 'Stan'],
        'key_logic': 'AND_ANY',
        'avatar': stan_card.get('avatar'),
        'custom_avatar_regex': True,
        'lines_parsed': 1,
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Stanley\ Davies\ Jr\.|Stanley\ Davies|Stan\ Davies|Stan)\s*:',
        'npc_info': {
            'first_name': 'Stanley',
            'last_name': 'Davies Jr.',
            'nicknames': ['Stan'],
            'titles': []
        },
        'content': stan_card.get('description'),
        'ignored_characters': ['_Xd3NhKnRJByMTtdb6PjxJ'],
        'ignored_personas': []
    },
    'RM6rcwv8MlY1XWaCTQp0M': {
        'name': 'Jared Thompson',
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ['Jared Thompson', 'J-Man', 'Jared'],
        'key_logic': 'AND_ANY',
        'avatar': jared_card.get('avatar'),
        'custom_avatar_regex': True,
        'lines_parsed': 1,
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Jared\ Thompson|J-Man|Jared)\s*:',
        'npc_info': {
            'first_name': 'Jared',
            'last_name': 'Thompson',
            'nicknames': ['J-Man', 'The Golden Bull'],
            'titles': []
        },
        'content': jared_card.get('description'),
        'ignored_characters': ['_xJVPtBLL3dxy69RLKL9X9'],
        'ignored_personas': []
    },
    'alyssa_world_dossier_2b54a223': {
        'name': 'Alyssa Hvit Douglas Bloodmoon',
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ['Alyssa Douglas', 'Alyssa Hvit', 'Alyssa Douglas-Bloodmoon', 'Alyssa', 'White Moon Alyssa'],
        'key_logic': 'AND_ANY',
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public',
        'custom_avatar_regex': True,
        'lines_parsed': 1,
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Alyssa\ Douglas|Alyssa\ Hvit|White\ Moon|Alyssa)\s*:',
        'npc_info': {
            'first_name': 'Alyssa',
            'last_name': 'Douglas Bloodmoon',
            'nicknames': ['White Moon', 'Lyssa'],
            'titles': []
        },
        'content': alyssa_card.get('description'),
        'ignored_personas': ['persona_1786335754946'],
        'ignored_characters': ['_6exg3yPfe2eCDK4hTftkh']
    },
    'Vcj4h2TL4Usola2A4OOl6': {
        'name': 'Jasper Svartr Douglas Bloodmoon',
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ['Jasper Douglas', 'Jasper Svartr', 'Jasper Douglas-Bloodmoon', 'Jasper', 'Shadow Wolf Jasper'],
        'key_logic': 'AND_ANY',
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/343ac305-0d85-4a8e-2ea6-e76750020800/public',
        'custom_avatar_regex': True,
        'lines_parsed': 1,
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Jasper\ Douglas|Jasper\ Svartr|Shadow\ Wolf|Jasper)\s*:',
        'npc_info': {
            'first_name': 'Jasper',
            'last_name': 'Douglas Bloodmoon',
            'nicknames': ['Shadow Wolf', 'Jasp'],
            'titles': []
        },
        'content': jasper_card.get('description'),
        'ignored_personas': ['1792155173728'],
        'ignored_characters': ['_t4J9aQNJM36cUKAP4wB4U']
    },
    # Approved active cards in Primary:
    'C-JisFj8qA1tsFEqZKevk': {  # Erik
        'ignored_characters': ['_QPea6g4Q1QfeYCVHCLMPR']
    },
    'jDuJtzirlEZC3K_ArIufh': {  # Malachia
        'ignored_characters': ['_RDfz7XzTpM23LpPALVXHM']
    },
    'H2JX-NkHRiJ2FzoekC5ZZ': {  # Noah
        'ignored_characters': ['_zFLUjV8aVxQRAfQxGcAcY']
    },
    'tAcrWLtWSDGf3xJJRwUOM': {  # Logan
        'ignored_characters': ['_T8Ywcr9FEqNf9JxbK6eHP']
    },
    'HhuMluMmIIENUei3bX6ed': {  # Wulfnic
        'ignored_characters': ['_HEQQbbRFwKdG8QE2Fh1z1']
    },
    'BXi3sENAVYB8OKF80Q9Su': {  # Mackenzie
        'ignored_characters': ['_zn24784jfcchQ7EwCyAnm']
    }
}

# Update Primary Lorebook
lb_primary_path = final_dir / 'Svartulfr_NPC_Primary.json'
prim_data = json.loads(lb_primary_path.read_text(encoding='utf-8'))

for arr_name in ['entries', 'lexicon']:
    if arr_name in prim_data:
        for entry in prim_data[arr_name]:
            eid = entry.get('entry_id')
            if eid in primary_updates:
                upd = primary_updates[eid]
                for k, v in upd.items():
                    entry[k] = v

lb_primary_path.write_text(json.dumps(prim_data, indent=2, ensure_ascii=False), encoding='utf-8')
(ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json').write_text(
    json.dumps(prim_data, indent=2, ensure_ascii=False), encoding='utf-8'
)
print("Updated FINAL/Svartulfr_NPC_Primary.json and lorebooks/optimized/Svartulfr_NPC_Primary.json successfully!")

# Update Secondary Lorebook (Edric)
lb_secondary_path = final_dir / 'Svartulfr_NPC_Secondary.json'
sec_data = json.loads(lb_secondary_path.read_text(encoding='utf-8'))
for arr_name in ['entries', 'lexicon']:
    if arr_name in sec_data:
        for entry in sec_data[arr_name]:
            if entry.get('entry_id') == 'h-ttmlgJYeRXqyDvQjSX7':
                entry['ignored_characters'] = ['_TbRM3EdxDjHFgqztTbCpL']

lb_secondary_path.write_text(json.dumps(sec_data, indent=2, ensure_ascii=False), encoding='utf-8')
(ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Secondary.json').write_text(
    json.dumps(sec_data, indent=2, ensure_ascii=False), encoding='utf-8'
)
print("Updated FINAL/Svartulfr_NPC_Secondary.json and lorebooks/optimized/Svartulfr_NPC_Secondary.json successfully!")

# Now deploy Primary Lorebook (_zwEqgEEzh12X6gHVmMKKC) via PUT to Wyvern API
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

base_payload_prim = {
    'name': prim_data.get('name', 'Svartúlfr - NPC Primary'),
    'description': prim_data.get('description', ''),
    'visibility': prim_data.get('visibility', 'private'),
    'rating': prim_data.get('rating', 'explicit'),
    'scan_depth': prim_data.get('scan_depth', 5),
    'token_budget': prim_data.get('token_budget', 5000),
    'recursive_scanning': prim_data.get('recursive_scanning', True),
    'lexicon': prim_data.get('lexicon', [])
}

payload_bytes = json.dumps(base_payload_prim, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
req = urllib.request.Request(
    'https://app.wyvern.chat/api/lorebooks/_zwEqgEEzh12X6gHVmMKKC',
    data=payload_bytes,
    headers=headers,
    method='PUT'
)

with urllib.request.urlopen(req, timeout=90) as resp:
    print(f"PUT Lorebook Primary status: {resp.status}")

# Also deploy Secondary Lorebook (_Uht3Ckz44JBDrPnUHq7LV) via PUT to Wyvern API to persist Edric's ignored_characters
time.sleep(2.5)
base_payload_sec = {
    'name': sec_data.get('name', 'Svartúlfr - NPC Secondary'),
    'description': sec_data.get('description', ''),
    'visibility': sec_data.get('visibility', 'private'),
    'rating': sec_data.get('rating', 'explicit'),
    'scan_depth': sec_data.get('scan_depth', 5),
    'token_budget': sec_data.get('token_budget', 5000),
    'recursive_scanning': sec_data.get('recursive_scanning', True),
    'lexicon': sec_data.get('lexicon', [])
}
payload_bytes_sec = json.dumps(base_payload_sec, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
req_sec = urllib.request.Request(
    'https://app.wyvern.chat/api/lorebooks/_Uht3Ckz44JBDrPnUHq7LV',
    data=payload_bytes_sec,
    headers=headers,
    method='PUT'
)

with urllib.request.urlopen(req_sec, timeout=90) as resp:
    print(f"PUT Lorebook Secondary status: {resp.status}")

print("Task 1 finished successfully!")
