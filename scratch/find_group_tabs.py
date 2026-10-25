import re

path = r"E:\repository\SvartulfrVerse\scratch\001216.log"
with open(path, "rb") as f:
    data = f.read()

target = b"73c71ee0-b197-4a37-9dfd-11818d5b890e"
idx = 0
matches = []
while True:
    pos = data.find(target, idx)
    if pos == -1:
        break
    matches.append(pos)
    idx = pos + len(target)

print(f"Found {len(matches)} occurrences of UUID {target.decode()}:")
for pos in matches:
    start = max(0, pos - 100)
    end = min(len(data), pos + 1000)
    snippet = data[start:end]
    urls = re.findall(rb"https?://[^\x00-\x20\x7f-\xff\"\'<>]+", snippet)
    print(f"\nOffset {pos}:")
    for u in urls:
        print("   URL:", u.decode("latin1"))
    strings = re.findall(rb"[\x20-\x7e]{4,}", snippet)
    print("   Strings:", strings[:10])
