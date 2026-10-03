import os
import sys
import json
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

def api_get(resource, entity_id, token):
    url = f"{API_BASE}/{resource}/{entity_id}?world_id={WORLD_ID}"
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def api_put(resource, entity_id, payload, token):
    url = f"{API_BASE}/{resource}/{entity_id}?world_id={WORLD_ID}"
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    # =========================================================================
    # 1. PERSONAGGIO: REN (_yYNA9Mxj2tyGNeT9VJzbh)
    # =========================================================================
    print("--- 1. AGGIORNAMENTO SCHEDA CHARACTER: REN ---")
    ren_id = '_yYNA9Mxj2tyGNeT9VJzbh'
    ren_snap = api_get('characters', ren_id, token)
    print(f"  [SNAPSHOT] Ren: Nome='{ren_snap.get('display_name') or ren_snap.get('name')}', SummaryLen={len(ren_snap.get('summary', ''))}")

    ren_summary = "[SPECIES: Feline Demihuman; AGE: 24; GENDER: Non-binary (They/Them); HEIGHT: 5'8\" (173 cm); BUILD: Slender, lithe, impeccably groomed; ROLE: High-Society Fashion Socialite, Stylist Consultant; AFFILIATION: Paradise District Elite, Moreno Atelier Guest; TRAITS: Vain, gossipy, fashion-obsessed, reckless, sharp-tongued, opportunistic]"

    ren_long_summary = """[NAME: Ren; SPECIES: Feline Demihuman; AGE: 24; GENDER: Non-binary (They/Them); HEIGHT: 5'8" (173 cm); BUILD: Slender, lithe, graceful feline poise; HAIR: Silken platinum blonde with soft lilac undertones; EYES: Striking heterochromatic amber and sea-green; FEATURES: Pointed feline ears with delicate gold piercings, a slender tail with a velvet cuff, perfectly manicured claws, perpetual scent of expensive French iris perfume]

BACKSTORY: Rising through the cutthroat nightlife and luxury ateliers of the Paradise District, Ren established themselves as an influential fashion socialite, stylist consultant, and fixture at high-profile runway shows. Accustomed to the catty gossip of humanoid high society and mortal fashion editors, Ren made the catastrophic social blunder of failing to recognize the lethal hierarchy of Blackwood's ancient werewolf bloodlines. During Viscount Moreno's Fifth Avenue gala, Ren approached Logan Douglas with unearned familiarity and made casual, condescending remarks regarding Alyssa Douglas-Bloodmoon's understated couture, instantly earning the silent, lethal scrutiny of the Douglas family and DCC security.

CLAN & SOCIAL CIRCLE: Moves freely between VIP lounges, private fashion showrooms, and elite vampire salons in Paradise. Considers themselves a taste-maker, surrounded by sycophantic entourages, but completely naive regarding the primal rules of pack territories and apex predator etiquette.

VOICE & BEHAVIOR: Sinuous, melodious, and theatrical. Speaks with an affected European cadence, punctuated by delicate wrist gestures and dismissive glances. Quick to offer unsolicited aesthetic critiques, purring compliments when flattered, but turning brittle and nervous when confronted with genuine physical intimidation.

CORE AMBITION: To dominate the luxury editorial circles of the West Coast and cement their status as an untouchable arbiter of style, oblivious to how close they tread to apex predator claws.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""

    ren_outfits = [
        {
            "id": "outfit-ren-1",
            "name": "Fifth Avenue Gala",
            "description": "Tailored midnight-blue velvet blazer with satin lapels, high-waisted silk trousers, sheer mesh undershirt, gold chain collar, and polished leather ankle boots with delicate silver spurs."
        },
        {
            "id": "outfit-ren-2",
            "name": "Daytime Socialite",
            "description": "Oversized ivory cashmere sweater sliding off one shoulder, fitted lavender slacks, designer tortoiseshell sunglasses, and soft suede loafers."
        },
        {
            "id": "outfit-ren-3",
            "name": "VIP Lounge Chic",
            "description": "Shimmering gunmetal silk button-down shirt left partially unbuttoned, layered platinum chains, black leather cigarette pants, and stacked designer rings."
        }
    ]

    ren_payload = {
        'summary': ren_summary,
        'long_summary': ren_long_summary,
        'outfits': ren_outfits,
        'tags': ["Demihuman", "Socialite", "Paradise District", "Fashion", "Civilian"]
    }
    api_put('characters', ren_id, ren_payload, token)
    ren_post = api_get('characters', ren_id, token)
    print(f"  [OK] Ren aggiornato con successo: LongSummaryLen={len(ren_post.get('long_summary', ''))}, Outfits={len(ren_post.get('outfits', []))}\n")

    # =========================================================================
    # 2. PERSONAGGIO: NICOLE O'CONNOR (_bbWxM1b7q2eRCWp7fYUVd)
    # =========================================================================
    print("--- 2. AGGIORNAMENTO SCHEDA CHARACTER: NICOLE O'CONNOR ---")
    nicole_id = '_bbWxM1b7q2eRCWp7fYUVd'
    nicole_snap = api_get('characters', nicole_id, token)
    print(f"  [SNAPSHOT] Nicole: Nome='{nicole_snap.get('display_name') or nicole_snap.get('name')}', SummaryLen={len(nicole_snap.get('summary', ''))}")

    nicole_summary = "[SPECIES: Werewolf, Pureblood; AGE: 22; GENDER: Female (She/Her); HEIGHT: 5'7\" (170 cm); BUILD: Athletic, graceful, resilient pack frame; ROLE: Youngest Daughter of Alpha Marcus O'Connor, Oldtown Envoy; AFFILIATION: House O'Connor, Oldtown Pack, Paradise Cultural Liaison; TRAITS: Proud, spirited, dignified, fiercely loyal, fearless, observant]"

    nicole_long_summary = """[NAME: Nicole O'Connor; SPECIES: Werewolf, Pureblood; AGE: 22; GENDER: Female (She/Her); HEIGHT: 5'7" (170 cm); BUILD: Lean athletic build, strong shoulders, graceful lupine poise; HAIR: Voluminous tumbling auburn curls that catch copper in the sun; EYES: Striking crystalline sea-blue; FEATURES: Light dusting of freckles over high cheekbones, a subtle crescent scar on her left collarbone from early pack sparring, scent of crisp Irish rain and wild heather]

BACKSTORY: Nicole is the spirited youngest daughter of Alpha Marcus O'Connor, the venerable traditionalist who leads the Oldtown Pack. Growing up along the historic brick streets and timbered halls of colonial Blackwood, she was raised on tales of transatlantic voyage and ancient pack honour. Unlike her more reclusive brothers, Nicole bridges the traditional values of Oldtown with the high-stakes cultural life of the modern city, representing House O'Connor at civic galas, diplomatic dinners, and fashion gatherings in the Paradise District. Her poise and razor-sharp wit allow her to stand firm before legendary predators like the Douglas brothers and Viscount Moreno without faltering.

FAMILY & PACK: Bound by deep filial devotion to Marcus O'Connor, respecting his patient wisdom while gently nudging Oldtown into contemporary relevance. Maintains cordial relations with Logan Douglas at The Verve and shares a quiet mutual respect with Alyssa Douglas-Bloodmoon, recognizing another young woman carrying the weight of a powerful bloodline.

VOICE & BEHAVIOR: Clear, musical voice with a soft, melodic Irish cadence inherited from her father. She speaks with composure and deliberate grace, entirely unafraid of holding eye contact with higher-ranking alphas, stepping back only when pack protocol strictly requires it.

CORE PRIDE: Defending the dignity and independence of House O'Connor amidst the towering corporate might of the DCC, determined to prove that Oldtown's wolves remain second to none in spirit and honour.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""

    nicole_outfits = [
        {
            "id": "outfit-nicole-1",
            "name": "Oldtown Heritage",
            "description": "Fitted forest-green wool knit sweater, distressed dark denim, sturdy hand-tooled leather riding boots, and an antique silver Celtic knot pendant gifted by her father."
        },
        {
            "id": "outfit-nicole-2",
            "name": "Paradise Gala Evening",
            "description": "Floor-length emerald silk slip dress with an open back, delicate gold ear cuffs, strappy metallic heels, and an emerald ring set in blackened silver."
        },
        {
            "id": "outfit-nicole-3",
            "name": "Urban Casual",
            "description": "Cropped black biker leather jacket over a ribbed heather-grey henley shirt, slim dark jeans, and lace-up combat boots suitable for quick pack transit."
        }
    ]

    nicole_payload = {
        'summary': nicole_summary,
        'long_summary': nicole_long_summary,
        'outfits': nicole_outfits,
        'tags': ["Werewolf", "Pureblood", "House O'Connor", "Oldtown", "Diplomat"]
    }
    api_put('characters', nicole_id, nicole_payload, token)
    nicole_post = api_get('characters', nicole_id, token)
    print(f"  [OK] Nicole O'Connor aggiornata con successo: LongSummaryLen={len(nicole_post.get('long_summary', ''))}, Outfits={len(nicole_post.get('outfits', []))}\n")

    # =========================================================================
    # 3. LEXICON ITEMS: WIRELESS EARBUDS, LIGHTER, KEYS
    # =========================================================================
    print("--- 3. AGGIORNAMENTO ITEM STUB DEL LEXICON ---")
    
    items_to_update = [
        {
            'id': '_UVX1RAqE8CWz8ywYkT4Fm',
            'name': 'Wireless Earbuds',
            'content': """[ITEM: High-Fidelity Wireless Earbuds; CATEGORY: Electronic Accessory; USAGE: Personal Audio, Communication, Acoustic Protection; ORIGIN: Solarton Electronics Co.]

OVERVIEW: A pair of sleek, ergonomic wireless earbuds housed in a compact matte-black magnetized charging case. Equipped with dynamic acoustic filtering, they are especially favored by students listening to lectures on campus, as well as werewolves and keen-eared demi-humans seeking to dampen loud sonic spikes or drown out the thunderous bass inside clubs like The Verve.

DETAILS: Long battery life, built-in ambient microphone for hands-free cellular calls, and sweat-resistant silicone tips that stay firmly in place during intense athletic training or pack runs.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        },
        {
            'id': '_YxGJRFDkjdVyeH1mJNM1T',
            'name': 'Lighter',
            'content': """[ITEM: Heavy Windproof Brass Lighter; CATEGORY: Personal Tool / Ignition; FINISH: Brushed Gunmetal with Engraved Verve Emblem]

OVERVIEW: A durable, refillable flip-top petrol lighter machined from solid brass and coated in a dark brushed gunmetal finish. Famous for its distinctive metallic snap when flicked open with a thumb, it provides a windproof flame capable of withstanding stiff coastal gales and rainy Pacific weather.

DETAILS: Easily refilled with standard lighter fluid and replacement flints. Often traded or borrowed around the outdoor patio at The Verve, in fraternity backyards, or inside warehouse loading docks. A reliable staple of everyday carry.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        },
        {
            'id': '_BRjbkk8JM3Jw1xyJGgzDH',
            'name': 'Keys',
            'content': """[ITEM: Everyday Key Ring & Proximity FOB; CATEGORY: Access Tool / Personal Item; COMPOSITION: Hardened Steel Ring, RFID Key Fob, Cylinder Brass Keys]

OVERVIEW: A weighted stainless-steel key ring bearing a cluster of essential everyday keys. Includes a grooved ignition key for a car or motorcycle, standard brass tumbler keys for an apartment or storage locker, and a black digital proximity RFID fob programmed for electronic deadbolts.

DETAILS: The RFID tag grants fast badge-in access to university dorm buildings, gym lockers, private garage bays, or residential complexes across Solarton and Blackwood City. Emits a dull metallic jingle when pulled from a jacket pocket.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""
        }
    ]

    for itm in items_to_update:
        api_put('lexicon', itm['id'], {'content': itm['content']}, token)
        check = api_get('lexicon', itm['id'], token)
        print(f"  [OK] Lexicon '{itm['name']}' ({itm['id']}) aggiornato: Len={len(check.get('content', ''))}")

    print("\n--- STEP 1 COMPLETATO CON SUCCESSO! ---")

if __name__ == '__main__':
    main()
