import urllib.request
import json

keys = {
    "google": "AQ.Ab8RN6JYsAe-Qrvhm1srfa4saQKD2OjU1zYAX3Q7SuPGRQDQRA",
    "openrouter": "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",
    "chutes": "cpk_d535cd6bccbb47b69643936a813557b3.2d163e81bd295ac0b053d60f8cf4a1ff.ggXvFBCFLdBBoGfvBlVaLhNT3QuoEfda",
    "groq": "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"
}

def test_completion(name, url, headers, body):
    print(f"\nTesting {name}...")
    try:
        req = urllib.request.Request(
            url,
            headers=headers,
            data=json.dumps(body).encode('utf-8')
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            content = data['choices'][0]['message']['content']
            print(f"SUCCESS {name} -> Response: {content.strip()[:100]}")
            return True
    except urllib.error.HTTPError as e:
        print(f"ERROR {name} -> Code: {e.code}, Body: {e.read().decode()[:200]}")
    except Exception as e:
        print(f"FAILED {name} -> {e}")
    return False

# 1. Test Google AI Studio via OpenAI endpoint
test_completion(
    "Google (gemini-2.5-pro)",
    "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
    {"Authorization": f"Bearer {keys['google']}", "Content-Type": "application/json"},
    {"model": "gemini-2.5-pro", "messages": [{"role": "user", "content": "Rispondi solo 'Gemini Pro OK'"}]}
)

# 2. Test Chutes (zai-org/GLM-5.2-TEE)
test_completion(
    "Chutes (GLM-5.2)",
    "https://llm.chutes.ai/v1/chat/completions",
    {"Authorization": f"Bearer {keys['chutes']}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
    {"model": "zai-org/GLM-5.2-TEE", "messages": [{"role": "user", "content": "Rispondi solo 'GLM 5.2 OK'"}]}
)

# 3. Test OpenRouter (deepseek/deepseek-r1:free)
test_completion(
    "OpenRouter (DeepSeek R1 free)",
    "https://openrouter.ai/api/v1/chat/completions",
    {"Authorization": f"Bearer {keys['openrouter']}", "Content-Type": "application/json", "HTTP-Referer": "https://app.wyvern.chat"},
    {"model": "deepseek/deepseek-r1:free", "messages": [{"role": "user", "content": "Rispondi solo 'DeepSeek R1 OK'"}]}
)

# 4. Test Chutes (Gemma 4)
test_completion(
    "Chutes (gemma-4-31B-turbo-TEE)",
    "https://llm.chutes.ai/v1/chat/completions",
    {"Authorization": f"Bearer {keys['chutes']}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
    {"model": "google/gemma-4-31B-turbo-TEE", "messages": [{"role": "user", "content": "Rispondi solo 'Gemma 4 OK'"}]}
)
