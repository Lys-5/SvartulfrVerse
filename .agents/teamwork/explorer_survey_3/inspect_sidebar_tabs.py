content = open('scratch/19010-2f567930ecf4f745.js', encoding='utf-8', errors='ignore').read()
start = 215000
end = 230000

# Search for tab titles and button labels in this section
import re
buttons = re.findall(r'title:"([^"]+)"|aria-label:"([^"]+)"|children:"([^"]+)"', content[start:end])
print(f"Buttons/labels found between {start} and {end}:")
for b in buttons[:50]:
    val = [x for x in b if x]
    if val and len(val[0]) < 40:
        print("  ", val[0])
