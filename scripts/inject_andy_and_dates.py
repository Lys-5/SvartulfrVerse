import sys, json, requests, time
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API = 'https://app.wyvern.chat/api'
token = get_auth_token()
H = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

andy_desc = """[NAME: Andrew Campbell; ALIASES: Andy, The Mascot; SPECIES: Vampire; AGE: {{age}}; GENDER: Male (He/Him); HEIGHT: 5'8"; BUILD: Chubby, thick thighs, dad bod, happy trail and dark body hair; HAIR: Messy black hair; EYES: Dark gray; FEATURES: Pale, broad features, thick eyebrows, stubble; CLOTHING: Baggy hoodies, ripped jeans, beanies, prefers dark muted colors; OCCUPATION: College student (Design / Magical Anthropology), SUCC Bears mascot]

BACKSTORY: Andrew comes from a wealthy, high-society vampire family in Montreal. The Campbells maintain a perfect, polished image, but Andy has always been the odd one out. He suffered from severe asthma as a child, missed school often, and was bullied for his looks and his "weeb" interests like anime. His parents are dismissive of his artistic passions, wanting him to join the family business instead of pursuing art. He only got into his frat, Alpha Sigma Sigma, because his perfect, golden-boy older brother Vincent pulled some strings. He is majoring in Magical Anthropology with a minor in Design, but currently spends his time surviving college, hiding in his messy dorm littered with manga and empty blood packs, and reluctantly working as the mascot for the SUCC Bears ice hockey team.

FAMILY & PACK: Younger brother to Vincent Campbell (the popular, arrogant vampire captain of the Bears). Andy deeply resents and secretly idolizes Vincent's effortless perfection. His parents view him as a disappointment, a fate he has mostly resigned himself to.

VOICE & BEHAVIOR: He is an insecure geek with deep feelings of inadequacy. He stammers, rambles, and drops references to obscure anime and videogames. He is highly self-deprecating, sarcastic, pessimistic, and socially awkward, trying to fade into the background when in public. However, he is secretly passionate, empathetic, and a hopeless romantic. As a vampire, he is surprisingly "haemo-intolerant" (only able to drink O-negative blood without getting sick) and actually gets lightheaded at the sight of blood. When around his crush, he blushes furiously and tries far too hard to act cool.

[THE MASCOT BEHIND THE MASK]"""

# 1. Create Andy
andy_payload = {
    'world_id': WORLD_ID,
    'display_name': 'Andrew "Andy" Campbell',
    'name': 'Andrew Campbell',
    'description': andy_desc,
    'long_summary': andy_desc,
    'is_global': True,
    'rpg_stats': {
        'enabled': True,
        'level': 2,
        'species_id': "Vampire",
        'occupation_id': "SUCC Student"
    }
}
r = requests.post(f'{API}/worlds/characters', headers=H, json=andy_payload)
print(f'Created Andy: {r.status_code}')
if r.status_code == 200:
    andy_id = r.json().get('id')
else:
    andy_id = None

# 2. Update all dates and levels
dates_table = {
    'Rozalia Tănase': {'age': 22, 'level': 2, 'hours': 10293618},
    'Ruby Valerius': {'age': 20, 'level': 2, 'hours': 10311150},
    'Vesna': {'age': 25, 'level': 3, 'hours': 10267320},
    'Mikan': {'age': 21, 'level': 2, 'hours': 10302384},
    'Ginger': {'age': 23, 'level': 3, 'hours': 10284852},
    'Orion and Sigrid Valois': {'age': 30, 'level': 4, 'hours': 10223490},
    'Henrey Cote': {'age': 26, 'level': 3, 'hours': 10258554},
    'Aria Xenthon': {'age': 24, 'level': 3, 'hours': 10276086},
    'Tori': {'age': 21, 'level': 2, 'hours': 10302384},
    'River': {'age': 22, 'level': 2, 'hours': 10293618},
    'Ailsa Hourie': {'age': 45, 'level': 7, 'hours': 10091954},
    'Silas': {'age': 1000, 'level': 99, 'hours': 1720470},
    'Bramble Mossmere': {'age': 300, 'level': 58, 'hours': 7856670},
    'Evan': {'age': 24, 'level': 3, 'hours': 10276086},
    'Vespera Thorne': {'age': 25, 'level': 3, 'hours': 10267320},
    'Eira Elloway': {'age': 120, 'level': 22, 'hours': 9434550},
    'Darius Azadi': {'age': 27, 'level': 3, 'hours': 10249788},
    'Andrew "Andy" Campbell': {'age': 22, 'level': 2, 'hours': 10293618}
}

chars = requests.get(f'{API}/worlds/characters/world/{WORLD_ID}', headers=H).json()
for c in chars:
    name = c.get('display_name', '')
    if name in dates_table:
        cid = c.get('id')
        data = dates_table[name]
        
        # Get full char
        full_c = requests.get(f'{API}/worlds/characters/{cid}', headers=H).json()
        
        rpg = full_c.get('rpg_stats') or {}
        rpg['enabled'] = True
        rpg['level'] = data['level']
        
        payload = {
            'rpg_stats': rpg,
            'start_timeline_position': data['hours'],
            'birthdate': data['hours']
        }
        
        # Add JED age macro to description/long_summary if not present and translate to english for the others if asked?
        # The user said "Rendi tutto in inglese", but translating 17 large cards via python string manipulation is hard.
        # I will let the script just update the RPG and dates for now. I'll translate the rest separately.
        
        pr = requests.put(f'{API}/worlds/characters/{cid}', headers=H, json=payload)
        print(f"Updated {name}: {pr.status_code}")
        time.sleep(0.3)
