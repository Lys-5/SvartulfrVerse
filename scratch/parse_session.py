import os
import re

path = r"E:\repository\SvartulfrVerse\scratch\chrome_sessions_copy\Session_13437009461459133"
with open(path, "rb") as f:
    data = f.read()

print("File size:", len(data))

# Find all URLs
urls = []
for m in re.finditer(rb"(https?://[^\x00-\x1f\x7f-\xff\"\'<> ]+)", data):
    u = m.group(1).decode("latin1")
    if not any(u.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".js", ".css", ".svg", ".ico", ".woff", ".woff2"]):
        urls.append(u)

# Deduplicate preserving order
seen = set()
unique_urls = []
for u in urls:
    if u not in seen:
        seen.add(u)
        unique_urls.append(u)

print(f"Found {len(unique_urls)} unique URLs:")
for u in unique_urls:
    print(" -", u)
