import urllib.request
import concurrent.futures
import re

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\edit_page_chunks.txt', 'r', encoding='utf-8') as f:
    chunks = [line.strip() for line in f if line.strip()]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def check_chunk(chunk_path):
    url = 'https://app.wyvern.chat' + chunk_path
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            res = []
            if 'Offer a persona' in text:
                res.append(('Offer a persona', text))
            if '41680' in text and ('41680:' in text or '"41680":' in text or '41680,' in text):
                res.append(('41680', text))
            if 'Select Lorebooks' in text or 'attached_lorebooks' in text or 'lorebook_ids' in text:
                res.append(('lorebook', text))
            return chunk_path, res
    except Exception as e:
        return chunk_path, []

print(f"Scanning {len(chunks)} chunks concurrently...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(check_chunk, chunks)
    for chunk_path, matches in results:
        for tag, text in matches:
            print(f"\n=============================")
            print(f"MATCH [{tag}] in {chunk_path}")
            if tag == 'Offer a persona':
                idx = text.find('Offer a persona')
                print(text[max(0, idx-300):min(len(text), idx+600)])
            elif tag == '41680':
                for m in re.finditer(r'[\'"]?41680[\'"]?\s*:', text):
                    idx = m.start()
                    print(text[max(0, idx-100):min(len(text), idx+600)])
            elif tag == 'lorebook':
                for kw in ['Select Lorebooks', 'lorebook_ids']:
                    if kw in text:
                        idx = text.find(kw)
                        print(f"--- KW: {kw} ---")
                        print(text[max(0, idx-150):min(len(text), idx+350)])
