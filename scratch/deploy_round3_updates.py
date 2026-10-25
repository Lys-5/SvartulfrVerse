import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
sys.path.insert(0, str(ROOT / 'scratch'))
import refresh_token

TOKEN = refresh_token.refresh()
API_APP = 'https://app.wyvern.chat/api'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'AuditorBot/1.0'
}

def api_call(method: str, url: str, payload=None, timeout=90):
    data = json.dumps(payload, separators=(',', ':'), ensure_ascii=False).encode('utf-8') if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode('utf-8')
            return resp.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode('utf-8', errors='ignore')
        print(f"HTTP {e.code} on {method} {url}: {err_body[:300]}")
        return e.code, {'error': err_body}
    except Exception as e:
        print(f"Exception on {method} {url}: {e}")
        return 0, {'error': str(e)}

EDITABLE_FIELDS = [
    'name', 'avatar', 'description', 'personality', 'mes_example', 'creator_notes',
    'post_history_instructions', 'pre_history_instructions', 'visual_description',
    'first_mes', 'alternate_greetings', 'scenario', 'model_url', 'soundcloud_url',
    'character_note', 'tagline', 'backgroundURL', 'tags', 'community_tags', 'rating',
    'chat_name', 'pronouns', 'outfits', 'default_outfit', 'shared_info',
    'secretFields', 'secrets', 'fields', 'commands', 'lexicon', 'can_fork',
    'linked_world', 'metadata', 'prompt_assembly', 'first_message_name',
    'enable_advanced_greetings', 'greetings', 'gallery', 'lorebooks', 'personas',
    'sprite_sets', 'regex_scripts', 'visibility'
]

def normalize_pronouns(p):
    if isinstance(p, dict):
        return p
    if isinstance(p, str):
        if 'she' in p.lower():
            return {
                'pronoun_subjective': 'she',
                'pronoun_objective': 'her',
                'pronoun_possessive_determiner': 'her',
                'pronoun_possessive_pronoun': 'hers',
                'pronoun_reflexive': 'herself'
            }
        else:
            return {
                'pronoun_subjective': 'he',
                'pronoun_objective': 'him',
                'pronoun_possessive_determiner': 'his',
                'pronoun_possessive_pronoun': 'his',
                'pronoun_reflexive': 'himself'
            }
    return {
        'pronoun_subjective': 'they',
        'pronoun_objective': 'them',
        'pronoun_possessive_determiner': 'their',
        'pronoun_possessive_pronoun': 'theirs',
        'pronoun_reflexive': 'themselves'
    }

def deploy():
    print("=" * 70)
    print("DEPLOYING ROUND 3 UPDATES TO LIVE WYVERN API")
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
        ('_Uht3Ckz44JBDrPnUHq7LV', 'Svartulfr_NPC_Secondary.json', 'NPC Secondary'),
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
    print("ALL ROUND 3 DEPLOYMENTS COMPLETED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == '__main__':
    deploy()
