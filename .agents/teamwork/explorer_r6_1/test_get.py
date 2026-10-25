import json
import urllib.request
import urllib.error
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'

def check():
    token = WT_PATH.read_text(encoding='utf-8').strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json'
    }
    scenarios = [
        ('char_scenario_CKgwq246DyCj1NNTBV9rt', 'Alyssa Route'),
        ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'Jasper Route')
    ]
    results = {}
    for sc_id, name in scenarios:
        url = f'https://app.wyvern.chat/api/character-scenarios/{sc_id}'
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                print(f"SUCCESS: {name} ({sc_id}) -> Status: {resp.status}, Revision: {data.get('revision')}, Name: {data.get('name')}")
                print(f"  Slots count: {len(data.get('slots', []))}")
                print(f"  Greetings count: {len(data.get('greetings', []))}")
                print(f"  Lorebook IDs count: {len(data.get('lorebook_ids', []))}")
                results[sc_id] = data
        except urllib.error.HTTPError as e:
            print(f"ERROR: {name} ({sc_id}) -> HTTP {e.code}: {e.reason}")
            results[sc_id] = {'error': e.code, 'reason': e.reason}
        except Exception as e:
            print(f"EXCEPTION: {name} ({sc_id}) -> {e}")
            results[sc_id] = {'error': str(e)}

    out_file = pathlib.Path(__file__).parent / 'live_scenarios_dump.json'
    out_file.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding='utf-8')
    print("Dump written to", out_file)

if __name__ == '__main__':
    check()
