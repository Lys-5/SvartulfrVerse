import urllib.request
import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()

url = "https://app.wyvern.chat/api/worlds/_CgYT8fHXpDC4crjmegQF7"
req = urllib.request.Request(url, headers={
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
})

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print("Name:", data.get('name'))
    print("ID:", data.get('id'))
    print("Visibility:", data.get('visibility'))
    print("World Age:", data.get('world_age'))
    print("Human Start Date:", data.get('human_start_date'))
    print("Calendar:", json.dumps(data.get('calendar'), indent=2))
    print("World Features:", json.dumps(data.get('world_features'), indent=2))
    print("Stat Config:", json.dumps(data.get('stat_config'), indent=2))
    print("System Prompt Override length:", len(data.get('system_prompt_override') or ""))
    print("Base Instructions length:", len(data.get('base_instructions') or ""))
    print("Final Instructions length:", len(data.get('final_instructions') or ""))
    print("Environments count:", data.get('environments_count'))
    print("Locations count:", data.get('locations_count'))
    print("Lexicon count:", data.get('lexicon_count'))
