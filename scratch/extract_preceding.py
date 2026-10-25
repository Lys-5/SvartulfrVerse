with open("scratch/66353-44918b7fd11ff8ae.js", "r", encoding="utf-8") as f:
    c66 = f.read()

idx = c66.find("NPC Information")
start = max(0, idx - 2500)
end = idx + 200

with open("scratch/c66_preceding.txt", "w", encoding="utf-8") as out:
    out.write(c66[start:end])

print("Written scratch/c66_preceding.txt successfully!")
