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

print("=== LOCAL PERSONAS IN FINAL/personas/ ===")
for p in sorted(glob.glob("FINAL/personas/*.json")):
    d = json.load(open(p, encoding="utf-8"))
    desc = d.get("description", "")
    headers = re.findall(r"^([A-Z][A-Z0-9 &'\"/\(\)\-,]+):", desc, flags=re.M)
    has_bracket = desc.lstrip().startswith("[")
    has_bs = "BACKSTORY:" in desc
    has_fp = ("FAMILY & PACK:" in desc) or ("CLAN AND COMPANY:" in desc)
    has_vb = "VOICE & BEHAVIOR:" in desc
    outfits = d.get("appearances") or d.get("outfits") or []
    print(f"LOCAL PERSONA {p} ({d.get('name')}): id={d.get('persona_id') or d.get('id')}, len={len(desc)}, bracket={has_bracket}, bs={has_bs}, fp={has_fp}, vb={has_vb}, appearances={len(outfits)}")
    print("   headers:", headers)

print("\n=== LIVE USER PERSONAS (/user-personas) ===")
try:
    req = urllib.request.Request("https://app.wyvern.chat/api/user-personas", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    p_list = res if isinstance(res, list) else res.get("personas", res.get("results", res.get("items", [])))
    print(f"Total live user-personas: {len(p_list)}")
    for p in p_list:
        pid = p.get("persona_id") or p.get("id") or p.get("_id")
        desc = p.get("description", "")
        headers = re.findall(r"^([A-Z][A-Z0-9 &'\"/\(\)\-,]+):", desc, flags=re.M)
        has_bracket = desc.lstrip().startswith("[")
        has_bs = "BACKSTORY:" in desc
        has_fp = ("FAMILY & PACK:" in desc) or ("CLAN AND COMPANY:" in desc)
        has_vb = "VOICE & BEHAVIOR:" in desc
        outfits = p.get("appearances") or p.get("outfits") or []
        print(f"LIVE PERSONA {pid} ({p.get('name')}): len={len(desc)}, bracket={has_bracket}, bs={has_bs}, fp={has_fp}, vb={has_vb}, appearances={len(outfits)}")
        print("   headers:", headers)
except Exception as e:
    print("Error fetching live personas:", e)
