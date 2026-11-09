import json
import urllib.request
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

def check_live():
    print("Testing http://127.0.0.1:5005/health ...")
    req = urllib.request.Request("http://127.0.0.1:5005/health")
    with urllib.request.urlopen(req, timeout=5) as res:
        health_data = json.loads(res.read().decode("utf-8"))
        print(f"Health Response (HTTP {res.status}):", health_data)
        assert health_data.get("status") == "ok"

    print("\nTesting http://127.0.0.1:5005/v1/models ...")
    req = urllib.request.Request("http://127.0.0.1:5005/v1/models")
    with urllib.request.urlopen(req, timeout=5) as res:
        models_data = json.loads(res.read().decode("utf-8"))
        print(f"Models Response (HTTP {res.status}):", models_data)
        assert models_data.get("object") == "list"

    print("\nTesting POST http://127.0.0.1:5005/v1/chat/completions ...")
    payload = {
        "model": "free-tier-master",
        "messages": [{"role": "user", "content": "Respond with the word PASS"}],
        "temperature": 0.5,
        "max_tokens": 100,
    }
    req = urllib.request.Request(
        "http://127.0.0.1:5005/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        comp_data = json.loads(res.read().decode("utf-8"))
        served_by = res.headers.get("X-Served-By")
        print(f"Completions Response (HTTP {res.status}):")
        print(f"  Served By: {served_by}")
        print(f"  Content: {comp_data['choices'][0]['message']['content']}")
        assert len(comp_data["choices"][0]["message"]["content"]) > 0

    print("\n✅ Live Proxy is fully functional and serving requests!")

if __name__ == "__main__":
    check_live()
