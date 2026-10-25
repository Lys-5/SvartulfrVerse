with open("scratch/66353-44918b7fd11ff8ae.js", "r", encoding="utf-8") as f:
    c66 = f.read()

idx = c66.find("e7(e.imageURL)")
if idx != -1:
    s = max(0, idx - 1000)
    e = idx + 200
    with open("scratch/e7_definition.txt", "w", encoding="utf-8") as out:
        out.write(c66[s:e])
    print("Found e7 usage! Written to scratch/e7_definition.txt")
