import json

CANONICAL_BROAD_KEYS = {
    "solarton", "succ", "blackwood", "losangeles", "underworld",
    "vampire", "werewolf", "human", "demihuman", "demi-human",
    "demon", "college", "student", "alpha", "beta", "omega", "pack"
}

with open("FINAL/Svartulfr_NPC_Primary.json", "r", encoding="utf-8") as f:
    d = json.load(f)

violations = []
for idx, e in enumerate(d["lexicon"]):
    name = e.get("name")
    for k in e.get("keys", []):
        if k.strip().lower() in CANONICAL_BROAD_KEYS:
            violations.append((idx, name, "keys", k))
    for sk in e.get("secondary_keys", []):
        if sk.strip().lower() in CANONICAL_BROAD_KEYS:
            violations.append((idx, name, "secondary_keys", sk))
    info = e.get("npc_info", {})
    for nk in info.get("nicknames", []):
        if nk.strip().lower() in CANONICAL_BROAD_KEYS:
            violations.append((idx, name, "nicknames", nk))

if violations:
    print(f"FOUND {len(violations)} UMBRELLA KEYWORD VIOLATIONS:")
    for v in violations:
        print(v)
else:
    print("Zero umbrella keywords found across all 99 entries in Primary Lorebook!")
