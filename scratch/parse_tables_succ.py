import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/sites_raw/io_succ.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("=== TABLES IN IO_SUCC ===")
for t in soup.find_all('table'):
    tid = t.get('id', 'no-id')
    print(f"\n--- TABLE ID: {tid} ---")
    rows = t.find_all('tr')
    for r in rows:
        cols = [c.get_text(strip=True) for c in r.find_all(['td', 'th'])]
        print(" | ".join(cols))
