import json
import requests
from pathlib import Path

ROOT = Path(r"e:\repository\SvartulfrVerse")
WT_PATH = ROOT / "scratch" / "wyvern_token.txt"
token = WT_PATH.read_text(encoding="utf-8").strip()
headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "AdversarialReviewer/1.0"
}

r = requests.get("https://app.wyvern.chat/api/characters/_QPea6g4Q1QfeYCVHCLMPR", headers=headers)
with open(ROOT / "FINAL" / "Erik_Douglas_card.json", "r", encoding="utf-8") as f:
    local_data = json.load(f)
remote_data = r.json()

loc_outfits = local_data.get("outfits", [])
rem_outfits = remote_data.get("outfits", [])
print(f"Local outfits count: {len(loc_outfits)}")
print(f"Remote outfits count: {len(rem_outfits)}")
for i in range(min(len(loc_outfits), len(rem_outfits))):
    lo = loc_outfits[i]
    ro = rem_outfits[i]
    if lo != ro:
        print(f"Outfit {i} ({lo.get('name')}) differs:")
        for k in set(list(lo.keys()) + list(ro.keys())):
            if lo.get(k) != ro.get(k):
                print(f"  key {k}: local={lo.get(k)!r} vs remote={ro.get(k)!r}")
