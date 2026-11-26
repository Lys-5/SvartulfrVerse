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

lid = "_zwEqgEEzh12X6gHVmMKKC"
url = f"https://app.wyvern.chat/api/lorebooks/{lid}"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

print("Top-level keys in live Wyvern lorebook:")
print(list(data.keys()))

print("\nTop-level values:")
for k in ["name", "description", "photoURL", "token_budget", "visibility", "rating", "scan_depth", "recursive_scanning", "enableEntryHighlighting", "gallery", "gallery_count"]:
    print(f"  {k}: {data.get(k)}")

lex = data.get("lexicon", [])
print(f"\nLexicon count: {len(lex)}")
if lex:
    e0 = lex[0]
    print(f"\nEntry 0 ({e0.get('name')}):")
    print("Keys in entry 0:")
    print(list(e0.keys()))
    print("npc_info in entry 0:", e0.get("npc_info"))
    print("avatar_activation_regex in entry 0:", e0.get("avatar_activation_regex"))
    print("scan_persona:", e0.get("scan_persona"))
    print("whole_words_only:", e0.get("whole_words_only"))
    print("highlight_keys:", e0.get("highlight_keys"))
    print("enable_highlighting:", e0.get("enable_highlighting"))
    print("extensions:", e0.get("extensions"))
    print("ignored_characters:", e0.get("ignored_characters"))
    print("ignored_personas:", e0.get("ignored_personas"))

    # Also inspect Erik (C-JisFj8qA1tsFEqZKevk or idx around 76)
    for idx, e in enumerate(lex):
        if "Erik" in e.get("name", ""):
            print(f"\nErik entry [{idx}] ({e.get('name')}):")
            print("npc_info:", e.get("npc_info"))
            print("ignored_characters:", e.get("ignored_characters"))
            print("scan_persona:", e.get("scan_persona"))
            print("whole_words_only:", e.get("whole_words_only"))
            print("highlight_keys:", e.get("highlight_keys"))
            print("enable_highlighting:", e.get("enable_highlighting"))
            print("content length:", len(e.get("content", "")))
            break
