import json

files = [
    'FINAL/Edric_Douglas_card.json',
    'FINAL/Logan_Douglas_card.json',
    'FINAL/Svartulfr_Location.json',
    'FINAL/Svartulfr_Lorebook_I.json',
    'FINAL/Svartulfr_Lorebook_II.json',
    'FINAL/Svartulfr_NPC_Primary.json',
    'FINAL/Svartulfr_NPC_Secondary.json'
]

for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\n==================== {fp} ====================")
    if isinstance(data, dict) and 'entries' in data:
        for idx, e in enumerate(data['entries']):
            txt = json.dumps(e, ensure_ascii=False)
            if 'Edric' in txt:
                lines = [l.strip() for l in e.get('content', '').split('\n') if 'Edric' in l or '12' in l or '13' in l or 'Presentation' in l or 'Presentazione' in l or 'Yule' in l]
                if lines:
                    print(f"  Entry {idx} ({e.get('comment')}):")
                    for l in lines:
                        if any(w in l for w in ['Edric', '12', '13', 'Presentation', 'Presentazione', 'Yule']):
                            print(f"    {l[:130]}")
    elif isinstance(data, dict):
        # Character card
        for k in ['description', 'personality', 'long_summary', 'scenario']:
            if k in data and data[k]:
                for l in str(data[k]).split('\n'):
                    if 'Edric' in l or '12' in l or '13' in l or 'Presentation' in l or 'Presentazione' in l or 'Yule' in l:
                        print(f"  [{k}] {l[:130]}")
