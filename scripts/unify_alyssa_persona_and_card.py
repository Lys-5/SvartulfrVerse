import json
import urllib.request
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
PERSONA_ID = 'persona_1786335754946'
CARD_ID = '_MXcEC8Y6B3BNm3b1ttHj6'

def main():
    token = get_auth_token()
    print("Token ottenuto.\n")

    # 1. Fetch gallery map
    req = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/{WORLD_ID}/gallery', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    gal = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
    gal_map = {item['title']: item['imageURL'] for item in gal}

    # 2. Fetch live Persona
    req_p = urllib.request.Request(f'https://app.wyvern.chat/api/user-personas/{PERSONA_ID}', headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    persona = json.loads(urllib.request.urlopen(req_p).read().decode('utf-8'))

    # 3. Fetch live Card
    card = get_char(token, CARD_ID)

    print("=== 1. PREPARAZIONE OUTFIT UNIFICATI (17 OUTFITS) ===")
    
    # Unified outfits definition:
    # We will map each outfit name to its gallery avatar and descriptions
    outfit_defs = [
        ("Naked", "alyssa_nude", "outfit_yCiaXuagMWD331WV6u0ZU"),
        ("Tactic", "alyssa_tactic", "outfit_39I2lSLYfR3h4XlFMrgD9"),
        ("Summer", "alyssa_summer", "outfit_UT8FhemAi1PDZeh0Q11wC"),
        ("Winter", "alyssa_winter", "outfit_CFmgNuu4-XM5dcuDR86v1"),
        ("Beach", "alyssa_beach", "outfit__LkfgrzSO5h3xqgt8JsS0"),
        ("Sleep", "alyssa_sleep", "outfit_PYnUack2KVHlr-XbEMyiU"),
        ("Fest", "alyssa_fest", "outfit_QfmHYyqyke_MHFpLBc7UH"),
        ("Academy", "alyssa_academy", "outfit_mCfqp4V948Uvth9qrQtZm"),
        ("Sport", "alyssa_sport", "outfit_Vk_jZ6sT0MczcwFSpRNQe"),
        ("Spring", "alyssa_spring", "outfit_SQza_2JPLeGhgQrAjfyAf"),
        ("Hybrid", "alyssa_hybrid", "outfit_nPERIvpkjbT9anBosZYMJ"),
        ("Fullshift", "alyssa_fullshift", "outfit_s0b5DFsbIKbNQibgsOV8v"),
        ("Formal", "alyssa_formal", "outfit_7KnpWhND_GAqTDtRh2V5y"),
        ("Clinic", "alyssa_clinic", "outfit_ibAlc3Tx9E-b1WDgaQYe1"),
        ("Biker", "alyssa_biker", "outfit_plVtRGVyVzOZ1k96ikii0"),
        ("Dinner", "alyssa_dinner", "outfit_LFodvm40HL7QjHU92cDXM"),
        ("Angelo Moreno Couture", None, "outfit_0mUBHnzgq-GKKOCTYiebP")
    ]

    # Map existing descriptions from card or persona
    p_outfit_map = {o['name'].lower(): o for o in persona['outfits']}
    c_outfit_map = {o['name'].lower(): o for o in card['outfits']}

    card_outfits_payload = []
    persona_outfits_payload = []

    for name, gal_title, persona_oid in outfit_defs:
        key = name.lower()
        po = p_outfit_map.get(key, {})
        co = c_outfit_map.get(key, {})

        # Determine image URL
        if gal_title and gal_title in gal_map:
            img_url = gal_map[gal_title]
        else:
            img_url = po.get('image_url') or co.get('avatar')

        # Description: for Card use "Alyssa" (no {{user}}), for Persona keep rich text
        desc_card = co.get('description') or po.get('description', '')
        # Ensure Card description uses "Alyssa"
        desc_card = desc_card.replace("{{user}}", "Alyssa")
        desc_card = desc_card.replace("{{#ifEquals (lower (playerGet \"species\")) \"werewolf\"}}", "")
        desc_card = desc_card.replace("{{/ifEquals}}", "")

        # Description for Persona
        desc_persona = po.get('description') or desc_card

        # Card outfit item
        card_outfit_item = {
            "id": co.get('id') or f"outfit-alyssa-{key.replace(' ', '-')}",
            "name": name,
            "description": desc_card.strip(),
            "avatar": img_url
        }
        card_outfits_payload.append(card_outfit_item)

        # Persona outfit item
        persona_outfit_item = {
            "id": persona_oid,
            "name": name.lower() if name != "Angelo Moreno Couture" else name,
            "description": desc_persona.strip(),
            "image_url": img_url,
            "avatar": img_url
        }
        persona_outfits_payload.append(persona_outfit_item)

    print(f"Creati {len(card_outfits_payload)} outfit per Card.")
    print(f"Creati {len(persona_outfits_payload)} outfit per Persona.")

    # 4. Update World Character Card
    print("\n=== 2. SCRITTURA WORLD CHARACTER CARD ===")
    unified_description = persona['description'].strip()
    # Ensure long_summary matches
    card_update = {
        "display_name": "Alyssa Douglas Bloodmoon",
        "first_name": "Alyssa",
        "last_name": "Douglas Bloodmoon",
        "avatar": gal_map['alyssa'],
        "long_summary": unified_description,
        "outfits": card_outfits_payload
    }
    put_char(token, CARD_ID, card_update)
    card_verified = get_char(token, CARD_ID)
    print(f"Card aggiornata! Outfits count: {len(card_verified.get('outfits', []))}")
    print(f"Card avatar: {card_verified.get('avatar')}")
    print(f"Card long_summary len: {len(card_verified.get('long_summary', ''))}")

    # 5. Update Persona
    print("\n=== 3. SCRITTURA USER PERSONA ===")
    persona_update_payload = dict(persona)
    persona_update_payload['avatar'] = gal_map['alyssa']
    persona_update_payload['outfits'] = persona_outfits_payload
    
    put_url = f'https://app.wyvern.chat/api/user-personas/{PERSONA_ID}'
    req_put = urllib.request.Request(
        put_url,
        data=json.dumps(persona_update_payload).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='PUT'
    )
    with urllib.request.urlopen(req_put) as resp:
        persona_res = json.loads(resp.read().decode('utf-8'))
    
    # Verify Persona
    req_p_verify = urllib.request.Request(put_url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    persona_verified = json.loads(urllib.request.urlopen(req_p_verify).read().decode('utf-8'))
    print(f"Persona aggiornata! Outfits count: {len(persona_verified.get('outfits', []))}")
    print(f"Persona avatar: {persona_verified.get('avatar')}")

    print("\nUnificazione completata con successo al 100%!")

if __name__ == '__main__':
    main()
