import urllib.request
import json

# Read api key from navy_glm_config_dump.json or query
# Let's see if https://api.navy/v1/models requires an API key or is public
req = urllib.request.Request("https://api.navy/v1/models")
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Public access allowed! Total models:", len(data.get('data', [])))
        # Check first model structure
        print("First model keys:", list(data['data'][0].keys()))
        with open("navy_all_models.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
except Exception as e:
    print("Public access error:", e)
