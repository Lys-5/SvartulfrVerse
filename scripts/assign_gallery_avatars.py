import os
import sys
import json
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

def get_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

def get_gallery(token):
    url = f'{API_BASE}/{WORLD_ID}/gallery'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def put_lexicon(token, lid, body):
    url = f'{API_BASE}/lexicon/{lid}?world_id={WORLD_ID}'
    data = json.dumps(body).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=get_headers(token), method='PUT')
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def get_lexicon(token, lid):
    url = f'{API_BASE}/lexicon/{lid}?world_id={WORLD_ID}'
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

# Mappings of Gallery Title -> (Entity Type, Entity ID, Entity Display Name)
CHARACTER_MAPPINGS = [
    ("Kaladin", "character", "_b7QqV43D8pU1tewx4qenY", "Kaladin Nargathon"),
    ("zeera", "character", "_a6KYGdN3BWTgbYEbT4mx8", "Zeera Darkfire"),
    ("yael", "character", "_Ht3kV76zrCE9tPmDAYh8Q", "Yael"),
    ("wulfnic", "character", "_W9PLYt9ERTBJBXqKQL2en", "Wulfnic Bloodmoon"),
    ("warg", "character", "_bh8AHn7WKkNTnLjwXrUWE", "Varg Darkfire"),
    ("thomas", "character", "_pbNb7PrEanM1twU612VNg", "Tomas Matthews"),
    ("tate", "character", "_RQQcCAN4MHETcJLhXPe9k", "Tate"),
    ("sully", "character", "_E7kHtwcpVYedVkVTmMGKX", "Sullivan 'Sully' Jones"),
    ("stanley", "character", "_gqFXEaVj4aG9a8QL8R7f1", "Stanley Davies Sr."),
    ("stan", "character", "_C18UjnQzGMLcQaNW3UaKq", "Stanley Davies Jr."),
    ("santiago", "character", "_c643VDjNFzAMgj7xGKGXT", "Santiago Herrera"),
    ("roland", "character", "_2g1adXnHXcK62pVzGHUBm", "Roland Vickers"),
    ("rev", "character", "_DGkc2ALEYzNJ6mqGCW1KC", "Rev"),
    ("radek", "character", "_4bazKCAbPMmc19HzHAphC", "Radek"),
    ("noah", "character", "_r42cVzMjcGTAx7bR1DQVt", "Noah Douglas Bloodmoon"),
    ("nixara", "character", "_fmzBDjDn3Gnq2hXKy7tY6", "Nixara Bloodmoon"),
    ("nikolai", "character", "_AdCJWrQaTgC7xkPQECrtK", "Nikolaj Jökull"),
    ("malachia", "character", "_rAcN9GXD1Le4WxY28e49W", "Malachia Douglas Bloodmoon"),
    ("mac", "character", "_YY8VbpgzYk4dfFAL78rM3", "Mackenzie Sanchez-Rogers"),
    ("logan", "character", "_JL37wK9PQMNDChULCDrWj", "Logan Douglas"),
    ("loewe", "character", "_E2A8prBrWg1q9zNjAR7kQ", "Professor Loewe"),
    ("kian", "character", "_kc7TyfPDQwUALKXcmTMxQ", "Kian"),
    ("jasper", "character", "_x3VY2kcbaDbKyCqywGeET", "Jasper Douglas Bloodmoon"),
    ("jasmin", "character", "_mfjaQDYUnAhLG8UggXg6N", "Jasmin Thompson"),
    ("janice", "character", "_DKY9cDLMUaYpELYAdckH2", "Janice Thompson"),
    ("iordan", "character", "_QfcJQRWUV2yfHGUUjLD8V", "Iordan R. Vess"),
    ("hank", "character", "_4GdzX4McREFg4zRpEqth2", "Hank Thompson"),
    ("Goran", "character", "_JQGgmwyA3qRaTLWck3GjX", "Goran"),
    ("finn", "character", "_PQHGb4gL2LwDhNDrLFa3A", "Finnegan Novak"),
    ("fenris-full", "character", "_wpMTPQ2VVA2pWqJ3cMztJ", "Fenris"),
    ("fade", "character", "_mbBqR74dFceBFB4YegpyN", "Fade Greymoor"),
    ("eris", "character", "_q1n7hcz23ThY63JGEjdNq", "Eris Davies"),
    ("erik", "character", "_d44gDc8N18kkbEhAcfUCG", "Erik Douglas"),
    ("edric", "character", "_YJQ4cjdrT7brm7HWVkf3K", "Edric Douglas"),
    ("dullahan", "character", "_F8ee4UpyLr7Fyr69KKhzV", "Dullahan"),
    ("dominic", "character", "_dDXdeJrcYHbwagGFQVKQR", "Dominic Rogers"),
    ("danny", "character", "_VGAN3gQXchpTC2VFAcKUH", "Daniel 'Danny' Boone"),
    ("chase", "character", "_TLxzk97WmgYCA47nkDCVy", "Chase Anderson"),
    ("brak", "character", "_AycV4d9dJRBakCmdH4q4J", "Brak Ironfist"),
    ("barkley", "character", "_EXFAYyRCjRU19eebCFfXz", "Barkley Rover"),
    ("ballantine", "character", "_13rj1V7hPaJ2QederUYkx", "Ruaraidh 'Rory' Ballantine"),
    ("bailey", "character", "_eF7HAqWkLLYhQwt2tm4rn", "Bailey Rogers"),
    ("aries", "character", "_F4qM3efBRVyQnXXUxVqH7", "Harper Aries"),
    ("ariadne", "character", "_q1rYKHndN64QUgjHQazXB", "Ariadne Cirillo"),
    ("alicia", "character", "_8CCMxWyPxRBaC1f2ycDqe", "Alicia Virtuoso")
]

LEXICON_MAPPINGS = [
    ("wren", "lexicon", "_QLeJFGFWL2GrqwGbtfUAG", "Wren Lark"),
    ("griven", "lexicon", "_FkXtyrhQMhCpg7N6gm1Wm", "Asag Beast (Griven)"),
    ("alistar", "lexicon", "_daK4mwDzDLbCYQn4j2JpM", "Alistair DeVille")
]

def main():
    token = get_auth_token()
    print("Token ottenuto.\n")

    # 1. Load Gallery
    gallery = get_gallery(token)
    gallery_map = {item['title']: item['imageURL'] for item in gallery if item.get('type') == 'avatar'}
    print(f"Caricati {len(gallery_map)} avatar dalla gallery.\n")

    # 2. Update Characters
    print("=== 1. AGGIORNAMENTO AVATAR CHARACTER ===")
    success_chars = 0
    for title, typ, cid, name in CHARACTER_MAPPINGS:
        img_url = gallery_map.get(title)
        if not img_url:
            print(f"  [WARN] Nessun URL trovato per '{title}'")
            continue
        try:
            put_char(token, cid, {'avatar': img_url})
            # Verify
            live = get_char(token, cid)
            if live.get('avatar') == img_url:
                success_chars += 1
                print(f"  [OK] {name:30s} ({cid}) -> {title}")
            else:
                print(f"  [FAIL] {name} verifica fallita: {live.get('avatar')}")
        except Exception as e:
            print(f"  [ERRORE] {name} ({cid}): {e}")

    # 3. Update Lexicon NPCs / Creatures
    print("\n=== 2. AGGIORNAMENTO AVATAR LEXICON ===")
    success_lex = 0
    for title, typ, lid, name in LEXICON_MAPPINGS:
        img_url = gallery_map.get(title)
        if not img_url:
            print(f"  [WARN] Nessun URL trovato per '{title}'")
            continue
        try:
            put_lexicon(token, lid, {'avatar': img_url})
            live = get_lexicon(token, lid)
            if live.get('avatar') == img_url:
                success_lex += 1
                print(f"  [OK] {name:30s} ({lid}) -> {title}")
            else:
                print(f"  [FAIL] {name} verifica fallita: {live.get('avatar')}")
        except Exception as e:
            print(f"  [ERRORE] {name} ({lid}): {e}")

    # 4. Update Alyssa & Alyssa Outfits
    print("\n=== 3. AGGIORNAMENTO ALYSSA E OUTFITS ===")
    alyssa_cid = '_MXcEC8Y6B3BNm3b1ttHj6'
    alyssa = get_char(token, alyssa_cid)
    alyssa_main_av = gallery_map.get('alyssa')
    
    outfits = alyssa.get('outfits', [])
    updated_outfits = []
    outfit_updated_count = 0
    for o in outfits:
        oname = o['name']
        gallery_key = f"alyssa_{oname.lower()}"
        outfit_img = gallery_map.get(gallery_key)
        if outfit_img:
            o_copy = dict(o)
            o_copy['avatar'] = outfit_img
            updated_outfits.append(o_copy)
            outfit_updated_count += 1
            print(f"  [OUTFIT OK] {oname:15s} -> {gallery_key}")
        else:
            updated_outfits.append(o)
            print(f"  [OUTFIT SKIP] {oname:15s} (nessun match in gallery)")

    alyssa_payload = {
        'avatar': alyssa_main_av,
        'outfits': updated_outfits
    }
    put_char(token, alyssa_cid, alyssa_payload)
    alyssa_live = get_char(token, alyssa_cid)
    print(f"\nAlyssa main avatar verificato: {alyssa_live.get('avatar') == alyssa_main_av}")
    print(f"Outfits aggiornati verificati: {len(alyssa_live.get('outfits', []))} presenti, {outfit_updated_count} con nuovi avatar")

    print(f"\nRiepilogo finale:")
    print(f"- Characters aggiornati: {success_chars + 1} (inclusa Alyssa)")
    print(f"- Outfits aggiornati: {outfit_updated_count}")
    print(f"- Lexicon aggiornati: {success_lex}")

if __name__ == '__main__':
    main()
