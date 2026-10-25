import urllib.request
import json
import re

# 1. Read PROMPT_OVERRIDES_WYVERN.md to extract system_prompt and final_instructions
with open('FINAL/PROMPT_OVERRIDES_WYVERN.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract Section 1: System Prompt
sp_match = re.search(r'## 1\. System Prompt Override\s*```xml\s*(.*?)\s*```', text, re.DOTALL)
if not sp_match:
    raise ValueError("Could not extract System Prompt Override")
system_prompt = sp_match.group(1).strip()

# Extract Section 2: Final Instructions
fi_match = re.search(r'## 2\. Final Instructions Override \(`post_history_instructions`\)\s*```xml\s*(.*?)\s*```', text, re.DOTALL)
if not fi_match:
    raise ValueError("Could not extract Final Instructions Override")
final_instructions = fi_match.group(1).strip()

print(f"Extracted system_prompt: {len(system_prompt)} chars")
print(f"Extracted final_instructions: {len(final_instructions)} chars")

# 2. Load live scenario data from Wyvern API
token = open('scratch/wyvern_token.txt', encoding='utf-8').read().strip()
url = 'https://app.wyvern.chat/api/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4'
req = urllib.request.Request(
    url,
    headers={
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
)

with urllib.request.urlopen(req, timeout=15) as resp:
    live_sc = json.loads(resp.read().decode('utf-8'))

current_rev = live_sc.get('revision', 26)
print(f"Live scenario revision: {current_rev}")

# 3. Update live_sc payload with latest prompts
live_sc['system_prompt'] = system_prompt
live_sc['final_instructions'] = final_instructions
live_sc['revision'] = current_rev

# Ensure lorebook_ids has all our 6 standalone lorebooks + technical lorebooks
expected_lbs = [
    '_gwwCxCfQ6PQaLEjAQVpJL', # Lorebook I
    '_HfG7TeV6MJyj6bxMwxkpt', # Lorebook II
    '_9zWTGqYJNJ4BCDMj8gfcD', # Lorebook III
    '_EjXxkmPVhpCXg8xABpFkK', # Location
    '_zwEqgEEzh12X6gHVmMKKC', # NPC Primary
    '_Uht3Ckz44JBDrPnUHq7LV'  # NPC Secondary
]
for lb in expected_lbs:
    if lb not in live_sc['lorebook_ids']:
        live_sc['lorebook_ids'].append(lb)

# Save to FINAL/Svartulfr_Master_Scenario.json
with open('FINAL/Svartulfr_Master_Scenario.json', 'w', encoding='utf-8') as f:
    json.dump(live_sc, f, indent=2, ensure_ascii=False)

print("Saved updated scenario to FINAL/Svartulfr_Master_Scenario.json")

# 4. Deploy via PUT
req_put = urllib.request.Request(
    url,
    data=json.dumps(live_sc, ensure_ascii=False).encode('utf-8'),
    headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    },
    method='PUT'
)

with urllib.request.urlopen(req_put, timeout=20) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    print(f"Deploy success! Status: {resp.status}, New Revision: {res.get('revision')}")
    print(f"System prompt len: {len(res.get('system_prompt', ''))}")
    print(f"Final instructions len: {len(res.get('final_instructions', ''))}")
    print(f"Slots: {len(res.get('slots', []))}")
