import os

batch7_files = [
    'Gabriel', 'Everett_Rottmore', 'Eric_Grey', 'Emlyn_Danes', 'Emil',
    'Damien_Bishop', 'Dallas_Rhodes', 'Cyrus_Camden', 'Charles_DeVille',
    'Caim_Morningstar', 'August_Reed', 'Arturo_Cardona', 'Arran_Parker',
    'Aris_Thorne', 'Amelia_DeVille', 'Alad_C', 'Aiden_Anderson'
]

for name in batch7_files:
    fname = f"scratch/batch7_{name}.txt"
    if not os.path.exists(fname):
        print(f"MISSING: {fname}")
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    print("="*60)
    lines = content.split('\n')
    print(lines[0]) # NAME
    print(lines[1]) # FIRST_NAME
    print(lines[2]) # KEYS
    # print summary header or first 3 lines
    print("--- SUMMARY ---")
    for l in lines[3:8]:
        if l.strip():
            print(" ", l[:100])
    # find [NAME: ...] header in LONG SUMMARY
    for l in lines:
        if l.strip().startswith('[NAME:'):
            print("--- LONG SUMMARY HEADER ---")
            print(" ", l[:120])
            break
