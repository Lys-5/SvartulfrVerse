with open("scratch/66353-44918b7fd11ff8ae.js", "r", encoding="utf-8") as f:
    c66 = f.read()

with open("scratch/53944-e2a3f3ea28ad0416.js", "r", encoding="utf-8") as f:
    c53 = f.read()

with open("scratch/npc_analysis_raw.txt", "w", encoding="utf-8") as out:
    out.write("=== C66: NPC Information section ===\n")
    idx = c66.find("NPC Information")
    if idx != -1:
        start = max(0, idx - 800)
        end = min(len(c66), idx + 3500)
        out.write(c66[start:end])
        out.write("\n\n")

    out.write("\n=== C53: Regex generator function ===\n")
    idx2 = c53.find("middle_names")
    if idx2 != -1:
        start2 = max(0, idx2 - 800)
        end2 = min(len(c53), idx2 + 2500)
        out.write(c53[start2:end2])
        out.write("\n\n")

print("Written to scratch/npc_analysis_raw.txt successfully!")
