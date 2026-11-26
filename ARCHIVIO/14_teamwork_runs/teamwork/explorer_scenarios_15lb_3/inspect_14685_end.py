with open(r'e:\repository\SvartulfrVerse\scratch\14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    t = f.read()

print("File size:", len(t))
# Look at the end of file for export
print("End of file:")
print(t[-1500:])
