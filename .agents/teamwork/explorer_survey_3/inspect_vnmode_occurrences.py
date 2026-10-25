import re

content = open('scratch/19010-2f567930ecf4f745.js', encoding='utf-8', errors='ignore').read()

# Find definition of JE or module containing vnMode
idx = content.find('vnMode')
while idx != -1:
    print("=== vnMode match ===")
    print(content[max(0, idx-300):min(len(content), idx+400)])
    print("-" * 60)
    idx = content.find('vnMode', idx + 6)
