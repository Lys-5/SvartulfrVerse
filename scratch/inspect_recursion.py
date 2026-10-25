import json

primary_path = r"e:\repository\SvartulfrVerse\FINAL\Svartulfr_NPC_Primary.json"
with open(primary_path, "r", encoding="utf-8") as f:
    primary_data = json.load(f)

entry0 = primary_data["lexicon"][0]
print("extensions:", entry0.get("extensions"))
print("custom_fields:", entry0.get("custom_fields"))
print("top level exclude_from_recursion:", entry0.get("exclude_from_recursion"))

# Also check secondary entry0
secondary_path = r"e:\repository\SvartulfrVerse\FINAL\Svartulfr_NPC_Secondary.json"
with open(secondary_path, "r", encoding="utf-8") as f:
    secondary_data = json.load(f)

s_entry0 = secondary_data["lexicon"][0]
print("secondary extensions:", s_entry0.get("extensions"))
print("secondary top level exclude_from_recursion:", s_entry0.get("exclude_from_recursion"))

# Let's search if exclude_from_recursion exists anywhere in primary_data or secondary_data
def search_key(d, key, path=""):
    if isinstance(d, dict):
        for k, v in d.items():
            if k == key:
                print(f"Found {key} at {path}.{k}: {v}")
            search_key(v, key, f"{path}.{k}")
    elif isinstance(d, list):
        for i, item in enumerate(d):
            search_key(item, key, f"{path}[{i}]")

print("\nSearching for exclude_from_recursion in primary:")
search_key(primary_data, "exclude_from_recursion")

print("\nSearching for exclude_from_recursion in secondary:")
search_key(secondary_data, "exclude_from_recursion")
