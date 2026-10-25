import urllib.request
import urllib.error
import json
import glob
import time
import sys

token = open('scratch/wyvern_token.txt', 'r', encoding='utf-8').read().strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

files = glob.glob('FINAL/scenarios/*.json')
print(f"Deploying {len(files)} scenarios to Wyvern Web API...", flush=True)

results = {}

for fpath in files:
    print("\n" + "="*60, flush=True)
    print(f"DEPLOYING: {fpath}", flush=True)
    with open(fpath, 'r', encoding='utf-8') as f:
        payload = json.load(f)
    
    # Ensure visibility is private
    payload['visibility'] = 'private'
    
    # Remove id if present so POST generates a brand new scenario
    if 'id' in payload:
        del payload['id']

    req_data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    url = 'https://app.wyvern.chat/api/character-scenarios'
    
    req = urllib.request.Request(url, data=req_data, headers=headers, method='POST')
    try:
        print("  Sending POST request...", flush=True)
        with urllib.request.urlopen(req, timeout=25) as resp:
            status = resp.status
            resp_body = resp.read().decode('utf-8')
            res_json = json.loads(resp_body)
            new_id = res_json.get('id')
            title = res_json.get('title') or res_json.get('name')
            print(f"  [SUCCESS] HTTP {status}! Created scenario: {new_id} ('{title}')", flush=True)
            results[fpath] = {
                'id': new_id,
                'title': title,
                'status': status
            }
            
            # Update local file with the generated id
            payload['id'] = new_id
            with open(fpath, 'w', encoding='utf-8') as f_out:
                json.dump(payload, f_out, indent=2, ensure_ascii=False)
                
            # Perform GET verification
            time.sleep(1.0)
            verify_url = f'https://app.wyvern.chat/api/character-scenarios/{new_id}'
            verify_req = urllib.request.Request(verify_url, headers=headers, method='GET')
            with urllib.request.urlopen(verify_req, timeout=25) as v_resp:
                v_body = v_resp.read().decode('utf-8')
                v_json = json.loads(v_body)
                print(f"  [VERIFY] GET {new_id} -> HTTP {v_resp.status}, Slots: {len(v_json.get('slots', []))}, Greetings: {len(v_json.get('greetings', []))}, Visibility: {v_json.get('visibility')}", flush=True)
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='ignore')
        print(f"  [ERROR] HTTP {e.code}: {e.reason} -> {err_msg}", flush=True)
        results[fpath] = {'error': f"HTTP {e.code}: {err_msg}"}
    except Exception as e:
        print(f"  [ERROR] Exception: {e}", flush=True)
        results[fpath] = {'error': str(e)}
        
    time.sleep(1.5)

with open('scratch/deployed_scenarios_ids.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\n" + "="*60, flush=True)
print("Deployment completed. Results saved to scratch/deployed_scenarios_ids.json", flush=True)
