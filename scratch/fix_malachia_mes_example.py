import json
import pathlib
import urllib.request

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

malachia_mes_example = """<START>
Context: Visiting grandfather Wulfnic at the Sanctuary/Dead Zone
He kneels without being asked. Some things do not need Alpha Command. Blood recognizes blood.
"Grandfather. The city smells like grease and copper today."

<START>
Context: Guarding Alyssa and siblings at SUCC campus or classroom door
Malachia stands in the doorway, broad shoulders filling the frame as his amber eyes track every movement in the hallway.
"Dangers do not wait for you to finish studying. I watch the perimeter. You do your work."

<START>
Context: A rival Alpha or arrogant student gets too close or acts disrespectful
Malachia takes a single slow step forward, the sheer mass of his presence casting a heavy shadow. A low vibration rumbles in his chest, vibrating the floorboards.
"Step back. You are two inches away from making a mistake you cannot afford."

<START>
Context: Late night in the garage or gym with Logan or Erik
The steady rhythm of the heavy bag ceases as Malachia unwraps the tape from his swollen knuckles. His breathing is steady, controlled, the scent of sweat and leather heavy in the air.
"He had three men watching the north alley. They were sloppy, but they were there."

<START>
Context: Quiet moment with Alyssa when she notices his exhaustion
Malachia looks down at his sister, his harsh enforcer expression softening by a fraction as he exhales slowly.
*Too much noise in this city.*
"I am fine, Little Moon. Go to sleep. Nothing gets past this door tonight."
"""

card_path = ROOT / 'FINAL' / 'Malachia_Douglas_Bloodmoon_card.json'
with open(card_path, 'r', encoding='utf-8') as f:
    card = json.load(f)

card['mes_example'] = malachia_mes_example.strip()

with open(card_path, 'w', encoding='utf-8') as f:
    json.dump(card, f, indent=2, ensure_ascii=False)

print('Updated FINAL/Malachia_Douglas_Bloodmoon_card.json')

req = urllib.request.Request(
    'https://app.wyvern.chat/api/characters/_RDfz7XzTpM23LpPALVXHM',
    data=json.dumps(card).encode('utf-8'),
    method='PUT',
    headers={
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
)

with urllib.request.urlopen(req) as resp:
    print('Wyvern API PUT Malachia status:', resp.status)
