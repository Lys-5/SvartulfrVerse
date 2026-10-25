import re

def inspect_file(path, pattern_str, context=1000):
    content = open(path, encoding='utf-8', errors='ignore').read()
    for m in re.finditer(pattern_str, content):
        start = max(0, m.start() - context)
        end = min(len(content), m.end() + context)
        print(f"=== MATCH in {path} at {m.start()} ===")
        print(content[start:end])
        print("="*80)

print("--- Inspecting 19010-2f567930ecf4f745.js ---")
inspect_file('scratch/19010-2f567930ecf4f745.js', r'Visual Novel Mode', 800)

print("\n--- Inspecting 81904-87bfa0aca229c4ac.js ---")
inspect_file('scratch/81904-87bfa0aca229c4ac.js', r'vn_mode', 800)
