import urllib.request
import concurrent.futures
import re

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\edit_page_chunks.txt', 'r', encoding='utf-8') as f:
    chunks = [line.strip() for line in f if line.strip()]

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def scan_for_lorebook_field(chunk_path):
    url = 'https://app.wyvern.chat' + chunk_path
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            if 'lorebook_ids' in text:
                return chunk_path, text
            return chunk_path, None
    except Exception as e:
        return chunk_path, None

print("Scanning for lorebook_ids in all edit chunks...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    for chunk_path, text in executor.map(scan_for_lorebook_field, chunks):
        if text:
            print(f"=== FOUND lorebook_ids in {chunk_path} ===")
            for m in re.finditer(r'lorebook_ids', text):
                pos = m.start()
                print(text[max(0, pos-150):min(len(text), pos+300)])
                print("-" * 50)
