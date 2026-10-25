import re

content = open('scratch/match_chunk_108.js', 'r', encoding='utf-8').read()

# Let's slice the assistant form around 180000 to 195000
start = 180000
end = 205000
chunk = content[start:end]

with open('scratch/assistant_modal_form_extracted.js', 'w', encoding='utf-8') as out:
    out.write(chunk)

print("Saved assistant modal form slice. Searching for input names, labels, state...")

# Find labels, placeholders, input names
inputs = re.findall(r'(?:label|placeholder|name|title|value):\s*["\']([^"\']+)["\']', chunk)
print("Labels/Placeholders found:", list(set(inputs))[:40])

# Find form keys in default state
default_state_matches = re.findall(r'(\w+):\s*(?:["\'][^"\']*["\']|\[\]|\{\}|null|false|true|0)', chunk[:3000])
print("Potential state keys:", list(set(default_state_matches))[:40])
