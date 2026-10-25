import os
import re

dir_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sync Data", "LevelDB")
fpath = os.path.join(dir_path, "001220.ldb")
with open(fpath, "rb") as f:
    data = f.read()

pos = data.find(b"RPG Source")
print("Pos in 001220.ldb:", pos)
snippet = data[max(0, pos-200):min(len(data), pos+1500)]
strings = re.findall(rb"[\x20-\x7e]{4,}", snippet)
for s in strings:
    print("  *", s.decode("latin1"))

urls = re.findall(rb"https?://[^\x00-\x20\x7f-\xff\"\'<>]+", data)
print(f"Total URLs in 001220.ldb: {len(urls)}")
for u in set(urls):
    print("  URL in 001220.ldb:", u.decode("latin1"))
