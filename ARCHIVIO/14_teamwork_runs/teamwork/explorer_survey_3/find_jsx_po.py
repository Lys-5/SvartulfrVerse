import re

content = open('scratch/19010-2f567930ecf4f745.js', encoding='utf-8', errors='ignore').read()

matches = list(re.finditer(r'\(0,[a-zA-Z0-9_\$]+\.jsx\)\([a-zA-Z0-9_\$]+\.pO', content))
print(f"jsx(..pO) matches: {len(matches)}")
for m in matches:
    idx = m.start()
    print("=== JSX CALL TO pO ===")
    print(content[max(0, idx-200):min(len(content), idx+400)])
    print("=" * 60)

# Also check for jsxs or direct calls
matches2 = list(re.finditer(r'\bjsx\w*\)\([a-zA-Z0-9_\$]+\.pO', content))
print(f"jsx*(..pO) matches: {len(matches2)}")
for m in matches2:
    idx = m.start()
    print("=== JSX* CALL TO pO ===")
    print(content[max(0, idx-200):min(len(content), idx+400)])
    print("=" * 60)
