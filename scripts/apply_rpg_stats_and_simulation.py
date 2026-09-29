import urllib.request
import json
import os
import sys
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

CHARACTERS_RPG_CONFIG = [
    # --- G1 MAIN CAST (17) ---
    {
        'id': '_MXcEC8Y6B3BNm3b1ttHj6',
        'name': 'Alyssa Douglas Bloodmoon',
        'level': 19,
        'species': 'Werewolf (Founding Bloodline)',
        'occupation': 'Field Medic / Healing Mage',
        'stats': {'stat_1': 2, 'stat_2': 4, 'stat_3': 4, 'stat_4': 7, 'stat_5': 8, 'stat_6': 6},
        'traits': ['Pacifist Healer', 'Dominant Omega', 'White Moon Anchor', 'Medical Mage'],
        'inventory': [
            {'lexicon_entry_id': '_B3Y9cAUxJNbx266Ph1hCX', 'quantity': 1}, # Alyssa's Field Bag
            {'lexicon_entry_id': '_4XxeUWQBrBUJxH6JjQtNq', 'quantity': 1}, # Emergency Medallion
            {'lexicon_entry_id': '_GNAP7tw8UWry76Dww36FR', 'quantity': 1}  # SR3S Guild Pass
        ]
    },
    {
        'id': '_x3VY2kcbaDbKyCqywGeET',
        'name': 'Jasper Douglas Bloodmoon',
        'level': 19,
        'species': 'Werewolf (Founding Bloodline)',
        'occupation': 'Arcane Rogue / Spell-Hacker',
        'stats': {'stat_1': 4, 'stat_2': 3, 'stat_3': 8, 'stat_4': 9, 'stat_5': 3, 'stat_6': 4},
        'traits': ['Arcane Netrunner', 'Leyline Slicer', 'Twin Shadow', 'Abyssal Magic Apprentice'],
        'inventory': [
            {'lexicon_entry_id': '_746G8T2RVL2tRExw337cq', 'quantity': 1}, # Dragon Glass Katana
            {'lexicon_entry_id': '_8WaPQUH42VgQz2xVXaJF7', 'quantity': 1}, # Abyssal Armor and Twin Daggers
            {'lexicon_entry_id': '_GNAP7tw8UWry76Dww36FR', 'quantity': 1}  # SR3S Guild Pass
        ]
    },
    {
        'id': '_rAcN9GXD1Le4WxY28e49W',
        'name': 'Malachia Douglas Bloodmoon',
        'level': 25,
        'species': 'Werewolf (Founding Bloodline Alpha)',
        'occupation': 'Vanguard Commander / Guardian',
        'stats': {'stat_1': 8, 'stat_2': 7, 'stat_3': 5, 'stat_4': 4, 'stat_5': 5, 'stat_6': 2},
        'traits': ['Vanguard Commander', 'Founding Bloodline Alpha', 'Heavy Greatsword Master', 'Unflinching Guardian'],
        'inventory': [
            {'lexicon_entry_id': '_GNAP7tw8UWry76Dww36FR', 'quantity': 1}  # SR3S Guild Pass
        ]
    },
    {
        'id': '_r42cVzMjcGTAx7bR1DQVt',
        'name': 'Noah Douglas Bloodmoon',
        'level': 22,
        'species': 'Werewolf (Founding Bloodline Alpha)',
        'occupation': 'Security Commander / Pack Enforcer',
        'stats': {'stat_1': 6, 'stat_2': 6, 'stat_3': 5, 'stat_4': 6, 'stat_5': 6, 'stat_6': 2},
        'traits': ['Security Chief', 'Founding Bloodline Alpha', 'Surveillance Strategist', 'Pack Enforcer'],
        'inventory': []
    },
    {
        'id': '_d44gDc8N18kkbEhAcfUCG',
        'name': 'Erik Douglas',
        'level': 52,
        'species': 'Werewolf (Founding Bloodline Patriarch)',
        'occupation': 'War Veteran / Clan Patriarch',
        'stats': {'stat_1': 7, 'stat_2': 7, 'stat_3': 4, 'stat_4': 5, 'stat_5': 7, 'stat_6': 1},
        'traits': ['Clan Patriarch', 'Founding Alpha', 'War Veteran', 'Villa Douglas Lord'],
        'inventory': []
    },
    {
        'id': '_JL37wK9PQMNDChULCDrWj',
        'name': 'Logan Douglas',
        'level': 49,
        'species': 'Werewolf (Founding Bloodline)',
        'occupation': 'Combat Specialist / Biker Uncle',
        'stats': {'stat_1': 7, 'stat_2': 6, 'stat_3': 6, 'stat_4': 4, 'stat_5': 5, 'stat_6': 3},
        'traits': ['Combat Specialist', 'Founding Werewolf', 'Verve Veteran', 'Protective Uncle'],
        'inventory': []
    },
    {
        'id': '_YJQ4cjdrT7brm7HWVkf3K',
        'name': 'Edric Douglas',
        'level': 12,
        'species': 'Werewolf (Founding Bloodline Pup)',
        'occupation': 'Student Apprentice / Minor Pup',
        'stats': {'stat_1': 3, 'stat_2': 3, 'stat_3': 7, 'stat_4': 5, 'stat_5': 5, 'stat_6': 8},
        'traits': ['Pack Pup', 'Innocent Apprentice', 'Quick Reflexes', 'High Spirit'],
        'inventory': []
    },
    {
        'id': '_rJKYcCt61hQa8XRamHEdM',
        'name': 'Lord Cornelius Douglas',
        'level': 86,
        'species': 'Werewolf (Elder Patriarch)',
        'occupation': 'High Diplomat / Aristocrat',
        'stats': {'stat_1': 3, 'stat_2': 4, 'stat_3': 3, 'stat_4': 8, 'stat_5': 9, 'stat_6': 4},
        'traits': ['High Diplomat', 'Douglas Elder', 'Political Mastermind', 'Aristocratic Presence'],
        'inventory': []
    },
    {
        'id': '_jeJTbxLcrYWXNWYPDx4ph',
        'name': 'Magnus Douglas III',
        'level': 99,
        'species': 'Werewolf (Pureblood Elder)',
        'occupation': 'High Chancellor',
        'stats': {'stat_1': 5, 'stat_2': 5, 'stat_3': 4, 'stat_4': 8, 'stat_5': 7, 'stat_6': 2},
        'traits': ['High Chancellor', 'Pureblood Patriarch', 'Strict Traditionalist', 'Guild Arbiter'],
        'inventory': []
    },
    {
        'id': '_EwPN1te7qtUKYEx4NLgag',
        'name': 'Elizabeth Duskwood',
        'level': 48,
        'species': 'Werewolf (Pureblood Matriarch)',
        'occupation': 'Pack Mom / High Healer',
        'stats': {'stat_1': 3, 'stat_2': 5, 'stat_3': 4, 'stat_4': 7, 'stat_5': 8, 'stat_6': 4},
        'traits': ['Pack Mom', 'Pureblood Matriarch', 'Master Herbalist', 'Compound Caretaker'],
        'inventory': []
    },
    {
        'id': '_W9PLYt9ERTBJBXqKQL2en',
        'name': 'Wulfnic Bloodmoon',
        'level': 99,
        'species': 'Werewolf (Divine Blood Firstborn)',
        'occupation': 'Divine Warlord / Fenris Consacrated',
        'stats': {'stat_1': 8, 'stat_2': 8, 'stat_3': 5, 'stat_4': 3, 'stat_5': 5, 'stat_6': 2},
        'traits': ['Divine Blood Firstborn', 'Fenris Consacrated', 'Ancient Warlord', 'Pack Sovereign'],
        'inventory': []
    },
    {
        'id': '_NYtBzeKNkm3pedHMnYaka',
        'name': 'Ut Berg',
        'level': 99,
        'species': 'Werewolf (Divine Blood Firstborn)',
        'occupation': 'Berserker / Divine Champion',
        'stats': {'stat_1': 9, 'stat_2': 8, 'stat_3': 5, 'stat_4': 2, 'stat_5': 4, 'stat_6': 3},
        'traits': ['Divine Blood Firstborn', 'Fenris Champion', 'Immovable Berserker', 'Unstoppable Might'],
        'inventory': [
            {'lexicon_entry_id': '_XNkgRjKF6XRnKqgJjkUR3', 'quantity': 1} # Ut's Warhammer
        ]
    },
    {
        'id': '_FJhtBq4xUM4aUWpaJAPYF',
        'name': 'Zefir Hvitskog',
        'level': 99,
        'species': 'Werewolf (Divine Blood Firstborn)',
        'occupation': 'Shadow Stalker / Divine Scout',
        'stats': {'stat_1': 5, 'stat_2': 4, 'stat_3': 9, 'stat_4': 6, 'stat_5': 3, 'stat_6': 4},
        'traits': ['Divine Blood Firstborn', 'Fenris Scout', 'Silent Shadow', 'Ancient Tracker'],
        'inventory': [
            {'lexicon_entry_id': '_xbjVJJ3aNC4W9Uz4nNn4d', 'quantity': 1} # Zefir's Blade
        ]
    },
    {
        'id': '_wpMTPQ2VVA2pWqJ3cMztJ',
        'name': 'Fenris',
        'level': 99,
        'species': 'Divine Deity (Wolf God)',
        'occupation': 'Primordial Deity / Wolf God',
        'stats': {'stat_1': 8, 'stat_2': 7, 'stat_3': 5, 'stat_4': 3, 'stat_5': 4, 'stat_6': 4},
        'traits': ['Primordial Wolf God', 'Divine Originator', 'Patron of the Nine', 'Cosmic Lycanthrope'],
        'inventory': []
    },
    {
        'id': '_fmzBDjDn3Gnq2hXKy7tY6',
        'name': 'Nixara Bloodmoon',
        'level': 35,
        'species': 'Werewolf (Founding Bloodline)',
        'occupation': 'Dragonblade Matriarch',
        'stats': {'stat_1': 6, 'stat_2': 5, 'stat_3': 7, 'stat_4': 6, 'stat_5': 5, 'stat_6': 2},
        'traits': ['Dragon Glass Katana Master', 'Founding Matriarch', 'Fierce Mother', 'Blade Sovereign'],
        'inventory': []
    },
    {
        'id': '_b7QqV43D8pU1tewx4qenY',
        'name': 'Kaladin Nargathon',
        'level': 99,
        'species': 'Cyber-Werewolf',
        'occupation': 'Tactical Cyber-Commander',
        'stats': {'stat_1': 8, 'stat_2': 8, 'stat_3': 6, 'stat_4': 5, 'stat_5': 3, 'stat_6': 1},
        'traits': ['Project BlackWolf Veteran', 'Cyber-Werewolf', 'Heavy Military Augmentations', 'Tactical Sentinel'],
        'inventory': []
    },
    {
        'id': '_PCC1PLfcGrdw2VfMnhVcL',
        'name': 'Marcus Thornfield',
        'level': 99,
        'species': 'Cyber-Werewolf',
        'occupation': 'Heavy Cyber-Enforcer',
        'stats': {'stat_1': 9, 'stat_2': 8, 'stat_3': 5, 'stat_4': 4, 'stat_5': 3, 'stat_6': 2},
        'traits': ['Project BlackWolf Veteran', 'Cyber-Werewolf', 'Subdermal Titanium Armor', 'Breaching Specialist'],
        'inventory': []
    },

    # --- G2 GUILD CAST (5) ---
    {
        'id': '_4bazKCAbPMmc19HzHAphC',
        'name': 'Radek',
        'level': 26,
        'species': 'Werewolf',
        'occupation': 'Team Ukiyo Leader / Vanguard',
        'stats': {'stat_1': 7, 'stat_2': 6, 'stat_3': 7, 'stat_4': 5, 'stat_5': 4, 'stat_6': 2},
        'traits': ['Team Ukiyo Leader', 'Urban Scout', 'Dungeon Diver', 'Werewolf Vanguard'],
        'inventory': [
            {'lexicon_entry_id': '_GNAP7tw8UWry76Dww36FR', 'quantity': 1}  # SR3S Guild Pass
        ]
    },
    {
        'id': '_JQGgmwyA3qRaTLWck3GjX',
        'name': 'Goran',
        'level': 31,
        'species': 'Minotaur',
        'occupation': 'Team Ukiyo Tank / Heavy Sledge',
        'stats': {'stat_1': 9, 'stat_2': 8, 'stat_3': 4, 'stat_4': 3, 'stat_5': 5, 'stat_6': 2},
        'traits': ['Team Ukiyo Tank', 'Minotaur Sledge', 'Unbreakable Wall', 'Heavy Breacher'],
        'inventory': [
            {'lexicon_entry_id': '_GNAP7tw8UWry76Dww36FR', 'quantity': 1}  # SR3S Guild Pass
        ]
    },
    {
        'id': '_kc7TyfPDQwUALKXcmTMxQ',
        'name': 'Kian',
        'level': 23,
        'species': 'Half-Elf',
        'occupation': 'Team Ukiyo Infiltrator / DPS',
        'stats': {'stat_1': 3, 'stat_2': 3, 'stat_3': 9, 'stat_4': 8, 'stat_5': 4, 'stat_6': 4},
        'traits': ['Team Ukiyo DPS', 'Half-Elf Scout', 'Arcane Trapsmith', 'Prismatic Slicer'],
        'inventory': [
            {'lexicon_entry_id': '_GNAP7tw8UWry76Dww36FR', 'quantity': 1}  # SR3S Guild Pass
        ]
    },
    {
        'id': '_LEeEzdCCyGjQ8kfVkcra8',
        'name': 'Barrow',
        'level': 42,
        'species': 'Minotaur',
        'occupation': 'Master Builder / Retired Nomad Guardian',
        'stats': {'stat_1': 8, 'stat_2': 8, 'stat_3': 3, 'stat_4': 4, 'stat_5': 6, 'stat_6': 2},
        'traits': ['Master Builder', 'Demi-human Representative', 'The Horns Guardian', 'Ironhorn Nomad Veteran'],
        'inventory': []
    },
    {
        'id': '_cDx2yGNtVbCCDUCHcUUxG',
        'name': 'Marek',
        'level': 34,
        'species': 'Oni',
        'occupation': 'Frontline Brawler / Ironhorn Nomad Biker',
        'stats': {'stat_1': 8, 'stat_2': 7, 'stat_3': 6, 'stat_4': 3, 'stat_5': 5, 'stat_6': 2},
        'traits': ['Ironhorn Nomad Enforcer', 'Red Oni Brawler', 'Heavy Chopper Rider', 'Pool Party Host'],
        'inventory': []
    }
]

def apply_all():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    
    snapshot_dir = os.path.join('scratch', 'rpg_snapshots')
    os.makedirs(snapshot_dir, exist_ok=True)
    
    print(f"Starting RPG Stats application for {len(CHARACTERS_RPG_CONFIG)} characters...")
    
    results = []
    
    for cfg in CHARACTERS_RPG_CONFIG:
        cid = cfg['id']
        name = cfg['name']
        c_url = f'https://app.wyvern.chat/api/worlds/characters/{cid}'
        
        # 1. Snapshot previous state
        try:
            req = urllib.request.Request(c_url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                prev_data = json.loads(resp.read().decode('utf-8'))
            snap_file = os.path.join(snapshot_dir, f'{name.replace(" ", "_")}_{cid}.json')
            with open(snap_file, 'w', encoding='utf-8') as sf:
                json.dump(prev_data, sf, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error fetching snapshot for {name} ({cid}): {e}")
            continue

        # 2. Build partial payload
        st = cfg['stats']
        total_stat = sum(st.values())
        assert total_stat == 31, f"Stat sum for {name} is {total_stat}, must be 31!"
        
        rpg_block = {
            'enabled': True,
            'level': cfg['level'],
            'experience': 0,
            'species_id': cfg['species'],
            'occupation_id': cfg['occupation'],
            'base_stats': {
                'stat_1': st['stat_1'],
                'stat_2': st['stat_2'],
                'stat_3': st['stat_3'],
                'stat_4': st['stat_4'],
                'stat_5': st['stat_5'],
                'stat_6': st['stat_6'],
                'strength': st['stat_1'],
                'endurance': st['stat_2'],
                'agility': st['stat_3'],
                'intelligence': st['stat_4'],
                'charisma': st['stat_5'],
                'luck': st['stat_6'],
                'perception': st['stat_6']
            }
        }
        
        payload = {
            'rpg_stats': rpg_block,
            'character_traits': cfg['traits']
        }
        if cfg['inventory']:
            payload['default_inventory'] = cfg['inventory']
            
        # 3. PUT partial update
        try:
            put_req = urllib.request.Request(
                c_url,
                data=json.dumps(payload).encode('utf-8'),
                headers={**headers, 'Content-Type': 'application/json'},
                method='PUT'
            )
            with urllib.request.urlopen(put_req) as resp:
                put_status = resp.status
        except urllib.error.HTTPError as e:
            print(f"FAILED PUT for {name} ({cid}): {e.code} - {e.read().decode('utf-8', errors='ignore')}")
            continue
        except Exception as e:
            print(f"ERROR PUT for {name} ({cid}): {e}")
            continue
            
        # 4. GET verify
        try:
            ver_req = urllib.request.Request(c_url, headers=headers)
            with urllib.request.urlopen(ver_req) as resp:
                ver_data = json.loads(resp.read().decode('utf-8'))
            ver_rpg = ver_data.get('rpg_stats')
            ver_traits = ver_data.get('character_traits')
            ver_inv = ver_data.get('default_inventory')
            
            success = (
                ver_rpg is not None
                and ver_rpg.get('level') == cfg['level']
                and ver_rpg.get('species_id') == cfg['species']
                and ver_rpg.get('occupation_id') == cfg['occupation']
            )
            print(f"[{'OK' if success else 'FAIL'}] {name:30} | Lv {cfg['level']:2} | {cfg['species'][:20]:20} | Stats Sum: {total_stat} | Traits: {len(ver_traits or [])} | Inv: {len(ver_inv or [])}")
            results.append((name, cid, success))
        except Exception as e:
            print(f"Verification error for {name}: {e}")
            
    print(f"\nCompleted RPG Stats application! Successfully verified: {sum(1 for _, _, s in results if s)} / {len(CHARACTERS_RPG_CONFIG)}")

if __name__ == '__main__':
    apply_all()
