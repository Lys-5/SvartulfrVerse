import os
import re

dir_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sync Data", "LevelDB")
for fname in sorted(os.listdir(dir_path)):
    fpath = os.path.join(dir_path, fname)
    if os.path.isfile(fpath) and fname != "LOCK":
        with open(fpath, "rb") as f:
            data = f.read()
        pos = data.find(b"1ff24d14-3")
        if pos != -1:
            snippet = data[pos:pos+150]
            print(f"Found in {fname} at {pos}:", repr(snippet))
