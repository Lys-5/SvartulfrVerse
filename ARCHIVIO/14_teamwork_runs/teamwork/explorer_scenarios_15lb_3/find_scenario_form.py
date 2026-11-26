import urllib.request
import concurrent.futures
import re

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\edit_page_chunks.txt', 'r', encoding='utf-8') as f:
    chunks = [line.strip() for line in f if line.strip()]

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def scan_for_scenario_form(chunk_path):
    url = 'https://app.wyvern.chat' + chunk_path
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            keywords = ['Edit Scenario', 'Create Scenario', 'Scenario Details', 'Select Lorebooks', 'Lorebooks', 'lorebook_ids']
            matches = [kw for kw in keywords if kw in text]
            if matches:
                return chunk_path, matches, text
            return chunk_path, [], None
    except Exception as e:
        return chunk_path, [], None

print("Scanning for Scenario Form...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    for chunk_path, matches, text in executor.map(scan_for_scenario_form, chunks):
        if matches:
            print(f"=== MATCH {matches} in {chunk_path} ===")
            for kw in matches:
                idx = text.find(kw)
                print(f"  [{kw}] snippet: {text[max(0, idx-100):min(len(text), idx+250)]}\n")
