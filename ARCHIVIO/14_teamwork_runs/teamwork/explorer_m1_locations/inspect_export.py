import json

with open("exports/Svartulfr_Export.json", "r", encoding="utf-8") as f:
    exp = json.load(f)

w_locs = exp.get("world_locations", [])
w_envs = exp.get("world_environments", [])
print("exports world_locations count:", len(w_locs))
print("exports world_environments count:", len(w_envs))

print("\n--- ENVIRONMENTS IN EXPORT ---")
for env in w_envs:
    eid = env.get("id") or env.get("_id")
    name = env.get("name")
    parent = env.get("parent_environment")
    print(f"ID: {eid} | Name: '{name}' | Parent: {parent}")

print("\n--- SAMPLE LOCATION IN EXPORT ---")
if w_locs:
    l0 = w_locs[0]
    print("Name:", l0.get("name"))
    print("Parent location:", l0.get("parent_location"))
    print("Environment:", l0.get("environment"))
    print("Keys on loc:", list(l0.keys()))
