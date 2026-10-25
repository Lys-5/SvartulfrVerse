import os
import re

dir_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default", "Sync Data", "LevelDB")
for fname in os.listdir(dir_path):
    fpath = os.path.join(dir_path, fname)
    if not os.path.isfile(fpath):
        continue
    try:
        with open(fpath, "rb") as f:
            data = f.read()
    except Exception:
        continue
    
    matches = [m.start() for m in re.finditer(rb"saved_tab_group", data)]
    if matches:
        print(f"File {fname}: {len(matches)} occurrences of saved_tab_group")
        for pos in matches:
            snippet = data[pos:pos+400]
            urls = re.findall(rb"https?://[^\x00-\x20\x7f-\xff\"\'<>]+", snippet)
            strings = re.findall(rb"[\x20-\x7e]{4,}", snippet)
            if urls or any(b"http" in s for s in strings):
                print(f"  Pos {pos}:")
                for u in urls:
                    print("    URL:", u.decode("latin1"))
                for s in strings[:6]:
                    print("    Str:", s.decode("latin1"))
