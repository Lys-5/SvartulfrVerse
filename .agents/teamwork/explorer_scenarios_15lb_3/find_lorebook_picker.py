import urllib.request
import concurrent.futures
import re

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\edit_page_chunks.txt', 'r', encoding='utf-8') as f:
    chunks = [line.strip() for line in f if line.strip()]

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def search_scenario_lorebooks(chunk_path):
    url = 'https://app.wyvern.chat' + chunk_path
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            text = resp.read().decode('utf-8', errors='ignore')
            matches = []
            # Look for lorebook in scenario context
            if 'lorebook_ids' in text and ('scenario' in text or 'Scenario' in text):
                matches.append('lorebook_ids+scenario')
            if 'LorebookPicker' in text or 'LorebookSelect' in text or 'Attached Lorebooks' in text:
                matches.append('lorebook_picker')
            if 'lorebooks' in text and 'character-scenarios' in text:
                matches.append('lorebooks+character-scenarios')
            if matches:
                return chunk_path, matches, text
            return chunk_path, [], None
    except Exception as e:
        return chunk_path, [], None

print("Scanning for scenario lorebook component...")
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    for chunk_path, matches, text in executor.map(search_scenario_lorebooks, chunks):
        if matches:
            print(f"=== FOUND {matches} in {chunk_path} ===")
            for m in re.finditer(r'lorebook', text, re.IGNORECASE):
                pos = m.start()
                print(text[max(0, pos-150):min(len(text), pos+300)])
                print("-" * 40)
