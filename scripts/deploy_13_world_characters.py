"""
Script: scripts/deploy_13_world_characters.py
Objective: Deploy and verify 13 Primary World Characters into World `_YpX47fNraQFw2dD7TdycJ`
           ("Svartúlfr — Blackwood & Solarton") via Wyvern Web API.

Authoritative Characters:
 1. Erik Ulfr Douglas
 2. Logan Járn Douglas
 3. Edric Douglas
 4. Noah Loki Douglas Bloodmoon
 5. Malachia Björn Douglas Bloodmoon
 6. Jasper Svartr Douglas Bloodmoon
 7. Alyssa Hvit Douglas Bloodmoon
 8. Wulfnic Báleygr Bloodmoon
 9. Zefir Hvitskog
10. Mackenzie Sanchez-Rogers
11. Finnegan Novak
12. Sierra Cruz
13. Scarlett Rose
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'
API_BASE = 'https://app.wyvern.chat/api/worlds'

# Ensure refresh_token is accessible
sys.path.append(str(ROOT / 'scratch'))
try:
    import refresh_token
except ImportError:
    refresh_token = None

FINAL_INSTRUCTIONS = (
    "Format discipline: dialogue in quotes, actions and narration in plain text "
    "(no asterisks), asterisks reserved for internal thoughts only. "
    "Never use the em dash; use commas or periods instead."
)

# 13 Character Specifications
CHARACTER_SPECS = [
    {
        'id_key': 'Erik',
        'display_name': 'Erik Ulfr Douglas',
        'first_name': 'Erik',
        'middle_names': ['Cornelius', 'Ulfr'],
        'last_name': 'Douglas',
        'nicknames': ['The Prime Alpha', 'The Patriarch'],
        'titles': ['Alpha', 'Lord'],
        'tags': ['Pureblood', 'Werewolf', 'Alpha', 'DCC', 'Douglas'],
        'keys': ['Erik Douglas', 'Erik Ulfr Douglas', 'Prime Alpha', 'Erik'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/29a667f2-7846-474e-eff4-4dd81d3caf00/public',
        'birthdate': 10009344,
        'start_timeline_position': 10009344,
        'level': 55,
        'stats': {'might': 7, 'resilience': 7, 'agility': 4, 'wit': 5, 'presence': 7, 'scouting': 1},
        'summary': '[NAME: Erik Ulfr Douglas; ROLE: Pack Leader of Seven Hills, Billionaire CEO of Douglas Capital & Construction (DCC), Widower of Nixara Bloodmoon (d. 2005), Prime Alpha Patriarch; SPECIES: Werewolf (Pureblood LSE); AGE: 55; TRAITS: Authoritative, Overprotective, Corporate-Californian Mask, Grief-Driven Apex Predator, Ruthless Businessman, Devoted Father]',
        'display_description': 'Billionaire CEO of DCC and terrifying, overprotective Prime Alpha Patriarch of the Pack of Seven Hills, a grief-driven Apex Predator wearing a sunny Californian mask.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'C-JisFj8qA1tsFEqZKevk')
    },
    {
        'id_key': 'Logan',
        'display_name': 'Logan Járn Douglas',
        'first_name': 'Logan',
        'middle_names': ['Dominic', 'Járn'],
        'last_name': 'Douglas',
        'nicknames': ['Uncle Logan', 'The Peacemaker'],
        'titles': [],
        'tags': ['Pureblood', 'Werewolf', 'Veteran', 'Mechanic', 'Douglas'],
        'keys': ['Logan Douglas', 'Logan Járn Douglas', 'Logan'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/c90b110f-cebf-4223-1007-dec047b78400/public',
        'birthdate': 10054920,
        'start_timeline_position': 10054920,
        'level': 49,
        'stats': {'might': 7, 'resilience': 6, 'agility': 6, 'wit': 4, 'presence': 5, 'scouting': 3},
        'summary': '[NAME: Logan Járn Douglas; ROLE: Custom Garage Owner, Combat Veteran, Enforcer & Peacemaker; SPECIES: Werewolf (Pureblood LSE); AGE: 49; TRAITS: Loyal, Grounded, Protective, Pragmatic, Battle-Hardened, Patient]',
        'display_description': 'Combat veteran, custom motorcycle builder, and steady enforcer brother to Erik, anchoring the Douglas family with quiet strength.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'tAcrWLtWSDGf3xJJRwUOM')
    },
    {
        'id_key': 'Edric',
        'display_name': 'Edric Douglas',
        'first_name': 'Edric',
        'middle_names': [],
        'last_name': 'Douglas',
        'nicknames': ['Ed', 'Pup'],
        'titles': [],
        'tags': ['Werewolf', 'Pup', 'Douglas', 'Scout'],
        'keys': ['Edric Douglas', 'Edric'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public',
        'birthdate': 10371552,
        'start_timeline_position': 10371552,
        'level': 13,
        'stats': {'might': 3, 'resilience': 3, 'agility': 7, 'wit': 5, 'presence': 5, 'scouting': 8},
        'summary': '[NAME: Edric Douglas; ROLE: Youngest Pack Member, High-Speed Scout, Logan\'s Apprentice; SPECIES: Werewolf (Pureblood LSE); AGE: 13; TRAITS: Energetic, Observant, Eager to Prove Himself, Loyal, Fast]',
        'display_description': 'The youngest member of the Douglas pack, sharp-eyed, energetic, and learning the ropes from Logan and his older cousins.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Secondary.json', 'h-ttmlgJYeRXqyDvQjSX7')
    },
    {
        'id_key': 'Noah',
        'display_name': 'Noah Loki Douglas Bloodmoon',
        'first_name': 'Noah',
        'middle_names': ['Loki'],
        'last_name': 'Douglas Bloodmoon',
        'nicknames': ['The Grey Eminence', 'Golden Boy'],
        'titles': [],
        'tags': ['Pureblood', 'Werewolf', 'Politician', 'Delta', 'Douglas', 'Bloodmoon'],
        'keys': ['Noah Douglas', 'Noah Loki', 'Noah Douglas-Bloodmoon', 'Noah'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/469a5f2b-f56e-4925-b9aa-cea58fa25c00/public',
        'birthdate': 10262928,
        'start_timeline_position': 10262928,
        'level': 25,
        'stats': {'might': 6, 'resilience': 6, 'agility': 5, 'wit': 6, 'presence': 6, 'scouting': 2},
        'summary': '[NAME: Noah Loki Douglas Bloodmoon; ROLE: Pack Caretaker, Public Relations & Political Liaison, Second Son; SPECIES: Werewolf (Pureblood LSE); AGE: 25; TRAITS: Diplomatic, Charming, Calculating, Protective, Patient, Elegant]',
        'display_description': 'Second son of Erik, charismatic politician and diplomatic shield for the Pack of Seven Hills, smoothing tensions with poise.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'H2JX-NkHRiJ2FzoekC5ZZ')
    },
    {
        'id_key': 'Malachia',
        'display_name': 'Malachia Björn Douglas Bloodmoon',
        'first_name': 'Malachia',
        'middle_names': ['Björn'],
        'last_name': 'Douglas Bloodmoon',
        'nicknames': ['The Berserker', 'Ghost', 'The King'],
        'titles': ['Alpha'],
        'tags': ['Pureblood', 'Werewolf', 'Alpha', 'Enforcer', 'Douglas', 'Bloodmoon'],
        'keys': ['Malachia Douglas', 'Malachia Björn', 'Malachia Douglas-Bloodmoon', 'Malachia'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/b43869a0-d59a-4074-e99e-726ea2939b00/public',
        'birthdate': 10244064,
        'start_timeline_position': 10244064,
        'level': 28,
        'stats': {'might': 8, 'resilience': 7, 'agility': 5, 'wit': 4, 'presence': 5, 'scouting': 2},
        'summary': '[NAME: Malachia Björn Douglas Bloodmoon; ROLE: Heir to Seven Hills, Underground Fighting Ring Champion, Heavy Vanguard; SPECIES: Werewolf (Pureblood LSE); AGE: 28; TRAITS: Brooding, Lethal, Fiercely Protective, Quiet, Battle-Scarred, Devoted Brother]',
        'display_description': 'Eldest son and heir to Seven Hills, a scarred subterranean fighting champion carrying the physical brunt of pack protection.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'jDuJtzirlEZC3K_ArIufh')
    },
    {
        'id_key': 'Jasper',
        'display_name': 'Jasper Svartr Douglas Bloodmoon',
        'first_name': 'Jasper',
        'middle_names': ['Svartr'],
        'last_name': 'Douglas Bloodmoon',
        'nicknames': ['DJ Frequency', 'Shadow Wolf', 'Jasp'],
        'titles': [],
        'tags': ['Pureblood', 'Werewolf', 'Hacker', 'DJ', 'Twin', 'Douglas', 'Bloodmoon'],
        'keys': ['Jasper Douglas', 'Jasper Svartr', 'Jasper Douglas-Bloodmoon', 'Jasper', 'Shadow Wolf Jasper'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/061fed14-373e-44fb-639a-2a5638a47100/public',
        'birthdate': 10320312,
        'start_timeline_position': 10320312,
        'level': 19,
        'stats': {'might': 4, 'resilience': 3, 'agility': 8, 'wit': 9, 'presence': 3, 'scouting': 4},
        'summary': '[NAME: Jasper Svartr Douglas Bloodmoon; ROLE: Arcane Hacker, Audio Engineer, DJ Frequency, Alyssa\'s Twin; SPECIES: Werewolf (Pureblood LSE); AGE: 19; TRAITS: Brilliant, Restless, Tech-Savvy, Sarcastic, Fiercely Protective Twin]',
        'display_description': 'Alyssa\'s twin brother, an arcane technomancer and DJ balancing underground sound raves with subterranean data-mining.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'Vcj4h2TL4Usola2A4OOl6')
    },
    {
        'id_key': 'Alyssa',
        'display_name': 'Alyssa Hvit Douglas Bloodmoon',
        'first_name': 'Alyssa',
        'middle_names': ['Hvit'],
        'last_name': 'Douglas Bloodmoon',
        'nicknames': ['White Moon', 'Lyssa', 'The Anchor'],
        'titles': [],
        'tags': ['Pureblood', 'Werewolf', 'Healer', 'Pre-Med', 'Twin', 'Douglas', 'Bloodmoon'],
        'keys': ['Alyssa Douglas', 'Alyssa Hvit', 'Alyssa Douglas-Bloodmoon', 'Alyssa', 'White Moon Alyssa'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ba5a7fed-8425-478e-4314-16fb78d58300/public',
        'birthdate': 10320312,
        'start_timeline_position': 10320312,
        'level': 19,
        'stats': {'might': 2, 'resilience': 4, 'agility': 4, 'wit': 7, 'presence': 8, 'scouting': 6},
        'summary': '[NAME: Alyssa Hvit Douglas Bloodmoon; ROLE: Pack Healer, Pre-Med Student at SUCC, Jasper\'s Twin; SPECIES: Werewolf (Pureblood LSE); AGE: 19; TRAITS: Compassionate, Resolute, Gentle, Steadfast Vital Conduit, Devoted Twin]',
        'display_description': 'Jasper\'s twin sister, SUCC Pre-Med student and vital conduit healer whose white moon essence grounds the pack.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'alyssa_world_dossier_2b54a223')
    },
    {
        'id_key': 'Wulfnic',
        'display_name': 'Wulfnic Báleygr Bloodmoon',
        'first_name': 'Wulfnic',
        'middle_names': ['Báleygr'],
        'last_name': 'Bloodmoon',
        'nicknames': ['The First Tusk', 'Primo Zanna', 'The Ancient', 'Alpha of Alphas'],
        'titles': ['Jarl', 'Alpha'],
        'tags': ['Primordial', 'Werewolf', 'God', 'Firstborn', 'Bloodmoon'],
        'keys': ['Wulfnic', 'Wulfnic Bloodmoon', 'Primo Zanna'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/aa836754-29c6-4cd2-2655-2dce65ce2a00/public',
        'birthdate': 0,
        'start_timeline_position': 0,
        'level': 99,
        'stats': {'might': 8, 'resilience': 8, 'agility': 5, 'wit': 3, 'presence': 5, 'scouting': 2},
        'summary': '[NAME: Wulfnic Báleygr Bloodmoon; ROLE: Primordial Apex Sovereign, The First Tusk, Jarl of the Bloodmoon Ancestral Line; SPECIES: Primordial Werewolf / Ancient Deity; AGE: 1200; TRAITS: Colossal, Immovable, Ancient Honor, Absolute Authority, Patient Sovereign]',
        'display_description': 'Ancient Norse sovereign and progenitor of the Bloodmoon lineage, towering at nine feet with unyielding ancestral authority.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'HhuMluMmIIENUei3bX6ed')
    },
    {
        'id_key': 'Zefir',
        'display_name': 'Zefir Hvitskog',
        'first_name': 'Zefir',
        'middle_names': [],
        'last_name': 'Hvitskog',
        'nicknames': ['White Ghost', 'Firstborn'],
        'titles': ['Lord'],
        'tags': ['Primordial', 'Werewolf', 'Enigma', 'Firstborn', 'Hvitskog'],
        'keys': ['Zefir', 'White Ghost', 'Firstborn'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/bdd8961e-a68a-4c6b-b4e1-29a26db37e00/public',
        'birthdate': 176424,
        'start_timeline_position': 176424,
        'level': 99,
        'stats': {'might': 5, 'resilience': 4, 'agility': 9, 'wit': 6, 'presence': 3, 'scouting': 4},
        'summary': '[NAME: Zefir Hvitskog; ROLE: Primordial Scout & Assassin, Left Hand to Wulfnic; SPECIES: Primordial Werewolf / Divine Enigma; AGE: 1176; TRAITS: Quicksilver, Insolent Swagger, Lethal Precision, Glacial Stillness, Bound to Blood]',
        'display_description': 'Ancient Norse scout and silent blade of the Last Three Firstborn, possessing eternal youth, quicksilver speed, and deadly precision.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'aA5zIYvLivjMts978RWEn')
    },
    {
        'id_key': 'Mackenzie',
        'display_name': 'Mackenzie Sanchez-Rogers',
        'first_name': 'Mackenzie',
        'middle_names': [],
        'last_name': 'Sanchez-Rogers',
        'nicknames': ['Mac'],
        'titles': [],
        'tags': ['Werewolf', 'Brawler', 'Street', 'Sanchez-Rogers'],
        'keys': ['Mackenzie Sanchez-Rogers', 'Mackenzie Rogers', 'Mac Rogers', 'Mackenzie'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public',
        'birthdate': 10316496,
        'start_timeline_position': 10316496,
        'level': 19,
        'stats': {'might': 8, 'resilience': 7, 'agility': 7, 'wit': 3, 'presence': 3, 'scouting': 3},
        'summary': '[NAME: Mackenzie Sanchez-Rogers; ROLE: Underground Street Brawler, Solarton Tough, Pre-Law Student; SPECIES: Werewolf (LSE); AGE: 19; TRAITS: Fierce, Loyal, Direct, Uncompromising, Heavy-Hitter, Protective]',
        'display_description': 'Fierce Solarton street brawler and SUCC student, combining explosive physical aggression with fierce loyalty to her friends.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'BXi3sENAVYB8OKF80Q9Su')
    },
    {
        'id_key': 'Finn',
        'display_name': 'Finnegan Novak',
        'first_name': 'Finnegan',
        'middle_names': [],
        'last_name': 'Novak',
        'nicknames': ['Finn'],
        'titles': [],
        'tags': ['Demi-Human', 'Kemonomimi', 'Arctic Wolf', 'Varsity Hockey', 'SUCC'],
        'keys': ['Finnegan', 'Finn', 'Novak', 'Alpha Rho Omega', 'SUCC Bears'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/75456c02-dddc-4879-7822-ab7c4628f600/public',
        'birthdate': 10317984,
        'start_timeline_position': 10317984,
        'level': 19,
        'stats': {'might': 6, 'resilience': 6, 'agility': 8, 'wit': 3, 'presence': 4, 'scouting': 4},
        'summary': '[NAME: Finnegan Novak; ROLE: SUCC Bears Hockey Left Wing, Sports Medicine Student, Alpha Rho Omega Frat Member; SPECIES: Demi-Human Arctic Wolf (Kemonomimi); AGE: 19; TRAITS: Affectionate, High-Speed Athlete, Loyal Friend, Clean-Shaven, Protective]',
        'display_description': 'Kemonomimi Arctic Wolf left wing for the SUCC Bears hockey team, high-velocity skater and fiercely devoted childhood friend.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'EprHlMVM1g7vAhqUI-VUQ')
    },
    {
        'id_key': 'Sierra',
        'display_name': 'Sierra Cruz',
        'first_name': 'Sierra',
        'middle_names': [],
        'last_name': 'Cruz',
        'nicknames': [],
        'titles': [],
        'tags': ['Demi-Human', 'Lamia', 'Pre-Med', 'SUCC', 'Female'],
        'keys': ['Sierra Cruz', 'Sierra'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d27bf63b-2b8b-4dda-5554-72b32ac60b00/public',
        'birthdate': 10323648,
        'start_timeline_position': 10323648,
        'level': 18,
        'stats': {'might': 7, 'resilience': 6, 'agility': 3, 'wit': 8, 'presence': 3, 'scouting': 4},
        'summary': '[NAME: Sierra Cruz; ROLE: Pre-Med Scholar, Lamia Constrictor, Alyssa\'s SUCC Roommate; SPECIES: Demi-Human Lamia (Rainbow Iridescent Serpent Body, Zero Legs); AGE: 18; TRAITS: Academic, Pragmatic, Inquisitive, Seductive, Constrictor Strength]',
        'display_description': 'Iridescent rainbow lamia scholar and Alyssa\'s campus roommate, moving on coils with scholarly poise and crushing constrictor power.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', 'ijy8vrlphNv19-p-gbYuY')
    },
    {
        'id_key': 'Scarlett',
        'display_name': 'Scarlett Rose',
        'first_name': 'Scarlett',
        'middle_names': [],
        'last_name': 'Rose',
        'nicknames': ['Red'],
        'titles': [],
        'tags': ['Succubus', 'Socialite', 'SUCC', 'Theta Iota Theta', 'Female'],
        'keys': ['Scarlett Rose', 'Scarlett'],
        'avatar': 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/e96d176a-47e4-4829-2af4-7cd6ae239100/public',
        'birthdate': 10307808,
        'start_timeline_position': 10307808,
        'level': 20,
        'stats': {'might': 2, 'resilience': 3, 'agility': 6, 'wit': 6, 'presence': 9, 'scouting': 5},
        'summary': '[NAME: Scarlett Rose; ROLE: Theta Iota Theta Sorority President, Glamour Specialist, Alyssa\'s Best Friend; SPECIES: Succubus (Candy-Pink Hair, Scarlet Horns, Leathery Wings); AGE: 20; TRAITS: Radiant, Glamorous, Social Maven, Protective Best Friend, Magnetic]',
        'display_description': 'Candy-pink haired succubus with scarlet horns, Theta Iota Theta president, and fiercely loyal social coordinator at SUCC.',
        'lorebook_source': ('FINAL/Svartulfr_NPC_Primary.json', '4NzXF4_0hYxmN7Idltzpw')
    }
]

def get_auth_token():
    token_path = ROOT / 'scratch' / 'wyvern_token.txt'
    if token_path.exists():
        token = token_path.read_text(encoding='utf-8').strip()
        if token:
            return token
    if refresh_token:
        return refresh_token.refresh()
    raise RuntimeError("No auth token available in scratch/wyvern_token.txt")

def load_canonical_content(relative_path, entry_id):
    full_path = ROOT / relative_path
    with open(full_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for entry in data.get('lexicon', []):
        if entry.get('entry_id') == entry_id:
            return entry.get('content', '')
    raise ValueError(f"Entry {entry_id} not found in {relative_path}")

def build_payload(spec):
    source_file, entry_id = spec['lorebook_source']
    content = load_canonical_content(source_file, entry_id)
    
    st = spec['stats']
    base_stats = {
        'stat_1': st['might'],
        'stat_2': st['resilience'],
        'stat_3': st['agility'],
        'stat_4': st['wit'],
        'stat_5': st['presence'],
        'stat_6': st['scouting'],
        'might': st['might'],
        'resilience': st['resilience'],
        'agility': st['agility'],
        'wit': st['wit'],
        'presence': st['presence'],
        'scouting': st['scouting']
    }
    
    payload = {
        'world_id': TARGET_WORLD_ID,
        'name': spec['display_name'],
        'display_name': spec['display_name'],
        'first_name': spec['first_name'],
        'middle_names': spec['middle_names'],
        'last_name': spec['last_name'],
        'nicknames': spec['nicknames'],
        'titles': spec['titles'],
        'tags': spec['tags'],
        'avatar': spec['avatar'],
        'birthdate': spec['birthdate'],
        'start_timeline_position': spec['start_timeline_position'],
        'is_global': True,
        'world_only': False,
        'keys': spec['keys'],
        'key_logic': 'AND_ANY',
        'whole_words_only': True,
        'display_description': spec['display_description'],
        'summary': spec['summary'],
        'long_summary': content,
        'final_instructions': FINAL_INSTRUCTIONS,
        'rpg_stats': {
            'enabled': True,
            'level': spec['level'],
            'species_id': None,
            'occupation_id': None,
            'base_stats': base_stats
        }
    }
    return payload

def fetch_existing_world_characters(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    url = f"{API_BASE}/characters/world/{TARGET_WORLD_ID}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def deploy_characters():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    
    print(f"[*] Querying existing characters in World {TARGET_WORLD_ID}...")
    existing = fetch_existing_world_characters(token)
    print(f"[*] Found {len(existing)} existing characters in World.")
    
    existing_by_name = {c.get('display_name'): c for c in existing}
    
    deployed_records = []
    
    for idx, spec in enumerate(CHARACTER_SPECS, 1):
        name = spec['display_name']
        payload = build_payload(spec)
        existing_char = existing_by_name.get(name)
        
        # Verify stats sum
        stats_sum = sum(spec['stats'].values())
        assert stats_sum == 31, f"Error: {name} stats sum {stats_sum} != 31"
        
        if existing_char:
            cid = existing_char.get('_id') or existing_char.get('id')
            print(f"[{idx}/13] Updating existing character: {name} ({cid})...")
            put_url = f"{API_BASE}/characters/{cid}"
            req = urllib.request.Request(put_url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                print(f"      -> Updated successfully (HTTP {resp.status}). ID: {cid}")
                deployed_records.append(res)
        else:
            print(f"[{idx}/13] Creating new character: {name}...")
            post_url = f"{API_BASE}/characters"
            req = urllib.request.Request(post_url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                cid = res.get('_id') or res.get('id')
                print(f"      -> Created successfully (HTTP {resp.status}). ID: {cid}")
                deployed_records.append(res)
                
        time.sleep(0.5)

    print("\n[*] Deployment run completed. Starting verification...")
    verify_deployment()

def verify_deployment():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    
    url = f"{API_BASE}/characters/world/{TARGET_WORLD_ID}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        chars = json.loads(resp.read().decode('utf-8'))
        
    print(f"\n=======================================================")
    print(f"LIVE VERIFICATION: World {TARGET_WORLD_ID}")
    print(f"Total Characters Returned: {len(chars)} / 13 Expected")
    print(f"=======================================================")
    
    spec_by_name = {s['display_name']: s for s in CHARACTER_SPECS}
    chars_by_name = {c.get('display_name'): c for c in chars}
    
    all_passed = True
    verified_dump = []
    
    for s in CHARACTER_SPECS:
        name = s['display_name']
        c = chars_by_name.get(name)
        if not c:
            print(f"[FAIL] Missing character from world: {name}")
            all_passed = False
            continue
            
        cid = c.get('_id') or c.get('id')
        bdate = c.get('birthdate')
        tl_pos = c.get('start_timeline_position')
        avatar = c.get('avatar')
        rpg = c.get('rpg_stats') or {}
        level = rpg.get('level')
        base_stats = rpg.get('base_stats') or {}
        
        # Stat checks
        expected_stats = s['stats']
        might = base_stats.get('might', base_stats.get('stat_1'))
        resil = base_stats.get('resilience', base_stats.get('stat_2'))
        agil = base_stats.get('agility', base_stats.get('stat_3'))
        wit = base_stats.get('wit', base_stats.get('stat_4'))
        pres = base_stats.get('presence', base_stats.get('stat_5'))
        scout = base_stats.get('scouting', base_stats.get('stat_6'))
        
        stat_sum = sum([might, resil, agil, wit, pres, scout])
        
        bdate_ok = (bdate == s['birthdate'])
        tl_ok = (tl_pos == s['start_timeline_position'])
        avatar_ok = (avatar == s['avatar'])
        level_ok = (level == s['level'])
        sum_ok = (stat_sum == 31)
        dual_key_ok = ('stat_1' in base_stats and 'might' in base_stats)
        
        # Summary & JED+ checks
        long_sum = c.get('long_summary') or ''
        em_count = long_sum.count('\u2014')
        has_bracket = long_sum.startswith('[NAME:')
        has_backstory = ('BACKSTORY:' in long_sum)
        has_voice = ('VOICE & BEHAVIOR:' in long_sum or 'VOICE AND BEHAVIOR:' in long_sum)
        jed_ok = (has_bracket and has_backstory and has_voice and em_count == 0)
        
        char_passed = (bdate_ok and tl_ok and avatar_ok and level_ok and sum_ok and dual_key_ok and jed_ok)
        if not char_passed:
            all_passed = False
            status_str = "FAIL"
        else:
            status_str = "PASS"
            
        print(f"[{status_str}] {name:32} | ID: {cid:22} | Lv: {level:2} | Stats: M{might} R{resil} A{agil} W{wit} P{pres} S{scout} (Sum={stat_sum}) | BDate: {bdate:8} | JED+ Len: {len(long_sum):5}")
        
        verified_dump.append({
            'name': name,
            'id': cid,
            'birthdate': bdate,
            'start_timeline_position': tl_pos,
            'avatar': avatar,
            'level': level,
            'base_stats': base_stats,
            'stat_sum': stat_sum,
            'long_summary_len': len(long_sum),
            'verified_status': status_str
        })
        
    # Save verification snapshot
    snap_path = ROOT / 'scratch' / 'm1_13_world_characters_verified.json'
    with open(snap_path, 'w', encoding='utf-8') as sf:
        json.dump(verified_dump, sf, indent=2, ensure_ascii=False)
    print(f"\n[*] Saved verification snapshot to {snap_path}")
    
    if all_passed and len(chars) == 13:
        print("\n[SUCCESS] ALL 13 PRIMARY WORLD CHARACTERS VERIFIED LIVE WITH 100% PASS RATE!")
        return 0
    else:
        print(f"\n[ERROR] Verification failed. Total characters: {len(chars)}/13. All passed: {all_passed}")
        return 1

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--verify-only':
        sys.exit(verify_deployment())
    else:
        deploy_characters()
