with open("scratch/66353-44918b7fd11ff8ae.js", "r", encoding="utf-8") as f:
    c66 = f.read()

# Let's search for usages of npc_info in c66
matches = []
start = 0
while True:
    idx = c66.find("npc_info", start)
    if idx == -1:
        break
    s = max(0, idx - 150)
    e = min(len(c66), idx + 250)
    matches.append(c66[s:e])
    start = idx + 8

with open("scratch/npc_info_usages_in_c66.txt", "w", encoding="utf-8") as out:
    for i, m in enumerate(matches):
        out.write(f"--- Usage {i+1} ---\n{m}\n\n")

print(f"Found {len(matches)} usages of npc_info in c66. Written to scratch/npc_info_usages_in_c66.txt")
