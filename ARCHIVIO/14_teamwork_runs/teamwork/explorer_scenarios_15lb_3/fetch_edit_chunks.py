import urllib.request
import re

token_file = r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt'
with open(token_file, 'r', encoding='utf-8') as f:
    token = f.read().strip()

url = 'https://app.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4/edit'
headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8')
        print(f"Status: {resp.status}, HTML length: {len(html)}")
        chunks = re.findall(r'/_next/static/chunks/[a-zA-Z0-9_\-\.]+\.js', html)
        print("Found chunks in page:", len(chunks))
        with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\edit_page_chunks.txt', 'w', encoding='utf-8') as out:
            for c in sorted(set(chunks)):
                out.write(c + '\n')
        print("Saved chunk list to edit_page_chunks.txt")
except Exception as e:
    print("Error fetching edit page:", e)
