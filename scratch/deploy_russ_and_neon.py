import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'
FINAL_DIR = ROOT / 'FINAL'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

STRIP_FIELDS = {
    'id', '_id', 'created_at', 'updated_at', 'creator', 'status',
    'statistics_record', 'entity_statistics', 'approval_date', 'visibility_submitted_at',
    'last_public_submitted_at', 'rejection_date', 'approval_comment', 'rejection_comment',
    'updated_at_by_user', 'moderation_hold', 'moderation_events', 'token_count',
    'likes', 'liked_by_me', 'boosted_by_me', 'vanity_slug', 'wyldfire_code'
}

cards_to_deploy = [
    ('russ', 'Russ_card.json'),
    ('neon_purr', 'Neon_Purr_card.json'),
]

deployed = {}

for key, fname in cards_to_deploy:
    fpath = FINAL_DIR / fname
    card = json.loads(fpath.read_text(encoding='utf-8'))
    payload = {k: v for k, v in card.items() if k not in STRIP_FIELDS}
    
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(f"{API_BASE}/characters", data=body, headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            new_id = res.get('_id') or res.get('id')
            print(f"SUCCESS POST /characters ({fname}) -> Status {resp.status} | ID: {new_id}")
            if new_id:
                card['id'] = new_id
                card['_id'] = new_id
                fpath.write_text(json.dumps(card, indent=2, ensure_ascii=False), encoding='utf-8')
                deployed[key] = {'id': new_id, 'file': fname, 'name': card.get('name')}
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='ignore')
        print(f"Error deploying {fname}: HTTP {e.code} - {err[:300]}")

print("\nDeployment complete:", deployed)
