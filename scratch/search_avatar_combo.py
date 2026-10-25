with open("scratch/66353-44918b7fd11ff8ae.js", "r", encoding="utf-8") as f:
    c66 = f.read()

idx = c66.find("Select different avatar...")
if idx != -1:
    s = max(0, idx - 500)
    e = min(len(c66), idx + 2000)
    with open("scratch/avatar_combobox_logic.txt", "w", encoding="utf-8") as out:
        out.write(c66[s:e])
    print("Found! Written to scratch/avatar_combobox_logic.txt")
else:
    print("Not found")
