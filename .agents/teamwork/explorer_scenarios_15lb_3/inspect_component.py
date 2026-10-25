with open(r'e:\repository\SvartulfrVerse\scratch\14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's inspect before pos 96935
pos = 96935
print("=== CONTEXT BEFORE POS 96935 ===")
print(content[pos-1500:pos+500])
