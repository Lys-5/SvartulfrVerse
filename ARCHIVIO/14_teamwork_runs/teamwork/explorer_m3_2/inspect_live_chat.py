import json
import sys
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
chat_path = ROOT / 'scratch' / 'live_chat_log.json'

if chat_path.exists():
    with open(chat_path, encoding='utf-8') as f:
        chat = json.load(f)
    print("Chat title:", chat.get('title'))
    print("Chat ID:", chat.get('id') or chat.get('_id'))
    print("Scenario ID:", chat.get('scenario_id'))
    print("Assistant ID:", chat.get('narrator_profile_id') or chat.get('assistant_id'))
    print("Messages count:", len(chat.get('messages', [])))
    
    # Check settings/overrides
    settings = chat.get('settings', {})
    print("Chat settings keys:", list(settings.keys()))
    
    for i, m in enumerate(chat.get('messages', [])):
        c = m.get('content', '')
        for l in c.splitlines():
            if any(k in l.lower() for k in ['15 marzo', 'march 15', '15th of march', '15-03', '15/03']):
                print(f"Message {i} ({m.get('sender_name')}): {l}")
