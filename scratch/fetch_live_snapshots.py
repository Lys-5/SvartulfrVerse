import json
import urllib.request
import pathlib
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

def get_api(url):
    req = urllib.request.Request(url, headers={
        'Authorization': f'Bearer {TOKEN}',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def main():
    # 1. Master Scenario (app.wyvern.chat/api)
    scen = get_api('https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4')
    (ROOT / 'scratch' / 'live_scenario_latest.json').write_text(json.dumps(scen, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Scenario revision: {scen.get('revision')}, greetings: {len(scen.get('greetings', []))}, slots: {len(scen.get('slots', []))}, lorebooks: {len(scen.get('lorebook_ids', []))}")

    # 2. Check live cards for Wulfnic, Malachia, Alyssa, Edric, Russ
    cards = {
        'wulfnic': '_HEQQbbRFwKdG8QE2Fh1z1',
        'malachia': '_RDfz7XzTpM23LpPALVXHM',
        'alyssa_card': '_6exg3yPfe2eCDK4hTftkh',
        'edric': '_TbRM3EdxDjHFgqztTbCpL',
        'russ': '_wn6DkCcg3Xqa2Xpx9ttnT',
    }
    for name, cid in cards.items():
        time.sleep(1.0)
        c = get_api(f'https://api.wyvern.chat/characters/{cid}')
        (ROOT / 'scratch' / f'live_{name}.json').write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"Card {name} ({cid}): outfits={len(c.get('outfits') or [])}, rating={c.get('rating')}")

    # 3. Alyssa Persona
    time.sleep(1.0)
    ap = get_api('https://app.wyvern.chat/api/user-personas/persona_1786335754946')
    (ROOT / 'scratch' / 'live_alyssa_persona.json').write_text(json.dumps(ap, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Alyssa persona: outfits={len(ap.get('outfits') or [])}")

    # 4. Jasper Persona
    time.sleep(1.0)
    for pid in ['1792155173728', 'persona_1792155173728']:
        try:
            jp = get_api(f'https://app.wyvern.chat/api/user-personas/{pid}')
            (ROOT / 'scratch' / 'live_jasper_persona.json').write_text(json.dumps(jp, indent=2, ensure_ascii=False), encoding='utf-8')
            print(f"Jasper persona ({pid}): outfits={len(jp.get('outfits') or [])}")
            break
        except Exception as e:
            print(f"Jasper persona {pid} error: {e}")

if __name__ == '__main__':
    main()
