import sys
import time
import json
import traceback

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from fix_character_names_and_darkfire import get_char, put_char
from g1_outfits_data import G1_OUTFITS_DATA

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'

def main():
    token = get_auth_token()
    if not token:
        print("ERROR: Could not retrieve auth token.")
        sys.exit(1)

    print(f"Starting bulk update of outfits for {len(G1_OUTFITS_DATA)} characters in World {WORLD_ID}...")

    results = []
    snapshots = {}

    for i, (cid, new_outfits) in enumerate(G1_OUTFITS_DATA.items(), 1):
        print(f"\n[{i}/{len(G1_OUTFITS_DATA)}] Processing character {cid}...")
        try:
            # 1. Fresh GET snapshot
            char = get_char(token, cid)
            char_name = char.get("display_name") or char.get("first_name", "Unknown")
            print(f"  Name: {char_name}")
            existing_outfits = char.get("outfits", [])
            print(f"  Existing outfits on card: {len(existing_outfits)}")
            snapshots[cid] = {
                "name": char_name,
                "previous_outfits": existing_outfits
            }

            # 2. Build updated outfits list preserving any avatar URLs
            existing_map = {o.get("id"): o for o in existing_outfits}
            merged_outfits = []
            for new_o in new_outfits:
                oid = new_o["id"]
                item = {
                    "id": oid,
                    "name": new_o["name"],
                    "avatar": "",
                    "description": new_o["description"]
                }
                if oid in existing_map:
                    if existing_map[oid].get("avatar"):
                        item["avatar"] = existing_map[oid]["avatar"]
                merged_outfits.append(item)

            # 3. PUT partial body
            body = {"outfits": merged_outfits}
            put_res = put_char(token, cid, body)
            print(f"  PUT executed successfully.")

            # Short rate-limit pause
            time.sleep(0.6)

            # 4. GET verification
            verify_char = get_char(token, cid)
            verified_outfits = verify_char.get("outfits", [])
            print(f"  Verification GET: {len(verified_outfits)} outfits persisted.")

            # Validate schema presence
            all_valid = True
            for vo in verified_outfits:
                desc = vo.get("description", "")
                if "Abbigliamento:" not in desc or "Acconciatura:" not in desc:
                    all_valid = False
                    print(f"    WARNING: Missing schema keys in outfit {vo.get('name')}")

            if all_valid and len(verified_outfits) == len(merged_outfits):
                print(f"  -> SUCCESS: All {len(verified_outfits)} outfits verified!")
                results.append({"id": cid, "name": char_name, "status": "SUCCESS", "outfits_count": len(verified_outfits)})
            else:
                print(f"  -> WARNING: Partial verification for {char_name}")
                results.append({"id": cid, "name": char_name, "status": "WARNING", "outfits_count": len(verified_outfits)})

        except Exception as e:
            print(f"  -> ERROR updating character {cid}: {e}")
            traceback.print_exc()
            results.append({"id": cid, "name": "Unknown", "status": "FAILED", "error": str(e)})

    # Save snapshot log
    with open("d:/SvartulfrVerse/scripts/g1_outfits_snapshot_backup.json", "w", encoding="utf-8") as f:
        json.dump(snapshots, f, indent=2, ensure_ascii=False)
    print("\nSaved pre-update snapshots to scripts/g1_outfits_snapshot_backup.json")

    # Print summary table
    print("\n" + "="*60)
    print("BULK UPDATE EXECUTION SUMMARY")
    print("="*60)
    success_count = sum(1 for r in results if r["status"] == "SUCCESS")
    for r in results:
        print(f"{r['status']:<8} | {r['id']} | {r['name']:<30} | {r.get('outfits_count', 0)} outfits")
    print("="*60)
    print(f"Completed: {success_count}/{len(G1_OUTFITS_DATA)} characters successfully updated.")

if __name__ == "__main__":
    main()
