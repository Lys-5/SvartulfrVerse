import os

user_data = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "Default")
target = b"RPG Source"

for root, dirs, files in os.walk(user_data):
    for f in files:
        p = os.path.join(root, f)
        try:
            # skip huge files > 200MB
            if os.path.getsize(p) > 200 * 1024 * 1024:
                continue
            with open(p, "rb") as fp:
                content = fp.read()
                if target in content:
                    print("Found target in:", p)
        except Exception:
            pass
print("Search complete.")
