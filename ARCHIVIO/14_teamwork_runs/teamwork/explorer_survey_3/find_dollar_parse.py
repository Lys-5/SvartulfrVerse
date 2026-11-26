import re

content = open('scratch/14685-a6f37bf36e7cf713.js', encoding='utf-8', errors='ignore').read()
idx = content.find('$=V.z.object({version:V.z.literal(1)')

# Look for $.parse or $.safeParse or $ in that module
var_name = '$'
matches = list(re.finditer(r'\$\.(safeParse|parse)', content))
print(f"$.parse / safeParse matches: {len(matches)}")
for m in matches:
    p = m.start()
    print("=== Usage ===")
    print(content[max(0, p-100):min(len(content), p+200)])
