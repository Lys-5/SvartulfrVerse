import sys
sys.stdout.reconfigure(encoding='utf-8')

for fname in ['parsed_io_succ_char.html.txt', 'parsed_io_succc.html.txt']:
    print(f"\n==================== {fname} ====================")
    with open(f'scratch/sites_raw/{fname}', 'r', encoding='utf-8') as f:
        text = f.read()
    
    sections = text.split('============================== SECTION: ')
    for s in sections[1:]:
        lines = s.strip().split('\n')
        sec_name = lines[0].replace(' ==============================', '').strip()
        print(f"--- {sec_name} ({len(lines)-1} lines) ---")
        for l in lines[1:8]:
            if l.strip():
                print(f"  {l[:100]}")
