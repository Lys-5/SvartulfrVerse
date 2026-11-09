import json
import urllib.request
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRATCH = ROOT / 'scratch'
FINAL = ROOT / 'FINAL'

TOKEN = (SCRATCH / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

CANONICAL_ERAS = [
    {
        "name": "Epoca Primordiale & Patto dei Nove (827 - 1200 CE)",
        "description": "I Firstborn primordiali, radici norrene e vincolo sacro di sangue.",
        "start_position": 0,
        "end_position": 3261144,
        "display_order": 1,
        "tags": ["primordiale", "norreno", "patto_dei_nove", "firstborn"]
    },
    {
        "name": "Era dei Reclusi & Colonizzazione Costiera (1200 - 1848 CE)",
        "description": "Espansione della Casata Douglas in California, isolamento nelle foreste ancestrali di Blackwood.",
        "start_position": 3261144,
        "end_position": 8941392,
        "display_order": 2,
        "tags": ["reclusi", "douglas", "colonizzazione", "blackwood_forest"]
    },
    {
        "name": "Era della Modernita & Industrializzazione (1848 - 2000 CE)",
        "description": "Fondazione di Blackwood City, ascesa della DMHA e prime aperture di coesistenza.",
        "start_position": 8941392,
        "end_position": 10273800,
        "display_order": 3,
        "tags": ["modernita", "industrializzazione", "dmha", "blackwood_city"]
    },
    {
        "name": "Era Contemporanea & Integrazione SUCC (2000 - Presente 2024 CE)",
        "description": "Coesistenza accademica e metropolitana tra demi-umani, licantropi, vampiri e umani risvegliati a Solarton University.",
        "start_position": 10273800,
        "display_order": 4,
        "tags": ["contemporanea", "succ", "solarton", "integrazione", "2024"]
    }
]

def sync_canonical_eras():
    get_url = f"https://app.wyvern.chat/api/worlds/eras/world/{WORLD_ID}"
    req = urllib.request.Request(get_url, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        existing = json.loads(resp.read().decode('utf-8'))
    
    print(f"Retrieved {len(existing)} existing eras from World {WORLD_ID}.")
    order_to_existing = {e.get('display_order'): e for e in existing}
    
    post_url = "https://app.wyvern.chat/api/worlds/eras/world"
    for era_def in CANONICAL_ERAS:
        order = era_def['display_order']
        if order in order_to_existing:
            # Update existing era via PUT
            current = order_to_existing[order]
            eid = current.get('id') or current.get('_id')
            put_url = f"https://app.wyvern.chat/api/worlds/eras/world/era/{eid}"
            put_req = urllib.request.Request(
                put_url,
                data=json.dumps(era_def).encode('utf-8'),
                headers=HEADERS,
                method='PUT'
            )
            with urllib.request.urlopen(put_req) as put_resp:
                res = json.loads(put_resp.read().decode('utf-8'))
                print(f"[200] Updated Era [{order}]: '{res.get('name')}' ({eid})")
        else:
            # Create era via POST
            payload = {"world_id": WORLD_ID, **era_def}
            create_req = urllib.request.Request(
                post_url,
                data=json.dumps(payload).encode('utf-8'),
                headers=HEADERS,
                method='POST'
            )
            with urllib.request.urlopen(create_req) as post_resp:
                res = json.loads(post_resp.read().decode('utf-8'))
                print(f"[200] Created Era [{order}]: '{res.get('name')}' ({res.get('id')})")
                
    # Final GET verification
    verify_req = urllib.request.Request(get_url, headers=HEADERS)
    with urllib.request.urlopen(verify_req) as v_resp:
        verified = json.loads(v_resp.read().decode('utf-8'))
        
    verified.sort(key=lambda x: x.get('display_order', 0))
    print(f"\n--- VERIFIED {len(verified)} CANONICAL ERAS ---")
    for v in verified:
        print(f"[{v.get('display_order')}] ID: {v.get('id')} | Name: '{v.get('name')}' | Range: {v.get('start_position')} -> {v.get('end_position')}")
        
    final_path = FINAL / 'Svartulfr_World_Eras.json'
    with open(final_path, 'w', encoding='utf-8') as f:
        json.dump(verified, f, indent=2, ensure_ascii=False)
    print(f"Saved snapshot to {final_path}")
    
    scratch_path = SCRATCH / 'live_world__YpX47fNraQFw2dD7TdycJ_eras.json'
    with open(scratch_path, 'w', encoding='utf-8') as f:
        json.dump(verified, f, indent=2, ensure_ascii=False)
    print(f"Saved snapshot to {scratch_path}")

if __name__ == '__main__':
    sync_canonical_eras()
