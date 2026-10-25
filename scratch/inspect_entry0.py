import json

primary_path = r"e:\repository\SvartulfrVerse\FINAL\Svartulfr_NPC_Primary.json"
with open(primary_path, "r", encoding="utf-8") as f:
    primary_data = json.load(f)

entry0 = primary_data["lexicon"][0]
print("Keys in entry0:", list(entry0.keys()))
for k, v in entry0.items():
    if isinstance(v, str):
        print(f"{k}: {repr(v[:100])} (len={len(v)})")
    else:
        print(f"{k}: {type(v)}")
