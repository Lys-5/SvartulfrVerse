import json
import urllib.request
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'User-Agent': 'AuditorBot/1.0'}

def api_get(endpoint):
    url = f"https://app.wyvern.chat/api{endpoint}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return 0, str(e)

print("--- 1. Probing /characters/mine ---")
status, mine_chars = api_get('/characters/mine')
print(f"Status: {status}")
if status == 200:
    chars = mine_chars.get('characters', [])
    print(f"Active characters count: {len(chars)}")
    for c in chars:
        print(f"  {c.get('name')}: {c.get('id')} | avatar: {c.get('avatar', '')[:60]}")

print("\n--- 2. Probing Assistant simple_assistant_xRfBnV7wq48QppqbPPpTM ---")
status, asst = api_get('/simple-assistant-config/simple_assistant_xRfBnV7wq48QppqbPPpTM')
print(f"Status: {status}")
if status == 200:
    print(f"Title: {asst.get('title')}, kind: {asst.get('kind')}")
    print(f"Sys prompt len: {len(asst.get('system_prompt', ''))}, Final inst len: {len(asst.get('final_instructions', ''))}")

print("\n--- 3. Probing Prompt Assembly pha_kWkWUAfTJTF9q72c2bC98 ---")
status, pha = api_get('/prompt-assembly/pha_kWkWUAfTJTF9q72c2bC98')
print(f"Status: {status}")
if status == 200:
    print(f"Name: {pha.get('name')}, floating_depth_percent: {pha.get('floating_depth_percent')}, floating_role: {pha.get('floating_role')}")
    print(f"Blocks count: {len(pha.get('blocks', []))}")
    for b in pha.get('blocks', []):
        print(f"  Block: {b.get('block_id')} | label: {b.get('label')} | role: {b.get('role')} | order: {b.get('order')}")

print("\n--- 4. Probing Old World _CgYT8fHXpDC4crjmegQF7 ---")
status, wld = api_get('/worlds/_CgYT8fHXpDC4crjmegQF7')
print(f"Status: {status}")
if status == 200:
    print(f"Name: {wld.get('name')}, world_age: {wld.get('world_age')}")
    print(f"world_features: {json.dumps(wld.get('world_features', {}))}")
    print(f"stat_config count: {len(wld.get('stat_config', {}).get('stats', []))}")
    for st in wld.get('stat_config', {}).get('stats', []):
        print(f"  Stat: {st.get('id')} ({st.get('abbreviation')}) -> {st.get('label')}")
