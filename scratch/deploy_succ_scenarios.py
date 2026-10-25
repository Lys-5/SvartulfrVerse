import json
import time
import requests
import pathlib
import subprocess

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

ALYSSA_ID = "char_scenario_CKgwq246DyCj1NNTBV9rt"
JASPER_ID = "char_scenario_Kq4mJEBH83j7Q7DdVfFnF"

SCENARIOS = [
    {
        "name": "Alyssa Route",
        "id": ALYSSA_ID,
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Alyssa.json"
    },
    {
        "name": "Jasper Route",
        "id": JASPER_ID,
        "local_path": ROOT / "FINAL" / "scenarios" / "Svartulfr_Scenario_SUCC_Route_Jasper.json"
    }
]

def ensure_token():
    token_file = ROOT / 'scratch' / 'wyvern_token.txt'
    token = token_file.read_text(encoding='utf-8').strip() if token_file.exists() else ""
    
    # Test token
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
    r = requests.get('https://app.wyvern.chat/api/character-scenarios/' + ALYSSA_ID, headers=headers)
    if r.status_code == 200:
        print("[AUTH] Current token is valid.")
        return token
    
    print(f"[AUTH] Token invalid or expired (HTTP {r.status_code}). Refreshing...")
    refresh_script = ROOT / 'scratch' / 'refresh_token.py'
    res = subprocess.run(["python", str(refresh_script)], capture_output=True, text=True)
    print("[AUTH] Refresh output:", res.stdout, res.stderr)
    new_token = token_file.read_text(encoding='utf-8').strip()
    return new_token

def deploy():
    token = ensure_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    for sc in SCENARIOS:
        sc_id = sc["id"]
        name = sc["name"]
        local_path = sc["local_path"]

        print(f"\n==========================================")
        print(f"Deploying {name} ({sc_id})...")
        print(f"==========================================")

        # 1. Fetch live scenario
        get_url = f"https://app.wyvern.chat/api/character-scenarios/{sc_id}"
        resp_get = requests.get(get_url, headers=headers)
        if resp_get.status_code != 200:
            raise RuntimeError(f"GET failed for {name}: HTTP {resp_get.status_code} - {resp_get.text}")
        
        live_data = resp_get.json()
        live_rev = live_data.get("revision", 1)
        print(f"  [GET] Current remote revision: {live_rev}")

        # 2. Read local JSON
        with open(local_path, "r", encoding="utf-8") as f:
            local_data = json.load(f)

        # 3. Prepare payload
        payload = {
            "name": local_data.get("name"),
            "display_description": local_data.get("display_description", ""),
            "avatar": local_data.get("avatar", ""),
            "tags": local_data.get("tags", []),
            "visibility": "private",
            "rating": local_data.get("rating", "explicit"),
            "revision": live_rev,
            "linked_world_id": local_data.get("linked_world_id", ""),
            "scenario": local_data.get("scenario", ""),
            "startup_script": local_data.get("startup_script", ""),
            "slots": local_data.get("slots", []),
            "greetings": local_data.get("greetings", []),
            "lorebook_ids": local_data.get("lorebook_ids", []),
            "gallery": local_data.get("gallery", [])
        }

        # 4. PUT request
        put_url = f"https://app.wyvern.chat/api/character-scenarios/{sc_id}"
        resp_put = requests.put(put_url, headers=headers, json=payload)
        if resp_put.status_code != 200:
            raise RuntimeError(f"PUT failed for {name}: HTTP {resp_put.status_code} - {resp_put.text}")
        
        put_result = resp_put.json()
        new_rev = put_result.get("revision", live_rev + 1)
        print(f"  [PUT SUCCESS] HTTP 200! New revision: {new_rev}")

        # 5. Update local file revision
        local_data["revision"] = new_rev
        with open(local_path, "w", encoding="utf-8") as f:
            json.dump(local_data, f, indent=2, ensure_ascii=False)
        print(f"  [SAVED] Updated local revision to {new_rev}")

        time.sleep(2.5)

        # 6. Verify remote state
        resp_verify = requests.get(get_url, headers=headers)
        if resp_verify.status_code != 200:
            raise RuntimeError(f"Verification GET failed for {name}: HTTP {resp_verify.status_code}")
        
        verify_data = resp_verify.json()
        vg = verify_data.get("greetings", [])
        print(f"  [REMOTE CONFIRMED] Greetings count: {len(vg)}, Greeting 0 name: '{vg[0].get('name') if vg else None}'")
        assert len(vg) == len(local_data["greetings"]), f"Greeting count mismatch: {len(vg)} vs {len(local_data['greetings'])}"
        assert vg[0].get("name") == "SUCC Welcome Day", f"Greeting 0 title mismatch: {vg[0].get('name')}"
        assert vg[0].get("speaker_slot") == local_data["greetings"][0]["speaker_slot"]
        assert vg[0].get("content") == local_data["greetings"][0]["content"]

    print("\n[DEPLOYMENT COMPLETE] Both scenarios successfully deployed and verified!")

if __name__ == "__main__":
    deploy()
