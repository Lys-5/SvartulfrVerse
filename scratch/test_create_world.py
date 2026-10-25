import json
import urllib.request

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

payload = {
    "name": "Svartúlfr — Blackwood & Solarton",
    "description": "Svartúlfr | Urban is set in modern-day supernatural California, where an ancient werewolf dynasty, chaotic campus life, and high-stakes dungeon incursions collide. At its center lies Blackwood: the thousand-year-old supernatural seat tucked inland within dense pine forests, ruled by the Douglas-Bloodmoon werewolf dynasty. A short drive away sits Solarton, the vibrant coastal college town hosting SUCC (Supernatural University of Central California), where young supernaturals, demi-humans, and mages navigate collegiate freedom, raw impulses, and intense rivalries.",
    "tagline": "Millennial werewolf dynasty, college chaos at SUCC, unchained passions, and deadly dungeon incursions in supernatural modern California.",
    "visibility": "private",
    "rating": "explicit",
    "tags": [
        "Third",
        "AnyPOV",
        "multiple-characters",
        "Original",
        "Fantasy",
        "Modern",
        "Supernatural",
        "Action",
        "Adventure",
        "Romance",
        "Italian",
        "English",
        "Werewolf",
        "Demihuman",
        "Alpha",
        "narrator"
    ],
    "scan_depth": 10,
    "avatar_activation_prefix": "",
    "avatar_activation_suffix": ""
}

req = urllib.request.Request(
    'https://app.wyvern.chat/api/worlds',
    data=json.dumps(payload).encode('utf-8'),
    headers=headers,
    method='POST'
)

try:
    with urllib.request.urlopen(req) as resp:
        print("Status:", resp.status)
        data = json.loads(resp.read().decode('utf-8'))
        print("Created world data keys:", list(data.keys()))
        print("World ID:", data.get('id') or data.get('_id'))
        print(json.dumps(data, indent=2))
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print("Error:", e)
