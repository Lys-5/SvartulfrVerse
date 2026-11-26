import json
import urllib.request
from collections import Counter

TOKEN_PATH = r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt'
with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'ExplorerR73/1.0',
    'Accept': 'application/json'
}

for name, lb_id in [('Primary', '_zwEqgEEzh12X6gHVmMKKC'), ('Secondary', '_Uht3Ckz44JBDrPnUHq7LV')]:
    url = f"https://app.wyvern.chat/api/lorebooks/{lb_id}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    
    lex = data.get('lexicon', [])
    avatars = [e.get('avatar') for e in lex]
    counts = Counter(avatars)
    
    old_placeholder = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public"
    current_fallback = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public"
    dcc_target = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public"
    
    print(f"=== LIVE WYVERN API: {name} ({lb_id}) ===")
    print(f"Total lexicon entries: {len(lex)}")
    print(f"Entries with 6f8b7c78 fallback: {sum(1 for a in avatars if a == current_fallback)}")
    print(f"Entries with 98e2d06d fallback: {sum(1 for a in avatars if a == old_placeholder)}")
    print(f"Entries with 99d10d9b DCC target: {sum(1 for a in avatars if a == dcc_target)}")
    print(f"Entries with null/empty avatar: {sum(1 for a in avatars if not a)}")
    print(f"Top avatars:")
    for url, count in counts.most_common(5):
        print(f"  [{count}] {url}")
    print()
