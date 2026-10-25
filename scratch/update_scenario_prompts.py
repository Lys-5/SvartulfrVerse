import json
import urllib.request
import urllib.error
import time
import sys

sys.path.append("scripts")
from remediate_lorebook_npcs import refresh_wyvern_token

SCENARIO_FILE = "FINAL/Svartulfr_Master_Scenario.json"
SCENARIO_ID = "char_scenario_CKgwq246DyCj1NNTBV9rt"

with open(SCENARIO_FILE, "r", encoding="utf-8") as f:
    scen_data = json.load(f)

token = refresh_wyvern_token()
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

url = f"https://app.wyvern.chat/api/character-scenarios/{SCENARIO_ID}"
req_get = urllib.request.Request(url, headers=headers, method="GET")
with urllib.request.urlopen(req_get, timeout=30) as resp:
    live_scen = json.loads(resp.read().decode("utf-8"))
    latest_revision = live_scen.get("revision", 19)

print(f"Latest live revision: {latest_revision}")

# Put payload with all required fields
payload = {
    "revision": latest_revision,
    "name": scen_data["name"],
    "display_description": scen_data.get("display_description", ""),
    "scenario": scen_data.get("scenario", ""),
    "startup_script": scen_data.get("startup_script", ""),
    "slots": scen_data["slots"],
    "greetings": scen_data["greetings"],
    "lorebook_ids": scen_data.get("lorebook_ids", []),
    "system_prompt": scen_data["system_prompt"],
    "final_instructions": scen_data["final_instructions"],
    "visibility": scen_data.get("visibility", "unlisted"),
    "rating": scen_data.get("rating", "explicit")
}

req_put = urllib.request.Request(url, data=json.dumps(payload, ensure_ascii=False).encode("utf-8"), headers=headers, method="PUT")
try:
    with urllib.request.urlopen(req_put, timeout=30) as resp:
        print(f"Scenario PUT SUCCESS: HTTP {resp.status} {resp.reason}")
except urllib.error.HTTPError as e:
    print(f"Scenario PUT failed: HTTP {e.code} {e.reason}")
    print(e.read().decode("utf-8", errors="replace"))
