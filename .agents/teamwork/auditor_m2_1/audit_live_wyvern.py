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

targets = [
    ("_zwEqgEEzh12X6gHVmMKKC", "Svartúlfr - NPC Primary", 99, 7500),
    ("_Uht3Ckz44JBDrPnUHq7LV", "Svartúlfr - NPC Secondary", 211, 5000),
]

for lid, exp_name, exp_count, exp_budget in targets:
    url = f"https://app.wyvern.chat/api/lorebooks/{lid}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        status = resp.status
        data = json.loads(resp.read().decode("utf-8"))

    print(f"\n=======================================================")
    print(f"Live Lorebook: {lid}")
    print(f"=======================================================")
    print(f"HTTP Status: {status}")
    print(f"Name: {data.get('name')}")
    print(f"token_budget: {data.get('token_budget')}")
    print(f"photoURL: {data.get('photoURL')}")
    print(f"gallery: {data.get('gallery')}, gallery_count: {data.get('gallery_count')}")
    print(f"enableEntryHighlighting: {data.get('enableEntryHighlighting')}")
    
    lex = data.get("lexicon", [])
    print(f"Live Lexicon Count: {len(lex)}")
    assert status == 200, f"Expected status 200, got {status}"
    assert data.get("name") == exp_name, f"Expected {exp_name}, got {data.get('name')}"
    assert len(lex) == exp_count, f"Expected {exp_count} entries, got {len(lex)}"
    assert data.get("token_budget") == exp_budget, f"Expected budget {exp_budget}, got {data.get('token_budget')}"
    assert data.get("enableEntryHighlighting") is True, "Expected enableEntryHighlighting to be True"
    assert data.get("gallery") == [], "Expected root gallery to be empty list"
    assert data.get("gallery_count") == 0, "Expected gallery_count to be 0"

    # Sample entry inspections
    for idx, e in enumerate(lex):
        # Check toggles on every entry
        assert e.get("scan_persona") is True, f"Entry [{idx}] {e.get('name')} missing scan_persona: true"
        assert e.get("whole_words_only") is True, f"Entry [{idx}] {e.get('name')} missing whole_words_only: true"
        assert e.get("highlight_keys") is True, f"Entry [{idx}] {e.get('name')} missing highlight_keys: true"
        assert e.get("enable_highlighting") is True, f"Entry [{idx}] {e.get('name')} missing enable_highlighting: true"
        
        info = e.get("npc_info")
        assert isinstance(info, dict), f"Entry [{idx}] {e.get('name')} missing npc_info dict"
        assert "first_name" in info and info["first_name"], f"Entry [{idx}] missing first_name"
        assert "middle_names" in info and isinstance(info["middle_names"], list), f"Entry [{idx}] invalid middle_names"
        assert "titles" in info and isinstance(info["titles"], list), f"Entry [{idx}] invalid titles"
        assert "nicknames" in info and isinstance(info["nicknames"], list), f"Entry [{idx}] invalid nicknames"
        assert "npc_prefix" in info, f"Entry [{idx}] missing npc_prefix"

    print(f"Verified all {len(lex)} live entries have valid npc_info, scan_persona, whole_words_only, and highlighting!")

print("\n[ALL LIVE WYVERN CHECKS EMPIRICALLY CONFIRMED & PASSED]")
