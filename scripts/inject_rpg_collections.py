import sys
import json
import requests
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

# MGT=stat_1, RES=stat_2, AGI=stat_3, WIT=stat_4, PRS=stat_5, SCT=stat_6
def make_mods(mgt=0, res=0, agi=0, wit=0, prs=0, sct=0):
    mods = {}
    if mgt != 0: mods["stat_1"] = mgt
    if res != 0: mods["stat_2"] = res
    if agi != 0: mods["stat_3"] = agi
    if wit != 0: mods["stat_4"] = wit
    if prs != 0: mods["stat_5"] = prs
    if sct != 0: mods["stat_6"] = sct
    return mods

species_data = [
    {"name": "Human (Standard)", "mods": make_mods()},
    {"name": "Human (Magically Gifted)", "mods": make_mods(wit=2, mgt=-1)},
    {"name": "Werewolf (Pureblood)", "mods": make_mods(mgt=2, res=1, sct=1, wit=-1)},
    {"name": "Werewolf (Common)", "mods": make_mods(mgt=1, res=1, sct=1, wit=-1)},
    {"name": "Shapeshifter", "mods": make_mods(agi=2, sct=1, res=-1)},
    {"name": "Demi-Human (Apex Carnivore)", "mods": make_mods(mgt=2, agi=1, wit=-1)},
    {"name": "Demi-Human (Prey/Herbivore)", "mods": make_mods(agi=2, sct=2, mgt=-1, res=-1)},
    {"name": "Demi-Human (Avian/Reptilian)", "mods": make_mods(agi=1, wit=1, res=-1)},
    {"name": "Hybrid (Large Brute)", "mods": make_mods(mgt=3, res=2, agi=-2, sct=-1)},
    {"name": "Hybrid (Serpentine)", "mods": make_mods(mgt=1, agi=1, prs=1, res=-1)},
    {"name": "Hybrid (Aquatic)", "mods": make_mods(agi=1, res=1, wit=1, sct=-1)},
    {"name": "Demon (Brute / Ifrit)", "mods": make_mods(mgt=2, res=1, prs=-1)},
    {"name": "Demon (Succubus / Incubus)", "mods": make_mods(prs=3, agi=1, res=-1, mgt=-1)},
    {"name": "Fae (High/Sidhe/Dryads)", "mods": make_mods(wit=2, prs=1, mgt=-1)},
    {"name": "Fae (Small/Pixies/Sprites)", "mods": make_mods(agi=3, sct=1, mgt=-2, res=-1)},
    {"name": "Vampire (Elite)", "mods": make_mods(prs=2, agi=1, mgt=1, res=-1)},
    {"name": "Undead (Corporeal)", "mods": make_mods(res=3, mgt=1, agi=-2, prs=-1)},
    {"name": "Undead (Spectral)", "mods": make_mods(wit=2, agi=1, mgt=-2, res=-1)}
]

occupations_data = [
    {"name": "SUCC Student / Civilian", "mods": make_mods(prs=1, wit=1)},
    {"name": "DCC Security / PMC", "mods": make_mods(sct=2, agi=1)},
    {"name": "Street Scrapper / Rogue", "mods": make_mods(agi=2, sct=1)},
    {"name": "Guild Vanguard (DPS)", "mods": make_mods(mgt=1, agi=1)},
    {"name": "Guild Tank", "mods": make_mods(res=2, mgt=1)},
    {"name": "Guild Support (Healer/Mage)", "mods": make_mods(wit=2, prs=1)},
    {"name": "Pack Leader", "mods": make_mods(prs=2, wit=1, sct=-1)},
    {"name": "Leader's Mate / Pack Mom", "mods": make_mods(prs=2, res=1, mgt=-1)},
    {"name": "Right Hand (Peacekeeper)", "mods": make_mods(wit=2, prs=1, mgt=-1)},
    {"name": "Left Hand (Enforcer)", "mods": make_mods(mgt=2, agi=1, prs=-1)},
    {"name": "Caretaker / Breeder", "mods": make_mods(res=2, prs=1, mgt=-1)},
    {"name": "Hunter / Provider", "mods": make_mods(agi=1, sct=1)},
    {"name": "Defender", "mods": make_mods(res=2)},
    {"name": "Teacher", "mods": make_mods(wit=2)},
    {"name": "Diplomat", "mods": make_mods(prs=2)},
    {"name": "Scout", "mods": make_mods(sct=2)},
    {"name": "Builder", "mods": make_mods(mgt=1, wit=1)},
    {"name": "House Head (Lord/Patriarch)", "mods": make_mods(prs=2, wit=1, agi=-1)},
    {"name": "Knight (Sworn Warrior)", "mods": make_mods(mgt=1, res=1)},
    {"name": "Citizen", "mods": make_mods()},
    {"name": "Pro Athlete / Fighter", "mods": make_mods(mgt=1, agi=1)},
    {"name": "Academic / PhD Candidate", "mods": make_mods(wit=2)},
    {"name": "Patriarch / Coven Leader", "mods": make_mods(prs=2, wit=1, mgt=-1)},
    {"name": "Event Organizer / Fixer", "mods": make_mods(prs=1, wit=1)}
]

traits_data = [
    {"name": "LSE Alpha Biology", "mods": make_mods(prs=2, wit=-1)},
    {"name": "LSE Beta Biology", "mods": make_mods(mgt=1, res=1)},
    {"name": "LSE Omega Biology", "mods": make_mods(prs=2, res=1, mgt=-2)},
    {"name": "LSE Delta Biology", "mods": make_mods(sct=2, prs=-1)},
    {"name": "Lupine Senses", "mods": make_mods(sct=2)},
    {"name": "Silver Allergy", "mods": make_mods(res=-2)},
    {"name": "Dungeon Veteran", "mods": make_mods(mgt=1, wit=1)},
    {"name": "Feral Blood", "mods": make_mods(mgt=2, prs=-2)},
    {"name": "Regenerative Factor", "mods": make_mods(res=2)},
    {"name": "Night Stalker", "mods": make_mods(agi=1, sct=1)},
    {"name": "Tech Savvy", "mods": make_mods(wit=2)},
    {"name": "Blood Craze", "mods": make_mods(mgt=2, res=-1, agi=-1)},
    {"name": "S.R.F. Veteran", "mods": make_mods(res=1, wit=1)},
    {"name": "Cyber-Augmented (Sci-Fi)", "mods": make_mods(res=2, mgt=1, prs=-2)},
    {"name": "Symbiotic Feeder", "mods": make_mods(prs=2, res=-1)},
    {"name": "Ancient Heritage", "mods": make_mods(wit=1, prs=1)}
]

def create_item(token, collection, item_data):
    url = f"{API_BASE}/worlds/rpg/{collection}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "world_id": WORLD_ID,
        "name": item_data["name"],
        "description": "",
        "stat_modifiers": item_data["mods"],
        "player_selectable": True
    }
    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code != 200:
        print(f"Failed to create {collection} {item_data['name']}: {resp.status_code} {resp.text}")
    else:
        print(f"Created {collection}: {item_data['name']}")
    time.sleep(0.5)

def main():
    token = get_auth_token()
    
    print(f"Injecting {len(species_data)} species...")
    for s in species_data:
        create_item(token, "species", s)
        
    print(f"Injecting {len(occupations_data)} occupations...")
    for o in occupations_data:
        create_item(token, "occupations", o)
        
    print(f"Injecting {len(traits_data)} traits...")
    for t in traits_data:
        create_item(token, "traits", t)

    print("All custom RPG settings injected successfully!")

if __name__ == '__main__':
    main()
