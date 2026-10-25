import re

content = open('scratch/assistant_modal_form_extracted.js', 'r', encoding='utf-8').read()

print("Does assistant modal have lorebooks?")
print("lorebook:", 'lorebook' in content.lower())
print("lore_book:", 'lore_book' in content.lower())
print("entries:", 'entries' in content.lower())

# Let's inspect the save mutation and payload construction
idx = content.find("create(")
if idx != -1:
    print("\n--- create() call context ---")
    print(content[max(0, idx-200):min(len(content), idx+400)])

idx = content.find("update(")
if idx != -1:
    print("\n--- update() call context ---")
    print(content[max(0, idx-200):min(len(content), idx+400)])

# Let's inspect the default values function Y() or J()
idx = content.find("let eg=()=>{")
if idx != -1:
    print("\n--- eg / Y / J context ---")
    print(content[max(0, idx-1000):min(len(content), idx+1000)])
