import json
import glob
import os

def verify_all_greetings():
    files = sorted(glob.glob("FINAL/scenarios/*.json"))
    with open("scratch/all_greetings_dump.txt", "w", encoding="utf-8") as out:
        for sf in files:
            fname = os.path.basename(sf)
            out.write(f"\n==================== {fname} ====================\n")
            data = json.load(open(sf, encoding="utf-8"))
            greetings = data.get("greetings", [])
            out.write(f"Total Greetings: {len(greetings)}\n")
            for g_idx, g in enumerate(greetings):
                out.write(f"\n  --- Greeting {g_idx}: {g.get('title', 'Untitled')} ---\n")
                for m_idx, m in enumerate(g.get("messages", [])):
                    content = m.get("content", "")
                    author = m.get("author_name", m.get("author", ""))
                    role = m.get("role", "")
                    out.write(f"    [G{g_idx}:M{m_idx}] (role: {role}, author: '{author}')\n")
                    for line_idx, line in enumerate(content.split("\n")):
                        if line.strip():
                            out.write(f"      L{line_idx}: {line}\n")
                            
if __name__ == "__main__":
    verify_all_greetings()
    print("Done writing scratch/all_greetings_dump.txt")
