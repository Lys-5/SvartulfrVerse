import json
import urllib.request
import subprocess

# Refresh token first
subprocess.run(["python", "scratch/refresh_token.py"], check=True)

with open("scratch/wyvern_token.txt", "r", encoding="utf-8") as f:
    TOKEN = f.read().strip()

EMBLEM_URL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "AuditorBot/1.0"
}

def deploy_npc_lorebook(lb_id, local_path, opt_path):
    with open(local_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["photoURL"] = EMBLEM_URL
    data["id"] = lb_id
    data["lexicon"] = data["entries"]
    
    with open(local_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    with open(opt_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    payload = {k: v for k, v in data.items() if k != "entries"}
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"https://api.wyvern.chat/lorebooks/{lb_id}",
        data=body,
        headers=HEADERS,
        method="PUT"
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print(f"PUT {lb_id} ({data.get('name')}): HTTP {resp.status} | lexicon={len(res.get('lexicon', []))} | photoURL={res.get('photoURL')}")

def update_lorebook_cover(lb_id, local_paths):
    req_get = urllib.request.Request(
        f"https://api.wyvern.chat/lorebooks/{lb_id}",
        headers=HEADERS,
        method="GET"
    )
    with urllib.request.urlopen(req_get, timeout=60) as resp:
        live_data = json.loads(resp.read().decode("utf-8"))
    live_data["photoURL"] = EMBLEM_URL
    if "entries" in live_data and "lexicon" in live_data:
        del live_data["entries"]
    body = json.dumps(live_data, ensure_ascii=False).encode("utf-8")
    req_put = urllib.request.Request(
        f"https://api.wyvern.chat/lorebooks/{lb_id}",
        data=body,
        headers=HEADERS,
        method="PUT"
    )
    with urllib.request.urlopen(req_put, timeout=60) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print(f"PUT cover {lb_id} ({res.get('name')}): HTTP {resp.status} | lexicon={len(res.get('lexicon', []))} | photoURL={res.get('photoURL')}")
    for p in local_paths:
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
            d["photoURL"] = EMBLEM_URL
            d["id"] = lb_id
            with open(p, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
        except Exception as ex:
            print(f"Warning updating {p}: {ex}")

deploy_npc_lorebook("_zwEqgEEzh12X6gHVmMKKC", "FINAL/Svartulfr_NPC_Primary.json", "lorebooks/optimized/Svartulfr_NPC_Primary.json")
deploy_npc_lorebook("_Uht3Ckz44JBDrPnUHq7LV", "FINAL/Svartulfr_NPC_Secondary.json", "lorebooks/optimized/Svartulfr_NPC_Secondary.json")

update_lorebook_cover("_gwwCxCfQ6PQaLEjAQVpJL", ["FINAL/Svartulfr_Lorebook_I.json", "lorebooks/optimized/Svartulfr_Lorebook_I.json"])
update_lorebook_cover("_HfG7TeV6MJyj6bxMwxkpt", ["FINAL/Svartulfr_Lorebook_II.json", "lorebooks/optimized/Svartulfr_Lorebook_II.json"])
update_lorebook_cover("_9zWTGqYJNJ4BCDMj8gfcD", ["FINAL/Svartulfr_Lorebook_III.json", "lorebooks/optimized/Svartulfr_Lorebook_III.json"])
update_lorebook_cover("_EjXxkmPVhpCXg8xABpFkK", ["FINAL/Svartulfr_Location.json", "lorebooks/optimized/Svartulfr_Location.json"])
