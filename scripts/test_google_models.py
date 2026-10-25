import urllib.request
import json

models_to_test = [
    'gemini-2.5-flash',
    'gemini-flash-latest',
    'gemini-3.1-flash-lite-preview',
    'gemini-3.1-pro-preview',
    'gemini-pro-latest',
    'gemma-4-31b-it',
    'gemma-4-26b-a4b-it'
]

key = 'AQ.Ab8RN6Iu11nOz2VIpPOrmCdwpeE5_AH23BTlqQnzlOCfShbh7w'

for m in models_to_test:
    req = urllib.request.Request(
        'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions',
        headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
        data=json.dumps({'model': m, 'messages': [{'role': 'user', 'content': 'Test'}], 'max_tokens': 5}).encode('utf-8')
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            ans = data['choices'][0]['message']['content'].strip()
            print(f"SUCCESS {m}: {ans}")
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8')[:120]
        print(f"FAILED {m}: HTTP {e.code} -> {err}")
