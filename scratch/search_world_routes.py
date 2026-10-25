import re

with open("scratch/wyvern_index.html", "r", encoding="utf-8") as f:
    text = f.read()

matches = re.findall(r'\"(/[^\"]*world[^\"]*)\"', text, re.IGNORECASE)
print("Matches in html:")
for m in set(matches):
    print(" ", m)
