import re

chunk93 = open('scratch/match_chunk_93.js', 'r', encoding='utf-8').read()

start = 70000
end = 90000
slice_93 = chunk93[start:end]

with open('scratch/prompt_assembly_ui_slice.js', 'w', encoding='utf-8') as out:
    out.write(slice_93)

print("Saved prompt assembly UI slice. Searching for inputs, tabs, buttons, placeholders...")

placeholders = re.findall(r'placeholder:\s*["\']([^"\']+)["\']', slice_93)
print("Placeholders found:", set(placeholders))

titles = re.findall(r'(?:DialogTitle|title|label|tab):\s*["\']([^"\']+)["\']', slice_93)
print("Titles / Labels found:", list(set(titles))[:30])

buttons = re.findall(r'children:\s*["\']([^"\']{2,40})["\']', slice_93)
print("Button/Text snippets:", list(set(buttons))[:40])
