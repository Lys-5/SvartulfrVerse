import json
import urllib.request

with open('scratch/wyvern_token.txt', 'r', encoding='utf-8') as f:
    token = f.read().strip()

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

# 1. Create a temporary world
create_payload = {
    "name": "Test Lex World",
    "description": "Test Lex World Description",
    "visibility": "private",
    "rating": "none",
    "tags": ["test"]
}
req = urllib.request.Request('https://app.wyvern.chat/api/worlds', data=json.dumps(create_payload).encode('utf-8'), headers=headers, method='POST')
with urllib.request.urlopen(req) as resp:
    wdata = json.loads(resp.read().decode('utf-8'))
    wid = wdata.get('id') or wdata.get('_id')
    print("Created test world:", wid)

try:
    # 2. Test bulk lexicon creation
    bulk_payload = {
        "world_id": wid,
        "entries": [
            {
                "name": "Douglas Commercial Coalition (DCC)",
                "type": "organization/faction",
                "content": "La Douglas Commercial Coalition (DCC) e il braccio economico, commerciale e geopolitico primario della dinastia Douglas.",
                "keys": ["DCC", "Douglas Commercial Coalition"],
                "key_logic": "AND_ANY",
                "secondary_keys": ["commercio", "societa", "corporation"],
                "selective": True,
                "is_global": False,
                "scan_persona": True,
                "whole_words_only": True,
                "enableEntryHighlighting": True,
                "highlight_keys": True,
                "ignored_characters": ["_t4J9aQNJM36cUKAP4wB4U"],
                "ignored_personas": [],
                "enabled": True,
                "position": "after_char",
                "insertion_order": 10
            },
            {
                "name": "Ecologia Sociale Licantropica (LSE)",
                "type": "lore/concept",
                "content": "La Lupine Social Ecology (LSE) definisce la biologia, i feromoni, la struttura di branco e le risonanze psichiche dei lupi mannari.",
                "keys": ["LSE", "Lupine Social Ecology"],
                "key_logic": "AND_ANY",
                "secondary_keys": ["biologia", "feromoni", "branco"],
                "selective": True,
                "is_global": True,
                "scan_persona": True,
                "whole_words_only": True,
                "enableEntryHighlighting": True,
                "highlight_keys": True,
                "ignored_characters": [],
                "ignored_personas": [],
                "enabled": True,
                "position": "after_char",
                "insertion_order": 10
            }
        ]
    }
    req_bulk = urllib.request.Request('https://app.wyvern.chat/api/worlds/lexicon/bulk', data=json.dumps(bulk_payload).encode('utf-8'), headers=headers, method='POST')
    with urllib.request.urlopen(req_bulk) as resp:
        print("Bulk Lexicon Status:", resp.status)
        lex_data = json.loads(resp.read().decode('utf-8'))
        print("Bulk returned entries count:", len(lex_data))
        if lex_data:
            print("First entry sample:")
            print(json.dumps(lex_data[0], indent=2))

    # 3. Read back via GET /api/worlds/lexicon/world/{id}
    req_get = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/lexicon/world/{wid}', headers=headers)
    with urllib.request.urlopen(req_get) as resp:
        get_data = json.loads(resp.read().decode('utf-8'))
        print("GET Lexicon returned count:", len(get_data))

finally:
    # 4. Cleanup test world
    req_del = urllib.request.Request(f'https://app.wyvern.chat/api/worlds/{wid}', headers=headers, method='DELETE')
    with urllib.request.urlopen(req_del) as resp:
        print("Cleaned up test world, status:", resp.status)
