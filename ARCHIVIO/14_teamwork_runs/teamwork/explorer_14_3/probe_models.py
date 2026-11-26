import json
import httpx

with open("proxy/config_free_proxy.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

client = httpx.Client(timeout=10.0)

# Check Groq models
groq_key = cfg.get("keys", {}).get("groq")
if groq_key:
    try:
        r = client.get("https://api.groq.com/openai/v1/models", headers={"Authorization": f"Bearer {groq_key}"})
        if r.status_code == 200:
            models = [m["id"] for m in r.json().get("data", [])]
            print("Groq valid models:", models)
        else:
            print("Groq error:", r.status_code, r.text[:100])
    except Exception as e:
        print("Groq exc:", e)

# Check SambaNova models
samba_key = cfg.get("keys", {}).get("sambanova")
if samba_key:
    try:
        r = client.get("https://api.sambanova.ai/v1/models", headers={"Authorization": f"Bearer {samba_key}"})
        if r.status_code == 200:
            models = [m["id"] for m in r.json().get("data", [])]
            print("SambaNova valid models:", models)
        else:
            print("SambaNova error:", r.status_code, r.text[:100])
    except Exception as e:
        print("SambaNova exc:", e)

# Check NVIDIA models
nv_key = cfg.get("keys", {}).get("nvidia")
if nv_key:
    try:
        r = client.get("https://integrate.api.nvidia.com/v1/models", headers={"Authorization": f"Bearer {nv_key}"})
        if r.status_code == 200:
            models = [m["id"] for m in r.json().get("data", []) if "llama" in m["id"].lower() or "nemotron" in m["id"].lower()]
            print("NVIDIA relevant models:", models[:10])
        else:
            print("NVIDIA error:", r.status_code, r.text[:100])
    except Exception as e:
        print("NVIDIA exc:", e)
