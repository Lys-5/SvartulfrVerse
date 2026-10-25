import urllib.request
import json

keys = {
    "google": "AQ.Ab8RN6JYsAe-Qrvhm1srfa4saQKD2OjU1zYAX3Q7SuPGRQDQRA",
    "groq": "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",
    "openrouter_1": "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",
    "openrouter_2": "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"
}

# 1. Test Google AI Studio
print("--- TEST 1: Google AI Studio ---")
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={keys['google']}"
try:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        models = [m['name'].replace('models/', '') for m in data.get('models', [])]
        print("Google AI Studio OK! Available models count:", len(models))
        # Filter for relevant models
        relevant = [m for m in models if any(k in m for k in ['gemini-2.5', 'gemini-1.5-pro', 'gemini-2.0-flash', 'gemini-exp', 'gemma'])]
        print("Sample models:", relevant[:10])
except Exception as e:
    print("Google AI Studio Error:", e)

# 2. Test Groq
print("\n--- TEST 2: Groq ---")
url = "https://api.groq.com/openai/v1/models"
try:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {keys['groq']}"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        groq_models = [m['id'] for m in data.get('data', [])]
        print("Groq OK! Available models count:", len(groq_models))
        r1_models = [m for m in groq_models if 'deepseek' in m or 'r1' in m]
        print("Groq DeepSeek / R1 models:", r1_models)
except Exception as e:
    print("Groq Error:", e)

# 3. Test OpenRouter 1
print("\n--- TEST 3: OpenRouter Key 1 ---")
url = "https://openrouter.ai/api/v1/auth/key"
try:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {keys['openrouter_1']}"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        print("OpenRouter Key 1 OK:", data)
except Exception as e:
    print("OpenRouter Key 1 Error:", e)

# 4. Test OpenRouter 2
print("\n--- TEST 4: OpenRouter Key 2 ---")
try:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {keys['openrouter_2']}"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        print("OpenRouter Key 2 OK:", data)
except Exception as e:
    print("OpenRouter Key 2 Error:", e)
