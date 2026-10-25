import requests, json, difflib

token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
headers = {'Authorization': f'Bearer {token}'}

for sc_id, local_file, name in [
    ('char_scenario_CKgwq246DyCj1NNTBV9rt', 'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json', 'SUCC Alyssa'),
    ('char_scenario_Kq4mJEBH83j7Q7DdVfFnF', 'FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Jasper.json', 'SUCC Jasper')
]:
    r = requests.get(f'https://app.wyvern.chat/api/character-scenarios/{sc_id}', headers=headers)
    if r.status_code == 200:
        remote_data = r.json()
        local_data = json.load(open(local_file, encoding='utf-8'))
        
        print(f"================ {name} ================")
        print(f"Remote rev: {remote_data.get('revision')} | Local rev: {local_data.get('revision')}")
        
        # compare keys
        all_keys = set(remote_data.keys()).union(set(local_data.keys()))
        for k in sorted(all_keys):
            rv = remote_data.get(k)
            lv = local_data.get(k)
            if rv != lv:
                if isinstance(rv, (dict, list)) and isinstance(lv, (dict, list)):
                    rs = json.dumps(rv, indent=2, sort_keys=True)
                    ls = json.dumps(lv, indent=2, sort_keys=True)
                    if rs != ls:
                        print(f"Field '{k}' differs: remote len={len(rs)} vs local len={len(ls)}")
                        diff = list(difflib.unified_diff(ls.splitlines(), rs.splitlines(), fromfile='local', tofile='remote', lineterm='', n=2))
                        print("  Diff preview (first 25 lines):")
                        for l in diff[:25]:
                            print("   ", l)
                else:
                    print(f"Field '{k}' differs:\n  Local:  {repr(lv)[:120]}\n  Remote: {repr(rv)[:120]}")
