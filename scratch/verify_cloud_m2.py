import json
import urllib.request
import urllib.error

def verify_cloud():
    print("=== Checking Wyvern Cloud API State ===")
    with open("scratch/wyvern_token.txt", "r", encoding="utf-8") as f:
        token = f.read().strip()

    headers = {"Authorization": f"Bearer {token}", "User-Agent": "AuditorBot/1.0"}

    for lid, expected_count in [("_zwEqgEEzh12X6gHVmMKKC", 99), ("_Uht3Ckz44JBDrPnUHq7LV", 211)]:
        url = f"https://app.wyvern.chat/api/lorebooks/{lid}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            d = json.loads(resp.read().decode("utf-8"))
            name = d.get("name")
            lex = d.get("lexicon", [])
            count = len(lex)
            budget = d.get("token_budget")
            hl = d.get("enableEntryHighlighting")
            print(f"Lorebook {lid}: HTTP {resp.status}, name='{name}', count={count}, budget={budget}, enableEntryHighlighting={hl}")
            assert count == expected_count, f"Expected {expected_count}, got {count}"
            
            # Check toggles on all entries in cloud
            for idx, e in enumerate(lex):
                ename = e.get("name")
                assert e.get("scan_persona") is True, f"Cloud [{idx}] {ename} scan_persona not True"
                assert e.get("whole_words_only") is True, f"Cloud [{idx}] {ename} whole_words_only not True"
                assert e.get("highlight_keys") is True, f"Cloud [{idx}] {ename} highlight_keys not True"
                assert "npc_info" in e, f"Cloud [{idx}] {ename} missing npc_info"
                info = e["npc_info"]
                assert "middle_names" in info and isinstance(info["middle_names"], list), f"Cloud [{idx}] {ename} missing or invalid middle_names in npc_info"
            print(f"  All {count} entries in cloud have scan_persona, whole_words_only, highlight_keys, and valid npc_info!")
    print("Cloud verification passed successfully!")

if __name__ == "__main__":
    verify_cloud()
