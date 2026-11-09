import json
import urllib.request
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRATCH = ROOT / 'scratch'
FINAL = ROOT / 'FINAL'

TOKEN = (SCRATCH / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

EQUIPMENT_EFFECTS = {
    "_FrLpFaULBEUrM1EnkYfUY": { # Wireless Earbuds (trinket)
        "name": "Wireless Earbuds",
        "statModifiers": {"perception": 1}
    },
    "_1WTbfahmng63e7qz8RbpA": { # DMHA: Sistemi d'Armamento Reliquia (weapon_main)
        "name": "DMHA: Sistemi d'Armamento Reliquia (Armi Vincolate / Messors)",
        "statModifiers": {"strength": 4, "agility": 2}
    },
    "_kW81naTxb2Mph9aQgMKbg": { # DMHA: Equipaggiamento d'Assalto (body)
        "name": "DMHA: Equipaggiamento d'Assalto per Operativi di Grado S & A",
        "statModifiers": {"endurance": 4, "strength": 1}
    },
    "_qacTbKEFgej4ndm8D7YmV": { # DMHA: Generatori Portatili di Barriera (trinket)
        "name": "DMHA: Generatori Portatili di Barriera & Dissuasione Mana (Mana Fields)",
        "statModifiers": {"endurance": 2, "intelligence": 2}
    },
    "_eGrfMqCybMRyChUgNbYCK": { # DMHA: Lame Mana-Conductive & Sigilli Runici (weapon_main)
        "name": "DMHA: Lame Mana-Conductive & Sigilli Runici da Trincea",
        "statModifiers": {"strength": 3, "intelligence": 1}
    },
    "_27xnFr6AqqJqN6EyzMAHj": { # DMHA: Visori Spettrali & Tracciatori di Squarcio (head)
        "name": "DMHA: Visori Spettrali & Tracciatori di Squarcio Classe 1 e 2",
        "statModifiers": {"perception": 3, "intelligence": 1}
    },
    "_kWJK9q3313zYAfR8UT1pc": { # SUCC: Catalizzatori, Focus Runici (weapon_off)
        "name": "SUCC: Catalizzatori, Focus Runici & Sigilli d'Incanalamento",
        "statModifiers": {"intelligence": 2, "perception": 1}
    },
    "_emAUbbxE3WBAAn7rX18BY": { # Reinforced Runic Mechanic Wrench (weapon_main)
        "name": "Reinforced Runic Mechanic Wrench",
        "statModifiers": {"strength": 2, "endurance": 1}
    },
    "_a2MtcAwG1QCcd2eJKt1KN": { # Obsidian Balanced Polyhedral Dice Set (trinket)
        "name": "Obsidian Balanced Polyhedral Dice Set",
        "statModifiers": {"luck": 2, "intelligence": 1}
    },
    "_b4YjVRQ2hVJLHGJMfgUFp": { # Reinforced Carbon-Fiber Shortboard (weapon_main)
        "name": "Reinforced Carbon-Fiber Shortboard",
        "statModifiers": {"agility": 2, "strength": 1}
    },
    "_Dp9qtARRc7ahMWHb8KDdh": { # Thermal Neoprene Pacific Wetsuit (body)
        "name": "Thermal Neoprene Pacific Wetsuit (4/3mm)",
        "statModifiers": {"endurance": 2, "agility": 1}
    },
    "_gKLdADmXkpM1XdLC6L6T2": { # Braided Silver Thread Talisman Bracelet (ring1)
        "name": "Braided Silver Thread Talisman Bracelet",
        "statModifiers": {"luck": 2, "perception": 1}
    },
    "_LMbFnEpxDDTdwyUCAkkmB": { # Surgical Black Titanium Industrial Piercing (trinket)
        "name": "Surgical Black Titanium Industrial Piercing",
        "statModifiers": {"charisma": 1, "endurance": 1}
    },
    "_yxP6wUGEkwxk7FFH7Br91": { # Handcrafted Distressed Leather Belt Pouch (trinket)
        "name": "Handcrafted Distressed Leather Belt Pouch",
        "statModifiers": {"agility": 1, "luck": 1}
    }
}

def update_live_lexicon():
    print(f"--- Updating {len(EQUIPMENT_EFFECTS)} equipment items on Wyvern World Lexicon ---")
    results = []
    for item_id, config in EQUIPMENT_EFFECTS.items():
        url = f"https://app.wyvern.chat/api/worlds/lexicon/{item_id}"
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req) as resp:
            entry = json.loads(resp.read().decode('utf-8'))
        
        ic = entry.get('item_config') or {}
        ic['effects'] = {"statModifiers": config['statModifiers']}
        
        patch_payload = {
            "item_config": ic
        }
        
        put_req = urllib.request.Request(
            url,
            data=json.dumps(patch_payload).encode('utf-8'),
            headers=HEADERS,
            method='PUT'
        )
        with urllib.request.urlopen(put_req) as p_resp:
            updated = json.loads(p_resp.read().decode('utf-8'))
            status = p_resp.status
            print(f"[{status}] Updated '{config['name']}' ({item_id}) -> {updated.get('item_config', {}).get('effects')}")
            results.append(updated)
            
    return results

def update_local_snapshots(updated_entries):
    # 1. Update scratch/live_world__YpX47fNraQFw2dD7TdycJ_lexicon.json
    lex_path = SCRATCH / 'live_world__YpX47fNraQFw2dD7TdycJ_lexicon.json'
    if lex_path.exists():
        with open(lex_path, 'r', encoding='utf-8') as f:
            lex_list = json.load(f)
        
        updated_map = {e.get('id'): e for e in updated_entries}
        modified_count = 0
        for i, item in enumerate(lex_list):
            item_id = item.get('id') or item.get('_id')
            if item_id in updated_map:
                lex_list[i] = updated_map[item_id]
                modified_count += 1
        
        with open(lex_path, 'w', encoding='utf-8') as f:
            json.dump(lex_list, f, indent=2, ensure_ascii=False)
        print(f"Updated {modified_count} entries in {lex_path}")
        
    # 2. Update FINAL/Svartulfr_Lorebook_I.json if matching
    lb1_path = FINAL / 'Svartulfr_Lorebook_I.json'
    if lb1_path.exists():
        with open(lb1_path, 'r', encoding='utf-8') as f:
            lb1 = json.load(f)
        
        name_to_effects = {cfg['name']: cfg['statModifiers'] for cfg in EQUIPMENT_EFFECTS.values()}
        lb_modified = 0
        for entry in lb1.get('entries', []):
            name = entry.get('name')
            if name in name_to_effects:
                ic = entry.get('item_config') or {}
                ic['effects'] = {"statModifiers": name_to_effects[name]}
                entry['item_config'] = ic
                lb_modified += 1
        
        # Enforce entries == lexicon parity
        lb1['lexicon'] = json.loads(json.dumps(lb1['entries']))
        with open(lb1_path, 'w', encoding='utf-8') as f:
            json.dump(lb1, f, indent=2, ensure_ascii=False)
        print(f"Updated {lb_modified} entries in {lb1_path} (entries == lexicon parity preserved: {lb1['entries'] == lb1['lexicon']})")

if __name__ == '__main__':
    updated = update_live_lexicon()
    update_local_snapshots(updated)
    print("Done fixing 14 equipment effects!")
