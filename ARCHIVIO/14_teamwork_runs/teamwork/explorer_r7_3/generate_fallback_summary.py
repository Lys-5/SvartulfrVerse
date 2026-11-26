import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    prim = json.load(f)
with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    sec = json.load(f)

ph_url = 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public'

prim_fallback_entries = [
    {
        'index': i,
        'entry_id': e.get('entry_id'),
        'name': e.get('name'),
        'keys': e.get('keys')
    }
    for i, e in enumerate(prim.get('entries', []))
    if e.get('avatar') == ph_url
]

sec_fallback_entries = [
    {
        'index': i,
        'entry_id': e.get('entry_id'),
        'name': e.get('name'),
        'keys': e.get('keys')
    }
    for i, e in enumerate(sec.get('entries', []))
    if e.get('avatar') == ph_url
]

summary = {
    'primary_fallback_count': len(prim_fallback_entries),
    'secondary_fallback_count': len(sec_fallback_entries),
    'total_fallback_count': len(prim_fallback_entries) + len(sec_fallback_entries),
    'primary_fallback_entries': prim_fallback_entries,
    'secondary_fallback_entries': sec_fallback_entries
}

with open('.agents/teamwork/explorer_r7_3/fallback_entries_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)

print(f"Generated summary: {len(prim_fallback_entries)} Primary + {len(sec_fallback_entries)} Secondary fallback entries.")
