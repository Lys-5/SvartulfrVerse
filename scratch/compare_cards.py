"""
Compare local FINAL/ card IDs with Wyvern /characters/mine live IDs.
"""

import os
import json
import urllib.request

def main():
    token_path = os.path.join("scratch", "wyvern_token.txt")
    with open(token_path, "r", encoding="utf-8") as f:
        token = f.read().strip()
        
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "ReviewerR6-1/1.0",
        "Accept": "application/json"
    }

    # Live cards
    mine_url = "https://app.wyvern.chat/api/characters/mine"
    mine_req = urllib.request.Request(mine_url, headers=headers)
    with urllib.request.urlopen(mine_req) as resp:
        mine_data = json.loads(resp.read().decode("utf-8"))
    
    live_cards = {c["id"]: c.get("name") for c in mine_data.get("characters", [])}
    print(f"Live /characters/mine count: {len(live_cards)}")
    for cid, cname in sorted(live_cards.items()):
        print(f"  Live: {cid} -> {cname}")

    # Local cards
    final_dir = "FINAL"
    local_card_files = [f for f in os.listdir(final_dir) if f.endswith("_card.json")]
    print(f"\nLocal FINAL/ card files count: {len(local_card_files)}")
    local_cards = {}
    for fname in local_card_files:
        fpath = os.path.join(final_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            cdata = json.load(f)
            cid = cdata.get("id") or cdata.get("character_id") or cdata.get("data", {}).get("id")
            cname = cdata.get("name") or cdata.get("data", {}).get("name")
            local_cards[fname] = (cid, cname)
            print(f"  Local file {fname}: id={cid}, name={cname}")

    print("\n--- Cross-Verification ---")
    local_ids = {v[0] for v in local_cards.values() if v[0]}
    print("Local IDs set:", local_ids)
    print("Live IDs set:", set(live_cards.keys()))
    if local_ids:
        print("Set difference (local - live):", local_ids - set(live_cards.keys()))
        print("Set difference (live - local):", set(live_cards.keys()) - local_ids)
        assert local_ids == set(live_cards.keys()), "Mismatch between local card IDs and live card IDs!"
        print("PERFECT MATCH: Local card IDs and live card IDs are identical!")
    else:
        print("Note: Local card files use character schemas without root 'id' field, let's inspect structure.")

if __name__ == "__main__":
    main()
