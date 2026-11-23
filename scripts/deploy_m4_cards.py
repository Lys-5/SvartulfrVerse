#!/usr/bin/env python3
"""
Deploy updated cards for Milestone 4 to live Wyvern platform.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

import scripts.wyvern_api_client as c

FINAL = Path(__file__).resolve().parent.parent / "FINAL"

CARDS_TO_DEPLOY = [
    ("FINAL/Adam_Valencia_card.json", "_DEDnMNcgX8xDEpGmYqdrM"),
    ("FINAL/Dullahan_card.json", "_GADYjkenq7CW4RhU2wqbh"),
    ("FINAL/Fenrir_card.json", "_1zWxyEmwxKq1DhMxj3pXw"),
    ("FINAL/Hana_Valencia_card.json", "_DBd8Rx9pzaPtxeG8232V6"),
    ("FINAL/Jasper_Contractor_card.json", "_waQyWtVYDbJkhrH9ADYbn"),
    ("FINAL/Johan_Jakobsen_card.json", "_cPHFyL1FbeQWzX1QMptpW"),
    ("FINAL/Luka_Sutter_card.json", "_axCwFrFLmaUn6XE7hbQt2"),
    ("FINAL/Richard_Whitlock_card.json", "_2xh1VhxVjHx1Rje3fg7Bg"),
    ("FINAL/Mackenzie_Fantasy_card.json", "_nUkjqtKz9RrP7CJCxXnCL"),
    ("FINAL/Mackenzie_Sanchez_Rogers_card.json", "_zn24784jfcchQ7EwCyAnm"),
]

def main():
    tok = c.get_auth_token()
    print("Authentication token acquired.")
    
    results = {}
    for rel_path, expected_id in CARDS_TO_DEPLOY:
        file_path = FINAL.parent / rel_path
        with open(file_path, "r", encoding="utf-8") as f:
            card = json.load(f)
        
        cid = card.get("id") or expected_id
        print(f"Deploying {card.get('name')} ({cid})...")
        st, res = c.update_character(cid, card, token=tok)
        if st == 200:
            print(f"  -> SUCCESS (HTTP {st})")
            results[cid] = "SUCCESS"
        else:
            print(f"  -> FAILED (HTTP {st}): {res}")
            results[cid] = f"FAILED ({st})"

    print("\n=== Deployment Summary ===")
    all_ok = all(v == "SUCCESS" for v in results.values())
    for cid, status in results.items():
        print(f"  - {cid}: {status}")
    
    if all_ok:
        print("\nAll cards successfully synchronized to Wyvern!")
    else:
        print("\nSome deployments failed.")

if __name__ == "__main__":
    main()
