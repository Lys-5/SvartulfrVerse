import json
import os

print("--- RAW ENVIRONMENTS ---")
if os.path.exists("ARCHIVIO/05_Snapshots_and_Extractions/raw_db_dumps/raw_environments.json"):
    with open("ARCHIVIO/05_Snapshots_and_Extractions/raw_db_dumps/raw_environments.json", "r", encoding="utf-8") as f:
        envs = json.load(f)
    print("Count:", len(envs))
    for e in envs:
        eid = e.get("id") or e.get("_id")
        name = e.get("name")
        parent = e.get("parent_environment")
        print(f"ID: {eid} | Name: {name} | Parent: {parent}")

print("\n--- ENVIRONMENTS MD ---")
if os.path.exists("ARCHIVIO/04_Wyvern_Local_Legacy/environments.md"):
    with open("ARCHIVIO/04_Wyvern_Local_Legacy/environments.md", "r", encoding="utf-8") as f:
        print(f.read()[:1500])
