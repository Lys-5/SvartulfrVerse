import json
import httpx
import sys

with open("proxy/config_free_proxy.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

keys = cfg.get("keys", {})

print("=" * 60)
print("LIVE PROBE OF CONFIGURED KEYS IN proxy/config_free_proxy.json")
print("=" * 60)

client = httpx.Client(timeout=10.0)

# 1. Google AI Studio
google_key = keys.get("google_ai_studio")
if google_key:
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
        headers = {"Authorization": f"Bearer {google_key}", "Content-Type": "application/json"}
        payload = {"model": "gemini-3.1-flash-lite", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[Google AI Studio] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[Google AI Studio] Error: {e}")

# 2. OpenRouter
or_keys = keys.get("openrouter", [])
if isinstance(or_keys, str):
    or_keys = [or_keys]
for idx, ok in enumerate(or_keys):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {ok}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://app.wyvern.chat",
            "X-Title": "WyvernChat"
        }
        payload = {"model": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[OpenRouter Key #{idx+1} ({ok[-6:]})] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[OpenRouter Key #{idx+1}] Error: {e}")

# 3. Groq
groq_key = keys.get("groq")
if groq_key:
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {groq_key}", "Content-Type": "application/json"}
        payload = {"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[Groq] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[Groq] Error: {e}")

# 4. Chutes
chutes_key = keys.get("chutes")
if chutes_key:
    try:
        url = "https://llm.chutes.ai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {chutes_key}", "Content-Type": "application/json"}
        payload = {"model": "zai-org/GLM-5.1-TEE", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[Chutes] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[Chutes] Error: {e}")

# 5. SambaNova
samba_key = keys.get("sambanova")
if samba_key:
    try:
        url = "https://api.sambanova.ai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {samba_key}", "Content-Type": "application/json"}
        payload = {"model": "Meta-Llama-3.3-70B-Instruct", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[SambaNova] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[SambaNova] Error: {e}")

# 6. NVIDIA
nvidia_key = keys.get("nvidia")
if nvidia_key:
    try:
        url = "https://integrate.api.nvidia.com/v1/chat/completions"
        headers = {"Authorization": f"Bearer {nvidia_key}", "Content-Type": "application/json"}
        payload = {"model": "meta/llama-3.3-70b-instruct", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[NVIDIA NIM] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[NVIDIA NIM] Error: {e}")

# 7. Cloudflare
cf_key = keys.get("cloudflare")
if cf_key:
    try:
        url = "https://api.cloudflare.com/client/v4/accounts/a02ddeb54d2a0bb4f402088713a6d8ac/ai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {cf_key}", "Content-Type": "application/json"}
        payload = {"model": "@cf/meta/llama-3.1-8b-instruct", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[Cloudflare Workers AI] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[Cloudflare Workers AI] Error: {e}")

# 8. GitHub
github_key = keys.get("github")
if github_key:
    try:
        url = "https://models.inference.ai.azure.com/chat/completions"
        headers = {"Authorization": f"Bearer {github_key}", "Content-Type": "application/json"}
        payload = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[GitHub Models] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[GitHub Models] Error: {e}")

# 9. HuggingFace
hf_key = keys.get("huggingface")
if hf_key:
    try:
        url = "https://api-inference.huggingface.co/v1/chat/completions"
        headers = {"Authorization": f"Bearer {hf_key}", "Content-Type": "application/json"}
        payload = {"model": "meta-llama/Llama-3.2-3B-Instruct", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[HuggingFace] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[HuggingFace] Error: {e}")

# 10. DeepInfra
di_key = keys.get("deepinfra")
if di_key:
    try:
        url = "https://api.deepinfra.com/v1/openai/chat/completions"
        headers = {"Authorization": f"Bearer {di_key}", "Content-Type": "application/json"}
        payload = {"model": "meta-llama/Llama-3.3-70B-Instruct", "messages": [{"role": "user", "content": "ping"}], "max_tokens": 5}
        r = client.post(url, headers=headers, json=payload)
        print(f"[DeepInfra] HTTP {r.status_code}: {'OK' if r.status_code == 200 else r.text[:120]}")
    except Exception as e:
        print(f"[DeepInfra] Error: {e}")

print("=" * 60)
