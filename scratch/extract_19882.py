with open('scratch/14685-a6f37bf36e7cf713.js', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# Module 19882 is between 37057 and 47485
mod19882 = c[37057:47485]
with open('scratch/module_19882.js', 'w', encoding='utf-8') as f_out:
    f_out.write(mod19882)
print("Saved module 19882, length:", len(mod19882))
