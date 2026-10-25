import json
import pathlib
import sys
import time
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.insert(0, str(ROOT / 'scratch'))
import refresh_token

TOKEN = refresh_token.refresh()
API_APP = 'https://app.wyvern.chat/api'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'User-Agent': 'AuditorBot/1.0'
}

EDITABLE_FIELDS = [
    'name', 'display_name', 'avatar', 'description', 'personality', 'mes_example',
    'first_mes', 'scenario', 'post_history_instructions', 'pre_history_instructions',
    'visual_description', 'creator_notes', 'model_url', 'soundcloud_url', 'character_note',
    'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating', 'chat_name',
    'pronouns', 'outfits', 'default_outfit', 'shared_info', 'alternate_greetings',
    'secretFields', 'secrets', 'fields', 'commands', 'metadata'
]

def api_call(method, url, data=None, timeout=60):
    payload = json.dumps(data).encode('utf-8') if data is not None else None
    req = urllib.request.Request(url, data=payload, headers=HEADERS, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        return e.code, body

def normalize_pronouns(p):
    if not isinstance(p, dict):
        return {
            'pronoun_subjective': 'they',
            'pronoun_objective': 'them',
            'pronoun_possessive_determiner': 'their',
            'pronoun_possessive_pronoun': 'theirs',
            'pronoun_reflexive': 'themselves'
        }
    return {
        'pronoun_subjective': p.get('pronoun_subjective') or 'they',
        'pronoun_objective': p.get('pronoun_objective') or 'them',
        'pronoun_possessive_determiner': p.get('pronoun_possessive_determiner') or 'their',
        'pronoun_possessive_pronoun': p.get('pronoun_possessive_pronoun') or 'theirs',
        'pronoun_reflexive': p.get('pronoun_reflexive') or 'themselves'
    }

def deploy():
    print("=" * 70)
    print("DEPLOYING ROUND 4 UPDATES TO LIVE WYVERN API")
    print("=" * 70)

    # 1. DEPLOY WULFNIC CARD (_HEQQbbRFwKdG8QE2Fh1z1)
    print("\n--- 1. Deploying Wulfnic Character Card (_HEQQbbRFwKdG8QE2Fh1z1) ---")
    card_path = ROOT / 'FINAL' / 'Wulfnic_Bloodmoon_card.json'
    c = json.loads(card_path.read_text(encoding='utf-8'))
    payload_card = {k: c[k] for k in EDITABLE_FIELDS if k in c}
    if 'pronouns' in payload_card:
        payload_card['pronouns'] = normalize_pronouns(payload_card.get('pronouns'))
    payload_card['visibility'] = 'private'

    st, res = api_call('PUT', f'{API_APP}/characters/_HEQQbbRFwKdG8QE2Fh1z1', payload_card)
    print(f"PUT /characters/_HEQQbbRFwKdG8QE2Fh1z1 -> status={st}")
    assert st in (200, 201), f"Failed deploying Wulfnic card: {st} {res}"
    time.sleep(2)

    # 2. DEPLOY LOREBOOKS
    lorebooks_to_deploy = [
        ('_zwEqgEEzh12X6gHVmMKKC', 'Svartulfr_NPC_Primary.json', 'NPC Primary'),
        ('_gwwCxCfQ6PQaLEjAQVpJL', 'Svartulfr_Lorebook_I.json', 'Lorebook I'),
        ('_HfG7TeV6MJyj6bxMwxkpt', 'Svartulfr_Lorebook_II.json', 'Lorebook II'),
    ]

    print("\n--- 2. Deploying Lorebooks to Wyvern API ---")
    for lid, fname, label in lorebooks_to_deploy:
        fpath = ROOT / 'FINAL' / fname
        d = json.loads(fpath.read_text(encoding='utf-8'))
        entries = d.get('lexicon') or d.get('entries') or []
        payload_lb = {
            'name': d.get('name'),
            'description': d.get('description'),
            'visibility': 'private',
            'rating': 'explicit',
            'scan_depth': d.get('scan_depth', 5),
            'token_budget': d.get('token_budget', 5000),
            'recursive_scanning': d.get('recursive_scanning', True),
            'lexicon': entries
        }
        st, res = api_call('PUT', f'{API_APP}/lorebooks/{lid}', payload_lb, timeout=120)
        saved_cnt = len(res.get('lexicon', res.get('entries', []))) if isinstance(res, dict) else -1
        print(f"PUT /lorebooks/{lid} ({label}) -> status={st} | sent={len(entries)} | saved={saved_cnt}")
        assert st in (200, 201), f"Failed deploying lorebook {label}: {st} {res}"
        time.sleep(2)

    print("\n" + "=" * 70)
    print("ALL ROUND 4 DEPLOYMENTS COMPLETED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == '__main__':
    deploy()
