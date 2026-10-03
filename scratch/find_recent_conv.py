import json

with open('drive/claude_export/extracted/conversations/conversations.json', 'r', encoding='utf-8') as f:
    convs = json.load(f)

print(f'Total conversations: {len(convs)}')
sept_convs = []
for c in convs:
    created = c.get('created_at', '')
    updated = c.get('updated_at', '')
    if '2026-09' in created or '2026-09' in updated:
        sept_convs.append((updated, c.get('name', ''), len(c.get('chat_messages', [])), c))

sept_convs.sort(key=lambda x: x[0], reverse=True)
for u, n, m_count, c in sept_convs[:10]:
    print(f'{u} | {n} | msgs: {m_count}')

if sept_convs:
    latest = sept_convs[0][3]
    print("\n--- Latest messages in newest conversation ---")
    for m in latest.get('chat_messages', [])[-15:]:
        sender = m.get('sender')
        text = m.get('text', '')
        if text:
            print(f"[{sender}]: {text[:200]}...")
