with open(r'e:\repository\SvartulfrVerse\scratch\14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    t = f.read()

pos = t.find('function e6(e){')
if pos != -1:
    print("=== FUNCTION e6 ===")
    print(t[pos:pos+1500])
else:
    print("Not found")
