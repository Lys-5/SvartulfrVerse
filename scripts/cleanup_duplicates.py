import urllib.request
import json
import os
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

def cleanup_duplicates():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    
    # 1. Snapshot and Delete Lexicon duplicates
    lex_to_delete = [
        ('_M9jgVAFHHMJhYXUcgmhcG', 'Intimacy Profile - Jean-Luc Virtuoso (raw XML duplicate)'),
        ('_Padg7gBCkypyY9wVhWV1L', 'Intimacy Profile - Dante (raw XML duplicate)')
    ]
    
    snapshot_dir = os.path.join('scratch', 'duplicate_snapshots')
    os.makedirs(snapshot_dir, exist_ok=True)
    
    for lex_id, desc in lex_to_delete:
        get_url = f'https://app.wyvern.chat/api/worlds/lexicon/{lex_id}'
        try:
            req = urllib.request.Request(get_url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                lex_data = json.loads(resp.read().decode('utf-8'))
            
            snap_file = os.path.join(snapshot_dir, f'lex_{lex_id}.json')
            with open(snap_file, 'w', encoding='utf-8') as f:
                json.dump(lex_data, f, indent=2, ensure_ascii=False)
            print(f"Snapshot saved for {desc} -> {snap_file}")
            
            # Send DELETE
            del_req = urllib.request.Request(get_url, headers=headers, method='DELETE')
            with urllib.request.urlopen(del_req) as resp:
                print(f"DELETE {lex_id} response: {resp.status}")
                
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"Lexicon {lex_id} already not found / deleted (404).")
            else:
                print(f"Error on Lexicon {lex_id}: {e}")
        except Exception as e:
            print(f"Error deleting Lexicon {lex_id}: {e}")

    # 2. Update Marek's attitude target_id from duplicate Barrow to canonical Barrow
    # Canonical Barrow: _LEeEzdCCyGjQ8kfVkcra8
    # Duplicate Barrow: _V9JeyRrEFDyApmx3rJNeL
    marek_id = '_cDx2yGNtVbCCDUCHcUUxG'
    canonical_barrow_id = '_LEeEzdCCyGjQ8kfVkcra8'
    duplicate_barrow_id = '_V9JeyRrEFDyApmx3rJNeL'
    
    get_marek_url = f'https://app.wyvern.chat/api/worlds/characters/{marek_id}'
    req = urllib.request.Request(get_marek_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        marek_data = json.loads(resp.read().decode('utf-8'))
        
    snap_marek = os.path.join(snapshot_dir, f'char_marek_pre_fix.json')
    with open(snap_marek, 'w', encoding='utf-8') as f:
        json.dump(marek_data, f, indent=2, ensure_ascii=False)
        
    marek_attitudes = marek_data.get('attitudes') or []
    updated_marek_att = False
    for att in marek_attitudes:
        if att.get('target_id') == duplicate_barrow_id:
            att['target_id'] = canonical_barrow_id
            updated_marek_att = True
            print("Updated Marek's attitude target to canonical Barrow ID.")
            
    if updated_marek_att:
        patch_payload = json.dumps({'attitudes': marek_attitudes}).encode('utf-8')
        put_req = urllib.request.Request(get_marek_url, data=patch_payload, headers={**headers, 'Content-Type': 'application/json'}, method='PUT')
        with urllib.request.urlopen(put_req) as resp:
            print(f"PUT Marek attitudes response: {resp.status}")
            
    # 3. Update Canonical Barrow (_LEeEzdCCyGjQ8kfVkcra8)
    get_barrow_url = f'https://app.wyvern.chat/api/worlds/characters/{canonical_barrow_id}'
    req = urllib.request.Request(get_barrow_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        barrow_data = json.loads(resp.read().decode('utf-8'))
        
    snap_barrow = os.path.join(snapshot_dir, f'char_canonical_barrow_pre_fix.json')
    with open(snap_barrow, 'w', encoding='utf-8') as f:
        json.dump(barrow_data, f, indent=2, ensure_ascii=False)
        
    barrow_patch = {
        'tags': ['Male', 'Minotaur', 'Veteran', 'Guardian', 'Ironhorn Nomads', 'Builder', 'Council'],
        'outfits': [
            {
                "id": "outfit-1790649041281-bar01",
                "name": "Heavy Construction Workwear",
                "description": "Salopette in pesante denim rinforzato logorata dal cemento e dalla polvere di calce, una maglia grigia a maniche corte che fascia la sua muscolatura taurina massiccia, stivali da lavoro a punta d'acciaio spuntati per le zampe unghiose, cintura da carpentiere con martello da demolizione e guanti da carpentiere sfilati e infilati nella tasca posteriore.",
                "avatar": ""
            },
            {
                "id": "outfit-1790649041281-bar02",
                "name": "Morning Stoop Vigil",
                "description": "Camicia di flanella spessa a quadri scuri lasciata aperta sopra una canotta grigio fumo sbiadita, pantaloni da lavoro in tela pesante e scarponi comodi. Tra le mani enormi tiene un termos da cantiere ammaccato fumante di caffe nero mentre fissa la strada all'alba seduto sul muretto di The Horns.",
                "avatar": ""
            },
            {
                "id": "outfit-1790649041281-bar03",
                "name": "Council Session / Civic Formal",
                "description": "Una camicia da lavoro pulita e stirata in lino scuro abbottonata fino al collo, pantaloni scuri ordinati con cintura in cuoio pesante. Le corna sono lucidate con cura e l'anello d'ottone al setto risplende pulito, incarnando con austera dignita la voce dei demi-umani al Concilio di Blackwood.",
                "avatar": ""
            },
            {
                "id": "outfit-1790649041281-bar04",
                "name": "Ironhorn Nomads Veteran Cut",
                "description": "Il suo vecchio gilet di pelle conciata pesante e consumata con i colori storici degli Ironhorn Nomads del ventennio passato, ricoperto di toppe consunte e cuciture a filo spesso, custodito gelosamente ma tirato fuori solo quando il branco e i vecchi fratelli d'asfalto chiamano.",
                "avatar": ""
            }
        ],
        'default_outfit': 'Heavy Construction Workwear',
        'attitudes': [
            {
                "id": "attitude-1790649041281-bar01",
                "target_type": "world_character",
                "target_id": "_MXcEC8Y6B3BNm3b1ttHj6",
                "target": "",
                "tier": "best_friend",
                "intensity": 95,
                "reasoning": "Fragile angel carrying too much danger, my stoop and hands are her sanctuary."
            },
            {
                "id": "attitude-1790649041281-bar02",
                "target_type": "world_character",
                "target_id": "_cDx2yGNtVbCCDUCHcUUxG",
                "target": "",
                "tier": "best_friend",
                "intensity": 85,
                "reasoning": "Nomads blood brother, we survived twenty years of war together."
            },
            {
                "id": "attitude-1790649041281-bar03",
                "target_type": "world_character",
                "target_id": "_x3VY2kcbaDbKyCqywGeET",
                "target": "",
                "tier": "friend",
                "intensity": 80,
                "reasoning": "Sharp, anxious kid watching over his twin, has my respect and protection."
            }
        ]
    }
    
    put_barrow_req = urllib.request.Request(get_barrow_url, data=json.dumps(barrow_patch).encode('utf-8'), headers={**headers, 'Content-Type': 'application/json'}, method='PUT')
    with urllib.request.urlopen(put_barrow_req) as resp:
        print(f"PUT Canonical Barrow response: {resp.status}")
        
    # 4. Snapshot and Delete Duplicate Barrow (_V9JeyRrEFDyApmx3rJNeL)
    get_dup_url = f'https://app.wyvern.chat/api/worlds/characters/{duplicate_barrow_id}'
    try:
        req = urllib.request.Request(get_dup_url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            dup_data = json.loads(resp.read().decode('utf-8'))
        snap_dup = os.path.join(snapshot_dir, f'char_duplicate_barrow_{duplicate_barrow_id}.json')
        with open(snap_dup, 'w', encoding='utf-8') as f:
            json.dump(dup_data, f, indent=2, ensure_ascii=False)
            
        del_dup_req = urllib.request.Request(get_dup_url, headers=headers, method='DELETE')
        with urllib.request.urlopen(del_dup_req) as resp:
            print(f"DELETE duplicate Barrow response: {resp.status}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Duplicate Barrow {duplicate_barrow_id} already deleted (404).")
        else:
            print(f"Error on duplicate Barrow: {e}")
            
    print("Cleanup completed successfully!")

if __name__ == '__main__':
    cleanup_duplicates()
