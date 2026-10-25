import json

data = json.load(open('scratch/chat_log_snapshot.json', encoding='utf-8'))
for k, v in data.items():
    if k == 'messages':
        print(f"messages: {len(v)} items")
    elif isinstance(v, (dict, list)):
        dump = json.dumps(v)
        if len(dump) > 200:
            print(f"{k}: ({type(v).__name__}) {dump[:200]}...")
        else:
            print(f"{k}: ({type(v).__name__}) {dump}")
    else:
        print(f"{k}: {v}")
