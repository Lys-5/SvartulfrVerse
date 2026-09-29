import os
import sys
import json
import time
import urllib.request
import urllib.error

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

ALYSSA_ID = '_MXcEC8Y6B3BNm3b1ttHj6'
JASPER_ID = '_x3VY2kcbaDbKyCqywGeET'
RADEK_ID = '_4bazKCAbPMmc19HzHAphC'
GORAN_ID = '_JQGgmwyA3qRaTLWck3GjX'
KIAN_ID = '_kc7TyfPDQwUALKXcmTMxQ'
BARROW_ID = '_V9JeyRrEFDyApmx3rJNeL'
MAREK_ID = '_cDx2yGNtVbCCDUCHcUUxG'

CLUBHOUSE_LOC_ID = '_DJxYBCM7rNrXMj1WracGM'
SCENARIO_ID = '_Kn2DFVwyUgkVGz9UWUnBF'

ts = int(time.time() * 1000)

ATTITUDES = {
    RADEK_ID: [
        {"id": f"attitude-{ts}-rad01", "target_type": "world_character", "target_id": ALYSSA_ID, "target": "", "tier": "best_friend", "intensity": 85, "reasoning": "Invaluable medical force multiplier and squad savior, protected under official contract."},
        {"id": f"attitude-{ts}-rad02", "target_type": "world_character", "target_id": JASPER_ID, "target": "", "tier": "friend", "intensity": 75, "reasoning": "Skilled arcane infiltrator, though his hyper-jealousy requires constant monitoring."},
        {"id": f"attitude-{ts}-rad03", "target_type": "world_character", "target_id": GORAN_ID, "target": "", "tier": "best_friend", "intensity": 95, "reasoning": "Frontline brother rescued from the pits, indestructible shock-trooper."},
        {"id": f"attitude-{ts}-rad04", "target_type": "world_character", "target_id": KIAN_ID, "target": "", "tier": "best_friend", "intensity": 92, "reasoning": "Little brother and agile scout, kept on a disciplined leash."}
    ],
    GORAN_ID: [
        {"id": f"attitude-{ts}-gor01", "target_type": "world_character", "target_id": RADEK_ID, "target": "", "tier": "best_friend", "intensity": 95, "reasoning": "My squad leader and savior, I follow his command into hell."},
        {"id": f"attitude-{ts}-gor02", "target_type": "world_character", "target_id": KIAN_ID, "target": "", "tier": "best_friend", "intensity": 90, "reasoning": "Slick little brother, love talking trash and watching his back."},
        {"id": f"attitude-{ts}-gor03", "target_type": "world_character", "target_id": ALYSSA_ID, "target": "", "tier": "best_friend", "intensity": 88, "reasoning": "Miracle healer who cured my crushed shoulder, anyone touching her dies."},
        {"id": f"attitude-{ts}-gor04", "target_type": "world_character", "target_id": JASPER_ID, "target": "", "tier": "friend", "intensity": 70, "reasoning": "Cynical hacker kid with good tricks, fun to watch him get riled up."}
    ],
    KIAN_ID: [
        {"id": f"attitude-{ts}-kia01", "target_type": "world_character", "target_id": ALYSSA_ID, "target": "", "tier": "best_friend", "intensity": 85, "reasoning": "Bound by a sacred pact to conquer her heart through rational mind, not animal instinct."},
        {"id": f"attitude-{ts}-kia02", "target_type": "world_character", "target_id": JASPER_ID, "target": "", "tier": "friend", "intensity": 75, "reasoning": "Territorial rival, I take immense joy in driving his protective jealousy crazy."},
        {"id": f"attitude-{ts}-kia03", "target_type": "world_character", "target_id": RADEK_ID, "target": "", "tier": "best_friend", "intensity": 92, "reasoning": "The big brother who gave me dignity when I was just a street thief."},
        {"id": f"attitude-{ts}-kia04", "target_type": "world_character", "target_id": GORAN_ID, "target": "", "tier": "best_friend", "intensity": 88, "reasoning": "Big bumbling brute with a heart of gold, my heavy battering ram."}
    ],
    BARROW_ID: [
        {"id": f"attitude-{ts}-bar01", "target_type": "world_character", "target_id": ALYSSA_ID, "target": "", "tier": "best_friend", "intensity": 95, "reasoning": "Fragile angel carrying too much danger, my stoop and hands are her sanctuary."},
        {"id": f"attitude-{ts}-bar02", "target_type": "world_character", "target_id": MAREK_ID, "target": "", "tier": "best_friend", "intensity": 85, "reasoning": "Nomads blood brother, we survived twenty years of war together."},
        {"id": f"attitude-{ts}-bar03", "target_type": "world_character", "target_id": JASPER_ID, "target": "", "tier": "friend", "intensity": 80, "reasoning": "Sharp, anxious kid watching over his twin, has my respect and protection."}
    ],
    MAREK_ID: [
        {"id": f"attitude-{ts}-mar01", "target_type": "world_character", "target_id": ALYSSA_ID, "target": "", "tier": "best_friend", "intensity": 90, "reasoning": "Fascinating, innocent healer connected to high-level power, she is under my absolute law."},
        {"id": f"attitude-{ts}-mar02", "target_type": "world_character", "target_id": BARROW_ID, "target": "", "tier": "best_friend", "intensity": 90, "reasoning": "Old brother and legendary enforcer, one of the few men on Earth I respect."},
        {"id": f"attitude-{ts}-mar03", "target_type": "world_character", "target_id": JASPER_ID, "target": "", "tier": "acquaintance", "intensity": 65, "reasoning": "Clever little cyber-wolf, needs to learn his place around seasoned monsters."}
    ]
}

SCENARIO_TEXT = """=>Narrator:
Venerdi' 26 giugno 2026, ore 21:30 - Club House Ironhorn Nomads, Naperville, Illinois

Il rombo cavernoso di decine di chopper pesanti a motore sbloccato fa tremare l'asfalto del cortile recintato del Club House degli Ironhorn Nomads. L'aria estiva del Midwest e' satura dell'odore acre di pneumatici surriscaldati, birra industriale, bourbon barricato e dell'inconfondibile profumo di incenso sacro che Marek brucia per tenere a bada gli spiriti antichi.

I fari alogeni e le catene di lampadine da cantiere illuminano l'acqua turchese della grande piscina interrata nel retro dell'officina. Attorno alla vasca si muovono colossi di oltre due metri: biker Blue e Red Oni con le corna ornate di anelli d'acciaio, veterani con giubbotti di pelle logori coperti dalle toppe del club, minotauri e orchi che tracannano alcol ridendo a voce tonante.

La porta di ferro dell'officina sbatte, e il cortile subisce un'immediata, palpabile caduta di pressione.

=>Marek:
Marek fa il suo ingresso a torso nudo, imponente nei suoi due metri e sei di muscoli color blu reale, i lunghi capelli bianchi raccolti in una coda sciolta e le due corna scure che fendono la luce dei riflettori. Il gilet di pelle del club e' lasciato aperto sulle cicatrici di trent'anni di risse e guerre di strada.

Con la mano sinistra, pesante come una morsa d'acciaio, cinge con possessiva disinvoltura il fianco morbido di {{user}}, guidandola verso il bordo della piscina con passo lento e dominante. Lo sguardo grigio-blu dell'Oni vaga sui fratelli del club, freddo e tagliente come una mannaia.

"Drizzate le orecchie, bastardi," la voce di Marek e' un baritono roco e gutturale che sovrasta senza sforzo la musica rock delle casse. "Questa e' la guaritrice di cui vi ho parlato. E' sotto la mia parola, la mia protezione e il mio marchio per tutta la notte. Chiunque allunghi una mano o provi a fare il fenomeno senza che sia io a dirlo, perde le dita una per una sul banco dell'officina. Siamo intesi?"

=>Narrator:
Un mormorio di sguardi invidiosi e cenni di rispetto attraversa il gruppo di biker: tra gli Ironhorn Nomads la parola del Primo Enforcer e' legge assoluta. Marek abbassa lo sguardo su {{user}}, un mezzo sorriso arrogante che gli piega il pizzetto bianco mentre le offre un bicchiere di bourbon ghiacciato.

=>Marek:
"Rilassati, fiorellino. Qui nessuno fiata finche' sei con me. Ora dimmi che effetto ti fa vedere dove passo le notti quando non sono a ripulire i vostri cristalli di contrabbando."
"""

def fix_all():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    # 1. Update Attitudes
    print("--- 1. UPDATING MUTUAL ATTITUDES ---")
    for cid, att_list in ATTITUDES.items():
        payload = {"attitudes": att_list}
        req = urllib.request.Request(f"{API_BASE}/characters/{cid}", data=json.dumps(payload).encode('utf-8'), headers=headers, method='PUT')
        try:
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                print(f"  [OK] Attitudes updated for {res.get('display_name')} ({cid}): {len(res.get('attitudes', []))} attitudes.")
        except Exception as e:
            print(f"  [ERROR] Updating attitudes for {cid}: {e}")

    # 2. Fetch Club House location to see full object
    print("\n--- 2. FETCHING CLUB HOUSE LOCATION OBJECT ---")
    req_loc = urllib.request.Request(f"{API_BASE}/locations/{CLUBHOUSE_LOC_ID}", headers=headers)
    with urllib.request.urlopen(req_loc) as resp:
        loc_data = json.loads(resp.read().decode('utf-8'))
        print(f"  Fetched Location: {loc_data.get('name')} (ID: {loc_data.get('id')})")

    # 3. Update Scenario with scene text and location
    print("\n--- 3. UPDATING POOL PARTY SCENARIO ---")
    scen_payload = {
        "name": "Festa in Piscina agli Ironhorn Nomads con Marek",
        "description": "Venerdi' 26 giugno 2026. Marek porta Alyssa al Club House fortificato degli Ironhorn Nomads a Naperville per una rumorosa festa in piscina tra chopper, fusti di birra e biker Oni. Marek marca pubblicamente il territorio avvertendo l'intero club che nessuno puo' sfiorarla senza il suo permesso.",
        "tags": ["Ironhorn Nomads", "Marek", "Alyssa", "Pool Party", "Naperville", "Biker"],
        "premade_scenes": [
            {
                "id": f"scene-{ts}-pool-party",
                "description": "Club House Ironhorn Nomads, Naperville",
                "scene_text": SCENARIO_TEXT
            }
        ]
    }

    # First update description and scene text
    req_s = urllib.request.Request(f"{API_BASE}/scenarios/{SCENARIO_ID}", data=json.dumps(scen_payload).encode('utf-8'), headers=headers, method='PUT')
    with urllib.request.urlopen(req_s) as resp:
        res_s = json.loads(resp.read().decode('utf-8'))
        print(f"  [OK] Scenario updated! Name: '{res_s.get('name')}', Scenes: {len(res_s.get('premade_scenes', []))}")

    # Try setting location
    try:
        loc_ref = {
            "id": loc_data["id"],
            "_id": loc_data["id"],
            "name": loc_data["name"],
            "created_at": loc_data.get("created_at"),
            "updated_at": loc_data.get("updated_at")
        }
        req_sloc = urllib.request.Request(f"{API_BASE}/scenarios/{SCENARIO_ID}", data=json.dumps({"location": loc_ref}).encode('utf-8'), headers=headers, method='PUT')
        with urllib.request.urlopen(req_sloc) as resp:
            res_sloc = json.loads(resp.read().decode('utf-8'))
            print(f"  [OK] Scenario location linked successfully! Location: {res_sloc.get('location', {}).get('name')}")
    except Exception as e:
        print(f"  [NOTE] Location link direct dict: {e}")

if __name__ == '__main__':
    fix_all()
