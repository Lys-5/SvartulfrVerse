import os
import sys
import json
import requests
import uuid

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

def get_world(token, wid):
    url = f"{API_BASE}/worlds/{wid}"
    headers = {'Authorization': f'Bearer {token}'}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(f"GET world failed: {resp.status_code} {resp.text}")
    return resp.json()

def put_world(token, wid, body):
    url = f"{API_BASE}/worlds/{wid}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    resp = requests.put(url, headers=headers, json=body)
    if resp.status_code != 200:
        raise Exception(f"PUT world failed: {resp.status_code} {resp.text}")
    return resp.json()

def generate_modifiers(mgt=0, res=0, agi=0, wit=0, prs=0, sct=0):
    mods = []
    stats = {
        "stat_1": mgt,
        "stat_2": res,
        "stat_3": agi,
        "stat_4": wit,
        "stat_5": prs,
        "stat_6": sct
    }
    for stat_id, val in stats.items():
        if val != 0:
            mods.append({
                "stat_id": stat_id,
                "type": "add",
                "value": val
            })
    return mods

def main():
    token = get_auth_token()
    print("Fetching world...")
    world = get_world(token, WORLD_ID)
    
    species = [
        {"id": str(uuid.uuid4()), "name": "Human", "description": "Base neutrale.", "modifiers": generate_modifiers()},
        {"id": str(uuid.uuid4()), "name": "Werewolf (Pureblood)", "description": "Licantropo puro di dinastia.", "modifiers": generate_modifiers(mgt=2, res=1, sct=1, wit=-1)},
        {"id": str(uuid.uuid4()), "name": "Werewolf (Common)", "description": "Licantropo comune.", "modifiers": generate_modifiers(mgt=1, res=1, sct=1, wit=-1)},
        {"id": str(uuid.uuid4()), "name": "Minotaur", "description": "Forte, imponente ma lento.", "modifiers": generate_modifiers(mgt=3, res=2, agi=-2, sct=-1)},
        {"id": str(uuid.uuid4()), "name": "Half-Elf", "description": "Agile e carismatico.", "modifiers": generate_modifiers(agi=2, wit=1, prs=1, res=-1)},
        {"id": str(uuid.uuid4()), "name": "Vampire", "description": "Predatore notturno affascinante.", "modifiers": generate_modifiers(agi=1, prs=2, mgt=1, res=-1)},
        {"id": str(uuid.uuid4()), "name": "Mage / Caster", "description": "Utilizzatore di arti arcane.", "modifiers": generate_modifiers(wit=2, prs=1, mgt=-1, res=-1)}
    ]
    
    occupations = [
        {"id": str(uuid.uuid4()), "name": "SUCC Student / Civilian", "description": "Studente o civile.", "modifiers": generate_modifiers(prs=1, wit=1)},
        {"id": str(uuid.uuid4()), "name": "Guild Vanguard (DPS)", "description": "Assaltatore della Gilda.", "modifiers": generate_modifiers(mgt=1, agi=1)},
        {"id": str(uuid.uuid4()), "name": "Guild Tank", "description": "Difensore corazzato.", "modifiers": generate_modifiers(res=2, mgt=1)},
        {"id": str(uuid.uuid4()), "name": "Guild Support (Healer/Mage)", "description": "Supporto curativo o magico.", "modifiers": generate_modifiers(wit=2, prs=1)},
        {"id": str(uuid.uuid4()), "name": "DCC Security / PMC", "description": "Operativo corporativo.", "modifiers": generate_modifiers(sct=2, agi=1)},
        {"id": str(uuid.uuid4()), "name": "Street Scrapper / Rogue", "description": "Combattente clandestino.", "modifiers": generate_modifiers(agi=2, sct=1)}
    ]
    
    traits = [
        {"id": str(uuid.uuid4()), "name": "Lupine Senses", "description": "Olfatto e udito potenziati.", "modifiers": generate_modifiers(sct=2)},
        {"id": str(uuid.uuid4()), "name": "Alpha Dominance", "description": "Aura di comando, ma impulsivo.", "modifiers": generate_modifiers(prs=2, wit=-1)},
        {"id": str(uuid.uuid4()), "name": "Silver Allergy", "description": "Malus severo passivo.", "modifiers": generate_modifiers(res=-2)},
        {"id": str(uuid.uuid4()), "name": "Dungeon Veteran", "description": "Esperienza sul campo.", "modifiers": generate_modifiers(mgt=1, wit=1)},
        {"id": str(uuid.uuid4()), "name": "Feral Blood", "description": "Fortissimo ma selvaggio/incontrollabile.", "modifiers": generate_modifiers(mgt=2, prs=-2)},
        {"id": str(uuid.uuid4()), "name": "Regenerative Factor", "description": "Guarigione rapida.", "modifiers": generate_modifiers(res=2)},
        {"id": str(uuid.uuid4()), "name": "Night Stalker", "description": "Predatore notturno.", "modifiers": generate_modifiers(agi=1, sct=1)},
        {"id": str(uuid.uuid4()), "name": "Tech Savvy", "description": "Perfetto per la DCC.", "modifiers": generate_modifiers(wit=2)},
        {"id": str(uuid.uuid4()), "name": "Blood Craze", "description": "Furia berserker.", "modifiers": generate_modifiers(mgt=2, res=-1, agi=-1)}
    ]
    
    body = {
        "species": species,
        "occupations": occupations,
        "traits": traits
    }
    
    print("Updating world species, occupations, and traits...")
    put_world(token, WORLD_ID, body)
    print("Update successful!")

if __name__ == '__main__':
    main()
