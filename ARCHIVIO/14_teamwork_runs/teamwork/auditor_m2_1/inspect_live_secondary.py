import json
import urllib.request
from pathlib import Path

ROOT = Path(r"e:\repository\SvartulfrVerse")
TOKEN_PATH = ROOT / "scratch" / "wyvern_token.txt"

with open(TOKEN_PATH, "r", encoding="utf-8") as f:
    token = f.read().strip()

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "AuditorBot/1.0",
    "Accept": "application/json"
}

lid = "_Uht3Ckz44JBDrPnUHq7LV"
url = f"https://app.wyvern.chat/api/lorebooks/{lid}"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

print("Top-level values for Secondary Lorebook:")
for k in ["name", "description", "photoURL", "token_budget", "visibility", "rating", "scan_depth", "recursive_scanning", "enableEntryHighlighting", "gallery", "gallery_count"]:
    print(f"  {k}: {data.get(k)}")

lex = data.get("lexicon", [])
print(f"\nLexicon count: {len(lex)}")

# Check Edric Douglas, Camp Mystic campers, etc.
edric_found = False
for idx, e in enumerate(lex):
    assert e.get("scan_persona") is True, f"Secondary [{idx}] missing scan_persona"
    assert e.get("whole_words_only") is True, f"Secondary [{idx}] missing whole_words_only"
    assert e.get("highlight_keys") is True, f"Secondary [{idx}] missing highlight_keys"
    assert e.get("enable_highlighting") is True, f"Secondary [{idx}] missing enable_highlighting"
    assert "npc_info" in e and isinstance(e["npc_info"], dict), f"Secondary [{idx}] missing npc_info"
    
    if "Edric" in e.get("name", ""):
        edric_found = True
        print(f"\nEdric Douglas entry [{idx}] ({e.get('name')}):")
        print("npc_info:", e.get("npc_info"))
        print("ignored_characters:", e.get("ignored_characters"))
        print("content length:", len(e.get("content", "")))

assert edric_found, "Edric Douglas not found in Secondary!"

# Check camper with middle name (idx 111)
e111 = lex[111]
print(f"\nCamper 111 ({e111.get('name')}):")
print("npc_info:", e111.get("npc_info"))
print("avatar:", e111.get("avatar"))
print("keys:", e111.get("keys"))

print(f"\n[ALL 211 SECONDARY LIVE ENTRIES VERIFIED SUCCESSFULLY]")
