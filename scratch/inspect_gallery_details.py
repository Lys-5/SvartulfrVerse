import json

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    s = json.load(f)

print('Secondary gallery len:', len(s.get('gallery', [])))
print('Secondary gallery_count:', s.get('gallery_count'))
if s.get('gallery'):
    print('Sample gallery item:', s['gallery'][0])

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    p = json.load(f)

print('Primary top keys:', list(p.keys()))
