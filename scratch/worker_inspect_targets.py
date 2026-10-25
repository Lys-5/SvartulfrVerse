import json

def inspect_lorebook(path, target_ids):
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"=== {path} ===")
    print(f"Top-level keys: {list(d.keys())}")
    print(f"Token budget: {d.get('token_budget')}")
    print(f"photoURL: {d.get('photoURL')}")
    print(f"Entries count: entries={len(d.get('entries', []))} lexicon={len(d.get('lexicon', []))}")
    for entry in d.get('lexicon', []):
        if entry.get('id') in target_ids:
            print(f"Target found: id={entry.get('id')} name={entry.get('name')} type={entry.get('type')} ignored_characters={entry.get('ignored_characters')} keys={entry.get('keys')} avatar={entry.get('avatar')} content_len={len(entry.get('content', ''))}")

inspect_lorebook('FINAL/Svartulfr_NPC_Primary.json', {
    'C-JisFj8qA1tsFEqZKevk', # Erik
    'jDuJtzirlEZC3K_ArIufh', # Malachia
    'H2JX-NkHRiJ2FzoekC5ZZ', # Noah
    'tAcrWLtWSDGf3xJJRwUOM', # Logan
    'HhuMluMmIIENUei3bX6ed', # Wulfnic
    'BXi3sENAVYB8OKF80Q9Su', # Mackenzie
})

inspect_lorebook('FINAL/Svartulfr_NPC_Secondary.json', {
    'h-ttmlgJYeRXqyDvQjSX7', # Edric
    'NQd7n3QacMcK-TzowQ2LE', # Bruce
    'oov5UWuVhZ3RGgoxMkaTS', # Campus Staff Rat
    'Og7V6v67guXXAaP0_PsTM', # Adrian
})
