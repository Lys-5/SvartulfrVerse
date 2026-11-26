import re

content = open('scratch/81904-87bfa0aca229c4ac.js', encoding='utf-8', errors='ignore').read()

# Let's inspect 1000 characters before 258854
print("=== Before 258854 ===")
print(content[255000:259000])
