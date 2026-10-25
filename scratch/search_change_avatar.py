with open("scratch/66353-44918b7fd11ff8ae.js", "r", encoding="utf-8") as f:
    c66 = f.read()

idx = c66.find("CHANGE AVATAR")
if idx != -1:
    s = max(0, idx - 400)
    e = min(len(c66), idx + 1000)
    with open("scratch/change_avatar_code.txt", "w", encoding="utf-8") as out:
        out.write(c66[s:e])
    print("Found CHANGE AVATAR! Written to scratch/change_avatar_code.txt")
else:
    print("CHANGE AVATAR not found directly, searching 'avatar'...")
