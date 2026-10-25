import json
import pathlib
import copy

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
final_dir = ROOT / 'FINAL'

lb_path = final_dir / 'Svartulfr_NPC_Primary.json'
lb_data = json.loads(lb_path.read_text(encoding='utf-8'))
entries = copy.deepcopy(lb_data.get('lexicon', lb_data.get('entries', [])))

scarlett_card = json.loads((final_dir / 'Scarlett_Rose_card.json').read_text(encoding='utf-8'))
sierra_card = json.loads((final_dir / 'Sierra_Cruz_card.json').read_text(encoding='utf-8'))
russ_card = json.loads((final_dir / 'Russ_card.json').read_text(encoding='utf-8'))
stan_card = json.loads((final_dir / 'Stan_Davies_Jr_card.json').read_text(encoding='utf-8'))
jared_card = json.loads((final_dir / 'Jared_Thompson_card.json').read_text(encoding='utf-8'))
alyssa_card = json.loads((final_dir / 'Alyssa_Douglas_Bloodmoon_card.json').read_text(encoding='utf-8'))

# Test updating entries
updates = {
    '4NzXF4_0hYxmN7Idltzpw': {
        'name': 'Scarlett Rose',
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ['Scarlett Rose', 'Scarlett'],
        'key_logic': 'AND_ANY',
        'avatar': scarlett_card.get('avatar'),
        'custom_avatar_regex': True,
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Scarlett\ Rose|Scarlett)\s*:',
        'lines_parsed': 1,
        'npc_info': {
            'first_name': 'Scarlett',
            'last_name': 'Rose',
            'nicknames': ['Scarlett'],
            'titles': []
        },
        'content': scarlett_card.get('description')
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
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Sierra\ Cruz|Sierra)\s*:',
        'lines_parsed': 1,
        'npc_info': {
            'first_name': 'Sierra',
            'last_name': 'Cruz',
            'nicknames': ['Sierra'],
            'titles': []
        },
        'content': sierra_card.get('description')
    },
    'YCxAqNoShpefVvk0_Pc7i': {
        'name': "Russell 'Russ' Sinclair",
        'type': 'npc',
        'selective': False,
        'secondary_keys': [],
        'keys': ["Russell 'Russ' Sinclair", 'Russell Sinclair', 'Russ Sinclair', 'Russ'],
        'key_logic': 'AND_ANY',
        'avatar': russ_card.get('avatar'),
        'custom_avatar_regex': True,
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Russell\ Sinclair|Russ\ Sinclair|Russell\ \'Russ\'|Russell|Russ)\s*:',
        'lines_parsed': 1,
        'npc_info': {
            'first_name': 'Russell',
            'last_name': 'Sinclair',
            'nicknames': ['Russ'],
            'titles': []
        },
        'content': russ_card.get('description')
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
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Stanley\ Davies\ Jr\.|Stanley\ Davies|Stan\ Davies|Stan)\s*:',
        'lines_parsed': 1,
        'npc_info': {
            'first_name': 'Stanley',
            'last_name': 'Davies Jr.',
            'nicknames': ['Stan'],
            'titles': []
        },
        'content': stan_card.get('description')
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
        'avatar_activation_regex': r'(?:^|\n)\s*(?:Jared\ Thompson|J-Man|Jared)\s*:',
        'lines_parsed': 1,
        'npc_info': {
            'first_name': 'Jared',
            'last_name': 'Thompson',
            'nicknames': ['J-Man', 'The Golden Bull'],
            'titles': []
        },
        'content': jared_card.get('description')
    },
    'alyssa_world_dossier_2b54a223': {
        'name': 'Alyssa Hvit Douglas Bloodmoon',
        'type': 'lore/concept',
        'selective': True,
        'secondary_keys': ['Dossier', 'Scheda', 'Archivio', 'Database', 'Profilo'],
        'keys': ['Alyssa Douglas', 'Alyssa Hvit', 'Alyssa Douglas-Bloodmoon', 'White Moon Alyssa'],
        'key_logic': 'AND_ANY',
        'avatar': alyssa_card.get('avatar'),
        'content': alyssa_card.get('description')
    }
}

applied_count = 0
for e in entries:
    eid = e.get('entry_id')
    if eid in updates:
        u = updates[eid]
        for k, v in u.items():
            e[k] = v
        applied_count += 1
        print(f"Applied update to: {e.get('name')} (id: {eid}) -> content len: {len(e.get('content'))}")

print(f"\nTotal entries updated: {applied_count}/6")
print(f"Total entries in lorebook: {len(entries)}")
