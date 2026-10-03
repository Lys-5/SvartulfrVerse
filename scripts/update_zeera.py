import sys, json, requests
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

API_BASE = 'https://app.wyvern.chat/api'
token = get_auth_token()

with open(r'd:\SvartulfrVerse\docs\zeera_live.json', 'r', encoding='utf-8') as f:
    zeera = json.load(f)

zeera['rpg_stats']['level'] = 29
base_stats = {
    'stat_1': zeera['rpg_stats']['base_stats'].get('stat_1', 8),
    'stat_2': zeera['rpg_stats']['base_stats'].get('stat_2', 7),
    'stat_3': zeera['rpg_stats']['base_stats'].get('stat_3', 5),
    'stat_4': zeera['rpg_stats']['base_stats'].get('stat_4', 4),
    'stat_5': zeera['rpg_stats']['base_stats'].get('stat_5', 5),
    'stat_6': zeera['rpg_stats']['base_stats'].get('stat_6', 2)
}
zeera['rpg_stats']['base_stats'] = base_stats

old_text = "Detesta la mancanza di sottomissione, la simpatia non richiesta e la noia."
new_text = "Maschera il suo innato sadismo dietro un rigido gergo corporativo: chiama le punizioni corporali 'reallineamento HR', la schiavitu 'placement obbligatorio' e le torture psicologiche 'team building non opzionale'. Tratta i suoi dipendenti e consulenti come letterale proprieta privata sacrificabile. Detesta la mancanza di sottomissione, la simpatia non richiesta e la noia."

long_summary = zeera['long_summary'].replace(old_text, new_text)

url = f'{API_BASE}/worlds/characters/{zeera["id"]}'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
payload = {
    'rpg_stats': zeera['rpg_stats'],
    'long_summary': long_summary
}
resp = requests.put(url, headers=headers, json=payload)
print('Zeera Updated:', resp.status_code)
