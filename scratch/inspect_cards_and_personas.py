import json
import glob
import re
import urllib.request

with open("scratch/wyvern_token.txt", "r", encoding="utf-8") as f:
    TOKEN = f.read().strip()

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "User-Agent": "AuditorBot/1.0"
}

print("=== LOCAL CARDS IN FINAL/ ===")
for p in sorted(glob.glob("FINAL/*_card.json")):
    d = json.load(open(p, encoding="utf-8"))
    desc = d.get("description", "") or d.get("data", {}).get("description", "")
    pers = d.get("personality", "") or d.get("data", {}).get("personality", "")
    headers = re.findall(r"^([A-Z][A-Z0-9 &'\"/\(\)\-,]+):", desc, flags=re.M)
    has_bracket = desc.lstrip().startswith("[")
    has_bs = "BACKSTORY:" in desc
    has_fp = ("FAMILY & PACK:" in desc) or ("CLAN AND COMPANY:" in desc)
    has_vb = "VOICE & BEHAVIOR:" in desc
    print(f"CARD {p}: len={len(desc)}, bracket={has_bracket}, bs={has_bs}, fp={has_fp}, vb={has_vb}, pers_bracket={pers.lstrip().startswith('[')}")
    print("   headers:", headers)

print("\n=== LIVE CARDS (/characters/mine) ===")
try:
    req = urllib.request.Request("https://api.wyvern.chat/characters/mine", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    chars = res if isinstance(res, list) else res.get("characters", res.get("results", res.get("items", [])))
    print(f"Total live cards: {len(chars)}")
    for c in chars:
        cid = c.get("id") or c.get("_id")
        req_c = urllib.request.Request(f"https://api.wyvern.chat/characters/{cid}", headers=HEADERS)
        with urllib.request.urlopen(req_c, timeout=30) as r_c:
            full_c = json.loads(r_c.read().decode("utf-8"))
        desc = full_c.get("description", "")
        pers = full_c.get("personality", "") or full_c.get("summary", "")
        headers = re.findall(r"^([A-Z][A-Z0-9 &'\"/\(\)\-,]+):", desc, flags=re.M)
        has_bracket = desc.lstrip().startswith("[")
        has_bs = "BACKSTORY:" in desc
        has_fp = ("FAMILY & PACK:" in desc) or ("CLAN AND COMPANY:" in desc)
        has_vb = "VOICE & BEHAVIOR:" in desc
        outfits = full_c.get("outfits") or []
        print(f"LIVE CARD {cid} ({full_c.get('name')}): len={len(desc)}, bracket={has_bracket}, bs={has_bs}, fp={has_fp}, vb={has_vb}, pers_bracket={pers.lstrip().startswith('[')}, outfits={len(outfits)}")
        print("   headers:", headers)
except Exception as e:
    print("Error fetching live cards:", e)

print("\n=== LIVE PERSONAS ===")
for ep in ["https://api.wyvern.chat/personas", "https://api.wyvern.chat/personas/mine", "https://api.wyvern.chat/users/me/personas", "https://api.wyvern.chat/users/me"]:
    try:
        req = urllib.request.Request(ep, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8")
            print(f"Endpoint {ep}: HTTP {resp.status}, len={len(raw)}")
            data = json.loads(raw)
            if isinstance(data, dict):
                print("   keys:", list(data.keys()))
                if "personas" in data:
                    for p in data["personas"]:
                        print("   Persona:", p.get("id"), p.get("name"), "desc_len:", len(p.get("description", "")))
            elif isinstance(data, list):
                print("   list len:", len(data))
                for p in data:
                    print("   Persona:", p.get("id"), p.get("name"), "desc_len:", len(p.get("description", "")))
    except Exception as e:
        print(f"Endpoint {ep}: {e}")
