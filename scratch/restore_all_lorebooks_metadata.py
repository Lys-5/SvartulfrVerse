import urllib.request
import urllib.error
import json
import pathlib
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'

LOREBOOKS_META = [
    {
        'id': '_gwwCxCfQ6PQaLEjAQVpJL',
        'name': 'Svartúlfr - Lorebook I',
        'description': 'Lupine Social Ecology (LSE) Tetralogy, Rune Matrix, Founding Bloodlines, House Douglas, and Core World Lore.',
    },
    {
        'id': '_HfG7TeV6MJyj6bxMwxkpt',
        'name': 'Svartúlfr - Lorebook II',
        'description': 'Dead Dog Motel (DDM) Voidspace, Contracts Board, Economy, Artefacts, and Metropolitan Underworld Lore.',
    },
    {
        'id': '_9zWTGqYJNJ4BCDMj8gfcD',
        'name': 'Svartúlfr - Lorebook III (SUCC & Underworld)',
        'description': 'Supernatural University of Central California (SUCC), Campus life, fraternities, CUMS rivalry, Bakersfield rural district, and Underworld connections.',
    },
    {
        'id': '_EjXxkmPVhpCXg8xABpFkK',
        'name': 'Svartúlfr - Location',
        'description': 'Comprehensive structured locations across Blackwood City, Villa Douglas, Seven Hills, Solarton, SUCC Campus, and surrounding territories.',
    },
    {
        'id': '_zwEqgEEzh12X6gHVmMKKC',
        'name': 'Svartúlfr - NPC Primary',
        'description': 'Primary recurring NPC profiles, Douglas family members, Pack of Seven Hills, and intimate character memories.',
    },
    {
        'id': '_Uht3Ckz44JBDrPnUHq7LV',
        'name': 'Svartúlfr - NPC Secondary',
        'description': 'Secondary and tertiary supernatural NPCs across Blackwood City, SUCC campus factions, Underworld figures, and regional contacts.',
    },
]

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

for item in LOREBOOKS_META:
    lid = item['id']
    name = item['name']
    desc = item['description']
    
    print(f"\n--- Restoring {name} ({lid}) ---")
    
    # 1. Fetch current live data
    get_req = urllib.request.Request(f'{API_BASE}/lorebooks/{lid}', headers=headers)
    try:
        with urllib.request.urlopen(get_req, timeout=30) as resp:
            curr = json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {lid}: {e}")
        continue

    entries = curr.get('entries', [])
    lexicon = curr.get('lexicon', [])
    
    print(f"Current live entries: {len(entries)} | lexicon: {len(lexicon)}")

    payload = {
        'name': name,
        'description': desc,
        'visibility': 'private',
        'rating': 'explicit',
        'scan_depth': 5,
        'token_budget': 5000,
        'recursive_scanning': True,
        'entries': entries,
        'lexicon': lexicon,
    }

    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    print(f"Payload size: {len(body)} bytes")
    
    put_req = urllib.request.Request(f'{API_BASE}/lorebooks/{lid}', data=body, headers=headers, method='PUT')
    try:
        with urllib.request.urlopen(put_req, timeout=60) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            print(f"SUCCESS HTTP {resp.status}!")
            print(f"  Saved name: {repr(res.get('name'))}")
            print(f"  Saved description: {repr(res.get('description'))[:60]}...")
            print(f"  Saved visibility: {repr(res.get('visibility'))}")
            print(f"  Saved rating: {repr(res.get('rating'))}")
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='ignore')
        print(f"HTTPError {e.code}: {err[:300]}")
        # If payload too large, try sending with only lexicon if entries is empty or large
        if e.code == 413 or 'large' in err.lower():
            print("Payload too large, falling back to payload without entries...")
            payload_fallback = {
                'name': name,
                'description': desc,
                'visibility': 'private',
                'rating': 'explicit',
                'scan_depth': 5,
                'token_budget': 5000,
                'recursive_scanning': True,
                'lexicon': lexicon,
            }
            body_fb = json.dumps(payload_fallback, ensure_ascii=False).encode('utf-8')
            put_req_fb = urllib.request.Request(f'{API_BASE}/lorebooks/{lid}', data=body_fb, headers=headers, method='PUT')
            with urllib.request.urlopen(put_req_fb, timeout=60) as resp_fb:
                res_fb = json.loads(resp_fb.read().decode('utf-8'))
                print(f"SUCCESS HTTP {resp_fb.status} (fallback)!")
                print(f"  Saved name: {repr(res_fb.get('name'))}")
    except Exception as e:
        print(f"Error on PUT {lid}: {e}")

    time.sleep(1)

print("\nAll 6 Lorebooks metadata restoration complete!")
