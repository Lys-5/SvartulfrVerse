import os
import sys
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

html_path = r'C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\.system_generated\steps\2830\content.md'
with open(html_path, 'r', encoding='utf-8') as f:
    raw = f.read()

soup = BeautifulSoup(raw, 'html.parser')

# Let's inspect sections and article/containers
print("=== SECTIONS SUMMARY ===")
sections = soup.find_all('section')
for s in sections:
    sec_id = s.get('id', 'no-id')
    sec_text = s.get_text(separator=' | ', strip=True)
    print(f"\n--- SECTION: {sec_id} (chars: {len(sec_text)}) ---")
    print(sec_text[:300] + ("..." if len(sec_text) > 300 else ""))

# Find all cards, character containers, tabs
# Carrd.co usually puts elements in #home, #characters, #setting, #about, etc.
