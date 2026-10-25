import json
import urllib.request
import os

token_file = r'e:\repository\SvartulfrVerse\scratch\wyvern_token.txt'
with open(token_file, 'r', encoding='utf-8') as f:
    token = f.read().strip()

lorebook_ids = [
    '_gwwCxCfQ6PQaLEjAQVpJL',
    '_HfG7TeV6MJyj6bxMwxkpt',
    '_9zWTGqYJNJ4BCDMj8gfcD',
    '_EjXxkmPVhpCXg8xABpFkK',
    '_Uht3Ckz44JBDrPnUHq7LV',
    '_zwEqgEEzh12X6gHVmMKKC',
    '_GV1KyHVY1RMbCnWgLkzDG',
    '_GbWJbkhgLzWexMHrjyUUc',
    '_FaVcHfmrqcaJq8pa3WmRw',
    '_BbrRgrcdGPMLEbBU2b6xk',
    '_gchmML4Q478zdFjhXf8rN',
    '_brNyzEdhzNAyxK8xC8hhm',
    '_YtKLMTwyMxNf1DNYqBx1t',
    '_b9HgpUXtAW8VmTy82BPDV',
    '_c8bEm1bWphwqFBXWRPrV8'
]

persona_ids = [
    'persona_1786335754946',
    '1792155173728'
]

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0'
}

print("=== CHECKING 15 LOREBOOKS ===")
lorebook_results = []
for lbid in lorebook_ids:
    url = f'https://app.wyvern.chat/api/lorebooks/{lbid}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            title = data.get('title') or data.get('name') or 'NO_TITLE'
            entry_count = len(data.get('entries', []))
            lex_count = len(data.get('lexicon', []))
            visibility = data.get('visibility')
            print(f"[{resp.status}] ID: {lbid} | Title: '{title}' | Entries: {entry_count} | Lexicon: {lex_count} | Vis: {visibility}")
            lorebook_results.append({
                'id': lbid,
                'status': resp.status,
                'title': title,
                'entries_count': entry_count,
                'lexicon_count': lex_count,
                'visibility': visibility
            })
    except Exception as e:
        print(f"[ERR] ID: {lbid} | Error: {e}")
        lorebook_results.append({
            'id': lbid,
            'status': 'ERROR',
            'error': str(e)
        })

print("\n=== CHECKING PERSONAS ===")
persona_results = []
for pid in persona_ids:
    url = f'https://app.wyvern.chat/api/user-personas/{pid}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            name = data.get('name') or data.get('title') or 'NO_NAME'
            avatar = data.get('avatar')
            lorebooks = data.get('lorebook_ids', [])
            print(f"[{resp.status}] ID: {pid} | Name: '{name}' | Avatar: {avatar} | Lorebooks: {lorebooks}")
            persona_results.append({
                'id': pid,
                'status': resp.status,
                'name': name,
                'avatar': avatar,
                'lorebook_ids': lorebooks,
                'data': data
            })
    except Exception as e:
        print(f"[ERR] ID: {pid} | Error: {e}")
        persona_results.append({
            'id': pid,
            'status': 'ERROR',
            'error': str(e)
        })

out_data = {
    'lorebooks': lorebook_results,
    'personas': persona_results
}
out_path = r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\verification_results.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out_data, f, indent=2)

print(f"\nSaved results to {out_path}")
