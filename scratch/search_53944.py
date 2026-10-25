with open("scratch/66353-44918b7fd11ff8ae.js", "r", encoding="utf-8") as f:
    c66 = f.read()

# Let's search for "53944" or any import that uses it
idx = c66.find("53944")
print("53944 in c66:", idx)

# Let's check where the generator is called across all chunks
import os
for fname in os.listdir("scratch"):
    if fname.endswith(".js"):
        with open(os.path.join("scratch", fname), "r", encoding="utf-8") as f:
            content = f.read()
            if "53944" in content:
                print(f"53944 referenced in {fname}")
            if "auto-generate from NPC info" in content:
                print(f"'auto-generate from NPC info' in {fname}")
