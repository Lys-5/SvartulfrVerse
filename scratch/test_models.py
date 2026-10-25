import urllib.request, json

google_key = 'AQ.Ab8RN6JYsAe-Qrvhm1srfa4saQKD2OjU1zYAX3Q7SuPGRQDQRA'
openrouter_key = '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'

# 1. Test Google models
for m in ['gemini-3.1-pro-preview', 'gemini-4-argon', 'gemini-3.8-flash']:
    try:
        req = urllib.request.Request(
            'https://generativelanguage.googleapis.com/v1beta/openai/chat/completions',
            headers={'Authorization': f'Bearer {google_key}', 'Content-Type': 'application/json'},
            data=json.dumps({'model': m, 'messages': [{'role': 'user', 'content': 'Rispondi OK'}]}).encode('utf-8')
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            res = json.loads(r.read().decode())
            print(f'Google {m} SUCCESS ->', res['choices'][0]['message']['content'].strip()[:60])
    except urllib.error.HTTPError as e:
        print(f'Google {m} FAIL -> {e.code}: {e.read().decode()[:150]}')
    except Exception as e:
        print(f'Google {m} FAIL ->', e)

# 2. Check OpenRouter models
try:
    req = urllib.request.Request('https://openrouter.ai/api/v1/models')
    with urllib.request.urlopen(req, timeout=10) as r:
        data = json.loads(r.read().decode())
        free_models = [m['id'] for m in data.get('data', []) if ':free' in m['id']]
        print('\nOpenRouter :free models count:', len(free_models))
        r1_free = [m for m in free_models if 'deepseek' in m or 'r1' in m]
        print('OpenRouter R1 / DeepSeek free models:', r1_free)
        glm_free = [m for m in free_models if 'glm' in m]
        print('OpenRouter GLM free models:', glm_free)
except Exception as e:
    print('OpenRouter check error:', e)
