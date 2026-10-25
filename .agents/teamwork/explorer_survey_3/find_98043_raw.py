content = open('scratch/19010-2f567930ecf4f745.js', encoding='utf-8', errors='ignore').read()
idx = 0
while True:
    idx = content.find('98043', idx)
    if idx == -1:
        break
    print(f"Match 98043 at {idx}:")
    print(content[max(0, idx-100):min(len(content), idx+200)])
    print("-" * 50)
    idx += 5
