import json

with open(r'd:\SvartulfrVerse\exports\Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = data.get('world_characters', [])
real_chars = [c for c in chars if len(c.get('long_summary') or '') > 100]

print(f"Total characters: {len(chars)}")
print(f"Real authored characters (>100 chars): {len(real_chars)}")

# Let's inspect their names and categories/folders
names = sorted([c.get('display_name') or c.get('name') for c in real_chars])
with open(r'd:\SvartulfrVerse\scratch\real_chars_list.txt', 'w', encoding='utf-8') as out:
    for n in names:
        out.write(f"{n}\n")

print("Saved to scratch/real_chars_list.txt")
