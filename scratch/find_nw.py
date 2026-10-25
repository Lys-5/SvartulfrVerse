content = open('e:/repository/SvartulfrVerse/scratch/36457-688d656b1534b9f0.js', encoding='utf-8').read()

# Let's find module 59892 or N.W
idx = content.find("N=s(")
print("N=s(...) match:", content[idx:idx+50])

# Let's look around line 69700 to 71000
print("\n=== LINES 69500 to 71000 ===")
print(content[69500:71500])
