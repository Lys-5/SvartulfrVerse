import re

path = r"E:\repository\SvartulfrVerse\scratch\001216.log"
with open(path, "rb") as f:
    data = f.read()

idx = 0
while True:
    pos = data.find(b"RPG Source", idx)
    if pos == -1:
        break
    print(f"\n=== Found 'RPG Source' at offset {pos} ===")
    start = max(0, pos - 200)
    end = min(len(data), pos + 1500)
    snippet = data[start:end]
    
    # find URLs in snippet
    urls = re.findall(rb"https?://[^\x00-\x20\x7f-\xff\"\'<>]+", snippet)
    print("URLs in vicinity:")
    for u in urls:
        print("  *", u.decode("latin1"))

    # find printable strings
    strings = re.findall(rb"[\x20-\x7e]{4,}", snippet)
    print("Strings:")
    for s in strings:
        print("  -", s.decode("latin1"))

    idx = pos + 10
