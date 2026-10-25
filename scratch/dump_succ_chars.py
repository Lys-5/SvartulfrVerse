import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/sites_raw/parsed_io_succ_char.html.txt', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open('scratch/sites_raw/parsed_io_succc.html.txt', 'r', encoding='utf-8') as f:
    text2 = f.read()

def print_char_block(text, label):
    sections = text.split('============================== SECTION: ')
    for s in sections[1:]:
        lines = [l.strip() for l in s.split('\n') if l.strip()]
        if not lines:
            continue
        sec_name = lines[0].replace(' ==============================', '').strip()
        if sec_name in ['INTRO', 'students']:
            continue
        print(f"\n--- {label.upper()}: {sec_name.upper()} ---")
        for l in lines[1:]:
            print(f"  {l}")

print_char_block(text1, "SUCC CHAR 1")
print_char_block(text2, "SUCC CHAR 2")
