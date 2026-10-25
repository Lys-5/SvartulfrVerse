import re

path = r"E:\repository\SvartulfrVerse\scratch\001216.log"
with open(path, "rb") as f:
    data = f.read()

print("File length:", len(data))
if b"RPG Source" in data:
    print("FOUND 'RPG Source' in 001216.log!")

urls = re.findall(rb"https?://[^\x00-\x20\x7f-\xff\"\'<>]+", data)
unique_urls = []
seen = set()
for u in urls:
    s = u.decode("latin1", errors="ignore")
    if s not in seen and not any(s.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".js", ".css", ".svg", ".ico"]):
        seen.add(s)
        unique_urls.append(s)

print(f"Total unique URLs in log: {len(unique_urls)}")
for u in unique_urls:
    print(" -", u)
