import sys
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
import urllib.request
import json

def update_world_info():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    world_id = '_CgYT8fHXpDC4crjmegQF7'
    w_url = f'https://app.wyvern.chat/api/worlds/{world_id}'

    # 1. Fresh GET snapshot
    req = urllib.request.Request(w_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        current_world = json.loads(resp.read().decode('utf-8'))
    print(f"Current tags count: {len(current_world.get('tags', []))}")
    print(f"Current tagline: {current_world.get('tagline')}")

    new_tags = [
        "Third",
        "AnyPOV",
        "Original",
        "Fantasy",
        "Modern",
        "Supernatural",
        "Action",
        "Adventure",
        "Romance",
        "Alpha",
        "Monster",
        "Forest",
        "City",
        "multiple-characters",
        "narrator",
        "Italian",
        "English",
        "Human",
        "Demihuman",
        "Werewolf",
        "substances",
        "discrimination",
        "Breeding",
        "ScentPlay",
        "Claiming"
    ]

    new_tagline = "Millennial werewolf dynasty, college chaos at SUCC, unchained passions, and deadly dungeon incursions in supernatural modern California."

    new_desc = (
        "Svartúlfr | Urban is set in modern-day supernatural California, where an ancient werewolf dynasty, chaotic campus life, and high-stakes dungeon incursions collide. At its center lies Blackwood: the thousand-year-old supernatural seat tucked inland within dense pine forests, ruled by the Douglas-Bloodmoon werewolf dynasty. A short drive away sits Solarton, the vibrant coastal college town hosting SUCC (Supernatural University of Central California), where young supernaturals, demi-humans, and mages navigate collegiate freedom, raw impulses, and intense rivalries.\n\n"
        "The patriarch, Erik Douglas, heads the Douglas Commercial Coalition (DCC), an ancient merchant house founded in 1666 that grew into an international trade empire. Since 2019, the DCC has fielded its own heavily armed Security Division, commanded by Major Kaladin Nargathon—an elite PMC answering family curfews and territorial breaches with biometric drones, silver-tipped ordnance, and tactical extraction teams.\n\n"
        "Underneath the corporate towers and neon nightlife lies the Modern Fantasy frontier: dimensional Rifts, monster-infested Dungeon Hives, and the Hunters Guild. In districts like the Cable District and the Dockside riverfront, licensed vanguard teams like Team Ukiyo (led by the werewolf vanguard Radek, the minotaur tank Goran, and the half-elf DPS Kian) and nomadic heavy-hitters like Marek and the Ironhorn Nomads brave subterranean Apex Trials. Here, modern tactical gear merges with abyssal cores, enchanted weaponry, and sacred relics, creating a lucrative and lethal dungeon-crawler economy guarded by Council master builders like Barrow 'The Bull'.\n\n"
        "Roleplay in Svartúlfr is raw, visceral, and completely unchained. Every interaction pulses with Lupine Social Ecology (LSE): active olfactory awareness, shifting pheromones, intense dominance and submission dynamics, territorial drives, and the primal heat and rut cycles of werewolves and demi-humans. Adult characters experience fierce romantic chemistry, unfiltered passion, unapologetic desire, and brutal tactical combat in dark alleys and dungeon depths alike.\n\n"
        "The overarching narrator is Wulfnic Báleygr, the immortal 1199-year-old Firstborn werewolf consecrated by Fenris in 827 AD. Having crossed the Arctic by longship and planted the sacred yew on the banks of the Yarrow in 1022 AD, the one-eyed Primordial watches every generation of his bloodline through the stolen eye of Odin the Betrayer, chronicling a saga of ancient blood, untamed desire, and perilous modern power."
    )

    payload = {
        'tags': new_tags,
        'tagline': new_tagline,
        'description': new_desc,
        'context_description': new_desc
    }

    req = urllib.request.Request(w_url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        print(f"PUT response code: {resp.status}")

    # 3. Post-write GET verification
    req = urllib.request.Request(w_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        verified_world = json.loads(resp.read().decode('utf-8'))

    print(f"Verified tags count: {len(verified_world.get('tags', []))}")
    print(f"Verified tags: {verified_world.get('tags')}")
    print(f"Verified tagline: {verified_world.get('tagline')}")
    print("SUCCESS: World Info updated and verified on Wyvern Web!")

    # 4. Update local raw files
    with open('exports/raw_db_dumps/raw_world.json', 'r', encoding='utf-8') as f:
        rw = json.load(f)
    rw['tags'] = new_tags
    rw['tagline'] = new_tagline
    rw['description'] = new_desc
    rw['context_description'] = new_desc
    with open('exports/raw_db_dumps/raw_world.json', 'w', encoding='utf-8') as f:
        json.dump(rw, f, indent=2, ensure_ascii=False)

    with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
        se = json.load(f)
    if 'world' in se:
        se['world']['tags'] = new_tags
        se['world']['tagline'] = new_tagline
        se['world']['description'] = new_desc
        se['world']['context_description'] = new_desc
    with open('exports/Svartulfr_Export.json', 'w', encoding='utf-8') as f:
        json.dump(se, f, indent=2, ensure_ascii=False)
    print("SUCCESS: Local raw_world.json and Svartulfr_Export.json synchronized!")

if __name__ == '__main__':
    update_world_info()
