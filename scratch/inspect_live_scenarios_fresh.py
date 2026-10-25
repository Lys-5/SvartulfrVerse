import urllib.request
import json

token = open('scratch/wyvern_token.txt').read().strip()
headers = {'Authorization': 'Bearer ' + token, 'User-Agent': 'AuditorBot/1.0', 'Accept': 'application/json'}

for sid in ['char_scenario_CKgwq246DyCj1NNTBV9rt', 'char_scenario_Kq4mJEBH83j7Q7DdVfFnF']:
    req = urllib.request.Request(f'https://app.wyvern.chat/api/character-scenarios/{sid}', headers=headers)
    with urllib.request.urlopen(req) as resp:
        d = json.loads(resp.read().decode())
        print(f"{sid}: status {resp.status}, rev {d.get('revision')}, slots {len(d.get('slots', []))}, greetings {len(d.get('greetings', []))}")
        print("  Slots:", [(s.get('key'), s.get('unavailable_count'), len(s.get('pool', []))) for s in d.get('slots', [])])
