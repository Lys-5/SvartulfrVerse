c = open("scratch/53944-e2a3f3ea28ad0416.js", encoding="utf-8").read()
idx = c.find("middle_names")
s = max(0, idx - 400)
e = min(len(c), idx + 2500)
with open("scratch/full_regex_generator.txt", "w", encoding="utf-8") as out:
    out.write(c[s:e])
print("Written UTF-8 full_regex_generator.txt")
