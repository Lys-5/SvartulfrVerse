content = open('scratch/19010-2f567930ecf4f745.js', encoding='utf-8', errors='ignore').read()
start = 290812
end = content.find('}},', start)
print(f"Module 98043 length: {end - start}")
print(content[start:min(end + 10, start + 8000)])
